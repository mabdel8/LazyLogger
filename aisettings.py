import logging
import sys
from datetime import datetime
from typing import Optional, Union, TextIO

class SimpleLogger:
    """A simple logger inspired by Loguru's simplicity"""
    
    def __init__(self):
        # Create the logger
        self._logger = logging.getLogger("simple_logger")
        self._logger.setLevel(logging.DEBUG)
        
        # Default format
        self._default_format = "<green>{time}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
        
        # Initialize with stderr handler
        self.add_handler()
    
    def add_handler(self, 
                   sink: Optional[Union[str, TextIO]] = sys.stderr,
                   level: str = "DEBUG",
                   format: Optional[str] = None) -> None:
        """Add a logging handler (file or stream)"""
        
        # Create handler based on sink type
        if isinstance(sink, str):
            handler = logging.FileHandler(sink)
        else:
            handler = logging.StreamHandler(sink)
            
        # Set level
        handler.setLevel(getattr(logging, level))
        
        # Create formatter
        if format is None:
            format = self._default_format
            
        # Convert Loguru-style format to standard logging format
        format = (format.replace("{time}", "%(asctime)s")
                      .replace("{level}", "%(levelname)s")
                      .replace("{name}", "%(name)s")
                      .replace("{function}", "%(funcName)s")
                      .replace("{line}", "%(lineno)d")
                      .replace("{message}", "%(message)s"))
        
        formatter = logging.Formatter(format)
        handler.setFormatter(formatter)
        
        # Add handler to logger
        self._logger.addHandler(handler)
    
    def debug(self, message: str, *args, **kwargs) -> None:
        """Log debug message"""
        self._logger.debug(message, *args, **kwargs)
        
    def info(self, message: str, *args, **kwargs) -> None:
        """Log info message"""
        self._logger.info(message, *args, **kwargs)
        
    def warning(self, message: str, *args, **kwargs) -> None:
        """Log warning message"""
        self._logger.warning(message, *args, **kwargs)
        
    def error(self, message: str, *args, **kwargs) -> None:
        """Log error message"""
        self._logger.error(message, *args, **kwargs)
        
    def critical(self, message: str, *args, **kwargs) -> None:
        """Log critical message"""
        self._logger.critical(message, *args, **kwargs)

# Create a global logger instance
logger = SimpleLogger() 