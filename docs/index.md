# 🕷️ ScrapeSome

Welcome to the documentation for **ScrapeSome** — a modern, async/sync-capable web scraping library with smart fallbacks and HTML formatting.

**ScrapeSome** is a lightweight, flexible web scraping library with both **synchronous** and **asynchronous** support. It includes intelligent fallbacks, JavaScript page rendering, response formatting (HTML → Text/JSON/Markdown), and retry mechanisms. Ideal for developers who need robust scraping utilities with minimal setup.

---

## 🚀 Features

- 🔁 Sync + Async scraping support
- 🔄 Automatic retries and intelligent fallbacks
- 🧪 Playwright rendering fallback for JS-heavy pages
- 📝 Format responses as raw HTML, plain **text**, **Markdown**, or structured **JSON**
- ⚙️ Configurable: timeouts, redirects, user agents, and logging
- 🧪 Test coverage with `pytest` and `pytest-asyncio`

---

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

```bash
scrapesome/
├── .gitignore
├── pytest.ini
├── .github/
│   ├── workflows/
│       └── deploy.yml
├── __init__.py
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