"""3D Animations Skill - Core modules"""

__version__ = "1.0.0"
__author__ = "OpenClaw Community"
__description__ = "Fetch and integrate 3D animations from 21st.dev into websites"

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

__all__ = [
    'Fetcher21stDev',
    'PromptParser',
    'PromptLibrary',
    'ThreeJsGenerator',
    'BabylonJsGenerator',
    'AnimationIntegrator',
    'Components3D',
    'PerformanceOptimizer',
    'MobileHandler',
    'DeploymentManager',
]
