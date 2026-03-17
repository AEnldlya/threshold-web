---
name: frontend-design-enhanced
description: Production-grade frontend design system with business-type deduction, Fontshare typography, 21st.dev animations, and ContentCore 3D. Creates distinctive, human-looking websites that avoid generic AI aesthetics.
---

# Frontend Design Enhanced

Production-grade design system for building human-looking websites. Before writing code, run the BUSINESS DEDUCTION SYSTEM to auto-select typography, color, 3D usage, and animation tone.

## Business Deduction System

Identify the business type, then apply the matching row as your starting defaults:

| BUSINESS TYPE | DISPLAY FONT | BODY FONT | COLOR DIRECTION | 3D USAGE | ANIMATION TONE |
|--------------|--------------|-----------|-----------------|----------|----------------|
| SaaS / Tech startup | Clash Display | Satoshi | Dark base + electric accent | Device mockup hero | Counters, skeleton shimmer, subtle fades |
| Luxury / Fashion | Melodrama or Boska | Zodiak/Sentient | Cream + deep ink, minimal accent | Abstract floating shape | Slow silk reveals, clip-path wipes |
| Creative agency | Tanker or Ranade | Switzer | High contrast + unexpected accent | 3D logotype statement | Scramble text, kinetic swap, glitch |
| Restaurant / Food | Author or Rowan | General Sans | Warm, earthy palette | Floating product/dish shot | Gentle fade-up, slow parallax |
| Finance / Legal | Fraunces | Epilogue | Navy/charcoal + gold or teal | Minimal or none | Counters, progress fill, subtle reveals |
| Health / Wellness | Syne Serif | Chillax | Soft green, cream, warm white | None or organic shape | Breathe animations, slow fade |
| Gaming / Entertainment | Clash Display | Supreme | Near-black + neon accent | Full 3D hero, rotating models | Glitch, snap, spring physics |
| Portfolio / Personal | Boska or Melodrama | Cabinet Grotesk | Monochromatic + one sharp accent | Optional 3D name/title | Scramble reveal, stagger, magnetic |
| E-commerce / Retail | Cabinet Grotesk | General Sans | Brand-extracted, warm or bold | Product 3D mockup | Hover card tilt, fill sweep buttons |
| Education / Non-profit | Plein | Epilogue | Accessible, warm, readable | Minimal or none | Scroll reveal, counter increment |

Always add a one-line comment justifying the choice:
```css
/* Clash Display: tech-forward SaaS, needs authority + edge */
```

## Typography (Fontshare)

All fonts loaded from Fontshare — free, commercial-use, from Indian Type Foundry.

Load syntax:
```css
@import url('https://api.fontshare.com/v2/css?f[]=satoshi@700,400&display=swap');
```

### Font Catalog

**Sans-Serif (modern/neutral):**
- Satoshi — geometric grotesque, 10 styles + variable. Best for: SaaS, tech, clean UI
- General Sans — neutral humanist, works at body AND display. Best for: food, e-commerce, neutral brands
- Cabinet Grotesk — softened terminals, friendlier tone. Best for: portfolios, lifestyle brands
- Switzer — clean neo-grotesk, sharp. Best for: agencies, editorial
- Clash Grotesk — small apertures, very distinctive. Best for: corporate identity, editorial
- Epilogue — versatile 18 styles + variable. Best for: body text, accessible UI
- Plein — humanist, double-storey a/g, very readable. Best for: education, professional services
- Chillax — rounded, friendly. Best for: wellness, consumer apps
- Supreme — bold weight-focused. Best for: gaming, entertainment

**Display/Statement (headings only):**
- Clash Display — ultra-wide at heavy weights, high contrast strokes. Best for: tech, gaming, bold brands
- Boska — elegant high-contrast serif display. Best for: luxury, editorial, portfolios
- Melodrama — editorial high-fashion display. Best for: fashion, luxury, creative studios
- Tanker — heavy slab display. Best for: agencies, impact-first brands
- Ranade — strong display serif. Best for: agencies, editorial
- Author — humanist display. Best for: food, hospitality

**Serif/Editorial:**
- Fraunces — soft optical serif, beautiful italics. Best for: finance, longform, legal
- Sentient — elegant transitional serif. Best for: luxury, fashion
- Zodiak — high-contrast editorial serif. Best for: magazines, fashion
- Syne Serif — geometric serif. Best for: wellness, modern editorial
- Rowan — warm serif. Best for: restaurants, hospitality

### Pairing Rules
- Always pair ONE display font + ONE body font. Never use more than two families.
- Display font: use only at headings (h1, h2), hero text, large pull quotes
- Body font: everything else — nav, paragraphs, labels, buttons, captions
- When in doubt: Clash Display + Satoshi (tech), Boska + General Sans (editorial), Melodrama + Switzer (luxury)
- NEVER use: Inter, Roboto, Arial, system-ui, or Space Grotesk

## Color System

Rules:
- Always use CSS custom properties (--color-base, --color-accent, --color-text, --color-surface)
- Use a dominant base color with ONE sharp accent — avoid even color distribution
- Vary between light and dark themes across different builds — never default to the same
- NEVER use default Tailwind blue (#3B82F6) as an accent

### Palettes by tone:
- Tech/SaaS: #0A0A0F base, #00E5FF or #39FF14 accent
- Luxury: #FAF7F2 base, #1A1208 text, #C9A84C gold accent
- Agency/Creative: #0D0D0D base, #FF3B00 or #E8FF00 accent
- Food/Hospitality: #FDF6EE base, #2C1810 text, #D4824A accent
- Finance: #0F1923 base, #E8D5A3 gold accent
- Wellness: #F5F0EB base, #3D6B4F green accent
- Gaming: #060608 base, #00FF88 or #FF00FF neon accent

## Layout Rules

Default direction: Asymmetry. Overlap. Diagonal flow. Grid-breaking elements.
Pick ONE layout pattern and commit to it throughout the site.

### Layout options:
- 12-column CSS Grid (SaaS, finance, data-heavy)
- Bento box / card grid (tech, portfolios, dashboards)
- Editorial magazine-style — large hero type, staggered columns (luxury, fashion, creative)
- Brutalist — raw, intentionally misaligned (agencies, art, creative studios)
- Centered narrow column (blogs, longform, education)
- Full-bleed alternating sections (e-commerce, marketing sites)
- Overlapping z-index layers with sticky scroll panels (high-impact portfolios, luxury)

### Spacing scale:
- Multiples of 8px
- Section padding minimum 80px vertical on desktop, 48px mobile
- Grid: max-width 1280px, gutters 24px desktop / 16px mobile

## Animation System (21st.dev)

Source: 21st.dev — 426+ animated React components, Tailwind CSS, built for Next.js.

### Animation Picker — use tone to select:
- Brutalist/bold tone → glitch, snap cuts, hard cubic-bezier easing, short duration (0.15–0.25s)
- Luxury/editorial tone → slow silk reveals, clip-path wipes, long ease-out (0.8–1.4s)
- Playful/consumer tone → spring physics, elastic stretch, bounce (Motion library)
- Data/SaaS tone → counters, progress fills, skeleton shimmer, subtle fade-up
- Text-heavy content → typography animations first (scramble, stagger, marquee)
- Image-heavy content → clip-path reveals, parallax depth layers
- Any site → ONE signature hero animation that defines the page; everything else supports quietly

### Animation Library from 21st.dev:

**Text (58 components):**
Typewriter + cursor blink, scramble decode (Matrix-style), word-by-word stagger, kinetic word swap (vertical ticker), marquee infinite scroll, gradient color shift per char, counter increment (numbers count up), character-by-character reveal, text mask wipe

**Heroes (73 components):**
Full-viewport animated, split-layout with motion, shader abstract background, video background, 3D perspective hero, particle field hero

**Shaders (15 components — WebGL/GLSL):**
Noise gradient field, aurora borealis hue-shift, liquid blob morph, bokeh depth-of-field layers, scanline CRT flicker

**Backgrounds (33 components):**
Gradient mesh drift, animated particle field, noise grain overlay, geometric pattern pan, starfield parallax, dot grid breathe pulse

**Scroll Areas (24 components):**
Horizontal scroll gallery, parallax depth, scroll progress indicator, sticky pinned reveal panels, SVG path draw on scroll

**Buttons (130 components):**
Fill sweep (color floods from edge), magnetic cursor follow, elastic stretch on press, glow bloom on hover, border trace draw, ripple from click point

**Cards (79 components):**
3D tilt with light reflection (gyroscope-style), clip-path reveal on hover, glassmorphism blur, bento tile layout

**Hooks (31 utility hooks):**
Spring physics, scroll-triggered state, mouse position tracking, reduced-motion detection

### Libraries to use:
- CSS only (keyframes, @property, clip-path) — for HTML artifacts and mobile-first
- Motion (Framer Motion) — for React, spring physics, layout animations
- GSAP + ScrollTrigger — for complex timeline sequences and scroll-driven motion
- Three.js / GLSL — for WebGL hero moments and shader backgrounds

## 3D Elements (ContentCore.xyz)

EVERY website built with this system should include at least ONE 3D element.

### When to use what:
- Hero section → Rotating device mockup showing the product/app (WEBM, transparent bg, autoplay loop)
- Feature section → Floating 3D icon or abstract shape accent per feature card
- About / brand section → 3D logotype or abstract identity shape
- Product showcase → Multi-angle 3D render exported as looping WEBM
- Background texture → Abstract 3D geometry as subtle ambient layer behind content
- Gaming / entertainment → Full 3D scene as hero background

### How to embed:
Export from ContentCore as .webm with transparent background.
```html
<video autoplay loop muted playsinline style="mix-blend-mode: screen;">
  <source src="your-3d-asset.webm" type="video/webm">
</video>
```
Use CSS mix-blend-mode (screen, multiply, overlay) to blend seamlessly with any background.

### 3D Material Rules by Business:
- Tech/SaaS: glass material, cool blue/cyan lighting, dark environment
- Luxury: gold/chrome material, warm studio lighting, minimal rotation
- Agency: matte bold colors, dramatic shadows, fast rotation
- Wellness: soft clay or matte green, warm ambient light, slow drift
- Gaming: emissive neon materials, dark environment, particle trails

## Component Patterns

### Navigation:
- Tech/SaaS: sticky top bar with blur backdrop, pill CTA button
- Luxury/Fashion: minimal top bar, text-only nav, no background
- Agency: floating pill nav OR sidebar
- E-commerce: sticky top with cart icon + search

### Cards:
- Tech: flat + border or glassmorphism with subtle glow
- Luxury: no border, white space does the work, thin rule separators
- Agency: overlapping, broken grid, bold typography cards
- E-commerce: clean image-forward with hover zoom + fill sweep button

### Buttons:
- Tech: sharp rectangle, ghost variant for secondary
- Luxury: pill shape, no fill, just border + letter-spaced label
- Agency: full-width bold slab with color fill sweep animation
- E-commerce: pill, high contrast, fill sweep on hover

### Heroes:
- Always full-viewport height on desktop
- Always includes: headline (display font, large), subhead (body font), one CTA, one 3D element
- Background: either shader, gradient mesh, or solid with 3D WEBM overlay

## Anti-Patterns (Never Do These)

### Typography:
- Inter, Roboto, Arial, system-ui, -apple-system
- Space Grotesk (overused)
- More than 2 font families on one site
- Using a display font at body size

### Color:
- Purple gradient on white background
- Default Tailwind blue #3B82F6 as accent
- Even color distribution — pick a dominant, use accent sparingly
- More than 2 accent colors

### Layout:
- Centered hero with gradient blob background and floating card UI screenshots
- Three-column feature grid with icon + heading + paragraph (the most overdone SaaS pattern)
- Rounded corners above 12px (use either sharp 0–4px or full pill, nothing mushy in between)
- Stock photo placeholders

### Animation:
- Animation on every single element — exhausting and cheap
- Infinite looping animations that never stop (except marquees and background ambience)
- Scroll-jacking that breaks native scroll behavior
- Purple/blue gradient button with shine sweep (cliche)

### Components:
- Auto-playing carousel/slider
- Cookie banner as modal
- Hero with video background + dark overlay + centered white text (overused)
- Footer with 4 equal columns of links

## Design System Execution Checklist

Before finalizing any website build, verify:

- [ ] Business type identified and deduction table applied
- [ ] Fontshare fonts loaded via API — correct display + body pair for the business
- [ ] Font comment added in code justifying the choice
- [ ] Color system uses CSS variables and follows dominant + accent rule
- [ ] Layout pattern chosen and consistent throughout
- [ ] ONE signature hero animation selected and implemented
- [ ] At least ONE ContentCore 3D element embedded (WEBM, transparent bg, correct blend mode)
- [ ] 3D material style matches business type
- [ ] Animations sourced or inspired by 21st.dev component library
- [ ] Anti-pattern list checked — none present
- [ ] Mobile responsive with correct spacing scale (8px grid)
- [ ] No generic AI aesthetics — the design should look handcrafted for this specific business
