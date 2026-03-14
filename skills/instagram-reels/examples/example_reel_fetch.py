#!/usr/bin/env python3
"""
Example: Fetch a Single Reel

This example demonstrates how to fetch metadata from a single Instagram reel.
"""

import asyncio
import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from instagram_reels import InstagramReelsSkill


async def main():
    """Fetch and analyze a single reel."""
    
    # Initialize skill
    skill = InstagramReelsSkill()
    
    # Example reel URL (replace with actual public reel)
    reel_url = "https://www.instagram.com/reel/DUHmsKkjZw0/"
    
    print(f"📸 Fetching reel: {reel_url}")
    print("-" * 60)
    
    # Fetch reel metadata and analysis
    result = await skill.fetch_reel(
        url=reel_url,
        include_video=False,        # Don't download video (slower)
        include_image=True,         # Download thumbnail
        extract_analysis=True       # Extract design patterns
    )
    
    # Check if successful
    if not result.get('success'):
        print(f"❌ Error: {result.get('error')}")
        print(f"Error type: {result.get('error_type')}")
        return
    
    # Display results
    print(f"✅ Success!\n")
    print(f"Reel ID: {result.get('reel_id')}")
    print(f"Creator: {result.get('creator')}")
    print(f"Description: {result.get('description', '(no description)')}")
    print(f"Likes: {result.get('likes', 0):,}")
    print(f"Comments: {result.get('comments', 0):,}")
    print(f"Duration: {result.get('duration_seconds', 'unknown')}s")
    
    if result.get('thumbnail_url'):
        print(f"Thumbnail saved: {result['thumbnail_url']}")
    
    # Display design analysis
    if result.get('design_analysis'):
        print("\n🎨 Design Analysis:")
        analysis = result['design_analysis']
        
        if analysis.get('animations'):
            print(f"  Animations: {', '.join(analysis['animations'])}")
        
        if analysis.get('layout'):
            print(f"  Layout: {analysis['layout']}")
        
        if analysis.get('typography'):
            print(f"  Typography: {analysis['typography']}")
        
        if analysis.get('colors'):
            colors = analysis['colors'][:5]
            print(f"  Colors: {', '.join(colors)}")
        
        if analysis.get('techniques'):
            techniques = analysis['techniques'][:3]
            print(f"  Techniques: {', '.join(techniques)}")
        
        if analysis.get('ui_elements'):
            elements = analysis['ui_elements'][:3]
            print(f"  UI Elements: {', '.join(elements)}")
        
        if analysis.get('interactions'):
            interactions = analysis['interactions'][:3]
            print(f"  Interactions: {', '.join(interactions)}")
    
    # Save to DESIGN_REFERENCES.md
    print("\n📝 Saving to DESIGN_REFERENCES.md...")
    save_result = await skill.save_reel_to_markdown(
        reel_id=result['reel_id'],
        creator=result['creator'],
        design_analysis=result.get('design_analysis', {}),
        description=result.get('description', ''),
        custom_notes="Fetched via example script"
    )
    
    if save_result['success']:
        print(f"✅ Saved to: {save_result['file']}")
    else:
        print(f"⚠️  Could not save: {save_result.get('error')}")
    
    # Print full JSON for reference
    print("\n📋 Full Result (JSON):")
    print(json.dumps(result, indent=2, default=str))


if __name__ == '__main__':
    asyncio.run(main())
