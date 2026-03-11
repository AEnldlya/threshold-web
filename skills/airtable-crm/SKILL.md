# Airtable CRM

**Track prospects, leads, clients, and revenue. Single source of truth for your business.**

## What It Does

Airtable manages:
- **Prospects**: All Boston businesses found (1000+)
- **Verified**: Passed 6-point check (300+)
- **Interested**: Said YES to call (20-50/week)
- **Clients**: Paid $2,500 and in build (2-5 active)
- **Revenue**: Track $$ per client, LTV, MRR

## Setup

1. Create Airtable account: https://airtable.com
2. Create new base called "Website Agency"
3. Get API token from: https://airtable.com/account/tokens
4. Store as environment variable:
   ```bash
   export AIRTABLE_TOKEN="patXXXXXXXXXXXXXX"
   export AIRTABLE_BASE_ID="appXXXXXXXXXXXXXX"
   ```

## Create Tables

### 1. **Prospects Table**
```
Fields:
- Business Name (text)
- Category (dropdown: Salon, Restaurant, Plumber, etc.)
- Phone (phone)
- Email (email)
- Address (text)
- Found Date (date)
- Source (dropdown: Google Maps, Yelp, Local directory)
- Notes (long text)
```

### 2. **Verified Table**
```
Link to Prospects
- Check 1: No Google website (checkbox)
- Check 2: No GBP website (checkbox)
- Check 3: No Facebook website (checkbox)
- Check 4: No Instagram link (checkbox)
- Check 5: No direct domain (checkbox)
- Check 6: No Yelp website (checkbox)
- Status (dropdown: Ready to Call, Called, Interested, Not Interested)
- Date Verified (date)
```

### 3. **Clients Table**
```
Link to Prospects
- Status (dropdown: Discovery, Design, Build, Deploy, Paid, Active)
- Start Date (date)
- Completion Date (date)
- Website Price ($2,500 fixed)
- Maintenance Monthly ($100 recurring)
- Payment Received (checkbox)
- Live URL (url)
- GitHub Repo (url)
```

### 4. **Revenue Dashboard**
```
Lookup Fields:
- Client Count (count)
- Total Revenue = (Client Count × $2,500) + (Active Maintenance × $100 × 12)
- Target This Month
- Actual This Month
- MRR (Monthly Recurring Revenue)
```

## API Usage

### Add New Prospect
```bash
curl -X POST "https://api.airtable.com/v0/$AIRTABLE_BASE_ID/Prospects" \
  -H "Authorization: Bearer $AIRTABLE_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "records": [{
      "fields": {
        "Business Name": "Sarah Chen Salon",
        "Category": "Salon",
        "Phone": "(617) 555-0123",
        "Email": "sarah@example.com",
        "Found Date": "2026-03-11"
      }
    }]
  }'
```

### Update Client Status
```bash
curl -X PATCH "https://api.airtable.com/v0/$AIRTABLE_BASE_ID/Clients/recXXXX" \
  -H "Authorization: Bearer $AIRTABLE_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "fields": {
      "Status": "Build",
      "Start Date": "2026-03-11"
    }
  }'
```

### Mark Payment Received
```bash
curl -X PATCH "https://api.airtable.com/v0/$AIRTABLE_BASE_ID/Clients/recXXXX" \
  -H "Authorization: Bearer $AIRTABLE_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "fields": {
      "Payment Received": true,
      "Status": "Deploy"
    }
  }'
```

## Views to Create

### 1. **Today's Calls**
Filter: Verified → Status = "Ready to Call"
Sort: Date Verified (oldest first)
Limit: 15

### 2. **Active Builds**
Filter: Clients → Status = "Discovery" OR "Design" OR "Build"
Sort: Start Date (oldest first)

### 3. **Revenue Dashboard**
Grouped by: Status
Summary: Total Revenue, Count of Clients, Avg Build Time

### 4. **Monthly Pipeline**
Filter: Clients → Status = "Paid" OR "Active"
Grouped by: Month
Summary: Revenue this month

## Integration Points

- **With GitHub**: Link GitHub repo URL when build starts
- **With Stripe**: Add payment link to Clients table when ready
- **With Email**: Pull email from Prospects for outreach
- **With Telegram**: Query dashboard for daily summary

## Commands in OpenClaw

```
/airtable add-prospect "Sarah Chen" "Salon" "(617) 555-0123"
/airtable list-verified          # Show today's call list
/airtable add-client "Sarah Chen" "$2500"
/airtable check-revenue          # Show monthly dashboard
/airtable mark-paid [client-id]  # Payment received
```

## Formulas for Dashboard

**Total Revenue:**
```
(COUNT(values(Clients.Status = "Paid")) * 2500) + 
(COUNT(values(Clients.Status = "Active")) * 100 * 12)
```

**Days Since Start:**
```
DATETIME_DIFF(TODAY(), {Start Date}, 'days')
```

**Expected Completion:**
```
DATEADD({Start Date}, 10, 'days')
```

## Useful Links

- Airtable: https://airtable.com
- API Docs: https://airtable.com/api
- Your Base: https://airtable.com/appXXXXXXXXXXXXXX

## Revenue Tracking Example

| Client | Category | Status | Start | Price | Monthly | 12mo Total |
|--------|----------|--------|-------|-------|---------|-----------|
| Sarah Chen | Salon | Paid | 3/11 | $2,500 | $100 | $3,700 |
| Mike Smith | Restaurant | Build | 3/5 | $2,500 | TBD | TBD |
| **Total (15 Clients)** | - | - | - | **$37,500** | **$1,200+** | **$52K+** |

