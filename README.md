# ScrapeSome

![Scrapesome Logo](https://raw.githubusercontent.com/scrapesome/scrapesome/refs/heads/main/docs/assets/images/favicon.png)


![PyPI](https://img.shields.io/pypi/v/scrapesome)
![Python](https://img.shields.io/pypi/pyversions/scrapesome)
![Downloads](https://img.shields.io/pypi/dm/scrapesome)
![License](https://img.shields.io/github/license/scrapesome/scrapesome)
![Build Status](https://github.com/scrapesome/scrapesome/actions/workflows/deploy.yml/badge.svg)
![Issues](https://img.shields.io/github/issues/scrapesome/scrapesome)
![Discussions](https://img.shields.io/github/discussions/scrapesome/scrapesome)
![Contributors](https://img.shields.io/github/contributors/scrapesome/scrapesome)
![Forks](https://img.shields.io/github/forks/scrapesome/scrapesome)
![Stars](https://img.shields.io/github/stars/scrapesome/scrapesome)



**ScrapeSome** is a lightweight, flexible web scraping library with both **synchronous** and **asynchronous** support. It includes intelligent fallbacks, JavaScript page rendering, response formatting (HTML → Text/JSON/Markdown), and retry mechanisms. Ideal for developers who need robust scraping utilities with minimal setup.

---

## Table of Contents

- [💡 Why Use ScrapeSome?](#-why-use-scrapesome)
- [🚀 Features](#-features)
- [⚖ Comparison with Alternatives](#-comparison-with-alternatives)
- [📦 Installation](#-installation)
- [Playwright Setup](#playwright-setup)
  - [Windows](#windows)
  - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
  - [macOS](#macos)
- [⚡ Quick Start](#-quick-start)
- [🖥️ CLI Usage](#-cli-usage)
- [🧰 Advanced Usage](#-advanced-usage)
- [🧪 Testing](#-testing)
- [⚙️ Environment Configuration](#️-environment-configuration)
- [📄 Output Formats](#-output-formats)
- [📁 Project Structure](#-project-structure)
- [🔒 License](#-license)
- [🤝 Contributions](#-contributions)


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

| Feature                          | ScrapeSome ✅                         | Playwright (Python)        | Selenium + UC               | Requests-HTML              | Scrapy + Playwright         |
|----------------------------------|--------------------------------------|-----------------------------|------------------------------|-----------------------------|------------------------------|
| 🧠 JS Rendering Support          | ✅ Auto fallback on 403/JS content    | ✅ Always (manual control)  | ✅ Always (manual control)   | ✅ Partial (via Pyppeteer)  | ✅ Requires setup            |
| 🔄 Automatic Fallback (403/Blank)| ✅ Yes (seamless)                     | ❌ Manual logic needed       | ❌ Manual logic needed        | ❌ No                       | ❌ Needs per-request config  |
| 🔁 Uses Browser Engine           | ✅ Only when needed (Playwright)      | ✅ Always                   | ✅ Always                    | ✅ (Unstable, slow)         | ✅ Always (if enabled)       |
| ✅ Sync + Async Support         | ✅ Built-in                           | ❌ Async only               | ❌ Manual (via threading)    | ❌ Sync only                | ❌ Async only (via plugin)   |
| 📝 JSON/Markdown/HTML Output    | ✅ Built-in formats                   | ❌ Manual parsing           | ❌ Manual parsing            | ❌ Basic only               | ❌ Custom pipeline needed    |
| ⚡ Minimal Setup                 | ✅ Near zero                          | ❌ Code + browser install   | ❌ Driver + setup            | ✅ Simple pip install       | ❌ Complex + plugin setup    |
| 🔁 Retries, Timeouts, Agents    | ✅ Smart defaults built-in            | ❌ Manual handling          | ❌ Manual handling           | ❌ Limited                  | ⚠️ Partial via settings      |
| 🧪 Pytest-Ready Out-of-the-box  | ✅ Fully testable                     | ⚠️ Requires mocks           | ❌ Hard to test              | ❌ Minimal                  | ⚠️ Needs testing harness     |
| ⚙️ Config via .env / Inline     | ✅ Flexible and optional              | ❌ Code/config only         | ❌ Manual via code           | ❌ Hardcoded mostly         | ⚠️ Project settings          |
| 📦 Install & Run in <1 Min      | ✅ Yes                                | ❌ Setup required           | ❌ Driver + config needed    | ✅ Yes                      | ❌ Needs project + plugin    |




## 📦 Installation

```bash
pip install scrapesome
```


## Playwright Setup

ScrapeSome uses Playwright for JavaScript rendering fallback. To enable this, you need to install Playwright and its dependencies.

### 1. Install Playwright Python package if not installed

```bash
pip install playwright
```

### 2. Install Playwright browsers

```bash
playwright install
```
### 3. Install system dependencies
Playwright requires some system libraries to run browsers, which vary by operating system.

For Windows
Playwright installs everything you need automatically with playwright install, so no additional setup is usually required.

For Linux (Ubuntu/Debian)
Run the following command to install required system libraries:

```bash
playwright install-deps
```
If you don't have playwright CLI available, you can install dependencies manually:

```bash
sudo apt-get update
sudo apt-get install -y libwoff1 libopus0 libwebp6 libharfbuzz-icu0 libwebpmux3 \
                        libenchant-2-2 libhyphen0 libegl1 libglx0 libgudev-1.0-0 \
                        libevdev2 libgles2 libx264-160
```
Note: Package names may vary depending on your distribution and version.

For macOS
You can install required libraries using Homebrew:

```bash
brew install harfbuzz enchant
```

After this setup, you should be able to use ScrapeSome with full Playwright rendering support!

## ⚡ Quick Start
Synchronous Example

```python
from scrapesome import sync_scraper
html = sync_scraper("https://example.com")
html
```


Asynchronous Example

```python
import asyncio
from scrapesome import async_scraper
html = asyncio.run(async_scraper("https://example.com"))
html
```
## 🖥️ CLI Usage

ScrapeSome also includes a powerful CLI for quick and easy scraping from the command line.

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

## 📄 File Saving

ScrapeSome allows you to format and save your scraped content with zero hassle—both via the **CLI** and in **Python code**.

---

### 💻 Save Output to File

Use these flags to save your output directly from the command line:

- `--save-to-file` or `-s`: Enable saving to a file
- `--file-name` or `-n`: Desired filename (extension added automatically)
- `--output-format` or `-f`: One of `html`, `text`, `markdown`, or `json`

⚠️ **Note:** When saving to a file, only one URL can be scraped at a time.

#### 📦 Example:

```bash
scrapesome scrape "https://example.com" \
  --output-format markdown \
  --save-to-file \
  --file-name output
```

👉 This saves the result as `output.md`.

---

### Save Output in Code

The `sync_scraper` function supports saving to file using two optional flags:

- `save_to_file=True`: Enables saving
- `file_name="your_file_name"`: Sets the base filename (extension inferred from format)

The output will be returned as a dictionary:

```bash
{
    "data": "<formatted content>",
    "file": "your_file_name.<ext>"  # if saving is enabled
}
```

#### 📌 Example:

```python
result = sync_scraper(
    url="https://example.com",
    output_format_type="json",
    save_to_file=True,
    file_name="example_output"
)
print(f"Saved output to {result['file']}")
```

Now you're set to save clean, readable data in your preferred format—programmatically or from the CLI.

## 🧰 Advanced Usage

Force Rendering (Playwright)

```python
from scrapesome import sync_scraper
content = sync_scraper("https://example.com", force_playwright=True)
content
```

Custom User Agents

```python
from scrapesome import sync_scraper
content = sync_scraper("https://example.com", user_agents=["MyCustomAgent/1.0"])
content
```

Control Redirects

```python
from scrapesome import sync_scraper
content = sync_scraper("https://example.com", allow_redirects=False)
content
```

similarly **async_scraper** can also be used.

## 🧪 Testing
Run tests with:

```bash
pytest --cov=scrapesome tests/
```
Target coverage: 75–100%

## ⚙️ Environment Configuration
ScrapeSome reads from environment variables if a .env file is present.

Example .env

```env
LOG_LEVEL=INFO
OUTPUT_FORMAT=text
FETCH_PLAYWRIGHT_TIMEOUT=10
FETCH_PAGE_TIMEOUT=10
USER_AGENTS=["Mozilla/5.0 (Windows NT 10.0; Win64; x64)......."]
```

| Key                      | Description                                          |
|--------------------------|------------------------------------------------------|
| FETCH_PLAYWRIGHT_TIMEOUT | Timeout for Playwright-rendered pages (in seconds)  |
| FETCH_PAGE_TIMEOUT       | Timeout for standard page fetch (in seconds)        |
| LOG_LEVEL                | Logging verbosity (DEBUG, INFO, WARNING, etc.)      |
| OUTPUT_FORMAT            | Default output format (text, markdown, json, html)  |
| USER_AGENTS              | Default user agents ("Mozilla/5.0 (Windows NT 10.0; Win64; x64).......")  |

## 📄 Output Formats

JSON Example

Get `json` version

```python
from scrapesome import sync_scraper
content = sync_scraper("https://example.com", output_format_type="json")
content
```

Output

```json
{
  "title": "Example Domain",
  "description": "This domain is for use in illustrative examples.",
  "url": "https://example.com"
}
```

## Markdown

Convert HTML to Markdown with:

```python
from scrapesome import sync_scraper
content = sync_scraper("https://adenuniversity.us", output_format_type="markdown")
content
```
Output

```text
# Online Global Masters that boost your global career

**ADEN University** offers students access to professionals who operate in the world of business and administration, who share their knowledge and acumen collaboratively with their students in all **academic programs** offered at ADEN.

[About Us](about-aden-university)


Watch testimonial video 


##### Watch testimonial video

×

[

](https://res.cloudinary.com/cruminott/video/upload/vc_auto,w_auto,q_auto,f_auto/adenu/aden-university-3.mp4)



## ADEN University offers the following academic programs

[![EXECUTIVE MBA. Master of Business Administration](https://adenuniversity.us/files/2016/06/ADENU_miniatura_Emba_900-1-820x400.jpg "EXECUTIVE MBA. Master of Business Administration")](https://adenuniversity.us/academics/executive-mba/  "EXECUTIVE MBA. Master of Business Administration")

##### [EXECUTIVE MBA. Master of Business Administration](https://adenuniversity.us/academics/executive-mba/ "EXECUTIVE MBA. Master of Business Administration")

The ADEN University Executive MBA is designed to strengthen business leaders to manage...

* **37** credits
* **15** months
* **Spanish Only**

[Visit EMBA Course](https://adenuniversity.us/academics/executive-mba/ "EXECUTIVE MBA. Master of Business Administration")

[![GLOBAL MBA. Master of Business Administration](https://adenuniversity.us/files/2016/06/ADENU_miniatura_MBAgl1_900-820x400.jpg "GLOBAL MBA. Master of Business Administration")](https://adenuniversity.us/academics/global-mba/  "GLOBAL MBA. Master of Business Administration")

##### [GLOBAL MBA. Master of Business Administration](https://adenuniversity.us/academics/global-mba/ "GLOBAL MBA. Master of Business Administration")

The Global MBA is designed to prepare business leaders to manage companies in an...

* **36** credits
* **14** months
* **Spanish and English**
```

similarly **async_scraper** can also be used.

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

## 🤝 Contributions

Contributions are welcome! Whether it's bug reports, feature suggestions, or pull requests — your help is appreciated.

To get started:

```bash
git clone https://github.com/scrapesome/scrapesome.git
cd scrapesome
```

## Documentation & Community

- [Contributing Guidelines](./docs/contribution.md)
- [Code of Conduct](.github/CODEOFCONDUCT.md)
- [Issue Templates](.github/issue_templates/index.md)
- [Pull Request Templates](.github/pull_request_template.md)
- [GitHub Discussions](https://github.com/scrapesome/scrapesome/discussions)
