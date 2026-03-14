# Setup Daily 7 AM Prospect Reports

## Quick Setup (5 minutes)

Your automated daily workflow is ready to activate. Here's how:

### Option 1: Using OpenClaw Cron (Recommended)

Run this command:
```bash
openclaw run --cron "0 7 * * *" \
  "python3 ~/.openclaw/workspace/daily_prospect_report.py"
```

This schedules the report to run every day at 7 AM UTC.

**What happens:**
- 7 AM: `daily_prospect_report.py` runs automatically
- Report is generated with 50 new prospects
- Report saved to `daily_report.txt`
- You'll see notification/message in your OpenClaw session

---

### Option 2: Using System Cron

Edit your crontab:
```bash
crontab -e
```

Add this line:
```
0 7 * * * cd ~/.openclaw/workspace && python3 daily_prospect_report.py >> daily_cron.log 2>&1
```

**What this does:**
- Runs at 7 AM every day
- Logs output to `daily_cron.log`
- Can be checked anytime

---

### Option 3: Using OpenClaw HEARTBEAT

Edit `~/.openclaw/workspace/HEARTBEAT.md`:

```markdown
# Daily Tasks (Run at 7 AM)

## Check Prospects
- Run: `python3 ~/.openclaw/workspace/daily_prospect_report.py`
- Check for 50 new companies without websites
- Review responses from previous outreach
```

Then configure OpenClaw to run heartbeats at 7 AM.

---

## Verification

### Test It Works

Run the script manually first:
```bash
python3 ~/.openclaw/workspace/daily_prospect_report.py
```

You should see:
```
Loaded 167 total Boston businesses
Already sent: 0 emails
Responses: 0
Loaded 167 total Boston businesses

╔═══════════════════════════════════════════════════════════════════════════╗
║                    DAILY PROSPECT REPORT - 7 AM                           ║
║                         2026-03-02 07:15 UTC                              ║
╚═══════════════════════════════════════════════════════════════════════════╝

📊 TODAY'S PROSPECTS (Top 50 by Confidence)
...
✅ Report saved to: daily_report.txt
✅ Pending batch saved: 50 emails
```

### Check for Success
```bash
cat ~/.openclaw/workspace/daily_report.txt
```

You should see your 50 prospects organized by category and confidence.

---

## Daily Workflow Activation

### When You Get the Report (7 AM)

You'll see something like:

```
📊 DAILY PROSPECT REPORT GENERATED
50 prospects ready to contact
3 responses from yesterday
Ready for your approval
```

### Your Response Options

**To Send All 50 Emails:**
```
SEND
```

**To See Details:**
```
INFO tony@tonypizza.com
```

**To Skip & Try Tomorrow:**
```
SKIP
```

**To See Statistics:**
```
STATS
```

---

## Files Required (Should Already Exist)

```
✅ ~/.openclaw/workspace/daily_prospect_report.py
✅ ~/.openclaw/workspace/send_approved_batch.py
✅ ~/.openclaw/workspace/boston_167_VERIFIED_FINAL.csv
✅ ~/.openclaw/workspace/EMAIL_TEMPLATES_HUMANIZED.md
✅ ~/.openclaw/workspace/send_free_demo_emails.py
```

If any are missing, let me know and I'll recreate them.

---

## What Happens Behind the Scenes

### 7 AM Daily Execution
1. Script loads 167 Boston companies
2. Checks which ones already got emails
3. Selects top 50 by confidence score
4. Groups by category (restaurants, salons, plumbing, etc.)
5. Loads any responses from previous days
6. Formats beautiful report
7. Saves to `daily_report.txt`
8. Shows to you for approval

### Example Report Structure
```
1. RESTAURANTS (15 prospects)
   - Tony's Pizzeria           73% confidence
   - Marco's Italian Kitchen   72% confidence
   - etc.

2. SALONS (12 prospects)
   - Salon Bella              71% confidence
   - etc.

3. PLUMBING (10 prospects)
   - South End Plumbing       69% confidence
   - etc.

Responses So Far:
   • john@jplumbing.com - Interested (Mar 1)
   • sarah@salon.com - Sent Photos (Feb 28)

Ready to Send? Reply with: SEND / SKIP / INFO
```

### When You Say "SEND"
1. System loads `pending_send_batch.json` (50 emails)
2. Gets Gmail credentials
3. Loads email template
4. Sends first email
5. Waits 5 minutes
6. Sends second email
7. Waits 5 minutes
8. ... continues for all 50 ...
9. Total time: ~4 hours
10. Logs all sends to `sent_emails_log.json`
11. Updates `outreach_tracker.csv`

### Response Tracking
- Gmail labels auto-organize replies
- Next morning's report shows responses
- You can manually update status
- Track conversions in `daily_responses.json`

---

## Expected Timeline

### Day 1 (Today)
- [ ] Activate daily routine
- [ ] Test manual run
- [ ] Verify report generates

### Day 2 (Tomorrow, 7 AM)
- Report auto-generates
- Review 50 prospects
- Review any previous responses (likely none yet)
- Approve "SEND" if happy

### Day 3
- 50 emails sent (over 4 hours)
- Start getting first replies
- Next morning: see responses in report

### Week 1
- Send 3-4 batches (150-200 emails)
- Get 15-40 replies
- Have 3-10 interested prospects

### Week 2-4
- Continue daily cycle
- Build relationships
- Close first deals

---

## Customization

### Change Time
Default is 7 AM UTC. To change:

```bash
# 9 AM UTC instead:
openclaw run --cron "0 9 * * *" \
  "python3 ~/.openclaw/workspace/daily_prospect_report.py"

# 8 AM UTC:
openclaw run --cron "0 8 * * *" \
  "python3 ~/.openclaw/workspace/daily_prospect_report.py"
```

### Change Prospect Count
Default is 50. To change to 25 or 100:

Edit `daily_prospect_report.py`:
```python
# Line ~80: change
return unsent[:50]

# To:
return unsent[:25]  # For 25 prospects
# Or:
return unsent[:100] # For 100 prospects
```

### Change Email Delay
Default is 5 minutes. To change:

Edit `send_approved_batch.py`:
```python
DELAY_SECONDS = 300  # 5 minutes (5 * 60)

# Change to 3 minutes:
DELAY_SECONDS = 180  # (3 * 60)

# Or 10 minutes:
DELAY_SECONDS = 600  # (10 * 60)
```

---

## Troubleshooting

### Script Says "No New Prospects"
- You've already contacted all 167 companies
- Time to expand to other cities
- Or create follow-up sequence

### Says "No pending batch found"
- Report must run before you can send
- Run: `python3 daily_prospect_report.py`
- Then use SEND command

### Gmail authentication error
- Check credentials: `ls ~/.openclaw/workspace/.gmail_credentials.json`
- Regenerate if needed

### Cron not running at 7 AM
- Check cron logs: `grep CRON /var/log/syslog`
- Verify timezone is UTC
- Manually run to test

---

## Monitoring

### Check if Cron is Set Up
```bash
crontab -l | grep daily_prospect
```

Should show your scheduled job.

### Check Recent Runs
```bash
ls -lh ~/.openclaw/workspace/daily_report.txt
```

Shows when report last ran.

### Check Sent Emails
```bash
cat ~/.openclaw/workspace/sent_emails_log.json
```

Shows all sent emails with timestamps.

### Check Campaign Stats
```bash
wc -l ~/.openclaw/workspace/sent_emails_log.json
```

Shows how many emails sent so far.

---

## Integration with Your Workflow

This automates the **daily outreach routine**:

1. **Morning (7 AM)** - Report auto-generated ✅
2. **You review** - Check prospects & responses
3. **You approve** - "SEND" command
4. **Emails send** - Over 4 hours automatically ✅
5. **Track responses** - Next morning's report shows them
6. **Follow up** - Reply to interested prospects
7. **Close deals** - Build websites, get paid

**You only need to:**
- Review report each morning (5 minutes)
- Reply "SEND" or "SKIP" (10 seconds)
- Reply to interested prospects (10 minutes/day)

**Everything else is automated!**

---

## Next Steps

### Activate Now
1. Choose Option 1, 2, or 3 above
2. Run the setup command
3. Test with manual run
4. Verify report generates

### Tomorrow Morning
1. Check for auto-generated report
2. Review 50 prospects
3. Reply "SEND" if happy
4. Emails send automatically over 4 hours

### This Week
1. Monitor responses
2. Reply to interested prospects
3. Track conversions
4. Close first deals

---

## Support

If cron setup doesn't work:
1. Manually run: `python3 daily_prospect_report.py`
2. Review any error messages
3. Check file permissions
4. Verify Python installed: `python3 --version`

---

**Status**: Setup files created, ready to activate ✅
**Action**: Choose setup option above and run command
**Timeline**: First report tomorrow at 7 AM

Let me know which setup option you want and I'll help you activate it!
