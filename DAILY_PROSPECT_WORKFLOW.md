# Daily Prospect Workflow - 7 AM Automatic Reports

## Overview
Every morning at 7 AM UTC, you'll receive an automated report with:
- **50 New Prospects** - Companies without websites (sorted by confidence)
- **Response Summary** - Who has replied to previous emails
- **Action Prompt** - Ready to approve and send

## How It Works

### 1. Daily 7 AM Report (Automated)
```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    DAILY PROSPECT REPORT - 7 AM                           ║
║                         2026-03-02 07:00 UTC                              ║
╚═══════════════════════════════════════════════════════════════════════════╝

📊 TODAY'S PROSPECTS (Top 50 by Confidence)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. RESTAURANTS (12 prospects)
   1. Tony's Pizzeria                    | 73% | tony@tonypizza.com
   2. Marco's Italian Kitchen           | 72% | marco@marcoitalian.com
   ...

2. SALONS (8 prospects)
   ...

✉️  RESPONSES RECEIVED (3 total)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   • john@jplumbing.com        | Interested          | 2026-03-01
   • sarah@salon-elegance.com  | Sent Photos         | 2026-02-28
   • mike@hvac-pro.com         | Awaiting Demo       | 2026-02-27

🚀 READY TO SEND?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When ready, reply with:
   "SEND"  - Send emails to all 50 prospects
   "INFO"  - Show more details about a prospect
   "SKIP"  - Skip these and see next batch
   "STATS" - Show campaign statistics
```

### 2. You Review & Approve

```
You: "SEND"
System: "✅ Sending 50 emails with 5-min delays..."
```

### 3. Emails Send Automatically
- 5-minute delays between each email (Gmail spam prevention)
- Total time: ~4 hours for 50 emails
- All sends logged to tracker
- No manual work required

### 4. Responses Tracked
- Auto-organize with Gmail labels
- Next morning's report shows responses
- You can reply and progress deals

---

## Setup Instructions

### Step 1: Verify Scripts Are Created
```bash
ls -la ~/.openclaw/workspace/daily_prospect_report.py
ls -la ~/.openclaw/workspace/send_approved_batch.py
```

Both files should exist.

### Step 2: Create Cron Job

Use OpenClaw's cron system to run the report at 7 AM daily:

```bash
# Edit your HEARTBEAT.md or create a cron task:
openclaw run --cron "0 7 * * *" \
  "python3 ~/.openclaw/workspace/daily_prospect_report.py && \
   cat ~/.openclaw/workspace/daily_report.txt"
```

Or add to your cron with:
```bash
crontab -e

# Add this line:
0 7 * * * cd ~/.openclaw/workspace && python3 daily_prospect_report.py
```

### Step 3: Test It

Run manually first:
```bash
python3 ~/.openclaw/workspace/daily_prospect_report.py
```

You should see:
```
✅ Report saved to: daily_report.txt
✅ Pending batch saved: 50 emails
```

---

## Daily Workflow

### Morning (7 AM)
1. You receive report with 50 prospects
2. Review responses from previous days
3. Decide: SEND, SKIP, or INFO

### If You Say "SEND"
1. System sends emails over ~4 hours
2. 5-min delays prevent spam flagging
3. All tracked automatically

### If You Say "SKIP"
1. Same prospects available tomorrow
2. You can review again later

### If You Say "INFO"
1. Get detailed info about a specific prospect
2. Phone number, owner name, confidence score
3. Customize template if needed

---

## Commands Available

| Command | Action | Example |
|---------|--------|---------|
| `SEND` | Send all 50 pending emails | `SEND` |
| `SKIP` | Don't send today, try again tomorrow | `SKIP` |
| `STATS` | Show campaign statistics | `STATS` |
| `INFO [email]` | Details about specific prospect | `INFO tony@tonypizza.com` |

---

## What Gets Tracked

### outreach_tracker.csv
```
Email,Status,Timestamp,Response,Notes
john@jplumbing.com,Sent,2026-03-01T14:23:45,Interested,Replied with phone
sarah@salon.com,Sent,2026-03-01T14:18:45,Photos,Waiting for quote
...
```

### sent_emails_log.json
```json
{
  "tony@tonypizza.com": {
    "timestamp": "2026-03-01T14:13:45",
    "status": "sent"
  },
  ...
}
```

### daily_responses.json
```json
{
  "john@jplumbing.com": {
    "status": "Interested",
    "date": "2026-03-01",
    "response": "Yes, I'd like to see a demo"
  },
  ...
}
```

---

## Workflow Timeline Example

### Day 1 (Monday 7 AM)
```
System: "📊 Daily Report - 50 prospects ready"
User: "SEND"
System: "✅ Sending 50 emails over 4 hours..."
       (sends with 5-min delays)
```

### Day 2 (Tuesday 7 AM)
```
System: "📊 Daily Report"
         "3 responses since yesterday"
         "50 new prospects ready"
User: "SEND"
System: "✅ Sending..."
```

### Day 3 (Wednesday 7 AM)
```
System: "📊 Daily Report"
         "2 more responses"
         "7 total interested so far"
         "50 new prospects ready"
```

---

## Campaign Statistics

After sending batches, check with `STATS`:

```
Campaign Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Sent:        150 emails
Total Responses:   15 (10% response rate)
Interested:        8  (5.3% interested)
Awaiting Demo:     4  (2.7% demo scheduled)
Awaiting Payment:  2  (1.3% ready to close)

Closed Deals:      1  ($500 revenue)
Expected Revenue:  $400-800 (4-8 more likely to close)
```

---

## Expected Response Rates

Based on industry data for email campaigns:

| Metric | Expected | Your Target |
|--------|----------|-------------|
| Open Rate | 20-30% | - |
| Response Rate | 5-15% | 8-12% |
| Demo Scheduled | 30% of responses | 2-4 from 50 |
| Close Rate | 20-30% | 1-3 from 50 |

**From 50 emails**: Expect 4-6 responses, 1-2 demos, 0-1 closed deals ($0-500/day)

---

## Tips for Best Results

### Email Timing
- Emails send over ~4 hours with 5-min gaps
- Arrives at random times (looks natural)
- Avoid Gmail spam detection
- Higher reply rates than bulk sends

### Response Handling
- Check your email every few hours
- Reply quickly to interested prospects
- Use auto-responder for "send photos" requests
- Update tracker with responses

### Customize If Needed
Before sending:
1. Review prospect list for errors
2. Edit email template for specific industries
3. Add personalization if desired
4. Then run SEND

---

## Monthly Overview

**Sending 50 emails per day:**
- Week 1: 350 emails → ~35-50 responses → 5-10 interested
- Week 2: 350 emails → ~35-50 responses → 5-10 interested
- Week 3: 350 emails → ~35-50 responses → 5-10 interested
- Week 4: 350 emails → ~35-50 responses → 5-10 interested

**Month 1 Total**: 1,400 emails → 140-200 responses → 20-40 interested

**Revenue Potential**: 5-15 closed deals at $500 = $2,500-$7,500/month

---

## Troubleshooting

### "No pending batch found"
- Run daily report first: `python3 daily_prospect_report.py`
- Then use SEND command

### "Gmail auth error"
- Check Gmail credentials: `ls ~/.openclaw/workspace/.gmail_credentials.json`
- Regenerate if needed

### "All 167 prospects sent"
- Time to expand to surrounding areas
- Or follow up with non-responsive prospects
- Or build for current interested prospects

### "Too many responses to handle"
- Prioritize by confidence score
- Focus on high-confidence first
- Batch build 5-10 sites at once

---

## Next Actions

### Immediate
1. ✅ Scripts created (`daily_prospect_report.py`, `send_approved_batch.py`)
2. ⏳ Set up cron job for 7 AM daily
3. ⏳ Test with manual run
4. ⏳ Start receiving daily reports

### This Week
1. Review first day's prospects
2. Send first batch (50 emails)
3. Monitor responses
4. Adjust template if needed

### This Month
1. Send 3-4 batches (150-200 emails)
2. Expect 15-40 responses
3. Schedule 3-10 demos
4. Close 1-3 deals ($500-$1500 revenue)

---

## Files Used

- `daily_prospect_report.py` - Generates morning report
- `send_approved_batch.py` - Sends approved emails
- `boston_167_VERIFIED_FINAL.csv` - Prospect list
- `sent_emails_log.json` - Send tracking
- `outreach_tracker.csv` - Full campaign tracker
- `daily_responses.json` - Response tracking
- `pending_send_batch.json` - Pending emails (temporary)
- `daily_report.txt` - Daily report output
- `EMAIL_TEMPLATES_HUMANIZED.md` - Email templates

---

## Support

If something breaks:
1. Check the error message
2. Run `python3 daily_prospect_report.py` manually
3. Review `daily_report.txt` for logs
4. Check file permissions in workspace

---

**Status**: Ready to set up 7 AM daily automation ✅
**Next**: Create cron job and test first run
