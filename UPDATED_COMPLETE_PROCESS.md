# Updated Complete Process
## You Close Deals, I Build Websites

---

## THE FLOW (SIMPLIFIED)

1. **You close deal** → Customer says YES ($500)
2. **Customer sends photos** → You collect business info
3. **You forward to me** → "Build this website"
4. **I build website** → 2 hours, professional site
5. **I deploy to temp URL** → Customer reviews
6. **Customer approves** → Pays $500
7. **You register domain** → 5 minutes
8. **I deploy to permanent** → Website goes live
9. **You setup maintenance** → Optional $40/month

**Total time from close to live: 3-4 days**
**Your time per customer: ~25 minutes**
**My time per customer: 2.5 hours (build + deploy)**

---

## DAY BY DAY TIMELINE

### DAY 1 (Tomorrow, Feb 28): Launch Email Campaign

**9:00 AM:**
```bash
python3 schedule_daily_sends.py
```

**What happens:** 50 emails send automatically (over 4.5 hours)

**Your job:** Be ready to answer calls

---

### DAYS 2-7: Answer Phones & Close Deals

**When they call:**
```
"Hi, this is Andy. Thanks for calling back.

I build professional websites for local businesses.
$500, 3 days, you own everything.

You interested?"
```

**If YES:**
```
"Perfect. Send me:
- 5-8 photos (your storefront, team, work samples)
- Your business info (hours, phone, address, what you do)

I'll build your website in a couple days and show you."
```

**Log in spreadsheet:** Contact info + interested = YES

---

### DAY 8-10: You Get Photos & Forward to Me

**Customer sends:**
- Photos in email/folder
- Business name, hours, phone, address, services
- Any special requests

**You message me:**
```
Ready to build.

Business: Bob's Plumbing
Owner: Bob Smith
Phone: 303-555-0101
Email: bob@bobby.com
City: Denver, CO

Services: Emergency repair, water heater, drain cleaning
Hours: 24/7
Address: 123 Main St, Denver, CO 80202

Photos: [Folder location]
Google Reviews: [Link or copy reviews]

Build and deploy to temp URL.
```

**I reply (within 24 hours):**
```
✓ Website complete

Temp URL: https://bob-plumbing-temp.netlify.app

Send to customer.
```

---

### DAY 11-12: Customer Reviews & Pays

**You message customer:**
```
"Your website is ready! Check it out:
https://bob-plumbing-temp.netlify.app

Test it on your phone, try the contact form, reviews section.
If you like it, payment is $500.

Here's my PayPal: [Link]"
```

**Customer reviews** → Tests website → Pays $500

**You receive payment** → Log it in spreadsheet

---

### DAY 13: Register Domain

**You go to Namecheap:**
```
https://www.namecheap.com/

Search: bobsplumbing-denver.com
Buy: $12
Setup DNS: Point to Netlify
```

**Get Permanent Netlify Site ID:**
```
Go to netlify.com
Create new site
Copy Site ID
```

**Message me:**
```
Domain: bobsplumbing-denver.com
Site ID: a1b2c3d4e5f6g7h8

Deploy to permanent.
```

**I reply:**
```
✓ Deployed

Website now live: https://bobsplumbing-denver.com
```

---

### DAY 14: Website Live & Celebrate

**Message customer:**
```
"Your website is LIVE!

Visit: bobsplumbing-denver.com

Everything set up:
✓ Professional design
✓ Mobile friendly
✓ Contact form
✓ Your reviews displayed
✓ Secure (HTTPS)

Want optional $40/month maintenance to keep it updated?"
```

**Log final result:** Domain + Launched + Revenue $500

---

## YOUR RESPONSIBILITIES

### Close the Deal (10 minutes)
- Answer call
- Pitch website ($500, 3 days, they own it)
- Get YES
- Ask for photos + business info

### Collect Assets (5 minutes)
- Receive photos/info from customer
- Forward to me with briefing

### Register Domain (5 minutes)
- Go to Namecheap
- Buy domain ($12)
- Point to Netlify

### Collect Payment (1 minute)
- Receive $500 via PayPal
- Log it

### Optional Maintenance (2 minutes)
- Offer $40/month
- Setup PayPal recurring

**Total per customer: ~23 minutes**

---

## MY RESPONSIBILITIES

### Build Website (2 hours)
- Read their photos
- Create HTML/CSS
- Add business info
- Add reviews
- Optimize images
- Build contact form
- Test everything

### Deploy to Temp (30 seconds)
```bash
python3 deploy_website.py temp ./bob-site bob-temp
```

### Deploy to Permanent (30 seconds)
```bash
python3 deploy_website.py permanent ./bob-site site-id-123
```

---

## SCALE THIS UP

**Example Month:**

**Week 1:**
- Close: 2 deals
- Get photos: 2 customers
- I build: 2 websites
- Deploy temp: 2 sites
- Customers review: 2 sites

**Week 2:**
- Close: 2 more deals
- Get photos: 2 customers
- Customers from week 1 pay
- I build: 2 websites
- Register domains: 2 from week 1
- Deploy permanent: 2 from week 1

**Week 3-4:** Same pattern

**End of month:**
- 8 websites built
- 8 × $500 = $4,000 revenue
- 5 customers want maintenance = $200/month recurring
- Your time: ~3 hours total (mostly closing deals)
- My time: 16 hours building

---

## MONEY MATH

| Metric | Per Site | Per Month (4 sites) | Per Year (50 sites) |
|--------|----------|-------------------|-------------------|
| Revenue | $500 | $2,000 | $25,000 |
| Domain cost | -$12 | -$48 | -$600 |
| Hosting cost | $0 | $0 | $0 |
| Gross profit | $488 | $1,952 | $24,400 |
| Recurring (@60% signup) | $40/mo × 2.4 = $96/mo | $288 | $3,600 |
| **Total/month** | — | **$2,240** | **$27,000/year** |

---

## COMPLETE CHECKLIST

### Setup (Do today):
- [ ] Install libraries: `pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client schedule`
- [ ] Start scheduler: `python3 schedule_daily_sends.py`
- [ ] Clear calendar for calls
- [ ] Have phone ready
- [ ] Create Namecheap account
- [ ] Have PayPal links ready

### Per Customer (When they say YES):
- [ ] Ask for photos + business info
- [ ] Receive package
- [ ] Forward to me with briefing
- [ ] I build website (wait 24 hrs)
- [ ] Deploy to temp URL (30 sec)
- [ ] Send customer link
- [ ] Customer reviews (24 hrs)
- [ ] Collect $500 payment
- [ ] Register domain (5 min)
- [ ] Get Netlify Site ID
- [ ] Tell me to deploy permanent (30 sec)
- [ ] Website live

---

## MESSAGE TEMPLATES

### To Customer (When they say YES):
```
"Perfect! Here's what I need:

1. Photos: 5-8 photos of your storefront, team, or work samples
2. Business info:
   - Hours of operation
   - Main services (2-3 sentences)
   - Address
   - Phone number

Send these to me and I'll have your website ready in a couple days."
```

### To Customer (When website is ready):
```
"Your website is ready to review!

Check it out: [TEMP_URL]

Look at:
✓ Homepage
✓ Services
✓ Contact form (try it!)
✓ Mobile (view on your phone)
✓ Reviews section

Let me know if you want any changes. Once you're happy, 
payment is $500 and I'll move it to your permanent domain."
```

### To Customer (When deployed permanent):
```
"Your website is LIVE!

Visit: [DOMAIN_URL]

Everything is set up and ready. Google will start showing 
your site in search results over the next 1-2 weeks.

Questions? Let me know."
```

### To Me (When ready to build):
```
Ready to build.

Business: [Name]
Owner: [Name]
City: [City]
Phone: [Phone]
Email: [Email]
Services: [Description]
Hours: [Hours]
Address: [Address]

Photos: [Folder or description]
Google Reviews: [Link or copy]

Build and deploy to temp URL.
```

---

## EXPECTED RESULTS BY MARCH 7

| Metric | Low | High |
|--------|-----|------|
| Emails sent | 250 | 350 |
| Responses | 20 | 42 |
| Demos scheduled | 8 | 20 |
| Deals closed | 2 | 5 |
| Websites built | 2 | 5 |
| Revenue | $1,000 | $2,500 |
| Maintenance signups | 1 | 3 |
| Monthly recurring | $40 | $120 |

---

## TIMELINE TO FIRST PAYMENT

```
Feb 28, 9 AM: Email campaign launches
Feb 28, 2 PM: First calls arrive
Feb 28-Mar 2: Close first deal
Mar 2-3: Collect photos
Mar 3-4: I build website
Mar 4: Deploy to temp, customer reviews
Mar 5: Customer pays $500
Mar 5-6: Register domain
Mar 6: Website live

TOTAL: 7 DAYS TO FIRST REVENUE
```

---

## READY?

**Tomorrow morning at 9 AM:**

```bash
python3 schedule_daily_sends.py
```

**Everything else follows.**

---

**Let's go. 🚀**
