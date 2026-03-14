#!/usr/bin/env python3
"""
Example: Create Custom 3D Animations

This example shows how to generate custom 3D animations from text prompts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.three_js_generator import ThreeJsGenerator
from src.babylon_js_generator import BabylonJsGenerator


def example_threejs_animation():
    """Example: Generate Three.js animation"""
    print("=" * 60)
    print("Example 1: Generate Three.js Animation")
    print("=" * 60)
    
    generator = ThreeJsGenerator()
    
    result = generator.generate(
        prompt="Create a rotating product showcase with glassmorphism cards",
        performance_target=60,
        include_mobile=True
    )
    
    print(f"\nGenerated Three.js Component:")
    print(f"  File: {result['code_file']}")
    print(f"  Lines: {result['lines_of_code']}")
    print(f"  Libraries: {', '.join(result['libraries_used'])}")
    print(f"  Performance: {result['performance']} FPS")
    print(f"  Mobile Optimized: {'✓' if result['mobile_optimized'] else '✗'}")
    print(f"\nGenerated Code:\n{result['code'][:300]}...")


def example_hero_section():
    """Example: Generate hero section"""
    print("\n" + "=" * 60)
    print("Example 2: Hero Section Component")
    print("=" * 60)
    
    generator = ThreeJsGenerator()
    
    code = generator.generate_hero_section(
        colors=["#3b82f6", "#10b981"],
        speed=1.5
    )
    
    print("\nGenerated Hero Section Code:")
    print(code[:400] + "...")


def example_product_rotator():
    """Example: Generate product rotator"""
    print("\n" + "=" * 60)
    print("Example 3: Product Rotator")
    print("=" * 60)
    
    generator = ThreeJsGenerator()
    
    code = generator.generate_product_rotator()
    
    print("\nGenerated Product Rotator:")
    print(code[:400] + "...")


def example_text_animation():
    """Example: Generate text animation"""
    print("\n" + "=" * 60)
    print("Example 4: 3D Text Animation")
    print("=" * 60)
    
    generator = ThreeJsGenerator()
    
    code = generator.generate_text_animation("Welcome to Our Studio")
    
    print("\nGenerated 3D Text Animation:")
    print(code[:400] + "...")


def example_babylon_animation():
    """Example: Generate Babylon.js animation"""
    print("\n" + "=" * 60)
    print("Example 5: Babylon.js Animation")
    print("=" * 60)
    
    generator = BabylonJsGenerator()
    
    result = generator.generate(
        prompt="Create a 3D scene with animated objects",
        performance_target=60,
        include_mobile=False
    )
    
    print(f"\nGenerated Babylon.js Component:")
    print(f"  File: {result['code_file']}")
    print(f"  Lines: {result['lines_of_code']}")
    print(f"  Libraries: {', '.join(result['libraries_used'])}")


def example_performance_variations():
    """Example: Generate variations for different performance targets"""
    print("\n" + "=" * 60)
    print("Example 6: Performance Variations")
    print("=" * 60)
    
    generator = ThreeJsGenerator()
    
    targets = [30, 60, 120]
    
    print("\nGenerating for different FPS targets:")
    for fps in targets:
        result = generator.generate(
            prompt="Create a particle system",
            performance_target=fps,
            include_mobile=(fps <= 60)
        )
        print(f"  {fps} FPS: {result['lines_of_code']} lines, Mobile: {result['mobile_optimized']}")


def main():
    """Run all generation examples"""
    try:
        example_threejs_animation()
        example_hero_section()
        example_product_rotator()
        example_text_animation()
        example_babylon_animation()
        example_performance_variations()
        
        print("\n" + "=" * 60)
        print("✓ All generation examples completed!")
        print("=" * 60)
    
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
