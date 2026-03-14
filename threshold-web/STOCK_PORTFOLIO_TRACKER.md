# Stock Portfolio Tracker

**Maintained by Stock Watcher Agent**

This file tracks all stock positions Andy has bought based on Stock Watcher recommendations.

---

## Current Holdings

### MSFT (Microsoft)
- **Entry Date**: March 15, 2026
- **Entry Price**: $380
- **Shares**: 10
- **Cost Basis**: $3,800
- **Current Price**: $385 (as of March 11, 02:52 UTC)
- **Current Value**: $3,850
- **Unrealized P/L**: +$50 (+1.3%)
- **Target Price**: $430
- **Stop Loss**: $360
- **Entry Thesis**: Azure cloud growing 30% YoY, AI integration, broke above 200-day MA
- **Conviction**: 8/10
- **Status**: HELD
- **Days Held**: 0 (just example)
- **% to Target**: 14.4% upside remaining
- **% to Stop Loss**: 6.3% downside to stop

---

## Closed Positions (History)

*(None yet - awaiting first trades)*

### Example Entry
- **Ticker**: AAPL
- **Entry Date**: March 1, 2026
- **Entry Price**: $180
- **Shares**: 5
- **Exit Date**: March 15, 2026
- **Exit Price**: $190
- **Realized Profit**: +$50 (+5.6%)
- **Days Held**: 14
- **Thesis Success**: ✓ (hit target)
- **Notes**: iPhone 15 supercycle thesis confirmed by earnings

---

## Portfolio Summary

```
PORTFOLIO OVERVIEW

Total Positions: 1 HELD
Total Invested: $3,800
Current Value: $3,850
Total Unrealized P/L: +$50 (+1.3%)

Closed Trades: 0
Realized Gains: $0
Realized Losses: $0
Total Realized P/L: $0

Cash Available (from CPA): $4,150
Total Portfolio Value: $8,000 (including cash)

Win Rate: N/A (need >5 trades)
Target Win Rate: 60%+
Average Hold: N/A
```

---

## Daily Updates (Stock Watcher Maintains)

### How to Add a Position

When Andy says "I bought X shares at $Y":

1. Add new section under "Current Holdings"
2. Fill in: Entry date, price, shares, cost basis
3. Set target/stop from recommendation
4. Update daily: current price, current value, P/L
5. Alert when target/stop hit

### How to Close a Position

When position hits target or stop loss:

1. Record exit date, exit price
2. Calculate realized P/L = (exit price - entry price) × shares
3. Move to "Closed Positions" section
4. Update portfolio summary
5. Alert Andy: "SOLD X shares at $Y. Profit: $Z"

### Daily Price Updates

Stock Watcher checks daily (or weekly):

```
MSFT: $385 → $388 (no change to P/L impact)
Updated 2026-03-11 10:00 UTC
P/L now: +$80 (+2.1%)
```

---

## Example Workflow

### Day 1: Recommendation
```
Stock Watcher → Andy:
"📈 BUY MSFT at $380-385
Target: $430 (+13%)
Stop: $360 (-5%)
Conviction: 8/10"
```

### Day 1: Andy Buys
```
Andy → Stock Watcher:
"I bought 10 shares of MSFT at $380"

Stock Watcher logs:
- Entry Date: March 15, 2026
- Entry Price: $380
- Shares: 10
- Cost Basis: $3,800
- Target: $430
- Stop: $360
```

### Days 2-30: Monitoring
```
Stock Watcher (daily):
Check price on Yahoo Finance
If MSFT = $385 → Update in tracker
P/L now: +$50 (+1.3%)
Status: HELD, 14% to target
```

### Day 45: Target Hit
```
Stock Watcher → Andy:
"🚨 EXIT SIGNAL: MSFT

Entry: $380 (March 15)
Current: $430
Profit: +$500 (+13.2%)

TARGET HIT ✓

ACTION: SELL 10 SHARES NOW"

Andy → Stock Watcher:
"Sold 10 shares at $430"

Stock Watcher logs:
- Exit Date: April 30, 2026
- Exit Price: $430
- Realized P/L: +$500
- Days Held: 45
- Moved to "Closed Positions"
```

---

## Telegram Alerts Format

### New Buy Alert (from Stock Watcher to Andy)
```
📈 STOCK RECOMMENDATION

Ticker: MSFT
Entry Price: $380-385
Target: $430
Stop: $360
Conviction: 8/10
```

### Position Update (Daily/Weekly)
```
📊 PORTFOLIO UPDATE

MSFT: 10 shares @ $380
Current Price: $388
P/L: +$80 (+2.1%)
Status: HELD, 11% to target

Continue holding.
```

### Exit Alert (Immediate)
```
🚨 EXIT SIGNAL: MSFT

Entry: $380 → Target Hit at $430
Profit: +$500 (+13.2%)

SELL 10 SHARES NOW
```

### Loss Alert (Stop Hit)
```
⚠️ STOP LOSS: AAPL

Entry: $185 → Stop Hit at $175
Loss: -$100 (-5.4%)

SELL 10 SHARES NOW
Cut losses quickly.
```

---

## Key Rules for Stock Watcher

✅ **DO**:
- Track entry price, date, shares accurately
- Update prices daily/weekly
- Alert immediately when target/stop hit
- Calculate P/L correctly
- Log all exits with realized gains/losses
- Maintain 60%+ win rate
- Risk/reward ratio always 1:2+
- Cut losses quickly (respect stop loss)

❌ **DON'T**:
- Make emotional trading calls
- Ignore stop losses (cut when hit)
- Trade without clear thesis
- Over-trade (max 1-2 recommendations/week)
- Risk more than 2% per position
- Trade without defined exit
- Chase losses

---

## Monthly Summary (for CPA)

Every month, provide summary to CPA:

```
MARCH 2026 TRADING SUMMARY

Trades Made: 2
Winning Trades: 2 (100%)
Losing Trades: 0
Total Realized P/L: +$550

Current Holdings: 1 (MSFT)
Unrealized P/L: +$50

Investment Account Value: $4,400
(started with $3,800 cash from profits)

Notes: All trades hit targets. No stops hit.
Ready to deploy more capital in April.
```

---

## Notes

- Maintain this file daily/weekly (Stock Watcher responsibility)
- Update prices from: Yahoo Finance, Google Finance, or your broker
- Calculate P/L: (current price - entry price) × shares
- Alert Andy when target/stop hit (do not wait)
- Log exits same day trade closes

---

*This file is the source of truth for Andy's stock portfolio.*
*Stock Watcher: Keep it updated. It's your trading journal.*
