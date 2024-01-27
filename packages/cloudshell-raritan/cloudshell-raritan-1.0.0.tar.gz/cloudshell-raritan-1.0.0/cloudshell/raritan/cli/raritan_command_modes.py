from __future__ import annotations

from typing import TYPE_CHECKING

from cloudshell.cli.service.command_mode import CommandMode

if TYPE_CHECKING:
    from cloudshell.cli.service.auth_model import Auth


class EnableCommandMode(CommandMode):
    PROMPT: str = r"(?:(?!\)).)#\s*$"
    ENTER_COMMAND: str = ""
    EXIT_COMMAND: str = ""

    def __init__(self, auth: Auth):
        """Initialize Default command mode."""
        self._auth = auth
        CommandMode.__init__(
            self,
            EnableCommandMode.PROMPT,
            EnableCommandMode.ENTER_COMMAND,
            EnableCommandMode.EXIT_COMMAND,
        )


class ConfigCommandMode(CommandMode):
    PROMPT: str = r"config:#\s*$"
    ENTER_COMMAND: str = "config"
    EXIT_COMMAND: str = "apply"  # Save changed settings and leave config mode

    def __init__(self, auth: Auth):
        """Initialize Configuration command mode."""
        self._auth = auth

        CommandMode.__init__(
            self,
            ConfigCommandMode.PROMPT,
            ConfigCommandMode.ENTER_COMMAND,
            ConfigCommandMode.EXIT_COMMAND,
        )


CommandMode.RELATIONS_DICT = {EnableCommandMode: {ConfigCommandMode: {}}}
