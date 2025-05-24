"""
Console logger setup for Scrapesome library.

Logs to console only, with configurable log level from Settings.
"""

import logging
from scrapesome.config import Settings

def get_logger() -> logging.Logger:
    """
    Creates and configures a logger instance.

    Returns:
        logging.Logger: Configured logger instance that outputs to console.

    Notes:
        - Respects the log level specified in settings.log_level.
        - Logs include timestamp, level, filename, line number, and message.
        - Prevents adding multiple handlers if called repeatedly for the same logger.
    """
    settings = Settings()
    logger = logging.getLogger()
    if logger.hasHandlers():
        return logger

    level = getattr(logging, settings.log_level.upper(), logging.INFO)
    logger.setLevel(level)


    formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    if level=="DEBUG":
        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )


    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
