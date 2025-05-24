
# Getting Started

## Sync Example

```python
from scrapesome.scraper.sync_scraper import scraper
html = scraper("https://example.com")
html
```

## Async Example

```python
import asyncio
from scrapesome.scraper.async_scraper import scraper
html = asyncio.run(scraper("https://example.com"))
html
```