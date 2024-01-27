from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from attrs import define

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)
from cloudshell.snmp.snmp_parameters import SNMPV3Parameters  # noqa F401

from cloudshell.raritan.command_templates import snmp_configuration_templates

if TYPE_CHECKING:
    from cloudshell.cli.service.cli_service import CliService


@define
class BaseSnmpActions:
    _cli_service: CliService
    SNMP_VERSION: ClassVar[str] = "snmp_version"

    def enable_snmp(self) -> str:
        """Enable snmp."""
        return CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=snmp_configuration_templates.ENABLE_SNMP,
        ).execute_command(snmp_version=self.SNMP_VERSION)

    def disable_snmp(self) -> str:
        """Disable snmp."""
        return CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=snmp_configuration_templates.DISABLE_SNMP,
        ).execute_command(snmp_version=self.SNMP_VERSION)

    def commit(self) -> str:
        """Save changed settings and leave config mode."""
        return CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=snmp_configuration_templates.COMMIT,
        ).execute_command()


class EnableDisableSnmpV2Actions(BaseSnmpActions):
    SNMP_VERSION: ClassVar[str] = "v1/v2c"

    def set_snmp_ro_community(self, snmp_community):
        """Set read community."""
        return CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=snmp_configuration_templates.SET_RO_SNMP_COMMUNITY,
        ).execute_command(name=snmp_community)

    def set_snmp_rw_community(self, snmp_community):
        """Set write community."""
        return CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=snmp_configuration_templates.SET_RW_SNMP_COMMUNITY,
        ).execute_command(name=snmp_community)


class EnableDisableSnmpV3Actions(BaseSnmpActions):
    SNMP_VERSION: ClassVar[str] = "v3"
