# ClawHub Skills - Recommended for Website Agency

## Installation Quick Start

```bash
npm install -g clawhub          # Install ClawHub CLI
clawhub login                   # Authenticate with GitHub
clawhub search "skill-name"     # Search for skills
clawhub install skill-slug      # Install a skill
clawhub update --all            # Update all installed skills
```

---

## Tier 1: CRITICAL (Install First)

### 1. **github** ⭐⭐⭐⭐⭐
**Why:** Manage your entire salon website repo, issues, PRs, and deployment pipeline
```bash
clawhub install github
```
**Use Cases:**
- Create issues for client projects
- Manage pull requests and code reviews
- Check CI/CD status (Vercel deployments)
- Push commits automatically
- Manage branches for different clients

**For Your Work:**
- Track website builds as GitHub issues
- Auto-create PR for each completed website
- Check Vercel deployment status before client preview
- Manage AEnldlya/summer-street-salon repo

---

### 2. **stripe** ⭐⭐⭐⭐⭐
**Why:** Collect $2,500 website payments from clients (essential for business)
```bash
clawhub install stripe
```
**Use Cases:**
- Generate payment links for new websites
- Track invoice status
- Create recurring billing for $100/month maintenance
- Issue refunds if needed
- Monitor payment failures

**For Your Work:**
- Generate $2,500 payment link when client says YES
- Create $100/month maintenance invoice
- Track client payment history
- Automate invoice reminders

---

### 3. **airtable** ⭐⭐⭐⭐⭐
**Why:** CRM system to track prospects → leads → clients → revenue
```bash
clawhub install airtable
```
**Use Cases:**
- Store all Boston business prospects (name, phone, email, category)
- Track call history and outcomes (YES/NO/MAYBE)
- Manage website builds (status: discovery → design → dev → deploy)
- Forecast revenue (pipeline value)
- Report on win rate and LTV per client

**For Your Work:**
- Verified prospects database (link to VERIFICATION_RULES.md)
- "Interested" (called) vs "Closed" (paid) pipeline
- Website project tracking (15 builds → $37,500 revenue)
- Maintenance clients tracking ($100/month recurring)
- Monthly revenue dashboard

---

### 4. **email** or **himalaya** ⭐⭐⭐⭐
**Why:** Send proposals, payment reminders, delivery confirmations
```bash
clayhub install himalaya
```
**Use Cases:**
- Send "Your website is ready for review" emails
- Payment reminders ("We've built your site, click here to pay")
- Delivery confirmations when website goes live
- Maintenance renewal notices (month 12)

**For Your Work:**
- Automated email sequence:
  - Day 1: "Kickoff discovery call confirmed"
  - Day 5: "Figma mockup ready for approval"
  - Day 8: "Website ready on Netlify for review"
  - Day 10: "Payment received, site live!"
  - Month 2: "Website maintenance update"

---

## Tier 2: HIGHLY USEFUL (Install Next)

### 5. **browser** ⭐⭐⭐⭐
**Why:** Verify businesses (check if they have websites)
```bash
clawhub install browser
```
**Use Cases:**
- Screenshot competitor websites
- Verify business websites exist/don't exist
- Check Google Business Profile
- Monitor website performance
- Take before/after screenshots for portfolio

**For Your Work:**
- 6-point verification automation (VERIFICATION_RULES.md)
- Screenshot salon websites for portfolio
- Check if businesses have website changes
- Verify Vercel deployment successful

---

### 6. **slack** or **telegram** ⭐⭐⭐⭐
**Why:** Instant notifications (you're already using Telegram)
```bash
clawhub install telegram
```
**Use Cases:**
- Alert when client calls YES (start building!)
- Notify when website deployed and ready
- Payment received notification
- Daily business verification summary

**For Your Work:**
- "New client: Sarah Chen (Boston Salon) $2,500"
- "Website live: summer-street-salon.vercel.app"
- "Payment received! $500"
- "15 verified businesses found today"

---

### 7. **pdf-generator** ⭐⭐⭐⭐
**Why:** Create professional proposals and invoices
```bash
clayhub install pdf-generator
```
**Use Cases:**
- Generate proposal PDF before kickoff
- Create invoice PDFs for payment
- Portfolio PDF for pitching
- Website specification document

**For Your Work:**
- "Website_Proposal_SarahChen_$2500.pdf"
- Invoice with payment link (Stripe)
- Portfolio: "10 Completed Salon Websites"

---

### 8. **scheduling** ⭐⭐⭐
**Why:** Calendar management for discovery calls and reviews
```bash
clayhub install scheduling
```
**Use Cases:**
- Schedule discovery call with interested prospect
- Calendar reminder for website review (day 8)
- Schedule maintenance review calls
- Track busy/free time

**For Your Work:**
- "Discovery call: Sarah Chen, Sat 2pm, 30 min"
- Auto-reminder: "Website review call in 1 hour"
- Monthly "maintenance check-in" slots

---

## Tier 3: NICE TO HAVE (Install Later)

### 9. **seo-audit** ⭐⭐⭐
**Why:** Verify website meets quality standards before launch
```bash
clayhub install seo-audit
```
**Use Cases:**
- Verify Lighthouse 95+
- Check WCAG AA compliance
- Core Web Vitals check
- Meta tags validation

**For Your Work:**
- Final QA before client payment
- Prove Lighthouse 95+ achievement
- SEO health report for client

---

### 10. **screenshot** ⭐⭐⭐
**Why:** Capture website screenshots across devices
```bash
clayhub install screenshot
```
**Use Cases:**
- Mobile/tablet/desktop screenshots
- Before/after comparison
- Portfolio showcase images
- Client preview mockups

**For Your Work:**
- "Your website on iPhone/iPad/Desktop" images
- Portfolio: 3-device mockups per completed site
- Client case study images

---

### 11. **analytics** ⭐⭐
**Why:** Track website performance and traffic
```bash
clayhub install analytics
```
**Use Cases:**
- Google Analytics integration
- Monthly traffic reports for clients
- Bounce rate monitoring
- Conversion tracking

**For Your Work:**
- Month 2 client report: "You got 450 visitors, 15 calls"
- Maintenance value justification
- Portfolio metrics ("Avg 200 visits/month")

---

### 12. **backup/versioning** ⭐⭐
**Why:** Automatic website backups and version control
```bash
clayhub install backup
```
**Use Cases:**
- Backup website before changes
- Rollback if something breaks
- Archive old versions

**For Your Work:**
- "Website version 1.2 restored (client requested old design)"
- Disaster recovery for client sites

---

## Setup Workflow

### Step 1: Install Core Skills
```bash
clayhub install github
clayhub install stripe
clayhub install airtable
clayhub install himalaya
```

### Step 2: Verify Installation
```bash
clayhub list        # Show all installed skills
```

### Step 3: Configure Integrations
```bash
# GitHub - already authenticated via git
# Stripe - get API key from dashboard
# Airtable - create base, get API token
# Email - configure SMTP or Gmail
```

### Step 4: Build Your First Automation
Use these together:
1. **Airtable**: Store prospects
2. **Browser**: Verify no website exists
3. **Stripe**: Generate payment link when ready
4. **Email**: Send "site is ready" notification
5. **Slack/Telegram**: Alert you to take next step

---

## Automation Blueprint: Website Pipeline

```
PROSPECT FOUND (Airtable)
    ↓
VERIFY NO WEBSITE (Browser)
    ↓
PHONE CALL (Manual, but Airtable tracks)
    ↓
CLIENT SAYS YES
    ↓
SEND PROPOSAL (PDF Generator + Email)
    ↓
RECEIVE PAYMENT (Stripe)
    ↓
BUILD WEBSITE (GitHub + Coding)
    ↓
WEBSITE READY (Browser screenshot)
    ↓
SEND FINAL LINK (Email)
    ↓
DEPLOY LIVE (GitHub → Vercel)
    ↓
INVOICE PAID ✅
```

---

## Where to Find Them

**Visit:** https://clawhub.ai/
**Search:** Type skill name or use CLI

```bash
clayhub search "invoice"           # Find billing skills
clayhub search "website builder"   # Find web skills
clayhub search "scheduling"        # Find calendar skills
```

---

## Priority Installation Order

**Week 1 (Core):**
```bash
clayhub install github
clayhub install stripe
clayhub install airtable
```

**Week 2 (Notifications):**
```bash
clayhub install himalaya
clayhub install telegram
clayhub install pdf-generator
```

**Week 3+ (Polish):**
```bash
clayhub install scheduling
clayhub install seo-audit
clayhub install analytics
```

---

## Tips

✅ **Do:**
- Start with GitHub + Stripe + Airtable (the core trio)
- Use Telegram for real-time alerts (you already configured it)
- Test skills in your workspace before production use

❌ **Don't:**
- Install every skill at once (focus on what you need)
- Skip GitHub (it's essential for your workflow)
- Manually track clients in spreadsheets (use Airtable instead)

---

## Commands You'll Use Most

```bash
# Check what's installed
clayhub list

# Update all to latest versions
clayhub update --all

# Search for specific skill
clayhub search "invoice generator"

# Install specific version
clayhub install skill-name --version 2.0.0

# Publish your own skill
clayhub publish ./my-skill --slug my-skill --name "My Skill" --version 1.0.0
```

---

## Example: Complete Client Lifecycle

**Day 1: Discovery**
- Create Airtable record for Sarah Chen
- Send email: "Discovery call scheduled for Saturday 2pm"
- Calendar: Reminder 24h before

**Day 5: Proposal**
- Verify website requirements in discovery notes
- Generate PDF proposal with Stripe payment link
- Email: "Your proposal is ready"
- Slack: "Sent proposal to Sarah Chen"

**Day 8: Website Ready**
- Take screenshots (mobile/tablet/desktop)
- Run SEO audit (verify Lighthouse 95+)
- Generate preview PDF
- Email: "Your website is ready! Review at: [link]"

**Day 9: Client Review**
- Slack: "Sarah approved! Waiting on payment"
- Email: Payment reminder

**Day 10: Payment + Launch**
- Stripe webhook: Payment received
- GitHub: Merge production branch
- Vercel: Deploy live
- Email: "Website is live!"
- Slack: "Sarah Chen website launched! 🎉"
- Airtable: Mark as "Closed - Paid"

**Month 2+: Recurring**
- Email: Monthly maintenance check-in
- Airtable: Track as "Active Maintenance Client"

---

## Revenue Tracking with Airtable

Create an Airtable view called "Revenue Dashboard":

```
Client Name  | Status    | Website Cost | Monthly | Total (12mo)
Sarah Chen   | Paid      | $2,500       | $100    | $3,700
Mike Smith   | Build     | $2,500       | TBD     | TBD
...
TOTAL: 15 clients × $2,500 = $37,500 + 12 × $100 = $39,200/year
```

---

## Next Steps

1. **Install CLI:** `npm install -g clayhub`
2. **Login:** `clayhub login`
3. **Install core 3:** GitHub, Stripe, Airtable
4. **Configure:** Add your API keys
5. **Build first automation:** Prospect → Verify → Track
6. **Document:** Update this file as you add skills

---

**See:** https://clawhub.ai/ for full skill directory
**Docs:** https://docs.openclaw.ai/tools/clawhub
