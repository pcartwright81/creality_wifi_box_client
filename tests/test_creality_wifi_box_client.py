"""Tests for the Creality Wifi Box Client."""

from collections.abc import Generator
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest

from creality_wifi_box_client.creality_wifi_box_client import CrealityWifiBoxClient
from creality_wifi_box_client.exceptions import (
    ClientConnectionError,
    CommandError,
    InvalidResponseError,
    RequestTimeoutError,
)


@pytest.fixture
def client() -> CrealityWifiBoxClient:
    """Create a client instance for testing."""
    return CrealityWifiBoxClient("192.168.1.100", 8080)


@pytest.fixture
def mock_session() -> Generator[MagicMock, Any]:
    """Mock the aiohttp ClientSession."""
    with patch("aiohttp.ClientSession") as mock:
        session = MagicMock()
        mock.return_value = session
        session.closed = False
        session.close = AsyncMock()
        session.get.return_value = AsyncMock()
        yield session


@pytest.mark.asyncio
async def test_init() -> None:
    """Test client initialization."""
    client = CrealityWifiBoxClient("1.2.3.4", 1234)
    assert client.base_url == "http://1.2.3.4:1234/protocal.csp"


@pytest.mark.asyncio
async def test_context_manager(mock_session: MagicMock) -> None:
    """Test the async context manager."""
    async with CrealityWifiBoxClient("1.2.3.4", 1234):
        pass

    # Verify session is closed after context exit
    mock_session.close.assert_called_once()


@pytest.mark.asyncio
async def test_get_info_success(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test successful get_info call."""
    # Mock response
    mock_response = AsyncMock()
    mock_response.text.return_value = '{"model": "test"}'
    mock_session.get.return_value.__aenter__.return_value = mock_response

    # Mock BoxInfo to avoid Pydantic dependency in tests
    with patch("creality_wifi_box_client.creality_wifi_box_client.BoxInfo") as mock_box_info:
        await client.get_info()

        mock_session.get.assert_called_once()
        # Verify URL parameters
        args, _ = mock_session.get.call_args
        assert "fname=Info" in args[0]
        assert "opt=main" in args[0]
        assert "function=get" in args[0]

        mock_box_info.model_validate.assert_called_once_with({"model": "test"})


@pytest.mark.asyncio
async def test_get_info_timeout(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test get_info timeout."""
    mock_session.get.side_effect = aiohttp.ServerTimeoutError()

    with pytest.raises(RequestTimeoutError, match="Request to WiFi Box timed out"):
        await client.get_info()


@pytest.mark.asyncio
async def test_get_info_connection_error(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test get_info connection error."""
    mock_session.get.side_effect = aiohttp.ClientConnectionError("Connection refused")

    with pytest.raises(ClientConnectionError, match="Failed to connect to WiFi Box"):
        await client.get_info()


@pytest.mark.asyncio
async def test_get_info_invalid_json(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test get_info with invalid JSON response."""
    mock_response = AsyncMock()
    mock_response.text.return_value = "Not JSON"
    mock_session.get.return_value.__aenter__.return_value = mock_response

    with pytest.raises(InvalidResponseError, match="Invalid response from WiFi Box"):
        await client.get_info()


@pytest.mark.asyncio
async def test_get_info_http_error(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test get_info HTTP error."""
    mock_session.get.side_effect = aiohttp.ClientResponseError(
        request_info=MagicMock(), history=(), status=500, message="Internal Error"
    )

    with pytest.raises(ClientConnectionError, match="HTTP error from WiFi Box"):
        await client.get_info()


@pytest.mark.asyncio
async def test_pause_print_success(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test successful pause_print."""
    mock_response = AsyncMock()
    mock_response.text.return_value = '{"error": 0}'
    mock_session.get.return_value.__aenter__.return_value = mock_response

    result = await client.pause_print()
    assert result is True

    args, _ = mock_session.get.call_args
    assert "pause=1" in args[0]


@pytest.mark.asyncio
async def test_send_command_failure(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test command failure (error != 0)."""
    mock_response = AsyncMock()
    mock_response.text.return_value = '{"error": 1}'
    mock_session.get.return_value.__aenter__.return_value = mock_response

    with pytest.raises(CommandError, match="Command 'pause print' failed"):
        await client.pause_print()


@pytest.mark.asyncio
async def test_send_command_timeout(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test command timeout."""
    mock_session.get.side_effect = aiohttp.ServerTimeoutError()

    with pytest.raises(RequestTimeoutError, match="Command 'pause print' timed out"):
        await client.pause_print()


@pytest.mark.asyncio
async def test_send_command_connection_error(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test command connection error."""
    mock_session.get.side_effect = aiohttp.ClientConnectionError("Fail")

    with pytest.raises(ClientConnectionError, match="Failed to connect to WiFi Box"):
        await client.pause_print()


@pytest.mark.asyncio
async def test_send_command_invalid_json(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test command invalid JSON response."""
    mock_response = AsyncMock()
    mock_response.text.return_value = "Bad JSON"
    mock_session.get.return_value.__aenter__.return_value = mock_response

    with pytest.raises(InvalidResponseError, match="Invalid response for 'pause print'"):
        await client.pause_print()


@pytest.mark.asyncio
async def test_resume_print_success(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test successful resume_print."""
    mock_response = AsyncMock()
    mock_response.text.return_value = '{"error": 0}'
    mock_session.get.return_value.__aenter__.return_value = mock_response

    result = await client.resume_print()
    assert result is True

    args, _ = mock_session.get.call_args
    assert "pause=0" in args[0]


@pytest.mark.asyncio
async def test_stop_print_success(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test successful stop_print."""
    mock_response = AsyncMock()
    mock_response.text.return_value = '{"error": 0}'
    mock_session.get.return_value.__aenter__.return_value = mock_response

    result = await client.stop_print()
    assert result is True

    args, _ = mock_session.get.call_args
    assert "stop=1" in args[0]


@pytest.mark.asyncio
async def test_send_command_http_error(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test command HTTP error."""
    mock_session.get.side_effect = aiohttp.ClientResponseError(
        request_info=MagicMock(), history=(), status=500, message="Internal Error"
    )

    with pytest.raises(ClientConnectionError, match="HTTP error for 'pause print'"):
        await client.pause_print()


@pytest.mark.asyncio
async def test_session_reuse(client: CrealityWifiBoxClient) -> None:
    """Test session reuse."""
    with patch("aiohttp.ClientSession") as mock_cls:
        mock_instance = MagicMock()
        mock_cls.return_value = mock_instance
        mock_instance.closed = False
        mock_instance.get.return_value.__aenter__.return_value = AsyncMock(
            text=AsyncMock(return_value='{"model": "test"}')
        )

        with patch("creality_wifi_box_client.creality_wifi_box_client.BoxInfo"):
            # First call creates session
            await client.get_info()

            # Second call should reuse session
            await client.get_info()

        assert mock_cls.call_count == 1


@pytest.mark.asyncio
async def test_close_no_session(client: CrealityWifiBoxClient) -> None:
    """Test close when no session exists."""
    await client.close()


@pytest.mark.asyncio
async def test_close_closed_session(client: CrealityWifiBoxClient, mock_session: MagicMock) -> None:
    """Test close when session is already closed."""
    # Setup: Create a session
    mock_response = AsyncMock()
    mock_response.text.return_value = "{}"
    mock_session.get.return_value.__aenter__.return_value = mock_response

    with patch("creality_wifi_box_client.creality_wifi_box_client.BoxInfo"):
        await client.get_info()

    # Simulate session being closed externally
    mock_session.closed = True

    await client.close()
    mock_session.close.assert_not_called()
