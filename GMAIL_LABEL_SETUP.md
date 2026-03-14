# Gmail Label Setup — Auto-Organize Responses

## Goal
Automatically route all responses from the 167 prospects into a specific folder so you know which ones to follow up with.

---

## Step 1: Create Gmail Labels

In Gmail:

1. Click the **gear icon** (top right)
2. Select **Labels**
3. Click **Create new label**
4. Create these labels:

```
📧 DEMO-PROSPECTS
└── DEMO-INTERESTED (for "yes" responses)
└── DEMO-PHOTOS-SENT (for those who sent photos)
└── DEMO-READY-TO-BUILD (ready to start building)
```

---

## Step 2: Set Up Auto-Filters

### Filter #1: Route ALL Responses to "DEMO-PROSPECTS"

1. Click **gear icon** → **Filters and Blocked Addresses**
2. Click **Create a new filter**
3. In "From" field, enter: (leave empty for all)
4. In "To" field, enter: `Andy.li.zhang2010@gmail.com`
5. Click **Create filter**
6. Check: **Skip the Inbox** (optional, but keeps inbox clean)
7. Check: **Apply label**
8. Select: **DEMO-PROSPECTS**
9. Click **Create filter**

**What this does:** Every reply to your email goes to the "DEMO-PROSPECTS" label.

---

### Filter #2: Auto-Label "YES" Responses

1. Create new filter
2. In "Has the words" field, add keywords:

```
yes
interested
demo
free demo
photos attached
let's do it
sounds good
want to see
```

3. Check: **Apply label: DEMO-INTERESTED**
4. Click **Create filter**

**What this does:** Emails with positive keywords get a special label for quick scanning.

---

### Filter #3: Photos Attached = "DEMO-PHOTOS-SENT"

1. Create new filter
2. In "Has attachment" field, check: **Yes**
3. Check: **Apply label: DEMO-PHOTOS-SENT**
4. Click **Create filter**

**What this does:** Emails with photos attached get flagged so you know they're serious.

---

## Step 3: Check Responses Daily

**Each morning:**

1. Go to **DEMO-PROSPECTS** label
2. Sort by **Newest first**
3. Look for emails marked **DEMO-PHOTOS-SENT**
4. Those are your hottest leads—respond immediately
5. Emails in **DEMO-INTERESTED** are second tier
6. Others can wait

---

## Step 4: Manual Workflow

**When a response comes in:**

1. **They ask "How do I sign up?"**
   - Reply: "Send me 3 photos and let me know what you want on the site"
   - Label: **DEMO-READY-TO-BUILD**

2. **They send photos**
   - Reply: "Building your demo now. 24 hours."
   - Start building
   - Label: **DEMO-READY-TO-BUILD**

3. **They ask questions**
   - Reply with answers
   - Keep label: **DEMO-PROSPECTS**
   - Wait for them to send photos

4. **They say "not interested"**
   - Reply: "No problem. If you change your mind..."
   - Archive (remove labels)

---

## Gmail Label View (What You'll See)

```
Gmail Labels (Left Sidebar)
├── DEMO-PROSPECTS (All responses from the 167)
│   ├── Email from Tony's Restaurant (Subject: "Interested")
│   ├── Email from Smith Plumbing (Subject: "Tell me more")
│   ├── Email from Salon Elena (Subject: "Free demo" + photos)
│   └── 15 more emails this week
├── DEMO-INTERESTED (Positive responses)
│   └── 8 emails with "yes" or "interested"
└── DEMO-PHOTOS-SENT (Photos attached)
    └── 3 emails with photos = your hottest leads
```

---

## Advanced: Gmail Search Operators

**Find specific prospects quickly:**

- `label:DEMO-PROSPECTS from:tony` — Find emails from "tony"
- `label:DEMO-PROSPECTS has:attachment` — Find photos
- `label:DEMO-PROSPECTS "photos attached"` — Find specific replies
- `label:DEMO-INTERESTED newer_than:2d` — Find replies from last 2 days

---

## Spreadsheet Tracking (Optional)

Create a simple Google Sheet:

```
| Business Name | Email | Sent Date | Response | Photos? | Status | Notes |
|---|---|---|---|---|---|---|
| Tony's Restaurant | tony@... | Feb 28 | Yes | Yes | Building | Sent hello |
| Smith Plumbing | smith@... | Feb 28 | No | No | Waiting | Will follow up |
| Salon Elena | elena@... | Feb 28 | Yes | Yes | Demo Built | Waiting for approval |
```

---

## Expected Flow

**Day 1 (Send emails)**
- 167 emails sent (every 5 minutes)
- Labels created and filters set up
- DEMO-PROSPECTS label is empty (no responses yet)

**Day 2 (First responses)**
- 15-20 replies come in
- Auto-sort into DEMO-INTERESTED and DEMO-PHOTOS-SENT
- You reply to photo-senders immediately

**Day 3-7 (Building demos)**
- You build websites for 3-5 prospects
- Send them demo links
- Get their feedback

**Week 2 (Closing)**
- 1-3 say "yes, let's do it"
- Collect $500 each
- Deploy their real sites

---

## Keyboard Shortcut (Make It Faster)

In Gmail settings, enable **keyboard shortcuts**:

- `c` = Compose new email
- `a` = Apply label
- `e` = Archive
- `#` = Delete
- `g` then `l` = Go to labels

**Use these to process responses faster.**

---

## Mobile Access

On your phone:

1. Open Gmail app
2. Tap **Labels** (menu icon)
3. Scroll to **DEMO-PROSPECTS**
4. Tap to see all responses
5. Reply directly from phone

---

## Summary

✓ **Create 4 labels** (DEMO-PROSPECTS, DEMO-INTERESTED, DEMO-PHOTOS-SENT, DEMO-READY-TO-BUILD)

✓ **Set up 3 auto-filters** (route responses, auto-label positives, flag photos)

✓ **Check daily** (morning = process responses)

✓ **Respond fast** (first to reply usually wins)

✓ **Track in spreadsheet** (optional but helpful)

This way, you know exactly which prospects are interested and which ones are hot leads (photos sent = serious).

Zero responses get lost. Zero follow-ups are forgotten.

---

## Quick Setup Checklist

- ☐ Create label: DEMO-PROSPECTS
- ☐ Create label: DEMO-INTERESTED
- ☐ Create label: DEMO-PHOTOS-SENT
- ☐ Create label: DEMO-READY-TO-BUILD
- ☐ Set filter #1 (route all responses)
- ☐ Set filter #2 (positive keywords)
- ☐ Set filter #3 (attachments)
- ☐ Create tracking spreadsheet
- ☐ Enable keyboard shortcuts
- ☐ Ready to send

You're good to go.
