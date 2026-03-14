#!/usr/bin/env python3
"""
Example: Batch Processing Multiple Websites

This example demonstrates batch processing of 3D animations across multiple websites.
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.animation_integrator import AnimationIntegrator
from src.performance_optimizer import PerformanceOptimizer


def example_batch_basic():
    """Example: Basic batch processing"""
    print("=" * 60)
    print("Example 1: Basic Batch Processing")
    print("=" * 60)
    
    integrator = AnimationIntegrator()
    
    websites = [
        {"website_id": "site-1", "animation_id": "3d-hero-1"},
        {"website_id": "site-2", "animation_id": "3d-hero-2"},
        {"website_id": "site-3", "animation_id": "3d-product-1"},
    ]
    
    result = integrator.batch_integrate(
        websites=websites,
        max_parallel=3,
        deploy_all=False
    )
    
    print(f"\nBatch Processing Results:")
    print(f"  Websites Processed: {result['websites_processed']}")
    print(f"  Successful: {result['successful']}")
    print(f"  Failed: {result['failed']}")
    print(f"  Total Time: {result['total_time']}ms")
    print(f"  Animations Added: {result['animations_added']}")


def example_batch_with_customization():
    """Example: Batch with custom configuration"""
    print("\n" + "=" * 60)
    print("Example 2: Batch with Customization")
    print("=" * 60)
    
    integrator = AnimationIntegrator()
    
    websites = [
        {
            "website_id": "salon-1",
            "animation_id": "3d-hero-1",
            "colors": ["#d4af37", "#ffffff"],  # Gold and white
            "intensity": "high"
        },
        {
            "website_id": "tech-startup",
            "animation_id": "3d-product-1",
            "colors": ["#0066ff", "#00ff00"],  # Tech colors
            "scale": 1.2
        },
        {
            "website_id": "design-agency",
            "animation_id": "3d-gallery-1",
            "colors": ["#ff0066", "#ff6600"],
            "speed": 1.5
        }
    ]
    
    result = integrator.batch_integrate(websites=websites, deploy_all=True)
    
    print(f"\nBatch Results with Customization:")
    print(f"  Total: {result['websites_processed']} websites")
    print(f"  Success: {result['successful']}/{result['websites_processed']}")
    print(f"  Deployed: {result['all_deployed']}")


def example_batch_with_optimization():
    """Example: Batch processing with performance optimization"""
    print("\n" + "=" * 60)
    print("Example 3: Batch with Performance Optimization")
    print("=" * 60)
    
    integrator = AnimationIntegrator()
    optimizer = PerformanceOptimizer()
    
    websites = [
        {"website_id": f"site-{i}", "animation_id": "3d-hero-1"}
        for i in range(1, 6)
    ]
    
    # Batch integrate
    integrate_result = integrator.batch_integrate(websites=websites)
    print(f"\nIntegration: {integrate_result['successful']}/{integrate_result['websites_processed']} successful")
    
    # Optimize each
    print("\nOptimizing each website:")
    for website in websites[:3]:  # Show first 3
        result = optimizer.optimize(
            website_id=website["website_id"],
            target_fps=60,
            target_lighthouse=95,
            include_mobile=True
        )
        print(f"  ✓ {website['website_id']}")
        print(f"    Optimizations: {len(result['optimizations_applied'])}")
        print(f"    Lighthouse: {result['lighthouse_before']} → {result['lighthouse_after']}")


def example_batch_different_animations():
    """Example: Batch with different animation types"""
    print("\n" + "=" * 60)
    print("Example 4: Different Animation Types")
    print("=" * 60)
    
    integrator = AnimationIntegrator()
    
    animation_types = [
        ("hero", "3d-hero-1"),
        ("product", "3d-product-1"),
        ("text", "3d-text-1"),
        ("scroll", "3d-scroll-1"),
        ("gallery", "3d-gallery-1"),
    ]
    
    websites = [
        {
            "website_id": f"{anim_type}-showcase",
            "animation_id": anim_id,
            "page": "home",
            "section": anim_type
        }
        for anim_type, anim_id in animation_types
    ]
    
    result = integrator.batch_integrate(websites=websites, deploy_all=True)
    
    print(f"\nBatch with Different Animation Types:")
    for i, (anim_type, _) in enumerate(animation_types):
        status = "✓" if i < result['successful'] else "✗"
        print(f"  {status} {anim_type} showcase")
    
    print(f"\nTotal: {result['successful']}/{result['websites_processed']} successful")


def example_batch_monitoring():
    """Example: Batch processing with monitoring"""
    print("\n" + "=" * 60)
    print("Example 5: Batch Monitoring")
    print("=" * 60)
    
    integrator = AnimationIntegrator()
    
    # Large batch
    websites = [
        {"website_id": f"customer-{i}", "animation_id": "3d-hero-1"}
        for i in range(1, 21)  # 20 websites
    ]
    
    print(f"\nProcessing {len(websites)} websites...")
    
    result = integrator.batch_integrate(
        websites=websites,
        max_parallel=5,
        deploy_all=True
    )
    
    print(f"\nBatch Monitoring Report:")
    print(f"  Total Websites: {result['websites_processed']}")
    print(f"  Successful: {result['successful']}")
    print(f"  Failed: {result['failed']}")
    success_rate = (result['successful'] / result['websites_processed']) * 100
    print(f"  Success Rate: {success_rate:.1f}%")
    print(f"  Total Time: {result['total_time']}ms")
    print(f"  Avg Time per Website: {result['total_time'] / result['websites_processed']:.0f}ms")
    print(f"  All Deployed: {'✓ Yes' if result['all_deployed'] else '✗ No'}")


def main():
    """Run all batch processing examples"""
    try:
        example_batch_basic()
        example_batch_with_customization()
        example_batch_with_optimization()
        example_batch_different_animations()
        example_batch_monitoring()
        
        print("\n" + "=" * 60)
        print("✓ All batch processing examples completed!")
        print("=" * 60)
    
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
