# Website Making Playbook — Professional Framework

**Apply these patterns to EVERY website you build.**

---

## 1. DESIGN PATTERNS (What Works)

### Hero Section (First Thing People See)
```
✓ Large headline (32-64px)
✓ Subheading/tagline
✓ 1-2 clear CTAs (buttons)
✓ Professional background (gradient, image, or animated)
✓ Animated entrance (fade-in or slide-in)
```

**When to use:** Every homepage, every service page

### Trust Section (Prove You're Real)
```
✓ 3-5 customer reviews/testimonials
✓ Real names + photos
✓ Star ratings (⭐⭐⭐⭐⭐)
✓ Specific details ("saved $5K in first month")
✓ Hover animation (lift effect)
```

**When to use:** After hero (builds confidence)

### Product/Service Cards
```
✓ Title + description
✓ Hover effect (scale up + shadow)
✓ Icon or image
✓ Link/CTA button
✓ Consistent grid layout
```

**When to use:** Show products, services, features, team members

### Feature Grid (6 Items)
```
✓ Icon/emoji + title + description
✓ 2-3 columns on desktop, 1 on mobile
✓ Hover animation (lift or color change)
✓ Equal visual weight
✓ 250-300px cards
```

**When to use:** Why choose us, what makes us special

### Image Gallery
```
✓ Consistent aspect ratio (16:9 or square)
✓ Border + subtle shadow
✓ Hover zoom (transform: scale(1.1))
✓ Overlay text on hover
✓ Responsive grid
```

**When to use:** Portfolio, projects, achievements

### CTA Section (Call to Action)
```
✓ Bold headline
✓ Supporting text (benefit-focused)
✓ Primary button + secondary option
✓ Contrasting background color
✓ Center-aligned
```

**When to use:** Before footer, after major sections

---

## 2. ANIMATION PRINCIPLES (Make It Smooth)

### Fade-In (Subtle)
```css
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
/* Use on: Text, cards, sections on scroll */
/* Duration: 0.6-0.8s ease-out */
```

### Slide-In (Directional Entry)
```css
@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-50px); }
    to { opacity: 1; transform: translateX(0); }
}
/* Use on: Hero content, article text */
/* Duration: 0.8-1s ease-out */
```

### Scale-In (Growth Effect)
```css
@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.8); }
    to { opacity: 1; transform: scale(1); }
}
/* Use on: Feature cards, buttons, icons */
/* Duration: 0.6s ease-out */
```

### Hover Effects (Interactivity)
```css
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
}
/* Use on: Cards, buttons, links */
/* Duration: 0.3s (snappy response) */
```

### Parallax (Depth)
```javascript
window.addEventListener('scroll', () => {
    element.style.transform = `translateY(${scrollY * 0.5}px)`;
});
/* Use on: Hero background only (subtle) */
/* Don't overuse (slows page) */
```

### Key Animation Rules
- ✅ **Fast interactivity**: 0.3s for hover/click effects
- ✅ **Scroll animations**: 0.6-0.8s fade-in
- ✅ **Stagger grids**: Add 0.1s delay to each item
- ✅ **Smooth scroll**: `scroll-behavior: smooth;` on html
- ✅ **Avoid**: Spinning logos, auto-play videos, >1s animations

---

## 3. COLOR SCHEME (Professional Palette)

### The Formula
```
Primary Color (1 main): #00D9FF (cyan), #0366D6 (blue), #C41E3A (red)
Secondary Color (1 accent): #FF006E (magenta), #FFB800 (orange)
Dark Background: #0A0E27 or #050A15
Light Text: #E0E0E0 or #F0F0F0
Neutral Gray: #666 for secondary text
```

### Usage
```css
:root {
    --primary: #00D9FF;      /* Headers, buttons, highlights */
    --secondary: #FF006E;    /* Accents, hover states */
    --dark: #0A0E27;         /* Section backgrounds */
    --text: #E0E0E0;         /* Body text */
    --gray: #666;            /* Secondary text */
}
```

### Rules
- ✅ **2-3 colors max** (including white/dark)
- ✅ **High contrast** (text readable on background)
- ✅ **Gradient text** on headings (primary → secondary)
- ✅ **Consistent usage** (primary always for CTAs)
- ✅ **Test on mobile** (colors look different on screens)

---

## 4. TYPOGRAPHY (Readable & Professional)

### Font Stack
```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
}
```

### Font Sizes
```
H1 (Hero):     48-64px, font-weight: 900
H2 (Section):  32-42px, font-weight: 700
H3 (Card):     20-24px, font-weight: 600
Body:          14-16px, font-weight: 400
```

### Rules
- ✅ **Readable minimum**: 14px body text
- ✅ **System fonts fast**: Arial, Segoe UI, Geneva
- ✅ **Generous line-height**: 1.6 for body
- ✅ **Contrast**: Dark text on light, light on dark
- ✅ **No fancy fonts**: Avoid Comic Sans, impact fonts

---

## 5. LAYOUTS (Grid-Based)

### Container
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```

### Grid Patterns
```css
/* Cards (3-4 columns) */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
}

/* Mobile fallback */
@media (max-width: 768px) {
    .grid {
        grid-template-columns: 1fr;
    }
}
```

### Spacing (Consistent)
```
Padding: 20px (mobile), 40-60px (desktop)
Margin-bottom: 40px (sections), 30px (cards)
Gap: 20-30px (grids)
```

### Rules
- ✅ **Max-width 1200px** (don't make lines too long)
- ✅ **Mobile-first** (start with 1 column)
- ✅ **Consistent gaps** (all grids same spacing)
- ✅ **White space** (professional = generous padding)

---

## 6. RESPONSIVE DESIGN (Mobile First)

### Breakpoints
```css
/* Mobile: 320-768px (default, no query needed) */
/* Tablet: 768px */
@media (min-width: 768px) {
    .hero h1 { font-size: 48px; }
}

/* Desktop: 1024px+ */
@media (min-width: 1024px) {
    .hero h1 { font-size: 64px; }
}
```

### Mobile Checklist
- ☑ Buttons full-width or stacked
- ☑ Font sizes readable (14px+ for body)
- ☑ Touch targets 48px+ (fingers)
- ☑ No horizontal scroll
- ☑ Test on real device (not just browser)

---

## 7. IMAGES (Proper Handling)

### Image Tags
```html
<!-- DO THIS: -->
<img src="images/photo.jpg" alt="Descriptive text">

<!-- NOT THIS: -->
<div style="background: url(photo.jpg)"></div>

<!-- Video: -->
<video controls width="100%">
    <source src="video.mp4" type="video/mp4">
</video>
```

### Image Organization
```
/images
  /team
    - kastner-anderson.jpg
    - elizabeth-anderson.jpg
  /gallery
    - project-1.jpg
    - project-2.jpg
  /icons
    - feature-1.svg
```

### Rules
- ✅ **Optimized images** (compress before upload)
- ✅ **Descriptive alt text** (for accessibility)
- ✅ **Consistent aspect ratio** (16:9 for gallery)
- ✅ **Responsive sizes** (100% width, object-fit: cover)
- ✅ **Fallbacks** (onerror handler for missing images)

---

## 8. SITE STRUCTURE (Information Architecture)

### Standard Pages
```
index.html        → Home (hero + about + features + CTA)
team.html         → Team members with photos
products.html     → Products/services showcase
gallery.html      → Images, videos, portfolio
about.html        → About company, mission, values
contact.html      → Contact form, location
donate.html       → Support/funding page
```

### Page Layout (Every Page)
```
1. Navigation (sticky at top)
2. Hero section
3. Main content
4. CTA section
5. Footer
```

### Rules
- ✅ **Consistent navigation** (same on every page)
- ✅ **Clear hierarchy** (H1 once per page)
- ✅ **Logical flow** (sections build on each other)
- ✅ **Multiple CTAs** (hero + mid-page + footer)

---

## 9. PERFORMANCE (Speed Matters)

### Optimization
- ✅ **Pure HTML/CSS/JS** (no heavy frameworks)
- ✅ **Image compression** (use tools like TinyPNG)
- ✅ **Minimize animations** (don't animate everything)
- ✅ **Lazy load images** (load on scroll)
- ✅ **Remove unused CSS** (audit before deploy)

### Target
- **Load time**: <3 seconds
- **File size**: <500KB total
- **Lighthouse score**: 90+

---

## 10. DEPLOYMENT (Go Live)

### Netlify (Fastest)
```
1. Create folder with HTML/CSS/JS files
2. Go to app.netlify.com/drop
3. Drag & drop folder
4. Done in 30 seconds
```

### Custom Domain
```
1. Register domain (Namecheap, GoDaddy)
2. Netlify: Settings → Domain → Add custom domain
3. Point nameservers to Netlify
4. Wait 24-48 hours for DNS
```

### Version Control (GitHub)
```bash
git init
git add .
git commit -m "Initial website"
git push origin main
```

---

## 11. CHECKLIST (Before Launch)

### Design
- ☑ Colors tested on mobile
- ☑ Typography readable (14px+)
- ☑ Contrast sufficient (accessibility)
- ☑ No broken links
- ☑ Images load correctly

### Animation
- ☑ Animations smooth (60fps)
- ☑ No stuttering on scroll
- ☑ Parallax subtle (not distracting)
- ☑ Hover effects work on mobile (touch)

### Performance
- ☑ Load time <3 seconds
- ☑ No console errors
- ☑ Images optimized
- ☑ Mobile responsive

### Content
- ☑ Spelling/grammar checked
- ☑ Photos high quality
- ☑ CTAs clear and actionable
- ☑ Contact info visible

---

## 12. QUICK REFERENCE (Copy These)

### HTML Template (Every Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <!-- Logo + Links -->
    </nav>

    <!-- Hero -->
    <section class="hero">
        <h1>Headline</h1>
        <p>Subheading</p>
    </section>

    <!-- Content -->
    <section class="container">
        <h2>Section Title</h2>
        <!-- Cards, grid, text -->
    </section>

    <!-- CTA -->
    <section class="cta">
        <h2>Ready?</h2>
        <a href="#" class="btn">Action</a>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; Year Company. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

### CSS Template (Essential Styles)
```css
:root {
    --primary: #00D9FF;
    --secondary: #FF006E;
    --dark: #0A0E27;
    --text: #E0E0E0;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Segoe UI', sans-serif;
    background: var(--dark);
    color: var(--text);
    line-height: 1.6;
}

.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

.hero {
    min-height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.btn {
    padding: 12px 32px;
    border: 2px solid var(--primary);
    background: transparent;
    color: var(--primary);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.3s;
}

.btn:hover {
    background: var(--primary);
    color: var(--dark);
    transform: translateY(-3px);
}

@media (max-width: 768px) {
    .hero { min-height: 400px; }
    .btn { width: 100%; }
}
```

### JavaScript Template (Basic Animations)
```javascript
// Fade-in on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            observer.unobserve(entry.target);
        }
    });
});

document.querySelectorAll('.fade-in').forEach(el => {
    el.style.opacity = '0';
    observer.observe(el);
});

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Parallax
window.addEventListener('scroll', () => {
    const hero = document.querySelector('.hero');
    hero.style.transform = `translateY(${window.scrollY * 0.5}px)`;
});
```

---

## 13. INDUSTRY PATTERNS (Proven Winners)

### Restaurant Websites
- ✅ Food photos prominent
- ✅ Menu easy to find
- ✅ Reservation button above fold
- ✅ Hours + address visible
- ✅ Trust section with reviews

### Service Businesses (Plumber, Electrician)
- ✅ Phone number HUGE
- ✅ "Call Now" button sticky
- ✅ License/insurance visible
- ✅ Before/after portfolio
- ✅ Transparent pricing (no "call for quote")

### Portfolio/Creative
- ✅ Large imagery
- ✅ Minimal text
- ✅ Gallery foreground
- ✅ Project case studies
- ✅ Contact prominent

### SaaS/Software
- ✅ Problem statement hero
- ✅ Feature comparison table
- ✅ Customer logos/testimonials
- ✅ Pricing tiers
- ✅ Free trial CTA

---

## 14. COMMON MISTAKES (Avoid These)

❌ **Too many colors** (use 2-3 max)  
❌ **Auto-playing video** (kills conversions)  
❌ **Spinning animations** (looks unprofessional)  
❌ **Small fonts** (<14px unreadable)  
❌ **Hidden contact info** (people give up)  
❌ **Horizontal scroll** (mobile users hate)  
❌ **Heavy frameworks** (slow loading)  
❌ **Unoptimized images** (kills performance)  
❌ **No mobile view** (60% of traffic is mobile)  
❌ **Flickering animations** (bad performance)  

---

## 15. YOUR NEXT PROJECTS

**Apply this framework to:**

1. **Client websites** → Use patterns section
2. **Portfolios** → Use portfolio industry pattern
3. **Landing pages** → Use CTA section pattern
4. **E-commerce** → Use product card pattern
5. **Blogs** → Adapt for content-focused layout

**Template structure:**
1. Copy the HTML template
2. Use CSS template for base styles
3. Add custom colors for brand
4. Apply animations from library
5. Deploy to Netlify
6. Done in 4-6 hours

---

## 16. TESTING CHECKLIST (Every Site)

- ☑ **Desktop**: Chrome, Firefox, Safari
- ☑ **Mobile**: iPhone 12, Android (real devices)
- ☑ **Performance**: Lighthouse 90+
- ☑ **Accessibility**: WCAG AA standard
- ☑ **Links**: All internal + external work
- ☑ **Forms**: Submit + validation work
- ☑ **Loading**: <3 seconds
- ☑ **Mobile zoom**: Can zoom to 200%

---

## Summary

**Every professional website should have:**

1. ✅ **Clear hierarchy** (H1 > H2 > body text)
2. ✅ **Trust signals** (reviews, testimonials, credentials)
3. ✅ **Smooth animations** (fade/slide/hover, not spinning)
4. ✅ **Professional colors** (2-3 colors max, high contrast)
5. ✅ **Multiple CTAs** (hero + mid + footer)
6. ✅ **Mobile responsive** (1 column → 3 columns)
7. ✅ **Fast loading** (<3 seconds, <500KB)
8. ✅ **Good images** (optimized, consistent aspect ratio)
9. ✅ **Clear navigation** (same on every page)
10. ✅ **Easy deployment** (Netlify, GitHub, custom domain)

---

**This is your playbook. Use it for every project.**

Build it, test it, deploy it. Repeat.

