# Duplicate Prevention & City Rotation System

## Critical: NEVER Send Duplicate Emails

Sending duplicate emails to the same business is **CATASTROPHIC** for your reputation.

### What Happens If You Send Duplicates
- Business thinks you're unprofessional
- Emails get marked as spam
- They lose trust immediately
- You lose the sale
- They tell others (bad reputation)

### Your System Prevents This Automatically ✅

---

## How the System Works

### 1. Master Tracking File
**File**: `all_contacted_businesses.json`

This file is the **source of truth**. It contains EVERY business ever contacted, including:
- Email address (primary key)
- Business name
- City & state
- Category
- First contact date
- Contact history
- Responses received
- Conversion status

**RULE**: If an email is in this file, it can NEVER be contacted again.

### 2. Daily Report Generation
**File**: `daily_prospect_report_v2.py`

When generating your 7 AM report:
1. Load all prospects for current week's city
2. Check against `all_contacted_businesses.json`
3. **EXCLUDE** any email already in master file
4. Show only completely NEW prospects
5. Display count of already-contacted businesses

**Result**: Report shows ONLY businesses never contacted before.

### 3. Batch Sending
**File**: `send_approved_batch_v2.py`

When you say "SEND":
1. Get list of emails to send
2. Load business details
3. Send emails (with 5-min delays)
4. **UPDATE master file** with each send
5. Mark these businesses as "contacted"
6. Never show them in future reports

**Result**: Master file grows by 50 each day. Duplicates impossible.

---

## City Rotation (Weekly)

### How It Works

**File**: `cities_rotation.json`

Every 7 days, you switch to a new city:

```
Week 1: Boston, MA (167 prospects)
   ├─ Day 1-7: Email 350 total (50/day × 7)
   └─ Result: ~35 responses, ~5 closed deals

Week 2: Providence, RI (new prospects)
   ├─ Day 8-14: Email 350 total (50/day × 7)
   └─ Result: ~35 responses, ~5 closed deals

Week 3: Hartford, CT (new prospects)
   ├─ Day 15-21: Email 350 total
   └─ Result: ~35 responses, ~5 closed deals

Week 4: Manchester, NH (new prospects)
   ...and so on
```

### Rotation Schedule

```json
{
  "cities": [
    {
      "name": "Boston",
      "state": "MA",
      "week": 1,
      "prospects": 167,
      "status": "active"
    },
    {
      "name": "Providence",
      "state": "RI",
      "week": 2,
      "status": "pending"
    },
    {
      "name": "Hartford",
      "state": "CT",
      "week": 3,
      "status": "pending"
    }
  ]
}
```

### Automatic City Switching

The report script automatically:
1. Calculates current week number
2. Loads current week's city
3. Loads prospects from that city's file
4. Shows in report header

**You don't need to change anything!** It happens automatically.

---

## Master File Structure

### Example Entry

```json
{
  "tony@tonypizza.com": {
    "email": "tony@tonypizza.com",
    "business_name": "Tony's Pizzeria",
    "city": "Boston",
    "state": "MA",
    "category": "Restaurant",
    "first_contact_date": "2026-03-02T10:45:00Z",
    "contact_count": 1,
    "status": "Sent",
    "responses": [
      {
        "date": "2026-03-02T14:30:00Z",
        "message": "Interested in demo",
        "action_needed": "Schedule call"
      }
    ],
    "follow_ups": [
      {
        "date": "2026-03-03T09:00:00Z",
        "type": "Reply to inquiry",
        "message": "Thanks for interest! Can you send business photos?"
      }
    ],
    "conversion_status": "Interested",
    "notes": "High confidence. Quick responder. Scheduled demo for Mar 5."
  }
}
```

### Key Fields

- **email** - PRIMARY KEY (must be unique)
- **contact_count** - How many times contacted (1 = first, 2+ = follow-up only)
- **status** - "Sent", "Responded", "Interested", "Demo Scheduled", "Closed"
- **responses** - Array of replies received
- **follow_ups** - Your follow-up actions
- **conversion_status** - Current stage in sales pipeline
- **notes** - Context and next steps

---

## Duplicate Prevention Workflow

### Daily Report Generation

```
7:00 AM → daily_prospect_report_v2.py runs

1. Load cities_rotation.json
   └─ Determine current week (1, 2, 3, etc.)
   └─ Get city for this week (Boston week 1, Providence week 2, etc.)

2. Load all_contacted_businesses.json
   └─ Read list of EVERY email ever contacted
   └─ Store in memory as "contacted_set"

3. Load prospects for current city
   └─ Load boston_167_VERIFIED_FINAL.csv (or other city file)
   └─ Store as "all_prospects"

4. Filter: all_prospects - contacted_set
   └─ Subtract all previously contacted emails
   └─ Keep only NEW prospects

5. Sort by confidence
   └─ Highest confidence scores first

6. Select top 50
   └─ Take first 50 NEW prospects

7. Generate report
   └─ Show these 50 with details
   └─ Display count of already-contacted
   └─ Show city rotation week

8. Save report & pending batch
   └─ daily_report.txt (for you to read)
   └─ pending_send_batch.json (for sending)
```

### Sending Process

```
You say "SEND" → send_approved_batch_v2.py runs

1. Load pending_send_batch.json
   └─ 50 emails ready to send

2. Load business_details from CSV
   └─ Get name, city, category, etc.

3. For each of 50 emails:
   └─ Log to sent_emails_log.json
   └─ Log to outreach_tracker.csv
   └─ Wait 5 minutes
   └─ Continue to next

4. CRITICAL: Update all_contacted_businesses.json
   └─ For each sent email:
      └─ If not in master file: ADD NEW ENTRY
      └─ If already exists: UPDATE contact_count & notes
   └─ Set status = "Sent"
   └─ Set contact_date = now
   └─ Save file

5. Clean up pending_send_batch.json
   └─ Delete temporary file
```

**Result**: Master file now has 50 more emails. They can NEVER be contacted again.

---

## Verification: No Duplicates Possible

### Before Sending Each Day

1. Check master file: `cat all_contacted_businesses.json | wc -l`
2. Should have grown by 50 from yesterday
3. All yesterday's emails now excluded from today's report

### Example Timeline

**Day 1** (Boston, Week 1)
```
Morning report: 167 prospects available
You send: 50 emails
Master file now has: 50 entries
```

**Day 2** (Boston, Week 1)
```
Morning report: 117 prospects available (167 - 50 sent yesterday)
You send: 50 emails
Master file now has: 100 entries
```

**Day 3** (Boston, Week 1)
```
Morning report: 67 prospects available (167 - 100 sent)
You send: 50 emails
Master file now has: 150 entries
```

**Day 4** (Boston, Week 1)
```
Morning report: 17 prospects available (167 - 150 sent)
You send: 17 emails
Master file now has: 167 entries
Boston fully contacted! ✅
```

**Day 5** (Week 1 ends)
```
No new prospects for Boston
Wait for week 2 rotation
```

**Day 8** (Providence, Week 2)
```
Morning report: 200 prospects available (NEW city, fresh prospects)
You send: 50 emails
Master file now has: 217 entries
```

---

## Adding New Cities

### When Boston Runs Out

1. Research new city (Providence, Hartford, etc.)
2. Find 150-200 verified prospects
3. Create CSV file: `providence_prospects.csv`
4. Update `cities_rotation.json`:
   ```json
   {
     "name": "Providence",
     "state": "RI",
     "prospects_file": "providence_prospects.csv",
     "week": 2,
     "status": "active"
   }
   ```
5. System automatically switches Week 2

### Cities to Add (Eventually)

- Providence, RI (150 prospects)
- Hartford, CT (150 prospects)
- Manchester, NH (150 prospects)
- Springfield, MA (150 prospects)
- New Haven, CT (150 prospects)
- Burlington, VT (100 prospects)

**Year 1 Strategy**: 8-12 cities × 150-200 prospects each = 1,200-2,400 total leads

---

## Safety Checks

### Before Each "SEND" Approval

```
System checks:
✓ Are these emails in all_contacted_businesses.json? NO (good!)
✓ Were these already sent today? NO (good!)
✓ Is this a new city this week? Check cities_rotation.json
✓ Do all emails have valid format? Check for @
✓ Are confidence scores good? 50%+ minimum
```

All checks pass → Safe to send!

### Manual Verification

```bash
# Check total contacted:
cat all_contacted_businesses.json | jq '.total_contacted'

# Check if email was already sent:
cat all_contacted_businesses.json | jq '.contacts | has("tony@tonypizza.com")'

# List all Boston contacts:
cat all_contacted_businesses.json | jq '.contacts | keys[] | select(. | contains("boston"))' 

# View current week's city:
cat cities_rotation.json | jq '.cities[] | select(.week == 1)'
```

---

## What Happens If Someone Gets Contacted Twice

**Scenario**: You accidentally send to `tony@tonypizza.com` twice

1. **First email** (Day 1):
   - Added to all_contacted_businesses.json
   - Status: "Sent"

2. **Duplicate email** (Day 10, new city cycle):
   - Report generation checks: "Is tony@tonypizza.com in master file?"
   - Answer: YES (from Day 1)
   - Report excludes it: ✅ Duplicate prevented

3. **If you override** (manually send anyway):
   - Script catches it: "This email is already in master file"
   - Logs as duplicate
   - Updates contact_count: 2
   - Notes: "DUPLICATE EMAIL SENT - BAD"
   - You see warning in logs

---

## Monthly Statistics

### Master File Growth

```
Week 1 (Boston): 350 emails → 350 total in master
Week 2 (Providence): 350 emails → 700 total in master
Week 3 (Hartford): 350 emails → 1,050 total in master
Week 4 (Manchester): 350 emails → 1,400 total in master
Month 1: 1,400 businesses contacted, NEVER contacted twice ✅
```

### Conversion Tracking

Master file tracks:
- **Status**: Sent → Responded → Interested → Demo → Closed
- **Contact count**: How many touches per prospect
- **Follow-ups**: Sequence of interactions
- **Revenue**: Which ones closed

Example:
```
Day 1: "tony@tonypizza.com" status="Sent"
Day 3: "tony@tonypizza.com" status="Responded", responses=[...interest...]
Day 4: "tony@tonypizza.com" status="Interested", follow_ups=[...photo request...]
Day 7: "tony@tonypizza.com" status="Demo Scheduled"
Day 10: "tony@tonypizza.com" status="Closed", notes="Paid $500"
```

---

## Rules (NEVER BREAK THESE)

1. **If email is in master file, it is NEVER contacted again**
2. **Each day's report only shows NEW prospects (never before contacted)**
3. **After sending, master file MUST be updated immediately**
4. **Cities rotate weekly automatically (no manual switching needed)**
5. **All contacts tracked permanently (no deletion)**
6. **Every follow-up/response recorded in master file**

---

## Files Reference

| File | Purpose |
|------|---------|
| `all_contacted_businesses.json` | MASTER tracking file (source of truth) |
| `cities_rotation.json` | Weekly city schedule |
| `daily_prospect_report_v2.py` | Generates reports (checks master file) |
| `send_approved_batch_v2.py` | Sends emails & updates master |
| `boston_167_VERIFIED_FINAL.csv` | Boston prospects (original) |
| `sent_emails_log.json` | Simple list of sent emails |
| `outreach_tracker.csv` | Spreadsheet-style tracking |

---

## Status: Duplicate Prevention ACTIVE ✅

Your system now:
- ✅ Tracks every business ever contacted
- ✅ Never shows duplicates in reports
- ✅ Prevents sending to same business twice
- ✅ Rotates cities automatically
- ✅ Updates master file after each send
- ✅ Logs all interactions permanently

**Result**: Zero duplicate emails. Professional reputation intact. 🎯
