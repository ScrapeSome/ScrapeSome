"""
Response Formatting Module for Scrapesome
-----------------------------------------

This module provides utility functions to format HTML content fetched from web scraping
into various output formats such as plain text, JSON summary, or Markdown.

Features:
    - Default returns raw HTML.
    - Converts HTML to plain text by stripping tags.
    - Extracts key metadata as JSON (title, description, URL).
    - Converts HTML to Markdown using the markdownify library.

Usage:
    from scrapesome.scraper.formatter import format_response
"""

from typing import Optional, Union
from bs4 import BeautifulSoup
import markdownify


def get_text(html: str) -> str:
    """
    Converts HTML content to plain text by stripping all tags.

    Args:
        html (str): Raw HTML content.

    Returns:
        str: Plain text extracted from HTML.
    """
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)


def get_json(html: str, url: Optional[str] = None) -> dict:
    """
    Extracts key metadata from HTML content and returns it as a JSON-like dictionary.

    Args:
        html (str): Raw HTML content.
        url (Optional[str]): URL of the page (optional).

    Returns:
        dict: Dictionary containing title, description, and URL.
    """
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    description_tag = soup.find("meta", attrs={"name": "description"})
    description = description_tag["content"].strip() if description_tag and description_tag.get("content") else ""
    return {
        "title": title,
        "description": description,
        "url": url or ""
    }


def get_markdown(html: str) -> str:
    """
    Converts HTML content to Markdown format.

    Args:
        html (str): Raw HTML content.

    Returns:
        str: Markdown formatted text.
    """
    return markdownify.markdownify(html, heading_style="ATX")


def format_response(
    html: str, 
    url: Optional[str] = None, 
    output_format_type: Optional[str] = None
) -> Union[str, dict]:
    """
    Formats the HTML response content based on output_format_type.

    Args:
        html (str): Raw HTML content.
        url (Optional[str]): URL of the page (used in JSON output).
        output_format_type (Optional[str]): One of None, "text", "json", or "markdown".

    Returns:
        Union[str, dict]: Formatted output as raw HTML, plain text, markdown, or dict.
    """
    if output_format_type is None:
        return html

    if output_format_type == "text":
        return get_text(html)

    if output_format_type == "json":
        return get_json(html, url)

    if output_format_type == "markdown":
        return get_markdown(html)

    # Fallback: unknown output_format_type returns raw HTML
    return html
