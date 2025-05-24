
# Usage

## Force Rendering
```python
scraper("https://example.com", force_playwright=True)
```

Custom User Agents
```python
scraper("https://example.com", user_agents=["AgentX/1.0"])
```

Redirects
```python
scraper("https://example.com", allow_redirects=False)
```
