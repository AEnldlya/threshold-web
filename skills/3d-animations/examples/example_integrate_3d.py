#!/usr/bin/env python3
"""
Example: Integrate 3D Animations into Website

This example demonstrates how to integrate 3D animations into an existing website.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.fetcher_21st_dev import Fetcher21stDev
from src.animation_integrator import AnimationIntegrator


def example_simple_integration():
    """Example: Simple integration"""
    print("=" * 60)
    print("Example 1: Simple Integration")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    integrator = AnimationIntegrator()
    
    # Get a hero animation
    animations = fetcher.search(category="3d-hero", limit=1)
    animation_id = animations[0]["id"]
    
    # Integrate into website
    result = integrator.integrate(
        website_id="my-portfolio",
        animation_id=animation_id,
        page="home",
        section="hero"
    )
    
    print(f"\nIntegration Result:")
    print(f"  Component: {result['component_created']}")
    print(f"  Performance Score: {result['performance_score']}/100")
    print(f"  Lighthouse Score: {result['lighthouse_score']}/100")
    print(f"  Status: {'✓ Ready to Deploy' if result['deployed'] else '○ Not Deployed'}")


def example_custom_colors():
    """Example: Integration with custom colors"""
    print("\n" + "=" * 60)
    print("Example 2: Custom Colors")
    print("=" * 60)
    
    integrator = AnimationIntegrator()
    
    # Integrate with brand colors
    result = integrator.integrate(
        website_id="spa-business",
        animation_id="3d-hero-1",
        page="home",
        section="hero",
        colors=["#d4af37", "#ffffff"],  # Gold and white
        speed=1.5,
        intensity="high"
    )
    
    print(f"\nIntegration with custom colors:")
    print(f"  Colors: {result['customization']['colors']}")
    print(f"  Speed: {result['customization']['speed']}x")
    print(f"  Intensity: {result['customization']['intensity']}")
    print(f"  Component: {result['component_created']}")


def example_product_showcase():
    """Example: Product showcase integration"""
    print("\n" + "=" * 60)
    print("Example 3: Product Showcase")
    print("=" * 60)
    
    fetcher = Fetcher21stDev()
    integrator = AnimationIntegrator()
    
    # Get product animation
    animations = fetcher.search(category="3d-product", limit=1)
    
    if animations:
        result = integrator.integrate(
            website_id="ecommerce-store",
            animation_id=animations[0]["id"],
            page="products",
            section="showcase",
            scale=1.2,
            speed=1.0
        )
        
        print(f"\nProduct showcase integrated:")
        print(f"  Component: {result['component_created']}")
        print(f"  Scale: {result['customization']['scale']}x")
        print(f"  Lighthouse Score: {result['lighthouse_score']}/100")


def example_multiple_sections():
    """Example: Integrate to multiple sections"""
    print("\n" + "=" * 60)
    print("Example 4: Multiple Sections")
    print("=" * 60)
    
    integrator = AnimationIntegrator()
    
    sections = [
        ("home", "hero", "3d-hero-1"),
        ("about", "intro", "3d-hero-2"),
        ("contact", "background", "3d-text-1")
    ]
    
    print("\nIntegrating animations to multiple sections:")
    for page, section, anim_id in sections:
        result = integrator.integrate(
            website_id="my-site",
            animation_id=anim_id,
            page=page,
            section=section
        )
        print(f"  ✓ {page}/{section}: {result['component_created']}")


def example_batch_integration():
    """Example: Batch integration"""
    print("\n" + "=" * 60)
    print("Example 5: Batch Integration")
    print("=" * 60)
    
    integrator = AnimationIntegrator()
    
    websites = [
        {
            "website_id": "site-1",
            "animation_id": "3d-hero-1",
            "page": "home",
            "section": "hero"
        },
        {
            "website_id": "site-2",
            "animation_id": "3d-product-1",
            "page": "products",
            "section": "showcase"
        },
        {
            "website_id": "site-3",
            "animation_id": "3d-gallery-1",
            "page": "portfolio",
            "section": "gallery"
        }
    ]
    
    result = integrator.batch_integrate(websites=websites, deploy_all=True)
    
    print(f"\nBatch Integration Results:")
    print(f"  Websites Processed: {result['websites_processed']}")
    print(f"  Successful: {result['successful']}")
    print(f"  Animations Added: {result['animations_added']}")
    print(f"  Total Time: {result['total_time']}ms")
    print(f"  Status: {'✓ All Deployed' if result['all_deployed'] else '○ Pending Deployment'}")


def main():
    """Run all integration examples"""
    try:
        example_simple_integration()
        example_custom_colors()
        example_product_showcase()
        example_multiple_sections()
        example_batch_integration()
        
        print("\n" + "=" * 60)
        print("✓ All integration examples completed!")
        print("=" * 60)
    
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
