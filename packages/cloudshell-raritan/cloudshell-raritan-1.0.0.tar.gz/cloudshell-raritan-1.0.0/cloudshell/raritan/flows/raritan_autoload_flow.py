from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from cloudshell.shell.flows.autoload.basic_flow import AbstractAutoloadFlow

from cloudshell.raritan.command_actions.system_actions import SystemActions

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from cloudshell.shell.core.driver_context import AutoLoadDetails
    from cloudshell.shell.standards.pdu.autoload_model import PDUResourceModel

    from ..cli.raritan_cli_configurator import RaritanCliConfigurator


class RaritanAutoloadFlow(AbstractAutoloadFlow):
    """Autoload flow."""

    def __init__(self, cli_configurator: RaritanCliConfigurator):
        super().__init__()
        self.cli_configurator = cli_configurator

    def _autoload_flow(
        self, supported_os: list[str], resource_model: PDUResourceModel
    ) -> AutoLoadDetails:
        """Autoload Flow."""
        logger.info("*" * 70)
        logger.info("Start discovery process .....")
        with self.cli_configurator.enable_mode_service() as enable_cli_service:
            system_actions = SystemActions(enable_cli_service)
            outlets_info = system_actions.get_outlets()
            pdu_info = system_actions.get_pdu_info()

            resource_model.vendor = "Raritan"
            resource_model.model = pdu_info.get("model", "")

            for outlet_id, outlet_state in outlets_info.items():
                outlet_object = resource_model.entities.PowerSocket(index=outlet_id)
                resource_model.connect_power_socket(outlet_object)

            logger.info("Discovery process finished successfully")

            autoload_details = resource_model.build()

        return autoload_details
