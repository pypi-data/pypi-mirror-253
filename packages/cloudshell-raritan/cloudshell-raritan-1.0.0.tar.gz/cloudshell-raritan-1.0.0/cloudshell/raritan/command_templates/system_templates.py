from __future__ import annotations

from cloudshell.cli.command_template.command_template import CommandTemplate

GET_PDU_INFO = CommandTemplate(command="show pdu details")
GET_OUTLETS_INFO = CommandTemplate(command="show outlets")

CHANGE_OUTLET_STATE = CommandTemplate(
    command="power outlets {outlet_ids} {outlet_state} /y",
    action_map={r"\[y/n\]": lambda session, logger: session.send_line("y", logger)},
    error_map={
        "[Ii]nvalid outlet specified": "Invalid outlet specified.",
        "[Oo]peration  on/off/cycle": "Wrong outlet state provided. "
        "Possible values: on/off/cycle",
    },
)
