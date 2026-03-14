#!/usr/bin/env python3
"""
Example: Fetch 3D Animations from 21st.dev

This example demonstrates how to search for and fetch 3D animation prompts
from 21st.dev using the 3D Animations skill.
"""

import sys
import json
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.fetcher_21st_dev import Fetcher21stDev


def example_basic_search():
    """Example: Basic search"""
    print("=" * 60)
    print("Example 1: Basic Search")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    
    # Search for floating cube animations
    animations = fetcher.search(
        query="floating cube",
        framework="three.js",
        limit=5
    )
    
    print(f"\nFound {len(animations)} animations:\n")
    for anim in animations:
        print(f"  • {anim['name']}")
        print(f"    ID: {anim['id']}")
        print(f"    Framework: {anim['technology']}")
        print(f"    Difficulty: {anim['difficulty']}\n")


def example_category_filter():
    """Example: Filter by category"""
    print("=" * 60)
    print("Example 2: Filter by Category")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    
    # Get all categories
    categories = fetcher.get_categories()
    print(f"\nAvailable categories: {', '.join(categories)}\n")
    
    # Get hero animations
    hero_animations = fetcher.get_by_category("3d-hero", limit=3)
    print(f"Hero animations ({len(hero_animations)}):")
    for anim in hero_animations:
        print(f"  • {anim['name']}")


def example_advanced_search():
    """Example: Advanced search with multiple filters"""
    print("=" * 60)
    print("Example 3: Advanced Search")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    
    # Advanced search
    results = fetcher.advanced_search(
        query="rotating",
        frameworks=["three.js"],
        complexity="intermediate",
        performance="high"
    )
    
    print(f"\nAdvanced search results ({len(results)}):\n")
    for result in results:
        print(f"  Rank #{result['rank']}: {result['name']}")
        print(f"    Framework: {result['framework']}")
        print(f"    Performance: {result['performance_rating']}/10")
        print(f"    Browser Support: {', '.join(result['browser_support'])}\n")


def example_get_animation():
    """Example: Get specific animation"""
    print("=" * 60)
    print("Example 4: Get Specific Animation")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    
    # Get specific animation
    animation = fetcher.get_by_id("3d-hero-1")
    
    if animation:
        print(f"\n{animation['name']}")
        print(f"Description: {animation['description']}")
        print(f"Technology: {animation['technology']}")
        print(f"Difficulty: {animation['difficulty']}")
        print(f"\nPrompt:\n{animation['prompt']}\n")
        print(f"Code Preview:\n{animation['code'][:200]}...")


def example_extract_prompts():
    """Example: Extract prompts by category"""
    print("=" * 60)
    print("Example 5: Extract Prompts")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    
    # Extract hero animation prompts
    prompts = fetcher.extract_prompts(
        category="3d-hero",
        extract_code=False
    )
    
    print(f"\nExtracted {len(prompts)} prompts:")
    for prompt in prompts[:3]:
        print(f"\n• {prompt['name']}")
        print(f"  Prompt: {prompt['prompt'][:100]}...")


def example_frameworks():
    """Example: Get available frameworks"""
    print("=" * 60)
    print("Example 6: Available Frameworks")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    
    frameworks = fetcher.get_frameworks()
    print(f"\nSupported frameworks: {', '.join(frameworks)}\n")
    
    # Get animations for each framework
    for fw in frameworks:
        anims = fetcher.search(framework=fw, limit=1)
        if anims:
            print(f"  {fw}: {len(anims)} animation(s)")


def example_trending():
    """Example: Get trending animations"""
    print("=" * 60)
    print("Example 7: Trending Animations")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    
    trending = fetcher.get_trending(limit=5)
    print(f"\nTrending animations ({len(trending)}):\n")
    for i, anim in enumerate(trending, 1):
        print(f"  {i}. {anim['name']}")
        print(f"     Category: {anim['category']}\n")


def main():
    """Run all examples"""
    try:
        example_basic_search()
        example_category_filter()
        example_advanced_search()
        example_get_animation()
        example_extract_prompts()
        example_frameworks()
        example_trending()
        
        print("\n" + "=" * 60)
        print("✓ All examples completed successfully!")
        print("=" * 60)
    
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
