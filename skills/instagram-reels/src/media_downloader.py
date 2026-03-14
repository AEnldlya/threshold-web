"""
Media Downloader for Instagram Reels

Downloads video and thumbnail files from Instagram,
with caching and error handling.
"""

import asyncio
import logging
import os
from pathlib import Path
from typing import Optional, Tuple
from datetime import datetime
import hashlib

import requests
from PIL import Image
from io import BytesIO


logger = logging.getLogger(__name__)


class MediaDownloader:
    """Download and manage reel media files."""
    
    def __init__(self, cache_dir: Optional[str] = None):
        """
        Initialize media downloader.
        
        Args:
            cache_dir: Directory for caching media files
        """
        self.cache_dir = Path(cache_dir or os.path.expanduser("~/.openclaw/workspace/.cache/instagram-reels"))
        self.video_cache = self.cache_dir / "videos"
        self.image_cache = self.cache_dir / "images"
        
        self.video_cache.mkdir(parents=True, exist_ok=True)
        self.image_cache.mkdir(parents=True, exist_ok=True)
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def _get_cache_path(self, reel_id: str, media_type: str) -> Path:
        """
        Get cache file path for media.
        
        Args:
            reel_id: Instagram reel ID
            media_type: 'video' or 'image'
            
        Returns:
            Path object for cache file
        """
        cache_dir = self.video_cache if media_type == 'video' else self.image_cache
        ext = '.mp4' if media_type == 'video' else '.jpg'
        return cache_dir / f"{reel_id}{ext}"
    
    def is_cached(self, reel_id: str, media_type: str) -> bool:
        """
        Check if media is cached.
        
        Args:
            reel_id: Instagram reel ID
            media_type: 'video' or 'image'
            
        Returns:
            True if file exists in cache
        """
        cache_path = self._get_cache_path(reel_id, media_type)
        return cache_path.exists()
    
    async def download_video(self, url: str, reel_id: str, force: bool = False) -> Tuple[bool, Optional[str]]:
        """
        Download video from URL.
        
        Args:
            url: Video URL
            reel_id: Instagram reel ID
            force: Re-download even if cached
            
        Returns:
            Tuple of (success, file_path)
        """
        if not url:
            logger.warning(f"No video URL provided for reel {reel_id}")
            return False, None
        
        cache_path = self._get_cache_path(reel_id, 'video')
        
        # Check cache
        if not force and cache_path.exists():
            logger.info(f"Video {reel_id} found in cache: {cache_path}")
            return True, str(cache_path)
        
        try:
            logger.info(f"Downloading video from {url}")
            
            # Download with timeout and streaming
            response = self.session.get(url, timeout=30, stream=True)
            response.raise_for_status()
            
            # Get file size
            file_size = int(response.headers.get('content-length', 0))
            if file_size == 0:
                logger.error("Video has zero size")
                return False, None
            
            # Limit to 500MB
            if file_size > 500 * 1024 * 1024:
                logger.error(f"Video too large ({file_size} bytes), skipping")
                return False, None
            
            # Download in chunks
            with open(cache_path, 'wb') as f:
                downloaded = 0
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
            
            logger.info(f"Video downloaded: {cache_path} ({file_size} bytes)")
            return True, str(cache_path)
            
        except Exception as e:
            logger.error(f"Error downloading video: {e}")
            # Clean up partial file
            if cache_path.exists():
                cache_path.unlink()
            return False, None
    
    async def download_image(self, url: str, reel_id: str, force: bool = False) -> Tuple[bool, Optional[str]]:
        """
        Download image thumbnail.
        
        Args:
            url: Image URL
            reel_id: Instagram reel ID
            force: Re-download even if cached
            
        Returns:
            Tuple of (success, file_path)
        """
        if not url:
            logger.warning(f"No image URL provided for reel {reel_id}")
            return False, None
        
        cache_path = self._get_cache_path(reel_id, 'image')
        
        # Check cache
        if not force and cache_path.exists():
            logger.info(f"Image {reel_id} found in cache: {cache_path}")
            return True, str(cache_path)
        
        try:
            logger.info(f"Downloading image from {url}")
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Validate and save image
            img = Image.open(BytesIO(response.content))
            
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize if too large
            max_width = 1080
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Save as JPEG
            img.save(cache_path, 'JPEG', quality=85)
            
            logger.info(f"Image downloaded: {cache_path}")
            return True, str(cache_path)
            
        except Exception as e:
            logger.error(f"Error downloading image: {e}")
            if cache_path.exists():
                cache_path.unlink()
            return False, None
    
    async def download_media(
        self,
        reel_id: str,
        video_url: Optional[str] = None,
        image_url: Optional[str] = None,
        include_video: bool = True,
        include_image: bool = True
    ) -> dict:
        """
        Download both video and image with parallel requests.
        
        Args:
            reel_id: Instagram reel ID
            video_url: Video URL
            image_url: Image URL
            include_video: Whether to download video
            include_image: Whether to download image
            
        Returns:
            Dictionary with download results
        """
        results = {
            "reel_id": reel_id,
            "video_downloaded": False,
            "image_downloaded": False,
            "video_path": None,
            "image_path": None
        }
        
        # Download in parallel
        tasks = []
        
        if include_video and video_url:
            tasks.append(self.download_video(video_url, reel_id))
        
        if include_image and image_url:
            tasks.append(self.download_image(image_url, reel_id))
        
        if not tasks:
            return results
        
        try:
            download_results = await asyncio.gather(*tasks)
            
            # Parse results
            result_idx = 0
            if include_video and video_url:
                success, path = download_results[result_idx]
                results["video_downloaded"] = success
                results["video_path"] = path
                result_idx += 1
            
            if include_image and image_url:
                success, path = download_results[result_idx]
                results["image_downloaded"] = success
                results["image_path"] = path
            
        except Exception as e:
            logger.error(f"Error in parallel downloads: {e}")
        
        return results
    
    def cleanup_cache(self, days_old: int = 30):
        """
        Remove cached files older than specified days.
        
        Args:
            days_old: Delete files older than this many days
        """
        import time
        cutoff_time = time.time() - (days_old * 86400)
        
        removed = 0
        for cache_dir in [self.video_cache, self.image_cache]:
            for file_path in cache_dir.glob('*'):
                if file_path.is_file():
                    if os.path.getmtime(file_path) < cutoff_time:
                        file_path.unlink()
                        removed += 1
                        logger.info(f"Removed cached file: {file_path}")
        
        logger.info(f"Cleanup complete: {removed} files removed")
    
    def get_cache_size(self) -> dict:
        """
        Get cache directory sizes.
        
        Returns:
            Dictionary with cache sizes in bytes
        """
        def dir_size(path: Path) -> int:
            return sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())
        
        return {
            "videos": dir_size(self.video_cache),
            "images": dir_size(self.image_cache),
            "total": dir_size(self.cache_dir)
        }
    
    def __del__(self):
        """Cleanup on deletion."""
        try:
            self.session.close()
        except:
            pass


def main():
    """Test media downloader."""
    downloader = MediaDownloader()
    
    # Test cache checking
    print("Cache size:", downloader.get_cache_size())
    print("Videos cached:", list(downloader.video_cache.glob('*.mp4')))
    print("Images cached:", list(downloader.image_cache.glob('*.jpg')))


if __name__ == '__main__':
    main()
