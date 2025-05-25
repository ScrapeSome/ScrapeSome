"""
JavaScript Rendering Module for Scrapesome
------------------------------------------

This module provides functions to render JavaScript-heavy web pages using Playwright.
It supports both synchronous and asynchronous rendering modes.

Features:
    - Renders pages that require JavaScript execution.
    - Falls back from 'networkidle' to 'domcontentloaded' if initial wait fails.
    - Blocks images and known ad providers to reduce bandwidth and speed up rendering.
    - Supports custom headers and timeout configuration.

Usage:
    from scrapesome.scraper.rendering import sync_render_page, async_render_page
"""

import random
from typing import Optional, List
from playwright.sync_api import sync_playwright, TimeoutError as SyncTimeoutError
from playwright.async_api import async_playwright, TimeoutError as AsyncTimeoutError
from scrapesome.logging import get_logger
from scrapesome.config import Settings
from scrapesome.exceptions import ScraperError

settings = Settings()
logger = get_logger()


def _should_block(request_url: str, resource_type: str) -> bool:
    """
    Helper to decide whether a request should be blocked.

    Args:
        request_url (str): The URL of the request.
        resource_type (str): The type of resource being requested.

    Returns:
        bool: True if request should be blocked, False otherwise.
    """
    blocked_resources = {"image", "media", "font"}
    return resource_type in blocked_resources or "ads" in request_url


def sync_render_page(url: str, headers: Optional[dict] = None, timeout: int = int(settings.fetch_playwright_timeout), user_agents: Optional[List[str]] = None) -> str:
    """
    Renders the given URL using synchronous Playwright with headless Chromium.

    Args:
        url (str): URL to render.
        headers (Optional[dict]): Optional request headers.
        timeout (int): Timeout in seconds for page load.

    Returns:
        str: Rendered HTML content of the page.

    Raises:
        ScraperError: If page rendering fails.
    """
    browser = None
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            
            context_args = {}
            context_args["java_script_enabled"] = True
            if user_agents:
                context_args["user_agent"] = random.choice(user_agents)
            

            context = browser.new_context(user_agent=context_args["user_agent"], java_script_enabled=context_args["java_script_enabled"])

            # Block images and ads for performance
            context.route("**/*", lambda route, request: route.abort()
                          if _should_block(request.url, request.resource_type)
                          else route.continue_())

            page = context.new_page()
            if headers:
                page.set_extra_http_headers(headers)

            try:
                page.goto(url, wait_until="networkidle", timeout=timeout * 1000)
            except SyncTimeoutError:
                logger.warning(f"Timeout with 'networkidle'. Retrying with 'domcontentloaded' for {url}")
                page.goto(url, wait_until="domcontentloaded", timeout=timeout * 1000)

            content = page.content()
            logger.info(f"Synchronous JS rendering completed for: {url}")
            return content

    except Exception as e:
        logger.exception(e)
        logger.error(f"Playwright sync rendering failed for {url}: {e}")
        raise ScraperError(f"Sync rendering failed for {url}") from e

    finally:
        if browser:
            try:
                browser.close()
            except Exception:
                pass


async def async_render_page(url: str, headers: Optional[dict] = None, timeout: int = int(settings.fetch_playwright_timeout), user_agents: Optional[List[str]] = None) -> str:
    """
    Renders the given URL using asynchronous Playwright with headless Chromium.

    Args:
        url (str): URL to render.
        headers (Optional[dict]): Optional request headers.
        timeout (int): Timeout in seconds for page load.

    Returns:
        str: Rendered HTML content of the page.

    Raises:
        ScraperError: If page rendering fails.
    """
    browser = None
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context_args = {}
            context_args["java_script_enabled"] = True
            if user_agents:
                context_args["user_agent"] = random.choice(user_agents)
            

            context = browser.new_context(user_agent=context_args["user_agent"], java_script_enabled=context_args["java_script_enabled"])


            # Block images and ads for performance
            await context.route("**/*", lambda route, request: route.abort()
                                if _should_block(request.url, request.resource_type)
                                else route.continue_())

            page = await context.new_page()
            if headers:
                await page.set_extra_http_headers(headers)

            try:
                await page.goto(url, wait_until="networkidle", timeout=timeout * 1000)
            except AsyncTimeoutError:
                logger.warning(f"Timeout with 'networkidle'. Retrying with 'domcontentloaded' for {url}")
                await page.goto(url, wait_until="domcontentloaded", timeout=timeout * 1000)

            content = await page.content()
            logger.info(f"Asynchronous JS rendering completed for: {url}")
            return content

    except Exception as e:
        logger.exception(e)
        logger.error(f"Playwright async rendering failed for {url}: {e}")
        raise ScraperError(f"Async rendering failed for {url}") from e

    finally:
        if browser:
            try:
                await browser.close()
            except Exception:
                pass
