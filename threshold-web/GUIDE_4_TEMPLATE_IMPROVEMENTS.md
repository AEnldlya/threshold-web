# Guide 4: Improved Website Templates — Apply Everything You Learned

## How to Use These 3 Guides to Build Better Sites

The learning is in the patterns. Here's how to actually apply them.

---

## The Template Formula

Every professional website follows this structure:

```
1. HERO (Get attention + CTA)
2. TRUST (Prove you're real)
3. SERVICES (Show what you do)
4. SOCIAL PROOF (Reviews/testimonials)
5. CTA (Make it easy to act)
6. FOOTER (Backup contact info)
```

---

## Restaurant Site Template (Building It)

### Step 1: Create Hero Section

**HTML:**
```html
<header class="hero">
  <img src="food-hero.jpg" alt="Restaurant dish" class="hero-img">
  <div class="hero-content">
    <h1>Mario's Italian Kitchen</h1>
    <p class="tagline">Authentic Italian • Since 1990</p>
    <div class="cta-buttons">
      <a href="#booking" class="btn btn-primary">Reserve a Table</a>
      <a href="#menu" class="btn btn-secondary">View Menu</a>
      <a href="tel:+16175551234" class="btn btn-tertiary">Call Now</a>
    </div>
  </div>
</header>
```

**CSS:**
```css
.hero {
  position: relative;
  height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.hero-img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}

.hero-content {
  text-align: center;
  color: white;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.hero-content h1 {
  font-size: 48px;
  margin-bottom: 10px;
}

.tagline {
  font-size: 20px;
  margin-bottom: 30px;
}

.cta-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
}

/* Buttons with hover effects */
.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s;
  text-decoration: none;
  display: inline-block;
}

.btn-primary {
  background: #C41E3A;
  color: white;
}

.btn-primary:hover {
  background: #A01830;
  transform: scale(1.02);
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}

.btn-secondary {
  background: white;
  color: #333;
}

.btn-secondary:hover {
  background: #f0f0f0;
  transform: scale(1.02);
}

/* Mobile */
@media (max-width: 768px) {
  .hero {
    height: 300px;
  }
  
  .hero-content h1 {
    font-size: 32px;
  }
  
  .cta-buttons {
    flex-direction: column;
  }
  
  .btn {
    width: 100%;
  }
}
```

### Step 2: Add Trust Section

**HTML:**
```html
<section class="trust-section fade-in">
  <h2>Loved by Boston</h2>
  <div class="reviews-grid">
    <div class="review-card">
      <div class="stars">⭐⭐⭐⭐⭐</div>
      <p class="review-text">"Best pasta in the city. Been coming for 10 years."</p>
      <p class="review-author">— John M., Google Reviews</p>
    </div>
    
    <div class="review-card">
      <div class="stars">⭐⭐⭐⭐⭐</div>
      <p class="review-text">"Warm atmosphere, excellent service, worth every penny."</p>
      <p class="review-author">— Sarah T., Yelp</p>
    </div>
    
    <div class="review-card">
      <div class="stars">⭐⭐⭐⭐⭐</div>
      <p class="review-text">"Perfect for date nights. The owner remembers regulars."</p>
      <p class="review-author">— Mike H., Google Reviews</p>
    </div>
  </div>
  <p class="review-count">847 reviews on Google • 4.9 rating</p>
</section>
```

**CSS:**
```css
.trust-section {
  background: #f9f9f9;
  padding: 60px 20px;
  text-align: center;
}

.trust-section h2 {
  font-size: 36px;
  margin-bottom: 40px;
  color: #333;
}

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  max-width: 1000px;
  margin: 0 auto 30px;
}

.review-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.3s;
}

.review-card:hover {
  box-shadow: 0 8px 16px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}

.stars {
  font-size: 18px;
  margin-bottom: 10px;
}

.review-text {
  font-size: 14px;
  color: #555;
  margin-bottom: 10px;
  font-style: italic;
}

.review-author {
  font-size: 12px;
  color: #999;
  font-weight: bold;
}

.review-count {
  color: #999;
  font-size: 14px;
}

/* Fade-in animation */
.fade-in {
  opacity: 0;
  transition: opacity 1s ease-in;
}

.fade-in.in-view {
  opacity: 1;
}
```

### Step 3: Menu Section

**HTML:**
```html
<section class="menu-section" id="menu">
  <h2>Our Menu</h2>
  
  <div class="menu-category">
    <h3>Signature Dishes</h3>
    <div class="menu-items">
      <div class="menu-item">
        <div class="menu-name">Grandmother's Lasagna</div>
        <div class="menu-description">Hand-rolled pasta with slow-cooked meat sauce</div>
        <div class="menu-price">$16</div>
      </div>
      <div class="menu-item">
        <div class="menu-name">Osso Buco</div>
        <div class="menu-description">Braised veal shanks with risotto</div>
        <div class="menu-price">$24</div>
      </div>
    </div>
  </div>
  
  <div class="menu-category">
    <h3>Appetizers</h3>
    <div class="menu-items">
      <div class="menu-item">
        <div class="menu-name">Calamari Fritti</div>
        <div class="menu-price">$12</div>
      </div>
      <div class="menu-item">
        <div class="menu-name">Bruschetta</div>
        <div class="menu-price">$10</div>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.menu-section {
  padding: 60px 20px;
  max-width: 800px;
  margin: 0 auto;
}

.menu-section h2 {
  text-align: center;
  font-size: 36px;
  margin-bottom: 40px;
}

.menu-category {
  margin-bottom: 40px;
}

.menu-category h3 {
  font-size: 20px;
  color: #C41E3A;
  border-bottom: 2px solid #C41E3A;
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.menu-items {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.menu-item {
  padding: 15px 0;
  border-bottom: 1px solid #eee;
}

.menu-item:last-child {
  border-bottom: none;
}

.menu-name {
  font-weight: bold;
  font-size: 16px;
  color: #333;
  margin-bottom: 5px;
}

.menu-description {
  font-size: 13px;
  color: #666;
  margin-bottom: 8px;
  font-style: italic;
}

.menu-price {
  color: #C41E3A;
  font-weight: bold;
  font-size: 16px;
}
```

### Step 4: Booking Section

**HTML:**
```html
<section class="booking-section" id="booking">
  <h2>Reserve a Table</h2>
  <form class="booking-form">
    <input type="date" name="date" required placeholder="Select Date">
    <input type="time" name="time" required placeholder="Select Time">
    <input type="number" name="guests" required placeholder="Number of Guests" min="1" max="20">
    <input type="text" name="name" required placeholder="Your Name">
    <input type="tel" name="phone" required placeholder="Phone Number">
    <button type="submit" class="btn btn-primary">Book Now</button>
  </form>
</section>
```

**CSS:**
```css
.booking-section {
  background: #f9f9f9;
  padding: 60px 20px;
  text-align: center;
}

.booking-section h2 {
  font-size: 32px;
  margin-bottom: 30px;
}

.booking-form {
  max-width: 500px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.booking-form input {
  padding: 12px;
  border: 2px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  transition: border-color 0.3s;
}

.booking-form input:focus {
  outline: none;
  border-color: #C41E3A;
  box-shadow: 0 0 5px rgba(196,30,58,0.3);
}

.booking-form button {
  padding: 12px;
  background: #C41E3A;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s;
}

.booking-form button:hover {
  background: #A01830;
  transform: scale(1.02);
}
```

### Step 5: Footer with Contact Info

**HTML:**
```html
<footer class="footer">
  <div class="footer-content">
    <div class="footer-section">
      <h3>Contact</h3>
      <p>📞 (617) 555-1234</p>
      <p>📍 123 Boston Street, Boston, MA</p>
    </div>
    <div class="footer-section">
      <h3>Hours</h3>
      <p>Mon-Thu: 11 AM - 10 PM</p>
      <p>Fri-Sat: 11 AM - 11 PM</p>
      <p>Sun: 12 PM - 9 PM</p>
    </div>
    <div class="footer-section">
      <h3>Follow</h3>
      <p>
        <a href="#">Facebook</a> | 
        <a href="#">Instagram</a>
      </p>
    </div>
  </div>
  <p class="footer-credit">© 2024 Mario's Italian Kitchen. All rights reserved.</p>
</footer>
```

**CSS:**
```css
.footer {
  background: #333;
  color: white;
  padding: 40px 20px;
  text-align: center;
}

.footer-content {
  max-width: 1000px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.footer-section h3 {
  margin-bottom: 10px;
}

.footer-section p {
  margin: 5px 0;
  font-size: 14px;
}

.footer-section a {
  color: #C41E3A;
  text-decoration: none;
}

.footer-section a:hover {
  text-decoration: underline;
}

.footer-credit {
  border-top: 1px solid #555;
  padding-top: 20px;
  font-size: 12px;
  color: #999;
}
```

---

## Service Site Template (Electrician/Plumber)

### Quick Template Structure

**HTML:**
```html
<!-- Sticky phone banner -->
<div class="phone-banner">
  <a href="tel:+16175551234">📞 (617) 555-1234 — Call Now</a>
</div>

<!-- Hero -->
<header class="hero">
  <h1>24/7 Emergency Electrical Service</h1>
  <p>Licensed • Insured • Same-Day Service</p>
  <a href="#booking" class="btn btn-large">Schedule Service</a>
</header>

<!-- Services -->
<section class="services">
  <h2>What We Do</h2>
  <div class="service-list">
    <div class="service-card">
      <h3>✓ Residential Wiring</h3>
      <p>New installations, repairs, and upgrades</p>
    </div>
    <div class="service-card">
      <h3>✓ Panel Replacement</h3>
      <p>Upgrade old panels safely</p>
    </div>
    <div class="service-card">
      <h3>✓ 24/7 Emergency</h3>
      <p>Nights, weekends, holidays</p>
    </div>
  </div>
</section>

<!-- Trust -->
<section class="trust">
  <h2>You Can Trust Us</h2>
  <div class="trust-items">
    <div>
      <strong>Master Electrician</strong>
      <p>License #23847</p>
    </div>
    <div>
      <strong>Fully Insured</strong>
      <p>Bonded & Licensed</p>
    </div>
    <div>
      <strong>30 Years Experience</strong>
      <p>Serving Boston since 1995</p>
    </div>
  </div>
</section>

<!-- Reviews -->
<section class="reviews">
  <h2>Customer Reviews</h2>
  <div class="review-card">
    <div class="stars">⭐⭐⭐⭐⭐</div>
    <p>"Emergency call at 2 AM. They were here in 30 minutes. Fair price."</p>
    <p>— Jennifer M., Google</p>
  </div>
</section>

<!-- Pricing -->
<section class="pricing">
  <h2>Pricing</h2>
  <p><strong>Service Call:</strong> $75 (waived with repair)</p>
  <p><strong>Common Jobs:</strong> $150-$500+</p>
  <p><strong>Emergency (nights/weekends):</strong> +$100</p>
</section>

<!-- Booking -->
<section class="booking" id="booking">
  <h2>Schedule Service</h2>
  <form>
    <input type="text" placeholder="Your Name" required>
    <input type="tel" placeholder="Phone Number" required>
    <input type="email" placeholder="Email" required>
    <textarea placeholder="Describe your issue..."></textarea>
    <select required>
      <option>Preferred Date</option>
      <option>Today</option>
      <option>Tomorrow</option>
      <option>This Week</option>
    </select>
    <button class="btn btn-large">Book Service</button>
  </form>
</section>
```

**CSS:**
```css
/* Sticky phone banner */
.phone-banner {
  position: sticky;
  top: 0;
  background: #D32F2F;
  color: white;
  padding: 15px;
  text-align: center;
  z-index: 100;
  font-weight: bold;
}

.phone-banner a {
  color: white;
  text-decoration: none;
  font-size: 18px;
}

/* Services grid */
.services {
  padding: 60px 20px;
  background: #f9f9f9;
}

.services h2 {
  text-align: center;
  margin-bottom: 40px;
  font-size: 32px;
}

.service-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  max-width: 1000px;
  margin: 0 auto;
}

.service-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.service-card h3 {
  color: #D32F2F;
  margin-bottom: 10px;
}

/* Trust section */
.trust {
  padding: 60px 20px;
  background: white;
}

.trust h2 {
  text-align: center;
  margin-bottom: 40px;
}

.trust-items {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  max-width: 1000px;
  margin: 0 auto;
  text-align: center;
}

.trust-items strong {
  color: #D32F2F;
  display: block;
  margin-bottom: 5px;
}

/* Mobile: sticky call button */
@media (max-width: 768px) {
  .booking-form button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    z-index: 99;
  }
}
```

---

## Template Checklist: What to Include

### Restaurant
- ☐ Hero with food photo + CTAs
- ☐ Trust section with 5+ reviews
- ☐ Menu (categorized)
- ☐ Booking form
- ☐ Location + hours + phone
- ☐ Mobile-friendly

### Service (Electrician/Plumber/HVAC)
- ☐ Sticky phone number
- ☐ Hero with clear headline
- ☐ Service list
- ☐ Trust signals (license, years, insurance)
- ☐ Customer reviews
- ☐ Clear pricing
- ☐ Booking form
- ☐ Mobile "Call" button

### Salon
- ☐ Hero photo
- ☐ Services list
- ☐ Team bios
- ☐ Booking system
- ☐ Reviews
- ☐ Contact info

---

## How to Build These Efficiently

**Day 1:** Copy restaurant template, customize with their info (4 hours)
**Day 2:** Copy service template, customize with electrician info (4 hours)

Total: 8 hours per site = $500 revenue.

Build 2 sites per week = $4,000/month.

---

## What Makes Sites Convert

Based on all 3 guides:

✓ Clear hero section  
✓ Trust signals immediately visible  
✓ Easy CTA repeated 2-3 times  
✓ Fast loading (no heavy animations)  
✓ Mobile-friendly  
✓ Real customer reviews  
✓ Simple design (2-3 colors)  
✓ Smooth hover effects  
✓ No auto-play videos  
✓ Phone number prominent  

That's it. Build to this checklist, and you'll have professional sites ready to sell.
