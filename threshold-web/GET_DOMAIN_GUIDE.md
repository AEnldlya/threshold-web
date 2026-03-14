# How to Get & Register Domains
## Complete Step-by-Step Guide (5 minutes per domain)

---

## WHERE TO BUY DOMAINS

**Best options:**
1. **Namecheap** (recommended) — $12/year, easy, good support
2. GoDaddy — $14/year, popular, more ads
3. Google Domains — $12/year, integrated with Google

**I recommend: Namecheap** (cheapest, cleanest interface)

---

## STEP-BY-STEP: NAMECHEAP

### Step 1: Go to Namecheap
```
https://www.namecheap.com/
```

### Step 2: Search for Domain
```
Search bar at top: "bobsplumbing-denver.com"

Results show:
✓ Available ($12/year)
OR
✗ Taken (try alternatives)
```

### Step 3: If Available, Click "Add to Cart"

### Step 4: Go to Checkout
- Click: Proceed to checkout
- Sign in (create account if needed)
- Add billing address
- Add payment method (credit card)

### Step 5: Choose Registration Length
- **Recommended:** 2 years ($24)
- Why: Shows customer you're committed + saves money per year

### Step 6: Add-ons (Optional)
- Auto-renew: YES (don't let it lapse)
- Privacy protection: Optional (hides your info from WHOIS)
- Email forwarding: Optional (forward domain@example.com to your email)

### Step 7: Pay & Confirm
- Click: Complete order
- Domain is now yours

### Step 8: Set Up DNS (Point to Netlify)
**In Namecheap dashboard:**
1. Click: "Manage" (next to your domain)
2. Click: "Advanced DNS" tab
3. Add DNS records to point to Netlify

**Option A: Netlify Nameservers (Easiest)**
```
In Namecheap:
- Nameservers: Custom DNS
- Add Netlify nameservers (Netlify will give you these)
- Save
```

**Option B: CNAME Record**
```
Type:   CNAME
Host:   www
Value:  [your-site].netlify.app

Type:   A Record
Host:   @
Value:  75.2.60.5
```

### Step 9: Done
- Domain is registered
- Domain is pointing to Netlify
- Website is live

---

## DOMAIN NAMING STRATEGY

**When customer wants a domain, give them options:**

### Best Option (Tier 1):
- `bobsplumbing-denver.com` (business name + city)
- Professional, branded, easy to remember

### Good Option (Tier 2):
- `denverplumbing.com` (service + city)
- Good for SEO, clear what they do

### Backup Option (Tier 3):
- `bobsplumbing.pro` (name + extension)
- If .com is taken
- Still professional

### Alternatives if taken:
- `bobs-plumbing-denver.com` (add hyphen)
- `bobsplumbing24.com` (add number)
- `denveremergencyplumbing.com` (add descriptor)

**Always give customer 3 options:**
1. "Here's the best domain for your business..."
2. "If that's taken, here's a good alternative..."
3. "Or we could use..."

---

## COST BREAKDOWN

| Item | Cost | Who Pays |
|------|------|----------|
| Domain (1 year) | $12 | **You (included in $500)** |
| Domain (2 years) | $24 | **You (better value)** |
| Netlify hosting | $0 | **Free** |
| HTTPS/SSL | $0 | **Free** |
| **Total Year 1** | **$12-24** | **You** |
| **Year 2+** | **$12/year** | **Customer pays OR you charge $50/year** |

---

## WHEN TO REGISTER DOMAIN

**Option A: Register before building** (you pay upfront)
- Register domain → Give customer domain name → Build site → Deploy to domain
- Cost: $12 upfront (you're out of pocket until payment)

**Option B: Register after customer pays** (safer for cash flow)
- Customer says YES → Build site → Deploy to temp URL → Customer pays → Register domain → Deploy to permanent
- Cost: $12 from their payment
- Better: You're not spending money before getting paid

**I recommend: Option B** (build → temp deploy → payment → register → permanent deploy)

---

## COMPLETE WORKFLOW WITH DOMAINS

### Day 1: Customer Says YES
```
You: "Perfect! Let me build your website."
Message: "I'll have you live in 3 days at one of these domains:"
- Option 1: bobsplumbing-denver.com
- Option 2: denverplumbing.com
- Option 3: bobsplumbing.pro
"Which do you prefer?"
```

### Day 2-3: Build Website
```
Create website files locally
Test everything
Ready to deploy
```

### Day 3 Evening: Deploy to Temp URL
```
You message me: "Deploy to temp"
I deploy: bob-plumbing-site.netlify.app
You send customer: "Your website is ready! Check it out..."
```

### Day 4: Customer Reviews & Pays
```
Customer: "Looks great, here's the $500"
PayPal payment arrives
```

### Day 4-5: Register Domain & Go Live
```
You: "One more thing - which domain did you want?"
Customer: "bobsplumbing-denver.com"

You:
1. Go to Namecheap.com
2. Search: bobsplumbing-denver.com
3. Buy ($12)
4. Point DNS to Netlify
5. Wait 5-30 minutes for propagation

Me:
python3 deploy_website.py permanent ./bob-plumbing-site site-id-123
```

### Day 5-6: Website Live
```
bobsplumbing-denver.com is now LIVE
Customer sees professional website on their custom domain
You've collected $500 + setup $40/month recurring
```

---

## DOMAIN REGISTRATION CHECKLIST

Before registering:
- [ ] Customer approved domain choice
- [ ] Customer has paid $500
- [ ] Website is built and tested
- [ ] Temporary deployment is working
- [ ] Customer confirmed they like the design

Registration:
- [ ] Go to Namecheap (or preferred registrar)
- [ ] Search domain
- [ ] Add to cart ($12-24)
- [ ] Checkout
- [ ] Complete payment
- [ ] Copy Netlify nameservers (or setup CNAME)
- [ ] Add DNS records in Namecheap

Setup:
- [ ] DNS records are pointing to Netlify
- [ ] Wait 5-30 minutes for propagation
- [ ] Test: Open domain in browser
- [ ] Confirm website loads correctly

---

## QUICK REFERENCE

**Namecheap URL:**
```
https://www.namecheap.com/
```

**Search:**
```
Enter domain name → Check availability
```

**Buy:**
```
Add to cart → Proceed to checkout → Complete payment
```

**DNS Setup:**
```
Dashboard → Manage → Advanced DNS → Add Netlify nameservers
```

**Test:**
```
Open browser, enter domain, website should load
```

---

## MULTIPLE DOMAINS STRATEGY

**As you grow:**
- Customer 1: `bobsplumbing-denver.com`
- Customer 2: `sallyhair-austin.com`
- Customer 3: `mikesvac-chicago.com`
- etc.

**Cost:** $12 per domain
**Revenue:** $500 per website
**Profit:** $488 per site (first year)

---

## DOMAIN RENEWAL REMINDER

**Set calendar reminder:**
- 1 year after purchase: Domain expires
- Enable auto-renew in Namecheap
- OR: Charge customer $50/year to manage renewal

**Example:**
```
Customer: "Can I just pay you to handle it?"
You: "Sure, $50/year and I renew it automatically. Sound good?"
Customer: "Yep"
→ $50/year passive revenue per customer
```

---

## DONE

You now know how to:
1. Find domain availability
2. Register domain at Namecheap
3. Point domain to Netlify
4. Test it's working

**Next time customer says YES:**
1. Build website
2. I deploy to temp URL
3. Customer pays
4. You register domain (5 min)
5. I deploy to permanent (30 sec)
6. Done

---

**Simple, fast, profitable.**
