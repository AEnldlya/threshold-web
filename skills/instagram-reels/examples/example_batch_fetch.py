#!/usr/bin/env python3
"""
Example: Batch Fetch Multiple Reels

This example demonstrates how to fetch and analyze multiple reels concurrently.
"""

import asyncio
import json
import sys
from pathlib import Path
from collections import Counter

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from instagram_reels import InstagramReelsSkill


async def main():
    """Fetch and analyze multiple reels."""
    
    # Initialize skill
    skill = InstagramReelsSkill()
    
    # List of reel URLs (replace with actual public reels)
    reel_urls = [
        "https://www.instagram.com/reel/DUHmsKkjZw0/",
        "https://www.instagram.com/reel/DUplhdqAbNt/",
        "https://www.instagram.com/reel/ABC123/",
        # Add more URLs as needed
    ]
    
    print(f"📸 Fetching {len(reel_urls)} reels...")
    print("-" * 60)
    
    # Fetch all reels concurrently
    result = await skill.fetch_reels_batch(
        urls=reel_urls,
        include_videos=False,       # Don't download videos
        concurrent_limit=3,         # 3 at a time
        extract_analysis=True       # Extract design patterns
    )
    
    # Summary
    print(f"\n✅ Summary:")
    print(f"Total: {result['total_reels']}")
    print(f"Successful: {result['successful']}")
    print(f"Failed: {result['failed']}")
    
    if result['failed'] == 0:
        print("🎉 All reels fetched successfully!")
    
    # Analyze results
    print("\n📊 Analysis:")
    
    animations_counter = Counter()
    layouts_counter = Counter()
    techniques_counter = Counter()
    colors_list = []
    
    for reel in result['reels']:
        if reel.get('success') and reel.get('design_analysis'):
            analysis = reel['design_analysis']
            
            # Collect data
            if analysis.get('animations'):
                animations_counter.update(analysis['animations'])
            
            if analysis.get('layout'):
                layouts_counter[analysis['layout']] += 1
            
            if analysis.get('techniques'):
                techniques_counter.update(analysis['techniques'])
            
            if analysis.get('colors'):
                colors_list.extend(analysis['colors'][:3])
    
    # Print statistics
    if animations_counter:
        print("\n🎬 Most Common Animations:")
        for anim, count in animations_counter.most_common(5):
            print(f"  {anim}: {count}")
    
    if layouts_counter:
        print("\n📐 Layout Types:")
        for layout, count in layouts_counter.most_common(5):
            print(f"  {layout}: {count}")
    
    if techniques_counter:
        print("\n🛠️ Techniques Used:")
        for technique, count in techniques_counter.most_common(5):
            print(f"  {technique}: {count}")
    
    if colors_list:
        color_counter = Counter(colors_list)
        print("\n🎨 Most Common Colors:")
        for color, count in color_counter.most_common(5):
            print(f"  {color}: {count}")
    
    # Save all to markdown
    print("\n📝 Saving all reels to DESIGN_REFERENCES.md...")
    saved_count = 0
    
    for reel in result['reels']:
        if reel.get('success'):
            save_result = await skill.save_reel_to_markdown(
                reel_id=reel['reel_id'],
                creator=reel['creator'],
                design_analysis=reel.get('design_analysis', {}),
                description=reel.get('description', ''),
                custom_notes=f"Batch fetched on {asyncio.get_event_loop().time()}"
            )
            
            if save_result['success']:
                saved_count += 1
    
    print(f"✅ Saved {saved_count} reels to markdown")
    
    # Print sample of results
    print("\n📋 Sample Results:")
    for i, reel in enumerate(result['reels'][:3]):
        print(f"\nReel {i+1}: {reel.get('reel_id')}")
        print(f"  Creator: {reel.get('creator')}")
        print(f"  Status: {'✅ Success' if reel.get('success') else '❌ Failed'}")
        if reel.get('design_analysis'):
            print(f"  Animations: {', '.join(reel['design_analysis'].get('animations', [])[:2])}")


if __name__ == '__main__':
    asyncio.run(main())
