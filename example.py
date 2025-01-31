from aisettings import logger

# Basic usage
logger.info("Hello from Simple Logger!")
logger.debug("This is a debug message")
logger.warning("Warning: something might be wrong")
logger.error("An error occurred")

# Add a file handler
logger.add_handler("app.log", level="DEBUG")

# Log to both console and file
logger.info("This message goes to both console and file") 