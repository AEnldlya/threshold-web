"""
URL Parser for Instagram Reels

Parses and validates Instagram reel URLs, extracts reel IDs,
and handles various URL format variations.
"""

import re
from typing import Optional, Tuple
from urllib.parse import urlparse, parse_qs


class URLParser:
    """Parse and validate Instagram reel URLs."""
    
    # Instagram URL patterns
    PATTERNS = {
        'reel_short': r'https?://(?:www\.)?instagram\.com/reel/([a-zA-Z0-9_-]+)',
        'reel_long': r'https?://(?:www\.)?instagram\.com/reel/([a-zA-Z0-9_-]+)/\?',
        'account': r'https?://(?:www\.)?instagram\.com/([a-zA-Z0-9._-]+)/?$',
        'hashtag': r'https?://(?:www\.)?instagram\.com/explore/tags/([a-zA-Z0-9_-]+)',
    }
    
    @staticmethod
    def extract_reel_id(url: str) -> Optional[str]:
        """
        Extract reel ID from Instagram URL.
        
        Args:
            url: Instagram reel URL
            
        Returns:
            Reel ID if valid, None otherwise
            
        Examples:
            >>> URLParser.extract_reel_id("https://www.instagram.com/reel/DUHmsKkjZw0/")
            'DUHmsKkjZw0'
            >>> URLParser.extract_reel_id("https://instagram.com/reel/ABC123/?igsh=...")
            'ABC123'
        """
        for pattern_name, pattern in URLParser.PATTERNS.items():
            if pattern_name.startswith('reel'):
                match = re.search(pattern, url)
                if match:
                    return match.group(1)
        return None
    
    @staticmethod
    def extract_username(url: str) -> Optional[str]:
        """
        Extract Instagram username from account URL.
        
        Args:
            url: Instagram account URL
            
        Returns:
            Username if valid account URL, None otherwise
        """
        match = re.search(URLParser.PATTERNS['account'], url)
        if match:
            return match.group(1)
        return None
    
    @staticmethod
    def extract_hashtag(url: str) -> Optional[str]:
        """
        Extract hashtag from Instagram hashtag URL.
        
        Args:
            url: Instagram hashtag URL
            
        Returns:
            Hashtag (without #) if valid, None otherwise
        """
        match = re.search(URLParser.PATTERNS['hashtag'], url)
        if match:
            return match.group(1)
        return None
    
    @staticmethod
    def is_reel_url(url: str) -> bool:
        """
        Check if URL is a valid Instagram reel URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid reel URL, False otherwise
        """
        return URLParser.extract_reel_id(url) is not None
    
    @staticmethod
    def is_account_url(url: str) -> bool:
        """
        Check if URL is a valid Instagram account URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid account URL, False otherwise
        """
        return URLParser.extract_username(url) is not None
    
    @staticmethod
    def is_hashtag_url(url: str) -> bool:
        """
        Check if URL is a valid Instagram hashtag URL.
        
        Args:
            url: URL to validate
            
        Returns:
            True if valid hashtag URL, False otherwise
        """
        return URLParser.extract_hashtag(url) is not None
    
    @staticmethod
    def classify_url(url: str) -> Tuple[str, Optional[str]]:
        """
        Classify URL type and extract relevant identifier.
        
        Args:
            url: URL to classify
            
        Returns:
            Tuple of (url_type, identifier)
            url_type: 'reel', 'account', 'hashtag', or 'unknown'
            identifier: extracted ID or username or hashtag
            
        Examples:
            >>> URLParser.classify_url("https://www.instagram.com/reel/DUHmsKkjZw0/")
            ('reel', 'DUHmsKkjZw0')
            >>> URLParser.classify_url("https://www.instagram.com/design_inspiration/")
            ('account', 'design_inspiration')
        """
        # Try each pattern in order
        reel_id = URLParser.extract_reel_id(url)
        if reel_id:
            return ('reel', reel_id)
        
        username = URLParser.extract_username(url)
        if username:
            return ('account', username)
        
        hashtag = URLParser.extract_hashtag(url)
        if hashtag:
            return ('hashtag', hashtag)
        
        return ('unknown', None)
    
    @staticmethod
    def normalize_url(url: str) -> str:
        """
        Normalize Instagram URL to standard format.
        
        Args:
            url: Raw Instagram URL (may have parameters, etc.)
            
        Returns:
            Normalized URL
            
        Examples:
            >>> URLParser.normalize_url("https://instagram.com/reel/ABC/?igsh=...")
            'https://www.instagram.com/reel/ABC/'
        """
        url_type, identifier = URLParser.classify_url(url)
        
        if url_type == 'reel':
            return f"https://www.instagram.com/reel/{identifier}/"
        elif url_type == 'account':
            return f"https://www.instagram.com/{identifier}/"
        elif url_type == 'hashtag':
            return f"https://www.instagram.com/explore/tags/{identifier}/"
        else:
            return url
    
    @staticmethod
    def remove_query_params(url: str) -> str:
        """
        Remove query parameters from URL.
        
        Args:
            url: URL with possible query parameters
            
        Returns:
            URL without query parameters
        """
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"


def main():
    """Test URL parser with examples."""
    test_urls = [
        "https://www.instagram.com/reel/DUHmsKkjZw0/?igsh=YTQ4YzNnNG50OGVt",
        "https://instagram.com/reel/ABC123/",
        "https://www.instagram.com/design_inspiration/",
        "https://instagram.com/explore/tags/webdesign/",
        "invalid_url",
    ]
    
    for url in test_urls:
        url_type, identifier = URLParser.classify_url(url)
        print(f"URL: {url}")
        print(f"  Type: {url_type}, ID: {identifier}")
        if url_type == 'reel':
            print(f"  Normalized: {URLParser.normalize_url(url)}")
        print()


if __name__ == '__main__':
    main()
