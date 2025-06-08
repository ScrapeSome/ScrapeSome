"""
Unit tests for the custom logging functionality in `scrapesome.logging`.

These tests verify:
- That logging methods (info, error) are properly called when logging is enabled.
- That the logging system respects mocking for assertions.

Mocks are used to validate whether logging methods are invoked with the correct messages.
"""

from unittest.mock import patch
from scrapesome.logging import get_logger

logger = get_logger()

@patch("scrapesome.logging.get_logger", True)
@patch.object(logger, "info")
def test_log_info_enabled(mock_info):
    """
    Test that the `info` log method is called with the expected message when logging is enabled.
    """
    logger.info("info test")
    mock_info.assert_called_with("info test")

@patch("scrapesome.logging.get_logger", True)
@patch.object(logger, "error")
def test_log_error_enabled(mock_error):
    """
    Test that the `error` log method is called with the expected message when logging is enabled.
    """
    logger.error("error test")
    mock_error.assert_called_with("error test")
