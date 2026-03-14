#!/usr/bin/env python3
"""
3D Animations Skill - Main CLI Entry Point

Fetch 3D animations from 21st.dev, integrate advanced 3D effects into websites
using Three.js and Babylon.js, with automatic performance optimization.

Usage:
    3d_animations fetch_3d_animations_from_21st --query "floating cube" --framework "three.js"
    3d_animations integrate_3d_animation --website-id "site-1" --animation-id "3d-hero-1"
    3d_animations search_21st_dev_animations --query "morphing text"
    3d_animations create_custom_3d_animation --prompt "rotating product showcase"
    3d_animations optimize_3d_performance --website-id "site-1"
    3d_animations batch_add_3d_to_websites --websites "[...]"
    3d_animations extract_21st_dev_prompts --category "3d"
"""

import sys
import json
import logging
import argparse
from typing import Any, Dict, List, Optional
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ThreeDAnimationsSkill:
    """Main skill class for 3D animations"""
    
    def __init__(self):
        """Initialize the skill"""
        self.skill_dir = Path(__file__).parent
        self.src_dir = self.skill_dir / "src"
        self.prompts_dir = self.skill_dir / "prompts"
        self.components_dir = self.skill_dir / "components"
        logger.info(f"Initialized 3D Animations Skill at {self.skill_dir}")
    
    def fetch_3d_animations_from_21st(
        self,
        query: str,
        category: Optional[str] = "3d",
        framework: Optional[str] = None,
        limit: int = 10,
        include_code: bool = True
    ) -> Dict[str, Any]:
        """
        Fetch 3D animation prompts from 21st.dev
        
        Args:
            query: Search term for animations
            category: Animation category filter
            framework: Technology filter (three.js, babylon.js, etc.)
            limit: Maximum results to return
            include_code: Include source code samples
        
        Returns:
            Dict with success status and animation results
        """
        logger.info(f"Fetching 3D animations from 21st.dev: {query}")
        
        # Import fetcher module
        try:
            from src.fetcher_21st_dev import Fetcher21stDev
            fetcher = Fetcher21stDev()
            
            results = fetcher.search(
                query=query,
                category=category,
                framework=framework,
                limit=limit,
                include_code=include_code
            )
            
            logger.info(f"Successfully fetched {len(results)} animations")
            return {
                "success": True,
                "animations_found": len(results),
                "animations": results
            }
        except Exception as e:
            logger.error(f"Error fetching animations: {e}")
            return {
                "success": False,
                "error": str(e),
                "animations_found": 0,
                "animations": []
            }
    
    def integrate_3d_animation(
        self,
        website_id: str,
        animation_id: str,
        page: str = "home",
        section: str = "hero",
        colors: Optional[List[str]] = None,
        scale: float = 1.0,
        speed: float = 1.0,
        intensity: str = "medium",
        auto_deploy: bool = False
    ) -> Dict[str, Any]:
        """
        Integrate a 3D animation into a website
        
        Args:
            website_id: Target website ID
            animation_id: Animation to integrate
            page: Target page name
            section: Target section name
            colors: Custom colors for animation
            scale: Size scaling factor
            speed: Animation speed multiplier
            intensity: Effect intensity (low, medium, high)
            auto_deploy: Auto-deploy after integration
        
        Returns:
            Dict with integration results
        """
        logger.info(f"Integrating animation {animation_id} into {website_id}")
        
        try:
            from src.animation_integrator import AnimationIntegrator
            integrator = AnimationIntegrator()
            
            result = integrator.integrate(
                website_id=website_id,
                animation_id=animation_id,
                page=page,
                section=section,
                colors=colors,
                scale=scale,
                speed=speed,
                intensity=intensity,
                auto_deploy=auto_deploy
            )
            
            logger.info(f"Successfully integrated animation")
            return {
                "success": True,
                "animation_integrated": True,
                **result
            }
        except Exception as e:
            logger.error(f"Error integrating animation: {e}")
            return {
                "success": False,
                "error": str(e),
                "animation_integrated": False
            }
    
    def search_21st_dev_animations(
        self,
        query: str,
        frameworks: Optional[List[str]] = None,
        complexity: Optional[str] = None,
        performance: Optional[str] = None,
        browser_support: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Search for 3D animations on 21st.dev with filtering
        
        Args:
            query: Search term
            frameworks: Technology filters
            complexity: beginner, intermediate, advanced
            performance: Performance level (high, medium, low)
            browser_support: Browser compatibility
        
        Returns:
            Dict with ranked animation results
        """
        logger.info(f"Searching 21st.dev for: {query}")
        
        try:
            from src.fetcher_21st_dev import Fetcher21stDev
            fetcher = Fetcher21stDev()
            
            results = fetcher.advanced_search(
                query=query,
                frameworks=frameworks,
                complexity=complexity,
                performance=performance,
                browser_support=browser_support
            )
            
            logger.info(f"Found {len(results)} matching animations")
            return {
                "success": True,
                "total_results": len(results),
                "best_matches": results
            }
        except Exception as e:
            logger.error(f"Error searching animations: {e}")
            return {
                "success": False,
                "error": str(e),
                "total_results": 0,
                "best_matches": []
            }
    
    def create_custom_3d_animation(
        self,
        prompt: str,
        framework: str = "three.js",
        use_cases: Optional[List[str]] = None,
        performance_target: int = 60,
        include_mobile: bool = True
    ) -> Dict[str, Any]:
        """
        Generate a custom 3D animation from a text prompt
        
        Args:
            prompt: Animation description
            framework: three.js or babylon.js
            use_cases: Intended use cases
            performance_target: Target FPS
            include_mobile: Mobile optimization
        
        Returns:
            Dict with generated code and metrics
        """
        logger.info(f"Creating custom 3D animation: {prompt}")
        
        try:
            if framework == "three.js":
                from src.three_js_generator import ThreeJsGenerator
                generator = ThreeJsGenerator()
            else:
                from src.babylon_js_generator import BabylonJsGenerator
                generator = BabylonJsGenerator()
            
            result = generator.generate(
                prompt=prompt,
                use_cases=use_cases,
                performance_target=performance_target,
                include_mobile=include_mobile
            )
            
            logger.info("Successfully generated custom animation")
            return {
                "success": True,
                "animation_generated": True,
                **result
            }
        except Exception as e:
            logger.error(f"Error generating animation: {e}")
            return {
                "success": False,
                "error": str(e),
                "animation_generated": False
            }
    
    def optimize_3d_performance(
        self,
        website_id: str,
        target_fps: int = 60,
        target_lighthouse: int = 95,
        include_mobile: bool = True,
        aggressive: bool = False
    ) -> Dict[str, Any]:
        """
        Optimize 3D animations for performance
        
        Args:
            website_id: Website to optimize
            target_fps: Target frame rate
            target_lighthouse: Target Lighthouse score
            include_mobile: Optimize for mobile
            aggressive: Apply aggressive optimizations
        
        Returns:
            Dict with optimization results
        """
        logger.info(f"Optimizing 3D performance for {website_id}")
        
        try:
            from src.performance_optimizer import PerformanceOptimizer
            optimizer = PerformanceOptimizer()
            
            result = optimizer.optimize(
                website_id=website_id,
                target_fps=target_fps,
                target_lighthouse=target_lighthouse,
                include_mobile=include_mobile,
                aggressive=aggressive
            )
            
            logger.info("Successfully optimized performance")
            return {
                "success": True,
                "optimizations_applied": True,
                **result
            }
        except Exception as e:
            logger.error(f"Error optimizing performance: {e}")
            return {
                "success": False,
                "error": str(e),
                "optimizations_applied": False
            }
    
    def batch_add_3d_to_websites(
        self,
        websites: List[Dict[str, Any]],
        max_parallel: int = 3,
        deploy_all: bool = False
    ) -> Dict[str, Any]:
        """
        Add 3D animations to multiple websites in parallel
        
        Args:
            websites: List of website configs
            max_parallel: Concurrent processing limit
            deploy_all: Deploy all after processing
        
        Returns:
            Dict with batch processing results
        """
        logger.info(f"Processing {len(websites)} websites in parallel")
        
        try:
            from src.animation_integrator import AnimationIntegrator
            integrator = AnimationIntegrator()
            
            result = integrator.batch_integrate(
                websites=websites,
                max_parallel=max_parallel,
                deploy_all=deploy_all
            )
            
            logger.info(f"Batch processing complete")
            return {
                "success": True,
                "websites_processed": len(websites),
                **result
            }
        except Exception as e:
            logger.error(f"Error in batch processing: {e}")
            return {
                "success": False,
                "error": str(e),
                "websites_processed": 0
            }
    
    def extract_21st_dev_prompts(
        self,
        category: Optional[str] = "3d",
        extract_prompts: bool = True,
        extract_code: bool = True,
        save_locally: bool = True,
        format: str = "markdown"
    ) -> Dict[str, Any]:
        """
        Extract animation prompts from 21st.dev for local caching
        
        Args:
            category: Animation category filter
            extract_prompts: Extract text prompts
            extract_code: Extract code samples
            save_locally: Save to local cache
            format: Output format (markdown or json)
        
        Returns:
            Dict with extraction results
        """
        logger.info(f"Extracting 21st.dev prompts (category: {category})")
        
        try:
            from src.fetcher_21st_dev import Fetcher21stDev
            from src.prompt_library import PromptLibrary
            
            fetcher = Fetcher21stDev()
            library = PromptLibrary()
            
            prompts = fetcher.extract_prompts(
                category=category,
                extract_code=extract_code
            )
            
            if save_locally:
                save_path = library.save_prompts(
                    prompts=prompts,
                    format=format
                )
            else:
                save_path = None
            
            logger.info(f"Extracted {len(prompts)} prompts")
            return {
                "success": True,
                "prompts_extracted": len(prompts),
                "saved_to": str(save_path) if save_path else None,
                "categories": list(set(p.get("category") for p in prompts))
            }
        except Exception as e:
            logger.error(f"Error extracting prompts: {e}")
            return {
                "success": False,
                "error": str(e),
                "prompts_extracted": 0
            }


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="3D Animations Skill - Fetch and integrate 3D effects into websites",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # fetch_3d_animations_from_21st
    fetch_parser = subparsers.add_parser(
        "fetch_3d_animations_from_21st",
        help="Fetch 3D animations from 21st.dev"
    )
    fetch_parser.add_argument("--query", required=True, help="Search term")
    fetch_parser.add_argument("--category", default="3d", help="Animation category")
    fetch_parser.add_argument("--framework", help="Technology filter")
    fetch_parser.add_argument("--limit", type=int, default=10, help="Max results")
    fetch_parser.add_argument("--include-code", action="store_true", help="Include code samples")
    
    # integrate_3d_animation
    integrate_parser = subparsers.add_parser(
        "integrate_3d_animation",
        help="Integrate 3D animation into website"
    )
    integrate_parser.add_argument("--website-id", required=True, help="Website ID")
    integrate_parser.add_argument("--animation-id", required=True, help="Animation ID")
    integrate_parser.add_argument("--page", default="home", help="Target page")
    integrate_parser.add_argument("--section", default="hero", help="Target section")
    integrate_parser.add_argument("--colors", help="Colors (comma-separated hex)")
    integrate_parser.add_argument("--scale", type=float, default=1.0, help="Scale factor")
    integrate_parser.add_argument("--speed", type=float, default=1.0, help="Speed multiplier")
    integrate_parser.add_argument("--intensity", default="medium", help="Intensity level")
    integrate_parser.add_argument("--auto-deploy", action="store_true", help="Auto-deploy")
    
    # search_21st_dev_animations
    search_parser = subparsers.add_parser(
        "search_21st_dev_animations",
        help="Search 21st.dev animations with filters"
    )
    search_parser.add_argument("--query", required=True, help="Search term")
    search_parser.add_argument("--frameworks", help="Frameworks (comma-separated)")
    search_parser.add_argument("--complexity", help="Complexity level")
    search_parser.add_argument("--performance", help="Performance level")
    search_parser.add_argument("--browser-support", help="Browser support")
    
    # create_custom_3d_animation
    create_parser = subparsers.add_parser(
        "create_custom_3d_animation",
        help="Create custom 3D animation from prompt"
    )
    create_parser.add_argument("--prompt", required=True, help="Animation description")
    create_parser.add_argument("--framework", default="three.js", help="Framework")
    create_parser.add_argument("--use-cases", help="Use cases (comma-separated)")
    create_parser.add_argument("--performance-target", type=int, default=60, help="Target FPS")
    create_parser.add_argument("--include-mobile", action="store_true", help="Mobile optimization")
    
    # optimize_3d_performance
    optimize_parser = subparsers.add_parser(
        "optimize_3d_performance",
        help="Optimize 3D performance"
    )
    optimize_parser.add_argument("--website-id", required=True, help="Website ID")
    optimize_parser.add_argument("--target-fps", type=int, default=60, help="Target FPS")
    optimize_parser.add_argument("--target-lighthouse", type=int, default=95, help="Target Lighthouse")
    optimize_parser.add_argument("--include-mobile", action="store_true", help="Mobile optimization")
    optimize_parser.add_argument("--aggressive", action="store_true", help="Aggressive optimizations")
    
    # batch_add_3d_to_websites
    batch_parser = subparsers.add_parser(
        "batch_add_3d_to_websites",
        help="Add 3D animations to multiple websites"
    )
    batch_parser.add_argument("--websites", required=True, help="JSON array of website configs")
    batch_parser.add_argument("--max-parallel", type=int, default=3, help="Concurrent limit")
    batch_parser.add_argument("--deploy-all", action="store_true", help="Deploy all")
    
    # extract_21st_dev_prompts
    extract_parser = subparsers.add_parser(
        "extract_21st_dev_prompts",
        help="Extract and cache 21st.dev prompts"
    )
    extract_parser.add_argument("--category", default="3d", help="Category filter")
    extract_parser.add_argument("--extract-prompts", action="store_true", help="Extract prompts")
    extract_parser.add_argument("--extract-code", action="store_true", help="Extract code")
    extract_parser.add_argument("--save-locally", action="store_true", help="Save locally")
    extract_parser.add_argument("--format", default="markdown", help="Output format")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    skill = ThreeDAnimationsSkill()
    
    try:
        if args.command == "fetch_3d_animations_from_21st":
            result = skill.fetch_3d_animations_from_21st(
                query=args.query,
                category=args.category,
                framework=args.framework,
                limit=args.limit,
                include_code=args.include_code
            )
        elif args.command == "integrate_3d_animation":
            colors = args.colors.split(",") if args.colors else None
            result = skill.integrate_3d_animation(
                website_id=args.website_id,
                animation_id=args.animation_id,
                page=args.page,
                section=args.section,
                colors=colors,
                scale=args.scale,
                speed=args.speed,
                intensity=args.intensity,
                auto_deploy=args.auto_deploy
            )
        elif args.command == "search_21st_dev_animations":
            frameworks = args.frameworks.split(",") if args.frameworks else None
            result = skill.search_21st_dev_animations(
                query=args.query,
                frameworks=frameworks,
                complexity=args.complexity,
                performance=args.performance,
                browser_support=args.browser_support
            )
        elif args.command == "create_custom_3d_animation":
            use_cases = args.use_cases.split(",") if args.use_cases else None
            result = skill.create_custom_3d_animation(
                prompt=args.prompt,
                framework=args.framework,
                use_cases=use_cases,
                performance_target=args.performance_target,
                include_mobile=args.include_mobile
            )
        elif args.command == "optimize_3d_performance":
            result = skill.optimize_3d_performance(
                website_id=args.website_id,
                target_fps=args.target_fps,
                target_lighthouse=args.target_lighthouse,
                include_mobile=args.include_mobile,
                aggressive=args.aggressive
            )
        elif args.command == "batch_add_3d_to_websites":
            websites = json.loads(args.websites)
            result = skill.batch_add_3d_to_websites(
                websites=websites,
                max_parallel=args.max_parallel,
                deploy_all=args.deploy_all
            )
        elif args.command == "extract_21st_dev_prompts":
            result = skill.extract_21st_dev_prompts(
                category=args.category,
                extract_prompts=args.extract_prompts,
                extract_code=args.extract_code,
                save_locally=args.save_locally,
                format=args.format
            )
        else:
            print(f"Unknown command: {args.command}")
            sys.exit(1)
        
        print(json.dumps(result, indent=2))
        sys.exit(0 if result.get("success") else 1)
    
    except Exception as e:
        logger.error(f"Command failed: {e}", exc_info=True)
        print(json.dumps({"success": False, "error": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
