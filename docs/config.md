### ⚙️ Environment Configuration

**ScrapeSome** supports environment-based configuration via a `.env` file.

| Key                      | Description                                          |
|--------------------------|------------------------------------------------------|
| FETCH_PLAYWRIGHT_TIMEOUT | Timeout for Playwright-rendered pages (in seconds)  |
| FETCH_PAGE_TIMEOUT       | Timeout for standard page fetch (in seconds)        |
| LOG_LEVEL                | Logging verbosity (DEBUG, INFO, WARNING, etc.)      |
| OUTPUT_FORMAT            | Default output format (text, markdown, json, html)  |
| USER_AGENTS              | Default user agents ("Mozilla/5.0 (Windows NT 10.0; Win64; x64).......")  |

📁 Example `.env`:
```env
LOG_LEVEL=INFO
OUTPUT_FORMAT=text
FETCH_PLAYWRIGHT_TIMEOUT=10
FETCH_PAGE_TIMEOUT=10
USER_AGENTS=["Mozilla/5.0 (Windows NT 10.0; Win64; x64)......."]
```
