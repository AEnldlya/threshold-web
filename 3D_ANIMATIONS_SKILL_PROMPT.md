# 3D Animations Skill - Advanced Web Development

**Goal**: Create an OpenClaw skill that fetches animation prompts from 21st.dev, adds 3D effects, and integrates them into websites using Three.js, Babylon.js, and Framer Motion.

**Status**: Ready for implementation

---

## Skill Overview

### Name
`3d-animations`

### Description
Fetch 3D animation patterns from 21st.dev, integrate advanced 3D effects (Three.js, Babylon.js), and auto-apply to websites for stunning visual impact.

### Use Cases
1. **3D Hero Sections**: Interactive 3D backgrounds
2. **3D Product Displays**: Rotating products, models
3. **3D Galleries**: WebGL image galleries
4. **3D Text Effects**: Flying text, morphing typography
5. **3D Data Visualization**: Charts, graphs, animations
6. **3D Scroll Interactions**: Parallax, scroll-triggered 3D
7. **3D Loading Screens**: Animated loaders with 3D

---

## Technical Architecture

### Core Dependencies
```
requests>=2.31.0              # HTTP for 21st.dev API
three-py>=0.0.0               # Three.js Python wrapper
babylon-py>=0.0.0             # Babylon.js wrapper
framer-motion>=10.0.0          # Advanced animations
tailwindcss>=3.3.0             # Styling
gsap>=3.12.0                   # Animation library
pixijs>=8.0.0                  # 2D WebGL renderer
```

### Recommended Tech Stack
- **3D Framework**: Three.js (primary) + Babylon.js (alternative)
- **Animation Library**: GSAP 3 (for sequential/complex animations)
- **3D Models**: glTF/GLB format (optimized)
- **Particle System**: Three.js particles or custom
- **Physics**: Cannon.js or Rapier (optional)
- **VR/AR**: Three.js with WebXR (future)

---

## Skill Commands

### 1. `fetch_3d_animations_from_21st`
**Purpose**: Fetch animation prompts from 21st.dev

**Input**:
```python
{
  "query": "3d hero animation",  # Search term
  "category": "3d",              # Animation category
  "filter_by": "three.js",       # Technology filter
  "limit": 10,                   # Max results
  "include_code": True           # Include code samples
}
```

**Output**:
```json
{
  "success": true,
  "animations_found": 8,
  "animations": [
    {
      "id": "3d-hero-1",
      "name": "Floating cube with particles",
      "description": "3D cube floating with particle effects",
      "technology": "three.js",
      "difficulty": "intermediate",
      "code": "// Full code from 21st.dev",
      "prompt": "Create a floating 3D cube with particle system...",
      "preview_url": "https://21st.dev/animations/3d-hero-1"
    }
  ]
}
```

---

### 2. `integrate_3d_animation`
**Purpose**: Integrate 3D animation into website

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "animation_id": "3d-hero-1",
  "page": "home",
  "section": "hero",
  "customize": {
    "colors": ["#3b82f6", "#10b981"],
    "scale": 1.2,
    "speed": 1.5,
    "intensity": "high"
  },
  "auto_deploy": True
}
```

**Output**:
```json
{
  "success": true,
  "animation_integrated": true,
  "component_created": "components/3d/FloatingCube.tsx",
  "imports_added": [
    "import * as THREE from 'three'",
    "import { useFrame } from '@react-three/fiber'"
  ],
  "performance_score": 92,
  "lighthouse_score": 94,
  "deployed": true
}
```

---

### 3. `search_21st_dev_animations`
**Purpose**: Smart search for animations on 21st.dev

**Input**:
```python
{
  "query": "morphing text 3d",
  "frameworks": ["three.js", "babylon.js"],
  "complexity": "intermediate",
  "performance": "high",  # "high" = <60ms render
  "browser_support": "modern"
}
```

**Output**:
```json
{
  "success": true,
  "total_results": 15,
  "best_matches": [
    {
      "rank": 1,
      "name": "3D Morphing Text",
      "framework": "three.js",
      "performance_rating": 9.5,
      "browser_support": ["Chrome", "Firefox", "Safari"],
      "code_quality": "production-ready"
    }
  ]
}
```

---

### 4. `create_custom_3d_animation`
**Purpose**: Generate custom 3D animation from prompt

**Input**:
```python
{
  "prompt": "Create a 3D rotating product showcase with glassmorphism cards",
  "framework": "three.js",
  "use_cases": ["product_display", "portfolio"],
  "performance_target": 60,  # FPS
  "include_mobile": True
}
```

**Output**:
```json
{
  "success": true,
  "animation_generated": true,
  "code_file": "components/3d/ProductShowcase.tsx",
  "lines_of_code": 342,
  "libraries_used": ["three.js", "framer-motion", "tailwindcss"],
  "performance": 58,
  "mobile_optimized": true,
  "ready_to_deploy": true
}
```

---

### 5. `optimize_3d_performance`
**Purpose**: Optimize 3D animations for performance

**Input**:
```python
{
  "website_id": "summer-street-hair-2026",
  "target_fps": 60,
  "target_lighthouse": 95,
  "include_mobile": True
}
```

**Output**:
```json
{
  "success": true,
  "optimizations_applied": [
    "Geometry LOD (level of detail)",
    "Texture optimization (compressed)",
    "Draw call reduction",
    "Mobile device detection",
    "WebGL context optimization",
    "Lazy loading 3D assets"
  ],
  "performance_before": 52,
  "performance_after": 59,
  "lighthouse_before": 87,
  "lighthouse_after": 94
}
```

---

### 6. `batch_add_3d_to_websites`
**Purpose**: Add 3D animations to multiple websites in parallel

**Input**:
```python
{
  "websites": [
    {
      "website_id": "site-1",
      "animation_type": "hero-3d",
      "customization": {}
    },
    {
      "website_id": "site-2",
      "animation_type": "product-3d",
      "customization": {}
    }
  ],
  "max_parallel": 3,
  "deploy_all": True
}
```

**Output**:
```json
{
  "success": true,
  "websites_processed": 3,
  "successful": 3,
  "total_time": 480,
  "animations_added": 3,
  "all_deployed": true
}
```

---

### 7. `extract_21st_dev_prompts`
**Purpose**: Extract animation prompts from 21st.dev for reuse

**Input**:
```python
{
  "category": "3d",
  "extract_prompts": True,
  "extract_code": True,
  "save_locally": True,
  "format": "markdown"  # or "json"
}
```

**Output**:
```json
{
  "success": true,
  "prompts_extracted": 45,
  "saved_to": "/workspace/21st-dev-prompts/3d-animations.md",
  "categories": [
    "3d-hero",
    "3d-product",
    "3d-text",
    "3d-scroll",
    "3d-gallery"
  ]
}
```

---

## Implementation Strategy

### Phase 1: 21st.dev Integration
1. **21st.dev API/Scraper**
   - Search animations on 21st.dev
   - Parse animation prompts
   - Extract code samples
   - Cache for reuse

2. **Prompt Library**
   - Store 100+ animation prompts
   - Categorize by type
   - Tag by framework, difficulty
   - Include code examples

3. **Search & Discovery**
   - Full-text search
   - Filter by framework
   - Filter by complexity
   - Rate by performance

### Phase 2: 3D Animation Integration
1. **Three.js Integration**
   - Create 3D hero components
   - Product display 3D
   - Text morphing 3D
   - Particle systems

2. **Advanced Effects**
   - Lighting and shadows
   - Materials and textures
   - Reflections/refractions
   - Post-processing

3. **Mobile Optimization**
   - Device detection
   - Performance scaling
   - Touch interactions
   - Fallbacks for low-end

### Phase 3: Website Integration
1. **Auto-Integration**
   - Parse website structure
   - Insert 3D components
   - Update package.json
   - Configure build

2. **Customization**
   - Color theming
   - Size/scale adjustments
   - Speed/intensity
   - Performance tuning

### Phase 4: Quality & Deployment
1. **Performance Testing**
   - Lighthouse scoring
   - Frame rate monitoring
   - Core Web Vitals
   - Browser compatibility

2. **Deployment**
   - Build optimization
   - Deploy to Vercel
   - Monitor performance
   - Rollback if needed

---

## File Structure

```
~/.openclaw/workspace/skills/3d-animations/
├── SKILL.md                          # Skill metadata
├── README.md                         # User guide
├── 3d_animations.py                  # Main CLI
├── src/
│   ├── __init__.py
│   ├── 21st_dev_fetcher.py          # Fetch from 21st.dev
│   ├── prompt_parser.py              # Parse animation prompts
│   ├── prompt_library.py             # Local prompt cache
│   ├── three_js_generator.py         # Generate Three.js code
│   ├── babylon_js_generator.py       # Generate Babylon.js code
│   ├── animation_integrator.py       # Integrate into websites
│   ├── 3d_components.py              # Reusable 3D components
│   ├── performance_optimizer.py      # Optimize 3D perf
│   ├── mobile_handler.py             # Mobile optimization
│   └── deployment_manager.py         # Deploy changes
├── prompts/
│   ├── 3d-hero-animations.md         # Hero section prompts
│   ├── 3d-product-showcase.md        # Product display prompts
│   ├── 3d-text-effects.md            # Text animation prompts
│   ├── 3d-scroll-interactions.md     # Scroll-triggered prompts
│   └── 3d-gallery.md                 # Gallery prompts
├── components/
│   ├── FloatingCube.tsx
│   ├── MorphingText.tsx
│   ├── ProductRotator.tsx
│   ├── ParticleSystem.tsx
│   ├── ScrollHero.tsx
│   └── WebGLGallery.tsx
├── examples/
│   ├── example_fetch_3d.py           # Fetch animation example
│   ├── example_integrate_3d.py       # Integration example
│   ├── example_custom_animation.py   # Custom animation example
│   └── example_batch_3d.py           # Batch processing example
├── test_3d_animations.py             # 40+ unit tests
├── requirements.txt
└── .env.example
```

---

## Core Modules

### 21st_dev_fetcher.py (18 KB)
Fetch animations from 21st.dev:
- Search animations
- Parse HTML/API
- Extract code samples
- Extract prompts
- Cache locally
- Rate limiting

### prompt_parser.py (14 KB)
Parse animation prompts:
- Extract key concepts
- Identify frameworks
- Parse code blocks
- Extract parameters
- Generate variants

### prompt_library.py (16 KB)
Local prompt library:
- Store 100+ prompts
- Full-text search
- Filter by category
- Filter by framework
- Caching system
- Version control

### three_js_generator.py (22 KB)
Generate Three.js code:
- Create 3D scenes
- Add geometries
- Add materials
- Add lighting
- Add animations
- Add interactions

### animation_integrator.py (18 KB)
Integrate 3D into websites:
- Inject components
- Update dependencies
- Configure imports
- Setup Three.js context
- Add performance monitoring
- Handle fallbacks

### performance_optimizer.py (16 KB)
Optimize 3D performance:
- Detect device capabilities
- Scale quality
- Implement LOD
- Compress textures
- Reduce draw calls
- Monitor FPS

---

## 3D Animation Categories (from 21st.dev)

### 1. Hero Animations
```
• Floating 3D cubes
• Morphing shapes
• Particle explosions
• Floating particles
• Rotating models
• Glowing orbs
```

### 2. Product Showcase
```
• 360-degree product rotation
• Product zooming
• Material showcase
• Color variations
• Size comparison
• Interactive exploration
```

### 3. Text Effects
```
• 3D flying text
• Text morphing
• Text distortion
• Text particles
• Text trails
• Glitch effects
```

### 4. Scroll Interactions
```
• Parallax 3D
• Scroll-triggered 3D
• Scroll-based rotation
• Scroll-based scale
• Scroll path animations
• Scroll reveal 3D
```

### 5. Galleries
```
• 3D card flip
• 3D carousel
• WebGL gallery
• 3D masonry
• 3D lightbox
• 360 photo viewer
```

### 6. Data Visualization
```
• 3D charts
• 3D graphs
• 3D bar charts
• 3D scatter plots
• 3D line charts
• Real-time data animation
```

### 7. Loading Screens
```
• 3D spinning loader
• Particle loader
• Progress bar 3D
• Loading text animation
• Animated skeleton
• Custom loader animation
```

---

## Integration Example

### From 21st.dev to Website

**Step 1: Fetch from 21st.dev**
```python
animations = skill.fetch_3d_animations_from_21st(
    query="floating cube hero animation",
    framework="three.js"
)
```

**Step 2: Extract Prompt & Code**
```python
prompt = animations[0]['prompt']
code = animations[0]['code']
# Prompt: "Create a floating 3D cube with particle system..."
# Code: Full Three.js implementation
```

**Step 3: Customize for Your Brand**
```python
result = skill.integrate_3d_animation(
    website_id="summer-street-hair",
    animation_id="3d-hero-1",
    customize={
        "colors": ["#d4af37", "#ffffff"],  # Gold and white
        "speed": 1.5
    }
)
```

**Step 4: Deploy**
```python
# Auto-deployed with Lighthouse 94+
# Mobile optimized
# 3D assets compressed
# Ready for production
```

---

## Performance Standards

✅ **Desktop Performance**:
- FPS: 60 constant
- Lighthouse: 95+
- LCP: <2.5s
- Core Web Vitals: Good

✅ **Mobile Performance**:
- FPS: 30-60 (scaling)
- Lighthouse: 90+
- Adaptive quality
- Touch optimized

✅ **Code Quality**:
- TypeScript strict
- Full type hints
- Error handling
- Logging
- 40+ unit tests

---

## Success Criteria

✅ Can fetch animations from 21st.dev
✅ Can parse animation prompts accurately
✅ Can generate Three.js code
✅ Can integrate into existing websites
✅ Can optimize for 60 FPS
✅ Can handle mobile devices
✅ Maintains Lighthouse 95+ score
✅ Batch process multiple websites
✅ Full documentation
✅ Production-ready code

---

## Technology Stack

**Fetching**:
- Requests (HTTP)
- BeautifulSoup (HTML parsing)
- Playwright (JavaScript rendering)

**3D Generation**:
- Three.js (primary 3D framework)
- Babylon.js (alternative)
- GSAP (animations)
- Cannon.js (physics - optional)

**Optimization**:
- TinyGltf (3D model compression)
- Imagemin (texture compression)
- Terser (code minification)

**Testing**:
- Pytest (unit tests)
- Lighthouse (performance)
- WebGL debugger

---

## Next Steps for Implementation

1. **Phase 1**: Build 21st.dev fetcher (18 KB)
2. **Phase 2**: Create prompt library (16 KB)
3. **Phase 3**: Generate Three.js code (22 KB)
4. **Phase 4**: Integrate into websites (18 KB)
5. **Phase 5**: Optimize performance (16 KB)
6. **Phase 6**: Mobile support (14 KB)
7. **Phase 7**: Testing & deployment (20 KB)

---

## Timeline

- **MVP (Phase 1-3)**: 1-2 weeks
  - Fetch from 21st.dev
  - Basic 3D generation
  - Simple integration

- **Production (Phase 1-5)**: 2-3 weeks
  - Full feature set
  - Performance optimization
  - Batch processing

- **Enterprise (Phase 1-7)**: 3-4 weeks
  - Complete testing
  - Mobile optimization
  - Advanced features

---

## Integration with OpenClaw Agents

### With Claude WebDev Skill
- Auto-add 3D animations to generated websites
- Use 21st.dev prompts for code generation
- 3D component library

### With Instagram Reels Skill
- Extract animation style from reels
- Translate to 3D equivalents
- Auto-apply to websites

### With Stock Watcher
- Celebrate stock wins with 3D animations
- Portfolio showcase with 3D products

### With CPA Agent
- Log animation enhancement cost ($0)
- Track increased conversion value (+$500-1000)
- Calculate ROI

---

**Ready for implementation!** This skill brings 3D animations from 21st.dev directly into your websites. 🚀

Follow this prompt to create the complete `3d-animations` skill.
