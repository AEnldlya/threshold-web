# WebMaker AI - 70 Animation Library Reference

## Animation Implementation Guide

### 1. SCROLL PROGRESS BAR
```tsx
<motion.div
  className="fixed top-0 h-1 bg-[#0d9488]"
  style={{ scaleX: scrollProgress }}
/>
```
**Use**: Top of every page to show scroll position
**Duration**: Real-time with scroll
**Tech**: Framer Motion useScroll hook

### 2. MAGNETIC BUTTON
```tsx
const handleMouseMove = (e) => {
  const x = (e.clientX - center.x) * 0.2;
  const y = (e.clientY - center.y) * 0.2;
  setPosition({ x, y });
};
```
**Use**: CTA buttons, navigation
**Duration**: Spring animation (150ms)
**Tech**: useRef, useState, spring physics

### 3. SPOTLIGHT CARD
```tsx
<motion.div
  className="absolute radial-gradient"
  style={{ left: mouseX, top: mouseY }}
  animate={{ opacity: isHovered ? 1 : 0 }}
/>
```
**Use**: Service cards, portfolio items
**Duration**: 300ms fade
**Tech**: Mouse tracking with radial-gradient

### 4. 3D TILT CARD
```tsx
animate={{
  rotateX: tilt.x,
  rotateY: tilt.y,
  transformStyle: 'preserve-3d'
}}
```
**Use**: Statistics cards, team members
**Duration**: Spring transition
**Tech**: CSS 3D transforms

### 5. COUNTER ANIMATION
```tsx
useEffect(() => {
  let start = 0;
  const increment = end / (duration * 1000);
  const timer = setInterval(() => {
    start += increment;
    if (start >= end) setCount(end);
  }, 10);
}, [isInView]);
```
**Use**: Statistics section
**Duration**: 2-3 seconds
**Tech**: requestAnimationFrame

### 6. NEON GLOW
```css
box-shadow: 0 0 10px #0d9488,
            0 0 20px #0d9488,
            0 0 30px #0d9488;
transition: box-shadow 0.3s;
```
**Use**: Cards, buttons, inputs on focus
**Duration**: 300ms
**Tech**: CSS box-shadow

### 7. BORDER DRAW
```css
.border-draw::before {
  clip-path: polygon(0 0, 0 0, 0 0, 0 0);
  transition: clip-path 0.6s ease-out;
}
.border-draw:hover::before {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}
```
**Use**: Card borders, form inputs
**Duration**: 600ms
**Tech**: CSS clip-path animation

### 8. FADE IN
```tsx
initial={{ opacity: 0 }}
animate={{ opacity: 1 }}
transition={{ duration: 0.5 }}
```
**Use**: Page elements on load
**Duration**: 500ms
**Tech**: Framer Motion

### 9. SLIDE UP
```tsx
initial={{ opacity: 0, y: 20 }}
animate={{ opacity: 1, y: 0 }}
transition={{ duration: 0.5 }}
```
**Use**: Text, headings, content
**Duration**: 500ms
**Tech**: Framer Motion

### 10. SCALE IN
```tsx
initial={{ opacity: 0, scale: 0.9 }}
animate={{ opacity: 1, scale: 1 }}
transition={{ duration: 0.3 }}
```
**Use**: Buttons, badges, icons
**Duration**: 300ms
**Tech**: Framer Motion

### 11. STAGGERED LIST
```tsx
container: {
  staggerChildren: 0.1,
  delayChildren: 0.3,
}
```
**Use**: Multiple items appearing in sequence
**Duration**: 100ms between items
**Tech**: Framer Motion variants

### 12. TYPE WRITER
```tsx
const letters = text.split('');
<motion.span>
  {letters.map((letter, i) => (
    <motion.span key={i}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: i * 0.05 }}
    >{letter}</motion.span>
  ))}
</motion.span>
```
**Use**: Headlines, brand name
**Duration**: Letter duration * count
**Tech**: Framer Motion with delay

### 13. ICON BOUNCE
```tsx
animate={{
  y: [0, -10, 0],
}}
transition={{
  duration: 0.6,
  repeat: Infinity,
}}
```
**Use**: Navigation icons, action icons
**Duration**: 600ms loop
**Tech**: Framer Motion

### 14. RIPPLE EFFECT
```tsx
<motion.div
  className="absolute rounded-full bg-[rgba(13,148,136,0.3)]"
  initial={{ scale: 0, opacity: 1 }}
  animate={{ scale: 4, opacity: 0 }}
  transition={{ duration: 0.6 }}
/>
```
**Use**: Button clicks, interactions
**Duration**: 600ms
**Tech**: Framer Motion

### 15. BUTTON FILL
```css
background: linear-gradient(90deg, #0d9488 0%, #0d9488 0%, white 0%, white 100%);
background-size: 200% 100%;
transition: background-position 0.3s;
```
**Use**: CTA buttons
**Duration**: 300ms
**Tech**: CSS gradient animation

### 16. PARALLAX
```tsx
const y = useTransform(scrollYProgress, [0, 1], [0, -50]);
<motion.div style={{ y }}>
```
**Use**: Hero section, background elements
**Duration**: Real-time with scroll
**Tech**: Framer Motion useTransform

### 17. TOAST NOTIFICATION
```tsx
initial={{ opacity: 0, y: -20 }}
animate={{ opacity: 1, y: 0 }}
exit={{ opacity: 0, y: -20 }}
transition={{ duration: 0.3 }}
```
**Use**: Success/error messages
**Duration**: 300ms in/out
**Tech**: Framer Motion + AnimatePresence

### 18. FORM FOCUS
```tsx
className="focus:shadow-[0_0_20px_rgba(13,148,136,0.5)]"
```
**Use**: All form inputs
**Duration**: 200ms
**Tech**: Tailwind focus state

### 19. MODAL OPEN
```tsx
initial={{ opacity: 0, scale: 0.9 }}
animate={{ opacity: 1, scale: 1 }}
exit={{ opacity: 0, scale: 0.9 }}
transition={{ duration: 0.3 }}
```
**Use**: Forms, modals, overlays
**Duration**: 300ms
**Tech**: Framer Motion + AnimatePresence

### 20. ACCORDION EXPAND
```tsx
initial={{ height: 0, opacity: 0 }}
animate={{ height: 'auto', opacity: 1 }}
exit={{ height: 0, opacity: 0 }}
transition={{ duration: 0.3 }}
```
**Use**: FAQ, collapsible sections
**Duration**: 300ms
**Tech**: Framer Motion

## Animation Performance Tips

1. **Use will-change CSS property** for frequently animated elements
2. **Debounce mouse tracking** to reduce re-renders
3. **Use transform and opacity** for smooth animations (GPU accelerated)
4. **Implement Intersection Observer** for scroll animations
5. **Lazy load animations** that aren't visible
6. **Use CSS animations** for simple, continuous effects
7. **Throttle scroll events** for better performance
8. **Test on mobile devices** for animation smoothness
9. **Implement prefers-reduced-motion** for accessibility
10. **Monitor bundle size** - animations add ~15-20KB

## Browser Support
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari 14+, Chrome Android)

## Testing Animations
- Use React DevTools Profiler
- Test on low-end devices
- Verify accessibility (prefers-reduced-motion)
- Check animation performance with DevTools
- Test keyboard navigation
- Verify form interactions work
