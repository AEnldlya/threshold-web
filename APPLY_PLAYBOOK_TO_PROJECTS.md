# Apply the Playbook to Your Real Projects

**Use the Website Making Playbook for everything you build.**

---

## PROJECT 1: Boston Business Websites (167 Prospects)

### Your Customers: Restaurants, Plumbers, Electricians, Salons, Dentists

### Apply Pattern: SERVICE BUSINESSES

**From the Playbook:**
```
Service Businesses Pattern:
✓ Phone number HUGE
✓ "Call Now" button sticky
✓ License/insurance visible
✓ Before/after portfolio
✓ Transparent pricing
```

### Build Process (Use the Playbook)

**Step 1: HTML Structure**
```html
<!-- Copy from Playbook HTML Template -->
<!-- Customize for service business -->

<nav class="navbar">
    <!-- Navigation with phone number prominent -->
</nav>

<section class="hero">
    <h1>24/7 Emergency [Service Type]</h1>
    <p>Licensed • Insured • Fast Response</p>
    <a href="tel:..." class="btn btn-primary">Call Now</a>
</section>

<section class="container">
    <h2>Our Services</h2>
    <!-- Use Feature Grid pattern (6 cards) -->
</section>

<section class="products">
    <!-- Use Product Card pattern (portfolio/before-after) -->
</section>

<section class="cta">
    <h2>Ready to Get Started?</h2>
    <a href="#" class="btn">Book Appointment</a>
</section>
```

**Step 2: CSS (Use Playbook Template)**
```css
:root {
    --primary: #0366D6;        /* Professional blue */
    --secondary: #FF6B35;      /* Orange accent */
    --dark: #0A0E27;
    --text: #E0E0E0;
}

/* Copy from Playbook CSS Template */
/* Customize colors for business type */
```

**Step 3: Animations (Copy from Playbook)**
```javascript
/* Fade-in on scroll (hero) */
/* Slide-in for features */
/* Hover effects on cards */
/* Parallax on hero */

/* Copy exact code from JavaScript Template */
```

**Step 4: Images**
```
/images
  /portfolio
    - before-1.jpg
    - after-1.jpg
    - before-2.jpg
    - after-2.jpg
  /team
    - team-photo.jpg
```

**Step 5: Deploy**
```
1. Test on mobile (checklist from playbook)
2. Drag to Netlify
3. Done
```

---

## PROJECT 2: HapLink Multi-Page Redesign

### Apply Pattern: PORTFOLIO/CREATIVE

**From the Playbook:**
```
Portfolio Pattern:
✓ Large imagery
✓ Minimal text
✓ Gallery foreground
✓ Project case studies
✓ Contact prominent
```

### Build Process (Using Playbook)

**Step 1: Structure**
```html
<!-- Each page gets same template -->
<nav class="navbar">
    <!-- All 8 navigation tabs -->
</nav>

<section class="hero">
    <!-- Page-specific headline -->
</section>

<section class="container">
    <!-- Main content -->
    <!-- Use gallery pattern for images/videos -->
    <!-- Use card pattern for team/robot -->
</section>

<section class="cta">
    <!-- Call to action -->
</section>
```

**Step 2: Add Real Images**
```html
<!-- BEFORE (placeholder): -->
<div style="background: linear-gradient(...)">Photo</div>

<!-- AFTER (real images): -->
<img src="images/team-group.jpg" alt="2024-25 Team">
```

**Step 3: Gallery Pattern** (From Playbook)
```css
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
}

.gallery-item {
    border-radius: 12px;
    overflow: hidden;
    aspect-ratio: 16/9;
}

.gallery-item:hover {
    transform: scale(1.05);
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}
```

**Step 4: Team Cards** (From Playbook)
```html
<div class="team-member">
    <img src="images/kastner.jpg" alt="Kastner Anderson">
    <p>Kastner Anderson</p>
</div>
```

**Step 5: Deploy**
```
1. Test all pages on mobile
2. Verify animations smooth
3. Check image loading
4. Drag to Netlify
5. Live in 30 seconds
```

---

## PROJECT 3: Restaurant Website (Example)

### Using the Complete Playbook

**Step 1: Choose Colors**
```css
:root {
    --primary: #C41E3A;        /* Restaurant red */
    --secondary: #FFB800;      /* Warm gold */
    --dark: #1a1a1a;
    --text: #F0F0F0;
}
```

**Step 2: Content Sections** (From Playbook)

### Page Structure
```
1. HERO
   - Food photo background
   - Restaurant name
   - "Reserve Table" button

2. ABOUT
   - Story + mission
   - Team photo

3. MENU
   - Organized by category
   - Prices visible
   - Photos of signature dishes

4. REVIEWS/TRUST
   - 5+ Google reviews
   - Star ratings
   - Real customer names

5. GALLERY
   - Interior photos
   - Dish photography
   - Team/atmosphere

6. CTA
   - "Make a Reservation"
   - Big button

7. FOOTER
   - Address
   - Hours
   - Phone
```

**Step 3: Apply Animations**

From Playbook:
```javascript
// Hero: fade-in + slide-in
// Menu: flip-up cards
// Reviews: scale-in
// Gallery: zoom on hover
// CTA: fade-in with delay
```

**Step 4: Mobile Checklist** (From Playbook)
```
☑ Buttons full-width
☑ Font 14px+ readable
☑ Touch targets 48px
☑ No horizontal scroll
☑ Test on real iPhone
```

**Step 5: Deploy & Test**
```
✓ Lighthouse 90+
✓ <3 second load
✓ Mobile responsive
✓ All images load
✓ Links work
```

---

## QUICK REFERENCE: Apply to ANY Project

### 1. Pick Industry Pattern
```
Choose from Playbook:
- Service Business → Plumber, Electrician, HVAC
- Restaurant → Food photos, reservations
- Portfolio → Images foreground, minimal text
- SaaS → Problem, features, pricing
```

### 2. Copy HTML Template
```html
<!-- Use exact template from Playbook -->
<!-- Just customize headings + content -->
```

### 3. Pick Color Scheme
```css
/* Pick 2-3 colors that match industry */
/* Use :root variables like Playbook shows */
```

### 4. Add Animations
```javascript
/* Copy fade-in, slide-in, hover from Playbook */
/* Add parallax if appropriate */
/* Stagger grid items by 0.1s */
```

### 5. Add Images
```html
<!-- Replace placeholder divs with real <img> tags -->
<!-- Use /images folder structure -->
```

### 6. Follow Checklist
```
✓ Design checklist (colors, fonts, contrast)
✓ Animation checklist (smooth, no stuttering)
✓ Performance checklist (<3s load)
✓ Content checklist (spelling, photos, CTAs)
✓ Mobile checklist (responsive, touch targets)
```

### 7. Deploy
```
1. Test everything
2. Go to app.netlify.com/drop
3. Drag folder
4. Done
```

---

## Template Reuse Strategy

**Your 10-Minute Website Formula:**

```
1. Copy Playbook HTML Template (2 min)
2. Edit headings/content (3 min)
3. Copy Playbook CSS Template (1 min)
4. Pick 2-3 colors (1 min)
5. Copy Playbook JavaScript (1 min)
6. Add images (2 min)
7. Deploy to Netlify (1 min)
= ONE WEBSITE IN 10 MINUTES
```

---

## For the 167 Boston Businesses

### Website Template (Same for All)

**Customize:**
- Color (by industry)
- Images (their photos)
- Content (their info)
- CTA (their service)

**Stay the Same:**
- HTML structure
- CSS framework
- Animations
- Responsive layout
- Netlify deployment

### Example: Apply to 5 Different Businesses

**Restaurant:**
```
Colors: Red + Gold
Hero: Food photo + "Reserve Now"
Gallery: Dishes + atmosphere
CTA: Book Table
```

**Electrician:**
```
Colors: Blue + Orange
Hero: "24/7 Emergency" + Phone
Gallery: Before/after repairs
CTA: Schedule Service
```

**Salon:**
```
Colors: Pink + Teal
Hero: Hair photo + "Book Now"
Gallery: Before/after + team
CTA: Book Appointment
```

**Dentist:**
```
Colors: White + Blue
Hero: Smile photo + "New Patients"
Gallery: Before/after smiles + office
CTA: Schedule Checkup
```

**Plumber:**
```
Colors: Navy + Gold
Hero: "Emergency Service" + Phone
Gallery: Completed jobs
CTA: Call Now
```

**Same framework. Different colors + content.**

---

## Implementation Timeline

### Day 1
- ✓ Pick industry pattern
- ✓ Customize HTML template
- ✓ Pick colors
- ✓ Add content

### Day 2
- ✓ Add images
- ✓ Customize animations
- ✓ Mobile testing
- ✓ Deploy

### Scale to 167 Sites
- 10 min per site = 28 hours total
- = 3-4 sites per day
- = 50 sites per week
- = All 167 sites in 3-4 weeks

---

## Success Metrics (From Playbook)

### Design
- ✓ Colors tested on mobile
- ✓ Fonts readable (14px+)
- ✓ High contrast (accessible)

### Animation
- ✓ Smooth (60fps)
- ✓ No stuttering on scroll
- ✓ Parallax subtle

### Performance
- ✓ <3 second load
- ✓ No console errors
- ✓ Lighthouse 90+

### Content
- ✓ Spelling checked
- ✓ Photos high quality
- ✓ CTAs clear

### Mobile
- ✓ Responsive layout
- ✓ Touch targets 48px
- ✓ No horizontal scroll

---

## The Playbook is Your Starting Point

**EVERY PROJECT:**

1. Open `WEBSITE_MAKING_PLAYBOOK.md`
2. Pick your industry pattern
3. Copy the template code
4. Customize colors + content
5. Add images
6. Deploy

**You have a framework. Use it.**

---

## Resources (Everything You Need)

**In `/home/clawdbot/.openclaw/workspace/`:**

- `WEBSITE_MAKING_PLAYBOOK.md` ← Start here (14K words)
- `haplink-multipage/` ← Real example (8 pages)
- `FREE_DEMO_EMAIL_TEMPLATES.md` ← Email copy
- `QUICK_BUILD_REFERENCE.md` ← Code copy-paste

**That's everything. Everything else is details.**

---

## Apply This Today

**Pick ONE project and build it:**

Option 1: **HapLink** (multi-page, real client)
Option 2: **Boston business website** (service industry)
Option 3: **Your portfolio** (example for clients)

Use the playbook. Build in 1 day. Deploy to Netlify. Done.

**Repeat for next 166 businesses.**

