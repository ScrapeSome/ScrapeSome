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
    file: Optional[str] = typer.Option(None, "--url-file", "-uf", help="Path to file with URLs (one per line)."),
    async_mode: bool = typer.Option(False, "--async-mode", "-a", help="Enable asynchronous scraping."),
    force_playwright: bool = typer.Option(False, "--force-playwright", "-r", help="Use Playwright for JS rendering."),
    output_format: str = typer.Option("html", "--output-format", "-f", help="Output format: text, markdown, json, html."),
    output_file: Optional[str] = typer.Option(None, "--output-file", "-o", help="Save output to file."),
    user_agent: Optional[str] = typer.Option(None, "--user-agent", "-ua", help="Custom User-Agent."),
    headers: Optional[List[str]] = typer.Option(None, "--headers", "-H", help="Custom headers (key=value)."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging."),
):
    """
    Scrape one or more URLs with customizable options.
    """
    if not url and not file:
        typer.echo("❌ Please provide at least one URL or a file with URLs.")
        raise typer.Exit(code=1)

    if output_format not in VALID_FORMATS:
        typer.echo(f"❌ Invalid format '{output_format}'. Choose from: {', '.join(VALID_FORMATS)}")
        raise typer.Exit(code=1)

    urls = url or []
    if file:
        try:
            with open(file, "r") as f:
                urls.extend(line.strip() for line in f if line.strip())
        except Exception as e:
            typer.echo(f"❌ Could not read URL file: {e}")
            raise typer.Exit(code=1)

    headers_dict = parse_headers(headers) if headers else {}
    if user_agent:
        headers_dict["User-Agent"] = user_agent

    for u in urls:
        if verbose:
            typer.echo(f"🔍 Scraping: {u} [Async: {async_mode}, Format: {output_format}]")

        try:
            if async_mode:
                content = asyncio.run(
                    async_scraper(u, force_playwright=force_playwright, output_format_type=output_format, headers=headers_dict)
                )
            else:
                content = sync_scraper(u, force_playwright=force_playwright, output_format_type=output_format, headers=headers_dict)
        except Exception as e:
            typer.echo(f"❌ Error scraping {u}: {e}")
            continue

        if output_file:
            filename = output_file
            if len(urls) > 1:
                filename = f"{u.replace('https://', '').replace('http://', '').replace('/', '_')}.{output_format}"
            save_output(content, filename)
        else:
            typer.echo(content)
