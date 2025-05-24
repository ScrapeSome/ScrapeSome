
## Sync Examples

```python
from scrapesome.scraper.sync_scraper import scraper

if __name__ == "__main__":
    url = "https://adenuniversity.us"
    format_type = "text"
    with open("test.txt","w", encoding="utf-8") as f:
        f.write(str(scraper(url=url,format_type=format_type)))
```

## Async Examples

```python
import asyncio
from scrapesome.scraper.async_scraper import scraper as async_scraper

async def main():
    url = "https://www.sandiego.edu/academics/"
    format_type = "html"
    content = await async_scraper(url=url, format_type=format_type, force_playwright=False)
    with open("test_async.txt", "w", encoding="utf-8") as f:
        f.write(str(content or ""))

if __name__ == "__main__":
    asyncio.run(main())
```