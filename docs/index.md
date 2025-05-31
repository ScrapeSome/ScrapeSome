# ScrapeSome

Welcome to the documentation for **ScrapeSome** — a modern, async/sync-capable web scraping library with smart fallbacks and HTML formatting.

![Scrapesome Logo](https://raw.githubusercontent.com/scrapesome/scrapesome/refs/heads/main/docs/assets/images/favicon.png)

**ScrapeSome** is a lightweight, flexible web scraping library with both **synchronous** and **asynchronous** support. It includes intelligent fallbacks, JavaScript page rendering, response formatting (HTML → Text/JSON/Markdown), and retry mechanisms. Ideal for developers who need robust scraping utilities with minimal setup.

---

## 💡 Why Use ScrapeSome?

- Handles both static and JS-heavy pages out of the box
- Supports both sync and async scraping
- Converts raw HTML into clean text, JSON, or Markdown
- Works with minimal configuration (`pip install scrapesome`)
- Handles timeouts, retries, redirects, user agents


## 🚀 Features

- 🔁 Sync + Async scraping support
- 🔄 Automatic retries and intelligent fallbacks
- 🧪 Playwright rendering fallback for JS-heavy pages
- 📝 Format responses as raw HTML, plain **text**, **Markdown**, or structured **JSON**
- ⚙️ Configurable: timeouts, redirects, user agents, and logging
- 🧪 Test coverage with `pytest` and `pytest-asyncio`

---

## ⚖ Comparison with Alternatives

| Feature                          | ScrapeSome ✅       | Scrapy              | Selenium/UC         | Playwright (Raw)     |
|----------------------------------|---------------------|---------------------|----------------------|----------------------|
| ✅ Sync + Async Scraping         | ✅ Built-in         | ❌ Async only*      | ❌ Manual            | ❌ Manual            |
| 🧠 JS Rendering (Fallback)       | ✅ Seamless         | ❌ Plugin setup     | ✅ Full              | ✅ Full              |
| 📝 Output as JSON/Markdown/HTML | ✅ Built-in         | ❌ Requires custom  | ❌ Manual parsing    | ❌ Manual parsing    |
| 🔁 Retry & Timeout Handling      | ✅ Built-in         | ⚠️ Requires config  | ❌ Manual            | ❌ Manual            |
| ⚡ Minimal Setup (Boilerplate)   | ✅ Near zero        | ❌ Needs project    | ❌ Driver setup      | ❌ Browser install   |
| 🧪 Testable out-of-the-box       | ✅ Pytest-ready     | ⚠️ Complex          | ❌                   | ❌                   |
| 🛠️ Config via .env or inline     | ✅ Simple           | ⚠️ Complex          | ❌                   | ❌                   |
| 📦 Install & Run in <1 Min       | ✅ Yes              | ❌                  | ❌                   | ❌                   |




## 📦 Installation

```bash
pip install scrapesome
```

## 🧪 Testing
Run tests with:

```bash
pytest --cov=scrapesome tests/
```
Target coverage: 75–100%

## 📁 Project Structure

```text
scrapesome/
├── .gitignore
├── pytest.ini
├── .github/
│   ├── workflows/
│   │   └── deploy.yml
│   ├── ISSUE_TEMPLATE/
│   │   └── index.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODE_OF_CONDUCT.md
│   └── SECURITY.md
├── __init__.py
├── cli.py
├── config.py
├── exceptions.py
├── formatter/
│   ├── __init__.py
│   └── output_formatter.py
├── logging.py
├── scraper/
│   ├── __init__.py
│   ├── async_scraper.py
│   ├── sync_scraper.py
│   └── rendering.py
├── docs/
│   ├── index.md
│   ├── getting_started.md
│   ├── usage.md
│   ├── config.md
│   ├── examples.md
│   ├── cli.md
│   ├── about.md
│   └── licence.md
├── tests/
│   ├── __init__.py
│   ├── test_sync_scraper.py
│   ├── test_async_scraper.py
│   └── test_config.py
├── setup.py
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── README.md
```

## 🔒 License
MIT License © 2025

### 📚 Documentation

- [Getting Started](getting-started.md)
- [Usage](usage.md)
- [Output Formats](output-formats.md)
- [Contribution](contribution.md)
- [CLI Usage](cli.md)
- [Configuration](config.md)
- [Examples](examples.md)
- [About / Contact](about.md)
- [License](licence.md)