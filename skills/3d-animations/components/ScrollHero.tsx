/**
 * ScrollHero Component
 * Scroll-triggered 3D hero animation
 */

import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import * as THREE from 'three';

interface ScrollHeroProps {
  color?: string;
}

function Hero({ color = '#3b82f6' }) {
  const meshRef = useRef<THREE.Mesh>(null);
  const scrollProgress = useRef(0);

  // Update scroll progress
  React.useEffect(() => {
    const handleScroll = () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      scrollProgress.current = scrollTop / docHeight;
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useFrame(() => {
    if (meshRef.current) {
      meshRef.current.rotation.x = scrollProgress.current * Math.PI * 2;
      meshRef.current.rotation.y = scrollProgress.current * Math.PI * 4;
      meshRef.current.scale.set(
        1 + scrollProgress.current * 0.5,
        1 + scrollProgress.current * 0.5,
        1 + scrollProgress.current * 0.5
      );
    }
  });

  return (
    <group ref={meshRef}>
      <mesh>
        <icosahedronGeometry args={[2, 4]} />
        <meshPhongMaterial
          color={color}
          emissive={color}
          wireframe={false}
          shininess={100}
        />
      </mesh>
    </group>
  );
}

function Lights() {
  return (
    <>
      <pointLight position={[10, 10, 10]} intensity={0.8} />
      <pointLight position={[-10, -10, 10]} intensity={0.6} />
      <ambientLight intensity={0.4} />
    </>
  );
}

export const ScrollHero: React.FC<ScrollHeroProps> = ({
  color = '#3b82f6',
}) => {
  return (
    <div className="w-full min-h-screen">
      <div className="sticky top-0 w-full h-screen">
        <Canvas
          gl={{ antialias: true, alpha: true }}
          className="w-full h-full"
          camera={{ position: [0, 0, 5], fov: 75 }}
        >
          <Lights />
          <Hero color={color} />
        </Canvas>
      </div>

      {/* Content below */}
      <div className="relative z-10 bg-white">
        <div className="h-[200vh] flex flex-col justify-between p-12 bg-gradient-to-b from-transparent via-white to-white">
          <div className="space-y-8">
            <h2 className="text-4xl font-bold text-slate-900">
              Scroll to See the Magic
            </h2>
            <p className="text-lg text-slate-600 max-w-2xl">
              The 3D object above responds to your scroll position. Keep scrolling
              to see it rotate and scale!
            </p>
          </div>

          <div className="space-y-8 pb-12">
            <h3 className="text-3xl font-bold text-slate-900">
              More Content Here
            </h3>
            <p className="text-slate-600">
              This section demonstrates how scroll-triggered 3D animations can
              enhance the user experience on your website.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ScrollHero;
