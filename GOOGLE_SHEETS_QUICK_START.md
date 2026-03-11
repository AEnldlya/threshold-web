# Google Sheets Quick Start (5 Minutes)

**Get your financial tracking in Google Sheets RIGHT NOW**

---

## Create Sheet 1: Daily Transactions

1. Go to **https://sheets.google.com**
2. Click **"+ Create"** → **"Blank spreadsheet"**
3. Name it: **"Website Agency - Daily Transactions"**
4. In cell A1, type: **Date**
5. In cell B1: **Type**
6. In cell C1: **Client**
7. In cell D1: **Category**
8. In cell E1: **Amount**
9. In cell F1: **Status**
10. In cell G1: **Notes**

**That's it! Your first sheet is ready.**

---

## Create Sheet 2: Monthly Summary

1. Click **"+ Create"** → **"Blank spreadsheet"**
2. Name it: **"Website Agency - Monthly Summary"**
3. In Row 1, add headers:
   - A1: Month
   - B1: Year
   - C1: Website_Builds
   - D1: Website_Revenue
   - E1: Maintenance_Clients
   - F1: Maintenance_Revenue
   - G1: Total_Revenue
   - H1: Total_Costs
   - I1: Gross_Profit
   - J1: Profit_Margin

**Your second sheet is ready.**

---

## Create Sheet 3: Master Dashboard

1. Click **"+ Create"** → **"Blank spreadsheet"**
2. Name it: **"Website Agency - Master Tracker"**
3. Create this simple layout:

```
Row 1: MARCH 2026 FINANCIAL SUMMARY

Row 3: REVENUE
Row 4: Website Builds     | $7,500
Row 5: Maintenance        | $200
Row 6: TOTAL REVENUE      | $7,700

Row 8: COSTS
Row 9: Claude API         | $20
Row 10: Server            | $16
Row 11: Stripe Fees       | $217
Row 12: TOTAL COSTS       | $253

Row 14: PROFIT            | $7,447
Row 15: PROFIT MARGIN     | 99.4%
```

**Your master dashboard is ready.**

---

## Add Formulas (Auto-Calculate)

### In Monthly Summary Sheet (Row 2)

**Cell G2 (Total Revenue):**
```
=D2+F2
```
(Adds Website Revenue + Maintenance Revenue)

**Cell I2 (Gross Profit):**
```
=G2-H2
```
(Adds Total Revenue - Total Costs)

**Cell J2 (Profit Margin):**
```
=I2/G2
```
(Then format as percentage)

---

## Add Your First Transaction

### In Daily Transactions Sheet

```
Row 2:
A2: 2026-03-01
B2: Expense
C2: N/A
D2: Claude API
E2: 20.00
F2: Paid
G2: Monthly subscription

Row 3:
A3: 2026-03-01
B3: Expense
C3: N/A
D3: Server
E3: 16.00
F3: Paid
G3: Monthly hosting
```

---

## Share with CPA Agent (via Link)

### How to get your Spreadsheet IDs:

1. Open **Daily Transactions** sheet
2. Look at URL: `https://docs.google.com/spreadsheets/d/**[ID]**/edit`
3. Copy the **[ID]** part
4. Save it

**Repeat for Monthly Summary and Master Tracker**

---

### Give Permissions (for Maton API updates):

1. Click **Share** (top right)
2. Click **"Change to anyone with the link"**
3. Set to **"Editor"** (so CPA can update)
4. Copy the link
5. Give to CPA agent

---

## What CPA Does Now

Instead of editing local CSV files:

**Every Day:**
1. Check Stripe for payments
2. Add new row to "Daily Transactions" sheet
3. Google Sheets auto-calculates totals
4. Send Telegram alert with numbers

**Every Week (Monday):**
1. Pull summary from "Master Tracker" sheet
2. Send Telegram report

**Every Month (1st):**
1. Add row to "Monthly Summary" sheet
2. Send final report

---

## View on Your Phone

1. Download **Google Sheets app** (free)
2. Sign in with your Google account
3. Your sheets appear automatically
4. Tap any sheet to view real-time data
5. See profits update as transactions happen

---

## Share Read-Only Links with Andy

**For each sheet:**
1. Click **Share**
2. Add: `andy.li.zhang2010@gmail.com`
3. Set to **"Viewer"** (read-only)
4. Click **Share**

**Andy can:**
✅ View your financials anytime
✅ See charts and summaries
✅ Access on his phone
❌ Can't accidentally edit

---

## Test It Works

1. **Add a test transaction** to Daily Transactions
2. **Check**: Does "Master Tracker" show updated numbers?
3. **Create a chart**: Select cells → Insert → Chart
4. **Share link with Andy**: Send the read-only link
5. **Ask Andy**: "Can you see it?" If yes, you're done!

---

## Files You No Longer Need

You can delete these (keep in git, but don't use):
- ❌ `FINANCIALS.csv` (local)
- ❌ `financials_transactions.csv` (local)
- ❌ `financials_monthly_summary.csv` (local)
- ✅ `FINANCIAL_TRACKER.md` (reference)

**From now on: Google Sheets = source of truth**

---

## Your 3 Google Sheets (Save These URLs)

```
1. Daily Transactions
   https://docs.google.com/spreadsheets/d/[ID1]/edit

2. Monthly Summary
   https://docs.google.com/spreadsheets/d/[ID2]/edit

3. Master Tracker
   https://docs.google.com/spreadsheets/d/[ID3]/edit
```

---

## Quick Checklist

- [ ] Create 3 sheets (Daily, Monthly, Master)
- [ ] Add headers to each
- [ ] Add formulas for auto-calculation
- [ ] Add your first transactions
- [ ] Get spreadsheet IDs
- [ ] Share with CPA (Editor access)
- [ ] Share read-only link with Andy
- [ ] Test on phone (Google Sheets app)
- [ ] Create sample chart
- [ ] You're done! ✓

---

## That's It!

You now have professional, real-time financial tracking in Google Sheets.

**Time to set up: 5 minutes**
**Value: Infinite** 📊

---

See `GOOGLE_SHEETS_SETUP.md` for detailed instructions and advanced features.
