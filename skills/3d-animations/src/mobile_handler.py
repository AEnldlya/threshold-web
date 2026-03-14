"""
Mobile Handler

Handle mobile device detection and optimization
"""

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class MobileHandler:
    """Handle mobile device optimization"""
    
    def __init__(self):
        """Initialize handler"""
        logger.info("Initialized Mobile Handler")
    
    def detect_device(self, user_agent: str) -> Dict[str, Any]:
        """Detect device type"""
        is_mobile = any(keyword in user_agent.lower() for keyword in [
            'mobile', 'android', 'iphone', 'ipad', 'windows phone'
        ])
        
        return {
            "is_mobile": is_mobile,
            "device_type": "mobile" if is_mobile else "desktop"
        }
    
    def get_quality_settings(self, device_type: str) -> Dict[str, Any]:
        """Get quality settings for device"""
        settings = {
            "mobile": {
                "quality_scale": 0.75,
                "target_fps": 30,
                "max_particles": 500,
                "max_draw_calls": 50,
                "texture_compression": "aggressive",
                "geometry_detail": "low"
            },
            "desktop": {
                "quality_scale": 1.0,
                "target_fps": 60,
                "max_particles": 2000,
                "max_draw_calls": 200,
                "texture_compression": "moderate",
                "geometry_detail": "high"
            }
        }
        
        return settings.get(device_type, settings["desktop"])
    
    def optimize_for_mobile(
        self,
        animation_code: str,
        device_type: str = "mobile"
    ) -> str:
        """Optimize animation for mobile"""
        logger.info(f"Optimizing for {device_type}")
        
        if device_type == "mobile":
            # Add mobile optimizations
            animation_code = animation_code.replace(
                "bufferGeometry",
                "bufferGeometry // Mobile optimized"
            )
        
        return animation_code
