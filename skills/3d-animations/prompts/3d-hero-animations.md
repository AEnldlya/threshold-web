# 3D Hero Animations

Collection of 3D animation prompts for hero sections from 21st.dev.

## 1. Floating Cube with Particles

**Prompt**: Create a 3D floating cube with particle system for hero section

**Description**: Interactive cube that rotates with surrounding particles

**Framework**: Three.js

**Difficulty**: Intermediate

**Performance**: 60 FPS on desktop, 30-40 FPS on mobile

**Best For**: Tech companies, innovative brands, product launches

---

## 2. Morphing Shapes

**Prompt**: Create morphing 3D shapes that transition smoothly between geometries

**Description**: Shapes that morph between cube, sphere, and tetrahedron

**Framework**: Three.js

**Difficulty**: Advanced

**Performance**: 60 FPS desktop

**Best For**: Design studios, creative agencies

---

## 3. Particle Explosion

**Prompt**: Create a particle explosion effect triggered on page load

**Description**: Particles explode from center with gravity effect

**Framework**: Three.js + Cannon.js

**Difficulty**: Advanced

**Performance**: 30-60 FPS (scaling)

**Best For**: Gaming studios, action-oriented brands

---

## 4. Floating Particles

**Prompt**: Create floating particles that respond to mouse movement

**Description**: Thousands of particles that attract to mouse position

**Framework**: Three.js

**Difficulty**: Intermediate

**Performance**: 60 FPS desktop

**Best For**: Creative portfolios, technology companies

---

## 5. Rotating Models

**Prompt**: Create rotating 3D models with lighting effects

**Description**: Smooth rotation with dynamic lighting

**Framework**: Three.js

**Difficulty**: Intermediate

**Performance**: 60 FPS

**Best For**: Product companies, design portfolios

---

## 6. Glowing Orbs

**Prompt**: Create multiple glowing orbs that orbit around a center point

**Description**: Glowing spheres with bloom post-processing effect

**Framework**: Three.js

**Difficulty**: Advanced

**Performance**: 45-60 FPS

**Best For**: Premium brands, luxury products

---

## 7. Abstract Landscape

**Prompt**: Create an abstract 3D landscape that responds to scroll

**Description**: Procedural terrain with interactive camera

**Framework**: Three.js

**Difficulty**: Advanced

**Performance**: 30-60 FPS (scaling)

**Best For**: Travel, nature-focused sites

---

## 8. Neural Network Visualization

**Prompt**: Create animated neural network nodes connected with lines

**Description**: Interactive nodes with flowing data between them

**Framework**: Three.js

**Difficulty**: Advanced

**Performance**: 45-60 FPS

**Best For**: AI/ML companies, tech startups

---

## 9. Holographic Interface

**Prompt**: Create a futuristic holographic interface effect

**Description**: Glowing lines and grids forming interactive interface

**Framework**: Three.js

**Difficulty**: Advanced

**Performance**: 50-60 FPS

**Best For**: Sci-fi themes, tech companies

---

## 10. Crystalline Structure

**Prompt**: Create a crystalline 3D structure with reflection and refraction

**Description**: Geometric crystal with realistic materials

**Framework**: Three.js

**Difficulty**: Advanced

**Performance**: 30-50 FPS

**Best For**: Jewelry, minerals, luxury brands

---

## Implementation Tips

### Desktop Optimization (60 FPS)
- Use InstancedMesh for repeated geometries
- Enable LOD (Level of Detail)
- Minimize draw calls
- Use WebGL context hints

### Mobile Optimization (30 FPS)
- Reduce geometry complexity by 50%
- Lower particle counts
- Use compressed textures
- Implement quality scaling

### General Best Practices
- Use BufferGeometry, not Geometry
- Implement frustum culling
- Cache transforms
- Use Object3D.updateMatrixWorld(false)
- Monitor with Chrome DevTools

---

**Last Updated**: January 2024

**Source**: 21st.dev Animation Library
