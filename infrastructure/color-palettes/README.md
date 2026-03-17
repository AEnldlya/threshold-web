# Color Palette Library

## CSS Variable System

### Base Structure
```css
:root {
  /* Core colors */
  --color-bg: #0A0A0F;
  --color-surface: #1A1A1F;
  --color-text: #FFFFFF;
  --color-accent: #00E5FF;
  
  /* Semantic colors */
  --color-primary: var(--color-accent);
  --color-secondary: rgba(255, 255, 255, 0.6);
  --color-muted: rgba(255, 255, 255, 0.4);
  --color-border: rgba(255, 255, 255, 0.1);
  
  /* State colors */
  --color-hover: rgba(255, 255, 255, 0.1);
  --color-active: rgba(255, 255, 255, 0.2);
  --color-focus: var(--color-accent);
  
  /* Gradients */
  --gradient-hero: linear-gradient(180deg, var(--color-bg) 0%, var(--color-surface) 100%);
  --gradient-accent: linear-gradient(135deg, var(--color-accent) 0%, var(--color-accent-dark) 100%);
}
```

## Pre-Built Palettes by Business Type

### Tech/SaaS
```css
[data-theme="tech"] {
  --color-bg: #0A0A0F;
  --color-surface: #141419;
  --color-text: #FFFFFF;
  --color-accent: #00E5FF;
  --color-accent-dark: #00B8CC;
  --color-accent-light: #66F0FF;
}
```
**Characteristics:** Dark void, electric cyan accent, high contrast
**Use For:** SaaS products, tech startups, developer tools
**Mood:** Futuristic, precise, cutting-edge

### Luxury
```css
[data-theme="luxury"] {
  --color-bg: #FAF7F2;
  --color-surface: #FFFFFF;
  --color-text: #1A1208;
  --color-accent: #C9A84C;
  --color-accent-dark: #A0853A;
  --color-accent-light: #E0C878;
}
```
**Characteristics:** Warm cream, deep ink text, gold accent
**Use For:** Fashion brands, high-end services, luxury goods
**Mood:** Elegant, refined, exclusive

### Agency/Creative
```css
[data-theme="agency"] {
  --color-bg: #0D0D0D;
  --color-surface: #1A1A1A;
  --color-text: #FFFFFF;
  --color-accent: #FF3B00;
  --color-accent-dark: #CC2F00;
  --color-accent-light: #FF6B3D;
}
```
**Characteristics:** Near-black, bold orange-red accent
**Use For:** Creative agencies, design studios, bold brands
**Mood:** Bold, energetic, unconventional

### Food/Hospitality
```css
[data-theme="food"] {
  --color-bg: #FDF6EE;
  --color-surface: #FFFFFF;
  --color-text: #2C1810;
  --color-accent: #D4824A;
  --color-accent-dark: #A8653A;
  --color-accent-light: #E8A87A;
}
```
**Characteristics:** Warm cream, earthy brown text, terracotta accent
**Use For:** Restaurants, cafes, food brands
**Mood:** Warm, inviting, appetizing

### Finance
```css
[data-theme="finance"] {
  --color-bg: #0F1923;
  --color-surface: #1A2530;
  --color-text: #FFFFFF;
  --color-accent: #E8D5A3;
  --color-accent-dark: #C4B082;
  --color-accent-light: #F0E3C4;
}
```
**Characteristics:** Deep navy, gold accent, trustworthy
**Use For:** Financial services, legal, consulting
**Mood:** Professional, trustworthy, established

### Wellness
```css
[data-theme="wellness"] {
  --color-bg: #F5F0EB;
  --color-surface: #FFFFFF;
  --color-text: #2D3748;
  --color-accent: #3D6B4F;
  --color-accent-dark: #2D5039;
  --color-accent-light: #5A8A6B;
}
```
**Characteristics:** Soft warm white, sage green accent
**Use For:** Health, wellness, yoga, meditation
**Mood:** Calm, natural, restorative

### Gaming
```css
[data-theme="gaming"] {
  --color-bg: #060608;
  --color-surface: #0F0F12;
  --color-text: #FFFFFF;
  --color-accent: #00FF88;
  --color-accent-dark: #00CC6D;
  --color-accent-light: #66FFB0;
}
```
**Characteristics:** Near-black void, neon green accent
**Use For:** Gaming, esports, entertainment
**Mood:** Energetic, futuristic, immersive

### E-commerce
```css
[data-theme="ecommerce"] {
  --color-bg: #FFFFFF;
  --color-surface: #F8F8F8;
  --color-text: #1A1A1A;
  --color-accent: #FF6B35;
  --color-accent-dark: #E55A2B;
  --color-accent-light: #FF8F66;
}
```
**Characteristics:** Clean white, coral/orange accent
**Use For:** Online stores, retail, product sites
**Mood:** Clean, conversion-focused, friendly

### Education
```css
[data-theme="education"] {
  --color-bg: #FDFBF7;
  --color-surface: #FFFFFF;
  --color-text: #2D3748;
  --color-accent: #4A5568;
  --color-accent-dark: #2D3748;
  --color-accent-light: #718096;
}
```
**Characteristics:** Warm off-white, slate gray accent
**Use For:** Schools, courses, non-profits
**Mood:** Accessible, trustworthy, clear

### Portfolio
```css
[data-theme="portfolio"] {
  --color-bg: #0A0A0A;
  --color-surface: #141414;
  --color-text: #FFFFFF;
  --color-accent: #FFFFFF;
  --color-accent-dark: #CCCCCC;
  --color-accent-light: #FFFFFF;
}
```
**Characteristics:** True black, white accent (monochrome)
**Use For:** Personal portfolios, creative showcases
**Mood:** Minimal, focused, artistic

## Dark/Light Mode Variants

### Auto-Generating Variants
```tsx
// utils/colorVariants.ts
export function generateVariants(basePalette) {
  return {
    dark: basePalette,
    light: {
      ...basePalette,
      '--color-bg': invertColor(basePalette['--color-bg']),
      '--color-surface': lightenColor(basePalette['--color-surface'], 0.9),
      '--color-text': basePalette['--color-bg'],
    }
  };
}
```

### Manual Light Variants

#### Tech Light
```css
[data-theme="tech-light"] {
  --color-bg: #F0F4F8;
  --color-surface: #FFFFFF;
  --color-text: #0A0A0F;
  --color-accent: #0088CC;
  --color-accent-dark: #006699;
  --color-accent-light: #33AAE6;
}
```

#### Luxury Dark
```css
[data-theme="luxury-dark"] {
  --color-bg: #1A1208;
  --color-surface: #2A2010;
  --color-text: #FAF7F2;
  --color-accent: #D4AF37;
  --color-accent-dark: #B8960C;
  --color-accent-light: #E5C76B;
}
```

## Logo Color Extraction Tool

### Implementation
```tsx
// components/LogoColorExtractor.tsx
import { useState, useRef, useEffect } from 'react';

export function LogoColorExtractor({ onColorsExtracted }) {
  const [image, setImage] = useState(null);
  const [colors, setColors] = useState([]);
  const canvasRef = useRef(null);
  
  const extractColors = (img) => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0);
    
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const pixels = imageData.data;
    const colorMap = new Map();
    
    // Sample every 10th pixel for performance
    for (let i = 0; i < pixels.length; i += 40) {
      const r = pixels[i];
      const g = pixels[i + 1];
      const b = pixels[i + 2];
      const a = pixels[i + 3];
      
      if (a < 128) continue; // Skip transparent
      
      const hex = `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`;
      colorMap.set(hex, (colorMap.get(hex) || 0) + 1);
    }
    
    // Sort by frequency and get top colors
    const sortedColors = Array.from(colorMap.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([color]) => color);
    
    setColors(sortedColors);
    onColorsExtracted(sortedColors);
  };
  
  return (
    <div className="color-extractor">
      <input 
        type="file" 
        accept="image/*"
        onChange={(e) => {
          const file = e.target.files[0];
          const img = new Image();
          img.onload = () => extractColors(img);
          img.src = URL.createObjectURL(file);
          setImage(img);
        }}
      />
      <canvas ref={canvasRef} style={{ display: 'none' }} />
      
      {colors.length > 0 && (
        <div className="extracted-colors">
          {colors.map((color, i) => (
            <div 
              key={i}
              className="color-swatch"
              style={{ backgroundColor: color }}
              title={color}
            />
          ))}
        </div>
      )}
    </div>
  );
}
```

## Accessibility Testing

### Contrast Ratio Calculator
```tsx
// utils/contrast.ts
function getLuminance(r, g, b) {
  const [rs, gs, bs] = [r, g, b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

export function getContrastRatio(color1, color2) {
  const lum1 = getLuminance(...hexToRgb(color1));
  const lum2 = getLuminance(...hexToRgb(color2));
  const brightest = Math.max(lum1, lum2);
  const darkest = Math.min(lum1, lum2);
  return (brightest + 0.05) / (darkest + 0.05);
}

export function meetsWCAG(color1, color2, level = 'AA') {
  const ratio = getContrastRatio(color1, color2);
  return level === 'AAA' ? ratio >= 7 : ratio >= 4.5;
}
```

### Automated Contrast Check
```tsx
// components/ContrastChecker.tsx
export function ContrastChecker({ bg, text, accent }) {
  const textRatio = getContrastRatio(bg, text);
  const accentRatio = getContrastRatio(bg, accent);
  
  return (
    <div className="contrast-checker">
      <div 
        className="preview"
        style={{ backgroundColor: bg, color: text }}
      >
        <p>Sample text on background</p>
        <button style={{ backgroundColor: accent }}>Button</button>
      </div>
      
      <div className="ratios">
        <div className={textRatio >= 4.5 ? 'pass' : 'fail'}>
          Text: {textRatio.toFixed(2)}:1 {textRatio >= 4.5 ? '✓' : '✗'}
        </div>
        <div className={accentRatio >= 3 ? 'pass' : 'fail'}>
          Accent: {accentRatio.toFixed(2)}:1 {accentRatio >= 3 ? '✓' : '✗'}
        </div>
      </div>
    </div>
  );
}
```

## Export Formats

### CSS Variables
```css
/* palettes/tech.css */
:root {
  --tech-bg: #0A0A0F;
  --tech-surface: #141419;
  --tech-text: #FFFFFF;
  --tech-accent: #00E5FF;
}
```

### Tailwind Config
```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        tech: {
          bg: '#0A0A0F',
          surface: '#141419',
          text: '#FFFFFF',
          accent: '#00E5FF',
        },
        luxury: {
          bg: '#FAF7F2',
          surface: '#FFFFFF',
          text: '#1A1208',
          accent: '#C9A84C',
        },
        // ... other palettes
      }
    }
  }
}
```

### Figma Variables
```json
{
  "tech": {
    "bg": { "r": 0.039, "g": 0.039, "b": 0.059 },
    "surface": { "r": 0.078, "g": 0.078, "b": 0.098 },
    "text": { "r": 1, "g": 1, "b": 1 },
    "accent": { "r": 0, "g": 0.898, "b": 1 }
  }
}
```

## Usage Guidelines

### Dominant + Accent Rule
- Background: 70-80% of visual weight
- Text: 15-20% of visual weight
- Accent: 5-10% of visual weight (buttons, links, highlights only)

### When to Use Each Palette
- **Dark themes:** Tech, gaming, agency, portfolio, luxury (dark variant)
- **Light themes:** Luxury, food, wellness, e-commerce, education
- **High contrast:** Finance, education (accessibility priority)
- **Low contrast:** Luxury, wellness (mood priority)

### Gradient Usage
- Maximum 2 colors in any gradient
- Slow transitions (subtle)
- Use for backgrounds only, never text
- Opacity variations preferred over new colors

## Implementation Checklist

- [ ] 10 base palettes defined
- [ ] Dark/light variants for each
- [ ] CSS variable system implemented
- [ ] Logo color extraction tool built
- [ ] Contrast ratio calculator working
- [ ] WCAG AA compliance verified for all palettes
- [ ] Tailwind config generated
- [ ] Figma variables exported
- [ ] Usage guidelines documented
- [ ] Real-time preview tool created
