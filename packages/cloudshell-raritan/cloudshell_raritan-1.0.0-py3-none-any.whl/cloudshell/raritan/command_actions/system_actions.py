from __future__ import annotations

import re
from typing import TYPE_CHECKING

from attrs import define

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)

from cloudshell.raritan.command_templates import system_templates

if TYPE_CHECKING:
    from cloudshell.cli.service.cli_service import CliService


@define
class SystemActions:
    _cli_service: CliService

    def get_pdu_info(self) -> dict[str, str]:
        """Get information about outlets."""
        pdu_info = {}
        output = CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=system_templates.GET_PDU_INFO,
        ).execute_command()

        match = re.search(
            r"Model:\s+(?P<model>.+)\s+"
            r"Firmware Version:\s+(?P<fw>.+)\s+"
            r"Serial Number: \s+(?P<serial>\w+)",
            output,
            re.I,
        )
        if match:
            pdu_info.update(
                {
                    "model": match.groupdict()["model"],
                    "fw": match.groupdict()["fw"],
                    "serial": match.groupdict()["serial"],
                }
            )
        return pdu_info

    def get_outlets(self) -> dict[str, str]:
        """Get information about outlets."""
        outlets_info = {}
        output = CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=system_templates.GET_OUTLETS_INFO,
        ).execute_command()

        for outlet_id, outlet_state in re.findall(
            r"Outlet\s+(?P<outlet_id>\d+):\sPower state:\s+(?P<outlet_state>\w+)",
            output,
        ):
            outlets_info.update({outlet_id: outlet_state})

        return outlets_info

    def set_outlets_state(self, outlets: str, outlet_state: str) -> str:
        """Set outlets state.

        Possible outlets states could be on/off/cycle.
        """
        return CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=system_templates.CHANGE_OUTLET_STATE,
        ).execute_command(outlet_ids=outlets, outlet_state=outlet_state)
