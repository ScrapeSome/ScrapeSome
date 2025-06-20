"""
Asynchronous Scraper Module for Scrapesome
------------------------------------------

This module handles asynchronous HTTP scraping with user-agent rotation,
optional redirect following, and JavaScript rendering fallback via Playwright.

Features:
    - User-agent rotation with default and user-provided lists.
    - Optional HTTP redirect handling.
    - Automatic fallback to JS rendering if server returns 403 or minimal content.
    - Option to skip requests and use Playwright rendering directly.
    - Informative logging for each major step.
"""

from typing import List, Optional
import asyncio
import httpx
from scrapesome.logging import get_logger
from scrapesome.exceptions import ScraperError
from scrapesome.scraper.rendering import async_render_page
from scrapesome.formatter.output_formatter import format_response
from scrapesome.utils.file_writer import write
from scrapesome.config import Settings

settings = Settings()
logger = get_logger()


async def async_scraper(
    url: str,
    user_agents: Optional[List[str]] = None,
    headers: Optional[dict] = None,
    allow_redirects: bool = True,
    max_retries: int = 3,
    timeout: int = None,
    force_playwright: bool = False,
    output_format_type: Optional[str] = None,
    file_name: Optional[str] = None,
    save_to_file: Optional[bool] = False
) -> Optional[str]:
    """
    Scrape a URL asynchronously with retries, user-agent rotation,
    optional JS rendering fallback, and optional output formatting, file writing.

    Args:
        url (str): URL to fetch.
        user_agents (Optional[List[str]]): List of user agents to rotate. Defaults to built-in list.
        allow_redirects (bool): Whether to follow HTTP redirects.
        max_retries (int): Number of retry attempts on failure or 403 responses.
        timeout (int): HTTP request timeout in seconds.
        force_playwright (bool): If True, skip HTTP requests and use Playwright rendering directly.
        output_format_type (Optional[str]): Output format: 'text', 'json', 'markdown', or None for raw HTML.
        save_to_file (Optional): If True, creates file in local else no.

    Returns:
        Optional[str]: The formatted page content or None if an error occurred.
    """
    try:

        if not timeout:
            timeout = int(settings.fetch_page_timeout)
        if not user_agents:
            user_agents = settings.default_user_agents
        if not output_format_type:
            output_format_type = settings.default_output_format

        content = await fetch_url(
            url=url,
            user_agents=user_agents,
            headers=headers,
            allow_redirects=allow_redirects,
            max_retries=max_retries,
            timeout=timeout,
            force_playwright=force_playwright,
        )
        if output_format_type:
            content = format_response(html=content, url=url, output_format_type=output_format_type)
            if save_to_file:
                file_name = write(data=content, file_name=file_name, output_format_type=output_format_type)
        return {"data": content, "file": file_name}
    except Exception as e:
        logger.exception(e)
        return {"error":str(e)}


async def fetch_url(
    url: str,
    user_agents: Optional[List[str]],
    headers: Optional[dict],
    allow_redirects: bool,
    max_retries: int,
    timeout: Optional[int],
    force_playwright: bool,
) -> str:
    """
    Fetches the URL content asynchronously with user-agent rotation and optional JS rendering.

    Args:
        url (str): URL to fetch.
        user_agents (Optional[List[str]]): List of user agents to rotate. Defaults to built-in list.
        allow_redirects (bool): Follow HTTP redirects or not.
        max_retries (int): Number of retries with different user agents on failure (403).
        timeout (Optional[int]): Timeout in seconds for HTTP request. Defaults to settings.playwright_timeout.
        force_playwright (bool): If True, skip requests and use Playwright rendering directly.

    Returns:
        str: HTML content of the page or None if an error occurred.

    Raises:
        ScraperError: On failure after retries or rendering fallback.
    """
    if user_agents is None:
        user_agents = settings.default_user_agents
    if timeout is None:
        timeout = int(settings.fetch_page_timeout)

    if force_playwright:
        logger.info(f"Force Playwright rendering enabled for URL: {url}")
        try:
            return await async_render_page(url, timeout=int(settings.fetch_playwright_timeout))
        except Exception as e:
            logger.error(f"Playwright rendering failed for URL {url}: {e}")
            raise ScraperError(f"Failed to render {url} with Playwright") from e

    last_exception = None
    for attempt in range(max_retries):
        ua = user_agents[attempt % len(user_agents)]
        custom_headers = headers or {}
        ua_header = {"User-Agent": ua}
        headers = {**ua_header, **custom_headers}
        logger.info(f"Attempt {attempt + 1}/{max_retries} fetching {url} with User-Agent: {ua}")

        try:
            async with httpx.AsyncClient(follow_redirects=allow_redirects, timeout=timeout) as client:
                response = await client.get(url, headers=headers)

                status = response.status_code
                logger.info(f"Received response {status} for {url}")

                if status == 403:
                    logger.warning(f"403 Forbidden encountered with User-Agent: {ua}. Retrying with next user agent.")
                    last_exception = ScraperError(f"403 Forbidden for URL {url}")
                    await asyncio.sleep(1)  # polite delay before retry
                    continue

                response.raise_for_status()
                text = response.text

                if len(text.strip()) < 200:
                    logger.info(f"Content too short, attempting JS rendering for {url}")
                    try:
                        return await async_render_page(url, timeout=timeout)
                    except Exception as e:
                        logger.error(f"JS rendering fallback failed for {url}: {e}")
                        raise ScraperError(f"Failed JS rendering fallback for {url}") from e

                logger.info(f"Successfully fetched {url} without JS rendering.")
                return text

        except (httpx.RequestError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            logger.error(f"RequestException for {url} on attempt {attempt + 1}: {exc}")
            last_exception = exc
            await asyncio.sleep(1)  # polite delay before retry

    # After exhausting retries, fallback to Playwright rendering as last resort
    logger.info(f"Retries exhausted. Falling back to Playwright rendering for {url}")
    try:
        return await async_render_page(url, timeout=timeout)
    except Exception as e:
        logger.error(f"Playwright fallback failed for {url}: {e}")
        raise ScraperError(f"Failed to fetch or render {url}") from last_exception or e
