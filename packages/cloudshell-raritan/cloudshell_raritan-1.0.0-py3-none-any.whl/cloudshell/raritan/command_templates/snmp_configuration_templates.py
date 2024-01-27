from __future__ import annotations

from cloudshell.cli.command_template.command_template import CommandTemplate

ENABLE_SNMP = CommandTemplate(
    command="network services snmp {snmp_version} enable",
    action_map={
        r"Are you sure you want to enable it\? \[y/n\]": lambda session, logger: session.send_line(  # noqa: E501
            "y", logger
        )
    },
)

DISABLE_SNMP = CommandTemplate("network services snmp {snmp_version} disable")

SET_RO_SNMP_COMMUNITY = CommandTemplate(
    command="network services snmp readCommunity {read_community}"
)

SET_RW_SNMP_COMMUNITY = CommandTemplate(
    command="network services snmp writeCommunity {write_community}"
)

COMMIT = CommandTemplate(command="apply")
