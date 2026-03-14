/**
 * MorphingText Component
 * 3D text morphing animation
 */

import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Text, PerspectiveCamera } from '@react-three/drei';
import * as THREE from 'three';

interface MorphingTextProps {
  text?: string;
  colors?: [string, string];
  speed?: number;
}

function AnimatedText({ text = '3D Text', colors = ['#3b82f6', '#1e40af'] }) {
  const groupRef = useRef<THREE.Group>(null);

  useFrame(({ clock }) => {
    if (groupRef.current) {
      groupRef.current.rotation.x = Math.sin(clock.elapsedTime) * 0.2;
      groupRef.current.rotation.y = clock.elapsedTime * 0.3;
      groupRef.current.position.y = Math.sin(clock.elapsedTime * 0.5) * 0.5;
    }
  });

  return (
    <group ref={groupRef}>
      <Text
        position={[0, 0, 0]}
        fontSize={1}
        maxWidth={200}
        lineHeight={1.2}
        letterSpacing={0.02}
        textAlign="center"
        color={colors[0]}
        outlineWidth={0.005}
        outlineColor={colors[1]}
        font="/fonts/inter-bold.woff"
      >
        {text}
      </Text>
    </group>
  );
}

function Lights() {
  return (
    <>
      <pointLight position={[5, 5, 5]} intensity={0.8} />
      <pointLight position={[-5, -5, 5]} intensity={0.6} color="#ff0000" />
      <ambientLight intensity={0.5} />
    </>
  );
}

export const MorphingText: React.FC<MorphingTextProps> = ({
  text = '3D Text',
  colors = ['#3b82f6', '#1e40af'],
  speed = 1,
}) => {
  return (
    <div className="w-full h-screen relative bg-gradient-to-br from-slate-900 to-slate-800">
      <Canvas className="w-full h-full">
        <PerspectiveCamera
          makeDefault
          position={[0, 0, 3]}
          fov={75}
        />
        <Lights />
        <AnimatedText text={text} colors={colors} />
      </Canvas>
    </div>
  );
};

export default MorphingText;
