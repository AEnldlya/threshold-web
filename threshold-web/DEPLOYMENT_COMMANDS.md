# Deployment Commands
## How to Deploy Websites Automatically

---

## YOUR NETLIFY TOKEN IS STORED ✅

Token saved securely at: `.netlify_token`

I can now deploy websites automatically.

---

## WORKFLOW

### Step 1: You Build Website
```
Create folder: ./bob-plumbing-site/
Add: index.html, css/, js/, images/
Test locally
```

### Step 2: Deploy to Temporary URL
```bash
python3 deploy_website.py temp ./bob-plumbing-site bob-plumbing-temp
```

**Output:**
```
✓ DEPLOYMENT SUCCESSFUL
Temporary URL: https://bob-plumbing-temp.netlify.app
```

You send customer: "Check out your website: https://bob-plumbing-temp.netlify.app"

### Step 3: Customer Reviews & Pays
Customer tests website, pays $500

### Step 4: Deploy to Permanent Domain
You create Netlify site for permanent domain first:
```bash
# Go to netlify.com → Create new site → Get Site ID
```

Then deploy:
```bash
python3 deploy_website.py permanent ./bob-plumbing-site abc123def456
```

**Output:**
```
✓ PERMANENT DEPLOYMENT SUCCESSFUL
Website now live on: bobsplumbing-denver.com
```

### Step 5: If No Payment
```bash
python3 deploy_website.py delete bob-plumbing-temp
```

**Website deleted.** Customer can no longer access it.

---

## COMPLETE EXAMPLE

**Customer: Bob's Plumbing, Denver**

### Day 1-2: Build
```
Build website files locally
Create folder: ./bob-plumbing-site/
Test everything
```

### Day 3: Show Customer
```bash
python3 deploy_website.py temp ./bob-plumbing-site bob-plumbing-temp
```

Get back:
```
Temporary URL: https://bob-plumbing-temp.netlify.app
```

Message customer:
```
"Your website is live! Check it out: https://bob-plumbing-temp.netlify.app

Test the contact form, check mobile, reviews section, everything.
Let me know if any changes needed. Once you approve, pay the $500 and I'll move it to your permanent domain (bobsplumbing-denver.com)."
```

### Day 4: Customer Approves & Pays
Customer sends $500 via PayPal

You:
1. Confirm payment received
2. Create permanent Netlify site (if not done): `bobsplumbing-denver.com`
3. Get Site ID from Netlify dashboard
4. Deploy permanently

```bash
python3 deploy_website.py permanent ./bob-plumbing-site site-id-123456
```

### Day 4: Website Goes Live
```
Website now live on: https://bobsplumbing-denver.com
Register domain, point DNS, done
```

### Day 5: Setup Maintenance (Optional)
Offer $40/month maintenance: "I'll keep it updated, monitor performance, and provide support."

---

## COMMANDS REFERENCE

### Deploy to Temporary URL
```bash
python3 deploy_website.py temp <folder> <site-name>
```

**Example:**
```bash
python3 deploy_website.py temp ./bob-plumbing-site bob-plumbing-temp
```

**Output:**
```
Temporary URL: https://bob-plumbing-temp.netlify.app
```

---

### Deploy to Permanent Domain
```bash
python3 deploy_website.py permanent <folder> <site-id>
```

**Example:**
```bash
python3 deploy_website.py permanent ./bob-plumbing-site abc123def456
```

**Note:** Get site ID from Netlify dashboard:
1. Go to netlify.com
2. Create new site for the domain
3. Copy "Site ID" from settings
4. Use in command above

---

### Delete Temporary Site (No Payment)
```bash
python3 deploy_website.py delete <site-id>
```

**Example:**
```bash
python3 deploy_website.py delete bob-plumbing-temp
```

**Result:** Website deleted, customer can no longer access it

---

## TRACKING

All deployments logged in: `deployments_log.json`

Shows:
- When deployed
- Which sites
- Status (active/deleted)
- URLs

---

## SETUP PERMANENT NETLIFY SITES

**Before you can deploy permanently, you need to create sites in Netlify:**

1. Go to: https://netlify.com
2. Click: "Add new site"
3. Site name: Use customer's domain or a reference name
4. Once created, go to Settings → Copy "Site ID"

**Example setup:**
```
Site: Bob's Plumbing
Site ID: a1b2c3d4e5f6g7h8
Domain: bobsplumbing-denver.com
Register domain, point DNS to Netlify nameservers
```

---

## DEPLOYMENT TIMELINE

| When | Action | Command |
|------|--------|---------|
| Build day | You build website locally | — |
| Show customer | Deploy to temp URL | `python3 deploy_website.py temp ./site bob-temp` |
| Customer reviews | They check temp site | Send them: `bob-temp.netlify.app` |
| Payment arrives | Customer pays $500 | Confirm PayPal |
| Go permanent | Deploy to permanent domain | `python3 deploy_website.py permanent ./site site-id` |
| Live | Website on their domain | `bobsplumbing-denver.com` live |
| No payment | Shut it down | `python3 deploy_website.py delete bob-temp` |

---

## WHAT I'LL DO AUTOMATICALLY

When you message me:
```
"Deploy bob-plumbing-site to temp URL"
```

I run:
```bash
python3 deploy_website.py temp ./bob-plumbing-site bob-plumbing-temp
```

And reply:
```
✓ Deployment successful
Temporary URL: https://bob-plumbing-temp.netlify.app

Send this to customer and have them review.
```

---

## WHEN YOU'RE READY

**First website build:**
1. Create folder: `./bob-plumbing-site/`
2. Add all files (HTML, CSS, JS, images)
3. Test locally
4. Message me: "Deploy bob-plumbing-site to temp URL"

**I deploy instantly** → You get temp URL → Send to customer

---

## SECURITY

- Token is stored locally in `.netlify_token`
- Never exposed in scripts or logs
- Only used for deployments
- Can be revoked anytime in Netlify account

---

**System is ready. Build your first website and message me when it's ready to deploy.**
