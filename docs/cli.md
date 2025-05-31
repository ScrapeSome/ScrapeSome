# 🖥️ CLI Usage Guide

ScrapeSome also includes a powerful convenient CLI for quick and easy scraping from the command line powered by [Typer](https://typer.tiangolo.com/) and configurable scraping directly from your terminal.

### 📦 Installation with CLI Support

To use the CLI, install with the optional `cli` extras:

```bash
pip install scrapesome[cli]
```

### 🔧 Basic Usage

```bash
scrapesome scrape --url https://example.com
```
This performs a synchronous scrape and outputs plain text by default.

### ⚙️ Available Options
| Option             | Description                               | Default |
|--------------------|-------------------------------------------|---------|
| `--async-mode`     | Use asynchronous scraping                  | False   |
| `--force-playwright`| Force JavaScript rendering using Playwright | False   |
| `--output-format`  | Choose `text`, `json`, `markdown`, or `html` | html    |


### Examples

#### Basic scrape
```bash
scrapesome scrape --url https://example.com
```

#### Force Playwright rendering
```bash
scrapesome scrape --url https://example.com --force-playwright
```

#### Get JSON output
```bash
scrapesome scrape --url https://example.com --output-format json
```

#### Async scrape with markdown output
```bash
scrapesome scrape --url https://example.com --async-mode --output-format markdown
```
