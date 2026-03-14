# Google Sheets Financial Tracking Setup

**Move your financial tracking from local files to shared Google Sheets**

---

## Why Google Sheets?

✅ Real-time updates from anywhere
✅ Share with team/advisors (CPA, accountants, Andy)
✅ Automate updates via API (CPA agent does it)
✅ Charts & pivot tables built-in
✅ Mobile access on phone
✅ Automatic backups
✅ See changes instantly across devices

---

## Step 1: Create 3 Google Sheets

### Sheet 1: Daily Transactions
**Name**: `[Andy's Business] - Daily Transactions`

1. Go to https://sheets.google.com
2. Click "Create" → "Blank spreadsheet"
3. Name it: "Website Agency - Daily Transactions"
4. Copy this structure:

```
Column A: Date
Column B: Type
Column C: Client_Name
Column D: Category
Column E: Amount
Column F: Status
Column G: Notes

Row 1: Headers (freeze this row)
Row 2+: Daily transactions
```

**Example data:**
```
2026-03-01 | Expense | N/A | Claude API | 20.00 | Paid | Monthly subscription
2026-03-01 | Expense | N/A | Server | 16.00 | Paid | Monthly hosting
2026-03-11 | Website_Sale | Sarah Chen Salon | Hair Salon | 2500.00 | In_Progress | Build starts
2026-03-21 | Website_Sale | Sarah Chen Salon | Hair Salon | 2500.00 | Pending | Awaiting payment
```

---

### Sheet 2: Monthly Summary
**Name**: `[Andy's Business] - Monthly Summary`

1. Create new spreadsheet
2. Name it: "Website Agency - Monthly Summary"
3. Copy this structure:

```
Column A: Month
Column B: Year
Column C: Website_Builds_Count
Column D: Website_Revenue
Column E: Maintenance_Clients
Column F: Maintenance_Revenue
Column G: Total_Revenue
Column H: Claude_Cost
Column I: Server_Cost
Column J: Stripe_Fees
Column K: Total_Costs
Column L: Gross_Profit
Column M: Profit_Margin
Column N: Cash_Invested_Stocks
Column O: Cash_Available
Column P: Notes

Row 1: Headers (freeze)
Row 2+: One row per month
```

**Example data:**
```
March | 2026 | 3 | 7500 | 2 | 200 | 7700 | 20 | 16 | 217 | 253 | 7447 | 96.8% | 0 | 7447 | Strong margin
```

---

### Sheet 3: Master Financial Tracker
**Name**: `[Andy's Business] - Master Tracker`

1. Create new spreadsheet
2. Name it: "Website Agency - Master Tracker"
3. This sheet has multiple sections:

#### Section A: Monthly Summary (Top)
```
Month: March 2026

REVENUE:
Website Builds: $7,500
Maintenance: $200
TOTAL: $7,700

COSTS:
Claude API: $20
Server: $16
Stripe Fees: $217
TOTAL: $253

PROFIT: $7,447
MARGIN: 96.8%

CASH POSITION:
Starting: $5,000
+ Profit: $7,447
- Investments: $0
= Ending: $12,447
```

#### Section B: Website Sales Log
```
Date | Client | Category | Amount | Status | Payment_Date | Stripe_Fee | Net_Amount
2026-03-11 | Sarah Chen Salon | Hair Salon | 2500.00 | Paid | 2026-03-21 | 72.80 | 2427.20
```

#### Section C: Maintenance Clients
```
Client | Category | Start_Date | Monthly_Amount | Status | Last_Payment | Next_Payment
Sarah's Salon | Hair Salon | 2026-02-15 | 100 | Active | 2026-03-01 | 2026-04-01
```

#### Section D: Monthly Expenses
```
Expense | Amount | Frequency | Notes
Claude API | 20.00 | Monthly | 5 agents running
Server | 16.00 | Monthly | VPS hosting
```

---

## Step 2: Share with CPA Agent

1. Open each spreadsheet
2. Click "Share" (top right)
3. Get shareable link OR
4. Add service account email (if using Maton API)

**To enable CPA updates via API:**
- Go to Share → "Share with others"
- Add: `cpa-agent@[your-workspace].iam.gserviceaccount.com`
- Or get Maton API integration credentials

---

## Step 3: Get Spreadsheet IDs

For CPA agent to update automatically, you need spreadsheet IDs.

For each sheet:
1. Open the spreadsheet
2. Look at URL: `https://docs.google.com/spreadsheets/d/**[SPREADSHEET_ID]**/edit`
3. Copy the ID (the long string)

**Example:**
```
Daily Transactions ID: 1x4F5kF9jK2mL0nP3qR4sT5uV6wX7yZ8aB9cD0eFg
Monthly Summary ID: 2a3B4c5D6e7F8g9H0i1J2k3L4m5N6o7P8q9R0sT
Master Tracker ID: 3x4F5kF9jK2mL0nP3qR4sT5uV6wX7yZ8aB9cD0eFg
```

Store these in your CPA_CREDENTIALS.md file for the agent to use.

---

## Step 4: Update CPA Agent Instructions

Tell CPA to use Maton API to update Google Sheets:

### Using Maton API (Universal Service Integration)

```bash
# Example: Add row to Daily Transactions sheet
maton action=google_sheets \
  --sheet-id "1x4F5kF9jK2mL0nP3qR4sT5uV6wX7yZ8aB9cD0eFg" \
  --tab "Daily Transactions" \
  --action "append" \
  --data '{"Date":"2026-03-21","Type":"Website_Sale","Client_Name":"Sarah Chen","Amount":"2500.00","Status":"Paid"}'
```

---

## Step 5: Automate with CPA Agent

### Every Day (CPA Does This):

1. **Morning**: Check Stripe for new payments
2. **Check**: Did any website complete?
3. **Log**: Add row to "Daily Transactions" sheet
4. **Formulas**: Google Sheets auto-calculates totals

### Every Week (Monday):

1. **Review**: Pull weekly summary from Daily Transactions
2. **Alert**: Send Telegram report to Andy

### Every Month (1st of month):

1. **Finalize**: Previous month numbers
2. **Add**: New row to "Monthly Summary" sheet
3. **Alert**: Send final report via Telegram

---

## Google Sheets Formulas (Auto-Calculate)

### In Monthly Summary Sheet

**Total Revenue (Column G):**
```
=D2+F2   (Website Revenue + Maintenance Revenue)
```

**Total Costs (Column K):**
```
=H2+I2+J2   (Claude + Server + Stripe)
```

**Gross Profit (Column L):**
```
=G2-K2   (Total Revenue - Total Costs)
```

**Profit Margin (Column M):**
```
=L2/G2   (then format as percentage)
```

**Cash Available (Column O):**
```
=L2   (For now, just profit available)
```

---

## In Master Tracker Sheet

**Total Revenue (auto-sum):**
```
=SUM(Website_Builds + Maintenance)
```

**Total Costs (auto-sum):**
```
=SUM(Claude + Server + Stripe Fees)
```

**Profit (auto-calculate):**
```
=Total_Revenue - Total_Costs
```

**Margin (auto-calculate):**
```
=Profit / Total_Revenue
```

---

## Real-World Example (March 2026)

### Daily Transactions Sheet (as CPA adds them)

| Date | Type | Client | Category | Amount | Status | Notes |
|------|------|--------|----------|--------|--------|-------|
| 2026-03-01 | Expense | N/A | Claude API | $20.00 | Paid | Monthly |
| 2026-03-01 | Expense | N/A | Server | $16.00 | Paid | Monthly |
| 2026-03-11 | Website_Sale | Sarah Chen | Hair Salon | $2,500 | In_Progress | Build started |
| 2026-03-11 | Website_Sale | Mike Smith | Plumbing | $2,500 | In_Progress | Build started |
| 2026-03-21 | Website_Sale | Sarah Chen | Hair Salon | $2,500 | Paid | Payment received |
| 2026-03-25 | Website_Sale | Mike Smith | Plumbing | $2,500 | Paid | Payment received |
| 2026-03-01 | Maintenance | Prev Client 1 | Hair Salon | $100 | Paid | Recurring |
| 2026-03-01 | Maintenance | Prev Client 2 | Plumbing | $100 | Paid | Recurring |

**Total Revenue**: $10,200 (auto-sum)
**Total Costs**: $43.40 (auto-sum)
**Profit**: $10,156.60
**Margin**: 99.6%

---

### Monthly Summary Sheet (at month-end)

| Month | Year | Website_Builds | Website_Revenue | Maintenance | Maint_Rev | Total_Rev | Costs | Profit | Margin |
|-------|------|---|---|---|---|---|---|---|---|
| March | 2026 | 3 | $7,500 | 2 | $200 | $7,700 | $43 | $7,657 | 99.4% |

---

### Master Tracker Sheet (Summary View)

```
MARCH 2026 FINANCIAL SUMMARY

REVENUE:
Website Builds (3): $7,500
Maintenance (2): $200
TOTAL: $7,700

COSTS:
Claude API: $20
Server: $16
Stripe Fees: $217
TOTAL: $253

PROFIT: $7,447
MARGIN: 99.4%

CASH POSITION:
Starting: $5,000
+ Profit: $7,447
- Investments: $0
Ending: $12,447

STATUS: Excellent
```

---

## Sharing with Others

### Option 1: Share Read-Only Link with Andy

1. Open spreadsheet
2. Click "Share"
3. Add Andy's email: andy.li.zhang2010@gmail.com
4. Set permission: "Viewer" (read-only)
5. Send link

**Andy can:**
✅ View all data real-time
✅ See charts and summaries
✅ Export to CSV if needed
❌ Cannot edit (prevents mistakes)

---

### Option 2: Share with Accountant/Advisor

Same process, add their email, give "Viewer" access.

---

## Mobile Access

### View on Phone:

1. Open Google Sheets app
2. Search for your spreadsheet
3. Tap to open
4. See real-time data anywhere

---

## Charts & Visualizations

### Create Charts (Google Sheets Built-In)

**Monthly Profit Trend:**
1. Select data: Month, Profit columns
2. Insert → Chart
3. Choose "Line chart"
4. Shows profit growth over time

**Revenue vs Costs:**
1. Select: Month, Revenue, Costs
2. Insert → Chart
3. Choose "Column chart"
4. Side-by-side comparison

**Margin Trend:**
1. Select: Month, Margin
2. Insert → Chart
3. Choose "Line chart"
4. See if margin stays stable at 99%+

---

## CPA Agent Integration

### Tell CPA Agent to Use Google Sheets:

**Instead of local CSV files:**
```
CPA, update your workflow:

OLD: Edit local files
NEW: Update Google Sheets via Maton API

Every day:
1. Check Stripe for payments
2. Use Maton to add row to "Daily Transactions" sheet
3. Google Sheets auto-calculates totals
4. Send Telegram alert with numbers

Every week:
1. Pull summary from Google Sheets
2. Send Telegram report

Every month:
1. Finalize numbers
2. Add row to "Monthly Summary" sheet
3. Send final report
```

---

## Step-by-Step Setup Checklist

- [ ] Create "Daily Transactions" sheet
- [ ] Create "Monthly Summary" sheet
- [ ] Create "Master Tracker" sheet
- [ ] Set up column headers
- [ ] Add formulas for auto-calculation
- [ ] Get spreadsheet IDs
- [ ] Share with CPA agent (via Maton API)
- [ ] Share view-only link with Andy
- [ ] Test: Add one transaction
- [ ] Verify: Formulas calculate correctly
- [ ] Create charts for visualization
- [ ] Brief CPA agent on new workflow

---

## Maton API Commands for CPA

```bash
# Add row to Daily Transactions
maton google-sheets add-row \
  --sheet-id "SPREADSHEET_ID" \
  --tab "Daily Transactions" \
  --data '{"Date":"2026-03-21","Type":"Website_Sale","Client":"Sarah Chen","Amount":"2500"}'

# Get monthly summary
maton google-sheets query \
  --sheet-id "SPREADSHEET_ID" \
  --tab "Monthly Summary" \
  --filter "March 2026"

# Update cell
maton google-sheets update-cell \
  --sheet-id "SPREADSHEET_ID" \
  --cell "A1" \
  --value "New Value"
```

---

## Your Google Sheets URLs

**Once created, share these links:**

```
Daily Transactions:
https://docs.google.com/spreadsheets/d/[ID1]/edit

Monthly Summary:
https://docs.google.com/spreadsheets/d/[ID2]/edit

Master Tracker:
https://docs.google.com/spreadsheets/d/[ID3]/edit

Share read-only links with Andy:
Daily Transactions (View Only):
https://docs.google.com/spreadsheets/d/[ID1]/edit?usp=sharing#gid=0

Monthly Summary (View Only):
https://docs.google.com/spreadsheets/d/[ID2]/edit?usp=sharing#gid=0

Master Tracker (View Only):
https://docs.google.com/spreadsheets/d/[ID3]/edit?usp=sharing#gid=0
```

---

## Benefits Once Set Up

✅ Real-time financial visibility (anywhere, any device)
✅ Auto-calculated totals and margins
✅ Charts showing growth trends
✅ Shareable with team/advisors
✅ Mobile access on phone
✅ Automatic API updates (no manual entry)
✅ Built-in backup (Google's cloud)
✅ Professional presentation

---

**Setup takes 15 minutes. Totally worth it for real-time financials.** 📊
