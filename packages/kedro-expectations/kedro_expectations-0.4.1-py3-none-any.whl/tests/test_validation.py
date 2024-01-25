import pytest
from kedro.framework.hooks import hook_impl
from kedro.framework.session import KedroSession
from kedro_expectations import KedroExpectationsHooks
from notification import DummyNotifier


def test_project_dir_exists(initialize_kedro_project):
    # The `initialize_kedro_project` fixture is automatically invoked,
    # and its return value is the project directory.
    project_dir = initialize_kedro_project

    # Check if the project directory contains the expected files
    assert (project_dir / "src" / "test_project").exists()
    assert (project_dir / "conf" / "base" / "catalog.yml").exists()


@pytest.mark.parametrize("notify_on", ["all", "success"])
def test_success_notification(initialize_kedro_project, capfd, notify_on):
    project_dir = initialize_kedro_project

    with KedroSession.create(project_path=project_dir) as session:
        assert not session._hook_manager.is_registered(KedroExpectationsHooks)
        session._hook_manager.register(
            KedroExpectationsHooks(on_failure="raise_fast",
                                   notify_config=DummyNotifier(notify_on=notify_on))
        )

        session.run()
        # Check if the DummyNotifier (which runs the gx NoOpAction) got called
        out, err = capfd.readouterr()
        assert "Happily doing nothing" in out


def test_failure_notification_no_failure(initialize_kedro_project, capfd):
    project_dir = initialize_kedro_project

    with KedroSession.create(project_path=project_dir) as session:
        assert not session._hook_manager.is_registered(KedroExpectationsHooks)
        session._hook_manager.register(
            KedroExpectationsHooks(on_failure="raise_fast",
                                   notify_config=DummyNotifier(notify_on="failure"))
        )

        session.run()
        # Check if the DummyNotifier (which runs the gx NoOpAction) got NOT called
        out, err = capfd.readouterr()
        assert "Happily doing nothing" not in out
