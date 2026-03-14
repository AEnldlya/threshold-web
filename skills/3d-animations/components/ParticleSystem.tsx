/**
 * ParticleSystem Component
 * Custom particle effects
 */

import React, { useMemo, useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import * as THREE from 'three';

interface ParticleSystemProps {
  count?: number;
  color?: string;
  speed?: number;
}

function Particles({ count = 1000, color = '#3b82f6' }) {
  const points = useRef<THREE.Points>(null);
  const particlePositions = useMemo(() => {
    const pos = new Float32Array(count * 3);
    for (let i = 0; i < count * 3; i += 3) {
      pos[i] = (Math.random() - 0.5) * 40;
      pos[i + 1] = (Math.random() - 0.5) * 40;
      pos[i + 2] = (Math.random() - 0.5) * 40;
    }
    return pos;
  }, [count]);

  const particleVelocities = useMemo(() => {
    const vel = new Float32Array(count * 3);
    for (let i = 0; i < count * 3; i += 3) {
      vel[i] = (Math.random() - 0.5) * 0.1;
      vel[i + 1] = (Math.random() - 0.5) * 0.1;
      vel[i + 2] = (Math.random() - 0.5) * 0.1;
    }
    return vel;
  }, [count]);

  useFrame(() => {
    if (points.current) {
      const positions = points.current.geometry.attributes.position.array as Float32Array;
      
      for (let i = 0; i < positions.length; i += 3) {
        positions[i] += particleVelocities[i];
        positions[i + 1] += particleVelocities[i + 1];
        positions[i + 2] += particleVelocities[i + 2];

        // Wrap around
        if (positions[i] > 20) positions[i] = -20;
        if (positions[i] < -20) positions[i] = 20;
        if (positions[i + 1] > 20) positions[i + 1] = -20;
        if (positions[i + 1] < -20) positions[i + 1] = 20;
      }
      points.current.geometry.attributes.position.needsUpdate = true;
      points.current.rotation.x += 0.0001;
      points.current.rotation.y += 0.0002;
    }
  });

  return (
    <points ref={points}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          count={count}
          array={particlePositions}
          itemSize={3}
        />
      </bufferGeometry>
      <pointsMaterial size={0.05} color={color} transparent sizeAttenuation={true} />
    </points>
  );
}

export const ParticleSystem: React.FC<ParticleSystemProps> = ({
  count = 1000,
  color = '#3b82f6',
  speed = 1,
}) => {
  return (
    <div className="w-full h-screen bg-black">
      <Canvas
        gl={{ antialias: true }}
        camera={{ position: [0, 0, 30], fov: 75 }}
      >
        <Particles count={count} color={color} />
      </Canvas>
    </div>
  );
};

export default ParticleSystem;
