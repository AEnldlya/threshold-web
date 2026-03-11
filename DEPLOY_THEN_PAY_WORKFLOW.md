# Deploy Then Pay Workflow
## Show Website → They Pay → Move to Permanent Domain

---

## THE FLOW

**Traditional (risky for you):**
- You build site → Customer sees mockup → They pay → You deploy

**Better (builds trust):**
- You build site → Deploy to temp URL → Customer sees **live, working website** → They pay → You move to permanent domain

**Why this works:**
- ✅ Customers see actual working website (not screenshot/mockup)
- ✅ Can test contact form, mobile, everything
- ✅ Zero doubt it will work
- ✅ Builds massive trust
- ✅ If they don't pay, you shut down temp site (no loss to you)
- ✅ Higher conversion rate (seeing working site = higher confidence)

---

## YOUR WORKFLOW

### Day 1-2: Build Website
- [ ] Create website files locally
- [ ] Add their photos + content
- [ ] Test everything (pages, forms, mobile, speed)
- [ ] Confirm it's perfect

### Day 3: Deploy to TEMPORARY URL
- [ ] Deploy to Netlify (`bob-plumbing-temp.netlify.app`)
- [ ] Send customer temporary link
- [ ] Message: "Your website is live! Check it out. Everything working?"

### Day 4: They Review & Pay
- [ ] Customer reviews website
- [ ] Customer clicks contact form, tests it
- [ ] Customer sees it on mobile, desktop
- [ ] Customer pays $500 via PayPal
- [ ] Once paid → You move to permanent domain

### Day 5: Go Permanent
- [ ] Register domain (if not done)
- [ ] Move website from temp URL to permanent domain
- [ ] Done

---

## IMPLEMENTATION: AUTOMATED DEPLOYMENT BY ME

**I can deploy by myself if you give me one of these:**

### Option A: Netlify API Token (Easiest)

**Setup (you do once):**
1. Go to Netlify → Account settings
2. Click: "Applications" → "Personal access tokens"
3. Create token → Copy it
4. Give me the token

**Then I can:**
```bash
# I run this command:
netlify deploy --auth=[YOUR_TOKEN] --dir=bob-plumbing-site

# Website deploys instantly to temp URL
# I send you the link: bob-plumbing-site.netlify.app
```

**You tell me:**
- Folder path: `/path/to/bob-plumbing-site/`
- Temporary site name: `bob-plumbing-temp` (I deploy as `bob-plumbing-temp.netlify.app`)

**I do the rest.**

---

### Option B: GitHub + Netlify Connected (Best for updates)

**Setup (you do once):**
1. Create GitHub repo: `bob-plumbing-site`
2. Push website files to GitHub
3. Connect GitHub repo to Netlify (auto-deploys)
4. Give me GitHub repo URL + Netlify site name

**Then I can:**
```bash
# I push updates to GitHub
git push origin main

# Netlify auto-deploys automatically
# Website updates instantly
```

**You tell me:**
- GitHub repo URL
- GitHub branch (usually `main`)
- Your GitHub token (if private repo)

**I do the rest.**

---

### Option C: Netlify Site Key (For direct uploads)

**Setup (you do once):**
1. Create Netlify site: `bob-plumbing-temp.netlify.app`
2. Get the "Site ID" from Netlify dashboard
3. Give me Site ID + API token

**Then I can:**
```bash
# I upload website directly
netlify deploy --site-id=[ID] --auth=[TOKEN] --dir=bob-plumbing-site

# Done
```

---

## WHAT I NEED FROM YOU (ONE-TIME SETUP)

### Minimal Setup (5 minutes):
1. Create Netlify account (free, if not done)
2. Go to: Netlify → Account settings → Personal access tokens
3. Create token
4. Copy token → Send to me securely

That's it. After that, I can deploy any website instantly.

---

## WORKFLOW WITH ME DEPLOYING

**When you finish building website:**

You message me:
```
Website ready for deployment.

Folder: /home/clawdbot/.openclaw/workspace/bob-plumbing-site/
Customer: Bob's Plumbing (Denver)
Temp site name: bob-plumbing-temp

Deploy when ready.
```

**I do:**
```bash
# 1. Deploy to temp URL
netlify deploy --auth=[YOUR_TOKEN] --dir=bob-plumbing-site/

# 2. Confirm deployment
# 3. Send you temp URL: bob-plumbing-temp.netlify.app
# 4. Log in tracking system
```

**You:**
```
Message customer:
"Your website is live! Check it out here: bob-plumbing-temp.netlify.app

Try the contact form, check mobile, let me know if changes needed."
```

**Customer reviews → Pays $500 → You tell me to move to permanent domain**

```bash
# I move from temp to permanent
netlify deploy --site-id=[PERMANENT_SITE_ID] --dir=bob-plumbing-site/

# Website now live on bobsplumbing-denver.com
# Done
```

---

## PAYMENT FLOW

**Customer sees working site on temp URL:**
- ✅ Homepage loads
- ✅ Services page works
- ✅ Contact form sends
- ✅ Mobile looks good
- ✅ No errors

**Customer confidence: 100%** → Pays immediately

---

## IF THEY DON'T PAY

**You message me:**
"Bob didn't pay. Shut down temp site."

**I do:**
```bash
# Delete temp site
netlify delete-site --site-id=[TEMP_SITE_ID]

# Website gone, temp URL dead
# Zero loss to you, zero wasted resources
```

**Customer can't access website → Realizes they need to pay → Pays or walks**

---

## WORKFLOW SUMMARY

| Step | You | Me |
|------|-----|-----|
| 1. Build website | Build on your computer | — |
| 2. Test locally | Test everything | — |
| 3. Ready to show | Tell me: "Deploy to temp URL" | Deploy website |
| 4. Temp URL live | — | Send you live link |
| 5. Customer reviews | Send link to customer | — |
| 6. Customer pays | Collect $500 PayPal | — |
| 7. Move to permanent | Tell me: "Move to permanent domain" | Deploy to permanent |
| 8. Live | Website on their custom domain | — |
| OR if no pay | Tell me: "Shut it down" | Delete temp site |

---

## CREDIBILITY BOOST

**What customer sees:**
- "Here's your live website" (not mockup)
- They can test everything
- See it on their phone
- Try contact form
- See reviews, pages, everything working

**Result:**
- 100% confidence it will work
- Happy to pay
- Trusts you completely
- Refers other businesses to you

---

## HOW TO GET NETLIFY TOKEN

**5-minute setup:**

1. Go to: https://netlify.com
2. Sign in (or create account)
3. Click: Your avatar (top right)
4. Click: "User settings"
5. Click: "Applications" tab
6. Click: "New access token"
7. Copy the token
8. Give it to me (keep it secure)

**That token = me deploying permission**

---

## TEMPLATE MESSAGE TO CUSTOMER

Once website is deployed to temp URL:

```
Hi Bob,

Your website is ready! Check it out here:
https://bob-plumbing-temp.netlify.app

Everything should be working:
✓ Homepage
✓ Services page
✓ Contact form (try sending yourself a test)
✓ Mobile (check on your phone)
✓ Reviews

Let me know if you want any changes, then we'll move it to your permanent domain (bobsplumbing-denver.com) and you'll pay the $500.

Sound good?

Andy
```

---

## SECURITY NOTE

**Netlify token is sensitive:**
- Don't post publicly
- Share with me securely (DM, encrypted, etc.)
- Can be revoked anytime if leaked
- I only use it to deploy your sites

---

## READY TO IMPLEMENT?

**Tell me when:**
1. You have your Netlify account + token
2. First website is built and tested locally
3. Ready for me to deploy to temp URL

**Then:**
```
Message me: "Deploy bob-plumbing-site to temp URL"

I run:
netlify deploy --auth=[TOKEN] --dir=./bob-plumbing-site/

You get: "Your website is live at: bob-plumbing-temp.netlify.app"

Done.
```

---

**This is the trust-building workflow that closes more deals.**

Let me know when you have the Netlify token + first site ready.
