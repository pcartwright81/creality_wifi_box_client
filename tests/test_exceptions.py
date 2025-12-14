"""Tests for custom exceptions."""

from creality_wifi_box_client.exceptions import (
    ClientConnectionError,
    CommandError,
    CrealityWifiBoxError,
    InvalidResponseError,
    RequestTimeoutError,
)


def test_base_exception() -> None:
    """Test base exception."""
    exc = CrealityWifiBoxError("Test error")
    assert str(exc) == "Test error"
    assert isinstance(exc, Exception)


def test_connection_error() -> None:
    """Test ClientConnectionError."""
    exc = ClientConnectionError("Connection failed")
    assert str(exc) == "Connection failed"
    assert isinstance(exc, CrealityWifiBoxError)


def test_timeout_error() -> None:
    """Test RequestTimeoutError."""
    exc = RequestTimeoutError("Request timed out")
    assert str(exc) == "Request timed out"
    assert isinstance(exc, CrealityWifiBoxError)


def test_invalid_response_error() -> None:
    """Test InvalidResponseError."""
    exc = InvalidResponseError("Invalid JSON")
    assert str(exc) == "Invalid JSON"
    assert isinstance(exc, CrealityWifiBoxError)


def test_command_error() -> None:
    """Test CommandError."""
    exc = CommandError("Command failed")
    assert str(exc) == "Command failed"
    assert isinstance(exc, CrealityWifiBoxError)
