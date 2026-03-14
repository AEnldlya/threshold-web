# Lead Database Setup (Airtable)

## Why Track Everything?

You need to know:
- How many people said yes vs. no
- Which outreach method works best
- When to follow up
- What your pipeline looks like

This takes 2 minutes per day and saves hours of confusion.

---

## AIRTABLE SETUP (Free)

**Step 1: Create Airtable Account**
- Go to airtable.com
- Sign up (free)
- Create new base called "Website Leads"

**Step 2: Create This Table**

### Fields (columns):

1. **ID** (auto-number)
2. **Business Name** (text)
3. **Owner/Manager Name** (text)
4. **Industry** (select dropdown):
   - Plumber
   - Electrician
   - HVAC
   - Salon/Barber
   - Restaurant
   - Accountant
   - Lawyer
   - Therapist
   - Gym/Trainer
   - Other

5. **City** (text)
6. **Phone** (phone format)
7. **Email** (email format)
8. **Website Exists?** (select):
   - No website
   - Has website (outdated)
   - Has website (OK)
   - Other

9. **Source** (select dropdown):
   - Cold email
   - Cold call
   - Door-to-door
   - Referral
   - LinkedIn
   - Other

10. **Status** (select dropdown):
    - Prospect (never contacted)
    - Contacted 1x (waiting)
    - Contacted 2x (waiting)
    - Contacted 3x (last attempt)
    - Meeting Booked
    - Demo Scheduled
    - Proposal Sent
    - Won (Closed)
    - Lost (Not interested)
    - Lost (Ghosted after 3+)
    - Nurture (follow up later)

11. **First Contact Date** (date)
12. **Last Contact Date** (date)
13. **Next Follow-up Date** (date)
14. **Notes** (long text):
    - What they said
    - Objections
    - Specific interests
    - Best time to call
    - Any personal info

15. **Contact Attempts** (number)
    - Count: 1, 2, 3, etc.

16. **Deal Value** ($)
    - If won: $500
    - If upsell: $40/month
    - If lost: $0

17. **Tags** (multi-select):
    - Hot prospect
    - Objection: budget
    - Objection: not interested
    - Objection: too busy
    - Decision maker
    - Referred by [name]

---

## DAILY WORKFLOW (2 minutes/day)

### Morning (5 min)
1. Open Airtable
2. Create new records for today's cold outreach (3-5 records)
   - Add: business name, owner, phone, email, city, industry
   - Status: "Prospect"
   - Source: "Cold email" or "Cold call"
   - First Contact Date: today

3. Filter view: Status = "Contacted 1x" + Next Follow-up Date = today
   - These are people who deserve follow-up email/call
   - Make it happen
   - Update "Last Contact Date" = today
   - Update "Contact Attempts" = 2
   - Update "Status" = "Contacted 2x"

4. Filter view: Status = "Meeting Booked"
   - Any calls today?
   - Prep notes
   - Have their phone # ready

### After Each Contact
- Update "Last Contact Date"
- Update "Contact Attempts" (increment by 1)
- Update "Status" (based on what they said)
- Update "Next Follow-up Date" (3-7 days from now usually)
- Add "Notes" (what they said, objections, tone, etc.)

### After Win
- Change Status to "Won"
- Add Deal Value: $500
- Add a tag: "Closed - [Date]"
- Add notes: "Paid deposit on [Date]"
- Schedule: "Next Follow-up" = when you'll upsell monthly maintenance

### Evening (2 min)
- Review: How many Contacted → How many Meeting Booked → How many Won
- Update pipeline numbers in a simple sheet:
  - Prospects: 47
  - Contacted 1x: 12
  - Contacted 2x: 5
  - Meetings: 2
  - Won: 1

---

## AIRTABLE VIEWS (Set These Up)

### View 1: "Today's Follow-ups"
- Filter: Next Follow-up Date = today
- Sort: By priority (Status ascending)
- Shows: Name, Phone, Last Contact, Status, Notes
- **Use this:** Every morning

### View 2: "Hot Pipeline"
- Filter: Status = "Meeting Booked" OR "Demo Scheduled" OR "Proposal Sent"
- Sort: By date (oldest first)
- Shows: Name, Phone, Status, Next Follow-up
- **Use this:** Track deals

### View 3: "All Wins"
- Filter: Status = "Won"
- Sort: By date (newest first)
- Shows: Name, Business, Date, Deal Value, Industry
- **Use this:** Portfolio / case studies / referrals

### View 4: "Lost Leads (30+ days)"
- Filter: Status = "Lost" AND Last Contact Date < 30 days ago
- Shows: Name, Status, Why (notes)
- **Use this:** Analyze why you're losing deals

### View 5: "Nurture List"
- Filter: Status = "Nurture"
- Sort: By Next Follow-up
- Shows: Name, Notes, Last Contact, Next Follow-up
- **Use this:** Revisit once a month

---

## MONTHLY REVIEW (1st of month)

Open Airtable and answer:

1. **How many prospects did I contact?** [number]
2. **What was my response rate?** [meetings / contacts]
   - Target: 10-20%
3. **How many meetings did I book?** [number]
   - Target: 2-4
4. **How many deals did I close?** [number]
   - Target: 1-2
5. **What was my close rate?** [wins / meetings]
   - Target: 30-50%
6. **Which source converts best?** [cold call? referral? etc.]
   - Double down on this
7. **Which objection comes up most?** [budget? timing? etc.]
   - Address this in your pitch next month
8. **How many in "Nurture" list?** [number]
   - Follow up with 2-3 this month
9. **Average time from contact → win?** [X days]
   - Should be 7-21 days
10. **Revenue this month?** [# of wins × $500]

---

## EXAMPLE ENTRIES

### Example 1: Cold Email Contact
```
ID: 001
Business Name: Thompson's Plumbing
Owner: John Thompson
Industry: Plumber
City: Portland, OR
Phone: (503) 555-0192
Email: john@thompsonsplumbing.com
Website Exists: No website
Source: Cold email
Status: Contacted 1x
First Contact Date: 2024-02-27
Last Contact Date: 2024-02-27
Next Follow-up Date: 2024-03-05 (5 days)
Contact Attempts: 1
Notes: "Sent initial email. No response yet. Will follow up Tue."
Tags: [not yet]
```

### Example 2: Cold Call Converted
```
ID: 002
Business Name: Sarah's Salon
Owner: Sarah Chen
Industry: Salon
City: Portland, OR
Phone: (503) 555-0284
Email: sarah@sarahssalon.com
Website Exists: No website
Source: Cold call
Status: Won
First Contact Date: 2024-02-26
Last Contact Date: 2024-02-28
Next Follow-up Date: 2024-03-15 (30 days, for maintenance upsell)
Contact Attempts: 2
Deal Value: $500 (website build) + $40/month (maintenance)
Tags: [Closed - Feb 2024, Hot prospect, Referred by friend]
Notes: "Called Tue, no answer. Called Wed, spoke with Sarah. 
She said 'Been meaning to do this!' Booked demo. Demo Wed at 2pm - 
she loved mockup. Signed contract same day. $250 deposit received 2/28.
Planning to launch site by 3/2. Will upsell maintenance after 2 weeks.
Very responsive client, asks detailed questions. Referred friend 
(Jane's Nails) - follow up with Jane ASAP."
```

### Example 3: Lost Lead
```
ID: 003
Business Name: Bob's Appliance Repair
Owner: Bob Wilson
Industry: Other (appliance repair)
City: Portland, OR
Phone: (503) 555-0917
Email: bob@bobsappliance.com
Website Exists: Has website (OK)
Source: Cold call
Status: Lost (Not interested)
First Contact Date: 2024-02-24
Last Contact Date: 2024-02-26
Contact Attempts: 2
Notes: "Called Sat morning, Bob said 'business is slow, not 
spending on marketing.' Called again Mon, he said 'already have 
website.' Offered to show improvement ideas - he declined politely. 
Good guy, just not interested now. Added to Nurture for 6 months."
Tags: [Lost - budget, Nurture 6mo]
```

---

## CALCULATIONS YOU CAN DO IN AIRTABLE

### Conversion Rate Formula
```
Created field: "Conversion %"
Formula: IF(Status = "Won", 100, 0)
Then: SUM all values, divide by total records
Shows: X% of all prospects converted
```

### Revenue Tracking
```
Created field: "Month" (extract from First Contact Date)
Then: ROLLUP on Deal Value by Month
Shows: Revenue by month
```

### Days to Close
```
Created field: "Days to Close"
Formula: IF(Status = "Won", 
    DATETIME_DIFF(Last Contact Date, First Contact Date, 'days'), 
    "")
```

---

## QUICK STATS TO TRACK

Every week, write these down (I recommend a separate sheet):

```
Week of [DATE]:

Total Outreach: 50 (20 calls, 20 emails, 10 door-to-door)
New Prospects Added: 45
Responses: 7 (14% response rate)
Meetings Booked: 2
Deals Closed: 0 (will close next week)
---

Cumulative (Month to Date):
Total Outreach: 200
Meetings: 8
Closed: 2 ($1,000 revenue)
Close Rate: 25%
Average Days to Close: 12 days
```

---

## WHY THIS MATTERS

After 30 days, you'll see:
- Which outreach method converts best
- How many touches it takes to close
- What your real conversion rates are
- Where to double down

This data turns you from "guessing" to "optimizing."

Example: If door-to-door converts at 35% but cold email at 8%, 
you should spend more time doing door-to-door visits (even though 
it feels slower).

---

## AIRTABLE FORMULA EXAMPLES

### If you want to automate some things:

**1. Auto-count contact attempts:**
```
Let the "Contact Attempts" field be manual (you increment it)
```

**2. Auto-generate next follow-up date:**
```
Formula: DATEADD({Last Contact Date}, 5, 'days')
This says: "5 days from last contact, follow up again"
```

**3. Auto-flag hot prospects:**
```
IF(AND(Status="Meeting Booked", DATETIME_DIFF(TODAY(), {Last Contact Date}, 'days') < 3),
  "🔥 FOLLOW UP TODAY", "")
```

---

**Get this set up today. It takes 15 minutes.**

After one month of use, you'll have data that tells you exactly 
what's working and what's not.

That's your competitive advantage.
