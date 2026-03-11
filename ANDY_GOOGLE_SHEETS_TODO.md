# Your Google Sheets Financial Dashboard - Setup Instructions

**Andy, here's exactly what to do to get your financial tracking live in Google Sheets**

---

## Why This Matters

Instead of looking at local CSV files, you'll have a **live, shareable, real-time financial dashboard** that:
- Updates automatically (CPA does it)
- Shows profit instantly
- Works on your phone
- Looks professional
- Auto-calculates everything
- Shows charts of your growth

---

## The 3 Sheets You're Creating

1. **Daily Transactions** - Records every payment, expense, sale
2. **Monthly Summary** - Shows profit at month-end
3. **Master Tracker** - Your executive dashboard

---

## Step 1: Create Sheet 1 (Daily Transactions)

### Go to https://sheets.google.com

### Create New Spreadsheet
1. Click **"+ Create"**
2. Click **"Blank spreadsheet"**
3. At the top, name it: **"Website Agency - Daily Transactions"**

### Add Column Headers (Row 1)
Copy this into Row 1:

```
A1: Date       B1: Type        C1: Client_Name    D1: Category    E1: Amount    F1: Status    G1: Notes
```

**Done! Sheet 1 is ready.**

---

## Step 2: Create Sheet 2 (Monthly Summary)

### Create New Spreadsheet
1. Click **"+ Create"**
2. Click **"Blank spreadsheet"**
3. Name it: **"Website Agency - Monthly Summary"**

### Add Column Headers (Row 1)
```
A1: Month     B1: Year    C1: Website_Builds    D1: Website_Revenue    E1: Maintenance_Clients
F1: Maintenance_Revenue    G1: Total_Revenue    H1: Total_Costs    I1: Gross_Profit    J1: Profit_Margin
```

### Add Formulas (Row 2)

In cell **G2**, type:
```
=D2+F2
```
(This adds Website Revenue + Maintenance Revenue)

In cell **I2**, type:
```
=G2-H2
```
(This subtracts costs from revenue)

In cell **J2**, type:
```
=I2/G2
```
(This calculates profit margin)

Then select **J2** and format as **Percentage** (right-click → Format Cells → Percentage)

**Done! Sheet 2 is ready.**

---

## Step 3: Create Sheet 3 (Master Tracker)

### Create New Spreadsheet
1. Click **"+ Create"**
2. Click **"Blank spreadsheet"**
3. Name it: **"Website Agency - Master Tracker"**

### Add Dashboard Layout

Type this into the sheet (or copy-paste):

```
MARCH 2026 FINANCIAL SUMMARY

REVENUE:
Website Builds            $7,500
Maintenance Clients       $200
TOTAL REVENUE             $7,700

COSTS:
Claude API                $20
Server                    $16
Stripe Fees               $217
TOTAL COSTS               $253

PROFIT                    $7,447
PROFIT MARGIN             99.4%

CASH ON HAND              $12,447
```

Make it pretty by:
- Making the title bold and large
- Color revenue rows green
- Color cost rows red
- Color profit rows dark green

**Done! Sheet 3 is ready.**

---

## Step 4: Get Your Spreadsheet IDs (Save These!)

For each of your 3 sheets:

1. Open the sheet
2. Look at the URL: `https://docs.google.com/spreadsheets/d/**[ID]**/edit`
3. Copy the **[ID]** part (the long string of characters)
4. Save it somewhere safe

**Example:**
```
Daily Transactions ID: 1x4F5kF9jK2mL0nP3qR4sT5uV6wX7yZ8aB9cD0eFg
Monthly Summary ID: 2a3B4c5D6e7F8g9H0i1J2k3L4m5N6o7P8q9R0sT
Master Tracker ID: 3x4F5kF9jK2mL0nP3qR4sT5uV6wX7yZ8aB9cD0eFg
```

Store in: `CPA_CREDENTIALS.md`

---

## Step 5: Share with CPA Agent

### For CPA to Update Your Sheets

1. Open **Daily Transactions** sheet
2. Click **"Share"** (top right)
3. Click **"Change to anyone with the link"**
4. Select **"Editor"** (so CPA can update)
5. Copy the link
6. Give to me (Ryan) - I'll pass it to CPA

**Do the same for Monthly Summary and Master Tracker**

---

## Step 6: Get Your Read-Only Links (Optional)

If you want to share your financials with advisors/partners:

1. Open each sheet
2. Click **"Share"**
3. Add their email address
4. Set to **"Viewer"** (read-only)
5. Click **"Share"**

They can see everything but can't edit (safer!)

---

## Step 7: Test It Works

1. Add a sample transaction to **Daily Transactions**:
   - Date: 2026-03-01
   - Type: Expense
   - Amount: $20
   - Status: Paid

2. Check **Monthly Summary**: Does it show the amount? (If formulas work)

3. Open on your phone (download Google Sheets app)

4. See if it updates when you add data

---

## Step 8: Tell Me When Done

Once your 3 sheets are created:

Message me: **"Google Sheets ready. Here are the IDs: [list them]"**

I'll:
1. Brief CPA agent on the sheet IDs
2. Configure CPA to update automatically
3. Set up Telegram alerts with real data
4. Get it all working

---

## What Happens After

### Every Day:
- You make sales calls
- CPA logs transactions to **Daily Transactions** sheet
- Numbers update in real-time
- You see it on your phone

### Every Week (Monday):
- CPA sends you: "Revenue: $X, Profit: $Y"
- You see weekly summary

### Every Month (1st):
- CPA logs final numbers to **Monthly Summary**
- Sends you: "March profit: $7,447"
- You see month-over-month growth

### Anytime:
- Open **Master Tracker** on your phone
- See your profit at a glance
- Know exactly how much cash you have

---

## The Result

**Before:** Local CSV files (complicated, hard to share)
**After:** Live Google Sheets (simple, real-time, on your phone)

You can:
✅ See profits instantly
✅ Share with advisors (read-only)
✅ Check on your phone anytime
✅ Show investors professional financials
✅ Make decisions based on real data

---

## Time Required

**Setup: 10 minutes**
**Value: Priceless** 💰

---

## Quick Checklist

- [ ] Create 3 Google Sheets
- [ ] Add headers and formulas
- [ ] Get spreadsheet IDs
- [ ] Share with CPA agent (Editor access)
- [ ] Optional: Share with advisors (Viewer access)
- [ ] Test on your phone
- [ ] Tell me: "Ready! Here are IDs: [list]"
- [ ] I configure CPA agent
- [ ] Done! Live financials running

---

## Questions?

If anything is unclear:
1. See `GOOGLE_SHEETS_QUICK_START.md` (5-min version)
2. See `GOOGLE_SHEETS_SETUP.md` (detailed guide)
3. See `GOOGLE_SHEETS_TEMPLATES.md` (copy-paste templates)

Or just ask me. Happy to help!

---

**Let's go! Get this set up today.** 🚀
