from abc import ABC, abstractmethod
from typing import List

from great_expectations.checkpoint import EmailAction, NoOpAction
from great_expectations.core import ExpectationSuiteValidationResult
from great_expectations.data_context.types.resource_identifiers import (
    ValidationResultIdentifier,
)


class BaseNotifier(ABC):
    def __init__(
        self,
        sender_alias: str,
        recipients: List[str],
        notify_on: str = "all",
        subject: str = "Summary Run Validation",
    ):
        """
        :param sender_alias: Alias of the sender
        :param recipients: List of recipients as str. Format is dependent on the specific notifier.
        :param notify_on: Specifies validation status that triggers notification. One of "all", "failure", "success".
        :param subject: General subject of the notification.
        """
        self._sender_alias = sender_alias
        self._recipients = recipients
        self._notify_on = notify_on
        self.subject = subject

    @property
    @abstractmethod
    def _action(self):
        pass

    def run(
        self,
        validation_result_suite: ExpectationSuiteValidationResult,
        validation_result_suite_identifier=ValidationResultIdentifier,
        data_asset=None,
        payload=None,
    ):
        # required to check success already here as e.g. NoOpAction does not check this.
        validation_success = validation_result_suite.success
        if (
                (self._notify_on == "all")
                or (self._notify_on == "success" and validation_success)
                or (self._notify_on == "failure" and not validation_success)
        ):
            try:
                self._action.run(
                    validation_result_suite=validation_result_suite,
                    validation_result_suite_identifier=validation_result_suite_identifier,
                    data_asset=data_asset,
                    payload=payload,
                )
            except TypeError:
                self._action.run(
                    validation_result_suite=validation_result_suite,
                    validation_result_suite_identifier=validation_result_suite_identifier,
                    data_asset=data_asset,
                )


class EmailNotifier(BaseNotifier):
    _action = None

    def __init__(
        self,
        recipients: List[str],
        sender_login: str,
        sender_password: str,
        smtp_address: str,
        smtp_port: str,
        sender_alias: str = "validation_notifier@kedro-expectations.io",
        security_protocol: str = "SSL",
        notify_on: str = "all",
        subject: str = "Summary Run Validation",
    ):
        super().__init__(
            sender_alias=sender_alias,
            recipients=recipients,
            notify_on=notify_on,
            subject=subject,
        )
        self._action = EmailAction(
            data_context=None,
            renderer={
                "module_name": "great_expectations.render.renderer.email_renderer",
                "class_name": "EmailRenderer",
            },
            smtp_address=smtp_address,
            smtp_port=smtp_port,
            sender_login=sender_login,
            sender_password=sender_password,
            receiver_emails=",".join(recipients),
            sender_alias=sender_alias,
            use_ssl=security_protocol.lower() == "ssl",
            use_tls=security_protocol.lower() == "tls",
            notify_on=self._notify_on,
            notify_with=None,
        )


class DummyNotifier(BaseNotifier):
    """
    Dummy class used for test purposes
    """
    _action = None

    def __init__(
        self,
        notify_on: str = "all",
    ):
        super().__init__(
            sender_alias="", recipients=[], notify_on=notify_on, subject=""
        )
        self._action = NoOpAction(data_context=None)
