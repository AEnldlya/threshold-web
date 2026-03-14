/**
 * FloatingCube Component
 * 3D floating cube with particle effects
 */

import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, PerspectiveCamera } from '@react-three/drei';
import * as THREE from 'three';

interface FloatingCubeProps {
  colors?: [string, string];
  speed?: number;
  scale?: number;
}

function CubeGeometry({ colors = ['#3b82f6', '#10b981'], speed = 1 }) {
  const meshRef = useRef<THREE.Mesh>(null);

  useFrame(({ clock }) => {
    if (meshRef.current) {
      meshRef.current.rotation.x = clock.elapsedTime * 0.5 * speed;
      meshRef.current.rotation.y = clock.elapsedTime * 0.3 * speed;
    }
  });

  return (
    <mesh ref={meshRef}>
      <boxGeometry args={[2, 2, 2]} />
      <meshPhongMaterial
        color={colors[0]}
        emissive={colors[1]}
        shininess={100}
      />
    </mesh>
  );
}

function ParticleField({ count = 100 }) {
  const pointsRef = useRef<THREE.Points>(null);
  const positions = React.useMemo(() => {
    const pos = new Float32Array(count * 3);
    for (let i = 0; i < count * 3; i += 3) {
      pos[i] = (Math.random() - 0.5) * 10;
      pos[i + 1] = (Math.random() - 0.5) * 10;
      pos[i + 2] = (Math.random() - 0.5) * 10;
    }
    return pos;
  }, [count]);

  useFrame(({ clock }) => {
    if (pointsRef.current) {
      pointsRef.current.rotation.x = clock.elapsedTime * 0.1;
      pointsRef.current.rotation.y = clock.elapsedTime * 0.15;
    }
  });

  return (
    <points ref={pointsRef}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          count={positions.length / 3}
          array={positions}
          itemSize={3}
        />
      </bufferGeometry>
      <pointsMaterial size={0.1} color="#10b981" />
    </points>
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

export const FloatingCube: React.FC<FloatingCubeProps> = ({
  colors = ['#3b82f6', '#10b981'],
  speed = 1,
  scale = 1,
}) => {
  return (
    <div className="w-full h-screen relative">
      <Canvas
        gl={{ antialias: true, alpha: true }}
        className="w-full h-full"
      >
        <PerspectiveCamera
          makeDefault
          position={[0, 0, 5]}
          fov={75}
        />
        <Lights />
        <CubeGeometry colors={colors} speed={speed} />
        <ParticleField count={100} />
        <OrbitControls
          enableZoom={true}
          enablePan={true}
          enableRotate={true}
        />
      </Canvas>
    </div>
  );
};

export default FloatingCube;
