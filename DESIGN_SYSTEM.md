# Design System & Color Reference

## Teal Color Palette (#0d9488)

### Primary Colors
```
Primary Teal:        #0d9488 (Main brand)
Primary Dark:        #0f766e (Hover, pressed states)
Primary Light:       #14b8a6 (Accents, highlights)
Primary Lighter:     #5eead4 (Text on dark, badges)
```

### Neutral Colors
```
Background:          #0f172a (Dark navy-blue)
Surface:             #1e293b (Cards, containers)
Border:              #334155 (Dividers)
Disabled:            #64748b (Disabled states)
```

### Text Colors
```
Text Primary:        #f8fafc (Main text, white)
Text Secondary:      #94a3b8 (Secondary, gray)
Text Muted:          #64748b (Subtle text)
```

### Status Colors
```
Success:             #10b981 (Green)
Warning:             #f59e0b (Amber)
Error:               #ef4444 (Red)
Info:                #3b82f6 (Blue)
```

## Typography

### Headings
- **H1**: 48-56px, Bold, Teal (#0d9488)
- **H2**: 36-42px, Bold, Text Primary
- **H3**: 24-28px, Semibold, Text Primary
- **H4**: 18-20px, Semibold, Text Primary

### Body
- **Large**: 18px, Regular, Text Primary (CTAs)
- **Default**: 16px, Regular, Text Primary
- **Small**: 14px, Regular, Text Secondary
- **XSmall**: 12px, Regular, Text Muted

### Font Family
```
Primary: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif
Mono: 'Courier New', monospace
```

## Spacing Scale
```
xs:  4px
sm:  8px
md:  16px
lg:  24px
xl:  32px
2xl: 48px
3xl: 64px
```

## Border Radius
```
xs:   2px
sm:   4px
md:   8px
lg:   12px
xl:   16px
2xl:  20px
full: 9999px
```

## Shadows
```
sm:   0 1px 2px 0 rgb(0 0 0 / 0.05)
md:   0 4px 6px -1px rgb(0 0 0 / 0.1)
lg:   0 10px 15px -3px rgb(0 0 0 / 0.1)
xl:   0 20px 25px -5px rgb(0 0 0 / 0.1)
2xl:  0 25px 50px -12px rgb(0 0 0 / 0.25)
neon: 0 0 20px rgba(13, 148, 136, 0.5)
```

## Breakpoints
```
xs:   0px
sm:   640px
md:   768px
lg:   1024px
xl:   1280px
2xl:  1536px
```

## Button Styles

### Primary Button
- Background: Teal (#0d9488)
- Text: White
- Hover: Dark Teal (#0f766e)
- Padding: 12px 24px
- Border Radius: 8px
- Animation: Magnetic pull + neon glow

### Secondary Button
- Background: Transparent
- Border: 2px Teal (#0d9488)
- Text: Teal (#0d9488)
- Hover: Background light teal, darker text
- Padding: 12px 24px
- Animation: Border draw + color shift

### Ghost Button
- Background: Transparent
- Text: Teal (#0d9488)
- Hover: Text darker, underline expand
- Animation: Underline expand

## Input Styles
- Border: 1px #334155
- Focus: Border #0d9488, box-shadow neon glow
- Placeholder: #94a3b8
- Padding: 12px 16px
- Border Radius: 8px
- Background: #1e293b (dark surface)

## Card Styles
- Background: #1e293b (surface)
- Border: 1px #334155
- Border Radius: 12px
- Padding: 24px
- Hover: Neon glow, lift shadow
- Animation: 3D tilt, spotlight shine

## Navigation Bar
- Background: Glass effect (rgba(30, 41, 59, 0.7) + blur)
- Height: 64-80px
- Sticky: Yes
- z-index: 40
- Animation: Slide down on load, color transition on scroll

## Hero Section
- Background: Dark gradient (#0f172a to #1e293b)
- Min Height: 80-100vh
- Padding: 60px 20px
- Animation: Gradient mesh, particles, fade in text

## Icon Usage
- No emoji - use Lucide React icons or text
- Size: 24px default, 32px large, 16px small
- Color: Match text color or Teal primary
- Animation: Bounce, rotate, fade

## Component Rules
1. Never use purple/violet (removed from palette)
2. Always use teal (#0d9488) for primary actions
3. Use spotlight effect on cards on hover
4. Include scroll progress bar on all pages
5. Implement scroll-triggered animations
6. Use counter animations for statistics
7. Add magnetic button effect to CTAs
8. Include form focus animations
9. Use staggered animations for lists
10. Respect prefers-reduced-motion

## Dark Mode Only
- This design is dark mode optimized
- No light mode variant
- High contrast for accessibility
- Minimum WCAG AA compliance

## Animation Guidelines
1. **Duration**: 300ms for standard, 600ms for complex
2. **Easing**: ease-out for entrance, ease-in for exit
3. **Stagger**: 100ms between items
4. **Spring**: stiffness 100-150, damping 25-30
5. **Scale**: 0.9 to 1.0 for entrance
6. **Opacity**: 0 to 1 for entrance
7. **Translate**: 20px offset for slide animations
8. **Reduced Motion**: Disable animations if preferred

## Accessibility
- Minimum contrast ratio: 4.5:1
- Focus indicators: Always visible
- Keyboard navigation: All interactive elements
- Screen readers: Proper semantic HTML
- Motion: Respect prefers-reduced-motion
- Color: Don't rely on color alone for meaning
