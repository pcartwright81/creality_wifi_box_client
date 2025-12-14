# Creality WiFi Box Client

A Python async client library for interacting with the Creality WiFi Box API.

## Installation

```bash
pip install creality-wifi-box-client
```

## Features

- ✨ Async/await support with proper resource management
- 🔒 Type-safe with full type hints
- 🛡️ Comprehensive error handling
- ⚡ Efficient session reuse
- 📦 Pydantic data validation
- 🧪 100% test coverage

## Quick Start

### Basic Usage

```python
import asyncio
from creality_wifi_box_client import CrealityWifiBoxClient

async def main() -> None:
    # Create client with context manager (recommended)
    async with CrealityWifiBoxClient("192.168.1.100", 8080) as client:
        # Get printer info
        info = await client.get_info()
        print(f"Printer Model: {info.model}")
        print(f"Print Progress: {info.print_progress}%")
        print(f"Nozzle Temperature: {info.nozzle_temp}°C")
        print(f"Bed Temperature: {info.bed_temp}°C")

        # Control print job
        await client.pause_print()
        await asyncio.sleep(5)
        await client.resume_print()

asyncio.run(main())
```

### Manual Session Management

```python
async def main() -> None:
    client = CrealityWifiBoxClient("192.168.1.100", 8080, timeout=30)

    try:
        info = await client.get_info()
        print(f"Current file: {info.print_name}")
    finally:
        await client.close()
```

## API Reference

### CrealityWifiBoxClient

#### Constructor

```python
CrealityWifiBoxClient(box_ip: str, box_port: int, timeout: int = 30)
```

**Parameters:**
- `box_ip`: IP address of the WiFi Box
- `box_port`: Port number (typically 8080)
- `timeout`: Request timeout in seconds (default: 30)

#### Methods

##### `async get_info() -> BoxInfo`

Retrieves comprehensive printer and box information.

**Returns:** `BoxInfo` object with all device data

**Raises:**
- `ClientConnectionError`: Connection to box failed
- `RequestTimeoutError`: Request timed out
- `InvalidResponseError`: Malformed response

##### `async pause_print() -> bool`

Pauses the current print job.

**Returns:** `True` if successful

**Raises:**
- `ClientConnectionError`: Connection failed
- `RequestTimeoutError`: Request timed out
- `CommandError`: Command failed on the box

##### `async resume_print() -> bool`

Resumes a paused print job.

**Returns:** `True` if successful

##### `async stop_print() -> bool`

Stops the current print job.

**Returns:** `True` if successful

##### `async close() -> None`

Closes the client session and cleans up resources. Called automatically when using context manager.

### BoxInfo

The `BoxInfo` class contains all printer and box information with the following key fields:

**Network:**
- `wanip`, `ssid`, `net_ip`

**Temperatures:**
- `nozzle_temp`, `bed_temp`, `chamber_temp`

**Print Status:**
- `print_name`, `print_progress`, `state`, `pause`
- `print_left_time`, `print_job_time`
- `layer`, `total_layer`

**Device Info:**
- `model`, `box_version`, `model_version`
- `filament_type`, `consumables_len`

## Error Handling

The library provides specific exceptions for different error scenarios:

```python
from creality_wifi_box_client import (
    CrealityWifiBoxClient,
    ClientConnectionError,
    RequestTimeoutError,
    CommandError,
    InvalidResponseError,
)

async def safe_print_control() -> None:
    async with CrealityWifiBoxClient("192.168.1.100", 8080) as client:
        try:
            await client.pause_print()
        except ClientConnectionError:
            print("Could not connect to printer")
        except RequestTimeoutError:
            print("Request timed out")
        except CommandError:
            print("Command failed on the printer")
        except InvalidResponseError:
            print("Received invalid response")
```

## Development

### Setup

```bash
# Clone repository
git clone https://github.com/pcartwright81/creality_wifi_box_client.git
cd creality_wifi_box_client

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install with dev dependencies
pip install -e .[dev,test]
```

### Testing

```bash
# Run tests with coverage
pytest

# Run linting
ruff check .
ruff format . --check
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

Created by Patrick Cartwright (@pcartwright81)
