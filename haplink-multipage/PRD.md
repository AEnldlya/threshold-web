# HapLink Product Requirements Document (PRD)

## Executive Summary

**Product Name**: HapLink - Happy Haptic Doctors (Team 26532)  
**Type**: FIRST Tech Challenge Robotics Team Website  
**Purpose**: Showcase robotics achievements, innovation project, and team journey  
**Target Audience**: Judges, sponsors, potential team members, robotics community  

---

## 1. Product Overview

### 1.1 Mission Statement
HapLink represents Team 26532 "Happy Haptic Doctors" - a FIRST Tech Challenge robotics team bringing haptic technology innovation to life. The website serves as a digital portfolio documenting their journey from First Lego League to World Championship competitors.

### 1.2 Core Value Proposition
- **Innovation**: Haptic vest and hoodie products for immersive entertainment experiences
- **Achievement**: State champions, #1 rookie team, World Championship qualifiers
- **Community**: Making premium entertainment accessible and affordable
- **Education**: STEM learning through competitive robotics

### 1.3 Target Users
| User Type | Needs | Goals |
|-----------|-------|-------|
| FTC Judges | Innovation documentation, team history, impact | Award evaluation |
| Sponsors | Team credibility, ROI visibility, brand association | Partnership decisions |
| Prospective Members | Team culture, learning opportunities, achievements | Join decision |
| Robotics Community | Technical inspiration, best practices, networking | Knowledge sharing |
| General Public | Understanding haptic technology, entertainment value | Awareness |

---

## 2. Website Architecture

### 2.1 Site Structure (8 Pages)

```
Home (index.html)
├── Hero Section
├── About HapLink
├── Products (Haptic Vest & Hoodie)
├── Features
└── CTA

Team (team.html)
├── 2024-2025 Members (8 students)
└── Coaches (2 mentors)

Robot Design (robot.html)
├── Design Philosophy
├── Advanced Systems
└── Hardware Gallery (3 images)

2023 FLL (2023-fll.html)
├── FLL History
├── Gallery (5 competition images)
└── Achievement Highlights

2024 Worlds (2024-worlds.html)
├── World Championship Journey
├── Gallery (6 championship images)
└── Global Partnerships

2024 Highlights (2024-highlights.html)
├── Season Overview
└── Gallery (5 event images)

2025 Season (2025.html)
├── Upcoming Season Preview
├── Development Updates
└── Gallery (5 preparation images)

Donate (donate.html)
├── Fundraising Goals
├── Sponsorship Tiers
├── Impact Statement
└── Donation Methods
```

### 2.2 Navigation Structure
**Primary Navigation** (Sticky Header):
- Home
- Our Team
- Robot Design
- 2023 FLL
- 2024 Worlds
- 2024 Highlights
- 2025
- Donate (CTA Button)

**Footer Navigation**:
- Copyright
- FIRST Tech Challenge branding
- Quick links

---

## 3. Visual Design System

### 3.1 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Primary (Cyan) | `#00D9FF` | CTAs, links, accents, highlights |
| Secondary (Magenta) | `#FF006E` | Gradients, hover states, emphasis |
| Dark Background | `#0A0E27` | Main background |
| Darker Background | `#050A15` | Deep sections, overlays |
| Light Text | `#F0F0F0` | Primary text |
| Body Text | `#E0E0E0` | Secondary text |

**Gradient Patterns**:
- Hero: `linear-gradient(135deg, rgba(0, 217, 255, 0.1), rgba(255, 0, 110, 0.1))`
- Cards: Subtle dark gradients with cyan border glow
- Buttons: Transparent with cyan border, fill on hover

### 3.2 Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Logo | System Sans | 24px | Bold (900) |
| H1 (Hero) | System Sans | 64px | Black (900) |
| H2 (Section) | System Sans | 36-48px | Bold (700) |
| H3 (Card) | System Sans | 24px | Semi-bold (600) |
| Body | System Sans | 16-18px | Regular (400) |
| Caption | System Sans | 14px | Regular (400) |

**Text Effects**:
- Gradient text: `linear-gradient(135deg, #00D9FF, #FF006E)` with background-clip
- Letter spacing: -1px for headings, 2px for logo

### 3.3 Spacing & Layout

**Container**: Max-width 1200px, centered  
**Section Padding**: 80px vertical (desktop), 40px (mobile)  
**Grid Gaps**: 30-40px between cards  
**Border Radius**: 6px (buttons), 8px (cards), 12px (images)  

**Responsive Breakpoints**:
- Desktop: 1200px+
- Tablet: 768px - 1199px
- Mobile: < 768px

---

## 4. Page Specifications

### 4.1 Home Page (index.html)

**Hero Section**:
- Full-width background image (team photo)
- Dark overlay for text contrast
- Animated headline: "HapLink"
- Subtitle: "Happy Haptic Doctors - Team 26532"
- Tagline: "Bringing haptic technology to life"
- Two CTAs: "Learn More" (primary), "See Our Work" (secondary)
- Floating gradient orbs (animated)

**About Section**:
- 3-column grid (responsive to 1-column mobile)
- Cards: "Who We Are", "Our Innovation", "Our Mission"
- Slide-in animations on scroll

**Products Section**:
- 2-column grid for Haptic Vest & Hoodie
- Product images with hover scale effect
- Price comparison context ($1,011 vs affordable)
- Value proposition text

**Features Section**:
- 4-column grid (2x2 on tablet, 1x4 on mobile)
- Icons: Haptic Sensing, Sound Reactive, Heartbeat Sync, Haptic Linking
- Scale-in animations

**CTA Section**:
- Full-width dark background
- "Ready to Experience the Future?"
- Two buttons: "Meet the Team", "Support Us"

### 4.2 Team Page (team.html)

**Hero**: Team photo background

**Team Grid**:
- 4-column grid (2 on tablet, 1 on mobile)
- 8 team member cards with photos
- Circular image masks
- Names below photos
- Scale-in staggered animations

**Coaches Section**:
- 2-column grid
- 2 coach cards with photos
- Separator line above section

### 4.3 Robot Design Page (robot.html)

**Hero**: Robot/engineering themed

**Content**:
- 2-column grid: Design Philosophy + Advanced Systems
- Hardware Gallery: 3 images in grid
- Image overlay with text on hover

### 4.4 History Pages (2023-fll, 2024-worlds, 2024-highlights, 2025)

**Structure**:
- Hero with relevant background
- Text content section
- Image gallery (5-6 images)
- Masonry or uniform grid layout
- Lightbox optional for image viewing

### 4.5 Donate Page (donate.html)

**Content**:
- Fundraising goals and progress
- Sponsorship tier cards (Bronze, Silver, Gold)
- Impact statement
- Multiple donation methods
- Contact for corporate sponsorship

---

## 5. Image Assets

### 5.1 Image Inventory (15+ Unique Images)

**Team Member Photos** (10):
- Kastner Anderson
- Elizabeth Anderson
- Jacob Hannan
- Grayson Lyall
- Owen Osterberg
- Alan Zhang
- Andy Zhang
- Ella Zhang
- Erich Osterberg (Coach)
- Yu Zhang (Coach)

**Product/Innovation Images** (4):
- Haptic Vest showcase
- Haptic Hoodie wearable
- Innovation project close-up
- Haptic technology demonstration

**Event/Competition Images** (7):
- States competition
- World Championship arena
- Robot build process
- Team victory moments
- Partnership/sponsor events
- 2025 team preparation

**Hero Backgrounds** (4):
- Home: Team group photo
- 2023 FLL: States picture
- 2024 Worlds: Championship venue
- 2025: New team photo

### 5.2 Image Specifications

| Type | Format | Optimization | Source |
|------|--------|--------------|--------|
| Hero backgrounds | JPG | 1920x1080, compressed | haplink.net |
| Team photos | JPG/PNG | 400x400, face-centered | haplink.net |
| Product images | JPG | 800x600, high quality | haplink.net |
| Gallery images | JPG | 1200x800, progressive | haplink.net |

**Image URLs**: All hosted on `https://haplink.net/wp-content/uploads/`

---

## 6. Animations & Interactions

### 6.1 Global Animations

| Animation | Trigger | Duration | Easing |
|-----------|---------|----------|--------|
| Header slide-down | Page load | 0.6s | ease-out |
| Hero fade-in-up | Page load | 1s | ease-out |
| Floating orbs | Continuous | 6-8s | ease-in-out |
| Scroll reveal | Scroll into view | 0.6s | ease-out |
| Card hover lift | Hover | 0.3s | ease |
| Button glow | Hover | 0.3s | ease |
| Image scale | Hover | 0.5s | ease |

### 6.2 Scroll Animations

**Slide-in-left**:
- Transform: translateX(-50px) → translateX(0)
- Opacity: 0 → 1
- Duration: 0.6s

**Slide-in-right**:
- Transform: translateX(50px) → translateX(0)
- Opacity: 0 → 1
- Duration: 0.6s

**Scale-in**:
- Transform: scale(0.9) → scale(1)
- Opacity: 0 → 1
- Duration: 0.5s
- Stagger: 0.1s between items

**Fade-in**:
- Opacity: 0 → 1
- Transform: translateY(20px) → translateY(0)
- Duration: 0.6s

### 6.3 Hover Effects

**Buttons**:
- Background: transparent → cyan
- Color: cyan → dark
- Transform: translateY(-2px)
- Box-shadow: 0 4px 12px rgba(0, 217, 255, 0.3)

**Cards**:
- Border: subtle → cyan glow
- Transform: translateY(-5px)
- Transition: 0.3s

**Images**:
- Transform: scale(1) → scale(1.05)
- Duration: 0.5s

**Navigation Links**:
- Background: transparent → cyan
- Color: light → dark
- Border-radius: 4px

---

## 7. Technical Requirements

### 7.1 Technology Stack

- **HTML5**: Semantic markup
- **CSS3**: Custom properties, Grid, Flexbox, Animations
- **JavaScript**: Vanilla JS for interactions
- **No Framework**: Pure HTML/CSS/JS for fast loading
- **No Build Step**: Direct file serving

### 7.2 Performance Requirements

| Metric | Target |
|--------|--------|
| First Contentful Paint | < 1.5s |
| Largest Contentful Paint | < 2.5s |
| Time to Interactive | < 3.5s |
| Cumulative Layout Shift | < 0.1 |
| Page Size | < 500KB per page |

**Optimizations**:
- Lazy loading for images below fold
- Compressed images (JPEG quality 80%)
- Minified CSS/JS (optional)
- CDN hosting for images

### 7.3 Browser Support

| Browser | Support |
|---------|---------|
| Chrome | Latest 2 versions |
| Firefox | Latest 2 versions |
| Safari | Latest 2 versions |
| Edge | Latest 2 versions |
| Mobile Safari | iOS 14+ |
| Chrome Mobile | Android 10+ |

### 7.4 Accessibility (WCAG 2.1 AA)

- Color contrast ratio: 4.5:1 minimum
- Keyboard navigation support
- Alt text for all images
- Focus indicators on interactive elements
- Semantic HTML structure
- ARIA labels where needed

---

## 8. Content Requirements

### 8.1 Copywriting Guidelines

**Tone**: Professional yet enthusiastic, technical but accessible  
**Voice**: First-person plural ("we", "our team")  
**Tense**: Present for current, past for history  

**Key Messages**:
1. Innovation in haptic technology
2. Championship-level robotics
3. Making entertainment accessible
4. STEM education and growth
5. Community impact

### 8.2 SEO Requirements

| Element | Requirement |
|---------|-------------|
| Title tags | Unique per page, 50-60 chars |
| Meta descriptions | 150-160 chars, include keywords |
| Header hierarchy | Single H1, logical H2-H6 |
| Image alt text | Descriptive, keyword-rich |
| URL structure | Clean, hyphenated, lowercase |
| Schema markup | Organization, Event (optional) |

**Keywords**: FIRST Tech Challenge, robotics team, haptic technology, innovation project, Team 26532, Happy Haptic Doctors

---

## 9. Deployment & Hosting

### 9.1 Hosting Requirements

- **Platform**: Netlify (recommended) or GitHub Pages
- **Domain**: Custom domain (haplink.net) or subdomain
- **SSL**: HTTPS required
- **CDN**: Image optimization and global delivery

### 9.2 Deployment Process

1. Build static files (no build step needed)
2. Upload to hosting platform
3. Configure custom domain
4. Enable SSL certificate
5. Test all pages and links
6. Verify image loading
7. Performance testing

### 9.3 Maintenance

**Regular Updates**:
- Season updates (new achievements)
- Team roster changes
- New competition photos
- Sponsor acknowledgments

**Backup Strategy**:
- Git repository for code
- Image backups from haplink.net
- Version control for changes

---

## 10. Success Metrics

### 10.1 KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Page load time | < 3s | Lighthouse |
| Mobile responsiveness | 100 | Lighthouse |
| Accessibility score | 90+ | Lighthouse |
| SEO score | 90+ | Lighthouse |
| Uptime | 99.9% | Hosting monitor |

### 10.2 Business Goals

- **Awards**: Support judge evaluation for Innovation and Connect awards
- **Sponsors**: Convert 2+ website visitors to sponsors per season
- **Recruitment**: 3+ prospective members contact team annually
- **Community**: 1000+ annual visitors

---

## 11. Future Enhancements

### 11.1 Phase 2 Features

- [ ] Blog/News section for updates
- [ ] Video integration (robot reveal, match highlights)
- [ ] Interactive robot 3D model
- [ ] Live competition updates
- [ ] Sponsor portal
- [ ] Team application form

### 11.2 Technical Improvements

- [ ] PWA capabilities (offline viewing)
- [ ] Dark/light theme toggle
- [ ] Multi-language support
- [ ] Advanced analytics
- [ ] CMS integration for easy updates

---

## 12. Appendix

### 12.1 File Structure

```
haplink-multipage/
├── index.html              # Home page
├── team.html               # Team members
├── robot.html              # Robot design
├── 2023-fll.html          # FLL history
├── 2024-worlds.html       # World championship
├── 2024-highlights.html   # Season highlights
├── 2025.html              # Upcoming season
├── donate.html            # Fundraising
├── styles.css             # Global styles
├── script.js              # Interactions
└── [documentation files]
```

### 12.2 External Dependencies

- Images: `https://haplink.net/wp-content/uploads/`
- Fonts: System fonts (no external font loading)
- Icons: None (text-based or CSS)
- Analytics: Optional (Google Analytics)

### 12.3 Contact Information

**Team**: Happy Haptic Doctors - Team 26532  
**Program**: FIRST Tech Challenge  
**Location**: Hanover, New Hampshire  
**Website**: https://haplink.net

---

**Document Version**: 1.0  
**Last Updated**: March 15, 2026  
**Status**: Production Ready  
**Author**: OpenClaw Agent
