
# Getting Started

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

For `Windows`
Playwright installs everything you need automatically with playwright install, so no additional setup is usually required.

For `Linux (Ubuntu/Debian)`
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

For `macOS`
You can install required libraries using Homebrew:

```bash
brew install harfbuzz enchant
```

After this setup, you should be able to use ScrapeSome with full Playwright rendering support!

## Sync Example

```python
from scrapesome import sync_scraper
html = sync_scraper("https://example.com")
html
```

## Async Example

```python
import asyncio
from scrapesome import async_scraper
html = asyncio.run(async_scraper("https://example.com"))
html
```