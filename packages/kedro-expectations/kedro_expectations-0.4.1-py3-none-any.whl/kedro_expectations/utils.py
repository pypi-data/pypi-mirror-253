import datetime
import os
import glob
from typing import Union

import pandas as pd
import json
import great_expectations as ge
from great_expectations import DataContext
from great_expectations.core import RunIdentifier

from great_expectations.datasource.fluent import PandasDatasource
from kedro.framework.session import KedroSession
from kedro_datasets.partitions import PartitionedDataset

from .constants import _DEFAULT_PANDAS_DATASOURCE_NAME
import click
from time import sleep


def base_ge_folder_exists(verbose=True):
    base_folder = os.getcwd()
    ge_folder_legacy = os.path.join(base_folder, "great_expectations")
    ge_folder = os.path.join(base_folder, "gx")
    if os.path.exists(ge_folder) or os.path.exists(ge_folder_legacy):
        return True
    else:
        if verbose is True:
            message = """
            This command has NOT been run
            Kedro expectations wasn't initiated yet!
            Please run \'kedro expectations init\' before running this command.
            """
            print(message)
        return False


def location_is_kedro_root_folder():
    try:
        project_path = os.getcwd()
        KedroSession.create(project_path=project_path)
        return True
    except ModuleNotFoundError:
        print(
            """
        Cannot run command!
        You need to be in a kedro root folder to use Kedro Expectations!
        """
        )
        return False


def is_dataset_in_catalog(input, catalog):
    if input in catalog.list():
        return True
    else:
        print(
            f"\n\nThe input {input} was not found at the DataCatalog.\n",
            "The following datasets are available for use:\n",
        )
        print(*catalog.list(), sep=", ")
        return False


def dot_to_underscore(value):
    adjusted_value = str(value).replace(".", "_")
    return adjusted_value


def get_or_add_pandas_datasource(ge_context, name=_DEFAULT_PANDAS_DATASOURCE_NAME):
    try:
        return ge_context.get_datasource(name)
    except ValueError:
        return ge_context.sources.add_pandas(name)


def get_or_add_dataframe_asset(datasource: PandasDatasource, name: str):
    try:
        return datasource.get_asset(name)
    except LookupError:
        return datasource.add_dataframe_asset(name)


def validate(
    ge_context: DataContext,
    adjusted_key: str,
    suite_name: str,
    validation_df: pd.DataFrame,
    run_id: Union[None, RunIdentifier] = None,
):
    # Downward-compatibility: Make sure the dataframe asset exists
    dataframe_asset = get_or_add_dataframe_asset(
        get_or_add_pandas_datasource(ge_context), name=adjusted_key
    )
    batch_request = dataframe_asset.build_batch_request(validation_df)
    # TODO: Statt immer neu machen lieber fest definieren und laden. Batch Request während Runtime rein
    checkpoint = ge_context.add_or_update_checkpoint(
        name=f"{suite_name}_kedro_checkpoint",
        batch_request=batch_request,
        expectation_suite_name=suite_name,
    )
    validation_result = checkpoint.run(run_id=run_id)
    return validation_result


def get_all_expectations(ge_context, adjusted_key):
    exp_suites_pattern = os.path.join(
        os.path.normpath(
            ge_context.expectations_store.store_backend.full_base_directory
        ),
        adjusted_key,
        "*.json",
    )
    all_expectations = glob.glob(exp_suites_pattern)
    return all_expectations


def get_suite_name(exp_file, adjusted_key):
    parent_path, filename = os.path.split(exp_file)
    suite_name = adjusted_key + "." + filename[:-5]
    return suite_name


def create_raw_suite(ge_context, adjusted_input, suite_name, expectation_suite_name):
    base_exp_path = os.path.join(
        os.path.normpath(
            ge_context.expectations_store.store_backend.full_base_directory
        ),
        adjusted_input,
    )

    if not os.path.exists(base_exp_path):
        os.makedirs(base_exp_path)

    new_suite_path = os.path.join(
        base_exp_path,
        suite_name + ".json",
    )

    json_base = {
        "meta": {
            "great_expectations_version": str(ge.__version__),
        },
        "data_asset_type": None,
        "expectation_suite_name": expectation_suite_name,
        "expectations": [],
        "ge_cloud_id": None,
    }

    with open(new_suite_path, "w") as f:
        json.dump(json_base, f, ensure_ascii=False, indent=4)


def populate_new_suite(input_data: pd.DataFrame, expectation_suite_name: str):
    ge_context = ge.data_context.DataContext()

    datasource = get_or_add_pandas_datasource(ge_context)
    data_asset = get_or_add_dataframe_asset(
        datasource, name=expectation_suite_name.split(".")[0]
    )
    batch_request = data_asset.build_batch_request(dataframe=input_data)

    validator = ge_context.get_validator(
        batch_request=batch_request,
        expectation_suite_name=expectation_suite_name,
    )

    click.echo("\n\nYour dataset has the following columns:")
    click.echo(input_data.columns.values)
    click.echo(
        "One by one, type the name of the columns you do NOT want to validate.\nOnce you are finished, "
        "type 0 to continue"
    )
    column_to_remove = ""
    exclude_column_names = []
    while column_to_remove != "0":
        column_to_remove = click.prompt("", type=str)
        if column_to_remove == "0":
            pass
        elif column_to_remove not in input_data.columns:
            print(
                f"The column {column_to_remove} doesn't exist in this dataframe. Try typing again"
            )
        else:
            exclude_column_names.append(column_to_remove)

    if exclude_column_names:
        print("The following columns are not going to be validated:")
        print(exclude_column_names)
        sleep(3)
    else:
        print("You chose for all columns to be validated!")
        sleep(3)

    # Removing duplicates
    exclude_column_names = [*set(exclude_column_names)]

    if len(exclude_column_names) >= len(input_data.columns.values):
        print(
            "\n\nAll the columns were marked to be excluded!", "Impossible to validate!"
        )
    else:
        result = ge_context.assistants.onboarding.run(
            batch_request=batch_request,
            exclude_column_names=exclude_column_names,
        )
        validator.expectation_suite = result.get_expectation_suite(
            expectation_suite_name=expectation_suite_name
        )
        validator.save_expectation_suite(discard_failed_expectations=False)
    print(
        "\nFor more information about how to edit the expectations suite, access: "
        "https://docs.greatexpectations.io/docs/guides/expectations/creating_custom_expectations/overview/\n"
    )


def choose_valid_suite_name():
    suite_name = "."
    while "." in suite_name or "," in suite_name or " " in suite_name:
        suite_name = click.prompt("", type=str)
        if "." in suite_name or " " in suite_name:
            print(
                "Please choose another name for your suite.",
                "It cannot contain dots, commas or spaces",
            )
    return suite_name


def choose_valid_dataset_name(catalog):
    dataset_name = click.prompt("", type=str)
    while not isinstance(getattr(catalog.datasets, dataset_name), PartitionedDataset):
        print(f"The dataset {dataset_name} is not partitioned! Type again:")
        dataset_name = click.prompt("", type=str)
    return dataset_name
