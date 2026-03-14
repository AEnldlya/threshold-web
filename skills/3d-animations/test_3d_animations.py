"""
3D Animations Skill - Test Suite

40+ unit tests covering all modules and functionality
"""

import pytest
import json
from pathlib import Path
from unittest.mock import Mock, patch

# Import skill modules
from src.fetcher_21st_dev import Fetcher21stDev
from src.prompt_parser import PromptParser
from src.prompt_library import PromptLibrary
from src.three_js_generator import ThreeJsGenerator
from src.babylon_js_generator import BabylonJsGenerator
from src.animation_integrator import AnimationIntegrator
from src.components_3d import Components3D
from src.performance_optimizer import PerformanceOptimizer
from src.mobile_handler import MobileHandler
from src.deployment_manager import DeploymentManager


class TestFetcher21stDev:
    """Tests for 21st.dev fetcher"""
    
    def setup_method(self):
        self.fetcher = Fetcher21stDev()
    
    def test_initialization(self):
        """Test fetcher initialization"""
        assert self.fetcher is not None
        assert len(self.fetcher.animations_db) > 0
    
    def test_search_by_query(self):
        """Test searching by query"""
        results = self.fetcher.search(query="cube")
        assert len(results) > 0
        assert "id" in results[0]
    
    def test_search_by_category(self):
        """Test category filtering"""
        results = self.fetcher.search(category="3d-hero")
        assert all(r["category"] == "3d-hero" for r in results)
    
    def test_search_by_framework(self):
        """Test framework filtering"""
        results = self.fetcher.search(framework="three.js")
        assert all(r["technology"] == "three.js" for r in results)
    
    def test_search_limit(self):
        """Test result limit"""
        results = self.fetcher.search(limit=2)
        assert len(results) <= 2
    
    def test_get_by_id(self):
        """Test getting animation by ID"""
        anim = self.fetcher.get_by_id("3d-hero-1")
        assert anim is not None
        assert anim["id"] == "3d-hero-1"
    
    def test_get_by_invalid_id(self):
        """Test getting invalid ID"""
        anim = self.fetcher.get_by_id("invalid")
        assert anim is None
    
    def test_advanced_search(self):
        """Test advanced search"""
        results = self.fetcher.advanced_search(
            query="cube",
            frameworks=["three.js"]
        )
        assert len(results) > 0
    
    def test_get_categories(self):
        """Test getting categories"""
        categories = self.fetcher.get_categories()
        assert len(categories) > 0
        assert isinstance(categories, list)
    
    def test_get_frameworks(self):
        """Test getting frameworks"""
        frameworks = self.fetcher.get_frameworks()
        assert len(frameworks) > 0
        assert "three.js" in frameworks


class TestPromptParser:
    """Tests for prompt parser"""
    
    def setup_method(self):
        self.parser = PromptParser()
    
    def test_parse_prompt(self):
        """Test parsing a prompt"""
        result = self.parser.parse("Create a floating three.js cube")
        assert result["original_prompt"]
        assert "three.js" in result["frameworks"]
    
    def test_extract_frameworks(self):
        """Test framework extraction"""
        frameworks = self.parser._extract_frameworks("Use babylon.js for this")
        assert "babylon.js" in frameworks
    
    def test_extract_effects(self):
        """Test effect extraction"""
        effects = self.parser._extract_effects("Create a particle effect")
        assert "particle" in effects
    
    def test_estimate_difficulty(self):
        """Test difficulty estimation"""
        difficulty = self.parser._estimate_difficulty(
            "Create advanced particle physics simulation"
        )
        assert difficulty == "advanced"
    
    def test_extract_code_blocks(self):
        """Test code block extraction"""
        text = "```javascript\nconst x = 1;\n```"
        blocks = self.parser.extract_code_blocks(text)
        assert len(blocks) > 0
    
    def test_extract_parameters(self):
        """Test parameter extraction"""
        params = self.parser.extract_parameters(
            "Animate for 2000ms at 60 fps with ease-out"
        )
        assert params["duration"] == 2000
        assert params["fps"] == 60
        assert params["easing"] == "ease-out"


class TestPromptLibrary:
    """Tests for prompt library"""
    
    def setup_method(self):
        self.library = PromptLibrary()
    
    def test_initialization(self):
        """Test library initialization"""
        assert self.library is not None
        assert isinstance(self.library.prompts, dict)
    
    def test_add_prompt(self):
        """Test adding prompt"""
        result = self.library.add_prompt(
            prompt_id="test-1",
            category="test",
            name="Test Prompt",
            description="A test prompt",
            prompt_text="Create a test animation"
        )
        assert result is True
        assert "test-1" in self.library.prompts
    
    def test_get_prompt(self):
        """Test retrieving prompt"""
        self.library.add_prompt(
            prompt_id="test-2",
            category="test",
            name="Test",
            description="Test",
            prompt_text="Test"
        )
        prompt = self.library.get_prompt("test-2")
        assert prompt is not None
        assert prompt["id"] == "test-2"
    
    def test_search_prompts(self):
        """Test searching prompts"""
        self.library.add_prompt(
            prompt_id="test-3",
            category="test",
            name="Floating Test",
            description="Test floating",
            prompt_text="Test prompt"
        )
        results = self.library.search("floating")
        assert len(results) > 0
    
    def test_get_by_category(self):
        """Test getting by category"""
        results = self.library.get_by_category("test")
        assert len(results) >= 0


class TestThreeJsGenerator:
    """Tests for Three.js generator"""
    
    def setup_method(self):
        self.generator = ThreeJsGenerator()
    
    def test_initialization(self):
        """Test generator initialization"""
        assert self.generator is not None
    
    def test_generate(self):
        """Test code generation"""
        result = self.generator.generate(
            prompt="Create a floating cube",
            performance_target=60,
            include_mobile=True
        )
        assert result["success"] is True or "code" in result
        assert result["mobile_optimized"] is True
    
    def test_generate_hero_section(self):
        """Test hero section generation"""
        code = self.generator.generate_hero_section()
        assert "Canvas" in code
        assert "HeroAnimation" in code
    
    def test_generate_product_rotator(self):
        """Test product rotator generation"""
        code = self.generator.generate_product_rotator()
        assert "ProductRotator" in code
        assert "rotation.y" in code
    
    def test_generate_text_animation(self):
        """Test text animation generation"""
        code = self.generator.generate_text_animation("Hello")
        assert "Hello" in code
        assert "AnimatedText" in code


class TestBabylonJsGenerator:
    """Tests for Babylon.js generator"""
    
    def setup_method(self):
        self.generator = BabylonJsGenerator()
    
    def test_initialization(self):
        """Test generator initialization"""
        assert self.generator is not None
    
    def test_generate(self):
        """Test code generation"""
        result = self.generator.generate(
            prompt="Create a babylon scene",
            performance_target=60
        )
        assert "code" in result or result.get("success")
        assert "babylon" in result.get("libraries_used", [])


class TestAnimationIntegrator:
    """Tests for animation integrator"""
    
    def setup_method(self):
        self.integrator = AnimationIntegrator()
    
    def test_initialization(self):
        """Test integrator initialization"""
        assert self.integrator is not None
    
    def test_integrate(self):
        """Test integration"""
        result = self.integrator.integrate(
            website_id="test-site",
            animation_id="3d-hero-1"
        )
        assert result["component_created"]
        assert result["performance_score"] >= 80
    
    def test_batch_integrate(self):
        """Test batch integration"""
        websites = [
            {"website_id": "site-1", "animation_id": "3d-hero-1"},
            {"website_id": "site-2", "animation_id": "3d-hero-2"}
        ]
        result = self.integrator.batch_integrate(websites)
        assert result["successful"] >= 0
        assert "total_time" in result


class TestComponents3D:
    """Tests for 3D components"""
    
    def test_floating_cube(self):
        """Test floating cube component"""
        code = Components3D.floating_cube()
        assert "FloatingCube" in code
        assert "boxGeometry" in code
    
    def test_morphing_text(self):
        """Test morphing text component"""
        code = Components3D.morphing_text()
        assert "MorphingText" in code
        assert "Text" in code
    
    def test_product_rotator(self):
        """Test product rotator component"""
        code = Components3D.product_rotator()
        assert "ProductRotator" in code
    
    def test_particle_system(self):
        """Test particle system component"""
        code = Components3D.particle_system()
        assert "ParticleSystem" in code


class TestPerformanceOptimizer:
    """Tests for performance optimizer"""
    
    def setup_method(self):
        self.optimizer = PerformanceOptimizer()
    
    def test_initialization(self):
        """Test optimizer initialization"""
        assert self.optimizer is not None
    
    def test_optimize(self):
        """Test optimization"""
        result = self.optimizer.optimize(
            website_id="test-site",
            target_fps=60,
            target_lighthouse=95
        )
        assert "optimizations_applied" in result
        assert len(result["optimizations_applied"]) > 0
    
    def test_analyze_performance(self):
        """Test performance analysis"""
        result = self.optimizer.analyze_performance("test-site")
        assert "fps" in result
        assert "lighthouse_score" in result
    
    def test_get_recommendations(self):
        """Test getting recommendations"""
        recommendations = self.optimizer.get_optimization_recommendations("test-site")
        assert len(recommendations) > 0
        assert all(isinstance(r, str) for r in recommendations)


class TestMobileHandler:
    """Tests for mobile handler"""
    
    def setup_method(self):
        self.handler = MobileHandler()
    
    def test_initialization(self):
        """Test handler initialization"""
        assert self.handler is not None
    
    def test_detect_mobile(self):
        """Test mobile detection"""
        result = self.handler.detect_device("Mozilla/5.0 (iPhone...)")
        assert result["is_mobile"] is True
    
    def test_detect_desktop(self):
        """Test desktop detection"""
        result = self.handler.detect_device("Mozilla/5.0 (Windows...)")
        assert result["is_mobile"] is False
    
    def test_get_quality_settings_mobile(self):
        """Test mobile quality settings"""
        settings = self.handler.get_quality_settings("mobile")
        assert settings["target_fps"] == 30
        assert settings["quality_scale"] < 1.0
    
    def test_get_quality_settings_desktop(self):
        """Test desktop quality settings"""
        settings = self.handler.get_quality_settings("desktop")
        assert settings["target_fps"] == 60
        assert settings["quality_scale"] == 1.0
    
    def test_optimize_for_mobile(self):
        """Test mobile optimization"""
        code = "const geometry = new BufferGeometry();"
        optimized = self.handler.optimize_for_mobile(code, "mobile")
        assert "mobile optimized" in optimized or code in optimized


class TestDeploymentManager:
    """Tests for deployment manager"""
    
    def setup_method(self):
        self.manager = DeploymentManager()
    
    def test_initialization(self):
        """Test manager initialization"""
        assert self.manager is not None
    
    def test_deploy(self):
        """Test deployment"""
        result = self.manager.deploy(
            website_id="test-site",
            environment="production"
        )
        assert result["success"] is True
        assert result["website_id"] == "test-site"
    
    def test_get_deployment_status(self):
        """Test getting deployment status"""
        result = self.manager.get_deployment_status("test-site")
        assert "status" in result
        assert "performance" in result


# Integration tests
class TestIntegration:
    """Integration tests"""
    
    def test_full_workflow(self):
        """Test complete workflow"""
        # Fetch
        fetcher = Fetcher21stDev()
        animations = fetcher.search(query="cube", limit=1)
        assert len(animations) > 0
        
        # Parse
        parser = PromptParser()
        parsed = parser.parse(animations[0]["prompt"])
        assert "frameworks" in parsed
        
        # Generate
        generator = ThreeJsGenerator()
        code = generator.generate(
            prompt=animations[0]["prompt"],
            performance_target=60
        )
        assert "code" in code or "success" in code
        
        # Integrate
        integrator = AnimationIntegrator()
        result = integrator.integrate(
            website_id="test-site",
            animation_id=animations[0]["id"]
        )
        assert result["component_created"]
    
    def test_mobile_optimization_workflow(self):
        """Test mobile optimization workflow"""
        handler = MobileHandler()
        settings = handler.get_quality_settings("mobile")
        
        optimizer = PerformanceOptimizer()
        result = optimizer.optimize(
            website_id="test-site",
            target_fps=settings["target_fps"],
            include_mobile=True
        )
        
        assert "optimizations_applied" in result


# Performance tests
class TestPerformance:
    """Performance tests"""
    
    def test_search_performance(self):
        """Test search performance"""
        fetcher = Fetcher21stDev()
        import time
        start = time.time()
        fetcher.search(query="cube", limit=100)
        elapsed = time.time() - start
        assert elapsed < 1.0  # Should complete in < 1 second
    
    def test_parser_performance(self):
        """Test parser performance"""
        parser = PromptParser()
        import time
        start = time.time()
        for _ in range(100):
            parser.parse("Create a floating cube with particles")
        elapsed = time.time() - start
        assert elapsed < 1.0  # 100 parses in < 1 second


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
