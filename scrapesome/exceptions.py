"""
Custom exceptions for Scrapesome library.

Defines specific error classes to represent common failure modes in scraping,
configuration, and runtime operations.
"""

class ScrapeSomeError(Exception):
    """
    Base exception class for Scrapesome library errors.
    """
    pass

class ConfigurationError(ScrapeSomeError):
    """
    Raised when there is a configuration problem,
    such as missing or invalid environment variables.
    """
    pass

class ScrapingError(ScrapeSomeError):
    """
    Raised when scraping fails due to network issues,
    invalid URLs, or unexpected content structure.
    """
    pass

class JavaScriptRenderingError(ScrapeSomeError):
    """
    Raised when a page requires JavaScript rendering but
    rendering via Playwright fails.
    """
    pass

class InvalidURLError(ScrapeSomeError):
    """
    Raised when the URL provided is invalid or malformed.
    """
    pass

class OutputFormatError(ScrapeSomeError):
    """
    Raised when an unsupported output format is requested.
    """
    pass

class ScraperError(ScrapeSomeError):
    """
    Raised when scraping fails due to network issues,
    invalid URLs, or unexpected content structure.
    """
    pass
