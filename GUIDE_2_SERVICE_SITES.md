# Guide 2: HVAC, Electricians, Plumbers — What Actually Converts

## Why Service Sites Are Different

People searching for a plumber at midnight are NOT looking at menus or ambiance.

They're asking: **"Can you fix this NOW? Are you trustworthy? How much?"**

Your site needs to answer that in 10 seconds.

---

## Pattern #1: The Emergency Hero Section

**What works:**
```
Large, clear headline:
"24/7 Emergency Plumbing"

Phone number (clickable)
Big, obvious button: "Call Now" or "Schedule Service"

Maybe a single image: truck, or fixing something, or person in uniform
```

**Why it works:**
- Person searching at 11 PM doesn't care about your story
- They want help NOW
- Phone number first = instant action
- Trust builds from fast response

**Code:**
```html
<section class="hero">
  <h1>24/7 Emergency Plumbing Service</h1>
  <p class="large-text">(617) 555-1234</p>
  <a href="tel:+16175551234" class="btn btn-large">
    Call Now
  </a>
  <a href="#booking" class="btn btn-secondary">
    Schedule Service
  </a>
</section>
```

---

## Pattern #2: Service Categories (So They Know You Handle Their Problem)

**What works:**
- Quick list of what you do:
  ```
  Water Heaters
  Burst Pipes
  Drain Cleaning
  Gas Line Repair
  Preventative Maintenance
  ```

- Just list, simple checkmarks, no descriptions needed
- Makes clear: "This is the right number"

**Why it works:**
- Removes doubt: "Do they handle water heaters? Let me check."
- Customer finds their problem = they call you
- Takes 5 seconds to scan

---

## Pattern #3: Trust Through License/Certification

**What works:**
```
Licensed Master Plumber #23847
Insured & Bonded
22 Years of Experience

Customer Reviews:
⭐⭐⭐⭐⭐ "Had an emergency on Sunday. They came in 30 minutes. 
Saved the day." — Jennifer M., Google

⭐⭐⭐⭐⭐ "Fair pricing, professional, knew exactly what was wrong." 
— Bob T., Yelp
```

**Why it works:**
- License proves legitimacy
- Insurance = customer is protected
- Years matter ("22 years" > "new company")
- Real reviews beat ads

---

## Pattern #4: Pricing Transparency

**What works:**
```
SERVICE PRICING
─────────────────

Service Call Fee: $75 (waived if you hire us)
After Hours (5 PM - 8 AM): +$50
Emergency (nights/weekends): +$100

Common Jobs:
Toilet Repair: $150-300
Drain Cleaning: $200-400
Water Heater Replacement: $1,200-2,500
```

**Why it works:**
- Customers HATE surprises
- Transparency builds trust
- Showing service fee (waived) is honest
- Common prices set expectations

**What NOT to do:**
- ❌ "Call for quote" (they'll call competitor)
- ❌ Vague pricing
- ❌ Hidden fees

---

## Pattern #5: Service Area Map

**What works:**
```
We service these areas:
Boston, Cambridge, Somerville, Newton, Waltham, Quincy

Response time: 30 minutes or less
Or we'll knock $50 off your bill
```

**Why it works:**
- Clarity: "Is my address served?"
- Promise sets expectations
- Penalty for lateness = you're confident

---

## Pattern #6: How to Schedule (Multiple Options)

**What works:**
Three ways to book:

**Option 1: Call**
```
(617) 555-1234
Available 24/7
```

**Option 2: Online Form**
```
[Simple form: Name, Address, Phone, Problem, Date/Time preference]
```

**Option 3: Text**
```
Text "PLUMBER" to (617) 555-1234
```

**Why it works:**
- Different people prefer different methods
- Offering choice = more bookings
- All methods feed to same system

---

## Pattern #7: Before/After Photos

**What works:**
```
Clogged Drain Job
[Photo of nasty drain]
"Before"
↓
[Photo of clean drain]
"After"

Caption: "Professional drain cleaning removes all debris"
```

**Why it works:**
- Visual proof of quality
- Shows scope of work
- Builds confidence: "They can fix MY problem"
- No expensive equipment needed—your phone is enough

---

## Pattern #8: FAQ Section (Reduces Phone Calls)

**What works:**
```
Q: What do you charge for a service call?
A: $75 for the visit, waived if you hire us for the job.

Q: How quickly can you come?
A: Usually 30-60 minutes. We do emergency service 24/7.

Q: Are you licensed?
A: Yes. Master Plumber License #23847. Full insurance.

Q: What if I need it done at night?
A: We do emergency service. Add $100 to cost.

Q: Do you offer discounts?
A: Senior/military discounts: 10%. Referral discount: $25 off.
```

**Why it works:**
- Answers common objections before they call
- Reduces phone time
- Shows you're confident (no hiding info)

---

## Pattern #9: Service Guarantee

**What works:**
```
100% Satisfaction Guarantee

We'll fix it right or your money back.
All work guaranteed 1 year.
```

**Why it works:**
- Removes risk for customer
- Shows you're confident in your work
- Converts fence-sitters

---

## Pattern #10: Testimonials From Local Customers

**What works:**
```
⭐⭐⭐⭐⭐ 
"Called them for a burst pipe at 2 AM. 
Thought it would cost thousands. They fixed it for $600. 
Professional and kind. Highly recommend."
— Sarah T., Cambridge, MA

⭐⭐⭐⭐⭐
"Have used them for 5 years. Never had an issue. 
They know our house inside and out."
— Tom M., Boston, MA
```

**Why it works:**
- Real names + locations = trustworthy
- Specific details (2 AM, $600) = genuine
- Long-term relationships prove quality

---

## Full Layout for Service Sites

```
Header
├── Company name
├── Phone number (clickable)
└── "Schedule Now" button

Hero
├── Clear headline ("24/7 [Service] Service")
├── Large phone number
└── Call/Schedule buttons

Services
├── List of what you do
└── Quick explanations

Pricing
├── Service fee
├── Common jobs + prices
└── Emergency surcharges

Reviews
├── 5-8 real reviews
├── Stars + names
└── Google/Yelp badges

Before/After
├── Photo gallery
├── Shows quality of work
└── Captions

How to Book
├── Phone
├── Online form
└── Text option

FAQ
├── 8-10 common questions
└── Direct answers

Guarantee/Trust
├── 1-year guarantee
├── License/Insurance info
└── Experience years

Footer
├── Phone
├── Address
├── Service area
└── Hours
```

---

## CSS Patterns (Service Sites)

```css
/* Large phone number - always visible */
.phone-banner {
  background-color: #D32F2F;
  color: white;
  padding: 20px;
  text-align: center;
  font-size: 28px;
  font-weight: bold;
  position: sticky;
  top: 0;
  z-index: 100;
}

.phone-banner a {
  color: white;
  text-decoration: none;
}

/* Service list - simple checkmarks */
.service-list {
  list-style: none;
  padding: 20px;
}

.service-list li:before {
  content: "✓ ";
  color: #4CAF50;
  font-weight: bold;
  margin-right: 10px;
}

/* Trust badges */
.trust-section {
  background-color: #f5f5f5;
  padding: 40px 20px;
  text-align: center;
}

.badge {
  display: inline-block;
  margin: 10px;
  padding: 15px 20px;
  border: 2px solid #D32F2F;
  border-radius: 4px;
}

/* Before/After */
.before-after {
  display: flex;
  gap: 10px;
  margin: 20px 0;
}

.before-after img {
  flex: 1;
  max-width: 300px;
}

/* Mobile sticky button */
@media (max-width: 768px) {
  .call-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: #D32F2F;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
  }
}
```

---

## Quick Checklist

- ☐ Large, clickable phone number
- ☐ "Call Now" button above fold
- ☐ Service categories listed
- ☐ License/insurance/experience visible
- ☐ Transparent pricing
- ☐ Service area clear
- ☐ Multiple booking options
- ☐ Before/after photos
- ☐ Real customer reviews
- ☐ FAQ section
- ☐ 1-year guarantee
- ☐ Mobile sticky "Call Now" button

---

## The Secret Pattern That Works Best

The most effective service sites all do ONE thing:

**Make it stupidly easy to call.**

Hero section:
```
BIG HEADING
BIG PHONE NUMBER
BIG CLICKABLE BUTTON
"CALL NOW"
```

Everything else is supporting that.

Your #1 job: Get them to call you in the next 60 seconds.

Everything else (FAQ, reviews, pricing) just removes friction.

---

## What to Copy (For Your Sites)

✓ Large, visible phone number  
✓ "Call Now" button prominent  
✓ Service list (simple checkmarks)  
✓ Trust signals (license, insurance, years)  
✓ Transparent pricing  
✓ Real customer reviews  
✓ Before/after photos  
✓ Multiple booking options  
✓ Simple, fast loading  
✓ Mobile-first (tap-to-call)  

Build this, and electricians/plumbers will book you for customer sites.
