"""
Environment configuration loader for the Scrapesome application.

This module defines a `Settings` class that loads all required environment
variables at startup and makes them available as attributes.

Raises:
    EnvironmentError: If a required environment variable is missing.
"""

import os
import logging

class Settings:
    """
    Loads and stores all required environment variables for the application.
    """

    def __init__(self) -> None:
        # APP Configuration
        self.log_level = self._get("LOG_LEVEL", default="INFO")

        #⚙️ Scraper Behavior Settings
        self.max_workers = self._get("MAX_WORKERS", default="1")

        #📤 Output Format Defaults
        self.default_export_format = self._get("EXPORT_FORMAT", default="text")

        self.fetch_playwright_timeout = self._get("FETCH_PLAYWRIGHT_TIMEOUT", default="60000")
        self.fetch_page_timeout = self._get("FETCH_PAGE_TIMEOUT", default="60000")


    def _get(self, key: str, default: str | None = None) -> str:
        """
        Retrieve an environment variable, or raise an error if missing and no default is provided.

        Args:
            key (str): The name of the environment variable.
            default (Optional[str]): Default value if the variable is not set.

        Returns:
            str: The value of the environment variable.

        Raises:
            EnvironmentError: If the variable is not set and no default is provided.
        """
        value = os.getenv(key)
        if value is None:
            if default is not None:
                # logging.warning("[Config] Environment variable '%s' not set, using default: '%s'", key, default)
                return default
            raise EnvironmentError(f"Missing required environment variable: '{key}'")
        return value
