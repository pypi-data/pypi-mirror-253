"""Implementation of the Kedro Expectations Hooks."""
from collections import defaultdict

import great_expectations as ge
import os
from typing import Any, Dict, cast, Callable

from great_expectations.core import (
    RunIdentifier,
    ExpectationSuiteValidationResult,
    ExpectationValidationResult,
)
from great_expectations.data_context.types.resource_identifiers import (
    ValidationResultIdentifier,
    ExpectationSuiteIdentifier,
)
from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog
from kedro_datasets.partitions.partitioned_dataset import PartitionedDataset

from .notification import BaseNotifier
from .exceptions import SuiteValidationFailure
from pandas import DataFrame as PandasDataFrame
from .utils import (
    dot_to_underscore,
    validate,
    get_suite_name,
    get_all_expectations,
    base_ge_folder_exists,
    location_is_kedro_root_folder,
)


RUN_NAME = "kedro_expectations_auto_validation"


class KedroExpectationsHooks:
    """Implementation of the Kedro Expectations Hooks."""

    def __init__(
        self,
        on_failure: str = "continue",
        check_orphan_expectation_suites: bool = True,
        single_datasource_check: bool = True,
        notify_config: BaseNotifier = None,
    ) -> None:
        """

        :param on_failure: Defines what to do when a validation fails. Valid strings are "continue" (failures are \
            visible in the data docs), "raise_fast" (directly raise a SuiteValidationFailure) and "raise_later" (raise \
            a SuiteValidationFailure at the end of the pipeline run, containing information on all failures).
        :param check_orphan_expectation_suites: Boolean to sanity check, if all expectation suites have a \
            corresponding data source.
        :param single_datasource_check: Boolean if each datasource should only be checked once per run (in cases the \
            datasource is used as nodes' input multiple times)
        :param notify_config: Configuration for sending a summarizing notification message about the run, e.g. via email
        """
        assert on_failure in ["continue", "raise_fast", "raise_later"], (
            f"Argument 'on_failure' has to be one of "
            f"'continue', 'raise_fast' or 'raise_later', "
            f"but was {on_failure}."
        )
        self._on_failure = on_failure
        self._check_orphan_expectation_suites = check_orphan_expectation_suites
        self._single_datasource_check = single_datasource_check
        self._datasource_run_counter = defaultdict(lambda: 0)
        self._fail_log = []
        self.checkpoint_results = []
        self.run_id = None
        self._notifier = notify_config

    # @hook_impl
    # def after_context_created(self, context: KedroContext):

    @hook_impl
    def after_catalog_created(
        self,
        catalog: DataCatalog,
        conf_catalog,
        conf_creds,
        feed_dict,
        save_version,
        load_versions,
    ) -> None:
        # Store the session id of the run for the validation result timestamp
        self.run_id = RunIdentifier(run_name=save_version, run_time=None)
        # Make sure each expectation suite has a corresponding dataset.
        if self._check_orphan_expectation_suites:
            gx = ge.get_context()
            exp_datasets = set(
                entry.expectation_suite_name.split(".")[0]
                for entry in gx.list_expectation_suites()
            )
            catalog_datasets = set(
                entry
                for entry in catalog.list()
                if not entry.startswith("params:") and entry != "parameters"
            )
            orphan_expectation_suites = exp_datasets - catalog_datasets
            if len(orphan_expectation_suites) > 0:
                msg = (
                    f"Found orphan expectation suites not corresponding to any dataset in the catalog: "
                    f"{orphan_expectation_suites}."
                )
                self.publish_failure_msg(msg)

    @hook_impl
    def before_node_run(self, catalog: DataCatalog, inputs: Dict[str, Any]) -> None:
        """Validate inputs that are supported and have an expectation suite available."""
        if (
            self.before_node_run
            and base_ge_folder_exists(verbose=False)
            and location_is_kedro_root_folder()
        ):
            self._run_validation(catalog, inputs)

    @hook_impl
    def after_pipeline_run(
        self, run_params: Dict, run_result, pipeline, catalog: DataCatalog
    ):
        ge_context = ge.get_context()

        # summarize the successful and failed validations for email report
        failed_validation_results: list[ExpectationValidationResult] = []
        successful_expectations = 0
        evaluated_expectations = 0
        payload = {"update_data_docs": {"class": "UpdateDataDocsAction"}}
        for checkpoint_result in self.checkpoint_results:
            # validation_result: ExpectationSuiteValidationResult = (
            #     ge_context.get_validation_result(suite_name, run_id=self.run_id)
            # )
            for validation_result, validation_result_id in zip(
                checkpoint_result.list_validation_results(),
                checkpoint_result.list_validation_result_identifiers(),
            ):
                if not validation_result.success:
                    doc_key = "_".join(validation_result_id.to_tuple())
                    doc_links = ge_context.get_docs_sites_urls(
                        resource_identifier=validation_result_id,
                        site_name="local_site",
                    )
                    payload["update_data_docs"][doc_key] = doc_links[0][
                        "site_url"
                    ].replace("%5C", "/")
                    failed_validation_results.extend(
                        [
                            result
                            for result in validation_result.results
                            if not result.success
                        ]
                    )
                successful_expectations += validation_result.statistics[
                    "successful_expectations"
                ]
                evaluated_expectations += validation_result.statistics[
                    "evaluated_expectations"
                ]

        # # old: check regularly if these workarounds for bugs in great expectations are still needed
        # validation_result.meta["active_batch_definition"][
        #     "batch_identifiers"
        # ] = IDDict(
        #     validation_result.meta["active_batch_definition"]["batch_identifiers"]
        # )
        # validation_result.meta["active_batch_definition"] = BatchDefinition(
        #     **validation_result.meta["active_batch_definition"]
        # )

        if evaluated_expectations == 0:
            success_percent = None
        else:
            success_percent = successful_expectations / evaluated_expectations * 100

        # create a summarizing validation result
        summary_validation_result = ExpectationSuiteValidationResult(
            success=len(failed_validation_results) == 0,
            results=failed_validation_results,
            evaluation_parameters=None,
            statistics={
                "successful_expectations": successful_expectations,
                "evaluated_expectations": evaluated_expectations,
                "success_percent": success_percent,
                "unsuccessful_expectations": evaluated_expectations
                - successful_expectations,
            },
            meta={
                "expectation_suite_name": self._notifier.subject,
                "batch_kwargs": {"data_asset_name": "All"},
                "run_id": self.run_id,
            },
        )

        self._notifier.run(
            validation_result_suite=summary_validation_result,
            validation_result_suite_identifier=ValidationResultIdentifier(
                expectation_suite_identifier=ExpectationSuiteIdentifier(
                    self._notifier.subject
                ),
                run_id=self.run_id,
                batch_identifier=None,
            ),
            data_asset=None,
            payload=payload,
        )

        # finally raise Exception if validations failed and option is set
        if self._fail_log and self._on_failure == "raise_later":
            raise SuiteValidationFailure(
                "During pipeline run one or more expectation suite validations failed:\n"
                "\n".join(self._fail_log)
            )

    def _run_validation(self, catalog: DataCatalog, data: Dict[str, Any]) -> None:
        ge_context = ge.get_context()

        for key, value in data.items():
            if self._single_datasource_check and self._datasource_run_counter[key] > 0:
                # skip each further check after the first
                continue
            self._datasource_run_counter[key] += 1
            catalog_key = key.replace(":", "__").replace(".", "__")
            adjusted_key = dot_to_underscore(key)

            if isinstance(getattr(catalog.datasets, catalog_key), PartitionedDataset):
                partitions = cast(Dict[str, Callable], value)
            else:
                partitions = {adjusted_key: lambda: value}

            for casted_key, casted_value in partitions.items():
                # Looking for a general expectation
                current_key = adjusted_key
                all_expectations = get_all_expectations(
                    ge_context=ge_context, adjusted_key=current_key
                )
                ge_adjusted_key = current_key

                # Looking for a specific expectation
                if (
                    not all_expectations and casted_key != adjusted_key
                ):  # partition dataset
                    adjusted_key_pt2 = dot_to_underscore(casted_key)
                    current_key = os.path.join(adjusted_key, adjusted_key_pt2)
                    all_expectations = get_all_expectations(
                        ge_context=ge_context, adjusted_key=current_key
                    )
                    ge_adjusted_key = current_key + "." + adjusted_key_pt2

                for exp_file in all_expectations:
                    suite_name = get_suite_name(exp_file, ge_adjusted_key)
                    value = casted_value()
                    if isinstance(value, PandasDataFrame):
                        result = validate(
                            ge_context,
                            casted_key,
                            suite_name,
                            value,
                            run_id=self.run_id,
                        )
                        self.checkpoint_results.append(result)
                    else:
                        raise SuiteValidationFailure(
                            f"Dataset {adjusted_key} is no Pandas DataFrame and not supported by Kedro Expectations"
                        )
                    if not result.success:
                        msg = f"Suite {suite_name} for DataSet {current_key} failed!"
                        self.publish_failure_msg(msg)
                if not all_expectations:
                    print(
                        f'No expectation suite was found for "{key}".',
                        "Validation will be skipped!",
                    )

    def publish_failure_msg(self, msg: str):
        if self._on_failure == "continue":
            print(msg)
        elif self._on_failure == "raise_fast":
            raise SuiteValidationFailure(msg)
        else:
            self._fail_log.append(msg)
