# Design References from Instagram Monitoring

**Purpose**: Track design inspiration, animations, and UI/UX patterns from Instagram to improve website builds

**Last Updated**: 2026-03-14 20:50

---

## Design Patterns to Implement

### Animations & Micro-interactions
- [ ] Fade-in transitions (entrance animations)
- [ ] Hover effects (interactive feedback)
- [ ] Scroll-triggered animations
- [ ] Loading states and spinners
- [ ] Button feedback animations

### Color Schemes & Typography
- [ ] Modern minimalist palettes
- [ ] Bold gradient combinations
- [ ] Serif/sans-serif pairings
- [ ] Hierarchy and readability

### Layout Patterns
- [ ] Hero section designs
- [ ] Card-based layouts
- [ ] Grid variations
- [ ] Asymmetrical layouts
- [ ] Mobile-first responsiveness

### UX Best Practices
- [ ] Form design patterns
- [ ] CTA button styles
- [ ] Navigation patterns
- [ ] Accessibility considerations

---

## Monitored Accounts

### 1. design_inspiration
**URL**: https://www.instagram.com/design_inspiration/
**Frequency**: Daily
**Focus**: UI/UX design patterns and animations
**Last Checked**: Not yet

### 2. webdesign_trends
**URL**: https://www.instagram.com/webdesign_trends/
**Frequency**: Daily
**Focus**: Web design trends and best practices
**Last Checked**: Not yet

### 3. framer_official
**URL**: https://www.instagram.com/framer/
**Frequency**: Daily
**Focus**: Framer animation library examples
**Last Checked**: Not yet

---

## Found Inspiration (To Be Updated)

### [Date] - [Account]
- **What**: [Description of reel/post]
- **Why Relevant**: [How it applies to website builds]
- **Implementation Notes**: [Code/technique to use]
- **Link**: [Instagram URL if available]

---

## Implementation Log

Track which designs have been integrated into actual projects:

| Date | Inspiration | Project | Implementation | Status |
|------|-------------|---------|-----------------|--------|
| - | - | - | - | Pending |

---

## Notes

- Check daily for new design trends
- Save screenshots of good patterns
- Document the technique/code for implementation
- Apply learnings to next website builds (Samantha's projects)

---

_This file is updated automatically as new Instagram content is discovered._

### 2026-03-14 - design_inspiration - Fade-in Animation

**What I Found**:
Beautiful fade-in animation on hero section with staggered text reveal

**Why It's Relevant**:
This reel demonstrates professional animation techniques that improve user engagement and visual appeal. Perfect for hero sections and landing pages.

**Implementation Notes**:

**Animations**: fade-in, slide-up, staggered reveal

**Code Example** (Framer Motion):
```jsx
<motion.h1
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.8 }}
>
  Welcome to Your Site
</motion.h1>
```

**Colors**: #1a1a1a (dark), #ffffff (white), #3b82f6 (blue)

**Techniques**: CSS animations, Framer Motion, CSS transform

**UI Elements**: Hero headline, Subtext, CTA button

**Interactions**: Smooth fade, Entrance animation, Text stagger

**Link**:
https://www.instagram.com/reel/DUHmsKkjZw0/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Glassmorphism Effect

**What I Found**:
Modern glassmorphism effect with gradient overlay and backdrop blur

**Why It's Relevant**:
Glassmorphism is a trendy modern design pattern that creates depth and sophistication. Great for cards, modals, and accent elements.

**Implementation Notes**:

**Animations**: opacity transition, gradient shift, backdrop blur

**Code Example** (Tailwind CSS):
```html
<div class="backdrop-blur-lg bg-white/30 border border-white/20 rounded-xl p-6">
  <!-- Content -->
</div>
```

**Or with CSS**:
```css
.glass-effect {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}
```

**Colors**: #ffffff (white), #f3f4f6 (light), #e5e7eb (lighter), #6b7280 (gray)

**Techniques**: CSS backdrop-filter, gradient, glass effect, blur

**UI Elements**: Glass card, Gradient background, Text overlay

**Interactions**: Smooth transitions, Hover effects, Blur effects

**Link**:
https://www.instagram.com/reel/DUplhdqAbNt/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - Micro-interactions

**What I Found**:
Smooth micro-interactions with subtle animations and hover effects

**Why It's Relevant**:
Micro-interactions improve perceived performance and user satisfaction. These small animations make interfaces feel responsive and polished.

**Implementation Notes**:

**Animations**: Subtle scale, opacity, color transitions

**Code Example** (Framer Motion):
```jsx
<motion.button
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  transition={{ type: "spring", stiffness: 400 }}
>
  Click Me
</motion.button>
```

**Or with CSS**:
```css
button {
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

button:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
```

**Colors**: Brand-specific (adapt to your palette)

**Techniques**: Spring animations, easing functions, transform scale

**UI Elements**: Buttons, links, cards, form inputs

**Interactions**: Hover scale, tap feedback, smooth transitions, visual feedback

**Link**:
https://www.instagram.com/reel/DVmBuLMjsoL/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - Gradient Animations

**What I Found**:
Smooth gradient color transitions with animated background shifts

**Why It's Relevant**:
Gradient animations create visual depth and modern sophistication. Great for hero sections, backgrounds, and premium design elements.

**Implementation Notes**:

**Animations**: Gradient shift, color transition, smooth flow

**Code Example** (Framer Motion + Tailwind):
```jsx
<motion.div
  animate={{
    backgroundPosition: ['0% 0%', '100% 100%', '0% 0%']
  }}
  transition={{ duration: 5, repeat: Infinity }}
  className="bg-gradient-to-r from-purple-500 via-pink-500 to-blue-500 bg-[length:200%_200%]"
>
  {/* Content */}
</motion.div>
```

**Or with CSS**:
```css
.gradient-animated {
  background: linear-gradient(
    45deg,
    #667eea 0%,
    #764ba2 25%,
    #f093fb 50%,
    #4facfe 75%,
    #00f2fe 100%
  );
  background-size: 200% 200%;
  animation: gradientShift 5s ease infinite;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

**Colors**: Gradient palette - purple, pink, blue, cyan

**Techniques**: CSS animation, gradient positioning, color transitions

**UI Elements**: Hero background, accent elements, section dividers

**Interactions**: Auto-animated, no user interaction required, continuous loop

**Link**:
https://www.instagram.com/reel/DVVnWgikb71/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - 21st.dev - Mouse-Following Spotlight Card Effect

**What I Found**:
Interactive card effect where a radial gradient spotlight follows the mouse cursor position, creating a dynamic glow/highlight effect on hover. The spotlight reveals a subtle gradient border that tracks cursor movement within the card boundaries.

**Why It's Relevant**:
This effect adds a premium, interactive feel to cards and makes websites feel alive and responsive. It's perfect for pricing cards, feature highlights, portfolio items, or any clickable card element. Creates a "wow" factor without hurting performance.

**Implementation Notes**:

**Animations**: Mouse-tracking spotlight, gradient reveal, smooth position updates

**Code Example** (React + Framer Motion):
```jsx
import { useState, useRef } from 'react';
import { motion } from 'framer-motion';

function SpotlightCard({ children, className = '' }) {
  const cardRef = useRef(null);
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
  const [isHovering, setIsHovering] = useState(false);

  const handleMouseMove = (e) => {
    if (!cardRef.current) return;
    const rect = cardRef.current.getBoundingClientRect();
    setMousePosition({
      x: e.clientX - rect.left,
      y: e.clientY - rect.top
    });
  };

  return (
    <motion.div
      ref={cardRef}
      className={`relative overflow-hidden rounded-2xl bg-gray-900 ${className}`}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setIsHovering(true)}
      onMouseLeave={() => setIsHovering(false)}
    >
      {/* Spotlight gradient layer */}
      <motion.div
        className="pointer-events-none absolute -inset-px opacity-0 transition-opacity duration-300"
        animate={{
          opacity: isHovering ? 1 : 0,
          background: `radial-gradient(600px circle at ${mousePosition.x}px ${mousePosition.y}px, rgba(255,255,255,0.1), transparent 40%)`
        }}
      />
      
      {/* Border gradient */}
      <motion.div
        className="pointer-events-none absolute -inset-px rounded-2xl opacity-0 transition-opacity duration-300"
        animate={{
          opacity: isHovering ? 1 : 0,
          background: `radial-gradient(600px circle at ${mousePosition.x}px ${mousePosition.y}px, rgba(99,102,241,0.4), transparent 40%)`
        }}
        style={{ mask: 'linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0)', maskComposite: 'exclude', padding: '1px' }}
      />
      
      {/* Content */}
      <div className="relative z-10 p-6">
        {children}
      </div>
    </motion.div>
  );
}
```

**CSS-Only Alternative**:
```css
.spotlight-card {
  position: relative;
  background: #111827;
  border-radius: 1rem;
  overflow: hidden;
}

.spotlight-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    600px circle at var(--mouse-x, 50%) var(--mouse-y, 50%),
    rgba(255, 255, 255, 0.06),
    transparent 40%
  );
  opacity: 0;
  transition: opacity 0.3s;
}

.spotlight-card:hover::before {
  opacity: 1;
}

/* JavaScript to update CSS variables */
/* document.querySelector('.spotlight-card').addEventListener('mousemove', (e) => {
  const rect = e.currentTarget.getBoundingClientRect();
  e.currentTarget.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
  e.currentTarget.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
}); */
```

**Colors**: 
- Card background: #111827 (dark gray)
- Spotlight: rgba(255,255,255,0.1) (subtle white)
- Border glow: rgba(99,102,241,0.4) (indigo tint)

**Techniques**: 
- CSS custom properties (--mouse-x, --mouse-y)
- Radial gradient with dynamic positioning
- Framer Motion animate prop for smooth updates
- mask/clip for border-only gradient effect

**UI Elements**: 
- Pricing cards
- Feature cards  
- Portfolio items
- Testimonial cards
- CTA cards

**Interactions**: 
- Mouse move tracking
- Gradient position updates
- Smooth opacity transitions
- Border glow reveal

**Link**:
https://21st.dev/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_inspiration - Scroll-Triggered Parallax Effect

**What I Found**:
Smooth parallax scrolling effect where background elements move at different speeds than foreground content, creating depth and visual interest

**Why It's Relevant**:
Parallax effects add sophistication and depth to websites without being overwhelming. Perfect for hero sections and storytelling layouts. Creates an immersive experience that keeps users engaged.

**Implementation Notes**:

**Animations**: Parallax scroll, layer depth, smooth transform

**Code Example** (Framer Motion + scroll):
```jsx
import { useScroll, useTransform, motion } from 'framer-motion';

function ParallaxSection() {
  const { scrollYProgress } = useScroll();
  const y = useTransform(scrollYProgress, [0, 1], [0, -100]);
  
  return (
    <motion.div style={{ y }} className="parallax-bg">
      <img src="/background.jpg" alt="" />
    </motion.div>
  );
}
```

**CSS Alternative**:
```css
.parallax-container {
  perspective: 1px;
  overflow-x: hidden;
  overflow-y: auto;
}

.parallax-layer {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.parallax-back {
  transform: translateZ(-1px) scale(2);
}
```

**Colors**: Any brand palette (works with all colors)

**Techniques**: CSS transform, Framer Motion useScroll, useTransform hook

**UI Elements**: Hero backgrounds, section dividers, image galleries

**Interactions**: Scroll-based movement, depth perception, layered content

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Bento Grid Layout

**What I Found**:
Modular bento box-style grid layout with varying card sizes creating visual hierarchy and organized content presentation

**Why It's Relevant**:
Bento grids are trending heavily in 2025. They create visual interest while maintaining organization. Perfect for feature showcases, portfolios, and service listings. The modular approach makes content scannable and engaging.

**Implementation Notes**:

**Animations**: Card hover effects, staggered entrance, smooth transitions

**Code Example** (Tailwind CSS + Grid):
```jsx
<div className="grid grid-cols-4 gap-4 auto-rows-[200px]">
  {/* Large feature card */}
  <div className="col-span-2 row-span-2 bg-gray-100 rounded-2xl p-6 hover:scale-[1.02] transition-transform">
    <h3>Featured Service</h3>
  </div>
  
  {/* Standard cards */}
  <div className="col-span-1 row-span-1 bg-gray-100 rounded-2xl p-6">
    <h3>Service 1</h3>
  </div>
  <div className="col-span-1 row-span-1 bg-gray-100 rounded-2xl p-6">
    <h3>Service 2</h3>
  </div>
  
  {/* Wide card */}
  <div className="col-span-2 row-span-1 bg-gray-100 rounded-2xl p-6">
    <h3>Wide Feature</h3>
  </div>
</div>
```

**Colors**: #f3f4f6 (light gray cards), #1f2937 (dark text), #3b82f6 (accent)

**Techniques**: CSS Grid, col-span, row-span, responsive breakpoints

**UI Elements**: Feature cards, service listings, portfolio items, stat cards

**Interactions**: Hover scale effects, click to expand, smooth transitions

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_inspiration - Morphing Shape Animations

**What I Found**:
Smooth morphing animations where shapes transform fluidly from one form to another (circle to square, blob to star)

**Why It's Relevant**:
Morphing animations create memorable brand moments and add personality to websites. They're eye-catching without being distracting. Great for loading states, transitions between sections, or accent elements.

**Implementation Notes**:

**Animations**: Shape morphing, path interpolation, smooth transitions

**Code Example** (Framer Motion + SVG):
```jsx
import { motion } from 'framer-motion';

const morphVariants = {
  circle: {
    d: "M50,50 m-40,0 a40,40 0 1,0 80,0 a40,40 0 1,0 -80,0"
  },
  square: {
    d: "M10,10 h80 v80 h-80 z"
  }
};

<motion.svg viewBox="0 0 100 100">
  <motion.path
    variants={morphVariants}
    initial="circle"
    animate="square"
    transition={{ duration: 1, ease: "easeInOut" }}
    fill="#3b82f6"
  />
</motion.svg>
```

**CSS Blob Morphing**:
```css
.blob {
  background: linear-gradient(45deg, #667eea, #764ba2);
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  animation: morph 8s ease-in-out infinite;
}

@keyframes morph {
  0%, 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
  50% { border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%; }
}
```

**Colors**: Gradient palettes work best (#667eea to #764ba2, or brand colors)

**Techniques**: SVG path morphing, CSS border-radius animation, Framer Motion

**UI Elements**: Loading states, section transitions, decorative elements, logos

**Interactions**: Auto-animated, hover triggers, scroll-triggered morphs

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Typewriter Text Reveal

**What I Found**:
Typewriter-style text animation where characters appear one by one with a blinking cursor effect

**Why It's Relevant**:
Typewriter animations add personality and draw attention to headlines or key messages. They create anticipation and make users read the text more carefully. Perfect for hero headlines, CTAs, and key value propositions.

**Implementation Notes**:

**Animations**: Character-by-character reveal, blinking cursor, typing sound (optional)

**Code Example** (Framer Motion):
```jsx
import { motion, useAnimation } from 'framer-motion';
import { useEffect } from 'react';

function TypewriterText({ text }) {
  const controls = useAnimation();
  
  useEffect(() => {
    async function animate() {
      for (let i = 0; i <= text.length; i++) {
        await controls.start({
          width: `${i}ch`,
          transition: { duration: 0.05 }
        });
      }
    }
    animate();
  }, []);
  
  return (
    <motion.span
      animate={controls}
      className="inline-block overflow-hidden whitespace-nowrap border-r-2 border-current"
      style={{ fontFamily: 'monospace' }}
    >
      {text}
    </motion.span>
  );
}
```

**CSS Only Alternative**:
```css
.typewriter {
  overflow: hidden;
  border-right: 2px solid;
  white-space: nowrap;
  animation: typing 3s steps(40, end), blink 0.75s step-end infinite;
}

@keyframes typing {
  from { width: 0; }
  to { width: 100%; }
}

@keyframes blink {
  from, to { border-color: transparent; }
  50% { border-color: currentColor; }
}
```

**Colors**: Any text color with good contrast

**Techniques**: Width animation, overflow hidden, monospace font, step timing

**UI Elements**: Hero headlines, taglines, CTAs, loading messages

**Interactions**: Auto-play on load, hover restart, scroll-triggered start

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - Staggered Grid Animation

**What I Found**:
Grid layout with staggered item entrance animations (items appear in sequence)

**Why It's Relevant**:
Staggered animations create visual interest and guide user attention through content. Perfect for portfolios, galleries, product grids, and team showcases.

**Implementation Notes**:

**Animations**: Staggered fade-in, scale entrance, cascade effect

**Code Example** (Framer Motion):
```jsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.2,
    }
  }
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
}

<motion.div variants={container} initial="hidden" animate="show">
  {items.map((item) => (
    <motion.div key={item.id} variants={item}>
      {/* Item content */}
    </motion.div>
  ))}
</motion.div>
```

**CSS Alternative**:
```css
.grid-item {
  opacity: 0;
  animation: slideIn 0.5s ease-out forwards;
}

.grid-item:nth-child(1) { animation-delay: 0s; }
.grid-item:nth-child(2) { animation-delay: 0.1s; }
.grid-item:nth-child(3) { animation-delay: 0.2s; }
/* ... etc */

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Colors**: Varies by design (use your brand palette)

**Techniques**: Stagger animation, CSS animation, Framer Motion variants

**UI Elements**: Grid items, portfolio thumbnails, product cards, gallery items

**Interactions**: Auto-animated on page load, sequential appearance, cascading effect

**Link**:
https://www.instagram.com/reel/DRYrEa5jzVh/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - Text Scramble Effect

**What I Found**:
Text that appears to scramble/decrypt as it reveals, like a hacker or decoding effect where characters cycle through random symbols before settling on the final text

**Why It's Relevant**:
Adds a tech-savvy, mysterious vibe to headlines or important text. Great for tech companies, cybersecurity, gaming sites, or any brand wanting an edgy feel. Creates curiosity and makes users pay attention.

**Implementation Notes**:

**Animations**: Character scrambling, random symbol cycling, final text reveal

**Code Example** (React):
```jsx
import { useState, useEffect } from 'react';

function ScrambleText({ text, className = '' }) {
  const [displayText, setDisplayText] = useState(text);
  const chars = '!<>-_\\/[]{}—=+*^?#________';
  
  useEffect(() => {
    let iteration = 0;
    const interval = setInterval(() => {
      setDisplayText(
        text
          .split('')
          .map((char, index) => {
            if (index < iteration) return text[index];
            return chars[Math.floor(Math.random() * chars.length)];
          })
          .join('')
      );
      
      if (iteration >= text.length) clearInterval(interval);
      iteration += 1/3;
    }, 30);
    
    return () => clearInterval(interval);
  }, [text]);
  
  return <span className={className}>{displayText}</span>;
}
```

**Colors**: #00ff00 (matrix green), #ff0080 (cyberpunk pink), or brand colors

**Techniques**: Random character generation, interval-based updates, progressive reveal

**UI Elements**: Hero headlines, loading screens, tech announcements, secret reveals

**Interactions**: Auto-play on load, hover to re-scramble, scroll-triggered

**Link**:
https://www.instagram.com/design_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_inspiration - Glitch Text Effect

**What I Found**:
Text with a digital glitch effect - RGB color separation, slight position jitter, and scan lines creating a corrupted digital look

**Why It's Relevant**:
Perfect for gaming, tech, cyberpunk, or retro-futuristic aesthetics. Adds energy and edginess to headlines. Makes text feel dynamic and alive.

**Implementation Notes**:

**Animations**: RGB split, position jitter, scan lines, flicker

**Code Example** (CSS):
```css
.glitch {
  position: relative;
  color: #fff;
  font-size: 2rem;
  font-weight: bold;
}

.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.glitch::before {
  left: 2px;
  text-shadow: -2px 0 #ff00c1;
  clip: rect(44px, 450px, 56px, 0);
  animation: glitch-anim 5s infinite linear alternate-reverse;
}

.glitch::after {
  left: -2px;
  text-shadow: -2px 0 #00fff9;
  clip: rect(44px, 450px, 56px, 0);
  animation: glitch-anim2 5s infinite linear alternate-reverse;
}

@keyframes glitch-anim {
  0% { clip: rect(30px, 9999px, 10px, 0); }
  20% { clip: rect(80px, 9999px, 90px, 0); }
  40% { clip: rect(10px, 9999px, 50px, 0); }
  60% { clip: rect(60px, 9999px, 20px, 0); }
  80% { clip: rect(40px, 9999px, 70px, 0); }
  100% { clip: rect(90px, 9999px, 30px, 0); }
}

@keyframes glitch-anim2 {
  0% { clip: rect(60px, 9999px, 80px, 0); }
  20% { clip: rect(20px, 9999px, 40px, 0); }
  40% { clip: rect(90px, 9999px, 10px, 0); }
  60% { clip: rect(30px, 9999px, 60px, 0); }
  80% { clip: rect(70px, 9999px, 20px, 0); }
  100% { clip: rect(10px, 9999px, 50px, 0); }
}
```

**Colors**: #ff00c1 (magenta), #00fff9 (cyan), white base

**Techniques**: CSS clip property, pseudo-elements, text-shadow, keyframe animation

**UI Elements**: Hero headlines, gaming titles, error messages, loading states

**Interactions**: Continuous animation, hover intensification

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Neon Glow Text Effect

**What I Found**:
Text with an animated neon sign effect - pulsing glow, flickering light, and vibrant colors mimicking real neon signage

**Why It's Relevant**:
Creates instant visual impact and draws attention to key messages. Perfect for nightlife, entertainment, retro themes, or any brand wanting bold, vibrant energy. Adds a premium, nightlife aesthetic.

**Implementation Notes**:

**Animations**: Pulsing glow, flicker effect, color cycling

**Code Example** (CSS):
```css
.neon-text {
  color: #fff;
  font-size: 3rem;
  font-weight: bold;
  text-shadow:
    0 0 5px #fff,
    0 0 10px #fff,
    0 0 20px #ff00de,
    0 0 40px #ff00de,
    0 0 80px #ff00de;
  animation: neon-pulse 1.5s ease-in-out infinite alternate;
}

@keyframes neon-pulse {
  from {
    text-shadow:
      0 0 5px #fff,
      0 0 10px #fff,
      0 0 20px #ff00de,
      0 0 40px #ff00de,
      0 0 80px #ff00de;
  }
  to {
    text-shadow:
      0 0 10px #fff,
      0 0 20px #fff,
      0 0 40px #ff00de,
      0 0 80px #ff00de,
      0 0 120px #ff00de;
  }
}

/* Optional flicker */
.neon-flicker {
  animation: flicker 3s linear infinite;
}

@keyframes flicker {
  0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
    opacity: 1;
    text-shadow: /* glow layers */;
  }
  20%, 24%, 55% {
    opacity: 0.8;
    text-shadow: none;
  }
}
```

**Colors**: #ff00de (hot pink), #00ffff (cyan), #9d00ff (purple)

**Techniques**: Multiple text-shadow layers, opacity animation, keyframes

**UI Elements**: Hero headlines, CTAs, brand names, promotional banners

**Interactions**: Continuous pulse, hover brightness increase

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_inspiration - Liquid Button Effect

**What I Found**:
Button with a fluid, liquid-like fill animation that flows and ripples when hovered or clicked

**Why It's Relevant**:
Adds organic, playful interaction to CTAs. The liquid effect feels tactile and satisfying. Makes buttons feel alive and responsive. Great for creative brands, children's sites, or any playful aesthetic.

**Implementation Notes**:

**Animations**: Liquid fill, ripple effect, organic flow

**Code Example** (CSS + SVG):
```css
.liquid-button {
  position: relative;
  padding: 16px 32px;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 50px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s;
}

.liquid-button::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  background: rgba(255,255,255,0.3);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.liquid-button:hover::before {
  width: 300px;
  height: 300px;
}

.liquid-button:hover {
  transform: scale(1.05);
}
```

**Colors**: #3b82f6 (blue), #8b5cf6 (purple), brand accent colors

**Techniques**: SVG filters (feGaussianBlur, feColorMatrix), CSS transforms, pseudo-elements

**UI Elements**: CTA buttons, submit buttons, interactive elements

**Interactions**: Hover liquid fill, click ripple, organic movement

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Skeleton Loading Shimmer

**What I Found**:
Animated placeholder content that mimics the structure of loading content with a shimmering gradient sweep across it

**Why It's Relevant**:
Improves perceived performance by giving users visual feedback that content is loading. Reduces bounce rate during load times. Modern alternative to spinners. Makes waiting feel faster.

**Implementation Notes**:

**Animations**: Shimmer sweep, gradient movement, pulsing opacity

**Code Example** (CSS):
```css
.skeleton {
  background: linear-gradient(
    90deg,
    #f0f0f0 25%,
    #e0e0e0 50%,
    #f0f0f0 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Skeleton variants */
.skeleton-text {
  height: 16px;
  margin-bottom: 8px;
}

.skeleton-text:last-child {
  width: 80%;
}

.skeleton-image {
  width: 100%;
  height: 200px;
  border-radius: 8px;
}
```

**Colors**: #f0f0f0 (base), #e0e0e0 (shimmer highlight)

**Techniques**: Linear gradient animation, background-position, background-size

**UI Elements**: Cards, lists, images, text blocks, entire page layouts

**Interactions**: Auto-plays during loading, fades out when content loads

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - 3D Card Flip Effect

**What I Found**:
Card that flips 180 degrees on hover to reveal content on the back side, creating a 3D rotation effect with perspective

**Why It's Relevant**:
Adds depth and interactivity to content cards. Perfect for team profiles (front: photo, back: bio), product cards (front: image, back: details), or feature showcases. Saves space while adding surprise.

**Implementation Notes**:

**Animations**: 3D rotation, perspective transform, backface visibility

**Code Example** (CSS):
```css
.flip-card {
  perspective: 1000px;
  width: 300px;
  height: 400px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.flip-card-front {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.flip-card-back {
  background: #1f2937;
  color: white;
  transform: rotateY(180deg);
}
```

**Colors**: Any brand colors (gradient front, solid back)

**Techniques**: CSS perspective, transform-style: preserve-3d, backface-visibility

**UI Elements**: Team cards, product cards, feature cards, portfolio items

**Interactions**: Hover to flip, can add click toggle for mobile

**Link**:
https://www.instagram.com/design_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_inspiration - Floating Levitation Animation

**What I Found**:
Elements that gently float up and down in a continuous loop, creating a weightless, levitating effect

**Why It's Relevant**:
Adds subtle life to static elements without being distracting. Perfect for hero images, icons, or decorative elements. Creates a dreamy, premium feel. Draws attention to key elements.

**Implementation Notes**:

**Animations**: Vertical float, gentle oscillation, smooth easing

**Code Example** (CSS):
```css
.float {
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

/* With rotation for more dynamic feel */
.float-rotate {
  animation: float-rotate 4s ease-in-out infinite;
}

@keyframes float-rotate {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-15px) rotate(3deg);
  }
}
```

**Colors**: Any (works with all elements)

**Techniques**: CSS keyframes, transform translateY, Framer Motion animate prop

**UI Elements**: Hero images, icons, decorative shapes, product mockups

**Interactions**: Continuous auto-play, can pause on hover

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Animated Underline Link

**What I Found**:
Links with an underline that animates in from left to right (or center out) on hover, creating a smooth reveal effect

**Why It's Relevant**:
Elevates basic links from boring to polished. Subtle but noticeable interaction that improves perceived quality. Works for navigation, text links, and CTAs. Professional feel without being flashy.

**Implementation Notes**:

**Animations**: Width expansion, scale transform, position shift

**Code Example** (CSS):
```css
/* Left to right */
.animated-link {
  position: relative;
  color: #3b82f6;
  text-decoration: none;
}

.animated-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 2px;
  background: #3b82f6;
  transition: width 0.3s ease;
}

.animated-link:hover::after {
  width: 100%;
}

/* Center out */
.animated-link-center::after {
  left: 50%;
  transform: translateX(-50%);
}

.animated-link-center:hover::after {
  width: 100%;
}
```

**Colors**: Current color (inherits from text), or brand accent

**Techniques**: Pseudo-elements, width/scale transitions, transform

**UI Elements**: Navigation links, text links, footer links, read more links

**Interactions**: Hover to reveal, hover out to hide

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - Count Up Number Animation

**What I Found**:
Numbers that animate from 0 to their final value, counting up with smooth easing - perfect for statistics and metrics

**Why It's Relevant**:
Makes statistics feel dynamic and impressive. Draws attention to key metrics. Creates a sense of achievement or growth. Much more engaging than static numbers.

**Implementation Notes**:

**Animations**: Number increment, easing function, duration control

**Code Example** (React Hook):
```jsx
import { useState, useEffect, useRef } from 'react';

function useCountUp(end, duration = 2000) {
  const [count, setCount] = useState(0);
  const countRef = useRef(0);
  const startTimeRef = useRef(null);
  
  useEffect(() => {
    const animate = (timestamp) => {
      if (!startTimeRef.current) startTimeRef.current = timestamp;
      const progress = timestamp - startTimeRef.current;
      const percentage = Math.min(progress / duration, 1);
      
      // Easing function (ease-out)
      const easeOut = 1 - Math.pow(1 - percentage, 3);
      countRef.current = Math.floor(easeOut * end);
      setCount(countRef.current);
      
      if (percentage < 1) {
        requestAnimationFrame(animate);
      }
    };
    
    requestAnimationFrame(animate);
  }, [end, duration]);
  
  return count;
}

// Usage
function StatCard({ value, label }) {
  const count = useCountUp(value, 2000);
  return (
    <div className="stat-card">
      <div className="stat-value">{count.toLocaleString()}+</div>
      <div className="stat-label">{label}</div>
    </div>
  );
}
```

**Colors**: Any (usually large bold text)

**Techniques**: requestAnimationFrame, easing functions, React hooks

**UI Elements**: Statistics, metrics, counters, achievements, social proof

**Interactions**: Auto-plays on scroll into view, can restart on re-enter

**Link**:
https://www.instagram.com/design_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_inspiration - Image Clip Path Reveal

**What I Found**:
Images that reveal using animated clip-path shapes - circles expanding, polygons forming, or custom shapes drawing themselves

**Why It's Relevant**:
Creates dramatic image reveals that feel cinematic. Adds storytelling to visuals. Perfect for portfolios, case studies, or hero sections. Makes images feel special, not just placed.

**Implementation Notes**:

**Animations**: Clip-path morphing, shape expansion, path drawing

**Code Example** (CSS):
```css
.clip-reveal {
  clip-path: circle(0% at 50% 50%);
  animation: circle-reveal 1s ease-out forwards;
}

@keyframes circle-reveal {
  to {
    clip-path: circle(100% at 50% 50%);
  }
}

/* Polygon reveal */
.polygon-reveal {
  clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  animation: polygon-reveal 0.8s ease-out forwards;
}

@keyframes polygon-reveal {
  to {
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  }
}
```

**Colors**: N/A (applies to images)

**Techniques**: CSS clip-path, polygon/circle shapes, Intersection Observer

**UI Elements**: Portfolio images, hero images, product photos, gallery items

**Interactions**: Scroll-triggered reveal, hover morphing

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Smooth Accordion FAQ

**What I Found**:
FAQ or accordion sections with smooth height transitions when expanding/collapsing, plus rotating chevron icons

**Why It's Relevant**:
Essential for any site with FAQ sections. Smooth animations feel premium compared to jarring opens/closes. Saves vertical space while keeping content accessible. Professional polish that users expect.

**Implementation Notes**:

**Animations**: Height expansion, opacity fade, icon rotation

**Code Example** (React):
```jsx
import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

function Accordion({ items }) {
  const [openIndex, setOpenIndex] = useState(null);
  
  return (
    <div className="accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className="accordion-header"
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            <span>{item.question}</span>
            <motion.span
              animate={{ rotate: openIndex === index ? 180 : 0 }}
              transition={{ duration: 0.2 }}
            >
              ▼
            </motion.span>
          </button>
          <AnimatePresence>
            {openIndex === index && (
              <motion.div
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: "auto", opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                transition={{ duration: 0.3, ease: "easeInOut" }}
                className="accordion-content"
              >
                <div className="accordion-body">{item.answer}</div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      ))}
    </div>
  );
}
```

**Colors**: #f9fafb (background), #1f2937 (text), #e5e7eb (border)

**Techniques**: Framer Motion AnimatePresence, max-height transitions, state management

**UI Elements**: FAQ sections, feature lists, pricing details, documentation

**Interactions**: Click to toggle, smooth expand/collapse, icon rotation

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - Magnetic Button Effect

**What I Found**:
Buttons that subtly move toward the cursor as it approaches, creating a magnetic pull effect before the user even clicks

**Why It's Relevant**:
Creates a delightful micro-interaction that makes buttons feel responsive and alive. Increases click-through rates by drawing attention. Premium feel that sets sites apart. Playful without being childish.

**Implementation Notes**:

**Animations**: Position shift based on cursor proximity, spring physics, magnetic pull

**Code Example** (React):
```jsx
import { useRef, useState } from 'react';
import { motion } from 'framer-motion';

function MagneticButton({ children }) {
  const buttonRef = useRef(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  
  const handleMouseMove = (e) => {
    if (!buttonRef.current) return;
    const rect = buttonRef.current.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    const distanceX = e.clientX - centerX;
    const distanceY = e.clientY - centerY;
    
    // Magnetic strength (lower = stronger pull)
    const strength = 0.3;
    
    setPosition({
      x: distanceX * strength,
      y: distanceY * strength
    });
  };
  
  const handleMouseLeave = () => {
    setPosition({ x: 0, y: 0 });
  };
  
  return (
    <motion.button
      ref={buttonRef}
      className="magnetic-button"
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      animate={{ x: position.x, y: position.y }}
      transition={{ type: "spring", stiffness: 150, damping: 15 }}
    >
      {children}
    </motion.button>
  );
}
```

**Colors**: Any CTA color

**Techniques**: Mouse position tracking, spring physics, transform translate

**UI Elements**: Primary CTAs, submit buttons, important links

**Interactions**: Mouse proximity detection, magnetic pull, spring return

**Link**:
https://www.instagram.com/design_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_inspiration - Before/After Image Slider

**What I Found**:
Interactive slider that reveals a second image as the user drags, perfect for showing transformations or comparisons

**Why It's Relevant**:
Perfect for portfolios (showing redesigns), beauty/services (before/after results), real estate (renovations), or any transformation story. Highly engaging interactive element. Users love playing with sliders.

**Implementation Notes**:

**Animations**: Clip-path adjustment, handle movement, smooth dragging

**Code Example** (React):
```jsx
import { useState, useRef } from 'react';

function BeforeAfterSlider({ beforeImage, afterImage }) {
  const [sliderPosition, setSliderPosition] = useState(50);
  const containerRef = useRef(null);
  
  const handleMove = (e) => {
    if (!containerRef.current) return;
    const rect = containerRef.current.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const percentage = Math.max(0, Math.min(100, (x / rect.width) * 100));
    setSliderPosition(percentage);
  };
  
  return (
    <div
      ref={containerRef}
      className="relative w-full h-96 cursor-ew-resize overflow-hidden"
      onMouseMove={(e) => e.buttons === 1 && handleMove(e)}
      onMouseDown={handleMove}
    >
      {/* After image (full width) */}
      <img src={afterImage} alt="After" className="absolute inset-0 w-full h-full object-cover" />
      
      {/* Before image (clipped) */}
      <div
        className="absolute inset-0 overflow-hidden"
        style={{ clipPath: `inset(0 ${100 - sliderPosition}% 0 0)` }}
      >
        <img src={beforeImage} alt="Before" className="w-full h-full object-cover" />
      </div>
      
      {/* Slider handle */}
      <div
        className="absolute top-0 bottom-0 w-1 bg-white shadow-lg"
        style={{ left: `${sliderPosition}%`, transform: 'translateX(-50%)' }}
      >
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-8 h-8 bg-white rounded-full shadow-lg flex items-center justify-center">
          ↔
        </div>
      </div>
    </div>
  );
}
```

**Colors**: White handle, shadow for depth

**Techniques**: Clip-path inset, mouse tracking, drag handling

**UI Elements**: Portfolio showcases, service results, product comparisons, testimonials

**Interactions**: Drag to reveal, click to jump, touch support

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Tilt Card Effect

**What I Found**:
Cards that tilt in 3D space following the mouse position, creating a dynamic perspective effect

**Why It's Relevant**:
Adds depth and interactivity to flat cards. Makes elements feel tangible and responsive. Premium effect that impresses users. Great for product cards, portfolio items, or feature highlights.

**Implementation Notes**:

**Animations**: 3D rotation based on mouse position, perspective shift, glare effect

**Code Example** (React):
```jsx
import { useRef, useState } from 'react';

function TiltCard({ children }) {
  const cardRef = useRef(null);
  const [transform, setTransform] = useState('');
  const [glarePosition, setGlarePosition] = useState({ x: 50, y: 50 });
  
  const handleMouseMove = (e) => {
    if (!cardRef.current) return;
    const rect = cardRef.current.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    
    const rotateX = (y - centerY) / 10;
    const rotateY = (centerX - x) / 10;
    
    setTransform(`perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`);
    setGlarePosition({ x: (x / rect.width) * 100, y: (y / rect.height) * 100 });
  };
  
  const handleMouseLeave = () => {
    setTransform('perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)');
  };
  
  return (
    <div
      ref={cardRef}
      className="relative transition-transform duration-100 ease-out"
      style={{ transform }}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
    >
      {children}
      <div
        className="absolute inset-0 pointer-events-none opacity-0 hover:opacity-20 transition-opacity"
        style={{
          background: `radial-gradient(circle at ${glarePosition.x}% ${glarePosition.y}%, rgba(255,255,255,0.8), transparent 50%)`
        }}
      />
    </div>
  );
}
```

**Colors**: Any card background with white glare overlay

**Techniques**: CSS 3D transforms, perspective, mouse position mapping

**UI Elements**: Product cards, portfolio items, feature cards, pricing cards

**Interactions**: Mouse move tracking, 3D rotation, glare effect

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future

### 2026-03-14 - design_inspiration - Smooth Page Transition

**What I Found**:
Animated page transitions that fade/slide between pages with smooth easing, creating a cinematic flow between views

**Why It's Relevant**:
Makes navigation feel fluid and premium. Reduces perception of page load time. Creates cohesive user journey. Perfect for SPAs (single page apps) or multi-page sites needing seamless transitions.

**Implementation Notes**:

**Animations**: Fade in/out, slide directions, staggered content reveal

**Code Example** (React + Framer Motion):
```jsx
import { motion } from 'framer-motion';

function PageTransition({ children }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      transition={{ duration: 0.5 }}
    >
      {children}
    </motion.div>
  );
}
```

**Colors**: Any (typically with fade/opacity)

**Techniques**: Framer Motion AnimatePresence, exit animations, layoutId for shared elements

**UI Elements**: Page wrappers, route transitions, section changes

**Interactions**: Auto-play on navigation, smooth between states

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Scroll Progress Bar

**What I Found**:
Animated progress bar at top of page that fills as user scrolls, providing visual feedback of reading progress

**Why It's Relevant**:
Improves user engagement and completion rates. Provides visual feedback on page length. Creates sense of progress. Great for long articles, documentation, or learning content.

**Implementation Notes**:

**Animations**: Width expansion based on scroll position, smooth transitions

**Code Example** (React):
```jsx
import { useState, useEffect } from 'react';

function ScrollProgressBar() {
  const [scrollProgress, setScrollProgress] = useState(0);
  
  useEffect(() => {
    const handleScroll = () => {
      const windowHeight = window.innerHeight;
      const docHeight = document.documentElement.scrollHeight - windowHeight;
      const scrolled = window.scrollY;
      const scrollPercent = (scrolled / docHeight) * 100;
      setScrollProgress(scrollPercent);
    };
    
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);
  
  return (
    <div
      className="fixed top-0 left-0 h-1 bg-gradient-to-r from-blue-500 to-purple-500 transition-all duration-300"
      style={{ width: `${scrollProgress}%` }}
    />
  );
}
```

**Colors**: Gradient (blue to purple), or brand accent

**Techniques**: Scroll event listener, width animation based on scroll

**UI Elements**: Page top bar, article progress indicator

**Interactions**: Auto-updates on scroll, smooth transitions

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - Pulse Dot Animation

**What I Found**:
Animated pulsing dots or circles that expand outward with fade, typically used to indicate live status or attract attention

**Why It's Relevant**:
Draws attention to important elements or live status indicators. Used for notifications, online status, new features. Simple but effective attention grabber without being aggressive.

**Implementation Notes**:

**Animations**: Scale expansion, opacity fade, continuous pulse

**Code Example** (CSS):
```css
.pulse-dot {
  position: relative;
  width: 16px;
  height: 16px;
  background: #ef4444;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(239, 68, 68, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(239, 68, 68, 0);
  }
}
```

**Colors**: #ef4444 (red), #10b981 (green for online), brand accent

**Techniques**: Box-shadow animation, scale pulse, opacity fade

**UI Elements**: Live status badges, notification indicators, attention grabbers

**Interactions**: Continuous pulse, can stop/pause on interaction

**Link**:
https://www.instagram.com/design_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_inspiration - Breadcrumb Animation

**What I Found**:
Navigation breadcrumbs with animated dividers or separators that reveal/animate between items

**Why It's Relevant**:
Improves navigation hierarchy visualization. Breadcrumbs help users understand site structure. Animated separators add polish and guide attention through the navigation path.

**Implementation Notes**:

**Animations**: Separator slide/scale, color transitions, staggered reveals

**Code Example** (CSS):
```css
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 12px;
}

.breadcrumb-item {
  color: #6b7280;
  text-decoration: none;
}

.breadcrumb-item:hover {
  color: #3b82f6;
  transition: color 0.3s ease;
}

.breadcrumb-divider {
  color: #d1d5db;
  position: relative;
  overflow: hidden;
}

.breadcrumb-divider::after {
  content: '→';
  display: inline-block;
  animation: slide-in 0.4s ease;
}

@keyframes slide-in {
  from {
    opacity: 0;
    transform: translateX(-4px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
```

**Colors**: #6b7280 (text), #3b82f6 (hover), #d1d5db (divider)

**Techniques**: CSS animations, inline-block dividers, slide transitions

**UI Elements**: Navigation breadcrumbs, path indicators, site hierarchy

**Interactions**: Hover color change, animated separator reveal

**Link**:
https://www.instagram.com/design_inspiration/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - webdesign_trends - Gradient Text Animation v2

**What I Found**:
Text with animated gradient background that shifts colors or position continuously

**Why It's Relevant**:
Creates eye-catching, modern headings. Great for branding and memorable CTAs. Makes text feel premium and alive. Perfect for hero sections and feature highlights.

**Implementation Notes**:

**Animations**: Gradient position shift, background-size animation, color cycling

**Code Example** (CSS):
```css
.gradient-text {
  background: linear-gradient(
    90deg,
    #667eea 0%,
    #764ba2 25%,
    #f093fb 50%,
    #4facfe 75%,
    #00f2fe 100%
  );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradient-shift 4s ease infinite;
}

@keyframes gradient-shift {
  0% { background-position: 0% center; }
  50% { background-position: 100% center; }
  100% { background-position: 0% center; }
}
```

**Colors**: Multi-color gradients (blue, purple, pink, cyan combinations)

**Techniques**: Background gradient, background-clip: text, background-size animation

**UI Elements**: Hero headlines, feature titles, brand names, CTAs

**Interactions**: Continuous auto-play, can pause on hover

**Link**:
https://www.instagram.com/webdesign_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

### 2026-03-14 - design_trends - Wave Text Animation Final

**What I Found**:
Text where each character waves up and down in sequence, creating an undulating wave effect through the text

**Why It's Relevant**:
Creates playful, eye-catching headlines that feel alive. Great for entertainment, kids, creative, or casual brands. Makes text memorable and fun while remaining readable.

**Implementation Notes**:

**Animations**: Y-axis oscillation, staggered timing per character, sine wave motion

**Code Example** (React):
```jsx
import { motion } from 'framer-motion';

function WaveText({ text }) {
  return (
    <div className="flex gap-1">
      {text.split('').map((char, index) => (
        <motion.span
          key={index}
          animate={{ y: [0, -10, 0] }}
          transition={{
            duration: 0.6,
            delay: index * 0.05,
            repeat: Infinity,
          }}
          className="inline-block"
        >
          {char}
        </motion.span>
      ))}
    </div>
  );
}
```

**Colors**: Any text color

**Techniques**: Character-level animation, stagger timing, sine wave motion

**UI Elements**: Hero headlines, playful CTAs, feature titles

**Interactions**: Continuous loop, can pause on hover

**Link**:
https://www.instagram.com/design_trends/

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Documented for future use
- [ ] Done - Implemented in project

---

---

### 2026-03-14 - Andy's Design Philosophy - Human-Crafted Website Guidelines

**What I Found**:
Core design principles for creating professional, human-designed websites that avoid AI-generated aesthetics

**Why It's Relevant**:
This is the master design brief for ALL future website builds. Ensures consistency, professionalism, and human-crafted feel across all client projects.

**Design Requirements**:

**Color Palette**:
- Balanced, neutral colors (NO neon, NO overly pastel, NO chaotic gradients)
- Professional tones: grays, navy, forest green, warm neutrals
- Maximum 2-3 colors total (primary + accent + neutral)

**Typography**:
- Sans-serif headers (Inter, Geist, or similar clean fonts)
- Highly legible body text (system fonts or clean sans-serif)
- Clear hierarchy: H1 (large), H2 (medium), body (readable), captions (small)
- Line height: 1.5-1.6 for body, 1.2-1.3 for headers

**Layout Principles**:
- Intentional spacing (consistent 8px grid system)
- Aligned sections (no random misalignments)
- Natural visual flow (F-pattern or Z-pattern reading)
- Generous whitespace (breathing room between sections)
- Max-width containers (1200-1400px) with centered content

**Required Sections**:
1. **Navigation** - Clean, clear labels, sticky on scroll
2. **Hero** - Strong headline, sub-headline, single clear CTA
3. **About** - Concise, confident copy (NO "We are passionate about...")
4. **Services/Features** - Clear value propositions, icon + text pairs
5. **Testimonials** - Real quotes, names, photos if available
6. **Contact** - Simple form or clear contact info
7. **Footer** - Essential links, copyright, social icons

**Copy Guidelines**:
- AVOID: "Welcome to our website", "We are passionate about", "At [Company], we believe"
- USE: Direct statements, benefits-focused, action-oriented
- Example: "Professional plumbing services in Boston" NOT "We are passionate about providing the best plumbing services"

**Animations** (70+ Total):
- **Button Effects**: Magnetic, liquid fill, neon glow, 3D flip, ripple, border draw, text scramble, scale bounce, gradient shift, arrow slide
- **Card Effects**: 3D tilt, spotlight hover, border glow, image zoom, content reveal, glass morphism, shadow lift, rotate entrance, stagger fade, flip card
- **Text Effects**: Typewriter, wave text, glitch effect, gradient text, underline draw, letter spacing, blur reveal, split text, count up, text mask
- **Section Effects**: Parallax scroll, pin section, horizontal scroll, reveal up, clip path, blur fade, scale reveal, rotate in, slide overlap, morphing background
- **Micro-interactions**: Skeleton screens, shimmer, progress bars, spinners, success checks, error shake, notifications, badge pulse, heart beat, save bookmark
- **Advanced**: Particle burst, smoke effect, fireworks, confetti, cursor trail, distortion, RGB split, noise texture, scan lines, vignette pulse, lens flare, hologram, neon flicker, glitch transition, morphing SVG, draw SVG, liquid button, elastic, spring physics, inertia scroll
- **Rules**: Subtle by default, purposeful motion, 60fps minimum, respect prefers-reduced-motion

**Technical Standards**:
- Responsive: mobile-first, breakpoints at 640px, 768px, 1024px
- Accessible: WCAG AA contrast (4.5:1 minimum), alt text, semantic HTML
- Performance: optimized images (WebP), lazy loading, minimal JS
- Clean code: semantic HTML5, BEM CSS naming, no inline styles

**Overall Tone**:
- Credible and trustworthy
- Modern but timeless
- Human-designed, not algorithmic
- Professional, not quirky

**Link**:
Internal Design System

**Status**:
- [ ] Todo - Save for later
- [x] In Progress - Active design standard
- [ ] Done - Implemented in all projects

---
