# Gmail API Setup for Andy Zhang
## Step-by-Step (You do the clicks, I handle the rest)

---

## YOUR INFO STORED
```
Name: Andy Zhang
Phone: 603-306-7508
Email: Andy.li.zhang2010@gmail.com
```

I'll use these in all outreach emails.

---

## GMAIL API SETUP (5 MINUTES)

### Step 1: Open Google Cloud Console
```
Go to: https://console.cloud.google.com/
```

### Step 2: Create New Project
```
Top left, click: "Select a Project"
Click: "New Project"
Project name: "Website Sales"
Click: "Create"
(wait 1-2 minutes for creation)
```

### Step 3: Enable Gmail API
```
At top, search bar: search "Gmail API"
Click: Gmail API (first result)
Click: "Enable"
(wait 30 seconds)
```

### Step 4: Create OAuth 2.0 Credentials
```
Left sidebar: Click "Credentials"
Blue button: "Create Credentials"
Type: Select "OAuth 2.0 Client ID"

First time? It'll ask you to configure consent screen:
- Click "Configure Consent Screen"
- User type: "External"
- Click "Create"
- App name: "Website Sales"
- User support email: andy.li.zhang2010@gmail.com
- Developer contact: andy.li.zhang2010@gmail.com
- Click "Save and Continue"
- (Skip optional scopes)
- Click "Save and Continue"
- Go back to Credentials

Back at Credentials:
- Click "Create Credentials" again
- Type: "OAuth 2.0 Client ID"
- Application type: "Desktop application"
- Name: "Website Sales App"
- Click "Create"
```

### Step 5: Download JSON File
```
A pop-up appears with your credentials
Click: "Download" (or the down arrow)
File saved: client_secret_XXXXX.json

Move it to your desktop or downloads folder.
```

### Step 6: Send Me the Credentials
```
Open the JSON file in notepad/text editor.
Copy the entire contents and paste in a message to me.

OR just give me these 4 fields:
- client_id: "..."
- client_secret: "..."
- redirect_uris: ["..."]
- auth_uri: "..."

I only need these to authenticate. 
Your Gmail stays 100% secure.
```

### Step 7: First Time Authorization (Browser popup)
```
When I send the first batch of emails, your browser will open.
Google will ask: "Website Sales wants to access your Gmail account"
Click: "Allow"
That's it. Credentials saved locally.

Future sends: No browser popup needed.
```

---

## PAYMENT SETUP (For When Customers Say YES)

**How it works:**

1. **Customer agrees to buy** ($500 website)
2. **You send them a payment link** (Stripe, PayPal, or Wave)
3. **They pay directly to you** (money goes to your bank)
4. **You deliver the website**
5. **They keep paying $40/month** for maintenance

---

## OPTION A: Stripe (Recommended)

### Setup (5 minutes):
```
1. Go to: stripe.com
2. Click: "Start now"
3. Sign up with email: andy.li.zhang2010@gmail.com
4. Verify email
5. Add your US bank account (where deposits go)
6. Done
```

### How to charge customers:
```
You give them a payment link:
"https://buy.stripe.com/aEl6qXXXXXXXXX"

They click → enter credit card → pay $500
Money deposits to your bank in 1-2 days.

For recurring $40/month:
You create a "subscription" link in Stripe dashboard
Send link to customer
They sign up for auto-billing

Cost: 2.9% + $0.30 per transaction
Example: $500 sale = costs you $14.80 (Stripe fee)
```

---

## OPTION B: Wave (Free)

### Setup (5 minutes):
```
1. Go to: waveapps.com
2. Sign up with email: andy.li.zhang2010@gmail.com
3. Add your bank account
4. Create invoice template
5. Send invoice to customer
```

### How to charge:
```
You create invoice in Wave:
- Client name
- Service: "Professional Website - 3 Day Build"
- Amount: $500
- Due date: Today

Click "Send" → email goes to customer
They click link → pay via credit card
Money deposits to your bank

For recurring:
Wave can't auto-bill, so you manually send $40/month invoices

Cost: FREE (Wave makes money from accounting add-ons, not payments)
```

---

## OPTION C: PayPal

### Setup (5 minutes):
```
1. Go to: paypal.com
2. Sign up (if you don't have account)
3. Create "Payment Link"
4. Set amount: $500
5. Copy link
```

### How to charge:
```
You send customer: "https://paypal.me/XXXXX/500"
They click → pay with PayPal or credit card
Money goes to your PayPal account
Withdraw to bank anytime

Cost: 3.49% + $0.49 per transaction
Example: $500 = costs you $17.99
```

---

## MY RECOMMENDATION

**Use Stripe** because:
- Cleanest setup
- Recurring billing built-in (for $40/month)
- 2.29% fee is competitive
- Professional invoice emails
- Mobile-friendly payment page

---

## DOMAIN STRATEGY

**Key point:** You DON'T rent domains upfront.

Here's when domains happen:

### Timeline:

**NOW (Mass outreach):**
- Send 200-300 emails
- No domains needed yet

**WHEN CUSTOMER SAYS YES:**
- You discuss domain options with them
- Example: "bobsplumbing-denver.com" or "denverplumbing.pro"
- **You offer to handle it for them** (include in $500 deal)

**HOW TO BUY DOMAIN:**

Option 1: **You buy it yourself** (with your card)
```
Go to: namecheap.com
Search domain: "bobsplumbing-denver.com"
Cost: $12/year
You pay $12 → own domain
You give domain to customer (it's theirs to use)
After year 1, they renew or you charge $50/year to manage
```

Option 2: **Customer buys it** (with their card)
```
You give them instructions:
"Go to namecheap.com, search 'bobsplumbing-denver.com', cost is $12/year.
Buy it, then send me the login. I'll point it to Netlify."
```

Option 3: **They give you their card** (you buy on their behalf)
```
Risky legally (you'd be handling their payment info)
Not recommended
Stick to Options 1 or 2
```

---

## MY ROLE IN DOMAINS

I **cannot:**
- Store credit cards (security risk)
- Make purchases on your behalf (legal liability)

I **can:**
- Tell you which domain registrar to use (Namecheap, GoDaddy, Google Domains)
- Write instructions for customers to buy themselves
- Configure DNS settings once domain is purchased
- Point domain to Netlify (technical setup)

---

## THE FLOW (WHEN CUSTOMER BUYS)

**Customer:** "Yes, I want the website"

**You:** "Great! Here's how it works:

$500 for the website + domain + 1 year hosting.
You own everything.

**Domain:** I'll get you a custom domain like 'bobsplumbing-denver.com' 
— I'll handle registering it. Cost: $12/year (included).

**Payment:** You can pay now or when the site goes live.
[Send Stripe link]

**Maintenance:** Optional — $40/month keeps it updated and performing well.
[Send maintenance contract]"

**Then:**
1. You buy domain on Namecheap ($12)
2. Give customer login (they own it)
3. Build website
4. Deploy to Netlify
5. Point domain to Netlify DNS
6. Site lives at bobsplumbing-denver.com
7. Collect $500 (minus Stripe fee)
8. Set up $40/month recurring (if they say yes)

---

## SUMMARY

| Component | What I Do | What You Do |
|-----------|-----------|-----------|
| **Gmail API** | Use it to send emails | Set it up (click Google buttons, give me JSON) |
| **Outreach emails** | Write 200-300 personalized emails | Just reply when leads respond |
| **Payments** | Help you set up Stripe | Click 5 buttons, add bank account |
| **Domains** | Configure DNS, help with technical setup | Buy on Namecheap ($12/year per customer) or tell them to buy |
| **Website building** | Build custom sites | Provide photos + content |
| **Phone closing** | None | You call interested leads, close deals |

---

## NEXT STEPS

1. **Set up Gmail API** (follow steps above, takes 5 min)
2. **Send me the credentials** (client_id, client_secret, redirect_uri)
3. **Set up Stripe** (5 min, get your payment link ready)
4. **Confirm:** I'm ready to research + write 200-300 personalized emails

You'll have:
- Gmail API ready to send emails ✅
- Stripe ready to collect payments ✅
- 200-300 personalized emails queued ✅
- Me ready to send them tomorrow morning ✅

**Do the Gmail setup now. Reply with credentials when done.**
