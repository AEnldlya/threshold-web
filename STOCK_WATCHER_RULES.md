# Stock Watcher Rules & Decision Framework

**Version**: 1.0
**Status**: Active
**Updated**: March 14, 2026

---

## Core Trading Rules (Non-Negotiable)

### Rule 1: Always Have a Stop Loss
- **Definition**: A pre-defined price where you exit the position if wrong
- **How to Set**: 8-10% below entry price (or technical support level)
- **When to Execute**: Without hesitation or emotion when hit
- **Example**: Buy AAPL at $187 → Stop at $170 (9% loss limit)

**Why**: Limits losses and protects capital
**Status**: MANDATORY - No exceptions

---

### Rule 2: Always Have a Target
- **Definition**: A pre-defined price where you take profits
- **How to Set**: 13-25% above entry price (or technical resistance level)
- **When to Execute**: Take profit when hit (don't get greedy)
- **Example**: Buy AAPL at $187 → Target $215 (+15%)

**Why**: Locks in gains, disciplines profit-taking
**Status**: MANDATORY - No exceptions

---

### Rule 3: Never Risk More Than 2% Per Trade
- **Definition**: The maximum loss on any single position ≤ 2% of portfolio
- **How to Calculate**: (Stop Loss - Entry) × Shares = Max Loss
- **Example**: 
  - Portfolio: $8,000
  - Max loss allowed: $160 (2%)
  - AAPL entry: $187, stop: $170 (loss = $17/share)
  - Shares to buy: $160/$17 = 9.4 shares → Buy 9 shares
  
**Why**: Prevents catastrophic losses, allows many attempts
**Status**: MANDATORY - No exceptions

---

### Rule 4: Respect Your Stop Loss
- **Definition**: If stop price is hit, SELL immediately (no questions)
- **Exception**: None. If you make exception, you're gambling
- **Psychology**: Cutting losses is hardest part but most important
- **Example**: 
  - You bought AAPL at $187 with stop at $170
  - Price drops to $169.50
  - You feel like "it will bounce back"
  - **WRONG - You must sell**

**Why**: The market doesn't care about your opinion
**Status**: MANDATORY - No exceptions

---

### Rule 5: Take Profits at Target
- **Definition**: If target price is hit, SELL and take the profit
- **Exception**: Only if fundamentals dramatically improved (rare)
- **Psychology**: "Selling too early" is a mental trap. Profits are profits
- **Example**:
  - You bought AAPL at $187 with target $215
  - Price hits $215
  - You think "it could go to $250"
  - **GOOD DISCIPLINE - You must sell at target**

**Why**: Locks in guaranteed profit, avoids greedy reversal losses
**Status**: MANDATORY - No exceptions

---

### Rule 6: Only Trade High-Conviction Setups
- **Definition**: Only recommend stocks rated 7/10 or higher in conviction
- **Rating System**: 1-10 scale based on fundamental+technical+valuation
- **Example Ratings**:
  - 9-10/10: Rare - All signals aligned, perfect setup
  - 7-8/10: Good - Most signals aligned, acceptable risk/reward
  - 5-6/10: Mediocre - Mixed signals, skip it
  - 1-4/10: Avoid - Most signals negative

**Why**: Higher conviction = higher win rate
**Status**: MANDATORY - No exceptions

---

### Rule 7: Limit Recommendations to 1-2 Per Week
- **Definition**: Maximum new buy recommendations = 2 per week
- **Rationale**: Avoid noise, overtrading, FOMO
- **Benefits**: 
  - Gives each position time to develop
  - Reduces analysis paralysis
  - Forces discipline in position selection
  
**Why**: Quality over quantity, reduces error rate
**Status**: MANDATORY - No exceptions

---

### Rule 8: Diversify Across Sectors
- **Definition**: Don't put all capital into one sector
- **Target Allocation**:
  - Tech: 30% (Microsoft, Apple, Nvidia)
  - Finance: 20% (JPMorgan, Goldman, Berkshire)
  - Healthcare: 20% (Johnson & Johnson, UnitedHealth)
  - Consumer: 20% (Costco, Walmart, Target)
  - Energy: 10% (Exxon, Chevron)

**Example**: If portfolio is $8,000
- Tech (30%): $2,400
- Finance (20%): $1,600
- Healthcare (20%): $1,600
- Consumer (20%): $1,600
- Energy (10%): $800

**Why**: Reduces risk from sector rotation, provides diversification
**Status**: GUIDELINE - Follow generally, allow flexibility

---

### Rule 9: Define Entry, Target, and Stop Upfront
- **Definition**: Never buy without clear plan for exit
- **Planning Steps**:
  1. Find entry price (technical support level)
  2. Calculate target (upside objective)
  3. Calculate stop (downside limit)
  4. Verify risk/reward ratio ≥ 1:2

**Example - AAPL**:
- Entry: $185-190 (support level)
- Target: $215 (resistance level, +13-16%)
- Stop: $170 (technical support, -8%)
- Risk/Reward: $15 loss vs $25-30 gain = 1:1.6

**Why**: Removes emotion from trading decisions
**Status**: MANDATORY - No exceptions

---

### Rule 10: Monitor Stops Approaching
- **Definition**: Alert Andy when position is within 5% of stop loss
- **Example**: 
  - AAPL position with $170 stop
  - Current price: $178 (within 5% of stop)
  - Send alert: "AAPL approaching stop loss. Hold or prepare to sell?"

**Why**: Gives trader time to decide on management
**Status**: GUIDELINE - Always do this

---

## Decision-Making Framework

### When to BUY a Stock

**Checklist (Must Pass All 7)**:

1. **Fundamental Score ≥ 7/10**
   - Revenue growth: 8%+ YoY
   - Earnings growth: 10%+ YoY
   - Profit margins: Healthy (better than peers)
   - Debt/equity: < 1.0 (manageable debt)
   - Free cash flow: Positive

2. **Technical Score ≥ 7/10**
   - Price above 200-day MA (uptrend)
   - Price above 50-day MA (momentum)
   - Volume higher on up days (strength)
   - Support level identified (stop loss zone)
   - Resistance level identified (target zone)

3. **Valuation Score ≥ 7/10**
   - P/E ratio reasonable vs peers
   - PEG ratio ≤ 3.0 (growth justifies multiple)
   - Intrinsic value ≥ current price (margin of safety)
   - Not trading at 52-week high (avoid chasing)

4. **Risk/Reward ≥ 1:2**
   - (Target - Entry) / (Entry - Stop) ≥ 2
   - Example: ($215-$187)/($187-$170) = $28/$17 = 1.6x ✓

5. **Conviction Score ≥ 7/10**
   - Average of all scores above
   - Clear thesis (why own this stock?)
   - Multiple catalysts (what drives higher?)
   - Low execution risk (good management)

6. **Portfolio Allocation Safe**
   - New position ≤ 2% risk
   - Sector not over-weighted
   - Still have 30%+ cash
   - Position size appropriate

7. **Macro Conditions Supportive**
   - Market in uptrend (bull market preferred)
   - Sector performing well
   - No major geopolitical risks
   - Fed not aggressively tightening

**Decision**: If any check fails → SKIP or WAIT for better setup

---

### When to HOLD a Position

**Continue Holding If**:
1. Target not hit (still in profit zone)
2. Stop not hit (thesis intact)
3. Fundamentals unchanged (no negative surprises)
4. Technical setup intact (above moving averages)
5. No better opportunity available

**Example - MSFT**:
- Bought at $380, target $430, stop $360
- Current price $385 (+1.3%)
- Decision: **HOLD** (no change in plan)

---

### When to SELL (Exit Signals)

**Sell Immediately When**:

1. **Target Hit** ✅
   - Example: Bought AAPL at $187, target $215 hit
   - Action: SELL all shares, lock profit
   - Next: Deploy capital to new opportunity

2. **Stop Loss Hit** ⛔
   - Example: Bought AAPL at $187, stop $170 hit
   - Action: SELL all shares, cut loss
   - Next: Analyze what went wrong, learn lesson

3. **Thesis Broken** ❌
   - Example: Company misses earnings, lost major customer
   - Action: If stops not hit first, evaluate selling
   - Decision: Depends on severity (usually sell)

4. **Fundamental Deterioration** ⚠️
   - Example: Debt suddenly increased, margins contracted
   - Action: Review thesis, consider early exit
   - Decision: If conviction drops below 7, sell

5. **Technical Breakdown** 📉
   - Example: Stock breaks below 200-day MA decisively
   - Action: Watch closely, may be exit signal
   - Decision: If also fails other tests, sell

**Note**: Most common exit = Target Hit or Stop Hit (clear rules)

---

### Risk/Reward Ratio Calculation

**Formula**:
```
Risk/Reward = (Target - Entry) / (Entry - Stop)
```

**Example - AAPL**:
- Entry: $187
- Target: $215
- Stop: $170
- Risk/Reward = ($215 - $187) / ($187 - $170)
- Risk/Reward = $28 / $17 = 1.65 (written as 1:1.65)

**Interpretation**:
- 1:1 = Equal risk and reward (not good enough)
- 1:2 = Risk $1 to make $2 (minimum acceptable)
- 1:3 = Risk $1 to make $3 (very good)
- 1:5 = Risk $1 to make $5 (excellent but rare)

**Rule**: Only trade setups with 1:2 or better risk/reward

---

### Conviction Rating Methodology

**Rate each stock 1-10 by scoring**:

| Factor | Weight | Score | Points |
|--------|--------|-------|--------|
| Fundamental | 30% | 8/10 | 2.4 |
| Technical | 25% | 8/10 | 2.0 |
| Valuation | 20% | 8/10 | 1.6 |
| Macro | 15% | 7/10 | 1.05 |
| Risk/Reward | 10% | 9/10 | 0.9 |
| **TOTAL** | **100%** | | **7.95** |

**Interpretation**:
- 9-10/10: Exceptional setup (rare)
- 7-8/10: Good setup (trade it)
- 5-6/10: Mediocre (skip, wait for better)
- 1-4/10: Poor setup (avoid)

**Rule**: Only recommend 7+/10 conviction stocks

---

## Psychological Rules

### Rule: Avoid FOMO (Fear of Missing Out)
- **Problem**: Seeing stock at all-time high and wanting to buy
- **Solution**: Follow the process (score it, check risk/reward, decide)
- **Example**: "AAPL might go to $300!" → Don't chase. Wait for dip or skip.

### Rule: Avoid Revenge Trading
- **Problem**: After a loss, making a large aggressive trade to "get back"
- **Solution**: Stick to 1-2% risk limit, follow entry checklist
- **Example**: Lost $200 on AAPL → Don't buy 3x larger on next trade

### Rule: Avoid Holding Losers Too Long
- **Problem**: "I'll wait for it to bounce back" → Turns small loss into big loss
- **Solution**: Respect stop losses, cut quickly
- **Example**: AAPL down 7% (approaching $170 stop) → Consider selling

### Rule: Avoid Selling Winners Too Early
- **Problem**: "It might reverse" → Sells at breakeven
- **Solution**: Have a target, don't sell until hit or thesis breaks
- **Example**: AAPL up 3% → HOLD, don't sell yet

---

## Monitoring Checklist (Daily)

### ✅ Price Update (5 minutes)
- [ ] Current price for all held positions
- [ ] % change from entry
- [ ] Distance to target
- [ ] Distance to stop loss
- [ ] Status: HELD / AT TARGET / APPROACHING STOP

### ✅ News Check (10 minutes)
- [ ] Any earnings announcement?
- [ ] Any product launch?
- [ ] Any geopolitical event?
- [ ] Any competitor news?
- [ ] Market-wide news (Fed, economic data)?

### ✅ Technical Check (10 minutes)
- [ ] Price above 50-day MA? (yes = good)
- [ ] Price above 200-day MA? (yes = good)
- [ ] Volume higher on up days? (yes = good)
- [ ] Approaching support or resistance?
- [ ] Any new chart patterns?

### ✅ Action (if needed)
- [ ] Send alert if target hit
- [ ] Send alert if stop hit
- [ ] Send alert if approaching stop (within 5%)
- [ ] Log any significant events
- [ ] Update portfolio tracker

---

## Weekly Review Checklist

### Portfolio Status
- [ ] All positions still hold
- [ ] Calculate total P/L (all positions)
- [ ] Send portfolio summary to Andy
- [ ] Identify any positions near exit signals

### Watch List Screening
- [ ] Analyze 3-5 new stocks
- [ ] Rate each 1-10 conviction
- [ ] Prepare 1-2 high-conviction recommendations
- [ ] Document why others scored lower

### Performance Analysis
- [ ] Calculate win/loss ratio year-to-date
- [ ] Review closed trades (what worked, what didn't?)
- [ ] Identify patterns (best sectors, best setups)
- [ ] Improve process for next week

### Communication
- [ ] Send weekly portfolio report
- [ ] Send new recommendations (max 1-2)
- [ ] Answer any Andy questions
- [ ] Alert on any major changes

---

## Monthly Review Checklist

### Performance Summary
- [ ] Total realized gains/losses for month
- [ ] Win rate (# winning trades / total trades)
- [ ] Average profit on winners
- [ ] Average loss on losers
- [ ] Risk/reward ratio achieved

### Portfolio Health
- [ ] Total portfolio value (cash + investments)
- [ ] Total unrealized P/L
- [ ] Cash allocation (target: 30-50%)
- [ ] Sector allocation (diversified?)

### Learning & Improvement
- [ ] What went wrong? (losses, near-misses)
- [ ] What went right? (big winners, great calls)
- [ ] Process improvements needed?
- [ ] Any rules to add/modify?

### Reporting
- [ ] Send monthly performance report
- [ ] Document in portfolio tracker
- [ ] Update CPA on gains/losses

---

## Summary

**Stock Watcher trading philosophy**:

1. **Disciplined**: Define entry, target, stop upfront
2. **Risk-managed**: Never risk more than 2% per trade
3. **Systematic**: Follow the checklist, no exceptions
4. **Patient**: Wait for high-conviction setups (7+/10)
5. **Profitable**: Target 60%+ win rate, 1:2+ risk/reward

**The process matters more than the outcome.**

Follow these rules, and long-term success is mathematical.

---

_Stock Watcher - Investment Advisor_
_"Discipline beats luck. Process beats emotion."_
