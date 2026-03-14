# Email Outreach

**Send proposals, payment reminders, and deployment notifications to clients**

## What It Does

Send professional emails:
- Welcome emails with proposal
- Figma mockup ready for review
- Website deployed and live
- Payment reminder with Stripe link
- Monthly maintenance updates
- Custom sequences for different client types

## Setup

### Gmail Configuration

1. Enable 2-factor authentication on your Google account
2. Create app password: https://myaccount.google.com/apppasswords
3. Store credentials:
   ```bash
   export GMAIL_EMAIL="Andy.li.zhang2010@gmail.com"
   export GMAIL_PASSWORD="your_app_password_here"
   ```

### Alternative: Use Himalaya CLI

```bash
# Install
brew install himalaya

# Configure Gmail
himalaya config create gmail

# Test
himalaya list gmail INBOX
```

## Email Templates

### 1. Welcome / Proposal Ready
```
To: [client-email]
Subject: Your Website Proposal - $2,500 Professional Design

Hi [Client Name],

Great to meet you! I've prepared a custom proposal for your [Business Type] website.

Your proposal includes:
- Professional Next.js website
- Mobile-responsive design
- Lighthouse 95+ performance
- 10-day build timeline
- 1 month free maintenance

Total investment: $2,500

To get started, click here to secure your spot: [STRIPE PAYMENT LINK]

Questions? Reply to this email or call [YOUR PHONE]

Best,
Andy
```

### 2. Figma Mockup Ready
```
To: [client-email]
Subject: Your Website Design Mockup - Ready for Review

Hi [Client Name],

Your website mockup is ready! 

View the design here: [FIGMA LINK]

Please review and reply with:
- Any color/font changes
- Sections you want to add
- Content updates

Timeline: Design approval → build starts immediately

Let me know by [DATE]!

Best,
Andy
```

### 3. Website Ready for Review
```
To: [client-email]
Subject: Your Website is Live - Preview Now

Hi [Client Name],

Your website is complete and ready for review!

Preview: [STAGING NETLIFY URL]

Please test:
- Desktop/mobile/tablet views
- All buttons work
- Form submissions send emails
- Loading speed (should be instant)

Reply with any changes needed. Revisions are free!

Next: Payment received → site goes live on your domain

Best,
Andy
```

### 4. Payment Reminder
```
To: [client-email]
Subject: Payment Link - Your Website is Ready

Hi [Client Name],

Your website is complete and live on a preview link!

To deploy it to your domain and go live, complete payment here:

[STRIPE PAYMENT LINK - $2,500]

Once received, your website is:
✓ Published to your domain
✓ Google indexed
✓ Ready for customer traffic

Payment needed by: [DATE]

Questions? Call me: [YOUR PHONE]

Best,
Andy
```

### 5. Website Live Confirmation
```
To: [client-email]
Subject: Your Website is LIVE! 🎉

Hi [Client Name],

Congratulations! Your website is now live at:

[LIVE URL]

What's included:
✓ Professional design and messaging
✓ Contact form (replies to your email)
✓ Google Business Profile integration
✓ Mobile-optimized
✓ Fast loading (Lighthouse 95+)

Next steps:
1. Share the link with friends/customers
2. Add photos/content updates (free this month)
3. Monthly maintenance plan: $100/month

Call if you have questions: [YOUR PHONE]

Welcome to the web!

Andy
```

### 6. Monthly Maintenance Reminder
```
To: [client-email]
Subject: Your Website Maintenance - February Update

Hi [Client Name],

Your website is running smoothly! This month we:

✓ Updated [specific change]
✓ Monitored performance (0 downtime)
✓ Security patches applied

Website stats this month:
- [Traffic number] visitors
- [Calls/leads] from website
- [Conversion metric]

Next month: [Planned improvements]

Monthly maintenance continues: $100/month

Questions? Reply here or call [YOUR PHONE]

Best,
Andy
```

## Sending Emails via Command Line

### Using Himalaya

```bash
# List emails
himalaya list gmail INBOX

# Send email
himalaya send gmail \
  --from "Andy.li.zhang2010@gmail.com" \
  --to "client@example.com" \
  --subject "Your Website is Ready" \
  --text "Hi, your website is live at..."

# Create draft
himalaya create gmail \
  --to "client@example.com" \
  --subject "Payment Reminder"
```

### Using curl + Gmail API

```bash
# Requires OAuth setup
# More complex but fully automated
```

## Email Sequence Automation

### Discovery Phase
- Day 0: Send discovery call confirmation
- Day 1: Send proposal document (PDF)
- Day 3: Follow up if no response

### Build Phase
- Day 5: Figma mockup ready
- Day 8: Website ready for review
- Day 9: Final revision if needed

### Launch Phase
- Day 10: Payment reminder
- Day 10+6h: Second payment reminder
- Day 10+12h: Payment received → live!

### Maintenance Phase
- Month 2+: Monthly check-in
- Month 12: Renewal reminder

## Integration Points

- **With Stripe**: Include payment link in emails
- **With Airtable**: Get email from prospects table
- **With Telegram**: Alert when email is sent/bounced

## Commands in OpenClaw

```
/email send [client-email] "proposal"     # Send proposal template
/email send [client-email] "mockup-ready" # Figma mockup ready
/email send [client-email] "live"         # Website live notification
/email send [client-email] "payment"      # Payment reminder
/email sequence [client-id]               # Start full sequence
```

## Best Practices

✅ **Do:**
- Use templates (faster, consistent)
- Include your phone number (builds trust)
- Include payment link (make it easy to buy)
- Send at 9am on weekdays (higher open rate)
- Follow up after 3 days of no response

❌ **Don't:**
- Send too many emails (max 1 per day)
- Use generic "Hello sir" greetings (personalize)
- Hide contact info (client should reach you easily)
- Send payment links in first email (build trust first)

## Measuring Success

Track in Airtable:
- Open rate: If client clicks link, update "Opened" checkbox
- Click rate: If client visits staging, update "Reviewed" checkbox
- Conversion: Payment received = deal closed

## Useful Links

- Gmail: https://mail.google.com
- Stripe payment links: https://dashboard.stripe.com/payment-links
- Himalaya: https://www.himalaya-mail.io/
