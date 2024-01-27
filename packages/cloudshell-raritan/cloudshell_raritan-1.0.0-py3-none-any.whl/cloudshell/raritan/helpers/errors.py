from __future__ import annotations


class BaseRaritanError(Exception):
    """Base Raritan Error."""


class NotSupportedRaritanError(BaseRaritanError):
    """Not supported by Raritan."""


class SnmpRaritanError(BaseRaritanError):
    """Base SNMP Raritan Error."""
