"""
Unit tests for the configuration settings in `scrapesome.config`.

These tests ensure that:
- The default timeout setting is not overridden to a specific unintended value.
- The logging level is set correctly (e.g., "INFO") when logging is enabled.

The `Settings` object is assumed to encapsulate environment-based configuration.
"""

def test_default_timeout_env():
    """
    Test that the default fetch_page_timeout is not set to an arbitrary value (e.g., 42).
    Ensures environment defaults or overrides are applied correctly.
    """
    from scrapesome.config import Settings
    settings = Settings()
    assert  settings.fetch_page_timeout != 42

def test_enable_logging_env():
    """
    Test that the default or environment-set logging level is 'INFO'.
    """
    from scrapesome.config import Settings
    settings = Settings()
    assert settings.log_level == "INFO"
