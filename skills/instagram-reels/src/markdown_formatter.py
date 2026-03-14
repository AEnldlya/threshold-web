"""
Markdown Formatter for Instagram Reels

Formats reel analysis into DESIGN_REFERENCES.md entries
with proper structure and metadata.
"""

import logging
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime


logger = logging.getLogger(__name__)


class MarkdownFormatter:
    """Format and save reel analysis to markdown files."""
    
    ENTRY_TEMPLATE = """### [{date}] - {creator} - {topic}

**Instagram Reel**: [{reel_id}](https://www.instagram.com/reel/{reel_id}/)

**What I Found**: 
{description}

**Design Analysis**:
{design_analysis}

**Why It's Relevant**: 
{custom_notes}

**Implementation Notes**:
- Reference for future projects
- Study the animations and layout approach
- Analyze color palette and typography choices
- Check UI element interactions

**Link**: https://www.instagram.com/reel/{reel_id}/

**Status**: [ ] Todo [ ] In Progress [x] Reference Saved

---
"""
    
    def __init__(self, output_file: Optional[str] = None):
        """
        Initialize markdown formatter.
        
        Args:
            output_file: Path to DESIGN_REFERENCES.md file
        """
        if output_file:
            self.output_file = Path(output_file)
        else:
            self.output_file = Path.home() / ".openclaw/workspace/DESIGN_REFERENCES.md"
        
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
    
    def format_entry(
        self,
        reel_id: str,
        creator: str,
        description: str,
        design_analysis: Dict[str, Any],
        custom_notes: str = "",
        topic: Optional[str] = None
    ) -> str:
        """
        Format a single reel entry for markdown.
        
        Args:
            reel_id: Instagram reel ID
            creator: Creator username
            description: Reel description
            design_analysis: Design analysis dictionary
            custom_notes: Custom notes about the reel
            topic: Topic/category (auto-generated if None)
            
        Returns:
            Formatted markdown entry
        """
        # Auto-generate topic from analysis
        if not topic:
            topic = self._generate_topic(design_analysis)
        
        # Format design analysis
        design_text = self._format_design_analysis(design_analysis)
        
        # Format custom notes
        notes_text = custom_notes or "Great design pattern to reference."
        
        # Create entry
        entry = self.ENTRY_TEMPLATE.format(
            date=datetime.now().strftime("%Y-%m-%d"),
            creator=creator,
            topic=topic,
            reel_id=reel_id,
            description=description or "(No description provided)",
            design_analysis=design_text,
            custom_notes=notes_text
        )
        
        return entry
    
    def _generate_topic(self, design_analysis: Dict[str, Any]) -> str:
        """
        Auto-generate topic from design analysis.
        
        Args:
            design_analysis: Design analysis dictionary
            
        Returns:
            Topic string
        """
        parts = []
        
        if design_analysis.get('layout'):
            parts.append(design_analysis['layout'])
        
        if design_analysis.get('animations'):
            parts.append(f"{len(design_analysis['animations'])} animations")
        
        if not parts:
            return "Design Pattern"
        
        return " - ".join(parts).title()
    
    def _format_design_analysis(self, design_analysis: Dict[str, Any]) -> str:
        """
        Format design analysis into markdown text.
        
        Args:
            design_analysis: Design analysis dictionary
            
        Returns:
            Formatted markdown text
        """
        lines = []
        
        if design_analysis.get('animations'):
            lines.append(f"- **Animations**: {', '.join(design_analysis['animations'])}")
        
        if design_analysis.get('layout'):
            lines.append(f"- **Layout**: {design_analysis['layout']}")
        
        if design_analysis.get('typography'):
            lines.append(f"- **Typography**: {design_analysis['typography']}")
        
        if design_analysis.get('colors'):
            colors = design_analysis['colors'][:5]
            lines.append(f"- **Colors**: {', '.join(colors)}")
        
        if design_analysis.get('techniques'):
            techniques = design_analysis['techniques'][:3]
            lines.append(f"- **Techniques**: {', '.join(techniques)}")
        
        if design_analysis.get('ui_elements'):
            elements = design_analysis['ui_elements'][:5]
            lines.append(f"- **UI Elements**: {', '.join(elements)}")
        
        if design_analysis.get('interactions'):
            interactions = design_analysis['interactions'][:3]
            lines.append(f"- **Interactions**: {', '.join(interactions)}")
        
        return "\n".join(lines) if lines else "- Design pattern analysis completed"
    
    def append_entry(
        self,
        reel_id: str,
        creator: str,
        description: str,
        design_analysis: Dict[str, Any],
        custom_notes: str = "",
        topic: Optional[str] = None
    ) -> bool:
        """
        Append entry to markdown file.
        
        Args:
            reel_id: Instagram reel ID
            creator: Creator username
            description: Reel description
            design_analysis: Design analysis dictionary
            custom_notes: Custom notes
            topic: Topic/category
            
        Returns:
            True if successful, False otherwise
        """
        try:
            entry = self.format_entry(
                reel_id=reel_id,
                creator=creator,
                description=description,
                design_analysis=design_analysis,
                custom_notes=custom_notes,
                topic=topic
            )
            
            # Create file if it doesn't exist
            if not self.output_file.exists():
                self.output_file.write_text(self._create_header())
            
            # Append entry
            with open(self.output_file, 'a') as f:
                f.write("\n" + entry)
            
            logger.info(f"Entry saved to {self.output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving entry: {e}")
            return False
    
    def _create_header(self) -> str:
        """
        Create markdown file header.
        
        Returns:
            Header text
        """
        return """# Design References

Collection of Instagram reel design patterns and inspiration for web development.

**Last Updated**: {date}

---

## Reels

""".format(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    def check_if_exists(self, reel_id: str) -> bool:
        """
        Check if reel entry already exists in file.
        
        Args:
            reel_id: Instagram reel ID
            
        Returns:
            True if entry exists, False otherwise
        """
        if not self.output_file.exists():
            return False
        
        content = self.output_file.read_text()
        return f"[{reel_id}]" in content
    
    def get_entry_count(self) -> int:
        """
        Get number of entries in markdown file.
        
        Returns:
            Number of entries
        """
        if not self.output_file.exists():
            return 0
        
        content = self.output_file.read_text()
        return content.count("### [")


def main():
    """Test markdown formatter."""
    formatter = MarkdownFormatter()
    
    # Test entry
    design_analysis = {
        'animations': ['fade-in', 'slide-up'],
        'layout': 'hero',
        'typography': 'sans-serif',
        'colors': ['#1a1a1a', '#ffffff'],
        'techniques': ['framer', 'react'],
        'ui_elements': ['button', 'header'],
        'interactions': ['hover', 'click']
    }
    
    entry = formatter.format_entry(
        reel_id="DUHmsKkjZw0",
        creator="design_inspiration",
        description="Beautiful hero section with smooth animations",
        design_analysis=design_analysis,
        custom_notes="Perfect for landing pages"
    )
    
    print("Formatted Entry:")
    print(entry)
    
    # Test file operations
    print(f"\nEntry exists: {formatter.check_if_exists('DUHmsKkjZw0')}")
    print(f"Total entries: {formatter.get_entry_count()}")


if __name__ == '__main__':
    main()
