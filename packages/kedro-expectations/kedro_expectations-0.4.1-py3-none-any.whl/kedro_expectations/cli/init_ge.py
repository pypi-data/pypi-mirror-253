"""Defines all functions related to Great Expectations Datasources."""
import click
import os
import yaml
import great_expectations as ge
from kedro_expectations.utils import location_is_kedro_root_folder, base_ge_folder_exists
from ..constants import _DEFAULT_PANDAS_DATASOURCE_NAME
from subprocess import Popen, DEVNULL


@click.command()
def init() -> None:
    if location_is_kedro_root_folder():
        if base_ge_folder_exists():
            message = """
            This command has NOT been run
            Kedro expectations was already initiated and is ready to use.
            If you want to reset everything related to the plugin, you
            can delete the great_expectations folder and run init again
            """
            print(message)
        else:
            init_ge_and_create_datasources()


def init_ge_and_create_datasources() -> None:
    try:
        print("Creating base great_expectations folder...")
        env = dict(os.environ)
        Popen(
            "echo Y | great_expectations init",
            shell=True,
            stdout=DEVNULL,
            env=env
        ).wait()
        context = ge.get_context()

        print(f"Great expectations folder successfully created under {context.root_directory}!")
        print("Generating Kedro Expectations Datasource...")

        context.sources.add_pandas(name=_DEFAULT_PANDAS_DATASOURCE_NAME)

        print("Kedro Expectations successfully generated!")

    except yaml.YAMLError as exc:
        print("Error while parsing YAML:\n", exc)
