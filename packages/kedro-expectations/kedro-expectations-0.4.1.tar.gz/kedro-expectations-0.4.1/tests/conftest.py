import shutil
import tempfile
import os
import pytest
from pathlib import Path
from kedro.framework.startup import bootstrap_project

_created_project_dirs = set()

test_dir = Path(__file__).parent


@pytest.fixture(scope="session", autouse=True)
def initialize_kedro_project(request):
    # Set up a temporary directory for the Kedro project
    temp_dir = tempfile.mkdtemp(prefix="kedro_expectation_tests_")
    project_dir = Path(temp_dir)

    # Change the working directory to the project directory
    os.chdir(project_dir)

    # Create a new Kedro project
    exit_code = os.system(
        f"kedro new --starter={str(test_dir.joinpath('template_project'))}"
    )
    if exit_code != 0:
        raise Exception("Failed to initialize Kedro project")

    project_dir = project_dir.joinpath("test-project").resolve()
    os.chdir(project_dir)

    # register the project directory in Kedro
    bootstrap_project(project_dir)

    # Return the project directory
    _created_project_dirs.add(project_dir)
    yield project_dir

    # Clean up the temporary project directory after the tests
    try:
        shutil.rmtree(temp_dir)
    except PermissionError:
        pass


def pytest_sessionfinish(session, exitstatus):
    # Cleanup any remaining temporary directories
    for project_dir in _created_project_dirs:
        shutil.rmtree(project_dir)
