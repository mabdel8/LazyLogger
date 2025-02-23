# Simple Python Logger

A lightweight, easy-to-use Python logging library inspired by Loguru's simplicity. This logger provides a straightforward way to add logging to your Python applications with minimal configuration.

## Features

- 🚀 Simple to use - just import and start logging
- 📝 Multiple output handlers (console and file)
- 🎨 Formatted output with timestamp and context information
- 🔍 Multiple logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- 🛠️ Customizable format strings
- 🧵 Thread-safe logging

## Installation

Clone this repository:
bash
git clone https://github.com/yourusername/simple-python-logger.git
cd simple-python-logger

## Quick Start

### Basic Usage

```python
from aisettings import logger
Basic logging with different levels
logger.debug("Debug message: Detailed information for developers")
logger.info("Info message: Normal program operation")
logger.warning("Warning message: Something unexpected but not critical")
logger.error("Error message: Something failed")
logger.critical("Critical message: Serious failure")
```
### Adding File Output

You can log to both console and file simultaneously:

```python
Add a file handler to log to a file
logger.add_handler("application.log", level="DEBUG")
Now your logs will go to both console and file
logger.info("This message appears in both console and file")
```
## Logging Levels

The logger supports five standard logging levels:

- `logger.debug()` - Detailed information for debugging
- `logger.info()` - General information about program execution
- `logger.warning()` - Warning messages for potentially problematic situations
- `logger.error()` - Error messages for serious problems
- `logger.critical()` - Critical messages for critical problems that may prevent program execution

## Configuration

### Custom Handler Configuration

You can customize the logging handler with different parameters:

### Default Format

The default log format includes:
- Timestamp
- Log level
- Module name
- Function name
- Line number
- Message

Example output:

## Advanced Usage

### Custom Format Strings

You can customize the log format using these placeholders:
- `{time}` - Timestamp
- `{level}` - Log level
- `{name}` - Module name
- `{function}` - Function name
- `{line}` - Line number
- `{message}` - Log message

Example:

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by [Loguru](https://github.com/Delgan/loguru)
- Built on top of Python's standard logging module

## Support

If you encounter any problems or have suggestions, please open an issue on the GitHub repository.
