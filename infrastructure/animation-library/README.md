# Animation Library & Timing Reference

## Easing Curves Library

```css
/* animations/easing.css */
:root {
  --ease-linear: linear;
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  
  /* Custom luxury easing */
  --ease-out-quad: cubic-bezier(0, 0.55, 0.45, 1);
  --ease-out-cubic: cubic-bezier(0.215, 0.61, 0.355, 1);
  --ease-out-quart: cubic-bezier(0.165, 0.84, 0.44, 1);
  --ease-out-quint: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-out-expo: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-out-circ: cubic-bezier(0, 0.55, 0.45, 1);
  
  /* Custom bold easing */
  --ease-in-back: cubic-bezier(0.6, -0.28, 0.735, 0.045);
  --ease-out-back: cubic-bezier(0.175, 0.885, 0.32, 1.275);
  
  /* Spring-like */
  --ease-spring-1: cubic-bezier(0.175, 0.885, 0.32, 1.275);
  --ease-spring-2: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## Duration Guidelines

```ts
// animations/durations.ts
export const DURATIONS = {
  // $500 Tier
  micro: 200,      // 0.2s - quick micro-interactions
  short: 300,      // 0.3s - button hovers, simple reveals
  base: 400,       // 0.4s - standard fade, scroll reveals
  
  // $50K Tier
  medium: 600,     // 0.6s - card reveals, stagger start
  long: 800,       // 0.8s - section transitions
  luxury: 1000,    // 1.0s - silk reveals
  cinematic: 1200, // 1.2s - elaborate sequences
  epic: 1600,      // 1.6s - maximum luxury feel
  
  // Scroll-driven
  scroll: 2000,    // 2.0s - full scroll sequence
} as const;
```

## Spring Physics Configurations

```ts
// animations/springs.ts
export const SPRINGS = {
  gentle: {
    stiffness: 100,
    damping: 20,
    mass: 1,
    tension: 26,
    friction: 1.7
  },
  
  smooth: {
    stiffness: 150,
    damping: 15,
    mass: 1,
    tension: 40,
    friction: 1.5
  },
  
  snappy: {
    stiffness: 300,
    damping: 30,
    mass: 1,
    tension: 40,
    friction: 1
  },
  
  bouncy: {
    stiffness: 500,
    damping: 10,
    mass: 1,
    tension: 280,
    friction: 60
  }
} as const;
```

## Scroll Trigger Settings

```ts
// animations/scrollTrigger.ts
export const SCROLL_TRIGGERS = {
  hero: {
    trigger: 'auto',
    start: 'top center',
    end: 'bottom center',
    scrub: 1,
  },
  
  parallax: {
    trigger: 'auto',
    start: 'top bottom',
    end: 'top top',
    scrub: 0.5,
  },
  
  reveal: {
    trigger: 'auto',
    start: 'top 80%',
    end: 'top 30%',
    scrub: false,
  },
  
  pin: {
    trigger: 'auto',
    start: 'top top',
    end: 'bottom bottom',
    pin: true,
    scrub: 2,
  }
} as const;
```

## Stagger Patterns

```ts
// animations/stagger.ts
export const STAGGER_PATTERNS = {
  text: {
    container: { staggerChildren: 0.03, delayChildren: 0.2 },
    item: { opacity: [0, 1], y: [20, 0] }
  },
  
  list: {
    container: { staggerChildren: 0.1, delayChildren: 0.3 },
    item: { opacity: [0, 1], x: [50, 0] }
  },
  
  cards: {
    container: { staggerChildren: 0.15, delayChildren: 0 },
    item: { opacity: [0, 1], y: [100, 0] }
  },
  
  slide: {
    container: { staggerChildren: 0.08 },
    item: { clipPath: ['inset(0 100% 0 0)', 'inset(0 0% 0 0)'] }
  }
} as const;
```

## Performance Budgets

```ts
// animations/performance.ts
export const PERF_BUDGET = {
  targetFPS: 60,
  maxDuration: 2000,
  gpuProperties: [
    'transform',
    'opacity',
    'filter',
    'backdrop-filter'
  ],
  avoidProperties: [
    'width',
    'height',
    'left',
    'top',
    'margin',
    'padding'
  ]
} as const;
```

## Reduced Motion Fallbacks

```tsx
// hooks/useReducedMotion.ts
export function useReducedMotion() {
  const [prefersReduced, setPrefersReduced] = useState(false);
  
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReduced(mediaQuery.matches);
    
    const handler = (e) => setPrefersReduced(e.matches);
    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);
  
  return prefersReduced;
}

// Usage:
const prefersReduced = useReducedMotion();
const duration = prefersReduced ? 0 : DURATIONS.long;
```

## Animation Type Glossary

| Type | Duration | Easing | Use Case |
|------|----------|--------|----------|
| Fade | 0.4-0.6s | ease-out | Subtle reveals |
| Slide | 0.6-1.0s | ease-out-expo | Section transitions |
| Scale | 0.3-0.6s | ease-out-back | Card hovers |
| Rotate | 0.8-1.6s | linear | Product spins |
| Glow | 0.4-0.8s | ease-in-out | Accent highlights |
| Parallax | Scroll | linear | Depth creation |
| Counter | 2.0s | ease-out | Statistics |
| Stagger | Variable | ease-out | List reveals |

## Implementation Checklist

- [ ] All easing curves defined and tested
- [ ] Duration guidelines documented for both tiers
- [ ] Spring physics configs provided
- [ ] Scroll trigger presets ready
- [ ] Stagger patterns with examples
- [ ] Performance budgets established
- [ ] Reduced motion detection working
- [ ] Fallback animations for older browsers
- [ ] Animation performance monitored
- [ ] Library of 50+ animation combinations
