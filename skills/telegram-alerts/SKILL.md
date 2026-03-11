# Telegram Alerts

**Get instant notifications when important business events happen**

## What It Does

Send alerts for:
- New client says YES to website
- Website deployed and live
- Payment received
- Daily business verification summary
- Website review deadline
- Build milestone reached

## Setup

Your Telegram is already configured in OpenClaw!

Bot token: `8728512079:AAExeLiSEkkygUjzxQ1tcbcUZZ5S8KkQdq4`
Your chat: Already authorized

## Alert Types

### 1. New Client Alert
When prospect says YES:
```
🎉 NEW CLIENT ALERT!

Client: Sarah Chen
Business: Hair Salon
Location: Boston, MA
Budget: $2,500

Timeline: 10 days
Start: Tomorrow
Deadline: March 20

Action: Send proposal PDF
```

### 2. Payment Received Alert
```
💰 PAYMENT RECEIVED!

Client: Sarah Chen
Amount: $2,500
Status: Website ready to deploy

Next: Deploy to live domain
Timeline: 1 day
```

### 3. Website Live Alert
```
✅ WEBSITE LIVE!

Client: Sarah Chen
URL: https://example.com
Lighthouse: 95
Status: Ready for traffic

Client notified: Yes
Next: Monthly maintenance
```

### 4. Daily Verification Report
```
📊 TODAY'S BUSINESS VERIFICATION

Prospects found: 25
Passed verification: 18
Ready to call: 15

Calls needed: 15
Estimated closes: 2-3
Potential revenue: $5,000-7,500

Top categories:
🏩 Salons: 6
🍔 Restaurants: 4
🔧 Plumbers: 3
🧘 Fitness: 2
```

### 5. Build Milestone
```
🏗️ BUILD MILESTONE

Client: Sarah Chen
Milestone: Design approved
Days elapsed: 2/10
Days remaining: 8

Next: Start development
Deadline: March 15
```

### 6. Review Deadline
```
⏰ WEBSITE REVIEW DEADLINE

Client: Sarah Chen
Deadline: Tomorrow (March 19)
Time: 9:00 AM

Action: Chase for feedback
Contact: (617) 555-0123
```

## Integration Points

- **With Airtable**: Trigger when status changes
- **With Stripe**: Alert when payment received
- **With GitHub**: Alert when PR merged (site deployed)
- **With Email**: Backup notification (in case you miss Telegram)

## Commands in OpenClaw

```
/alert "Sarah Chen" "YES" "$2500"      # New client alert
/alert "Sarah Chen" "paid"              # Payment received
/alert "Sarah Chen" "live"              # Website live
/alert-daily                            # Daily verification report
```

## Manual Send (for testing)

```bash
# Send test message
curl -X POST \
  https://api.telegram.org/bot8728512079:AAExeLiSEkkygUjzxQ1tcbcUZZ5S8KkQdq4/sendMessage \
  -d chat_id=8613714567 \
  -d text="Test message: Website is live!"
```

## Alert Frequency

- **High priority**: Immediate (new client, payment)
- **Medium priority**: Batch (daily report)
- **Low priority**: Once per day (reminders)

**Best times to send:**
- New client: Immediately (celebrate!)
- Payment: Immediately (confirm receipt)
- Daily report: 8 AM
- Reminders: 3 PM

## Best Practices

✅ **Do:**
- Include key metrics (client name, amount, deadline)
- Use emojis (makes it scannable)
- Send immediately for high-value events
- Batch low-priority alerts

❌ **Don't:**
- Send too many alerts (notification fatigue)
- Send during sleep hours (11 PM - 7 AM)
- Include sensitive info (don't leak client data)

## Useful Links

- Telegram Bot API: https://core.telegram.org/bots/api
- Your Bot: @SummerStreetBot (if public)
