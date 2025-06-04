"""
CLI for ScrapeSome - A simple, powerful web scraping utility.

Features:
- Sync and async scraping
- JavaScript rendering via Playwright
- Markdown, JSON, HTML, and text output formats
- File output, custom headers, verbose logging
- Support for batch scraping (via file)
"""

import asyncio
import typer
import json
from typing import Optional, List
from scrapesome import sync_scraper, async_scraper
from scrapesome.config import Settings

settings = Settings()

app = typer.Typer(help="ScrapeSome CLI - Web scraping with ease.")

VALID_FORMATS = ["text", "markdown", "json", "html"]


def parse_headers(header_list: List[str]) -> dict:
    headers = {}
    for header in header_list:
        if "=" not in header:
            typer.echo(f"❌ Invalid header format: {header}. Expected key=value.")
            raise typer.Exit(code=1)
        key, value = header.split("=", 1)
        headers[key.strip()] = value.strip()
    return headers


def save_output(output: str, file_path: str):
    try:
        if not isinstance(output,str):
            output = str(output)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output)
        typer.echo(f"✅ Output saved to {file_path}")
    except Exception as e:
        typer.echo(f"❌ Failed to write output file: {e}")
        raise typer.Exit(code=1)


@app.command()
def scrape(
    scrape: Optional[str] = typer.Argument(None, help="scraper."),
    url: Optional[List[str]] = typer.Option(None, "--url", "-url", help="URL(s) to scrape."),
    async_mode: bool = typer.Option(False, "--async-mode", "-a", help="Enable asynchronous scraping."),
    force_playwright: bool = typer.Option(False, "--force-playwright", "-r", help="Use Playwright for JS rendering."),
    output_format_type: str = typer.Option("html", "--output-format", "-f", help="Output format: text, markdown, json, html."),
    save_to_file: bool = typer.Option(False, "--save-to-file", "-s", help="Save output to file."),
    file_name: Optional[str] = typer.Option(None, "--file-name", "-n", help="Name of the output file."),
    user_agent: Optional[str] = typer.Option(None, "--user-agent", "-ua", help="Custom User-Agent."),
    headers: Optional[List[str]] = typer.Option(None, "--headers", "-H", help="Custom headers (key=value)."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging."),
):
    """
    Scrape one or more URLs with customizable options.
    """
    if not url:
        typer.echo("❌ Please provide at least one URL")
        raise typer.Exit(code=1)

    if output_format_type not in VALID_FORMATS:
        typer.echo(f"❌ Invalid format '{output_format_type}'. Choose from: {', '.join(VALID_FORMATS)}")
        raise typer.Exit(code=1)

    urls = url if url else []

    headers_dict = parse_headers(headers) if headers else {}
    if user_agent:
        headers_dict["User-Agent"] = user_agent

    if save_to_file:
        if not file_name:
            typer.echo("❌ --file-name must be provided when using --save-to-file.")
            raise typer.Exit(code=1)
        if len(urls) > 1:
            typer.echo("❌ Currently not supporting multiple URLS so cannot save multiple URLs to a single file. Provide one URL or disable --save-to-file.")
            raise typer.Exit(code=1)

    for url in urls:
        if verbose:
            typer.echo(f"🔍 Scraping: {url} [Async: {async_mode}, Format: {output_format_type}]")

        try:
            if async_mode:
                content = asyncio.run(
                    async_scraper(url, force_playwright=force_playwright, output_format_type=output_format_type, headers=headers_dict)
                )
            else:
                content = sync_scraper(url, force_playwright=force_playwright, output_format_type=output_format_type, headers=headers_dict)
        except Exception as e:
            typer.echo(f"❌ Error scraping {url}: {e}")
            continue

        if isinstance(content, dict):
            content = content.get("data", "")

        if save_to_file:
            file_extensions = settings.file_extensions
            filename_with_ext = f"{file_name}.{file_extensions.get(output_format_type,'')}"
            save_output(content, filename_with_ext)
        else:
            typer.echo(content)
