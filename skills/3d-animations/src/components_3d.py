"""
3D Components Library

Reusable 3D components
"""

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class Components3D:
    """Reusable 3D components"""
    
    @staticmethod
    def floating_cube(colors: list = None) -> str:
        """Generate floating cube component"""
        colors = colors or ["#3b82f6", "#10b981"]
        return f"""
export function FloatingCube() {{
  return (
    <mesh>
      <boxGeometry args={{[2, 2, 2]}} />
      <meshPhongMaterial color="{colors[0]}" emissive="{colors[1]}" />
    </mesh>
  );
}}
"""
    
    @staticmethod
    def morphing_text() -> str:
        """Generate morphing text component"""
        return """
export function MorphingText({ text = "3D Text" }) {
  return (
    <Text
      position={[0, 0, 0]}
      fontSize={1}
      maxWidth={200}
      textAlign="center"
      color="#3b82f6"
    >
      {text}
    </Text>
  );
}
"""
    
    @staticmethod
    def product_rotator() -> str:
        """Generate product rotator component"""
        return """
export function ProductRotator({ model = null }) {
  const meshRef = useRef(null);
  
  useFrame(() => {
    if (meshRef.current) {
      meshRef.current.rotation.y += 0.005;
    }
  });
  
  return (
    <group ref={meshRef}>
      {model ? <primitive object={model} /> : <cylinderGeometry args={[2, 2, 3]} />}
    </group>
  );
}
"""
    
    @staticmethod
    def particle_system() -> str:
        """Generate particle system component"""
        return """
export function ParticleSystem({ count = 1000 }) {
  const particles = useRef(null);
  
  useFrame(() => {
    if (particles.current) {
      particles.current.rotation.x += 0.001;
      particles.current.rotation.y += 0.002;
    }
  });
  
  return (
    <group ref={particles}>
      <points>
        <bufferGeometry />
        <pointsMaterial size={0.1} color="#3b82f6" />
      </points>
    </group>
  );
}
"""
    
    @staticmethod
    def scroll_hero() -> str:
        """Generate scroll-triggered hero component"""
        return """
export function ScrollHero() {
  const groupRef = useRef(null);
  
  useScroll(({ offset }) => {
    if (groupRef.current) {
      groupRef.current.rotation.x = offset * Math.PI;
    }
  });
  
  return (
    <group ref={groupRef}>
      <mesh>
        <icosahedronGeometry args={[2, 4]} />
        <meshPhongMaterial color="#3b82f6" />
      </mesh>
    </group>
  );
}
"""
    
    @staticmethod
    def webgl_gallery() -> str:
        """Generate WebGL gallery component"""
        return """
export function WebGLGallery({ images = [] }) {
  const canvasRef = useRef(null);
  
  useEffect(() => {
    // Initialize WebGL context
    const canvas = canvasRef.current;
    const gl = canvas.getContext('webgl2');
    
    // Set up shaders and rendering
    // ...gallery implementation
  }, [images]);
  
  return <canvas ref={canvasRef} className="w-full h-full" />;
}
"""
