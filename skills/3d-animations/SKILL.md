# 3D Animations Skill for OpenClaw

**Skill ID**: `3d-animations`

**Version**: 1.0.0

**Category**: Web Development / 3D / Visual Effects

**Status**: Production-Ready

## Skill Overview

Fetch 3D animation patterns from 21st.dev, generate advanced 3D effects using Three.js or Babylon.js, and seamlessly integrate them into websites for stunning visual impact.

### Primary Use Cases
1. **3D Hero Sections**: Interactive 3D backgrounds for landing pages
2. **Product Showcases**: Rotating 3D products with interactive controls
3. **3D Galleries**: WebGL-powered image galleries and lightboxes
4. **3D Text Effects**: Morphing text, flying typography, text distortions
5. **Scroll Interactions**: Parallax 3D, scroll-triggered animations
6. **Loading Screens**: Animated 3D loaders with particle effects
7. **Data Visualization**: Interactive 3D charts and graphs

## Installation

```bash
clawhub install 3d-animations
```

Or manually:
```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/clawhub/3d-animations.git
cd 3d-animations
pip install -r requirements.txt
```

## Commands

### 1. fetch_3d_animations_from_21st
Fetch and extract 3D animation prompts from 21st.dev.

```bash
3d_animations fetch_3d_animations_from_21st \
  --query "floating cube hero" \
  --category "3d" \
  --framework "three.js" \
  --limit 10 \
  --include-code
```

**Options**:
- `--query`: Search term for animations
- `--category`: Filter by category (3d, hero, product, text, etc.)
- `--framework`: Technology filter (three.js, babylon.js, pixi.js)
- `--limit`: Maximum results (default: 10)
- `--include-code`: Include source code samples

**Output**: JSON with animation metadata and code samples

---

### 2. integrate_3d_animation
Integrate a 3D animation into an existing website.

```bash
3d_animations integrate_3d_animation \
  --website-id "summer-street-hair-2026" \
  --animation-id "3d-hero-1" \
  --page "home" \
  --section "hero" \
  --colors "#3b82f6,#10b981" \
  --scale 1.2 \
  --speed 1.5 \
  --auto-deploy
```

**Options**:
- `--website-id`: Target website ID
- `--animation-id`: Animation to integrate
- `--page`: Target page (home, about, products, etc.)
- `--section`: Target section (hero, header, footer, etc.)
- `--colors`: Custom colors (comma-separated hex)
- `--scale`: Size scaling factor
- `--speed`: Animation speed multiplier
- `--intensity`: Effect intensity (low, medium, high)
- `--auto-deploy`: Deploy after integration

**Output**: Success status, component created, performance metrics

---

### 3. search_21st_dev_animations
Smart search for 3D animations on 21st.dev with filtering.

```bash
3d_animations search_21st_dev_animations \
  --query "morphing text 3d" \
  --frameworks "three.js,babylon.js" \
  --complexity "intermediate" \
  --performance "high" \
  --browser-support "modern"
```

**Options**:
- `--query`: Search term
- `--frameworks`: Technology filters
- `--complexity`: beginner, intermediate, advanced
- `--performance`: Performance level (high, medium, low)
- `--browser-support`: Browser compatibility filter

**Output**: Ranked animation results with compatibility info

---

### 4. create_custom_3d_animation
Generate a custom 3D animation from a text prompt.

```bash
3d_animations create_custom_3d_animation \
  --prompt "Create a rotating product showcase with glassmorphism cards" \
  --framework "three.js" \
  --use-cases "product_display,portfolio" \
  --performance-target 60 \
  --include-mobile
```

**Options**:
- `--prompt`: Animation description
- `--framework`: three.js or babylon.js
- `--use-cases`: Intended use cases
- `--performance-target`: Target FPS (default: 60)
- `--include-mobile`: Mobile optimization

**Output**: Generated component code, performance metrics, ready-to-deploy status

---

### 5. optimize_3d_performance
Optimize 3D animations for maximum performance and Lighthouse score.

```bash
3d_animations optimize_3d_performance \
  --website-id "summer-street-hair-2026" \
  --target-fps 60 \
  --target-lighthouse 95 \
  --include-mobile
```

**Options**:
- `--website-id`: Website to optimize
- `--target-fps`: Target frame rate
- `--target-lighthouse`: Target Lighthouse score
- `--include-mobile`: Optimize for mobile
- `--aggressive`: Apply aggressive optimizations

**Output**: Optimizations applied, before/after metrics, deployment status

---

### 6. batch_add_3d_to_websites
Add 3D animations to multiple websites in parallel.

```bash
3d_animations batch_add_3d_to_websites \
  --websites "[{\"website_id\": \"site-1\", \"animation_type\": \"hero-3d\"}, ...]" \
  --max-parallel 3 \
  --deploy-all
```

**Options**:
- `--websites`: JSON array of website configs
- `--max-parallel`: Concurrent processing limit
- `--deploy-all`: Deploy all after processing

**Output**: Batch processing results, timing, deployment status

---

### 7. extract_21st_dev_prompts
Extract and cache animation prompts from 21st.dev for local reuse.

```bash
3d_animations extract_21st_dev_prompts \
  --category "3d" \
  --extract-prompts \
  --extract-code \
  --save-locally \
  --format "markdown"
```

**Options**:
- `--category`: Animation category filter
- `--extract-prompts`: Extract text prompts
- `--extract-code`: Extract code samples
- `--save-locally`: Save to local cache
- `--format`: Output format (markdown or json)

**Output**: Extracted prompts and code, saved to local library

---

## Configuration

Create `.env` in the skill directory:

```bash
# 21st.dev configuration
TWENTYFIRST_DEV_URL=https://21st.dev
TWENTYFIRST_DEV_API_KEY=your_api_key_here

# Performance settings
TARGET_FPS=60
TARGET_LIGHTHOUSE=95
MOBILE_QUALITY_SCALE=0.75

# Deployment settings
AUTO_DEPLOY=true
VERCEL_TOKEN=your_vercel_token
GITHUB_TOKEN=your_github_token

# Optimization settings
ENABLE_LOD=true
ENABLE_TEXTURE_COMPRESSION=true
MAX_DRAW_CALLS=100
```

## File Structure

```
~/.openclaw/workspace/skills/3d-animations/
├── SKILL.md                          # This file
├── README.md                         # Comprehensive guide
├── 3d_animations.py                  # Main CLI entry point
├── requirements.txt                  # Python dependencies
├── .env.example                      # Configuration template
├── src/
│   ├── __init__.py
│   ├── 21st_dev_fetcher.py          # 21st.dev scraper & API
│   ├── prompt_parser.py              # Parse animation prompts
│   ├── prompt_library.py             # Local caching system
│   ├── three_js_generator.py         # Three.js code generation
│   ├── babylon_js_generator.py       # Babylon.js code generation
│   ├── animation_integrator.py       # Website integration
│   ├── 3d_components.py              # Component library
│   ├── performance_optimizer.py      # Performance optimization
│   ├── mobile_handler.py             # Mobile detection & scaling
│   └── deployment_manager.py         # Deployment automation
├── prompts/
│   ├── 3d-hero-animations.md         # Hero section prompts (100+)
│   ├── 3d-product-showcase.md        # Product display prompts
│   ├── 3d-text-effects.md            # Text animation prompts
│   ├── 3d-scroll-interactions.md     # Scroll-triggered prompts
│   └── 3d-gallery.md                 # Gallery prompts
├── components/
│   ├── FloatingCube.tsx              # Floating 3D cube
│   ├── MorphingText.tsx              # 3D text morphing
│   ├── ProductRotator.tsx            # 360° product viewer
│   ├── ParticleSystem.tsx            # Particle effects
│   ├── ScrollHero.tsx                # Scroll-triggered hero
│   └── WebGLGallery.tsx              # WebGL gallery
├── examples/
│   ├── example_fetch_3d.py           # Fetch animations
│   ├── example_integrate_3d.py       # Integrate into website
│   ├── example_custom_animation.py   # Create custom 3D
│   └── example_batch_3d.py           # Batch processing
├── test_3d_animations.py             # 40+ unit tests
└── .gitignore
```

## Performance Targets

✅ **Desktop**:
- FPS: 60 constant
- Lighthouse: 95+
- LCP: <2.5s
- CLS: <0.1
- FID: <100ms

✅ **Mobile**:
- FPS: 30-60 (adaptive)
- Lighthouse: 90+
- Adaptive quality scaling
- Touch-optimized

✅ **Code Quality**:
- Full type hints
- 40+ unit tests
- 100% error handling
- Comprehensive logging

## Examples

### Fetch 3D animations from 21st.dev
```python
from skills.3d_animations.src import fetcher

animations = fetcher.fetch_from_21st(
    query="floating cube hero animation",
    framework="three.js",
    limit=10
)

for anim in animations:
    print(f"{anim['name']}: {anim['description']}")
    print(f"Code: {anim['code']}")
```

### Integrate into website
```python
from skills.3d_animations.src import integrator

result = integrator.integrate_animation(
    website_id="summer-street-hair",
    animation_id="3d-hero-1",
    customize={
        "colors": ["#d4af37", "#ffffff"],
        "speed": 1.5
    }
)

print(f"Lighthouse score: {result['lighthouse_score']}")
print(f"FPS: {result['performance_fps']}")
```

### Create custom 3D animation
```python
from skills.3d_animations.src import generator

code = generator.create_custom_animation(
    prompt="Create a rotating product showcase with glassmorphism",
    framework="three.js",
    performance_target=60
)

print(code)  # Ready-to-use TSX component
```

## Support

- **GitHub Issues**: Report bugs and feature requests
- **Discord**: Community support
- **Email**: support@clawhub.com

## License

MIT License - Use freely in your projects

## Changelog

### v1.0.0 (Initial Release)
- Complete 21st.dev fetching
- Three.js code generation
- Website integration
- Performance optimization
- Mobile support
- Batch processing
- 40+ unit tests

---

**Built with ❤️ by the OpenClaw community**
