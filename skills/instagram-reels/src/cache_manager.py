"""
Cache Manager for Instagram Reels

Manages local caching of reel metadata to avoid re-fetching
and improve performance.
"""

import logging
import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime, timedelta


logger = logging.getLogger(__name__)


class CacheManager:
    """Manage local cache of reel metadata."""
    
    def __init__(self, cache_dir: Optional[str] = None):
        """
        Initialize cache manager.
        
        Args:
            cache_dir: Directory for cache files
        """
        self.cache_dir = Path(cache_dir or os.path.expanduser("~/.openclaw/workspace/.cache/instagram-reels"))
        self.metadata_cache_dir = self.cache_dir / "metadata"
        self.metadata_cache_dir.mkdir(parents=True, exist_ok=True)
    
    def _get_cache_path(self, reel_id: str) -> Path:
        """
        Get cache file path for reel metadata.
        
        Args:
            reel_id: Instagram reel ID
            
        Returns:
            Path object
        """
        return self.metadata_cache_dir / f"{reel_id}.json"
    
    def get(self, reel_id: str, max_age_hours: int = 24) -> Optional[Dict[str, Any]]:
        """
        Get cached metadata if it exists and is fresh.
        
        Args:
            reel_id: Instagram reel ID
            max_age_hours: Maximum age of cache in hours
            
        Returns:
            Cached metadata or None if expired/missing
        """
        cache_path = self._get_cache_path(reel_id)
        
        if not cache_path.exists():
            return None
        
        try:
            # Check age
            mtime = cache_path.stat().st_mtime
            age_hours = (datetime.now().timestamp() - mtime) / 3600
            
            if age_hours > max_age_hours:
                logger.info(f"Cache for {reel_id} expired (age: {age_hours:.1f}h)")
                return None
            
            # Load metadata
            with open(cache_path, 'r') as f:
                data = json.load(f)
            
            logger.info(f"Cache hit for {reel_id}")
            return data
            
        except Exception as e:
            logger.error(f"Error reading cache for {reel_id}: {e}")
            return None
    
    def set(self, reel_id: str, metadata: Dict[str, Any]) -> bool:
        """
        Cache metadata for a reel.
        
        Args:
            reel_id: Instagram reel ID
            metadata: Metadata to cache
            
        Returns:
            True if successful, False otherwise
        """
        cache_path = self._get_cache_path(reel_id)
        
        try:
            with open(cache_path, 'w') as f:
                json.dump(metadata, f, indent=2, default=str)
            
            logger.info(f"Cached metadata for {reel_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error caching metadata for {reel_id}: {e}")
            return False
    
    def exists(self, reel_id: str) -> bool:
        """
        Check if metadata is cached.
        
        Args:
            reel_id: Instagram reel ID
            
        Returns:
            True if cached, False otherwise
        """
        return self._get_cache_path(reel_id).exists()
    
    def delete(self, reel_id: str) -> bool:
        """
        Delete cached metadata.
        
        Args:
            reel_id: Instagram reel ID
            
        Returns:
            True if successful, False otherwise
        """
        cache_path = self._get_cache_path(reel_id)
        
        try:
            if cache_path.exists():
                cache_path.unlink()
                logger.info(f"Deleted cache for {reel_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting cache for {reel_id}: {e}")
            return False
    
    def clear_all(self) -> int:
        """
        Clear all cached metadata.
        
        Returns:
            Number of files deleted
        """
        deleted = 0
        try:
            for cache_file in self.metadata_cache_dir.glob('*.json'):
                cache_file.unlink()
                deleted += 1
            logger.info(f"Cleared {deleted} cache entries")
        except Exception as e:
            logger.error(f"Error clearing cache: {e}")
        
        return deleted
    
    def cleanup_old(self, days: int = 7) -> int:
        """
        Delete cache entries older than specified days.
        
        Args:
            days: Delete entries older than this many days
            
        Returns:
            Number of files deleted
        """
        import time
        cutoff_time = time.time() - (days * 86400)
        
        deleted = 0
        try:
            for cache_file in self.metadata_cache_dir.glob('*.json'):
                if cache_file.stat().st_mtime < cutoff_time:
                    cache_file.unlink()
                    deleted += 1
            logger.info(f"Cleaned up {deleted} old cache entries")
        except Exception as e:
            logger.error(f"Error cleaning up cache: {e}")
        
        return deleted
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get cache statistics.
        
        Returns:
            Dictionary with cache info
        """
        try:
            files = list(self.metadata_cache_dir.glob('*.json'))
            total_size = sum(f.stat().st_size for f in files)
            
            return {
                "total_entries": len(files),
                "total_size_bytes": total_size,
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "cache_dir": str(self.metadata_cache_dir)
            }
        except Exception as e:
            logger.error(f"Error getting cache stats: {e}")
            return {"error": str(e)}
    
    def list_cached(self) -> list:
        """
        List all cached reel IDs.
        
        Returns:
            List of reel IDs
        """
        try:
            return [f.stem for f in self.metadata_cache_dir.glob('*.json')]
        except Exception:
            return []


def main():
    """Test cache manager."""
    cache = CacheManager()
    
    # Test operations
    test_metadata = {
        "reel_id": "TEST123",
        "creator": "test_user",
        "description": "Test reel"
    }
    
    # Save
    cache.set("TEST123", test_metadata)
    
    # Retrieve
    retrieved = cache.get("TEST123")
    print("Cached:", retrieved)
    
    # Stats
    print("Cache stats:", cache.get_stats())
    
    # List
    print("Cached reels:", cache.list_cached())


if __name__ == '__main__':
    main()
