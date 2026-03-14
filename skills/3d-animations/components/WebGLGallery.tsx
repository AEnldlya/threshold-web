/**
 * WebGLGallery Component
 * High-performance WebGL image gallery
 */

import React, { useRef, useEffect, useState } from 'react';
import * as THREE from 'three';

interface WebGLGalleryProps {
  images?: string[];
  width?: number;
  height?: number;
}

export const WebGLGallery: React.FC<WebGLGalleryProps> = ({
  images = [],
  width = 800,
  height = 600,
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  useEffect(() => {
    if (!canvasRef.current || images.length === 0) return;

    // Initialize Three.js
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas: canvasRef.current, alpha: true });

    renderer.setSize(width, height);
    renderer.setPixelRatio(window.devicePixelRatio);
    camera.position.z = 5;

    // Create image plane
    const textureLoader = new THREE.TextureLoader();
    let currentTexture: THREE.Texture | null = null;
    let plane: THREE.Mesh | null = null;

    const loadImage = (index: number) => {
      if (index < images.length) {
        textureLoader.load(images[index], (texture) => {
          if (plane) {
            plane.material.dispose();
          }

          const geometry = new THREE.PlaneGeometry(8, 6);
          const material = new THREE.MeshBasicMaterial({ map: texture });

          if (plane) {
            scene.remove(plane);
          }

          plane = new THREE.Mesh(geometry, material);
          scene.add(plane);
          currentTexture = texture;
        });
      }
    };

    loadImage(currentImageIndex);

    // Lighting
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(5, 5, 5);
    scene.add(light);

    // Animation loop
    let animationId: number;
    const animate = () => {
      animationId = requestAnimationFrame(animate);

      if (plane) {
        plane.rotation.y += 0.001;
      }

      renderer.render(scene, camera);
    };

    animate();

    // Handle window resize
    const handleResize = () => {
      const newWidth = canvasRef.current?.clientWidth || width;
      const newHeight = canvasRef.current?.clientHeight || height;
      camera.aspect = newWidth / newHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(newWidth, newHeight);
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      cancelAnimationFrame(animationId);
      renderer.dispose();
    };
  }, [images, width, height, currentImageIndex]);

  const nextImage = () => {
    setCurrentImageIndex((prev) => (prev + 1) % images.length);
  };

  const prevImage = () => {
    setCurrentImageIndex((prev) => (prev - 1 + images.length) % images.length);
  };

  return (
    <div className="w-full h-screen flex flex-col items-center justify-center bg-black">
      <canvas
        ref={canvasRef}
        className="max-w-4xl max-h-[80vh] border-4 border-gray-800 rounded-lg"
      />

      {/* Controls */}
      <div className="mt-8 flex gap-4 items-center">
        <button
          onClick={prevImage}
          className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition"
        >
          ← Previous
        </button>

        <span className="text-white text-lg">
          {currentImageIndex + 1} / {images.length}
        </span>

        <button
          onClick={nextImage}
          className="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition"
        >
          Next →
        </button>
      </div>

      {/* Info */}
      <div className="mt-6 text-gray-400 text-center">
        <p>Drag to rotate • Scroll to zoom</p>
      </div>
    </div>
  );
};

export default WebGLGallery;
