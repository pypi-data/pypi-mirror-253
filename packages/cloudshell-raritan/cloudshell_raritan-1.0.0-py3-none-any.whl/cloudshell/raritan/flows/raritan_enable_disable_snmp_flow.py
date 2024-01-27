from __future__ import annotations

from typing import TYPE_CHECKING

from attrs import define

from cloudshell.snmp.snmp_configurator import EnableDisableSnmpFlowInterface

from cloudshell.raritan.command_actions.enable_disable_snmp_actions import (  # noqa: E501
    EnableDisableSnmpV2Actions,
    EnableDisableSnmpV3Actions,
)
from cloudshell.raritan.helpers.errors import SnmpRaritanError

if TYPE_CHECKING:
    from typing import Union

    from cloudshell.cli.service.cli_service import CliService
    from cloudshell.snmp.snmp_parameters import (
        SNMPReadParameters,
        SNMPV3Parameters,
        SNMPWriteParameters,
    )

    from ..cli.raritan_cli_configurator import RaritanCliConfigurator

    SnmpParams = Union[SNMPReadParameters, SNMPWriteParameters, SNMPV3Parameters]


@define
class RaritanEnableDisableSnmpFlow(EnableDisableSnmpFlowInterface):
    _cli_configurator: RaritanCliConfigurator

    def enable_snmp(self, snmp_parameters: SnmpParams) -> None:
        with self._cli_configurator.enable_mode_service() as cli_service:
            if snmp_parameters.version == snmp_parameters.SnmpVersion.V3:
                self._enable_snmp_v3(cli_service, snmp_parameters)
            else:
                self._enable_snmp_v2(cli_service, snmp_parameters)

    def disable_snmp(self, snmp_parameters: SnmpParams) -> None:
        with self._cli_configurator.enable_mode_service() as cli_service:
            if snmp_parameters.version == snmp_parameters.SnmpVersion.V3:
                self._disable_snmp_v3(cli_service, snmp_parameters)
            else:
                self._disable_snmp_v2(cli_service, snmp_parameters)

    @staticmethod
    def _enable_snmp_v2(cli_service: CliService, snmp_parameters: SnmpParams) -> str:
        """Enable SNMPv2."""
        snmp_community = snmp_parameters.snmp_community

        if not snmp_community:
            raise SnmpRaritanError("SNMP community can not be empty")

        snmp_v2_actions = EnableDisableSnmpV2Actions(cli_service=cli_service)
        output = snmp_v2_actions.enable_snmp()

        if snmp_parameters.is_read_only:
            output += snmp_v2_actions.set_snmp_ro_community(
                snmp_community=snmp_community
            )
        else:
            output += snmp_v2_actions.set_snmp_rw_community(
                snmp_community=snmp_community
            )
        return output

    @staticmethod
    def _enable_snmp_v3(cli_service: CliService, snmp_parameters: SnmpParams) -> str:
        """Enable SNMPv3."""
        snmp_v3_actions = EnableDisableSnmpV3Actions(cli_service=cli_service)
        output = snmp_v3_actions.enable_snmp()

        return output

    @staticmethod
    def _disable_snmp_v2(cli_service: CliService, snmp_parameters: SnmpParams) -> str:
        """Disable SNMPv2."""
        snmp_community = snmp_parameters.snmp_community

        if not snmp_community:
            raise SnmpRaritanError("SNMP community can not be empty")

        snmp_v2_actions = EnableDisableSnmpV2Actions(cli_service=cli_service)

        output = snmp_v2_actions.disable_snmp()

        return output

    @staticmethod
    def _disable_snmp_v3(cli_service: CliService, snmp_parameters: SnmpParams) -> str:
        """Disable SNMPv3."""
        snmp_v3_actions = EnableDisableSnmpV3Actions(cli_service)

        output = snmp_v3_actions.disable_snmp()

        return output
