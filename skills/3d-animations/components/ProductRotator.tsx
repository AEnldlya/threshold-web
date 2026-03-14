/**
 * ProductRotator Component
 * 360-degree product showcase
 */

import React, { useRef, useState } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, PerspectiveCamera } from '@react-three/drei';
import * as THREE from 'three';

interface ProductRotatorProps {
  color?: string;
  speed?: number;
  autoRotate?: boolean;
}

function Product({ color = '#ef4444' }) {
  const meshRef = useRef<THREE.Mesh>(null);
  const [autoRotate, setAutoRotate] = useState(true);

  useFrame(() => {
    if (meshRef.current && autoRotate) {
      meshRef.current.rotation.y += 0.005;
    }
  });

  return (
    <group ref={meshRef}>
      {/* Main cylinder */}
      <mesh>
        <cylinderGeometry args={[2, 2, 3, 32]} />
        <meshPhongMaterial color={color} emissive={color} shininess={100} />
      </mesh>

      {/* Top cap */}
      <mesh position={[0, 1.5, 0]}>
        <sphereGeometry args={[2, 32, 32]} />
        <meshPhongMaterial color={color} emissive={color} />
      </mesh>

      {/* Bottom cap */}
      <mesh position={[0, -1.5, 0]}>
        <sphereGeometry args={[2, 32, 32]} />
        <meshPhongMaterial color={color} emissive={color} />
      </mesh>
    </group>
  );
}

function Lights() {
  return (
    <>
      <pointLight position={[10, 10, 10]} intensity={1} />
      <pointLight position={[-10, 10, 10]} intensity={0.8} color="#0099ff" />
      <pointLight position={[0, -10, 5]} intensity={0.6} color="#ff00ff" />
      <ambientLight intensity={0.5} />
    </>
  );
}

function Environment() {
  return (
    <group>
      {/* Floor */}
      <mesh position={[0, -3.5, 0]} rotation={[-Math.PI / 2, 0, 0]}>
        <planeGeometry args={[20, 20]} />
        <meshPhongMaterial color="#1f2937" />
      </mesh>

      {/* Background */}
      <mesh position={[0, 0, -10]}>
        <planeGeometry args={[20, 20]} />
        <meshPhongMaterial color="#111827" />
      </mesh>
    </group>
  );
}

export const ProductRotator: React.FC<ProductRotatorProps> = ({
  color = '#ef4444',
  speed = 1,
  autoRotate = true,
}) => {
  return (
    <div className="w-full h-screen bg-black relative">
      <Canvas
        gl={{ antialias: true, alpha: false }}
        className="w-full h-full"
        camera={{ position: [0, 0, 8], fov: 50 }}
      >
        <PerspectiveCamera makeDefault position={[0, 0, 8]} fov={50} />
        <Lights />
        <Environment />
        <Product color={color} />
        <OrbitControls
          enableZoom={true}
          enablePan={false}
          enableRotate={true}
          autoRotate={autoRotate}
          autoRotateSpeed={2 * speed}
          minDistance={5}
          maxDistance={15}
        />
      </Canvas>

      {/* Info overlay */}
      <div className="absolute bottom-4 left-4 text-white text-sm">
        <p>Drag to rotate • Scroll to zoom</p>
      </div>
    </div>
  );
};

export default ProductRotator;
