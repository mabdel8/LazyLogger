from aisettings import logger

# Basic logging with different levels
logger.debug("Debug message: Detailed information for developers")
logger.info("Info message: Normal program operation")
logger.warning("Warning message: Something unexpected but not critical")
logger.error("Error message: Something failed")
logger.critical("Critical message: Serious failure")

# Add a file handler to log to a file
logger.add_handler("application.log", level="DEBUG")

# Now your logs will go to both console and file
logger.info("This message appears in both console and file")

# Define a custom format
custom_format = "{time} [{level}] - {message}"

# Add a new handler with custom format
logger.add_handler(
    "custom_formatted.log",
    level="DEBUG",
    format=custom_format
)

logger.info("This message will use the custom format") 