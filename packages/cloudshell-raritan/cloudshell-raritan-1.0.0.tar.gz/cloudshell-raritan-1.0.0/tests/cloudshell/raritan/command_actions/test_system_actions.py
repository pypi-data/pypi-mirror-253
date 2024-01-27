from __future__ import annotations

from unittest import TestCase
from unittest.mock import Mock, patch

from cloudshell.raritan.command_actions.system_actions import SystemActions


class TestSystemActions(TestCase):
    def setUp(self):
        self._cli_service = Mock()
        self.system_actions = SystemActions(self._cli_service)

    def test_init(self):
        self.assertIs(self.system_actions._cli_service, self._cli_service)

    @patch("cloudshell.raritan.command_actions.system_actions.CommandTemplateExecutor")
    def test_get_pdu_info(self, command_template_executor):
        output = """
PDU 'Raritan_PX3_demo_2'
Model:            PX3-5145R
Firmware Version: 4.1.1.5-49961
Serial Number:    RE25550015
Board Revision:   0x03

Relay behavior on power loss:     Non-latching
Trip cause outlet handling:       Keep unchanged
Default outlet state on power-up: Last known state
Power cycle delay:                10 seconds

Outlet power sequence:        default
Outlet sequence delays:       1-8: 0 s
Inrush guard delay:           200 ms
Outlet initialization delay:  3 s

Voltage rating:   100-120V
Current rating:   12A
Frequency rating: 50/60Hz
Power rating:     1.2-1.4kVA

Internal beeper: Off

Sensor data retrieval:      Enabled
Sensor data backup:         Disabled
Measurements per log entry: 60
Log capacity:               120 records
        """
        execute_command = Mock()
        command_template_executor.return_value = execute_command
        execute_command.execute_command.return_value = output

        # act
        res = self.system_actions.get_pdu_info()

        # assert
        self.assertEqual(
            res, {"model": "PX3-5145R", "fw": "4.1.1.5-49961", "serial": "RE25550015"}
        )

    @patch("cloudshell.raritan.command_actions.system_actions.CommandTemplateExecutor")
    def test_get_outlets(self, command_template_executor):
        output = """
Outlet 1:
Power state: On

Outlet 2:
Power state: Off

Outlet 3:
Power state: On

Outlet 4:
Power state: Off

Outlet 5:
Power state: On

Outlet 6:
Power state: Off

Outlet 7:
Power state: On

Outlet 8:
Power state: Off
        """
        execute_command = Mock()
        command_template_executor.return_value = execute_command
        execute_command.execute_command.return_value = output

        # act
        res = self.system_actions.get_outlets()

        # assert
        self.assertEqual(
            res,
            {
                "1": "On",
                "2": "Off",
                "3": "On",
                "4": "Off",
                "5": "On",
                "6": "Off",
                "7": "On",
                "8": "Off",
            },
        )
