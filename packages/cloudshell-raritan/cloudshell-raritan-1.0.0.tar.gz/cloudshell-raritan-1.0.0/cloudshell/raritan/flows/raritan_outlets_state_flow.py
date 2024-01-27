from __future__ import annotations

from typing import TYPE_CHECKING

from cloudshell.raritan.command_actions.system_actions import SystemActions
from cloudshell.raritan.helpers.errors import NotSupportedRaritanError

if TYPE_CHECKING:
    from ..cli.raritan_cli_configurator import RaritanCliConfigurator


class RaritanOutletsStateFlow:
    AVAILABLE_STATES = ["on", "off", "cycle"]

    def __init__(self, cli_configurator: RaritanCliConfigurator):
        self.cli_configurator = cli_configurator

    @staticmethod
    def _ports_to_outlet_ids(ports: list[str]) -> str:
        """Convert ports to the suitable format."""
        return ",".join(port.split("/")[-1].replace("PS", "") for port in ports)

    def set_outlets_state(self, ports: list[str], state: str) -> None:
        """Set Outlet/Outlets state.

        Change outlet or list of outlets state to the provided state.
        :param ports: ['192.168.30.128/PS4', '192.168.30.128/PS6']
        :param state: outlet state to be set. Possible values: on, off, cycle
        """
        if state not in self.AVAILABLE_STATES:
            raise NotSupportedRaritanError(f"State '{state}' is not supported.")

        outlets = RaritanOutletsStateFlow._ports_to_outlet_ids(ports=ports)
        with self.cli_configurator.enable_mode_service() as enable_cli_service:
            system_actions = SystemActions(enable_cli_service)

            system_actions.set_outlets_state(outlets=outlets, outlet_state=state)
