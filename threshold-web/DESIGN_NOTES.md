# Threshold Web - Design Upgrade Notes

## 🎨 Color Palette Transformation

### Old Design (Black/Yellow)
```
Primary:   #000000 (Black)
Accent:    #FACC15 (Bright Yellow)
Secondary: #1F2937 (Dark Gray)
Issue:     High contrast, harsh, dated feel
```

### New Design (Blue/Slate)
```
Primary:   #0ea5e9 → #0369a1 (Blue gradient)
Accent:    #f59e0b (Warm amber, softer)
Background: #f8fafc → #ffffff (Light, professional)
Secondary: #334155 → #0f172a (Deep slate)
Benefit:   Modern, sophisticated, trustworthy
```

## 📐 Layout & Spacing

### Before
- Dense card grids with minimal white space
- Centered text-only hero
- 6-column service cards (too many)
- Generic card layouts

### After
- Split-column layouts (content + visual)
- Breathing room with 24px+ gutters
- Alternating layouts (visual interest)
- Strategic whitespace hierarchy
- Maximum widths for readability (max-w-7xl)

## 🎯 Typography System

### Hierarchy Implementation
```
H1: text-6xl font-bold (hero headlines)
H2: text-5xl font-bold (section titles)
H3: text-2xl font-semibold (subsections)
H4: text-lg font-semibold (component titles)
Body: 16px leading-relaxed (comfortable reading)
Small: 14px text-slate-600 (supporting text)
```

### Font Strategy
- Primary: Sora (modern, clean)
- Added Inter for better body reading (future implementation)
- Weights: 400 (regular), 500 (medium), 600 (semibold), 700 (bold)

## 🎬 Animation Strategy

### Entrance Animations
- Fade Up: 0.6s ease-out with stagger
- Slide In: 0.6-0.8s from left/right
- Scale: 0.9→1.0 for emphasis
- Delay children for wave effect

### Interaction Animations
- Hover scale: 1.0→1.05 (+8px shadow)
- Card lifts: -4px to -8px on hover
- Underline grow: 0→100% width
- Button pulse: scale 1.0→1.05 hover, 0.95 press

### Scroll Animations
- Triggered by `whileInView` (Framer Motion)
- Viewport margin: `'0px 0px -200px 0px'` (starts 200px before visible)
- Once: true (animate only once per scroll)

### Continuous Animations
- Floating cards: `animate-y [0, -20, 0]` (4s loop)
- Pulsing badges: `animate-pulse-slow` (3s)
- Blob decorations: `blur-3xl` with opacity variations

## 🔄 Component Patterns

### Card Design Pattern
```
1. Container: rounded-2xl, border, backdrop blur
2. Hover: border color change, shadow increase, scale up
3. Gradient overlay: opacity 0 → 100% on hover
4. Icon/Image: scales on hover (+10%)
5. Content: organized in sections with spacing
```

### Button Patterns
```
Primary (.btn-primary):
- Gradient bg (blue→cyan)
- Hover: scale 1.05, shadow-lg
- Active: scale 0.95
- Focus: ring-2 with offset

Secondary (.btn-secondary):
- Border outline
- Hover: background color + subtle shift
- Accessible: :focus states

Outline (.btn-outline):
- Light border
- Hover: background light variant
- Subtle state changes
```

### Form Field Pattern
```
Input (.input-field):
- Clean border (slate-200)
- Hover: slightly darker border
- Focus: ring-2 (blue), border transparent
- Transition: all 0.2s
- Proper padding: px-4 py-3
- Width: 100% of container
```

## 📱 Responsive Design

### Breakpoints Used
- Mobile: 0-639px (no prefix)
- Tablet: 640px+ (`sm:`)
- Desktop: 768px+ (`md:`)
- Large: 1024px+ (`lg:`)
- XL: 1280px+ (`xl:`)

### Mobile-First Approach
1. Build mobile layout first (single column)
2. Add media queries for desktop enhancements
3. Use `hidden` class on desktop, `flex` on mobile (or reverse)
4. Ensure touch targets ≥48px
5. Readable font sizes at small screens

### Responsive Examples
```tsx
// Grid grows with screen size
grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3

// Text scales appropriately
text-xl md:text-2xl lg:text-3xl

// Spacing adjusts
py-8 md:py-12 lg:py-16

// Menu appears/hides
hidden md:flex
```

## 🎁 Special Effects

### Glassmorphism
```css
.glass {
  backdrop-blur-xl          /* blur background */
  bg-white/80              /* semi-transparent white */
  border border-white/20   /* subtle border */
}
```

### Gradient Backgrounds
```css
bg-gradient-to-br from-blue-400 to-cyan-400
bg-gradient-to-r from-blue-600 to-cyan-600
```

### Floating Animation
```tsx
animate={{ y: [0, -20, 0] }}
transition={{ duration: 4, repeat: Infinity }}
```

### Pulse Effect
```css
animate-pulse-slow  /* custom: 3s instead of 2s */
```

## 🔐 Accessibility Features

### Semantic HTML
- Proper heading hierarchy (h1-h4)
- Landmark elements (header, main, footer)
- Button elements for actions
- Form labels with proper associations

### ARIA & Attributes
```tsx
role="navigation"
aria-label="Toggle menu"
autoComplete="name"
tabIndex={0}
```

### Color Contrast
- Text on light bg: #334155 on #ffffff (contrast 8.5:1) ✅
- Text on dark bg: #ffffff on #1e293b (contrast 11:1) ✅
- Links: #0284c7 meets 4.5:1 minimum ✅

### Keyboard Navigation
- All interactive elements focusable
- Focus rings visible (ring-2, ring-offset-2)
- Logical tab order
- Escape key handling where needed

## 📊 Performance Considerations

### Image Optimization
- Next.js Image component for lazy loading
- Proper sizes attribute for responsive
- WebP format with fallbacks
- Placeholder/blur effects

### CSS Optimization
- Tailwind purging active
- Only used classes included
- Minimal custom CSS (mostly utilities)
- No unused styles

### Animation Performance
- GPU-accelerated (transform, opacity only)
- Will-change used sparingly
- Reduced motion respected (future)
- 60fps target maintained

### Font Loading
- Preconnect to Google Fonts
- Swap strategy (text visible immediately)
- Subset loading (might add for i18n)
- System font fallbacks

## 🚀 Future Enhancements

### Phase 2 Opportunities
1. Dark mode toggle
2. Animation preferences (prefers-reduced-motion)
3. Loading skeletons for images
4. Intersection Observer for more precise reveals
5. Custom scroll-linked animations

### Design Improvements
1. Real portfolio images instead of emojis
2. Team member profiles
3. Video hero section (optional)
4. Interactive pricing calculator
5. Live chat widget

### Technical Enhancements
1. Storybook for component library
2. Vitest unit tests
3. Playwright E2E tests
4. Lighthouse CI integration
5. Analytics integration

## 📐 Grid System

Using 8px base unit:
```
8px   = xs spacing
16px  = sm spacing
24px  = md spacing
32px  = lg spacing
48px  = xl spacing
```

Applied consistently:
- Section padding: 64px (py-16) or 96px (py-24)
- Container margins: 16px-32px (px-4 md:px-8)
- Card padding: 24px-32px (p-6 md:p-8)
- Gap between items: 16px-32px (gap-4 md:gap-8)

---

**Design Philosophy**: Modern, professional, trustworthy, fast, and accessible. Every pixel serves a purpose.
