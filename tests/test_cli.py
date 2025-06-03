"""
Test suite for ScrapeSome CLI.

This module contains test cases to verify the behavior of the ScrapeSome CLI,
particularly the `scrape` command. It tests validation, output formatting,
saving to file, and handling of async and sync scraping modes.

Uses pytest and typer's CliRunner for CLI testing.
"""

import os
import pytest
from typer.testing import CliRunner
from unittest.mock import patch, AsyncMock
from scrapesome.cli import app

runner = CliRunner()

# Sample scraped content to return from mocks
SAMPLE_CONTENT = {"data": "<html>sample content</html>"}


@pytest.mark.parametrize("args,expected_exit_code,expected_output_substring", [
    ([], 1, "Please provide at least one URL"),
    (["--url", "http://example.com", "--output-format", "invalid"], 1, "Invalid format"),
    (["--url", "http://example.com", "--save-to-file"], 1, "--file-name must be provided"),
    (["--url", "http://example.com", "--save-to-file", "--file-name", "output", "--output-format", "html"], 0, "✅ Output saved to output.html"),
])
def test_basic_validation_and_save(args, expected_exit_code, expected_output_substring):
    """
    Test the basic validation rules of the scrape command and saving output to a file.

    Validates that:
    - Providing no URL returns an error.
    - Invalid output format returns an error.
    - Specifying --save-to-file without --file-name returns an error.
    - Providing all required arguments results in successful save to file.
    """
    result = runner.invoke(app, ["scrape"] + args)
    assert result.exit_code == expected_exit_code
    assert expected_output_substring in result.output


@patch("scrapesome.cli.sync_scraper")
def test_sync_scraper_called(mock_sync_scraper):
    """
    Test that the synchronous scraper is called and that the scraped content
    is printed to stdout when async mode is not specified.
    """
    mock_sync_scraper.return_value = SAMPLE_CONTENT
    result = runner.invoke(app, ["scrape", "--url", "http://example.com"])
    assert result.exit_code == 0
    assert SAMPLE_CONTENT.get("data") in result.output
    mock_sync_scraper.assert_called_once()


@patch("scrapesome.cli.async_scraper", new_callable=AsyncMock)
def test_async_scraper_called(mock_async_scraper):
    """
    Test that the asynchronous scraper is called and that the scraped content
    is printed to stdout when async mode is specified.
    """
    mock_async_scraper.return_value = SAMPLE_CONTENT
    result = runner.invoke(app, ["scrape", "--url", "http://example.com", "--async-mode"])
    assert result.exit_code == 0
    assert SAMPLE_CONTENT.get("data") in result.output
    mock_async_scraper.assert_called_once()


@patch("scrapesome.cli.sync_scraper")
@patch("scrapesome.cli.save_output")
def test_save_to_file_calls_save_output(mock_save_output, mock_sync_scraper):
    """
    Test that the save_output function is called with correct arguments when
    --save-to-file and --file-name are provided.
    """
    mock_sync_scraper.return_value = SAMPLE_CONTENT
    result = runner.invoke(app, [
        "scrape", "--url", "http://example.com", "--save-to-file", "--file-name", "output"
    ])
    assert result.exit_code == 0
    mock_save_output.assert_called_once()
    args, kwargs = mock_save_output.call_args
    assert {"data":args[0]} == SAMPLE_CONTENT
    assert args[1] == "output.html"


@patch("scrapesome.cli.sync_scraper")
def test_verbose_logging_and_headers(mock_sync_scraper):
    """
    Test that verbose logging outputs scraping status, and headers including
    User-Agent and Accept are passed correctly to the scraper.
    """
    mock_sync_scraper.return_value = SAMPLE_CONTENT
    result = runner.invoke(app, [
        "scrape", "--url", "http://example.com", "--verbose",
        "--headers", "Accept=application/json",
        "--user-agent", "MyAgent/1.0"
    ])
    assert result.exit_code == 0
    assert "🔍 Scraping: http://example.com" in result.output
    called_headers = mock_sync_scraper.call_args.kwargs.get("headers")
    assert called_headers["User-Agent"] == "MyAgent/1.0"
    assert called_headers["Accept"] == "application/json"


@pytest.mark.parametrize("headers", [
    (["InvalidHeaderFormat"]),
    (["NoEqualSign"]),
])
def test_parse_headers_invalid_format(headers):
    """
    Test that parse_headers function raises an Exit exception when header
    strings are in invalid formats (missing '=' separator).
    """
    from scrapesome.cli import parse_headers
    from typer import Exit
    with pytest.raises(Exit):
        parse_headers(headers)
