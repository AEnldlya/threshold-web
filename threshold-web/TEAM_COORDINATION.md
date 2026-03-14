# Team Coordination Guide

## The Team
- **Ryan** (You): Main agent, strategist, operations, context keeper
- **Samantha**: Website builder (Next.js 14, TypeScript, Tailwind, Framer Motion)
- **JEwed**: Prospect finder (Boston businesses without websites)

## Daily Workflow

### 7 AM ET — JEwed's Prospect Batch
1. JEwed finds 20-30 Boston businesses (Google Maps, Yelp, directories)
2. JEwed verifies each against 6-point checklist (no website exists)
3. JEwed sends Ryan: "Today's 15 verified businesses" 
   - Format: Business Name | Phone | Email | Category | Rating | Location
4. JEwed waits for next day

### 7-8 AM ET — Ryan's Call List
1. Ryan receives JEwed's report
2. Ryan calls 15 businesses with sales script (from CONVERSION_PSYCHOLOGY_GUIDE.md)
3. Ryan logs results: "YES to: [Business Name] (phone)"
4. Ryan sends Samantha: "Build [Business Name]" when ready

### When Ryan Says "Build [Business]"
1. Samantha does discovery call with Andy:
   - Business details: name, type, location, contact, images
   - Design questions: colors, vibe, competitors, services/menu
2. Samantha creates Figma mockup (desktop + mobile)
3. Samantha waits for Ryan/Andy approval
4. Samantha builds 10-day timeline:
   - Days 1-2: Discovery + mockup
   - Days 3-5: Development
   - Days 6-7: Refinement
   - Days 8-9: Staging + review
   - Day 10: Production launch

### Recurring Daily Cycle
```
7 AM:  JEwed → "15 verified prospects" → Ryan
↓
9 AM:  Ryan → Call 15 businesses
↓
4 PM:  Ryan → "YES to: Business A, B, C" → Samantha
↓
Next day: Samantha → 10-day build starts
         JEwed → New 15 prospects → Ryan
```

## Communication Channels

### Ryan ↔ Samantha (Builds)
- "Build [Business Name]" — start new project
- Samantha reports: Day 2 mockup link, Days 3-5 progress, Day 8 staging link, Day 10 launch
- Ryan/Andy reviews and approves at each checkpoint

### Ryan ↔ JEwed (Prospects)
- 7 AM: JEwed sends daily batch to Ryan
- Ryan responds: "Thanks, calling now"
- Ryan reports: "YES to: [names], NO on others"
- JEwed logs results to DAILY_CALL_RESULTS.csv

### Samantha ↔ JEwed (Context Sharing)
- When a prospect becomes a build, JEwed sends Samantha:
  - Business name, category, location
  - Phone, email, Google rating
  - Business description from Google/Yelp
  - Social media presence

## Key Documents

| Document | Owner | Purpose |
|----------|-------|---------|
| SAMANTHA_BRIEFING.md | Ryan | Tech stack, workflow, quality standards for Samantha |
| JEWED_BRIEFING.md | Ryan | Verification rules, daily targets, data quality for JEwed |
| VERIFICATION_RULES.md | JEwed | 6-point checklist for confirming NO website |
| CONVERSION_PSYCHOLOGY_GUIDE.md | Ryan/Andy | Sales scripts, psychology, CTAs |
| INDUSTRY_SPECIFIC_TEMPLATES.md | Samantha | Design templates for salon, restaurant, plumbing, etc. |
| HEARTBEAT.md | Ryan | Daily task reminders and targets |
| DAILY_CALL_RESULTS.csv | Ryan | Tracking all calls, results, builds |

## Success Metrics

### JEwed's KPIs
- ✅ 15 verified prospects/day minimum
- ✅ 100% verification rate (zero false positives)
- ✅ Phone numbers all callable, emails all official
- ✅ Data in standard format for easy use

### Samantha's KPIs
- ✅ Lighthouse 95+ every time
- ✅ WCAG AA accessibility every time
- ✅ 10-day delivery (consistent, predictable)
- ✅ Responsive mobile/tablet/desktop every time
- ✅ Zero client revisions (ship quality)

### Ryan's KPIs (Pipeline)
- ✅ 75 calls/week (15/day × 5 days)
- ✅ 10-15 interested/week (13-20% conversion)
- ✅ 4-6 closed/week ($10K-15K revenue)
- ✅ Track all results in DAILY_CALL_RESULTS.csv

### Overall Revenue
- Base: $2,500 × 4-6 closes/week = $10K-15K/week
- Recurring: $100/month × 10-20 maintenance clients = $1K-2K/month passive
- **Year 1 Target**: 20-30 sites ($50K-75K) + recurring revenue base

## Handoff Checklist

When transferring knowledge to each agent:
- [ ] Agent reads their briefing document (SAMANTHA_BRIEFING.md or JEWED_BRIEFING.md)
- [ ] Agent confirms they understand role, workflow, and success metrics
- [ ] Agent gets access to all shared documentation in workspace
- [ ] Agent knows how to coordinate with other team members
- [ ] Agent acknowledges their place in the daily workflow

## Scaling Considerations

**As volume grows:**
- Hire VA for Samantha: photo collection, content writing, client calls ($2K/month)
- Hire VA for JEwed: automate prospect finding, data extraction, verification ($1.5K/month)
- Ryan focuses on: sales strategy, team management, new markets

**Multi-market expansion:**
- JEwed finds prospects in: Boston → New York → Philadelphia → DC
- Samantha scales: reuse templates, faster builds = 3 days instead of 10
- Ryan manages: larger sales pipeline, team coordination

---

**Mission**: Turn the trio (Ryan strategy + Samantha builds + JEwed prospects) into an efficient, scalable machine that closes 4-6 deals/week consistently.
