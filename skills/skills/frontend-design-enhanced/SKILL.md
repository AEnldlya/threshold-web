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

Load syntax:
```css
@import url('https://api.fontshare.com/v2/css?f[]=satoshi@700,400&display=swap');
```

### Font Catalog

**Sans-Serif:**
- Satoshi — geometric grotesque, best for SaaS, tech
- General Sans — neutral humanist, best for food, e-commerce
- Cabinet Grotesk — softened terminals, best for portfolios
- Switzer — clean neo-grotesk, best for agencies
- Epilogue — versatile, best for body text
- Plein — humanist, best for education
- Chillax — rounded, best for wellness
- Supreme — bold, best for gaming

**Display:**
- Clash Display — ultra-wide, best for tech, gaming
- Boska — elegant serif, best for luxury
- Melodrama — editorial, best for fashion
- Tanker — heavy slab, best for agencies
- Author — humanist, best for food

**Serif:**
- Fraunces — soft optical, best for finance
- Sentient — elegant transitional, best for luxury
- Zodiak — high-contrast, best for magazines
- Syne Serif — geometric, best for wellness
- Rowan — warm, best for restaurants

### Pairing Rules
- Always pair ONE display + ONE body font
- Display: headings (h1, h2), hero text only
- Body: nav, paragraphs, labels, buttons
- NEVER use: Inter, Roboto, Arial, system-ui, Space Grotesk

## Color System

Always use CSS custom properties:
```css
:root {
  --color-base: #0A0A0F;
  --color-accent: #00E5FF;
  --color-text: #FFFFFF;
  --color-surface: #1A1A1F;
}
```

Rules:
- Dominant base + ONE sharp accent
- Vary between light/dark themes per build
- NEVER use default Tailwind blue (#3B82F6)

### Palettes by Tone
- Tech/SaaS: #0A0A0F base, #00E5FF or #39FF14 accent
- Luxury: #FAF7F2 base, #1A1208 text, #C9A84C gold accent
- Agency: #0D0D0D base, #FF3B00 or #E8FF00 accent
- Food: #FDF6EE base, #2C1810 text, #D4824A accent
- Finance: #0F1923 base, #E8D5A3 gold accent
- Wellness: #F5F0EB base, #3D6B4F green accent
- Gaming: #060608 base, #00FF88 or #FF00FF neon accent

## Layout Rules

Default: Asymmetry. Overlap. Diagonal flow. Grid-breaking elements.

### Layout Patterns
- 12-column CSS Grid (SaaS, finance)
- Bento box / card grid (tech, portfolios)
- Editorial magazine-style (luxury, fashion)
- Brutalist — raw, misaligned (agencies)
- Centered narrow column (blogs, education)
- Full-bleed alternating sections (e-commerce)
- Overlapping z-index layers (high-impact portfolios)

### Spacing
- Multiples of 8px
- Section padding: 80px desktop, 48px mobile
- Grid: max-width 1280px, gutters 24px desktop / 16px mobile

## Animation System (21st.dev)

Source: 21st.dev — 426+ animated React components

### Animation Picker by Tone
- Brutalist/bold → glitch, snap cuts, 0.15–0.25s
- Luxury/editorial → slow silk reveals, 0.8–1.4s
- Playful → spring physics, elastic bounce
- Data/SaaS → counters, skeleton shimmer, fade-up

### Key Components
**Text:** Typewriter, scramble decode, word stagger, kinetic swap, marquee, counter increment
**Heroes:** Full-viewport animated, split-layout, shader background, 3D perspective
**Shaders:** Noise gradient, aurora, liquid blob, bokeh, scanline
**Backgrounds:** Gradient mesh, particle field, noise grain, geometric pattern
**Scroll:** Horizontal gallery, parallax, progress indicator, sticky panels
**Buttons:** Fill sweep, magnetic cursor, elastic stretch, glow bloom, border trace
**Cards:** 3D tilt, clip-path reveal, glassmorphism, bento tile

### Libraries
- CSS only — keyframes, @property, clip-path
- Motion (Framer Motion) — React, spring physics
- GSAP + ScrollTrigger — complex timelines
- Three.js / GLSL — WebGL shaders

## 3D Elements (ContentCore.xyz)

EVERY website must include at least ONE 3D element.

### Usage
- Hero → Rotating device mockup (WEBM, transparent bg)
- Features → Floating 3D icon per card
- About → 3D logotype
- Product → Multi-angle 3D render
- Background → Abstract 3D geometry

### Embed
```html
<video autoplay loop muted playsinline style="mix-blend-mode: screen;">
  <source src="asset.webm" type="video/webm">
</video>
```

### Material Rules
- Tech: glass, cool blue/cyan lighting
- Luxury: gold/chrome, warm studio lighting
- Agency: matte bold, dramatic shadows
- Wellness: soft clay, warm ambient
- Gaming: emissive neon, particle trails

## Component Patterns

### Navigation
- Tech: sticky blur backdrop, pill CTA
- Luxury: minimal, text-only, no background
- Agency: floating pill or sidebar
- E-commerce: sticky with cart + search

### Cards
- Tech: flat + border or glassmorphism
- Luxury: no border, white space, thin rules
- Agency: overlapping, broken grid
- E-commerce: image-forward, hover zoom

### Buttons
- Tech: sharp rectangle, ghost secondary
- Luxury: pill, no fill, border only
- Agency: full-width bold slab, fill sweep
- E-commerce: pill, high contrast, fill sweep

### Heroes
- Full-viewport height on desktop
- Headline (display font), subhead (body), CTA, 3D element
- Background: shader, gradient mesh, or solid + 3D WEBM

## Anti-Patterns (NEVER)

### Typography
- Inter, Roboto, Arial, system-ui, Space Grotesk
- More than 2 font families
- Display font at body size

### Color
- Purple gradient on white
- Default Tailwind blue #3B82F6
- Even color distribution
- More than 2 accent colors

### Layout
- Centered hero with gradient blob + floating cards
- Three-column feature grid (icon + heading + paragraph)
- Rounded corners 5–12px (use 0–4px or full pill)
- Stock photo placeholders

### Animation
- Animation on every element
- Infinite looping (except marquees)
- Scroll-jacking
- Purple/blue gradient button with shine

### Components
- Auto-playing carousel
- Cookie banner as modal
- Hero video + dark overlay + centered white text
- Footer with 4 equal columns

## Execution Checklist

Before finalizing, verify:
- [ ] Business type identified and deduction table applied
- [ ] Fontshare fonts loaded — correct pair for business
- [ ] Font comment added justifying choice
- [ ] Color system uses CSS variables, dominant + accent
- [ ] Layout pattern chosen and consistent
- [ ] ONE signature hero animation implemented
- [ ] At least ONE ContentCore 3D element embedded
- [ ] 3D material style matches business type
- [ ] Animations sourced from 21st.dev
- [ ] Anti-pattern list checked — none present
- [ ] Mobile responsive, 8px spacing grid
- [ ] Design looks handcrafted for this specific business
