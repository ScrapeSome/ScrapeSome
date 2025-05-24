
# Usage

## Force Rendering
```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", force_playwright=True)
content
```

Custom User Agents
```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", user_agents=["AgentX/1.0"])
content
```

Redirects
```python
from scrapesome.scraper.sync_scraper import scraper
content = scraper("https://example.com", allow_redirects=False)
content
```
Similarly, async can also be used.