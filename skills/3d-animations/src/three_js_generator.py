"""
Three.js Code Generator

Generate Three.js code from animation prompts
"""

import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class ThreeJsGenerator:
    """Generate Three.js 3D animation code"""
    
    def __init__(self):
        """Initialize generator"""
        logger.info("Initialized Three.js Generator")
    
    def generate(
        self,
        prompt: str,
        use_cases: Optional[List[str]] = None,
        performance_target: int = 60,
        include_mobile: bool = True
    ) -> Dict[str, Any]:
        """
        Generate Three.js code from prompt
        
        Args:
            prompt: Animation description
            use_cases: Intended use cases
            performance_target: Target FPS
            include_mobile: Mobile optimization
        
        Returns:
            Dict with generated code and metadata
        """
        logger.info(f"Generating Three.js code: {prompt}")
        
        code = self._generate_component(prompt, performance_target, include_mobile)
        
        return {
            "code_file": "components/3d/Animation.tsx",
            "code": code,
            "lines_of_code": len(code.split('\n')),
            "libraries_used": ["three.js", "react-three-fiber", "@react-three/drei"],
            "performance": performance_target,
            "mobile_optimized": include_mobile,
            "ready_to_deploy": True
        }
    
    def _generate_component(
        self,
        prompt: str,
        fps: int,
        mobile: bool
    ) -> str:
        """Generate component code"""
        
        mobile_check = """
  // Detect mobile device
  const isMobile = useMediaQuery({ maxWidth: 768 });
  const scale = isMobile ? 0.75 : 1;
""" if mobile else ""
        
        func_name = self._camel_case(prompt.split()[0] or 'Animation')
        code = """import * as THREE from 'three';
import { useEffect, useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, PerspectiveCamera } from '@react-three/drei';

/**
 * Three.js Animation Component
 * Generated from prompt: """ + prompt[:60] + """...
 * Target FPS: """ + str(fps) + """
 * Mobile Optimized: """ + str(mobile) + """
 */

function AnimationObject() {
  const meshRef = useRef(null);
  
  useFrame(({ clock }) => {
    if (meshRef.current) {
      meshRef.current.rotation.x = clock.elapsedTime * 0.5;
      meshRef.current.rotation.y = clock.elapsedTime * 0.3;
    }
  });
  
  return (
    <mesh ref={meshRef} position={[0, 0, 0]}>
      <boxGeometry args={[2, 2, 2]} />
      <meshPhongMaterial color="#3b82f6" emissive="#1e40af" />
    </mesh>
  );
}

function Lights() {
  return (
    <>
      <pointLight position={[10, 10, 10]} intensity={0.8} />
      <pointLight position={[-10, -10, 10]} intensity={0.6} color="#ff0000" />
      <ambientLight intensity={0.4} />
    </>
  );
}

export function """ + func_name + """() {""" + mobile_check + """
  return (
    <div className="w-full h-screen relative">
      <Canvas 
        gl={{ antialias: true, alpha: true }}
        className="w-full h-screen"
      >
        <PerspectiveCamera makeDefault position={[0, 0, 5]} />
        <Lights />
        <AnimationObject />
        <OrbitControls />
      </Canvas>
    </div>
  );
}
"""
        return code
    
    def _camel_case(self, text: str) -> str:
        """Convert to camelCase"""
        words = text.split()
        if not words:
            return "Animation"
        return words[0] + "".join(w.capitalize() for w in words[1:])
    
    def generate_hero_section(
        self,
        colors: Optional[List[str]] = None,
        speed: float = 1.0
    ) -> str:
        """Generate hero section component"""
        
        colors = colors or ["#3b82f6", "#10b981"]
        
        return f'''
import * as THREE from 'three';
import {{ Canvas, useFrame }} from '@react-three/fiber';
import {{ useRef }} from 'react';

function HeroAnimation() {{
  const meshRef = useRef(null);
  
  useFrame(({{'clock'}}) => {{
    if (meshRef.current) {{
      meshRef.current.rotation.x += {0.005 * speed};
      meshRef.current.rotation.y += {0.01 * speed};
    }}
  }});
  
  return (
    <mesh ref={{meshRef}}>
      <icosahedronGeometry args={{[2, 4]}} />
      <meshPhongMaterial 
        color="{colors[0]}"
        emissive="{colors[1]}"
        wireframe={{false}}
      />
    </mesh>
  );
}}

export function HeroSection() {{
  return (
    <div className="w-full h-screen relative overflow-hidden">
      <Canvas gl={{{{ antialias: true }}}} className="w-full h-full">
        <ambientLight intensity={{0.5}} />
        <pointLight position={{[10, 10, 10]}} intensity={{1}} />
        <HeroAnimation />
      </Canvas>
    </div>
  );
}}
'''
    
    def generate_product_rotator(self) -> str:
        """Generate product rotator component"""
        
        return '''
import * as THREE from 'three';
import { Canvas, useFrame } from '@react-three/fiber';
import { useRef, useState } from 'react';

function ProductModel() {
  const meshRef = useRef(null);
  const [autoRotate, setAutoRotate] = useState(true);
  
  useFrame(() => {
    if (meshRef.current && autoRotate) {
      meshRef.current.rotation.y += 0.005;
    }
  });
  
  return (
    <group ref={meshRef}>
      <mesh>
        <cylinderGeometry args={[2, 2, 3, 32]} />
        <meshPhongMaterial color="#ef4444" emissive="#dc2626" />
      </mesh>
    </group>
  );
}

export function ProductRotator() {
  return (
    <div className="w-full h-96 relative">
      <Canvas>
        <ambientLight intensity={0.6} />
        <pointLight position={[10, 10, 5]} intensity={1} />
        <ProductModel />
      </Canvas>
    </div>
  );
}
'''
    
    def generate_text_animation(self, text: str = "3D Text") -> str:
        """Generate 3D text animation"""
        
        return f'''
import {{ Canvas, useFrame }} from '@react-three/fiber';
import {{ Text }} from '@react-three/drei';
import {{ useRef }} from 'react';

function AnimatedText() {{
  const groupRef = useRef(null);
  
  useFrame(({{'clock'}}) => {{
    if (groupRef.current) {{
      groupRef.current.rotation.x = Math.sin(clock.elapsedTime) * 0.2;
      groupRef.current.rotation.y = clock.elapsedTime * 0.3;
    }}
  }});
  
  return (
    <group ref={{groupRef}}>
      <Text
        position={{[0, 0, 0]}}
        fontSize={{1}}
        maxWidth={{200}}
        lineHeight={{1.2}}
        letterSpacing={{0.02}}
        textAlign="center"
        color="#3b82f6"
        outlineWidth={{0.005}}
        outlineColor="#1e3a8a"
      >
        {text}
      </Text>
    </group>
  );
}}

export function TextAnimation() {{
  return (
    <Canvas camera={{{{ position: [0, 0, 3] }}}}>
      <ambientLight intensity={{0.5}} />
      <pointLight position={{[10, 10, 10]}} />
      <AnimatedText />
    </Canvas>
  );
}}
'''
