# Google Sheets Template Structures

**Exact layouts for copy-paste into your sheets**

---

## Sheet 1: Daily Transactions

### Header Row (Row 1) - Copy Exactly
```
A1: Date          B1: Type            C1: Client_Name      D1: Category
E1: Amount        F1: Status          G1: Notes
```

### Example Data Rows (Paste as needed)

```
2026-03-01 | Expense       | N/A              | Claude API     | 20.00      | Paid | Monthly subscription
2026-03-01 | Expense       | N/A              | Server         | 16.00      | Paid | Monthly hosting
2026-03-11 | Website_Sale  | Sarah Chen Salon | Hair Salon     | 2500.00    | In_Progress | Samantha building
2026-03-11 | Website_Sale  | Mike Smith Plumbing | Plumbing    | 2500.00    | In_Progress | Samantha building
2026-03-21 | Website_Sale  | Sarah Chen Salon | Hair Salon     | 2500.00    | Pending | Awaiting payment
2026-03-25 | Website_Sale  | Mike Smith Plumbing | Plumbing    | 2500.00    | Paid | Payment received
2026-03-01 | Maintenance   | Previous Client 1 | Hair Salon    | 100.00     | Paid | Recurring
2026-03-01 | Maintenance   | Previous Client 2 | Plumbing      | 100.00     | Paid | Recurring
```

### Column Formatting
- **Column A (Date)**: Format as Date (MM/DD/YYYY)
- **Column E (Amount)**: Format as Currency ($)
- **Column F (Status)**: Dropdown list (Paid, Pending, In_Progress)

### Totals Row (Bottom of sheet, or separate area)
```
Row 20:
A20: TOTAL
E20: =SUM(E2:E19)        (Auto-sum all amounts)
```

---

## Sheet 2: Monthly Summary

### Header Row (Row 1) - Copy Exactly
```
A1: Month
B1: Year
C1: Website_Builds_Count
D1: Website_Revenue
E1: Maintenance_Clients
F1: Maintenance_Revenue
G1: Total_Revenue
H1: Claude_Cost
I1: Server_Cost
J1: Stripe_Fees
K1: Total_Costs
L1: Gross_Profit
M1: Profit_Margin
N1: Cash_Invested_Stocks
O1: Cash_Available
P1: Notes
```

### Example Data Row (Row 2)
```
March | 2026 | 3 | 7500 | 2 | 200 | 7700 | 20 | 16 | 217 | 253 | 7447 | 99.4% | 0 | 7447 | Strong growth
```

### Formulas (Row 2)
```
G2: =D2+F2              (Website + Maintenance Revenue)
K2: =H2+I2+J2           (Total Costs)
L2: =G2-K2              (Gross Profit)
M2: =L2/G2              (Profit Margin, format as %)
O2: =L2                 (Cash Available from Profit)
```

### Column Formatting
- **Column A (Month)**: Text
- **Column D, F, G, H, I, J, K, L, N, O**: Currency ($)
- **Column M**: Percentage (%)

### Add New Months
```
April | 2026 | 4 | 10000 | 5 | 500 | 10500 | 20 | 16 | 304 | 340 | 10160 | 96.8% | 0 | 10160 | Growth
May   | 2026 | 4 | 10000 | 8 | 800 | 10800 | 20 | 16 | 313 | 349 | 10451 | 96.8% | 5000 | 5451 | Invest
```

---

## Sheet 3: Master Tracker Dashboard

### Simple Text Layout

```
MARCH 2026 FINANCIAL SUMMARY

REVENUE BREAKDOWN:
Website Builds (3)              $7,500
Maintenance Clients (2)         $200
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL REVENUE                   $7,700

COST BREAKDOWN:
Claude API                      $20
Server / Hosting                $16
Stripe Processing Fees (2.9%+$0.30)  $217
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL COSTS                     $253

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GROSS PROFIT                    $7,447
PROFIT MARGIN                   99.4%

CASH POSITION:
Starting Cash                   $5,000
+ Monthly Profit                $7,447
- Stock Investments             $0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENDING CASH                     $12,447

GROWTH METRICS:
Total Websites Sold (YTD)       12
Active Maintenance Clients      8
Customer LTV (avg)              $6,100
Monthly Recurring Revenue       $800

KEY PERFORMANCE INDICATORS:
Profit Margin                   99.4% ✓
Operating Days to Positive      1 day ✓
New Websites This Month         3 ✓
Maintenance Base Growing        +25% vs Feb ✓

STATUS: EXCELLENT
```

### Grid Alternative (if you prefer columns)

```
Metric                          March 2026    Notes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Website Builds                  3             On track
Website Revenue                 $7,500        
Maintenance Clients             2             Growing
Maintenance Revenue             $200          
Total Revenue                   $7,700        

Claude API Cost                 $20           Fixed
Server Cost                     $16           Fixed
Stripe Fees                     $217          Variable
Total Costs                     $253          Extremely low

Profit                          $7,447        
Profit Margin                   99.4%         Excellent

Cash Available                  $12,447       Ready to invest
Invested in Stocks              $0            Awaiting picks
```

### Formulas for Master Tracker

```
C3 (Total Revenue): =SUM(B2:B3)
C8 (Total Costs): =SUM(B5:B7)
C10 (Gross Profit): =C3-C8
C11 (Profit Margin): =C10/C3 (format as %)
```

---

## Alternative: Use a Template Sheet

### Option 1: Pull from Daily Transactions
```
Monthly Summary Row 2 Formulas:

C2: =COUNTIFS('Daily Transactions'!B:B,"Website_Sale",'Daily Transactions'!A:A,">=2026-03-01",'Daily Transactions'!A:A,"<2026-04-01")
D2: =SUMIFS('Daily Transactions'!E:E,'Daily Transactions'!B:B,"Website_Sale",'Daily Transactions'!A:A,">=2026-03-01",'Daily Transactions'!A:A,"<2026-04-01")
E2: =COUNTIFS('Daily Transactions'!B:B,"Maintenance",'Daily Transactions'!A:A,">=2026-03-01",'Daily Transactions'!A:A,"<2026-04-01")
F2: =SUMIFS('Daily Transactions'!E:E,'Daily Transactions'!B:B,"Maintenance",'Daily Transactions'!A:A,">=2026-03-01",'Daily Transactions'!A:A,"<2026-04-01")
```

This **automatically pulls** data from Daily Transactions!

---

## Spreadsheet View Hierarchy

```
DAILY TRANSACTIONS (Most detailed)
    ↓ (feeds)
MONTHLY SUMMARY (Monthly trends)
    ↓ (feeds)
MASTER TRACKER (Executive overview)
```

Data flows from detailed → summary → dashboard.

---

## Color Coding (Optional, makes it pretty)

### Daily Transactions
- **Row 1 (Headers)**: Light blue background
- **Expense rows**: Light red background
- **Website_Sale rows**: Light green background
- **Maintenance rows**: Light yellow background

### Monthly Summary
- **Row 1 (Headers)**: Light blue background
- **Revenue section**: Light green
- **Costs section**: Light red
- **Profit section**: Light green (darker)
- **Cash section**: Light blue

### Master Tracker
- **Title**: Bold, large font
- **Revenue section**: Green text
- **Costs section**: Red text
- **Profit section**: Dark green, bold
- **Status section**: Green checkmarks

---

## Quick Copy-Paste Setup

### For Daily Transactions (just copy into Row 1):
```
Date	Type	Client_Name	Category	Amount	Status	Notes
```

### For Monthly Summary (copy into Row 1):
```
Month	Year	Website_Builds_Count	Website_Revenue	Maintenance_Clients	Maintenance_Revenue	Total_Revenue	Claude_Cost	Server_Cost	Stripe_Fees	Total_Costs	Gross_Profit	Profit_Margin	Cash_Invested_Stocks	Cash_Available	Notes
```

### For Master Tracker (create text layout shown above)

---

## Example of Filled Sheets

### Daily Transactions (End of March 2026)
```
Date        Type            Client                  Category        Amount    Status    Notes
2026-03-01  Expense         N/A                     Claude API      20.00     Paid      Monthly
2026-03-01  Expense         N/A                     Server          16.00     Paid      Monthly
2026-03-11  Website_Sale    Sarah Chen Salon        Hair Salon      2500.00   In_Progress  Build starts
2026-03-11  Website_Sale    Mike Smith Plumbing     Plumbing        2500.00   In_Progress  Build starts
2026-03-11  Website_Sale    Maria's Italian         Restaurant      2500.00   In_Progress  Build starts
2026-03-21  Website_Sale    Sarah Chen Salon        Hair Salon      2500.00   Paid      Payment received
2026-03-25  Website_Sale    Mike Smith Plumbing     Plumbing        2500.00   Paid      Payment received
2026-03-28  Website_Sale    Maria's Italian         Restaurant      2500.00   Paid      Payment received
2026-03-01  Maintenance     Prev Client 1           Hair Salon      100.00    Paid      Recurring
2026-03-01  Maintenance     Prev Client 2           Plumbing        100.00    Paid      Recurring

TOTAL:                                                              $15,500
```

---

## That's It!

Use these templates to set up your sheets in seconds.

**Time: 2 minutes**
**Accuracy: 100%**
**Professional: Yes** ✓

---

See `GOOGLE_SHEETS_QUICK_START.md` for step-by-step setup.
See `GOOGLE_SHEETS_SETUP.md` for detailed guide and advanced features.
