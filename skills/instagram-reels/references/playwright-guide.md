# Playwright Setup Guide

Guide for setting up and using Playwright for Instagram scraping.

## Installation

### 1. Install Python Package
```bash
pip install playwright>=1.40.0
```

### 2. Install Browser Binaries
```bash
playwright install chromium
```

Or all browsers:
```bash
playwright install
```

### 3. Install System Dependencies (Linux/Mac)
```bash
playwright install-deps
```

## Quick Start

### Basic Browser Automation
```python
from playwright.async_api import async_playwright

async with async_playwright() as p:
    browser = await p.chromium.launch()
    page = await browser.new_page()
    await page.goto("https://www.instagram.com")
    
    # Wait for content to load
    await page.wait_for_load_state("networkidle")
    
    # Get page content
    content = await page.content()
    
    await browser.close()
```

## Best Practices for Instagram

### 1. Set User Agent
```python
context = await browser.new_context(
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
)
page = await context.new_page()
```

### 2. Handle Navigation Timeouts
```python
try:
    await page.goto(url, timeout=30000, wait_until="networkidle")
except TimeoutError:
    print("Page load timeout")
```

### 3. Wait for Dynamic Content
```python
# Wait for specific element
await page.wait_for_selector("video", timeout=10000)

# Or wait for network to idle
await page.wait_for_load_state("networkidle")
```

### 4. Extract JSON Data
```python
# Get JSON from page
script = """
const scripts = document.querySelectorAll('script[type="application/json"]');
const data = [];
scripts.forEach(s => {
    try {
        data.push(JSON.parse(s.textContent));
    } catch (e) {}
});
return data;
"""
json_data = await page.evaluate(script)
```

## Handling Instagram's Anti-Scraping

### 1. Add Delays
```python
import asyncio
asyncio.sleep(random.uniform(2, 5))  # Random delay 2-5 seconds
```

### 2. Use Persistent Context
```python
context = await browser.new_context(
    storage_state="cookies.json"  # Persist cookies
)
```

### 3. Rotate User Agents
```python
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
    # Add more agents
]
ua = random.choice(user_agents)
```

### 4. Handle Rate Limiting
```python
import time
from random import uniform

class RateLimiter:
    def __init__(self, requests_per_minute=10):
        self.delay = 60 / requests_per_minute
        self.last_request = 0
    
    async def wait(self):
        elapsed = time.time() - self.last_request
        if elapsed < self.delay:
            await asyncio.sleep(self.delay - elapsed)
        self.last_request = time.time()

limiter = RateLimiter(requests_per_minute=10)
await limiter.wait()
await page.goto(url)
```

## Debugging

### Enable Playwright Debug
```bash
PWDEBUG=1 python script.py
```

### Capture Screenshots
```python
await page.screenshot(path="screenshot.png")
```

### Print Page Content
```python
content = await page.content()
print(content)
```

### Get Console Logs
```python
page.on("console", lambda msg: print(msg.text))
```

## Performance Optimization

### 1. Disable Images
```python
await page.route("**/*.png", lambda r: r.abort())
await page.route("**/*.jpg", lambda r: r.abort())
```

### 2. Use Headless Mode
```python
browser = await p.chromium.launch(headless=True)
```

### 3. Close Unused Resources
```python
await page.close()
await context.close()
await browser.close()
```

## Common Issues

### Issue: "Timeout waiting for element"
**Solution**: Increase timeout or check if element is behind login
```python
await page.wait_for_selector("video", timeout=30000)
```

### Issue: "Navigation timeout"
**Solution**: Use longer timeout or try networkidle
```python
await page.goto(url, timeout=60000, wait_until="networkidle")
```

### Issue: "Page blocked by Instagram"
**Solution**: Add delays, use VPN, or rotate user agents
```python
await asyncio.sleep(random.uniform(5, 10))
```

### Issue: "JavaScript error on page"
**Solution**: Set error handlers
```python
page.on("pageerror", lambda error: print(f"Error: {error}"))
```

## Advanced Patterns

### Retry with Backoff
```python
async def fetch_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            await page.goto(url, timeout=30000)
            return True
        except Exception as e:
            wait_time = 2 ** attempt  # Exponential backoff
            print(f"Retry {attempt + 1} after {wait_time}s")
            await asyncio.sleep(wait_time)
    return False
```

### Concurrent Navigation
```python
async with async_playwright() as p:
    browser = await p.chromium.launch()
    
    tasks = [
        fetch_reel(browser, url)
        for url in urls
    ]
    results = await asyncio.gather(*tasks)
```

## Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [API Reference](https://playwright.dev/python/docs/api/class-browser)
- [Debugging Guide](https://playwright.dev/python/docs/debug)
- [Performance Tips](https://playwright.dev/python/docs/chrome-extensions)

---

**Note**: Always respect website ToS when using Playwright for scraping.
