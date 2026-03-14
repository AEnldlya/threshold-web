"""
Prompt Library

Local caching and management of animation prompts
"""

import logging
import json
from typing import Any, Dict, List, Optional
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)


class PromptLibrary:
    """Manage local prompt library"""
    
    def __init__(self):
        """Initialize library"""
        self.lib_dir = Path.home() / ".openclaw" / "workspace" / "skills" / "3d-animations" / "prompts"
        self.lib_dir.mkdir(parents=True, exist_ok=True)
        self.cache_file = self.lib_dir / "cache.json"
        self.prompts = self._load_cache()
        logger.info(f"Initialized prompt library with {len(self.prompts)} cached prompts")
    
    def _load_cache(self) -> Dict[str, Any]:
        """Load cached prompts"""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load cache: {e}")
        
        return {}
    
    def _save_cache(self):
        """Save cache to disk"""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.prompts, f, indent=2)
            logger.info(f"Saved cache with {len(self.prompts)} prompts")
        except Exception as e:
            logger.error(f"Failed to save cache: {e}")
    
    def add_prompt(
        self,
        prompt_id: str,
        category: str,
        name: str,
        description: str,
        prompt_text: str,
        code: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        Add prompt to library
        
        Args:
            prompt_id: Unique ID
            category: Category
            name: Display name
            description: Description
            prompt_text: Prompt text
            code: Optional code sample
            metadata: Optional metadata
        
        Returns:
            Success status
        """
        logger.info(f"Adding prompt: {prompt_id}")
        
        self.prompts[prompt_id] = {
            "id": prompt_id,
            "category": category,
            "name": name,
            "description": description,
            "prompt": prompt_text,
            "code": code,
            "metadata": metadata or {},
            "created_at": datetime.now().isoformat(),
            "usage_count": 0
        }
        
        self._save_cache()
        return True
    
    def get_prompt(self, prompt_id: str) -> Optional[Dict[str, Any]]:
        """Get prompt by ID"""
        if prompt_id in self.prompts:
            self.prompts[prompt_id]["usage_count"] += 1
            self._save_cache()
            return self.prompts[prompt_id]
        return None
    
    def search(
        self,
        query: str,
        category: Optional[str] = None,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Search prompts
        
        Args:
            query: Search term
            category: Optional category filter
            limit: Max results
        
        Returns:
            List of matching prompts
        """
        logger.info(f"Searching: {query} (category: {category})")
        
        results = []
        query_lower = query.lower()
        
        for prompt_id, prompt in self.prompts.items():
            # Apply category filter
            if category and prompt["category"] != category:
                continue
            
            # Check query match
            if (query_lower in prompt["name"].lower() or 
                query_lower in prompt["description"].lower() or
                query_lower in prompt["prompt"].lower()):
                results.append(prompt)
        
        logger.info(f"Found {len(results)} prompts")
        return results[:limit]
    
    def get_by_category(self, category: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get prompts by category"""
        results = [p for p in self.prompts.values() if p["category"] == category]
        return results[:limit]
    
    def save_prompts(
        self,
        prompts: List[Dict[str, Any]],
        format: str = "markdown"
    ) -> Optional[Path]:
        """
        Save prompts to file
        
        Args:
            prompts: List of prompts
            format: Output format (markdown or json)
        
        Returns:
            Path to saved file
        """
        logger.info(f"Saving {len(prompts)} prompts as {format}")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == "json":
            filepath = self.lib_dir / f"prompts_{timestamp}.json"
            with open(filepath, 'w') as f:
                json.dump(prompts, f, indent=2)
        else:  # markdown
            filepath = self.lib_dir / f"prompts_{timestamp}.md"
            with open(filepath, 'w') as f:
                f.write("# Animation Prompts Library\n\n")
                
                categories = {}
                for p in prompts:
                    cat = p.get("category", "uncategorized")
                    if cat not in categories:
                        categories[cat] = []
                    categories[cat].append(p)
                
                for category, cat_prompts in sorted(categories.items()):
                    f.write(f"## {category.replace('-', ' ').title()}\n\n")
                    
                    for p in cat_prompts:
                        f.write(f"### {p.get('name', 'Unnamed')}\n\n")
                        f.write(f"**Description**: {p.get('description', 'N/A')}\n\n")
                        f.write(f"**Prompt**: {p.get('prompt', 'N/A')}\n\n")
                        
                        if p.get('code'):
                            f.write(f"**Code**:\n```typescript\n{p['code']}\n```\n\n")
                        
                        f.write("---\n\n")
        
        logger.info(f"Saved prompts to {filepath}")
        return filepath
    
    def get_trending(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get trending prompts (by usage)"""
        sorted_prompts = sorted(
            self.prompts.values(),
            key=lambda p: p.get("usage_count", 0),
            reverse=True
        )
        return sorted_prompts[:limit]
    
    def get_categories(self) -> List[str]:
        """Get all categories"""
        categories = set(p.get("category") for p in self.prompts.values())
        return sorted(list(categories))
    
    def clear(self):
        """Clear all prompts"""
        logger.warning("Clearing all prompts")
        self.prompts = {}
        self._save_cache()
    
    def export(self, filepath: Path):
        """Export library to file"""
        logger.info(f"Exporting library to {filepath}")
        with open(filepath, 'w') as f:
            json.dump(self.prompts, f, indent=2)
    
    def import_from(self, filepath: Path):
        """Import prompts from file"""
        logger.info(f"Importing from {filepath}")
        with open(filepath, 'r') as f:
            imported = json.load(f)
            self.prompts.update(imported)
            self._save_cache()
