"""
Data Fetcher for Instagram Reels

Fetches reel metadata from Instagram pages using browser automation.
Extracts video URLs, descriptions, stats, and other metadata.
"""

import asyncio
import json
import logging
import re
import time
from typing import Dict, Optional, Any
from datetime import datetime

from .browser_manager import BrowserManager
from .url_parser import URLParser


logger = logging.getLogger(__name__)


class DataFetcher:
    """Fetch reel metadata from Instagram."""
    
    def __init__(self, browser_mgr: Optional[BrowserManager] = None):
        """
        Initialize data fetcher.
        
        Args:
            browser_mgr: BrowserManager instance (created if None)
        """
        self.browser_mgr = browser_mgr or BrowserManager()
    
    async def fetch_reel_metadata(self, url: str) -> Dict[str, Any]:
        """
        Fetch metadata from a single reel.
        
        Args:
            url: Instagram reel URL
            
        Returns:
            Dictionary with reel metadata or error info
        """
        # Normalize URL
        url = URLParser.normalize_url(url)
        reel_id = URLParser.extract_reel_id(url)
        
        if not reel_id:
            return {
                "success": False,
                "error": "Invalid Instagram reel URL",
                "error_type": "invalid_url"
            }
        
        try:
            # Navigate to reel
            await self.browser_mgr.navigate(url, wait_until="networkidle")
            
            # Wait a bit for dynamic content to load
            await asyncio.sleep(2)
            
            # Extract metadata from page
            metadata = await self._extract_metadata()
            
            if not metadata:
                return {
                    "success": False,
                    "error": "Failed to extract metadata",
                    "error_type": "parsing_error"
                }
            
            metadata['reel_id'] = reel_id
            metadata['success'] = True
            return metadata
            
        except Exception as e:
            error_type = self._classify_error(str(e))
            return {
                "success": False,
                "error": str(e),
                "error_type": error_type,
                "reel_id": reel_id
            }
    
    async def _extract_metadata(self) -> Optional[Dict[str, Any]]:
        """
        Extract metadata from page using JavaScript.
        
        Returns:
            Dictionary with extracted metadata or None
        """
        try:
            # Try to extract from window._sharedData or embedded JSON
            script = """
            (() => {
                // Look for embedded JSON data
                const scripts = document.querySelectorAll('script[type="application/json"]');
                
                for (let script of scripts) {
                    try {
                        const data = JSON.parse(script.textContent);
                        if (data?.props?.pageProps?.post) {
                            return data.props.pageProps.post;
                        }
                    } catch (e) {}
                }
                
                // Fallback: look for graphql data
                if (window.__INITIAL_STATE__) {
                    return window.__INITIAL_STATE__;
                }
                
                return null;
            })()
            """
            
            data = await self.browser_mgr.evaluate_script(script)
            
            if data:
                return self._parse_metadata(data)
            
            # Fallback: scrape from visible DOM
            return await self._scrape_from_dom()
            
        except Exception as e:
            logger.error(f"Error extracting metadata: {e}")
            return None
    
    def _parse_metadata(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse metadata from extracted data structure.
        
        Args:
            data: Raw metadata from page
            
        Returns:
            Cleaned metadata dictionary
        """
        try:
            metadata = {
                "creator": data.get("owner", {}).get("username", "unknown"),
                "description": data.get("caption", ""),
                "likes": data.get("likeCount", 0),
                "comments": data.get("commentCount", 0),
                "video_url": data.get("videoUrl") or data.get("mediaUrl"),
                "thumbnail_url": data.get("thumbnailUrl") or data.get("imageUrl"),
                "duration_seconds": data.get("videoLength", 15),
                "created_at": data.get("createdAt", datetime.now().isoformat()),
                "type": "reel"
            }
            return metadata
        except Exception as e:
            logger.error(f"Error parsing metadata: {e}")
            return {}
    
    async def _scrape_from_dom(self) -> Optional[Dict[str, Any]]:
        """
        Scrape metadata from visible DOM elements.
        
        Returns:
            Dictionary with scraped metadata or None
        """
        script = """
        (() => {
            try {
                // Get creator name
                const creator = document.querySelector('[data-testid="post_owner_self_profile"] span') 
                    || document.querySelector('a[title]');
                const creatorName = creator?.textContent?.trim() || "unknown";
                
                // Get description
                const descEl = document.querySelector('[data-testid="post_comments"] span')
                    || document.querySelector('span._a9ze');
                const description = descEl?.textContent || "";
                
                // Get stats
                const statsText = document.body.innerText;
                const likesMatch = statsText.match(/([\\d,]+)\\s+likes?/i);
                const commentsMatch = statsText.match(/([\\d,]+)\\s+comments?/i);
                
                // Get video/image URLs
                const videoEl = document.querySelector('video');
                const videoUrl = videoEl?.src || document.querySelector('source')?.src;
                
                const imgEl = document.querySelector('img[alt*="Instagram"]');
                const thumbnailUrl = imgEl?.src;
                
                return {
                    creator: creatorName,
                    description: description,
                    likes: parseInt(likesMatch?.[1]?.replace(/,/g, '') || 0),
                    comments: parseInt(commentsMatch?.[1]?.replace(/,/g, '') || 0),
                    video_url: videoUrl,
                    thumbnail_url: thumbnailUrl,
                    created_at: new Date().toISOString()
                };
            } catch (e) {
                return null;
            }
        })()
        """
        
        try:
            return await self.browser_mgr.evaluate_script(script)
        except Exception as e:
            logger.error(f"Error scraping from DOM: {e}")
            return None
    
    @staticmethod
    def _classify_error(error_msg: str) -> str:
        """
        Classify error type from error message.
        
        Args:
            error_msg: Error message
            
        Returns:
            Error type classification
        """
        error_lower = error_msg.lower()
        
        if "private" in error_lower or "not authorized" in error_lower:
            return "private_reel"
        elif "not found" in error_lower or "404" in error_lower:
            return "deleted_reel"
        elif "rate limit" in error_lower or "429" in error_lower:
            return "rate_limited"
        elif "timeout" in error_lower or "connection" in error_lower:
            return "network_error"
        else:
            return "unknown_error"
    
    async def close(self):
        """Close browser manager."""
        await self.browser_mgr.close()


async def main():
    """Test data fetcher."""
    fetcher = DataFetcher()
    
    try:
        await fetcher.browser_mgr.launch()
        await fetcher.browser_mgr.create_context()
        
        # Test with a public reel (you'd need to replace with actual public reel)
        result = await fetcher.fetch_reel_metadata(
            "https://www.instagram.com/reel/DUHmsKkjZw0/"
        )
        print(json.dumps(result, indent=2, default=str))
        
    finally:
        await fetcher.close()


if __name__ == '__main__':
    asyncio.run(main())
