
# Getting Started

## Sync Example

```python
from scrapesome.scraper import scraper
html = scraper("https://example.com")
```

## Async Example

```python
import asyncio
from scrapesome.scraper import async_scraper
html = asyncio.run(async_scraper("https://example.com"))
```