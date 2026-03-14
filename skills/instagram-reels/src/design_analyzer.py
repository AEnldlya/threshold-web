"""
Design Analyzer for Instagram Reels

Analyzes design patterns, colors, typography, and layout
from reel metadata and visual content.
"""

import logging
from typing import Dict, List, Any, Optional
import re
import json


logger = logging.getLogger(__name__)


class DesignAnalyzer:
    """Analyze design patterns from reel metadata."""
    
    # Common animation patterns
    ANIMATION_PATTERNS = {
        'fade': ['fade', 'opacity', 'transparent'],
        'slide': ['slide', 'translate', 'move'],
        'rotate': ['rotate', 'spin', 'rotation'],
        'scale': ['scale', 'zoom', 'grow', 'shrink'],
        'bounce': ['bounce', 'elastic'],
        'flip': ['flip', 'flip-x', 'flip-y'],
        'skew': ['skew', 'distort'],
    }
    
    # Common UI frameworks/libraries
    FRAMEWORK_KEYWORDS = {
        'framer': ['framer', 'framer motion'],
        'react': ['react', 'jsx'],
        'vue': ['vue', 'vuejs'],
        'tailwind': ['tailwind', 'tw-'],
        'gsap': ['gsap', 'greensock'],
        'three': ['three.js', 'threejs', '3d'],
        'webgl': ['webgl', 'gl'],
        'canvas': ['canvas', 'p5.js'],
    }
    
    # Typography patterns
    FONT_KEYWORDS = {
        'sans-serif': ['sans', 'helvetica', 'arial', 'inter', 'roboto', 'poppins'],
        'serif': ['serif', 'georgia', 'times', 'playfair'],
        'mono': ['mono', 'courier', 'code', 'monospace'],
        'script': ['script', 'cursive', 'handwriting'],
    }
    
    def __init__(self):
        """Initialize design analyzer."""
        pass
    
    def analyze(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze design patterns from reel metadata.
        
        Args:
            metadata: Reel metadata dictionary
            
        Returns:
            Dictionary with design analysis
        """
        analysis = {
            "animations": self._detect_animations(metadata),
            "layout": self._detect_layout(metadata),
            "typography": self._detect_typography(metadata),
            "colors": self._detect_colors(metadata),
            "techniques": self._detect_techniques(metadata),
            "ui_elements": self._detect_ui_elements(metadata),
            "interactions": self._detect_interactions(metadata),
        }
        
        return {key: val for key, val in analysis.items() if val}
    
    def _detect_animations(self, metadata: Dict[str, Any]) -> List[str]:
        """
        Detect animation types from description and metadata.
        
        Args:
            metadata: Reel metadata
            
        Returns:
            List of detected animation types
        """
        detected = set()
        text = (metadata.get('description', '') or '').lower()
        
        for anim_type, keywords in self.ANIMATION_PATTERNS.items():
            for keyword in keywords:
                if keyword in text:
                    detected.add(anim_type)
                    break
        
        return sorted(list(detected))
    
    def _detect_layout(self, metadata: Dict[str, Any]) -> Optional[str]:
        """
        Detect layout type from description.
        
        Args:
            metadata: Reel metadata
            
        Returns:
            Layout description or None
        """
        text = (metadata.get('description', '') or '').lower()
        
        layout_keywords = {
            'hero': ['hero', 'landing', 'full-screen', 'fullscreen'],
            'card': ['card', 'grid', 'layout'],
            'sidebar': ['sidebar', 'navigation', 'menu'],
            'modal': ['modal', 'popup', 'dialog'],
            'banner': ['banner', 'header', 'top'],
            'footer': ['footer', 'bottom'],
        }
        
        for layout_type, keywords in layout_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    return layout_type
        
        return None
    
    def _detect_typography(self, metadata: Dict[str, Any]) -> Optional[str]:
        """
        Detect typography style from description.
        
        Args:
            metadata: Reel metadata
            
        Returns:
            Typography description or None
        """
        text = (metadata.get('description', '') or '').lower()
        
        for font_type, keywords in self.FONT_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text:
                    return font_type
        
        # Default inference
        if any(word in text for word in ['bold', 'heading', 'title']):
            return 'sans-serif'
        
        return None
    
    def _detect_colors(self, metadata: Dict[str, Any]) -> List[str]:
        """
        Detect colors from description.
        
        Args:
            metadata: Reel metadata
            
        Returns:
            List of color descriptions
        """
        detected = []
        text = (metadata.get('description', '') or '').lower()
        
        # Color names
        color_keywords = [
            'black', 'white', 'gray', 'grey', 'red', 'blue', 'green',
            'yellow', 'orange', 'purple', 'pink', 'cyan', 'magenta',
            'dark', 'light', 'bright', 'muted', 'vibrant', 'pastel'
        ]
        
        for color in color_keywords:
            if color in text:
                detected.append(color)
        
        # Hex color patterns
        hex_pattern = r'#[0-9a-f]{6}'
        hex_matches = re.findall(hex_pattern, text, re.IGNORECASE)
        detected.extend(hex_matches)
        
        return list(set(detected))
    
    def _detect_techniques(self, metadata: Dict[str, Any]) -> List[str]:
        """
        Detect technical implementations from description.
        
        Args:
            metadata: Reel metadata
            
        Returns:
            List of detected techniques/frameworks
        """
        detected = []
        text = (metadata.get('description', '') or '').lower()
        creator = (metadata.get('creator', '') or '').lower()
        
        # Combine text sources
        full_text = f"{text} {creator}"
        
        for framework, keywords in self.FRAMEWORK_KEYWORDS.items():
            for keyword in keywords:
                if keyword in full_text:
                    detected.append(framework)
                    break
        
        return sorted(list(set(detected)))
    
    def _detect_ui_elements(self, metadata: Dict[str, Any]) -> List[str]:
        """
        Detect UI elements from description.
        
        Args:
            metadata: Reel metadata
            
        Returns:
            List of detected UI elements
        """
        detected = []
        text = (metadata.get('description', '') or '').lower()
        
        ui_elements = [
            'button', 'input', 'form', 'dropdown', 'menu', 'navbar',
            'sidebar', 'card', 'badge', 'tooltip', 'modal', 'dialog',
            'tabs', 'pagination', 'progress', 'slider', 'checkbox',
            'radio', 'select', 'search', 'autocomplete', 'datepicker'
        ]
        
        for element in ui_elements:
            if element in text:
                detected.append(element)
        
        return detected
    
    def _detect_interactions(self, metadata: Dict[str, Any]) -> List[str]:
        """
        Detect interaction patterns from description.
        
        Args:
            metadata: Reel metadata
            
        Returns:
            List of detected interactions
        """
        detected = []
        text = (metadata.get('description', '') or '').lower()
        
        interactions = [
            'hover', 'click', 'drag', 'scroll', 'swipe', 'gesture',
            'touch', 'keyboard', 'focus', 'blur', 'transition',
            'morphing', 'parallax', 'lazy-load', 'infinite-scroll'
        ]
        
        for interaction in interactions:
            if interaction in text:
                detected.append(interaction)
        
        return detected
    
    def generate_summary(self, analysis: Dict[str, Any]) -> str:
        """
        Generate human-readable design summary.
        
        Args:
            analysis: Design analysis dictionary
            
        Returns:
            Formatted summary string
        """
        parts = []
        
        if analysis.get('animations'):
            parts.append(f"Animations: {', '.join(analysis['animations'])}")
        
        if analysis.get('layout'):
            parts.append(f"Layout: {analysis['layout']}")
        
        if analysis.get('typography'):
            parts.append(f"Typography: {analysis['typography']}")
        
        if analysis.get('colors'):
            parts.append(f"Colors: {', '.join(analysis['colors'][:5])}")
        
        if analysis.get('techniques'):
            parts.append(f"Techniques: {', '.join(analysis['techniques'][:3])}")
        
        if analysis.get('ui_elements'):
            parts.append(f"UI Elements: {', '.join(analysis['ui_elements'][:3])}")
        
        if analysis.get('interactions'):
            parts.append(f"Interactions: {', '.join(analysis['interactions'][:3])}")
        
        return " | ".join(parts) if parts else "Design pattern recognition in progress..."


def main():
    """Test design analyzer."""
    analyzer = DesignAnalyzer()
    
    # Test metadata
    test_metadata = {
        'description': 'Beautiful fade-in and slide-up animations on hero section. Dark theme with white text. Built with Framer Motion and React. Smooth transitions with GSAP.',
        'creator': 'design_inspiration'
    }
    
    analysis = analyzer.analyze(test_metadata)
    print("Design Analysis:")
    print(json.dumps(analysis, indent=2))
    
    print("\nSummary:")
    print(analyzer.generate_summary(analysis))


if __name__ == '__main__':
    main()
