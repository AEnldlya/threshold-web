# Layout Pattern Templates

## 12-Column CSS Grid (SaaS, Finance)

```tsx
// layouts/GridLayout.tsx
import styles from './GridLayout.module.css';

export function GridLayout({ children }) {
  return (
    <div className={styles.gridContainer}>
      {children}
    </div>
  );
}

// layouts/GridLayout.module.css
.gridContainer {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 1.5rem;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

@media (max-width: 768px) {
  .gridContainer {
    grid-template-columns: repeat(6, 1fr);
    gap: 1rem;
    padding: 0 1rem;
  }
}

@media (max-width: 480px) {
  .gridContainer {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0 1rem;
  }
}

/* Section padding */
.section {
  grid-column: 1 / -1;
  padding: 5rem 0;
}

.section:first-child {
  padding-top: 0;
}

@media (max-width: 768px) {
  .section {
    padding: 3rem 0;
  }
}

/* Content column (8 columns wide on desktop) */
.content {
  grid-column: 2 / 12;
}

@media (max-width: 768px) {
  .content {
    grid-column: 1 / -1;
  }
}

/* Sidebar (4 columns wide) */
.sidebar {
  grid-column: 1 / 5;
}

@media (max-width: 768px) {
  .sidebar {
    grid-column: 1 / -1;
    order: 2;
  }
}
```

## Bento Box / Card Grid (Tech, Portfolios)

```tsx
// layouts/BentoLayout.tsx
import styles from './BentoLayout.module.css';

export function BentoLayout({ cards }) {
  return (
    <div className={styles.bentoGrid}>
      {cards.map((card, i) => (
        <div 
          key={i}
          className={`${styles.bentoCard} ${styles[`card${i + 1}`]}`}
          style={{
            gridColumn: card.span?.col || 'span 1',
            gridRow: card.span?.row || 'span 1'
          }}
        >
          {card.content}
        </div>
      ))}
    </div>
  );
}

// layouts/BentoLayout.module.css
.bentoGrid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  max-width: 1280px;
  margin: 0 auto;
  padding: 3rem 1.5rem;
}

.bentoCard {
  padding: 2rem;
  border-radius: 8px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  transition: all 0.3s ease;
}

.bentoCard:hover {
  border-color: var(--color-accent);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}

/* Card span variants */
.card1 {
  grid-column: span 2;
  grid-row: span 2;
}

.card2 {
  grid-column: span 1;
  grid-row: span 2;
}

.card3 {
  grid-column: span 1;
  grid-row: span 1;
}

@media (max-width: 768px) {
  .bentoGrid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .card1,
  .card2,
  .card3 {
    grid-column: span 1 !important;
    grid-row: span 1 !important;
  }
}

@media (max-width: 480px) {
  .bentoGrid {
    grid-template-columns: 1fr;
  }
}
```

## Editorial Magazine Style (Luxury, Fashion, Creative)

```tsx
// layouts/EditorialLayout.tsx
import styles from './EditorialLayout.module.css';

export function EditorialLayout({ sections }) {
  return (
    <article className={styles.editorial}>
      {sections.map((section, i) => (
        <section key={i} className={styles.editorialSection}>
          <div className={styles.editorialGrid}>
            <div className={styles.text}>
              {section.text}
            </div>
            <div className={styles.image}>
              {section.image}
            </div>
          </div>
        </section>
      ))}
    </article>
  );
}

// layouts/EditorialLayout.module.css
.editorial {
  max-width: 1400px;
  margin: 0 auto;
}

.editorialSection {
  padding: 8rem 2rem;
  border-bottom: 1px solid var(--color-border);
}

.editorialSection:last-child {
  border-bottom: none;
}

.editorialGrid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.editorialGrid:nth-child(even) {
  direction: rtl;
}

.editorialGrid:nth-child(even) > * {
  direction: ltr;
}

.text {
  grid-column: 1;
}

.image {
  grid-column: 2;
  overflow: hidden;
  border-radius: 4px;
}

.text h2 {
  font-size: 3.5rem;
  line-height: 1;
  margin-bottom: 2rem;
  letter-spacing: -0.02em;
}

.text p {
  font-size: 1.125rem;
  line-height: 1.8;
  color: var(--color-text);
  margin-bottom: 1.5rem;
}

@media (max-width: 1024px) {
  .editorialGrid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .editorialGrid:nth-child(even) {
    direction: ltr;
  }
  
  .image {
    grid-column: 1;
  }
}

@media (max-width: 768px) {
  .editorialSection {
    padding: 3rem 1rem;
  }
  
  .text h2 {
    font-size: 2rem;
  }
}
```

## Brutalist Raw Grid (Agencies, Art)

```tsx
// layouts/BrutalistLayout.tsx
import styles from './BrutalistLayout.module.css';

export function BrutalistLayout({ items }) {
  return (
    <div className={styles.brutalistGrid}>
      {items.map((item, i) => (
        <div key={i} className={styles.brutalistItem}>
          {item}
        </div>
      ))}
    </div>
  );
}

// layouts/BrutalistLayout.module.css
.brutalistGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 0;
  margin: 0;
  padding: 0;
}

.brutalistItem {
  aspect-ratio: 1;
  border: 2px solid var(--color-text);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: var(--color-bg);
  position: relative;
}

.brutalistItem:nth-child(odd) {
  background: var(--color-surface);
}

.brutalistItem::before {
  content: attr(data-index);
  position: absolute;
  top: 0.5rem;
  left: 0.5rem;
  font-family: monospace;
  font-size: 0.75rem;
  opacity: 0.5;
}

@media (max-width: 768px) {
  .brutalistGrid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .brutalistGrid {
    grid-template-columns: 1fr;
  }
}
```

## Centered Narrow Column (Blogs, Education)

```tsx
// layouts/ArticleLayout.tsx
import styles from './ArticleLayout.module.css';

export function ArticleLayout({ children }) {
  return (
    <article className={styles.article}>
      {children}
    </article>
  );
}

// layouts/ArticleLayout.module.css
.article {
  max-width: 800px;
  margin: 0 auto;
  padding: 4rem 1.5rem;
  line-height: 1.8;
  color: var(--color-text);
}

.article h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.article h2 {
  font-size: 1.875rem;
  margin-top: 3rem;
  margin-bottom: 1rem;
  line-height: 1.3;
}

.article p {
  margin-bottom: 1.5rem;
  font-size: 1.0625rem;
}

.article ul,
.article ol {
  margin: 1.5rem 0 1.5rem 2rem;
}

.article li {
  margin-bottom: 0.5rem;
}

.article blockquote {
  border-left: 4px solid var(--color-accent);
  padding-left: 1.5rem;
  margin: 2rem 0;
  font-style: italic;
  color: var(--color-secondary);
}

.article img {
  max-width: 100%;
  height: auto;
  margin: 2rem 0;
  border-radius: 4px;
}

@media (max-width: 640px) {
  .article {
    padding: 2rem 1rem;
  }
  
  .article h1 {
    font-size: 1.875rem;
  }
  
  .article h2 {
    font-size: 1.5rem;
  }
}
```

## Full-Bleed Alternating (E-commerce, Marketing)

```tsx
// layouts/FullBleedLayout.tsx
import styles from './FullBleedLayout.module.css';

export function FullBleedLayout({ sections }) {
  return (
    <main className={styles.fullBleed}>
      {sections.map((section, i) => (
        <section 
          key={i} 
          className={`${styles.bleedSection} ${i % 2 ? styles.reverse : ''}`}
        >
          <div className={styles.content}>
            {section.content}
          </div>
          <div className={styles.media}>
            {section.media}
          </div>
        </section>
      ))}
    </main>
  );
}

// layouts/FullBleedLayout.module.css
.fullBleed {
  margin: 0;
  padding: 0;
}

.bleedSection {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
  align-items: center;
}

.bleedSection.reverse {
  direction: rtl;
}

.bleedSection.reverse > * {
  direction: ltr;
}

.content {
  padding: 4rem;
  grid-column: 1;
  background: var(--color-bg);
}

.media {
  grid-column: 2;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.media img,
.media video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.bleedSection:nth-child(even) .content {
  background: var(--color-surface);
}

@media (max-width: 1024px) {
  .bleedSection {
    grid-template-columns: 1fr;
    min-height: auto;
  }
  
  .bleedSection.reverse {
    direction: ltr;
  }
  
  .content {
    grid-column: 1;
    padding: 3rem 1.5rem;
  }
  
  .media {
    grid-column: 1;
    min-height: 400px;
  }
}

@media (max-width: 640px) {
  .content {
    padding: 2rem 1rem;
  }
}
```

## Overlapping Z-Index Layers (High-Impact Portfolios, Luxury)

```tsx
// layouts/OverlapLayout.tsx
import styles from './OverlapLayout.module.css';

export function OverlapLayout({ layers }) {
  return (
    <section className={styles.overlapSection}>
      {layers.map((layer, i) => (
        <div 
          key={i}
          className={styles.layer}
          style={{ 
            zIndex: i,
            transform: `translateY(${i * 60}px)`
          }}
        >
          {layer}
        </div>
      ))}
    </section>
  );
}

// layouts/OverlapLayout.module.css
.overlapSection {
  position: relative;
  padding: 8rem 2rem;
  min-height: 800px;
}

.layer {
  position: relative;
  padding: 3rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 8px;
  margin-bottom: -40px;
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  cursor: pointer;
}

.layer:hover {
  transform: translateY(-20px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.layer:last-child {
  margin-bottom: 0;
}

@media (max-width: 768px) {
  .overlapSection {
    padding: 3rem 1rem;
  }
  
  .layer {
    margin-bottom: -20px;
  }
}
```

## 8px Grid System

```css
/* Base spacing scale */
:root {
  --space-0: 0;
  --space-1: 0.5rem;   /* 8px */
  --space-2: 1rem;     /* 16px */
  --space-3: 1.5rem;   /* 24px */
  --space-4: 2rem;     /* 32px */
  --space-5: 2.5rem;   /* 40px */
  --space-6: 3rem;     /* 48px */
  --space-7: 4rem;     /* 64px */
  --space-8: 5rem;     /* 80px */
  --space-9: 6rem;     /* 96px */
  --space-10: 8rem;    /* 128px */
  --space-11: 10rem;   /* 160px */
  --space-12: 12rem;   /* 192px */
}

/* Section padding (for all layouts) */
.section {
  padding-top: var(--space-10);
  padding-bottom: var(--space-10);
}

@media (max-width: 768px) {
  .section {
    padding-top: var(--space-8);
    padding-bottom: var(--space-8);
  }
}

@media (max-width: 480px) {
  .section {
    padding-top: var(--space-6);
    padding-bottom: var(--space-6);
  }
}

/* Gap/margin scales */
.gap-1 { gap: var(--space-1); }
.gap-2 { gap: var(--space-2); }
.gap-3 { gap: var(--space-3); }
.gap-4 { gap: var(--space-4); }
.gap-6 { gap: var(--space-6); }
```

## Responsive Breakpoints

```ts
// constants/breakpoints.ts
export const BREAKPOINTS = {
  xs: 320,
  sm: 480,
  md: 768,
  lg: 1024,
  xl: 1280,
  '2xl': 1536
} as const;

export const QUERIES = {
  'sm': `(min-width: ${BREAKPOINTS.sm}px)`,
  'md': `(min-width: ${BREAKPOINTS.md}px)`,
  'lg': `(min-width: ${BREAKPOINTS.lg}px)`,
  'xl': `(min-width: ${BREAKPOINTS.xl}px)`,
  '2xl': `(min-width: ${BREAKPOINTS['2xl']}px)`
} as const;
```

## Implementation Checklist

- [ ] All 7 layout patterns documented
- [ ] Responsive breakpoints tested
- [ ] 8px grid system implemented
- [ ] Max-widths configured (1280px content, 1440px bleed)
- [ ] Padding/margin scales defined
- [ ] Mobile-first approach verified
- [ ] All patterns tested at 3+ breakpoints
- [ ] Performance benchmarks established
- [ ] Accessibility tested (reflow, zoom)
