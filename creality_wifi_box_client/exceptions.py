"""Custom exceptions for the Creality WiFi Box client."""


class CrealityWifiBoxError(Exception):
    """Base exception for Creality WiFi Box errors."""


class ClientConnectionError(CrealityWifiBoxError):
    """Raised when connection to the box fails."""


class RequestTimeoutError(CrealityWifiBoxError):
    """Raised when a request times out."""


class InvalidResponseError(CrealityWifiBoxError):
    """Raised when the box returns an invalid response."""


class CommandError(CrealityWifiBoxError):
    """Raised when a command fails on the box."""
