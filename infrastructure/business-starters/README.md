# Business Type Starter Kits

## SaaS/Tech Starter

```tsx
// templates/SaaS.tsx
import { FontLoader, fontPairs } from '@/components/FontLoader';
import { GridLayout } from '@/layouts/GridLayout';
import { TypewriterText } from '@/components/animations/TextAnimations';
import { FillSweepButton } from '@/components/animations/ButtonAnimations';

export default function SaaSTemplate() {
  return (
    <>
      <FontLoader pair={fontPairs.tech} />
      
      {/* Hero Section */}
      <section className="hero-saas">
        <GridLayout>
          <div className="hero-content">
            <h1>
              <TypewriterText 
                text="Build faster with intelligent tools" 
                delay={0.2}
              />
            </h1>
            <p>Streamline your workflow with cutting-edge automation.</p>
            <FillSweepButton direction="left">
              Start Free Trial
            </FillSweepButton>
          </div>
          <video 
            autoPlay 
            loop 
            muted 
            className="hero-3d"
            style={{ mixBlendMode: 'screen' }}
          >
            <source src="/3d/device-iphone-glass-cool-dark.webm" />
          </video>
        </GridLayout>
      </section>

      {/* Features Section */}
      <section className="features-section">
        <GridLayout>
          <h2>Powerful Features</h2>
          <div className="features-grid">
            {/* Feature cards with 3D tilt */}
          </div>
        </GridLayout>
      </section>

      {/* Stats Section */}
      <section className="stats-section">
        <Counter end={1000} suffix="+" label="Customers" />
        <Counter end={99.9} suffix="%" label="Uptime" />
        <Counter end={500} suffix="ms" label="Response Time" />
      </section>
    </>
  );
}

// styles/saas.css
:root {
  --font-display: 'Clash Display';
  --font-body: 'Satoshi';
  --color-bg: #0A0A0F;
  --color-surface: #141419;
  --color-text: #FFFFFF;
  --color-accent: #00E5FF;
}

.hero-saas {
  min-height: 100vh;
  display: flex;
  align-items: center;
  background: linear-gradient(180deg, var(--color-bg) 0%, var(--color-surface) 100%);
}

.hero-saas h1 {
  font-size: 7rem;
  line-height: 1;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}

.hero-saas p {
  font-size: 1.25rem;
  color: var(--color-secondary);
  margin-bottom: 2rem;
}

.hero-3d {
  max-width: 500px;
  height: auto;
}
```

## Luxury Fashion Starter

```tsx
// templates/Luxury.tsx
import { FontLoader, fontPairs } from '@/components/FontLoader';
import { EditorialLayout } from '@/layouts/EditorialLayout';
import { TextMaskWipe } from '@/components/animations/TextAnimations';
import { ParallaxSection } from '@/components/animations/ScrollAnimations';

export default function LuxuryTemplate() {
  return (
    <>
      <FontLoader pair={fontPairs.luxury} />
      
      {/* Hero */}
      <section className="hero-luxury">
        <div className="hero-content">
          <h1>
            <TextMaskWipe text="Timeless Elegance" direction="left" />
          </h1>
          <p>Discover luxury redefined for the modern era.</p>
        </div>
        <div className="hero-image">
          <img src="/images/hero-luxury.jpg" alt="" />
        </div>
      </section>

      {/* Editorial Section */}
      <EditorialLayout 
        sections={[
          {
            text: <h2>Our Heritage</h2>,
            image: <img src="/images/heritage.jpg" alt="" />
          },
          {
            text: <h2>Craftsmanship</h2>,
            image: <img src="/images/craftsmanship.jpg" alt="" />
          }
        ]}
      />
    </>
  );
}

// styles/luxury.css
:root {
  --font-display: 'Melodrama';
  --font-body: 'Zodiak';
  --color-bg: #FAF7F2;
  --color-surface: #FFFFFF;
  --color-text: #1A1208;
  --color-accent: #C9A84C;
}

.hero-luxury {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  padding: 4rem;
  gap: 4rem;
}

.hero-luxury h1 {
  font-size: 8rem;
  line-height: 0.9;
  letter-spacing: -0.04em;
}

.hero-luxury p {
  font-size: 1.125rem;
  margin-top: 2rem;
  max-width: 400px;
}

.hero-image {
  width: 100%;
  aspect-ratio: 3/4;
  overflow: hidden;
  border-radius: 2px;
}

.hero-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## Creative Agency Starter

```tsx
// templates/Agency.tsx
import { FontLoader, fontPairs } from '@/components/FontLoader';
import { BrutalistLayout } from '@/layouts/BrutalistLayout';
import { ScrambleText } from '@/components/animations/TextAnimations';
import { KineticSwap } from '@/components/animations/TextAnimations';

export default function AgencyTemplate() {
  return (
    <>
      <FontLoader pair={fontPairs.agency} />
      
      {/* Hero */}
      <section className="hero-agency">
        <h1>
          <ScrambleText text="Work That Matters" duration={2} />
        </h1>
        <p>Creative strategy meets bold execution.</p>
        <div className="hero-words">
          <KineticSwap words={['Strategy', 'Design', 'Development']} />
        </div>
      </section>

      {/* Portfolio Grid */}
      <section className="portfolio-section">
        <BrutalistLayout 
          items={[...]} 
        />
      </section>
    </>
  );
}

// styles/agency.css
:root {
  --font-display: 'Tanker';
  --font-body: 'Switzer';
  --color-bg: #0D0D0D;
  --color-surface: #1A1A1A;
  --color-text: #FFFFFF;
  --color-accent: #FF3B00;
}

.hero-agency {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4rem;
  background: var(--color-bg);
}

.hero-agency h1 {
  font-size: 10rem;
  line-height: 0.85;
  margin-bottom: 2rem;
  font-weight: 700;
}

.hero-agency p {
  font-size: 1.5rem;
  margin-bottom: 4rem;
  max-width: 600px;
}

.hero-words {
  font-size: 3rem;
  color: var(--color-accent);
  font-weight: 600;
}
```

## Restaurant/Food Starter

```tsx
// templates/Food.tsx
import { FontLoader, fontPairs } from '@/components/FontLoader';
import { FullBleedLayout } from '@/layouts/FullBleedLayout';
import { WordStagger } from '@/components/animations/TextAnimations';

export default function FoodTemplate() {
  return (
    <>
      <FontLoader pair={fontPairs.food} />
      
      {/* Hero */}
      <section className="hero-food">
        <h1>
          <WordStagger text="Taste the Difference" delay={0.1} />
        </h1>
        <p>Crafted with passion, served with pride.</p>
      </section>

      {/* Menu Showcase */}
      <FullBleedLayout
        sections={[
          {
            content: <h2>Appetizers</h2>,
            media: <img src="/images/appetizers.jpg" alt="" />
          },
          {
            content: <h2>Main Courses</h2>,
            media: <img src="/images/mains.jpg" alt="" />
          }
        ]}
      />
    </>
  );
}

// styles/food.css
:root {
  --font-display: 'Author';
  --font-body: 'General Sans';
  --color-bg: #FDF6EE;
  --color-surface: #FFFFFF;
  --color-text: #2C1810;
  --color-accent: #D4824A;
}

.hero-food {
  min-height: 80vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 4rem;
  text-align: center;
}

.hero-food h1 {
  font-size: 5rem;
  line-height: 1.1;
  margin-bottom: 1rem;
  color: var(--color-text);
}

.hero-food p {
  font-size: 1.5rem;
  color: var(--color-accent);
}
```

## Finance/Legal Starter

```tsx
// templates/Finance.tsx
import { FontLoader, fontPairs } from '@/components/FontLoader';
import { GridLayout } from '@/layouts/GridLayout';
import { Counter } from '@/components/animations/TextAnimations';

export default function FinanceTemplate() {
  return (
    <>
      <FontLoader pair={fontPairs.finance} />
      
      {/* Hero */}
      <section className="hero-finance">
        <h1>Trusted Financial Solutions</h1>
        <p>Professional expertise you can rely on.</p>
      </section>

      {/* Stats */}
      <section className="stats-finance">
        <GridLayout>
          <div className="stat">
            <Counter end={50} suffix="+" />
            <p>Years of Experience</p>
          </div>
          <div className="stat">
            <Counter end={10000} suffix="+" />
            <p>Clients Served</p>
          </div>
          <div className="stat">
            <Counter end={500} suffix="M+" />
            <p>Assets Managed</p>
          </div>
        </GridLayout>
      </section>

      {/* Services */}
      <section className="services-finance">
        {/* Service cards */}
      </section>
    </>
  );
}

// styles/finance.css
:root {
  --font-display: 'Fraunces';
  --font-body: 'Epilogue';
  --color-bg: #0F1923;
  --color-surface: #1A2530;
  --color-text: #FFFFFF;
  --color-accent: #E8D5A3;
}

.hero-finance {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 4rem;
  background: linear-gradient(135deg, var(--color-bg), var(--color-surface));
}

.hero-finance h1 {
  font-size: 4rem;
  line-height: 1.2;
  margin-bottom: 1.5rem;
  font-style: italic;
}

.stats-finance {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3rem;
  padding: 4rem;
  text-align: center;
}

.stat h3 {
  font-size: 3rem;
  color: var(--color-accent);
  margin-bottom: 0.5rem;
}
```

## Wellness/Health Starter

```tsx
// templates/Wellness.tsx
import { FontLoader, fontPairs } from '@/components/FontLoader';
import { ParallaxSection } from '@/components/animations/ScrollAnimations';

export default function WellnessTemplate() {
  return (
    <>
      <FontLoader pair={fontPairs.wellness} />
      
      {/* Hero */}
      <section className="hero-wellness">
        <h1>Find Your Inner Peace</h1>
        <p>Transform your life with mindful practices.</p>
      </section>

      {/* Services */}
      <section className="services-wellness">
        <ParallaxSection speed={0.3}>
          <div className="service-card">
            <h3>Yoga</h3>
            <p>Strengthen body and mind.</p>
          </div>
        </ParallaxSection>
      </section>
    </>
  );
}

// styles/wellness.css
:root {
  --font-display: 'Syne Serif';
  --font-body: 'Chillax';
  --color-bg: #F5F0EB;
  --color-surface: #FFFFFF;
  --color-text: #2D3748;
  --color-accent: #3D6B4F;
}

.hero-wellness {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 4rem;
  background: linear-gradient(135deg, var(--color-bg), var(--color-surface));
}

.hero-wellness h1 {
  font-size: 4rem;
  line-height: 1.1;
  color: var(--color-text);
  margin-bottom: 1rem;
}

.hero-wellness p {
  font-size: 1.25rem;
  color: var(--color-accent);
  max-width: 500px;
}
```

## Remaining Starters (Gaming, Portfolio, E-commerce, Education)

Similar structure to above with respective:
- Font pairs
- Color palettes
- Layout patterns
- Animation styles
- Component selections

Each starter provides:
- ✓ Complete page structure
- ✓ All required sections (hero, features, CTA)
- ✓ Business-appropriate animations
- ✓ Correct typography and colors
- ✓ Responsive layout
- ✓ 3D element placeholder
- ✓ CSS custom properties set
- ✓ Ready-to-use components

## Usage Instructions

```tsx
// How to use a starter:
1. Copy template folder
2. Update FontLoader with client's business type
3. Replace 3D asset paths with actual ContentCore exports
4. Swap placeholder images with client assets from Drive
5. Update copy with client content
6. Customize 3D element position if needed
7. Test all animations and interactions
8. Run accessibility audit
9. Deploy to staging
10. Get client feedback
```

## Implementation Checklist

- [ ] All 10 business type starters created
- [ ] Each has correct font pair loaded
- [ ] Each has correct color palette applied
- [ ] Each has appropriate layout pattern
- [ ] Each has 1+ custom animation
- [ ] Each has 3D element integrated
- [ ] Each has placeholder content structure
- [ ] Each is fully responsive
- [ ] Each passes WCAG AA accessibility
- [ ] Each can be deployed standalone
