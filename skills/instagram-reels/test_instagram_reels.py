#!/usr/bin/env python3
"""
Unit Tests for Instagram Reels Skill

Test URL parsing, design analysis, and markdown formatting.
"""

import unittest
import sys
from pathlib import Path
import json

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src import (
    URLParser,
    DesignAnalyzer,
    MarkdownFormatter,
    CacheManager
)


class TestURLParser(unittest.TestCase):
    """Test URL parsing functionality."""
    
    def test_extract_reel_id_basic(self):
        """Test extracting reel ID from basic URL."""
        url = "https://www.instagram.com/reel/DUHmsKkjZw0/"
        reel_id = URLParser.extract_reel_id(url)
        self.assertEqual(reel_id, "DUHmsKkjZw0")
    
    def test_extract_reel_id_with_params(self):
        """Test extracting reel ID from URL with query parameters."""
        url = "https://www.instagram.com/reel/ABC123/?igsh=YTQ4YzNnNG50OGVt"
        reel_id = URLParser.extract_reel_id(url)
        self.assertEqual(reel_id, "ABC123")
    
    def test_extract_reel_id_short_url(self):
        """Test extracting reel ID from short URL."""
        url = "https://instagram.com/reel/XYZ789/"
        reel_id = URLParser.extract_reel_id(url)
        self.assertEqual(reel_id, "XYZ789")
    
    def test_is_reel_url_valid(self):
        """Test identifying valid reel URLs."""
        valid_urls = [
            "https://www.instagram.com/reel/DUHmsKkjZw0/",
            "https://instagram.com/reel/ABC123/",
            "https://www.instagram.com/reel/TEST/?igsh=xyz"
        ]
        for url in valid_urls:
            self.assertTrue(URLParser.is_reel_url(url))
    
    def test_is_reel_url_invalid(self):
        """Test identifying invalid reel URLs."""
        invalid_urls = [
            "https://www.instagram.com/username/",
            "https://www.instagram.com/",
            "not_a_url",
            ""
        ]
        for url in invalid_urls:
            self.assertFalse(URLParser.is_reel_url(url))
    
    def test_classify_url_reel(self):
        """Test classifying reel URL."""
        url_type, identifier = URLParser.classify_url("https://www.instagram.com/reel/ABC123/")
        self.assertEqual(url_type, 'reel')
        self.assertEqual(identifier, 'ABC123')
    
    def test_classify_url_account(self):
        """Test classifying account URL."""
        url_type, identifier = URLParser.classify_url("https://www.instagram.com/design_inspiration/")
        self.assertEqual(url_type, 'account')
        self.assertEqual(identifier, 'design_inspiration')
    
    def test_normalize_url(self):
        """Test URL normalization."""
        url = "https://instagram.com/reel/ABC/?igsh=xyz"
        normalized = URLParser.normalize_url(url)
        self.assertEqual(normalized, "https://www.instagram.com/reel/ABC/")


class TestDesignAnalyzer(unittest.TestCase):
    """Test design pattern analysis."""
    
    def setUp(self):
        """Set up test analyzer."""
        self.analyzer = DesignAnalyzer()
    
    def test_detect_animations(self):
        """Test animation detection."""
        metadata = {
            'description': 'Beautiful fade-in and slide-up animations on hero section'
        }
        animations = self.analyzer._detect_animations(metadata)
        self.assertIn('fade', animations)
        self.assertIn('slide', animations)
    
    def test_detect_layout_hero(self):
        """Test hero layout detection."""
        metadata = {
            'description': 'Full-screen hero section with animations'
        }
        layout = self.analyzer._detect_layout(metadata)
        self.assertEqual(layout, 'hero')
    
    def test_detect_layout_card(self):
        """Test card layout detection."""
        metadata = {
            'description': 'Grid of cards with hover effects'
        }
        layout = self.analyzer._detect_layout(metadata)
        self.assertEqual(layout, 'card')
    
    def test_detect_typography(self):
        """Test typography detection."""
        metadata = {
            'description': 'Bold sans-serif headlines with smooth transitions'
        }
        typography = self.analyzer._detect_typography(metadata)
        self.assertEqual(typography, 'sans-serif')
    
    def test_detect_colors(self):
        """Test color detection."""
        metadata = {
            'description': 'Dark theme with white text and blue accents'
        }
        colors = self.analyzer._detect_colors(metadata)
        self.assertIn('dark', colors)
        self.assertIn('white', colors)
        self.assertIn('blue', colors)
    
    def test_detect_colors_hex(self):
        """Test hex color detection."""
        metadata = {
            'description': 'Using colors #1a1a1a and #ffffff'
        }
        colors = self.analyzer._detect_colors(metadata)
        self.assertIn('#1a1a1a', colors)
        self.assertIn('#ffffff', colors)
    
    def test_detect_techniques(self):
        """Test technique detection."""
        metadata = {
            'description': 'Built with Framer Motion and React'
        }
        techniques = self.analyzer._detect_techniques(metadata)
        self.assertIn('framer', techniques)
        self.assertIn('react', techniques)
    
    def test_full_analysis(self):
        """Test full design analysis."""
        metadata = {
            'description': 'Beautiful fade-in animations on hero section. Dark theme with white text. Built with Framer Motion and React.',
            'creator': 'design_inspiration'
        }
        analysis = self.analyzer.analyze(metadata)
        
        # Should have extracted multiple patterns
        self.assertGreater(len(analysis), 0)
        self.assertIn('animations', analysis)
        self.assertIn('techniques', analysis)
    
    def test_generate_summary(self):
        """Test summary generation."""
        analysis = {
            'animations': ['fade', 'slide'],
            'layout': 'hero',
            'typography': 'sans-serif',
            'colors': ['#000000', '#ffffff']
        }
        summary = self.analyzer.generate_summary(analysis)
        self.assertIn('fade', summary)
        self.assertIn('hero', summary)
        self.assertIn('sans-serif', summary)


class TestMarkdownFormatter(unittest.TestCase):
    """Test markdown formatting."""
    
    def setUp(self):
        """Set up test formatter."""
        self.formatter = MarkdownFormatter("/tmp/test_references.md")
    
    def test_format_entry(self):
        """Test entry formatting."""
        analysis = {
            'animations': ['fade', 'slide'],
            'layout': 'hero'
        }
        entry = self.formatter.format_entry(
            reel_id="TEST123",
            creator="test_user",
            description="Test description",
            design_analysis=analysis,
            custom_notes="Test notes"
        )
        
        self.assertIn("TEST123", entry)
        self.assertIn("test_user", entry)
        self.assertIn("Test description", entry)
        self.assertIn("fade", entry)
        self.assertIn("hero", entry)
    
    def test_generate_topic_from_analysis(self):
        """Test auto-generating topic from analysis."""
        analysis = {
            'layout': 'hero',
            'animations': ['fade', 'slide', 'scale']
        }
        topic = self.formatter._generate_topic(analysis)
        self.assertIn("Hero", topic)
        self.assertIn("3 animations", topic)
    
    def test_format_design_analysis(self):
        """Test formatting design analysis for markdown."""
        analysis = {
            'animations': ['fade', 'slide'],
            'layout': 'hero',
            'colors': ['#1a1a1a', '#ffffff'],
            'techniques': ['framer', 'react']
        }
        formatted = self.formatter._format_design_analysis(analysis)
        
        self.assertIn("Animations", formatted)
        self.assertIn("Layout", formatted)
        self.assertIn("Colors", formatted)
        self.assertIn("Techniques", formatted)


class TestCacheManager(unittest.TestCase):
    """Test caching functionality."""
    
    def setUp(self):
        """Set up test cache manager."""
        self.cache = CacheManager("/tmp/test_cache")
    
    def test_cache_set_get(self):
        """Test setting and getting cache."""
        test_data = {
            "reel_id": "TEST123",
            "creator": "test_user",
            "description": "Test"
        }
        
        # Set cache
        self.cache.set("TEST123", test_data)
        self.assertTrue(self.cache.exists("TEST123"))
        
        # Get cache
        cached = self.cache.get("TEST123")
        self.assertEqual(cached["reel_id"], test_data["reel_id"])
    
    def test_cache_delete(self):
        """Test deleting cache entry."""
        test_data = {"test": "data"}
        self.cache.set("TEST_DELETE", test_data)
        self.assertTrue(self.cache.exists("TEST_DELETE"))
        
        self.cache.delete("TEST_DELETE")
        self.assertFalse(self.cache.exists("TEST_DELETE"))
    
    def test_cache_list_cached(self):
        """Test listing cached entries."""
        self.cache.set("TEST1", {"data": "1"})
        self.cache.set("TEST2", {"data": "2"})
        
        cached_list = self.cache.list_cached()
        self.assertIn("TEST1", cached_list)
        self.assertIn("TEST2", cached_list)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestURLParser))
    suite.addTests(loader.loadTestsFromTestCase(TestDesignAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestMarkdownFormatter))
    suite.addTests(loader.loadTestsFromTestCase(TestCacheManager))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    exit_code = run_tests()
    sys.exit(exit_code)
