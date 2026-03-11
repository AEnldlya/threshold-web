# Maton API - Universal Service Integration

**Connect 80+ services (Slack, Gmail, Notion, Stripe, Salesforce, GitHub, etc.) with natural language commands**

## What It Does

Maton is a universal API that lets you interact with 80+ services through simple natural language:
- "Send a Slack message to #general"
- "List my Stripe customers"
- "Add a row to my Google Sheet"
- "Create a Notion database entry"
- "Send an email via Gmail"
- "Create a GitHub issue"
- And hundreds more...

## Setup (4 Steps - 10 minutes)

### Step 1: Get API Key
1. Sign up at https://maton.ai
2. Go to Settings
3. Copy your API key

### Step 2: Add to Environment
```bash
echo 'export MATON_API_KEY="your-key-here"' >> ~/.profile
source ~/.profile

# Verify
echo $MATON_API_KEY
```

### Step 3: Connect Services via OAuth
For each service you want (Slack, Gmail, Notion, Stripe, etc.):

```bash
python3 <<'EOF'
import urllib.request, os, json

# Change 'slack' to your service
data = json.dumps({'app': 'slack'}).encode()

req = urllib.request.Request(
  'https://ctrl.maton.ai/connections',
  data=data,
  method='POST'
)
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')

response = urllib.request.urlopen(req)
result = json.load(response)
print(json.dumps(result, indent=2))
EOF
```

This will return a URL. Open it in your browser to authorize.

### Step 4: Use It
Once connected, just ask naturally:
```
"Send a Slack message to #general: Website is live!"
"Create Stripe invoice for $2,500"
"Add Sarah Chen to Google Contacts"
"Create GitHub issue: Website Sarah Chen"
```

---

## Supported Services (80+)

### Communication
- Slack
- Telegram
- Discord
- Gmail
- Outlook
- Microsoft Teams

### Business Tools
- Stripe
- PayPal
- HubSpot
- Salesforce
- Pipedrive
- Monday.com

### Productivity
- Notion
- Google Sheets
- Airtable
- Asana
- Monday
- Linear

### Code & CI/CD
- GitHub
- GitLab
- Bitbucket
- CircleCI
- Jenkins

### And 40+ more...

---

## Integration with Your Business

### Prospect Management
```
"Add Sarah Chen (617) 555-0123 to Airtable Prospects table"
"Create Slack reminder: Call Sarah Chen at 2pm"
```

### Payment Collection
```
"Create Stripe invoice for $2,500 for Sarah Chen"
"Add payment to HubSpot deal"
```

### Website Building
```
"Create GitHub issue: Website Sarah Chen Salon"
"Send Slack notification: Website deployed!"
```

### Email Campaigns
```
"Send Gmail: proposal to sarah@example.com"
"Create Salesforce lead for Sarah Chen"
```

### Reporting
```
"Create Google Sheet summary: Revenue this month"
"Send Slack report: 15 businesses verified today"
```

---

## Real-World Examples for Your Agency

### Morning Verification Flow
```bash
# 1. Find businesses (browser-verify)
# 2. Add to Airtable (manual or Maton)
"Add Sarah Chen Salon to Airtable Prospects"

# 3. Send Slack reminder to call
"Send Slack message: Call Sarah Chen (617) 555-0123 today"
```

### When Client Says YES
```bash
# 1. Create GitHub issue
"Create GitHub issue: Website Sarah Chen Salon"

# 2. Generate Stripe link
"Create Stripe payment link for $2,500"

# 3. Send email
"Send Gmail: proposal to sarah@example.com with $2,500 link"

# 4. Notify team
"Send Slack: NEW CLIENT Sarah Chen $2,500"
```

### Website Deployment
```bash
# 1. Update Airtable
"Update Airtable: Sarah Chen status = Deployed"

# 2. Notify client
"Send Gmail: Your website is live at https://..."

# 3. Alert team
"Send Slack: Sarah Chen website LIVE!"

# 4. Log to CRM
"Create HubSpot deal: Sarah Chen $2,500"
```

### Recurring Revenue Tracking
```bash
# Monthly
"Create Google Sheet row: Sarah Chen, March 2026, $100 maintenance"
"Send Gmail: Monthly maintenance invoice $100"
"Update Stripe subscription status"
```

---

## Commands You Can Use

### Airtable
- "Add [name] to Airtable [table]"
- "Update Airtable [table]: [name] status = [status]"
- "Get Airtable [table] records"

### Stripe
- "Create Stripe payment link for $[amount]"
- "List Stripe customers"
- "Update Stripe subscription"

### GitHub
- "Create GitHub issue: [title]"
- "Create GitHub pull request: [title]"
- "List GitHub issues"

### Gmail
- "Send Gmail: [subject] to [email]"
- "Create Gmail draft with [content]"

### Slack
- "Send Slack message to #[channel]: [message]"
- "Create Slack reminder: [message] at [time]"

### Google Sheets
- "Add row to Google Sheet [name]: [data]"
- "Update Google Sheet [name]"

### Notion
- "Create Notion page: [name]"
- "Add to Notion database [name]: [data]"

---

## Why Maton is Powerful

✅ **80+ services** in one API (vs creating custom integrations)
✅ **Natural language** interface (no complex API calls)
✅ **OAuth-secured** (safe credential management)
✅ **Gateway-based** (api.maton.ai handles routing)
✅ **Extensible** (new services added regularly)

---

## Combining Maton with Your Existing Skills

**Your 7 Installed Skills:**
1. GitHub Operations → Use Maton instead
2. Stripe Payments → Use Maton instead
3. Airtable CRM → Use Maton for data updates
4. Email Outreach → Use Maton instead
5. Browser Verify → Keep as-is (custom verification)
6. Telegram Alerts → Use Maton instead
7. PDF Generator → Keep as-is (local generation)

**Maton covers:** GitHub, Stripe, Airtable, Email, Telegram (and 75+ more)

---

## Alternative Workflows

### Before (7 separate skills)
```bash
stripe payment_links create --amount 250000
email send client@example.com proposal
github issue create "Website Sarah Chen"
airtable add-prospect "Sarah Chen"
telegram-alerts "Sarah Chen" "NEW"
```

### After (Maton - natural language)
```bash
"Create Stripe $2,500 link, send to sarah@example.com, 
 create GitHub issue, add to Airtable, notify Slack"
```

Maton handles all of it in one request!

---

## Setup for Your Workspace

```bash
# 1. Get API key from https://maton.ai
# 2. Add to environment
export MATON_API_KEY="your-key"

# 3. Connect Stripe
python3 <<'EOF'
import urllib.request, os, json
data = json.dumps({'app': 'stripe'}).encode()
req = urllib.request.Request('https://ctrl.maton.ai/connections', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.load(urllib.request.urlopen(req)))
EOF

# 4. Connect Airtable (same pattern, change 'stripe' to 'airtable')
# 5. Connect GitHub
# 6. Connect Gmail
# 7. Connect Slack

# 8. Use it!
"Create Stripe $2,500 payment link for Sarah Chen"
```

---

## Cost & Availability

- **Sign up**: https://maton.ai
- **Pricing**: Check their pricing page (likely free tier + paid)
- **Services**: 80+ and growing
- **Documentation**: https://docs.maton.ai

---

## Next Steps

1. Get API key from https://maton.ai
2. Add to ~/.profile: `export MATON_API_KEY="..."`
3. Connect Stripe, Airtable, GitHub, Gmail, Slack (OAuth)
4. Start using natural language commands
5. Replace some of your 7 existing skills with Maton (optional)

---

## Maton vs Your Existing Skills

| Task | Skill | Maton | Winner |
|------|-------|-------|--------|
| Create Stripe link | ✅ Easy | ✅ Easy | Tie |
| Send email | ⚠️ Gmail setup | ✅ Simple | Maton |
| Create GitHub issue | ✅ CLI | ✅ Simple | Maton |
| Update Airtable | ⚠️ API calls | ✅ Simple | Maton |
| Telegram alerts | ✅ Configured | ✅ Via Maton | Tie |
| PDF generation | ✅ Custom | ❌ No | Skill |
| Business verification | ✅ Custom | ❌ No | Skill |

**Recommendation**: Keep custom skills (browser-verify, pdf-generator), use Maton for service integration (Stripe, Airtable, GitHub, Gmail, Slack)

---

## Learn More

- **Website**: https://maton.ai
- **Docs**: https://docs.maton.ai
- **API Gateway**: https://gateway.maton.ai
- **Control Panel**: https://ctrl.maton.ai
