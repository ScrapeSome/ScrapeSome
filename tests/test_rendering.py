"""
test_rendering.py

Test suite for the Scrapesome JavaScript rendering module (rendering.py).

This suite covers both synchronous and asynchronous rendering functions,
including:
  - Successful page rendering
  - Timeout fallback behavior (networkidle -> domcontentloaded)
  - Request blocking logic (images, ads)
  - Proper exception handling and ScraperError raising

Mocks Playwright browser, context, page objects to avoid real browser interaction.
"""

import pytest
import asyncio
from unittest.mock import patch, AsyncMock, MagicMock
from scrapesome.scraper import rendering
from scrapesome.exceptions import ScraperError


@pytest.mark.parametrize("resource_type,url,expected", [
    ("image", "https://example.com/some.jpg", True),
    ("media", "https://example.com/video.mp4", True),
    ("font", "https://example.com/font.woff", True),
    ("script", "https://example.com/ads.js", True),
    ("script", "https://example.com/scripts/main.js", False),
    ("document", "https://example.com/", False),
])
def test_should_block(resource_type, url, expected):
    """Test the _should_block helper blocks expected resources/urls."""
    result = rendering._should_block(url, resource_type)
    assert result is expected


@patch("scrapesome.scraper.rendering.sync_playwright")
def test_sync_render_page_success(mock_sync_playwright):
    """Test sync_render_page returns content successfully."""
    mock_browser = MagicMock()
    mock_context = MagicMock()
    mock_page = MagicMock()

    mock_sync_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page
    mock_page.content.return_value = "<html>mocked content</html>"

    # Simulate page.goto succeeds on first try
    mock_page.goto.return_value = None

    url = "https://example.com"
    content = rendering.sync_render_page(url, timeout=1)

    assert content == "<html>mocked content</html>"
    mock_page.goto.assert_called_with(url, wait_until="networkidle", timeout=1000)
    mock_browser.close.assert_called_once()

@pytest.mark.asyncio
@patch("scrapesome.scraper.rendering.async_playwright")
async def test_async_render_page_timeout_fallback(mock_async_playwright):
    """Test async_render_page timeout fallback."""
    mock_browser = AsyncMock()
    mock_context = AsyncMock()
    mock_page = AsyncMock()

    mock_async_playwright.return_value.__aenter__.return_value.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page
    mock_page.content.return_value = "<html>async fallback content</html>"

    # Import TimeoutError from your module under test to match the caught exception
    AsyncTimeoutError = rendering.AsyncTimeoutError

    async def goto_side_effect(*args, **kwargs):
        if goto_side_effect.call_count == 0:
            goto_side_effect.call_count += 1
            raise AsyncTimeoutError("Timeout error")
        return None
    goto_side_effect.call_count = 0
    mock_page.goto.side_effect = goto_side_effect

    url = "https://example.com"
    content = await rendering.async_render_page(url, timeout=1)

    assert content == "<html>async fallback content</html>"
    assert mock_page.goto.call_count == 2
    mock_page.goto.assert_any_call(url, wait_until="networkidle", timeout=1000)
    mock_page.goto.assert_any_call(url, wait_until="domcontentloaded", timeout=1000)
    mock_browser.close.assert_awaited()


@patch("scrapesome.scraper.rendering.sync_playwright")
def test_sync_render_page_timeout_fallback(mock_sync_playwright):
    """Test sync_render_page timeout fallback."""
    mock_browser = MagicMock()
    mock_context = MagicMock()
    mock_page = MagicMock()

    mock_sync_playwright.return_value.__enter__.return_value.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page
    mock_page.content.return_value = "<html>fallback content</html>"

    SyncTimeoutError = rendering.SyncTimeoutError

    # Pass message argument to TimeoutError constructor to avoid TypeError
    mock_page.goto.side_effect = [SyncTimeoutError("Timeout error"), None]

    url = "https://example.com"
    content = rendering.sync_render_page(url, timeout=1)

    assert content == "<html>fallback content</html>"
    assert mock_page.goto.call_count == 2
    mock_page.goto.assert_any_call(url, wait_until="networkidle", timeout=1000)
    mock_page.goto.assert_any_call(url, wait_until="domcontentloaded", timeout=1000)
    mock_browser.close.assert_called_once()

@patch("scrapesome.scraper.rendering.sync_playwright")
def test_sync_render_page_raises_scraper_error_on_exception(mock_sync_playwright):
    """Test sync_render_page raises ScraperError on unexpected exception."""
    mock_sync_playwright.return_value.__enter__.return_value.chromium.launch.side_effect = RuntimeError("fail launch")

    with pytest.raises(ScraperError):
        rendering.sync_render_page("https://example.com", timeout=1)


@pytest.mark.asyncio
@patch("scrapesome.scraper.rendering.async_playwright")
async def test_async_render_page_success(mock_async_playwright):
    """Test async_render_page returns content successfully."""
    mock_browser = AsyncMock()
    mock_context = AsyncMock()
    mock_page = AsyncMock()

    mock_async_playwright.return_value.__aenter__.return_value.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page
    mock_page.content.return_value = "<html>async mocked content</html>"

    # Simulate page.goto succeeds on first try
    mock_page.goto.return_value = asyncio.Future()
    mock_page.goto.return_value.set_result(None)

    url = "https://example.com"
    content = await rendering.async_render_page(url, timeout=1)

    assert content == "<html>async mocked content</html>"
    mock_page.goto.assert_called_with(url, wait_until="networkidle", timeout=1000)
    mock_browser.close.assert_awaited()

@pytest.mark.asyncio
@patch("scrapesome.scraper.rendering.async_playwright")
async def test_async_render_page_raises_scraper_error_on_exception(mock_async_playwright):
    """Test async_render_page raises ScraperError on unexpected exception."""
    mock_async_playwright.return_value.__aenter__.return_value.chromium.launch.side_effect = RuntimeError("fail launch")

    with pytest.raises(ScraperError):
        await rendering.async_render_page("https://example.com", timeout=1)
