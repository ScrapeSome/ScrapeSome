
## Sync Examples

```python
from scrapesome import sync_scraper

if __name__ == "__main__":
    url = "https://adenuniversity.us"
    output_format_type = "text"
    with open("test.txt","w", encoding="utf-8") as f:
        f.write(str(sync_scraper(url=url,output_format_type=output_format_type)))
```

## Async Examples

```python
import asyncio
from scrapesome import async_scraper

async def main():
    url = "https://www.sandiego.edu/academics/"
    output_format_type = "html"
    content = await async_scraper(url=url, output_format_type=output_format_type, force_playwright=False)
    with open("test_async.txt", "w", encoding="utf-8") as f:
        f.write(str(content or ""))

if __name__ == "__main__":
    asyncio.run(main())
```