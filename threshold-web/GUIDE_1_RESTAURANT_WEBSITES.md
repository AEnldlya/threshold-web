# Guide 1: 10 Best Restaurant Websites — Design Patterns That Convert

## What Makes a Restaurant Website Work

A restaurant website does ONE job: get people in the door (or ordering online).

Here's what separates the good ones from the mediocre.

---

## Pattern #1: Hero Section with Immediate Trust Signals

**What works:**
- Large, mouth-watering food photo
- Restaurant name + tagline (e.g., "Farm-to-table Italian in downtown Boston")
- 3-4 obvious CTAs above the fold:
  - "Reserve a Table"
  - "Order Online"
  - "Call Now"
  - "View Menu"

**Why it works:**
- Visitor lands, immediately knows what you do
- No scrolling needed to understand who you are
- Multiple paths based on what they want to do

**Code pattern:**
```html
<section class="hero">
  <img src="food-photo.jpg" alt="Restaurant dish">
  <div class="hero-content">
    <h1>Mario's Italian Kitchen</h1>
    <p>Authentic Italian • Family-owned since 1990</p>
    <div class="cta-buttons">
      <a href="#booking" class="btn btn-primary">Reserve Table</a>
      <a href="#menu" class="btn btn-secondary">View Menu</a>
      <a href="tel:+1234567890" class="btn btn-tertiary">Call Now</a>
    </div>
  </div>
</section>
```

---

## Pattern #2: Trust Section (Reviews + Social Proof)

**What works:**
- 3-5 customer reviews with 5-star ratings
- Real names and photos (not stock photos)
- Short quotes: "Best pasta in the city!" ⭐⭐⭐⭐⭐
- Also show: Google review count, Yelp rating

**Why it works:**
- New customers want proof you're good
- Real reviews beat any marketing copy
- Shows other people trust you

**Real example section:**
```
⭐⭐⭐⭐⭐ "Incredible food, warm atmosphere. Been coming for 10 years." 
— John M., Google Reviews (847 reviews)

⭐⭐⭐⭐⭐ "Best carbonara outside of Rome. Worth the wait."
— Sarah T., Yelp

⭐⭐⭐⭐⭐ "Brought my parents for their anniversary. The owner came to our table. 
Perfect night."
— Mike H., Google Reviews
```

---

## Pattern #3: Menu Section (Easy to Scan)

**What works:**
- Menu organized by category (Appetizers, Mains, Desserts, Drinks)
- Simple text + prices, NOT fancy fonts
- 2-column layout on desktop, 1 column on mobile
- Highlight 3-5 "signature dishes" at the top
- NO heavy PDF downloads (people won't click)

**Why it works:**
- People want to know what to eat before arriving
- Easy scanning = more likely to come
- Signature dishes build hype

**Layout example:**
```
SIGNATURE DISHES
─────────────────
Grandmother's Lasagna ............................ $16
Hand-rolled pasta with slow-cooked meat sauce

Osso Buco ....................................... $24
Braised veal shanks with risotto

APPETIZERS
─────────────────
Calamari Fritti .................................. $12
Bruschetta ....................................... $10
Arancini ......................................... $9
```

---

## Pattern #4: Clear Reservation/Booking Flow

**What works:**
- "Reserve a Table" button visible on every page
- Opens a simple form (NOT external booking site):
  - Date
  - Time
  - Party size
  - Name
  - Phone
- Instant confirmation email
- Shows available times clearly

**Why it works:**
- Frictionless = more bookings
- People want quick confirmation, not bouncing to third-party sites
- Email confirmation builds trust

---

## Pattern #5: Location + Hours + Contact (Easy Access)

**What works:**
- Address, phone, hours prominently in header OR footer
- Google Map embedded below
- Hours clearly listed:
  ```
  Monday - Thursday: 11 AM - 10 PM
  Friday - Saturday: 11 AM - 11 PM
  Sunday: 12 PM - 9 PM
  ```
- "Call Now" button that's clickable on mobile

**Why it works:**
- People want to know right now: "Can I go tonight?"
- Clear hours = no frustrated customers
- Map proves you're a real place

---

## Pattern #6: High-Quality Food Photography

**What works:**
- 2-3 large food photos breaking up content
- Real photos (customers, your food, not stock)
- Captions under photos: "Daily special: Fresh-caught salmon"
- 70% of people visit restaurants BECAUSE of photos online

**Why it works:**
- People eat with their eyes first
- Good food photos are free marketing
- Creates desire

---

## Pattern #7: Simplicity in Design

**What works:**
- 2-3 colors max (pick your brand color + white/cream + one accent)
- Simple fonts: Arial, Helvetica, Georgia (readable on all devices)
- Lots of white space
- NO auto-playing music or videos
- NO animated backgrounds
- Fast loading (under 3 seconds)

**Why it fails:**
- Fancy animations = slower site = people leave
- Too many colors = unprofessional
- Auto-play video = annoying

**Color example:**
```
Primary: #C41E3A (nice red)
Background: #FFFFFF (white)
Accent: #2C3E50 (dark gray)
Text: #222222 (dark gray, readable)
```

---

## Pattern #8: Mobile-First Design

**What works:**
- Site looks perfect on phones (that's 70% of traffic)
- Buttons are large and easy to tap
- Menu collapses to a simple list
- "Call Now" button always visible
- No horizontal scrolling

**Why it works:**
- Most people find restaurants on their phone
- Tiny buttons = frustrated customers
- Mobile-friendly = Google ranks it higher

---

## Pattern #9: Special Events/Seasonal Info

**What works:**
- Clear section: "Happy Hour: Tues-Thurs 4-6 PM, $5 wines"
- "Valentine's Day: 7-course tasting menu available"
- "Private parties available—ask for details"
- Simple, easy to understand

**Why it works:**
- People want to plan special occasions
- Creates repeat visits (happy hour regulars)
- Shows you're active/current

---

## Pattern #10: Call-to-Action is Clear and Repeated

**What works:**
- Hero: "Reserve a Table" button
- After menu: "Ready to eat? Book now"
- At bottom: "Call for takeout: (617) 555-1234"
- Every page has 1-2 clear CTAs

**What doesn't work:**
- Hidden contact info
- Unclear buttons
- Too many choices (more than 3 CTAs)

---

## Real Example: What a Great Restaurant Site Has

```
Header
├── Logo
├── Navigation (Menu, Hours, Reservations, Contact)
└── "Reserve Now" button (always visible)

Hero Section
├── Food photo
├── Name + tagline
└── CTAs (Reserve, Order, Call)

About Section
├── 2-3 paragraphs about your story
├── Fun photos
└── Why customers love you

Menu Section
├── Organized by category
├── Signature dishes highlighted
└── NO PDFs (content on page)

Reviews Section
├── 5 real customer reviews
├── Star ratings
└── Google Maps rating embedded

Location/Hours
├── Address
├── Hours (clear)
├── Google Map
└── "Call Now" button

Footer
├── Contact info
├── Hours
├── Social links
└── "Reserve Now" link
```

---

## CSS You'll Need (Basic)

```css
/* Hero section - image as background */
.hero {
  background-image: url('food.jpg');
  background-size: cover;
  background-position: center;
  height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

/* Buttons - simple but effective */
.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary {
  background-color: #C41E3A;
  color: white;
}

.btn-primary:hover {
  background-color: #A01830;
}

/* Menu layout - cards for each item */
.menu-item {
  padding: 12px 0;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
}

.menu-item-name {
  font-weight: bold;
}

.menu-item-price {
  color: #C41E3A;
  font-weight: bold;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .hero {
    height: 300px;
  }
  
  .cta-buttons {
    flex-direction: column;
    gap: 10px;
  }
  
  .btn {
    width: 100%;
  }
}
```

---

## Quick Checklist for Your Restaurant Sites

- ☐ Hero section with food photo + clear CTA
- ☐ Trust section with 5+ real reviews
- ☐ Menu visible on page (not PDF)
- ☐ Simple reservation form
- ☐ Location, hours, phone visible
- ☐ 2-3 food photos throughout
- ☐ Simple, clean design (2-3 colors)
- ☐ Mobile-friendly (test on phone)
- ☐ Loading time under 3 seconds
- ☐ "Call Now" button on mobile
- ☐ Google Map embedded
- ☐ Social proof (Google reviews)

---

## What You Can Steal (For Your Sites)

✓ Hero photo + tagline pattern  
✓ Simple menu organization  
✓ Trust section with reviews  
✓ Clear CTAs repeated on each page  
✓ Mobile-first approach  
✓ Simple color scheme  
✓ Readable fonts  
✓ Plenty of white space  

Build this, and you'll have websites that restaurants will be happy to own and customers will actually use.
