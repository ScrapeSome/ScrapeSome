
from unittest.mock import patch
from scrapesome.logging import get_logger

logger = get_logger()

@patch("scrapesome.logging.get_logger", True)
@patch.object(logger, "info")
def test_log_info_enabled(mock_info):
    logger.info("info test")
    mock_info.assert_called_with("info test")

@patch("scrapesome.logging.get_logger", True)
@patch.object(logger, "error")
def test_log_error_enabled(mock_error):
    logger.error("error test")
    mock_error.assert_called_with("error test")
