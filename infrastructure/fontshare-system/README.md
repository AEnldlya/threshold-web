# Fontshare Integration System

## System Architecture

### Automated Font Loading Component

```tsx
// components/FontLoader.tsx
import { useEffect, useState } from 'react';

interface FontConfig {
  family: string;
  weights: number[];
  variable?: boolean;
}

interface FontPair {
  display: FontConfig;
  body: FontConfig;
}

export const fontPairs: Record<string, FontPair> = {
  tech: {
    display: { family: 'clash-display', weights: [400, 600, 800] },
    body: { family: 'satoshi', weights: [400, 500, 700], variable: true }
  },
  luxury: {
    display: { family: 'melodrama', weights: [400, 600] },
    body: { family: 'zodiak', weights: [400, 500] }
  },
  editorial: {
    display: { family: 'boska', weights: [400, 600, 800] },
    body: { family: 'general-sans', weights: [400, 500, 600] }
  },
  agency: {
    display: { family: 'tanker', weights: [400] },
    body: { family: 'switzer', weights: [400, 500, 600] }
  },
  food: {
    display: { family: 'author', weights: [400, 600] },
    body: { family: 'general-sans', weights: [400, 500] }
  },
  finance: {
    display: { family: 'fraunces', weights: [400, 600], variable: true },
    body: { family: 'epilogue', weights: [400, 500, 600], variable: true }
  },
  wellness: {
    display: { family: 'syne-serif', weights: [400, 600] },
    body: { family: 'chillax', weights: [400, 500], variable: true }
  },
  gaming: {
    display: { family: 'clash-display', weights: [600, 800] },
    body: { family: 'supreme', weights: [400, 700] }
  },
  portfolio: {
    display: { family: 'boska', weights: [400, 600] },
    body: { family: 'cabinet-grotesk', weights: [400, 500] }
  },
  ecommerce: {
    display: { family: 'cabinet-grotesk', weights: [500, 700] },
    body: { family: 'general-sans', weights: [400, 500] }
  },
  education: {
    display: { family: 'plein', weights: [400, 600] },
    body: { family: 'epilogue', weights: [400, 500, 600], variable: true }
  }
};

export function FontLoader({ pair }: { pair: FontPair }) {
  const [loaded, setLoaded] = useState(false);
  
  useEffect(() => {
    const displayWeights = pair.display.weights.join(',');
    const bodyWeights = pair.body.weights.join(',');
    
    const displayVar = pair.display.variable ? ',variable' : '';
    const bodyVar = pair.body.variable ? ',variable' : '';
    
    const url = `https://api.fontshare.com/v2/css?f[]=${pair.display.family}@${displayWeights}${displayVar}&f[]=${pair.body.family}@${bodyWeights}${bodyVar}&display=swap`;
    
    const link = document.createElement('link');
    link.href = url;
    link.rel = 'stylesheet';
    link.onload = () => setLoaded(true);
    
    document.head.appendChild(link);
    
    // Add CSS variables
    const style = document.createElement('style');
    style.textContent = `
      :root {
        --font-display: '${pair.display.family.replace(/-/g, ' ')}', sans-serif;
        --font-body: '${pair.body.family.replace(/-/g, ' ')}', sans-serif;
      }
    `;
    document.head.appendChild(style);
    
    return () => {
      document.head.removeChild(link);
      document.head.removeChild(style);
    };
  }, [pair]);
  
  return loaded ? null : <div className="font-loading">Loading fonts...</div>;
}
```

## Font Catalog with Full Details

### Sans-Serif Fonts

#### Satoshi
```
Family: satoshi
Styles: 9 (Light, Regular, Medium, Bold, Black + Italics)
Variable: Yes
Best For: SaaS, tech, clean UI
Characteristics: Geometric grotesque, modern, highly legible
Pair With: Clash Display (tech), Tanker (bold)
Weights to Load: 400, 500, 700
```

#### General Sans
```
Family: general-sans
Styles: 10 (Light to Bold + Italics)
Variable: No
Best For: Food, e-commerce, neutral brands
Characteristics: Neutral humanist, versatile, works at all sizes
Pair With: Author (food), Boska (editorial)
Weights to Load: 400, 500, 600
```

#### Cabinet Grotesk
```
Family: cabinet-grotesk
Styles: 8 (Thin to Black)
Variable: No
Best For: Portfolios, lifestyle brands
Characteristics: Softened terminals, friendly, approachable
Pair With: Boska (portfolio), Melodrama (luxury)
Weights to Load: 400, 500
```

#### Switzer
```
Family: switzer
Styles: 9 (Light to Black + Italics)
Variable: No
Best For: Agencies, editorial
Characteristics: Clean neo-grotesk, sharp, professional
Pair With: Tanker (agency), Ranade (editorial)
Weights to Load: 400, 500, 600
```

#### Clash Grotesk
```
Family: clash-grotesk
Styles: 8 (Extralight to Bold)
Variable: No
Best For: Corporate identity, editorial
Characteristics: Small apertures, distinctive, authoritative
Pair With: Clash Display (tech), Tanker (bold)
Weights to Load: 400, 600
```

#### Epilogue
```
Family: epilogue
Styles: 18 (9 weights + Italics)
Variable: Yes
Best For: Body text, accessible UI, longform
Characteristics: Versatile, highly readable, professional
Pair With: Fraunces (finance), Plein (education)
Weights to Load: 400, 500, 600
```

#### Plein
```
Family: plein
Styles: 6 (Light to Bold + Italics)
Variable: No
Best For: Education, professional services
Characteristics: Humanist, double-storey a/g, very readable
Pair With: Epilogue (education), Fraunces (professional)
Weights to Load: 400, 500
```

#### Chillax
```
Family: chillax
Styles: 6 (Extralight to Bold)
Variable: Yes
Best For: Wellness, consumer apps
Characteristics: Rounded, friendly, soft
Pair With: Syne Serif (wellness), Author (food)
Weights to Load: 400, 500
```

#### Supreme
```
Family: supreme
Styles: 5 (Light to Heavy)
Variable: No
Best For: Gaming, entertainment
Characteristics: Bold weight-focused, impactful, modern
Pair With: Clash Display (gaming), Tanker (bold)
Weights to Load: 400, 700
```

### Display Fonts

#### Clash Display
```
Family: clash-display
Styles: 8 (Extralight to Bold)
Variable: No
Best For: Tech, gaming, bold brands
Characteristics: Ultra-wide at heavy weights, high contrast strokes
Use At: h1, hero text, large pull quotes
Sizes: 72px minimum for impact
Pair With: Satoshi (tech), Supreme (gaming)
Weights to Load: 400, 600, 800
```

#### Boska
```
Family: boska
Styles: 9 (Light to Black + Italics)
Variable: No
Best For: Luxury, editorial, portfolios
Characteristics: Elegant high-contrast serif display
Use At: h1, hero text, luxury headlines
Sizes: 64px minimum
Pair With: General Sans (editorial), Cabinet Grotesk (portfolio)
Weights to Load: 400, 600, 800
```

#### Melodrama
```
Family: melodrama
Styles: 7 (Light to Bold)
Variable: No
Best For: Fashion, luxury, creative studios
Characteristics: Editorial high-fashion display, dramatic
Use At: h1, hero text, fashion headlines
Sizes: 80px minimum
Pair With: Zodiak (luxury), Switzer (editorial)
Weights to Load: 400, 600
```

#### Tanker
```
Family: tanker
Styles: 1 (Regular)
Variable: No
Best For: Agencies, impact-first brands
Characteristics: Heavy slab display, bold, commanding
Use At: h1, hero text, statements
Sizes: 96px minimum
Pair With: Switzer (agency), Satoshi (tech)
Weights to Load: 400
```

#### Ranade
```
Family: ranade
Styles: 7 (Light to Bold + Italics)
Variable: No
Best For: Agencies, editorial
Characteristics: Strong display serif, confident
Use At: h1, hero text, editorial headlines
Sizes: 72px minimum
Pair With: Switzer (agency), General Sans (editorial)
Weights to Load: 400, 600
```

#### Author
```
Family: author
Styles: 7 (Light to Bold + Italics)
Variable: No
Best For: Food, hospitality
Characteristics: Humanist display, warm, inviting
Use At: h1, hero text, restaurant headlines
Sizes: 64px minimum
Pair With: General Sans (food), Chillax (wellness)
Weights to Load: 400, 600
```

### Serif/Editorial Fonts

#### Fraunces
```
Family: fraunces
Styles: 9 (Light to Black + Italics)
Variable: Yes
Best For: Finance, longform, legal
Characteristics: Soft optical serif, beautiful italics, trustworthy
Use At: Headlines, pull quotes, editorial
Pair With: Epilogue (finance), Plein (legal)
Weights to Load: 400, 600
```

#### Sentient
```
Family: sentient
Styles: 7 (Light to Bold + Italics)
Variable: No
Best For: Luxury, fashion
Characteristics: Elegant transitional serif, refined
Use At: Body text, editorial, luxury content
Pair With: Melodrama (luxury), Boska (fashion)
Weights to Load: 400, 500
```

#### Zodiak
```
Family: zodiak
Styles: 8 (Light to Black + Italics)
Variable: No
Best For: Magazines, fashion
Characteristics: High-contrast editorial serif, dramatic
Use At: Body text, editorial headlines
Pair With: Melodrama (fashion), Boska (luxury)
Weights to Load: 400, 500
```

#### Syne Serif
```
Family: syne-serif
Styles: 5 (Regular to Bold)
Variable: No
Best For: Wellness, modern editorial
Characteristics: Geometric serif, modern, clean
Use At: Headlines, wellness content
Pair With: Chillax (wellness), Author (food)
Weights to Load: 400, 600
```

#### Rowan
```
Family: rowan
Styles: 6 (Light to Bold + Italics)
Variable: No
Best For: Restaurants, hospitality
Characteristics: Warm serif, inviting, traditional
Use At: Headlines, restaurant content
Pair With: Author (food), General Sans (hospitality)
Weights to Load: 400, 500
```

## Font Pairing Preview Tool

```tsx
// components/FontPreview.tsx
export function FontPreview() {
  const [selectedPair, setSelectedPair] = useState('tech');
  const pair = fontPairs[selectedPair];
  
  return (
    <div className="font-preview">
      <select 
        value={selectedPair} 
        onChange={(e) => setSelectedPair(e.target.value)}
      >
        {Object.keys(fontPairs).map(key => (
          <option key={key} value={key}>{key}</option>
        ))}
      </select>
      
      <div 
        className="preview-display"
        style={{ fontFamily: `var(--font-display)` }}
      >
        <h1>Display Font Sample</h1>
        <h2>Secondary Headline</h2>
      </div>
      
      <div 
        className="preview-body"
        style={{ fontFamily: `var(--font-body)` }}
      >
        <p>Body text sample for readability testing. The quick brown fox jumps over the lazy dog.</p>
        <button>Button Text</button>
        <small>Caption text sample</small>
      </div>
    </div>
  );
}
```

## CSS Integration

### Global Styles
```css
/* styles/fonts.css */
:root {
  /* These are set by FontLoader component */
  --font-display: 'Clash Display', sans-serif;
  --font-body: 'Satoshi', sans-serif;
  
  /* Size scale */
  --text-xs: 0.75rem;      /* 12px */
  --text-sm: 0.875rem;     /* 14px */
  --text-base: 1rem;       /* 16px */
  --text-lg: 1.125rem;     /* 18px */
  --text-xl: 1.25rem;      /* 20px */
  --text-2xl: 1.5rem;      /* 24px */
  --text-3xl: 2rem;        /* 32px */
  --text-4xl: 2.5rem;      /* 40px */
  --text-5xl: 3rem;        /* 48px */
  --text-6xl: 4rem;        /* 64px */
  --text-7xl: 6rem;        /* 96px */
  --text-8xl: 8rem;        /* 128px */
  --text-9xl: 10rem;       /* 160px */
}

/* Display font usage */
h1, h2, .display {
  font-family: var(--font-display);
  font-weight: 600;
  line-height: 0.95;
  letter-spacing: -0.02em;
}

h1 {
  font-size: var(--text-7xl); /* 96px default, override per design */
}

h2 {
  font-size: var(--text-5xl); /* 48px default */
}

/* Body font usage */
body, p, span, a, button, input, label {
  font-family: var(--font-body);
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: 0;
}

/* Navigation labels */
nav a {
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-size: var(--text-sm);
}

/* Utility classes */
.font-display {
  font-family: var(--font-display);
}

.font-body {
  font-family: var(--font-body);
}

.text-display-xl {
  font-size: var(--text-8xl);
  line-height: 0.9;
}

.text-display-lg {
  font-size: var(--text-7xl);
  line-height: 0.95;
}
```

## Font Loading Strategy

### Performance Optimization
```tsx
// hooks/useFontPreload.ts
export function useFontPreload(pair: FontPair) {
  useEffect(() => {
    // Preload critical fonts
    const criticalFonts = [
      `https://api.fontshare.com/v2/css?f[]=${pair.display.family}@600&display=swap`,
      `https://api.fontshare.com/v2/css?f[]=${pair.body.family}@400&display=swap`
    ];
    
    criticalFonts.forEach(href => {
      const link = document.createElement('link');
      link.rel = 'preload';
      link.as = 'style';
      link.href = href;
      document.head.appendChild(link);
    });
  }, [pair]);
}
```

### FOUT Prevention
```css
/* Prevent Flash of Unstyled Text */
@font-face {
  font-family: 'Clash Display';
  font-display: swap;
  src: local('Clash Display');
}

/* Loading state */
.font-loading {
  opacity: 0;
  transition: opacity 0.3s ease;
}

.fonts-loaded .font-loading {
  opacity: 1;
}
```

## Business Type Quick Reference

| Business Type | Display Font | Body Font | Display Size | Body Size |
|--------------|--------------|-----------|--------------|-----------|
| SaaS/Tech | Clash Display | Satoshi | 96-128px | 17-18px |
| Luxury | Melodrama | Zodiak | 80-120px | 17-18px |
| Agency | Tanker | Switzer | 96-160px | 17-18px |
| Food | Author | General Sans | 64-96px | 17-18px |
| Finance | Fraunces | Epilogue | 72-96px | 17-20px |
| Wellness | Syne Serif | Chillax | 64-80px | 17-18px |
| Gaming | Clash Display | Supreme | 96-160px | 17-18px |
| Portfolio | Boska | Cabinet Grotesk | 80-120px | 17-18px |
| E-commerce | Cabinet Grotesk | General Sans | 72-96px | 17-18px |
| Education | Plein | Epilogue | 64-80px | 17-20px |

## Implementation Checklist

- [ ] FontLoader component created and tested
- [ ] All 20 Fontshare fonts cataloged
- [ ] 11 business type pairs defined
- [ ] CSS variable system implemented
- [ ] Font preview tool built
- [ ] Preload strategy implemented
- [ ] FOUT prevention added
- [ ] Size scale defined (xs to 9xl)
- [ ] Line heights configured
- [ ] Letter spacing rules set
- [ ] Weight pairings documented
- [ ] Performance benchmarks established
- [ ] Loading states designed
- [ ] Fallback fonts specified
