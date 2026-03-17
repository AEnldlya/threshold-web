# Design References - Inspiration Log

## Date: March 17, 2025

### Web Design Trends 2025 - Key Findings

#### Animation & Motion Trends
1. **Advanced Scroll Animations**
   - Sophisticated scroll-triggered animations that guide users through narrative
   - Reversible animations (play forward on scroll down, reverse on scroll up)
   - Timeline-based sequencing with GSAP-style motion
   - Scroll-scrubbed timelines for precise control

2. **Multi-Layer Parallax Effects**
   - Deep parallax with 3+ depth layers
   - Foreground, midground, background moving at different speeds
   - Creates premium, dimensional feel
   - Particularly effective for luxury branding

3. **3D Graphics & WebGL Integration**
   - Three.js and WebGL for immersive 3D experiences
   - ContentCore 3D elements in hero sections
   - 3D perspective transforms on images
   - Mouse-responsive tilt effects

4. **Micro-interactions & Hover Effects**
   - Magnetic cursor effects on interactive elements
   - Buttons that lift 2-3px with soft shadows
   - Cards with subtle glow on hover
   - Icons that rotate, pulse, or tilt gently
   - Link underlines with smooth left-to-right motion

#### Layout & Visual Trends
5. **Full-Viewport Heroes**
   - Always full viewport height (100vh)
   - Cinematic, intentional compositions
   - One signature visual moment per hero
   - No generic centered text + gradient blob patterns

6. **Typography Trends**
   - Large display fonts: 96-160px for H1
   - Tight letter-spacing on display text
   - Two-font pairing (display + body)
   - Fontshare fonts preferred over Google Fonts

7. **Color Palettes**
   - 4-color systems with named CSS variables
   - Warm off-whites or deep near-blacks (not pure white)
   - Luxury minimal palettes with deep contrast
   - Subtle atmospheric gradients

8. **Card & Component Design**
   - Borderless cards with 3D tilt effects
   - Glass morphism effects
   - Spotlight/radial gradient follows cursor
   - No generic rounded corners (either sharp 0px or full pill 9999px)

#### Navigation & Transitions
9. **Custom Navigation**
   - Transparent minimal headers
   - Hidden navigation (hamburger-only)
   - No standard sticky top nav bars

10. **Page Transitions**
    - Curtain reveal (horizontal or vertical wipe)
    - Fade-through with blur
    - Slide transitions matching navigation flow
    - Masked transitions using clip-path
    - 400-800ms duration with custom easing

#### Technical Implementation
11. **Performance Standards**
    - 60fps animations with GPU acceleration
    - Transform and opacity only for animations
    - WebP/AVIF image optimization
    - Lighthouse 95+ scores

12. **Accessibility**
    - WCAG AA compliance
    - Reduced motion support
    - Semantic HTML structure
    - Custom focus outlines (not browser defaults)

### Awwwards Category Insights

**Popular Tags on Award-Winning Sites:**
- Animation
- Parallax
- Microinteractions
- Transitions
- 3D
- Typography
- Interaction Design
- Storytelling
- Minimal
- Fullscreen

**Technology Stack Trends:**
- GSAP (GreenSock) for advanced animations
- Framer Motion for React
- Three.js for 3D
- Next.js for framework
- Tailwind CSS for styling
- Lenis/Locomotive Scroll for smooth scrolling

### Inspiration Sources

**Sites to Reference:**
- Awwwards (Sites of the Day, Month, Year)
- Framer Marketplace Templates
- Dribbble (web design category)
- Behance (web design galleries)

### Application for Samantha's Website

**Recommended Approach:**
1. Use full-viewport hero with cinematic reveal animation
2. Implement multi-layer parallax on scroll
3. Add magnetic cursor effects on CTAs
4. Create custom page transitions (curtain reveal)
5. Use 3D tilt cards for portfolio items
6. Implement scroll-triggered counter animations
7. Add ambient floating particles in hero
8. Use Fontshare typography pairing
9. Apply warm off-white or deep dark color scheme
10. Ensure all animations run at 60fps

---

*Next Review: March 18, 2025*
