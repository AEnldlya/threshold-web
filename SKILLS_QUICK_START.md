# ClawHub Skills - Quick Start Guide

All 7 skills installed and ready to go! 🚀

## Location

All skills live in: `~/.openclaw/workspace/skills/`

Each skill has a `SKILL.md` file with full documentation, setup, and examples.

---

## TL;DR - The 7 Skills You Now Have

### 1. **GitHub Operations** 🐙
**Manage your code, repos, deployments**
```bash
# What you can do
gh issue create "Website: Sarah Chen Salon"  # New project issue
gh pr create "Website complete, ready to deploy"
gh run list                                   # Check Vercel deployments
```
**Setup**: Already have GitHub CLI + account (AEnldlya)
**File**: `skills/github-operations/SKILL.md`

---

### 2. **Stripe Payments** 💳
**Collect $2,500 payments + recurring $100/month**
```bash
# What you can do
stripe payment_links create                   # Generate $2,500 link
stripe invoices create                        # Create recurring $100/mo
stripe charges list                           # Track payments
```
**Setup**: Get API key from https://dashboard.stripe.com/apikeys
**File**: `skills/stripe-payments/SKILL.md`

---

### 3. **Airtable CRM** 📊
**Track prospects → leads → clients → revenue**
```bash
# What you can do
airtable add-prospect "Sarah Chen" "Salon"   # Add new prospect
airtable mark-paid "Sarah Chen"              # Mark payment received
airtable check-revenue                       # View revenue dashboard
```
**Setup**: Create base at https://airtable.com, get API token
**File**: `skills/airtable-crm/SKILL.md`

---

### 4. **Email Outreach** 📧
**Automated proposal, payment reminder, live notification emails**
```bash
# What you can do
email send client@example.com proposal       # Send proposal Day 1
email send client@example.com payment        # Send payment reminder Day 8
email send client@example.com live           # "Your site is live!" Day 10
```
**Setup**: Gmail with 2FA + app password
**File**: `skills/email-outreach/SKILL.md`

---

### 5. **Browser Verify** 🔍
**Automate 6-point business verification**
```bash
# What you can do
verify "Sarah Chen Salon" "Boston"           # Run 6-point check
verify-batch restaurants.csv                 # Verify 100 businesses
```
**Setup**: Already have browser tools installed
**File**: `skills/browser-verify/SKILL.md`

---

### 6. **Telegram Alerts** 🔔
**Get instant notifications**
```bash
# What you can do
alert "Sarah Chen" "YES"                     # Alert: New client!
alert "Sarah Chen" "paid"                    # Alert: Payment received!
alert-daily                                  # Daily business report
```
**Setup**: Already configured in OpenClaw
**File**: `skills/telegram-alerts/SKILL.md`

---

### 7. **PDF Generator** 📄
**Professional proposals, invoices, portfolios**
```bash
# What you can do
pdf proposal "Sarah Chen" $2500              # Generate proposal PDF
pdf invoice "Sarah Chen" $2500               # Generate invoice
pdf case-study "sarah-chen-salon"            # Portfolio case study
```
**Setup**: npm install pdfkit puppeteer
**File**: `skills/pdf-generator/SKILL.md`

---

## The Complete Workflow (Using All 7 Skills)

```
MORNING (7 AM):
  browser-verify → Find 20-30 Boston businesses
  airtable-crm → Log verified businesses
  telegram-alerts → Send daily report (15 verified ready to call)

DAY 1 (Client says YES):
  airtable-crm → Update status to "Interested"
  stripe-payments → Generate payment link
  telegram-alerts → Alert "NEW CLIENT: Sarah Chen $2,500!"

DAY 2 (Send proposal):
  pdf-generator → Create proposal PDF
  email-outreach → Send proposal with Stripe link
  airtable-crm → Log proposal sent

DAY 5 (Design ready):
  email-outreach → "Figma mockup ready for review"
  telegram-alerts → "Design approval needed by Friday"

DAY 8 (Website ready):
  email-outreach → "Your website is ready for review"
  telegram-alerts → "Website preview ready"
  pdf-generator → Create preview PDF

DAY 10 (Payment + Deploy):
  stripe-payments → Payment received ✅
  telegram-alerts → "PAYMENT RECEIVED! $2,500"
  github-operations → Merge to main branch
  email-outreach → "Your website is LIVE at [URL]!"
  airtable-crm → Mark as "Paid" + "Active"

MONTH 2+ (Recurring):
  email-outreach → Monthly maintenance updates
  airtable-crm → Track as "Active Maintenance"
  stripe-payments → Collect $100/month
```

---

## Quick Setup Checklist (30 minutes)

- [ ] **GitHub**: Already done (have account + CLI)
- [ ] **Stripe**: Get API key (5 min) → `export STRIPE_API_KEY="sk_live_..."`
- [ ] **Airtable**: Create account (5 min) → Create base → Get token → `export AIRTABLE_TOKEN="pat..."`
- [ ] **Gmail**: Enable 2FA (5 min) → Create app password → `export GMAIL_PASSWORD="..."`
- [ ] **Browser tools**: `npm install puppeteer playwright` (5 min)
- [ ] **Test each**: Run 1 command per skill (5 min)

---

## Commands by Use Case

### "I found a new prospect"
```bash
airtable add-prospect "Sarah Chen Salon" "Salon" "(617) 555-0123"
browser-verify "Sarah Chen Salon" "Boston"
```

### "Client said YES!"
```bash
airtable mark-interested "Sarah Chen Salon"
stripe payment_links create --amount 250000
pdf proposal "Sarah Chen" $2500
email send sarahchen@example.com proposal
telegram-alerts "Sarah Chen" "YES"
```

### "Website is ready, need payment"
```bash
email send sarahchen@example.com payment
telegram-alerts "Sarah Chen" "READY_FOR_PAYMENT"
```

### "Payment received, deploying!"
```bash
airtable mark-paid "Sarah Chen"
github-operations push main
telegram-alerts "Sarah Chen" "PAID_AND_LIVE"
email send sarahchen@example.com live
```

### "Need business report"
```bash
airtable check-revenue                    # Show pipeline value
telegram-alerts "send-daily-report"       # Full daily summary
```

---

## File Locations & Details

```
~/.openclaw/workspace/
├── skills/
│   ├── INSTALLED_SKILLS.md                    ← Master index (read this)
│   ├── github-operations/SKILL.md            ← GitHub reference
│   ├── stripe-payments/SKILL.md              ← Stripe setup & usage
│   ├── airtable-crm/SKILL.md                 ← CRM database setup
│   ├── email-outreach/SKILL.md               ← Email templates & automation
│   ├── browser-verify/SKILL.md               ← Business verification automation
│   ├── telegram-alerts/SKILL.md              ← Notification setup
│   └── pdf-generator/SKILL.md                ← PDF generation templates
├── CLAWHUB_SKILLS_RECOMMENDED.md             ← Original recommendations
└── SKILLS_QUICK_START.md                     ← This file
```

---

## Environment Variables to Set

```bash
# Stripe
export STRIPE_API_KEY="sk_live_..."

# Airtable
export AIRTABLE_TOKEN="pat..."
export AIRTABLE_BASE_ID="app..."

# Gmail
export GMAIL_EMAIL="Andy.li.zhang2010@gmail.com"
export GMAIL_PASSWORD="your_app_password"

# GitHub (optional, likely already configured)
export GITHUB_REPO="AEnldlya/summer-street-salon"
```

Add to `~/.bash_profile` or `~/.zshrc` to persist:
```bash
echo 'export STRIPE_API_KEY="sk_live_..."' >> ~/.bash_profile
source ~/.bash_profile
```

---

## Testing Each Skill (5 seconds per skill)

```bash
# GitHub
gh status

# Stripe  
stripe charges list --limit 1

# Airtable
# Run curl command from skills/airtable-crm/SKILL.md

# Email
# Send test from skills/email-outreach/SKILL.md

# Browser
npm list puppeteer

# Telegram
# Already works (preconfigured)

# PDF
npm list pdfkit
```

---

## When Things Break

**Stripe not working?**
- Check: `echo $STRIPE_API_KEY` 
- Fix: Get new key from https://dashboard.stripe.com/apikeys
- Test: `stripe charges list`

**Airtable not working?**
- Check: `echo $AIRTABLE_TOKEN`
- Fix: Create new token at https://airtable.com/account/tokens
- Test: See curl example in SKILL.md

**Email not sending?**
- Check: Gmail 2FA enabled
- Check: App password created
- Fix: https://myaccount.google.com/apppasswords
- Test: See template in SKILL.md

**GitHub issues not creating?**
- Check: `gh auth status`
- Check: Repo exists `gh repo view AEnldlya/summer-street-salon`
- Fix: Re-auth with `gh auth login`

---

## Next Steps

1. **Read INSTALLED_SKILLS.md** (comprehensive reference)
2. **Set up integrations** (Stripe, Airtable, Gmail) - 20 min
3. **Test each skill** (one command per skill) - 5 min
4. **Tomorrow 7 AM**: Run first verification - `verify [business] [city]`
5. **When first client says YES**: Execute complete workflow

---

## Success Metrics (Once Fully Set Up)

- 15 verified prospects/day ✅
- 2-3 closes/week ✅
- $5K-7.5K revenue/week ✅
- All tracked in Airtable ✅
- All automated via skills ✅

---

## Keep This Handy

Save this file locally:
```bash
cp ~/.openclaw/workspace/SKILLS_QUICK_START.md ~/Desktop/
```

Or print the individual skill docs:
```bash
# Print all skills
cat ~/.openclaw/workspace/skills/*/SKILL.md | less
```

---

**You're all set! Start with the morning verification tomorrow at 7 AM.** 🚀
