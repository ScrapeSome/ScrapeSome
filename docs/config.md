### ⚙️ Environment Configuration

Scrapesome supports environment-based configuration via a `.env` file.

| Variable                 | Description                                          |
|--------------------------|------------------------------------------------------|
| FETCH_PLAYWRIGHT_TIMEOUT | Timeout for Playwright-rendered pages (in seconds)  |
| FETCH_PAGE_TIMEOUT       | Timeout for standard page fetch (in seconds)        |
| LOG_LEVEL                | Logging verbosity (DEBUG, INFO, WARNING, etc.)      |
| EXPORT_FORMAT            | Default export format (text, markdown, json, html)  |

📁 Example `.env`:
```env
FETCH_PLAYWRIGHT_TIMEOUT=20
FETCH_PAGE_TIMEOUT=10
LOG_LEVEL=INFO
EXPORT_FORMAT=text
```
