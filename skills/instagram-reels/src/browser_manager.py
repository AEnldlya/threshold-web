"""
Browser Manager for Instagram Reels

Manages Playwright browser sessions, handles login if needed,
and maintains cookies/cache across requests.
"""

import asyncio
import logging
import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

try:
    from playwright.async_api import async_playwright, Browser, BrowserContext, Page
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    Browser = BrowserContext = Page = None


logger = logging.getLogger(__name__)
load_dotenv()


class BrowserManager:
    """Manage Playwright browser sessions for Instagram."""
    
    def __init__(
        self,
        headless: bool = True,
        cache_dir: Optional[str] = None,
        use_proxy: bool = False,
        proxy_url: Optional[str] = None
    ):
        """
        Initialize browser manager.
        
        Args:
            headless: Run browser in headless mode
            cache_dir: Directory for browser cache and cookies
            use_proxy: Whether to use proxy
            proxy_url: Proxy URL if use_proxy is True
        """
        if not PLAYWRIGHT_AVAILABLE:
            raise ImportError("Playwright not installed. Run: pip install playwright")
        
        self.headless = headless
        self.cache_dir = Path(cache_dir or os.path.expanduser("~/.openclaw/workspace/.cache/instagram-reels"))
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        self.use_proxy = use_proxy
        self.proxy_url = proxy_url
        
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None
        
        self.username = os.getenv("INSTAGRAM_USERNAME")
        self.password = os.getenv("INSTAGRAM_PASSWORD")
    
    async def launch(self) -> Browser:
        """
        Launch browser instance.
        
        Returns:
            Playwright Browser instance
        """
        if self.browser:
            return self.browser
        
        playwright = await async_playwright().start()
        
        browser_args = {
            "headless": self.headless,
        }
        
        if self.use_proxy and self.proxy_url:
            browser_args["proxy"] = {"server": self.proxy_url}
        
        self.browser = await playwright.chromium.launch(**browser_args)
        logger.info("Browser launched")
        return self.browser
    
    async def create_context(self) -> BrowserContext:
        """
        Create browser context with persistent storage.
        
        Returns:
            BrowserContext instance
        """
        if self.context:
            return self.context
        
        if not self.browser:
            await self.launch()
        
        context_args = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        
        # Use persistent storage for cookies
        cookies_file = self.cache_dir / "cookies.json"
        if cookies_file.exists():
            with open(cookies_file, 'r') as f:
                import json
                context_args["storage_state"] = json.load(f)
        
        self.context = await self.browser.new_context(**context_args)
        logger.info("Browser context created")
        return self.context
    
    async def get_page(self) -> Page:
        """
        Get or create a page instance.
        
        Returns:
            Page instance
        """
        if self.page:
            return self.page
        
        if not self.context:
            await self.create_context()
        
        self.page = await self.context.new_page()
        logger.info("New page created")
        return self.page
    
    async def save_cookies(self):
        """Save current cookies to file."""
        if not self.context:
            return
        
        try:
            cookies_file = self.cache_dir / "cookies.json"
            cookies = await self.context.cookies()
            
            import json
            with open(cookies_file, 'w') as f:
                json.dump(cookies, f, indent=2)
            logger.info(f"Cookies saved to {cookies_file}")
        except Exception as e:
            logger.error(f"Failed to save cookies: {e}")
    
    async def navigate(self, url: str, wait_until: str = "networkidle") -> None:
        """
        Navigate to URL and wait for page load.
        
        Args:
            url: URL to navigate to
            wait_until: Wait condition ('load', 'domcontentloaded', 'networkidle')
        """
        if not self.page:
            await self.get_page()
        
        try:
            await self.page.goto(url, wait_until=wait_until, timeout=30000)
            logger.info(f"Navigated to {url}")
        except Exception as e:
            logger.error(f"Failed to navigate to {url}: {e}")
            raise
    
    async def wait_for_selector(self, selector: str, timeout: int = 10000) -> bool:
        """
        Wait for element to appear on page.
        
        Args:
            selector: CSS selector
            timeout: Timeout in milliseconds
            
        Returns:
            True if element appeared, False if timeout
        """
        if not self.page:
            return False
        
        try:
            await self.page.wait_for_selector(selector, timeout=timeout)
            return True
        except Exception:
            return False
    
    async def get_page_content(self) -> str:
        """
        Get full page HTML content.
        
        Returns:
            Page HTML as string
        """
        if not self.page:
            return ""
        
        return await self.page.content()
    
    async def evaluate_script(self, script: str) -> any:
        """
        Evaluate JavaScript in page context.
        
        Args:
            script: JavaScript code to evaluate
            
        Returns:
            Result of script evaluation
        """
        if not self.page:
            return None
        
        return await self.page.evaluate(script)
    
    async def close(self):
        """Close browser and clean up resources."""
        try:
            if self.page:
                await self.page.close()
            if self.context:
                await self.save_cookies()
                await self.context.close()
            if self.browser:
                await self.browser.close()
            logger.info("Browser closed")
        except Exception as e:
            logger.error(f"Error closing browser: {e}")
    
    async def __aenter__(self):
        """Async context manager entry."""
        await self.launch()
        await self.create_context()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()


def get_browser_manager(headless: bool = True) -> BrowserManager:
    """
    Factory function to create a BrowserManager instance.
    
    Args:
        headless: Run in headless mode
        
    Returns:
        BrowserManager instance
    """
    return BrowserManager(headless=headless)


async def main():
    """Test browser manager."""
    async with get_browser_manager() as browser_mgr:
        await browser_mgr.navigate("https://www.instagram.com")
        content = await browser_mgr.get_page_content()
        print(f"Page loaded, content length: {len(content)}")


if __name__ == '__main__':
    asyncio.run(main())
