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

from typing import Optional, Union, Dict, List
from urllib.parse import urlparse, urljoin
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
    Extracts structured metadata and link information from raw HTML.

    This function parses the given HTML string and extracts key metadata such as 
    the page title, description, Open Graph tags, keywords, canonical URL, favicon, 
    main heading (H1), image sources, and categorized hyperlinks (internal/external).

    Args:
        html (str): Raw HTML content of the webpage.
        url (Optional[str]): The URL of the page (used for resolving relative links and 
                             determining internal/external links). Defaults to None.

    Returns:
        Dict[str, object]: A dictionary containing:
            - title (str): The content of the <title> tag.
            - description (str): Content of the <meta name="description"> tag.
            - og_title (str): Content of the <meta property="og:title"> tag.
            - og_description (str): Content of the <meta property="og:description"> tag.
            - keywords (str): Content of the <meta name="keywords"> tag.
            - canonical (str): URL from the <link rel="canonical"> tag.
            - favicon (str): URL of the favicon link.
            - h1 (str): Text content of the first <h1> tag.
            - url (str): Provided page URL or empty string if not given.
            - hrefs (List[str]): All hyperlink hrefs found in <a> tags.
            - internal_links (List[str]): Subset of hrefs pointing to the same domain.
            - external_links (List[str]): Subset of hrefs pointing to other domains.
            - images (List[str]): Sources (src) of all <img> tags found.
    """
    soup = BeautifulSoup(html, "html.parser")
    
    def get_meta_content(name=None, prop=None):
        if name:
            tag = soup.find("meta", attrs={"name": name})
        elif prop:
            tag = soup.find("meta", attrs={"property": prop})
        else:
            return ""
        return tag["content"].strip() if tag and tag.get("content") else ""

    def is_internal_link(href: str) -> bool:
        if not url:
            return href.startswith("/")
        parsed_base = urlparse(url)
        full_href = urljoin(url, href)
        return urlparse(full_href).netloc == parsed_base.netloc

    # Basic metadata
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    description = get_meta_content(name="description")
    og_title = get_meta_content(prop="og:title")
    og_description = get_meta_content(prop="og:description")
    keywords = get_meta_content(name="keywords")

    # Canonical URL
    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag["href"] if canonical_tag and canonical_tag.get("href") else ""

    # Favicon
    favicon_tag = soup.find("link", rel=lambda x: x and 'icon' in x.lower())
    favicon = favicon_tag["href"] if favicon_tag and favicon_tag.get("href") else ""

    # Hrefs
    all_hrefs = list(set([a.get("href") for a in soup.find_all("a", href=True)]))
    internal_links = list(set([href for href in all_hrefs if is_internal_link(href)]))
    external_links = list(set([href for href in all_hrefs if not is_internal_link(href)]))

    # Images
    images = list(set([img.get("src") for img in soup.find_all("img", src=True)]))

    return {
        "title": title,
        "description": description,
        "og_title": og_title,
        "og_description": og_description,
        "keywords": keywords,
        "canonical": canonical,
        "favicon": favicon,
        "url": url or "",
        "hrefs": all_hrefs,
        "internal_links": internal_links,
        "external_links": external_links,
        "images": images,
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
