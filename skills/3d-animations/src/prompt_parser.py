"""
Prompt Parser

Parses animation prompts to extract key concepts, frameworks, and parameters
"""

import logging
import re
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class PromptParser:
    """Parse animation prompts"""
    
    def __init__(self):
        """Initialize parser"""
        self.frameworks = ["three.js", "babylon.js", "pixi.js", "gsap", "framer-motion"]
        self.effects = ["particle", "morphing", "flying", "rotating", "floating", "glitch", "ripple"]
        self.technologies = ["webgl", "canvas", "svg", "css", "javascript"]
    
    def parse(self, prompt: str) -> Dict[str, Any]:
        """
        Parse animation prompt
        
        Args:
            prompt: Animation prompt text
        
        Returns:
            Dict with parsed concepts, frameworks, etc.
        """
        logger.info(f"Parsing prompt: {prompt[:50]}...")
        
        result = {
            "original_prompt": prompt,
            "frameworks": self._extract_frameworks(prompt),
            "effects": self._extract_effects(prompt),
            "technologies": self._extract_technologies(prompt),
            "concepts": self._extract_concepts(prompt),
            "difficulty": self._estimate_difficulty(prompt),
            "variants": self._generate_variants(prompt),
        }
        
        logger.info(f"Parsed prompt: {len(result['concepts'])} concepts, {len(result['effects'])} effects")
        return result
    
    def _extract_frameworks(self, prompt: str) -> List[str]:
        """Extract framework mentions"""
        prompt_lower = prompt.lower()
        found = []
        
        for fw in self.frameworks:
            if fw in prompt_lower:
                found.append(fw)
        
        # If no framework specified, default to three.js
        if not found:
            found.append("three.js")
        
        return found
    
    def _extract_effects(self, prompt: str) -> List[str]:
        """Extract effect types"""
        prompt_lower = prompt.lower()
        found = []
        
        for effect in self.effects:
            if effect in prompt_lower:
                found.append(effect)
        
        return found
    
    def _extract_technologies(self, prompt: str) -> List[str]:
        """Extract technology mentions"""
        prompt_lower = prompt.lower()
        found = []
        
        for tech in self.technologies:
            if tech in prompt_lower:
                found.append(tech)
        
        return found
    
    def _extract_concepts(self, prompt: str) -> List[str]:
        """Extract key concepts"""
        # Simple concept extraction - split by common delimiters
        concepts = []
        
        # Extract phrases in quotes
        quoted = re.findall(r'"([^"]+)"', prompt)
        concepts.extend(quoted)
        
        # Extract capitalized phrases
        capitalized = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', prompt)
        concepts.extend(capitalized)
        
        # Extract common animation concepts
        animation_words = ["animate", "transition", "morph", "rotate", "scale", "slide", "fade"]
        for word in animation_words:
            if word.lower() in prompt.lower():
                concepts.append(word)
        
        return list(set(concepts))
    
    def _estimate_difficulty(self, prompt: str) -> str:
        """Estimate difficulty level"""
        prompt_lower = prompt.lower()
        
        advanced_keywords = ["advanced", "complex", "multiple", "interactive", "physics", "3d model"]
        intermediate_keywords = ["morphing", "particle", "interactive", "effect"]
        
        advanced_count = sum(1 for kw in advanced_keywords if kw in prompt_lower)
        intermediate_count = sum(1 for kw in intermediate_keywords if kw in prompt_lower)
        
        if advanced_count >= 2:
            return "advanced"
        elif intermediate_count >= 1:
            return "intermediate"
        else:
            return "beginner"
    
    def _generate_variants(self, prompt: str) -> List[Dict[str, str]]:
        """Generate prompt variants"""
        variants = [
            {
                "name": "desktop_optimized",
                "description": f"{prompt} (optimized for desktop 60 FPS)"
            },
            {
                "name": "mobile_optimized",
                "description": f"{prompt} (optimized for mobile 30 FPS)"
            },
            {
                "name": "lightweight",
                "description": f"{prompt} (lightweight, minimal dependencies)"
            },
            {
                "name": "high_quality",
                "description": f"{prompt} (high quality, no performance limit)"
            },
        ]
        
        return variants
    
    def extract_code_blocks(self, text: str) -> List[str]:
        """Extract code blocks from text"""
        # Match triple backtick blocks
        code_blocks = re.findall(r'```(?:javascript|typescript|tsx|jsx)?\n(.*?)```', text, re.DOTALL)
        return code_blocks
    
    def extract_parameters(self, prompt: str) -> Dict[str, Any]:
        """Extract animation parameters from prompt"""
        params = {
            "duration": 1000,  # ms
            "fps": 60,
            "iterations": float('inf'),
            "easing": "ease-out",
        }
        
        # Extract duration
        duration_match = re.search(r'(\d+)\s*(?:ms|milliseconds?|s|seconds?)', prompt, re.IGNORECASE)
        if duration_match:
            duration_val = int(duration_match.group(1))
            if 's' in duration_match.group(0).lower() and 'ms' not in duration_match.group(0).lower():
                duration_val *= 1000
            params["duration"] = duration_val
        
        # Extract FPS target
        if "60 fps" in prompt.lower():
            params["fps"] = 60
        elif "30 fps" in prompt.lower():
            params["fps"] = 30
        elif "120 fps" in prompt.lower():
            params["fps"] = 120
        
        # Extract easing
        easing_options = ["ease-in", "ease-out", "ease-in-out", "linear", "ease"]
        for easing in easing_options:
            if easing in prompt.lower():
                params["easing"] = easing
                break
        
        return params
