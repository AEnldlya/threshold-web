# Domain & Deployment Guide
## From Website Files → Live on Custom Domain (15 minutes)

---

## THE COMPLETE FLOW

**When customer says YES:**

1. **Register domain** ($12/year)
2. **Build website** (12 hours)
3. **Deploy to Netlify** (2 minutes)
4. **Point domain to Netlify** (5 minutes)
5. **Live website goes online** (propagation: 5 min - 24 hours)
6. **Get paid** ($500 PayPal)

**Total setup time:** ~25 minutes (plus 12 hours build)

---

## STEP 1: REGISTER DOMAIN (5 MINUTES)

### Where to Register
- **Namecheap** (recommended, $12/year) — namecheap.com
- GoDaddy ($14/year) — godaddy.com
- Google Domains ($12/year) — domains.google.com

### Process

**Go to Namecheap:**
1. Go to: **namecheap.com**
2. Search domain: **"bobsplumbing-denver.com"** (or customer's choice)
3. Click: **"Add to cart"**
4. Checkout → Pay $12 (use your credit card)
5. Done

**You now own the domain.** Customer gets login credentials.

---

## STEP 2: BUILD WEBSITE (12 HOURS)

Use **WEBSITE_WITH_REVIEWS.md** template:
- Create folder: `bob-plumbing-site/`
- Add: `index.html`, `css/styles.css`, `js/script.js`
- Add: `images/` folder with customer photos
- Add: Other pages (`services.html`, `contact.html`, etc.)

**Build checklist:**
- [ ] Homepage with hero section
- [ ] Services/offerings page
- [ ] About/team page
- [ ] Reviews section (5-8 from Google)
- [ ] Contact form
- [ ] Mobile responsive
- [ ] Fast loading (images optimized)
- [ ] All links working

---

## STEP 3: DEPLOY TO NETLIFY (2 MINUTES)

### Option A: Drag & Drop (Easiest)

1. Go to: **netlify.com**
2. Sign in (create account if needed)
3. Click: **"Add new site"**
4. Drag folder `bob-plumbing-site/` into browser
5. Wait 30 seconds
6. Site deployed → Get temporary URL like: `bob-plumbing-site.netlify.app`

**Done.** Website is live (but on Netlify's domain, not custom domain yet).

### Option B: Git + Netlify (Better for updates)

1. Create GitHub repo: `bob-plumbing-site`
2. Push website files to GitHub
3. Go to Netlify → Connect GitHub repo
4. Netlify auto-deploys
5. Done

**Advantage:** Every time you update on GitHub, site auto-updates on Netlify.

---

## STEP 4: CONNECT CUSTOM DOMAIN (5 MINUTES)

Now point `bobsplumbing-denver.com` to the Netlify site.

### In Netlify Dashboard:

1. Go to your site dashboard
2. Click: **"Domain settings"**
3. Click: **"Add custom domain"**
4. Enter: **bobsplumbing-denver.com**
5. Click: **"Verify"**

### In Namecheap (DNS Settings):

1. Go to Namecheap dashboard
2. Click: **"Manage"** (next to your domain)
3. Click: **"Advanced DNS"** tab
4. Add these DNS records:

**Option 1: Point to Netlify nameservers (recommended)**
```
Go to Netlify domain settings
Copy Netlify nameservers (usually):
- dns1.p01.nsone.net
- dns2.p01.nsone.net
- dns3.p01.nsone.net
- dns4.p01.nsone.net

In Namecheap:
Nameservers: Custom DNS
- dns1.p01.nsone.net
- dns2.p01.nsone.net
- dns3.p01.nsone.net
- dns4.p01.nsone.net

Click: Save
```

**Option 2: Add CNAME record (simpler)**
```
In Namecheap Advanced DNS:

Type:   CNAME
Host:   www
Value:  [your-site].netlify.app

Type:   A
Host:   @
Value:  75.2.60.5  (Netlify's IP)

Click: Save
```

### Wait for Propagation

DNS propagation takes 5 minutes to 24 hours.

**Check status:**
- Go to: whatsmydns.net
- Enter your domain
- When it shows green everywhere = live

---

## STEP 5: HTTPS & SECURITY (AUTOMATIC)

**Netlify automatically:**
- ✅ Provides free HTTPS (SSL certificate)
- ✅ Auto-renews certificates
- ✅ Redirects HTTP → HTTPS
- ✅ Site is secure

**No work needed from you.** Just automatic.

---

## STEP 6: TESTING

**Before customer goes live, test:**

```
1. Open browser: bobsplumbing-denver.com
2. Check: Homepage loads
3. Check: All pages work (services, about, contact)
4. Check: Images load
5. Check: Contact form works
6. Check: Mobile looks good (resize browser)
7. Check: HTTPS (green lock icon)
8. Check: Speed (under 3 seconds load)
```

---

## COMPLETE EXAMPLE WALKTHROUGH

**Customer: Bob's Plumbing in Denver**

### Day 1: Register Domain + Build
```
9 AM:  Customer says YES, sends photos
10 AM: You register bobsplumbing-denver.com ($12)
10 AM-10 PM: Build website (12 hours)
```

### Day 2: Deploy
```
9 AM:  Website complete + tested
9:05 AM: Drag folder into Netlify (site deployed)
9:10 AM: Connect bobsplumbing-denver.com to Netlify
9:15 AM: DNS propagation starts (takes 5 min - 24 hours)
```

### Day 3: Live
```
By 2 PM: bobsplumbing-denver.com fully live
Call customer: "Your site is live! Check it out."
Send PayPal link: "Pay $500 here"
Once paid: Done
Setup $40/month maintenance (optional)
```

---

## QUICK REFERENCE CHECKLIST

### Domain Registration
- [ ] Decide domain name (bobsplumbing-denver.com)
- [ ] Go to Namecheap
- [ ] Search + buy domain ($12)
- [ ] Get login credentials for customer

### Website Build
- [ ] Create HTML/CSS/JS files
- [ ] Add customer photos
- [ ] Add reviews section
- [ ] Test all pages
- [ ] Test mobile
- [ ] Optimize images

### Deploy to Netlify
- [ ] Drag folder into Netlify
- [ ] Verify site loads on netlify.app URL
- [ ] Check all pages work

### Connect Domain
- [ ] Add custom domain in Netlify
- [ ] Update DNS in Namecheap (nameservers or CNAME)
- [ ] Wait for propagation (5 min - 24 hours)

### Go Live
- [ ] Test on custom domain
- [ ] Verify HTTPS working
- [ ] Check speed
- [ ] Send customer live link
- [ ] Send PayPal payment link
- [ ] Collect $500

---

## COST BREAKDOWN

| Item | Cost | Who Pays |
|------|------|----------|
| Domain (1 year) | $12 | You (included in $500 deal) |
| Hosting (Netlify) | $0 | Free |
| HTTPS/SSL | $0 | Free (auto) |
| Email (optional) | $0.88-6/mo | Customer (optional) |
| **Total Year 1** | **$12** | **You** |
| **Year 2+** | **$12/year domain** | **Customer or you charge $50/yr** |

---

## MAINTENANCE PACKAGE ($40/month)

If customer agrees to maintenance:

**Includes:**
- Domain renewal ($12/year, you pay upfront)
- Hosting on Netlify (free)
- Updates to content (2 per month)
- Security monitoring
- Performance checks
- Support via email

**You make:** $40/month × 12 = $480/year
**You spend:** $12/year domain = $468 profit per customer

---

## WHAT IF DOMAIN IS TAKEN?

**Problem:** `bobsplumbing-denver.com` already exists

**Solutions:**
1. **Try alternatives:**
   - `bobs-plumbing-denver.com`
   - `bobsplumbing.pro`
   - `denverplumbing.com`
   - `emergencyplumbing-denver.com`

2. **Call customer:**
   "Their preferred domain isn't available. Want to use this instead?"

3. **Still want that domain?**
   - Offer to buy it (might cost $50-500)
   - Negotiate with owner
   - Use premium domain marketplace (Sedo, Afternic)

**Recommendation:** Have 3-5 backup domain options ready before build.

---

## PRODUCTION WORKFLOW TEMPLATE

Save this as your checklist for each customer:

```
CUSTOMER: ________________________
DOMAIN: ________________________
BUILD START: ________________________
BUILD END: ________________________

DEPLOY CHECKLIST:
[ ] 1. Registered domain (cost: $12)
[ ] 2. Website built (12 hours)
[ ] 3. Website tested locally (all pages, mobile, forms)
[ ] 4. Images optimized (<100KB each)
[ ] 5. Deployed to Netlify
[ ] 6. Connected custom domain
[ ] 7. DNS updated in Namecheap
[ ] 8. Waiting for propagation...
[ ] 9. Live on custom domain
[ ] 10. Final testing (pages, forms, mobile, HTTPS, speed)

LAUNCH:
[ ] Customer calls - site is live
[ ] Send PayPal $500 link
[ ] Payment received
[ ] Set up $40/month maintenance (optional)
[ ] Update outreach tracker (CLOSED)

REVENUE LOGGED:
One-time: $500 ✓
Recurring: $40/month (if accepted)
```

---

## AUTOMATED DEPLOYMENT OPTION (Advanced)

If you want to automate deployment:

```bash
# 1. Create script to deploy on demand
# 2. Push to GitHub → auto-deploys to Netlify
# 3. Run command, site updates instantly

# Example:
./deploy.sh bob-plumbing-site
# Site updates on bobsplumbing-denver.com automatically
```

(Can build this later if you want.)

---

## DONE

You now know:
1. How to register a domain ($12)
2. How to deploy to Netlify (drag-drop)
3. How to connect domain (5-minute DNS setup)
4. How to test before going live
5. Cost breakdown ($12 total, you pay)
6. Maintenance model ($40/month = $468 profit per year)

**Next customer call:** "I'll have your site live in 3 days on your custom domain."

---

**Ready to start building?**
