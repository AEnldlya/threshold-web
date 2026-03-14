# Quick Build Reference — Copy This

## Copy-Paste Templates by Category

### 🍽️ RESTAURANT MINIMUM VIABLE SITE

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Restaurant Name</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; color: #333; }
    
    /* Hero */
    .hero {
      background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('food.jpg');
      background-size: cover;
      background-position: center;
      height: 400px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      color: white;
    }
    
    .hero h1 { font-size: 48px; margin-bottom: 10px; }
    .hero p { font-size: 18px; margin-bottom: 30px; }
    
    .btn {
      padding: 12px 24px;
      background: #C41E3A;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      margin: 0 10px;
      text-decoration: none;
      display: inline-block;
      transition: all 0.3s;
    }
    
    .btn:hover {
      background: #A01830;
      transform: scale(1.05);
    }
    
    .container {
      max-width: 1000px;
      margin: 0 auto;
      padding: 40px 20px;
    }
    
    .review {
      background: #f9f9f9;
      padding: 20px;
      margin: 15px 0;
      border-radius: 4px;
      border-left: 4px solid #C41E3A;
    }
    
    .review .stars { color: #FFB800; margin-bottom: 10px; }
    .review p { font-size: 14px; margin: 5px 0; }
    
    /* Footer */
    footer {
      background: #333;
      color: white;
      text-align: center;
      padding: 30px;
    }
    
    footer a { color: #C41E3A; text-decoration: none; }
    
    @media (max-width: 768px) {
      .hero { height: 300px; }
      .hero h1 { font-size: 32px; }
    }
  </style>
</head>
<body>

<div class="hero">
  <div>
    <h1>Mario's Italian Kitchen</h1>
    <p>Authentic Italian • Since 1990</p>
    <a href="#book" class="btn">Reserve Table</a>
    <a href="tel:+16175551234" class="btn">Call Now</a>
  </div>
</div>

<div class="container">
  <h2>Why Our Customers Love Us</h2>
  <div class="review">
    <div class="stars">⭐⭐⭐⭐⭐</div>
    <p>"Best pasta in the city. Been coming for 10 years."</p>
    <p><strong>— John M., Google Reviews</strong></p>
  </div>
  
  <h2>Our Menu</h2>
  <p><strong>Grandmother's Lasagna</strong> — Hand-rolled pasta with meat sauce — $16</p>
  <p><strong>Osso Buco</strong> — Braised veal shanks with risotto — $24</p>
  
  <h2 id="book">Reserve a Table</h2>
  <form>
    <input type="text" placeholder="Your Name" required style="padding: 10px; margin: 5px; width: 100%; max-width: 300px;">
    <input type="tel" placeholder="Phone" required style="padding: 10px; margin: 5px; width: 100%; max-width: 300px;">
    <input type="date" required style="padding: 10px; margin: 5px; width: 100%; max-width: 300px;">
    <button type="submit" class="btn">Book Now</button>
  </form>
</div>

<footer>
  <p>📞 (617) 555-1234</p>
  <p>📍 123 Boston Street, Boston MA</p>
  <p>Mon-Thu 11 AM - 10 PM | Fri-Sat 11 AM - 11 PM | Sun 12 PM - 9 PM</p>
</footer>

</body>
</html>
```

---

### 🔧 ELECTRICIAN MINIMUM VIABLE SITE

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Emergency Electrical Service</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; color: #333; }
    
    .phone-banner {
      background: #D32F2F;
      color: white;
      padding: 15px;
      text-align: center;
      font-weight: bold;
      font-size: 18px;
    }
    
    .phone-banner a { color: white; text-decoration: none; }
    
    .hero {
      background: linear-gradient(135deg, #0277BD, #01579B);
      color: white;
      padding: 60px 20px;
      text-align: center;
    }
    
    .hero h1 { font-size: 36px; margin-bottom: 10px; }
    .hero p { font-size: 16px; margin-bottom: 30px; }
    
    .btn {
      padding: 12px 24px;
      background: #D32F2F;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
      transition: all 0.3s;
    }
    
    .btn:hover { background: #B71C1C; transform: scale(1.05); }
    
    .container { max-width: 1000px; margin: 0 auto; padding: 40px 20px; }
    
    .card { background: #f9f9f9; padding: 20px; margin: 15px 0; border-radius: 4px; }
    .card h3 { color: #D32F2F; margin-bottom: 10px; }
    
    .trust { background: #f9f9f9; padding: 40px 20px; text-align: center; }
    .trust-item { background: white; padding: 20px; margin: 10px; display: inline-block; min-width: 200px; }
    .trust-item strong { color: #D32F2F; display: block; }
    
    footer { background: #333; color: white; text-align: center; padding: 30px; }
    footer a { color: #D32F2F; }
    
    @media (max-width: 768px) {
      .hero h1 { font-size: 24px; }
      .btn { width: 100%; }
    }
  </style>
</head>
<body>

<div class="phone-banner">
  <a href="tel:+16175551234">📞 (617) 555-1234 — CALL NOW</a>
</div>

<div class="hero">
  <div>
    <h1>24/7 Emergency Electrical Service</h1>
    <p>Licensed • Insured • Same-Day Service</p>
    <a href="#book" class="btn">Schedule Service</a>
  </div>
</div>

<div class="container">
  <h2>What We Do</h2>
  <div class="card"><h3>✓ Residential Wiring</h3><p>New installations and repairs</p></div>
  <div class="card"><h3>✓ Panel Replacement</h3><p>Upgrade old, unsafe panels</p></div>
  <div class="card"><h3>✓ 24/7 Emergency</h3><p>Nights, weekends, holidays</p></div>
  
  <h2>Why Trust Us</h2>
  <div class="trust">
    <div class="trust-item">
      <strong>Master Electrician</strong>
      <p>License #23847</p>
    </div>
    <div class="trust-item">
      <strong>30 Years Experience</strong>
      <p>Serving Boston since 1995</p>
    </div>
    <div class="trust-item">
      <strong>Fully Insured</strong>
      <p>Bonded & Licensed</p>
    </div>
  </div>
  
  <h2>Customer Reviews</h2>
  <div class="card">
    <div class="stars">⭐⭐⭐⭐⭐</div>
    <p>"Emergency call at 2 AM. Here in 30 minutes. Fair price. Highly recommend."</p>
    <p><strong>— Jennifer M., Google</strong></p>
  </div>
  
  <h2>Pricing</h2>
  <p><strong>Service Call:</strong> $75 (waived if you hire us)</p>
  <p><strong>Common Jobs:</strong> $150-$500+</p>
  <p><strong>Emergency (nights/weekends):</strong> +$100</p>
  
  <h2 id="book">Schedule Service</h2>
  <form>
    <input type="text" placeholder="Your Name" required style="display: block; width: 100%; max-width: 400px; padding: 10px; margin: 10px auto;">
    <input type="tel" placeholder="Phone" required style="display: block; width: 100%; max-width: 400px; padding: 10px; margin: 10px auto;">
    <textarea placeholder="Describe your issue..." style="display: block; width: 100%; max-width: 400px; padding: 10px; margin: 10px auto; height: 100px;"></textarea>
    <button type="submit" class="btn" style="display: block; margin: 20px auto;">Book Service</button>
  </form>
</div>

<footer>
  <p>📞 (617) 555-1234</p>
  <p>📍 123 Boston Street, Boston MA</p>
  <p>Available 24/7 for emergencies</p>
</footer>

</body>
</html>
```

---

## CSS Animations to Add (Copy & Paste)

```css
/* Hover effects */
.btn:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

/* Form focus */
input:focus, textarea:focus {
  outline: none;
  border-color: #D32F2F;
  box-shadow: 0 0 5px rgba(211,47,47,0.3);
}

/* Card hover */
.card:hover {
  box-shadow: 0 8px 16px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}

/* Smooth scroll */
html {
  scroll-behavior: smooth;
}
```

---

## Deployment (Netlify)

1. Create folder with HTML file
2. Drag & drop to Netlify
3. Done in 30 seconds

```bash
# OR command line:
npm install -g netlify-cli
cd your-site-folder
netlify deploy
```

---

## What You Need Per Site

- HTML file (from templates above)
- 2-3 images (food photos or team photo)
- Customer info (name, phone, address, hours)
- 3-5 Google reviews (copy exact text)
- That's it.

---

## Build Checklist

- ☐ Copy template
- ☐ Replace placeholder text with customer info
- ☐ Add images
- ☐ Add reviews
- ☐ Test on phone
- ☐ Deploy to Netlify
- ☐ Get temporary URL
- ☐ Send to customer
- ☐ Get approval
- ☐ Collect $500
- ☐ Deploy to permanent domain

---

Go build. You have everything you need.

