#!/usr/bin/env python3
"""
Instagram Reels Skill CLI

Fetch, analyze, and export Instagram reel design patterns.
"""

import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import Optional, List
import click
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src import (
    URLParser,
    BrowserManager,
    DataFetcher,
    MediaDownloader,
    DesignAnalyzer,
    MarkdownFormatter,
    CacheManager
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment
load_dotenv()


class InstagramReelsSkill:
    """Main skill class for Instagram Reels operations."""
    
    def __init__(self, headless: bool = True):
        """Initialize skill with dependencies."""
        self.browser_mgr = BrowserManager(headless=headless)
        self.data_fetcher = DataFetcher(self.browser_mgr)
        self.media_downloader = MediaDownloader()
        self.design_analyzer = DesignAnalyzer()
        self.markdown_formatter = MarkdownFormatter()
        self.cache_manager = CacheManager()
    
    async def fetch_reel(
        self,
        url: str,
        include_video: bool = False,
        include_image: bool = True,
        extract_analysis: bool = True
    ) -> dict:
        """
        Fetch metadata from a single reel.
        
        Args:
            url: Instagram reel URL
            include_video: Download video file
            include_image: Download thumbnail image
            extract_analysis: Extract design analysis
            
        Returns:
            Dictionary with reel data
        """
        reel_id = URLParser.extract_reel_id(url)
        
        # Check cache first
        cached = self.cache_manager.get(reel_id)
        if cached:
            logger.info(f"Using cached data for {reel_id}")
            return cached
        
        try:
            # Launch browser
            await self.browser_mgr.launch()
            await self.browser_mgr.create_context()
            
            # Fetch metadata
            logger.info(f"Fetching reel: {url}")
            metadata = await self.data_fetcher.fetch_reel_metadata(url)
            
            if not metadata.get('success'):
                return metadata
            
            # Download media
            if include_video or include_image:
                media_result = await self.media_downloader.download_media(
                    reel_id=reel_id,
                    video_url=metadata.get('video_url'),
                    image_url=metadata.get('thumbnail_url'),
                    include_video=include_video,
                    include_image=include_image
                )
                metadata.update(media_result)
            
            # Extract design analysis
            if extract_analysis:
                analysis = self.design_analyzer.analyze(metadata)
                metadata['design_analysis'] = analysis
            
            # Cache result
            self.cache_manager.set(reel_id, metadata)
            
            return metadata
            
        except Exception as e:
            logger.error(f"Error fetching reel: {e}")
            return {
                "success": False,
                "error": str(e),
                "error_type": "unknown_error",
                "reel_id": reel_id
            }
        finally:
            await self.browser_mgr.close()
    
    async def fetch_reels_batch(
        self,
        urls: List[str],
        include_videos: bool = False,
        concurrent_limit: int = 3,
        extract_analysis: bool = True
    ) -> dict:
        """
        Fetch multiple reels concurrently.
        
        Args:
            urls: List of Instagram reel URLs
            include_videos: Download videos
            concurrent_limit: Number of concurrent downloads
            extract_analysis: Extract design analysis
            
        Returns:
            Dictionary with batch results
        """
        logger.info(f"Fetching {len(urls)} reels with limit={concurrent_limit}")
        
        results = {
            "success": True,
            "total_reels": len(urls),
            "successful": 0,
            "failed": 0,
            "reels": []
        }
        
        # Process in batches
        for i in range(0, len(urls), concurrent_limit):
            batch = urls[i:i+concurrent_limit]
            
            tasks = [
                self.fetch_reel(
                    url,
                    include_video=include_videos,
                    extract_analysis=extract_analysis
                )
                for url in batch
            ]
            
            batch_results = await asyncio.gather(*tasks)
            
            for result in batch_results:
                results["reels"].append(result)
                if result.get('success'):
                    results["successful"] += 1
                else:
                    results["failed"] += 1
        
        return results
    
    async def save_reel_to_markdown(
        self,
        reel_id: str,
        creator: str,
        design_analysis: dict,
        description: str = "",
        custom_notes: str = "",
        output_file: Optional[str] = None
    ) -> dict:
        """
        Save reel analysis to DESIGN_REFERENCES.md.
        
        Args:
            reel_id: Instagram reel ID
            creator: Creator username
            design_analysis: Design analysis dictionary
            description: Reel description
            custom_notes: Custom notes
            output_file: Output markdown file path
            
        Returns:
            Dictionary with operation result
        """
        try:
            if output_file:
                formatter = MarkdownFormatter(output_file)
            else:
                formatter = self.markdown_formatter
            
            # Check if already exists
            if formatter.check_if_exists(reel_id):
                logger.info(f"Reel {reel_id} already in markdown file")
                return {
                    "success": True,
                    "already_exists": True,
                    "file": str(formatter.output_file)
                }
            
            # Append entry
            success = formatter.append_entry(
                reel_id=reel_id,
                creator=creator,
                description=description,
                design_analysis=design_analysis,
                custom_notes=custom_notes
            )
            
            return {
                "success": success,
                "entry_added": success,
                "file": str(formatter.output_file),
                "reel_id": reel_id
            }
            
        except Exception as e:
            logger.error(f"Error saving to markdown: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def cache_stats(self) -> dict:
        """Get cache statistics."""
        return self.cache_manager.get_stats()
    
    async def clear_cache(self) -> dict:
        """Clear all cache."""
        deleted = self.cache_manager.clear_all()
        return {
            "success": True,
            "deleted_entries": deleted
        }


# Click CLI interface
@click.group()
def cli():
    """Instagram Reels Skill - Fetch and analyze Instagram reel designs."""
    pass


@cli.command()
@click.option('--url', required=True, help='Instagram reel URL')
@click.option('--include-video', is_flag=True, help='Download video file')
@click.option('--include-image', is_flag=True, default=True, help='Download thumbnail')
@click.option('--extract-analysis', is_flag=True, default=True, help='Extract design analysis')
@click.option('--format', type=click.Choice(['json', 'markdown']), default='json')
def fetch_reel(url, include_video, include_image, extract_analysis, format):
    """Fetch metadata from a single reel."""
    skill = InstagramReelsSkill()
    
    async def run():
        result = await skill.fetch_reel(
            url=url,
            include_video=include_video,
            include_image=include_image,
            extract_analysis=extract_analysis
        )
        
        if format == 'json':
            click.echo(json.dumps(result, indent=2, default=str))
        else:
            click.echo(f"Reel ID: {result.get('reel_id')}")
            click.echo(f"Creator: {result.get('creator')}")
            click.echo(f"Likes: {result.get('likes')}")
            if result.get('design_analysis'):
                click.echo(f"Animations: {', '.join(result['design_analysis'].get('animations', []))}")
    
    asyncio.run(run())


@cli.command()
@click.option('--urls', multiple=True, required=True, help='Instagram reel URLs')
@click.option('--include-videos', is_flag=True, help='Download video files')
@click.option('--limit', type=int, default=3, help='Concurrent download limit')
def fetch_batch(urls, include_videos, limit):
    """Fetch multiple reels concurrently."""
    skill = InstagramReelsSkill()
    
    async def run():
        result = await skill.fetch_reels_batch(
            urls=list(urls),
            include_videos=include_videos,
            concurrent_limit=limit
        )
        click.echo(json.dumps(result, indent=2, default=str))
    
    asyncio.run(run())


@cli.command()
@click.option('--reel-id', required=True, help='Instagram reel ID')
@click.option('--creator', required=True, help='Creator username')
@click.option('--description', default='', help='Reel description')
@click.option('--custom-notes', default='', help='Custom notes')
@click.option('--output-file', help='Output markdown file')
def save_to_md(reel_id, creator, description, custom_notes, output_file):
    """Save reel analysis to markdown file."""
    skill = InstagramReelsSkill()
    
    async def run():
        result = await skill.save_reel_to_markdown(
            reel_id=reel_id,
            creator=creator,
            design_analysis={},
            description=description,
            custom_notes=custom_notes,
            output_file=output_file
        )
        click.echo(json.dumps(result, indent=2, default=str))
    
    asyncio.run(run())


@cli.command()
def cache_status():
    """Show cache statistics."""
    skill = InstagramReelsSkill()
    
    async def run():
        stats = await skill.cache_stats()
        click.echo(json.dumps(stats, indent=2))
    
    asyncio.run(run())


@cli.command()
@click.confirmation_option(prompt='Clear all cache? This cannot be undone.')
def cache_clear():
    """Clear all cached data."""
    skill = InstagramReelsSkill()
    
    async def run():
        result = await skill.clear_cache()
        click.echo(json.dumps(result, indent=2))
    
    asyncio.run(run())


if __name__ == '__main__':
    cli()
