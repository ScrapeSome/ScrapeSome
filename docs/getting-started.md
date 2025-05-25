
# Getting Started

## Sync Example

```python
from scrapesome.scraper.sync_scraper import sync_scraper
html = sync_scraper("https://example.com")
html
```

## Async Example

```python
import asyncio
from scrapesome.scraper.async_scraper import async_scraper
html = asyncio.run(async_scraper("https://example.com"))
html
```