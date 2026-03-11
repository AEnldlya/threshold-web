# Installed ClawHub Skills

All skills are installed and ready to use in your OpenClaw workspace.

## Tier 1: CRITICAL (Already Installed)

### 1. **github-operations**
- Manage website repo, PRs, issues
- Check Vercel deployment status
- Create issues for new clients
- Push commits automatically
- **Use**: When client says YES, create GitHub issue
- **Commands**: `gh issue create`, `gh pr create`, `gh run list`

### 2. **stripe-payments**
- Generate $2,500 payment links
- Create recurring $100/month invoices
- Track payment status
- Issue refunds if needed
- **Use**: Send payment link when website ready
- **Commands**: `stripe payment_links create`, `stripe invoices create`

### 3. **airtable-crm**
- Track prospects (1000+)
- Track verified businesses (300+)
- Manage clients (calls, builds, payments)
- Revenue dashboard
- **Use**: Single source of truth for all business data
- **Commands**: `airtable add-prospect`, `airtable mark-paid`

### 4. **email-outreach**
- Send proposals (Figma mockup ready)
- Send payment reminders
- Send website live notifications
- Monthly maintenance updates
- **Use**: Automated email sequences throughout build
- **Commands**: `email send [client] proposal`, `email send [client] live`

## Tier 2: HIGHLY USEFUL (Already Installed)

### 5. **browser-verify**
- Automate 6-point business verification
- Check if business has website
- Verify Google, Facebook, Instagram, domain, Yelp
- Save results to Airtable
- **Use**: Daily morning verification of 20-30 businesses
- **Commands**: `verify "Sarah Chen Salon" "Boston"`

### 6. **telegram-alerts**
- Send instant notifications
- Alert when client says YES
- Alert when payment received
- Daily verification report
- **Use**: Stay informed of business milestones
- **Commands**: `alert "Sarah Chen" "YES"`, `alert-daily`

### 7. **pdf-generator**
- Create professional proposals
- Generate invoices with payment links
- Build portfolio case studies
- Create specification documents
- **Use**: Send proposal Day 1, invoice Day 10
- **Commands**: `pdf proposal [client] $2500`, `pdf invoice [client]`

## Available Features by Skill

| Feature | Skill | Command |
|---------|-------|---------|
| Create client issue | github-operations | `gh issue create` |
| Check deployment | github-operations | `gh run list` |
| Payment link | stripe-payments | `stripe payment_links create` |
| Create invoice | stripe-payments | `stripe invoices create` |
| Add prospect | airtable-crm | `airtable add-prospect` |
| Mark paid | airtable-crm | `airtable mark-paid` |
| Show revenue | airtable-crm | `airtable check-revenue` |
| Send email | email-outreach | `email send [client] [template]` |
| Verify business | browser-verify | `verify [name] [city]` |
| Send alert | telegram-alerts | `alert [client] [event]` |
| Generate PDF | pdf-generator | `pdf [type] [client]` |

## Complete Workflow (End-to-End)

### Day 0: Find Prospects
1. **browser-verify**: Verify 20-30 businesses (6-point check)
2. **airtable-crm**: Store results in "Verified" table
3. **telegram-alerts**: Send daily report: "15 verified businesses ready"

### Day 1: Call & Sell
1. User calls 15 prospects
2. User reports back: "Sarah Chen said YES"
3. **airtable-crm**: Update status to "Interested"
4. **telegram-alerts**: Alert "NEW CLIENT: Sarah Chen $2,500!"

### Day 2: Send Proposal
1. **pdf-generator**: Create proposal PDF
2. **stripe-payments**: Generate payment link
3. **email-outreach**: Send proposal email with link
4. **airtable-crm**: Log proposal sent

### Days 3-9: Build Website
1. **github-operations**: Create issue, push commits
2. **telegram-alerts**: Send milestone alerts
3. **email-outreach**: Notify when Figma ready, when site ready

### Day 10: Get Paid & Launch
1. **stripe-payments**: Payment received alert
2. **telegram-alerts**: Alert "PAYMENT RECEIVED!"
3. **github-operations**: Merge to main (Vercel auto-deploys)
4. **email-outreach**: Send "Your website is LIVE!"
5. **airtable-crm**: Mark as "Paid" and "Active"

### Month 2+: Recurring
1. **email-outreach**: Send monthly maintenance updates
2. **airtable-crm**: Track as "Active Maintenance"
3. **stripe-payments**: Collect $100/month

## Installation Locations

All skills installed in: `~/.openclaw/workspace/skills/`

```
skills/
├── github-operations/
│   └── SKILL.md
├── stripe-payments/
│   └── SKILL.md
├── airtable-crm/
│   └── SKILL.md
├── email-outreach/
│   └── SKILL.md
├── browser-verify/
│   └── SKILL.md
├── telegram-alerts/
│   └── SKILL.md
├── pdf-generator/
│   └── SKILL.md
└── INSTALLED_SKILLS.md (this file)
```

## Reading Skills

To learn how to use each skill:

```bash
# View GitHub operations
cat ~/.openclaw/workspace/skills/github-operations/SKILL.md

# View Stripe setup
cat ~/.openclaw/workspace/skills/stripe-payments/SKILL.md

# View Airtable CRM
cat ~/.openclaw/workspace/skills/airtable-crm/SKILL.md

# View email outreach
cat ~/.openclaw/workspace/skills/email-outreach/SKILL.md

# View browser verify
cat ~/.openclaw/workspace/skills/browser-verify/SKILL.md

# View Telegram alerts
cat ~/.openclaw/workspace/skills/telegram-alerts/SKILL.md

# View PDF generator
cat ~/.openclaw/workspace/skills/pdf-generator/SKILL.md
```

## Setup Requirements

### GitHub
- GitHub CLI: `gh --version`
- Authenticated: `gh auth login`
- Repo: AEnldlya/summer-street-salon

### Stripe
- API key from: https://dashboard.stripe.com/apikeys
- Set env: `export STRIPE_API_KEY="sk_live_..."`
- Test: `stripe charges list`

### Airtable
- Account: https://airtable.com
- Create base: "Website Agency"
- API token from: https://airtable.com/account/tokens
- Set env: `export AIRTABLE_TOKEN="pat..."`

### Email (Gmail)
- 2FA enabled on Gmail
- App password created
- Set env: `export GMAIL_PASSWORD="app_password"`

### Telegram
- Already configured in OpenClaw
- Bot token: 8728512079:AAExeLiSEkkygUjzxQ1tcbcUZZ5S8KkQdq4
- Chat ID: 8613714567

## Quick Start (First Time)

1. **Set up Stripe** (5 min):
   - Copy API key from dashboard
   - `export STRIPE_API_KEY="sk_live_..."`
   - Test: `stripe charges list`

2. **Set up Airtable** (10 min):
   - Create base at https://airtable.com
   - Create tables: Prospects, Verified, Clients
   - Copy API token
   - `export AIRTABLE_TOKEN="pat..."`

3. **Set up Gmail** (5 min):
   - Enable 2FA at https://myaccount.google.com
   - Create app password
   - `export GMAIL_PASSWORD="xxxx xxxx xxxx xxxx"`

4. **Test each skill** (5 min):
   - GitHub: `gh status`
   - Stripe: `stripe charges list`
   - Airtable: Test API call (see SKILL.md)
   - Email: Send test email
   - Telegram: Send test message

5. **Start using**:
   - Run daily verification: `verify [business] [city]`
   - Log prospects: `airtable add-prospect`
   - Send emails: `email send [client] proposal`
   - Track revenue: `airtable check-revenue`

## Commands You'll Use Most

```bash
# Daily verification
verify "Sarah Chen Salon" "Boston"
verify-batch restaurants.csv

# Prospect management
airtable add-prospect "Sarah Chen" "Salon" "(617) 555-0123"
airtable list-verified

# When client says YES
email send sarahchen@example.com proposal
stripe payment_links create --amount 250000

# When payment received
airtable mark-paid "Sarah Chen"
telegram-alerts "Sarah Chen" "PAID"

# Website deployment
gh issue create "Website: Sarah Chen Salon"
gh pr create "Website: Sarah Chen - Complete"

# Check status
airtable check-revenue
github-operations list-repos
stripe charges list
```

## Troubleshooting

### Stripe not working
- Check API key: `echo $STRIPE_API_KEY`
- Verify format: `sk_live_...` or `sk_test_...`
- Test: `stripe charges list --limit 1`

### Airtable not working
- Check token: `echo $AIRTABLE_TOKEN`
- Verify format: `pat...`
- Test API: See SKILL.md for curl example

### Email not sending
- Check Gmail password: `echo $GMAIL_PASSWORD`
- Verify 2FA enabled: https://myaccount.google.com
- Test: Send test email from SKILL.md

### GitHub issues not creating
- Check auth: `gh auth status`
- Verify repo exists: `gh repo view AEnldlya/summer-street-salon`
- Test: `gh issue create --repo AEnldlya/summer-street-salon --title "test"`

## Next Steps

1. ✅ All skills installed
2. ⏭️ Set up integrations (Stripe, Airtable, Gmail)
3. ⏭️ Run daily verification (tomorrow 7 AM)
4. ⏭️ Wait for first YES from a prospect
5. ⏭️ Execute complete workflow (Day 0-10)

## Success Metrics

Once fully set up:
- 15 verified prospects per day
- 2-3 closes per week
- $5,000-7,500 revenue per week when pipeline fills
- All tracked in Airtable
- All automated via these skills

---

**See individual SKILL.md files for detailed usage, API keys, and examples.**
