
![Scrapesome Logo](https://raw.githubusercontent.com/scrapesome/scrapesome/refs/heads/main/docs/assets/images/favicon.png)

# ScrapeSome

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

## 🤝 Contributions

Contributions are welcome! Whether it's bug reports, feature suggestions, or pull requests — your help is appreciated.

To get started:

```bash
git clone https://github.com/scrapesome/scrapesome.git
cd scrapesome
```
