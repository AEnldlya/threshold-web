#!/usr/bin/env python3
"""
Send FREE DEMO emails to 167 Boston businesses.
Spreads sends over multiple days (5-minute delays).
Customizes emails by business category.
Tracks sent emails in log file.
"""

import csv
import json
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Email templates by category
TEMPLATES = {
    'Restaurant': {
        'subject': '[Business] — Your Free Website Demo',
        'body': '''Hi [Owner],

I'm [Your Name], Web Development Lead.

We built a professional website demo for [Business] — completely free, no obligation.

Here's what it includes:
✓ Professional hero section with your restaurant photos
✓ Full menu (organized and easy to read)
✓ Online reservation system (customers book 24/7)
✓ Your Google reviews displayed prominently
✓ Contact info, hours, location map
✓ Mobile-friendly (looks perfect on phones)

Why we're doing this:
Most restaurants in Boston aren't online yet, and they're losing customers. We want to show you what's possible—before you decide to invest anything.

The demo takes 15 minutes to review. It's a real, working website. You can see exactly what your customers will see.

Here's what we need from you:
1. 2-3 photos of your restaurant (inside, food, team)
2. Your menu (we can format it)
3. What you'd want to highlight (signature dishes, specials, etc.)
4. Hours of operation + address

Reply to this email with those details, and we'll build your demo in 24 hours.

No payment. No pressure. Just a real working website you can show to friends and decide if you want to go live.

Worth 15 minutes to see what's possible?

Thanks,
[Your Name]
Web Development Lead'''
    },
    
    'Electrical': {
        'subject': '[Business] — Your Free Professional Website Demo',
        'body': '''Hi [Owner],

I'm [Your Name], Web Development Lead.

We built a professional website demo for [Business] — completely free, no obligation.

Here's what it includes:
✓ Professional homepage with "24/7 Emergency Service"
✓ Your services clearly listed
✓ Your license, insurance, and experience displayed
✓ Customer testimonials and reviews
✓ Clear pricing (no "call for quote" nonsense)
✓ Online service booking form
✓ Your phone number prominently displayed
✓ Mobile-friendly (customers can call with one tap)

Why we're doing this:
Most service companies in Boston aren't getting found online. We want to show you what professional looks like—before you invest anything.

The demo takes 10 minutes to review. It's a real, working website that gets you found on Google.

Here's what we need from you:
1. Your company name, phone, address
2. 2-3 photos (team, work, truck, or office)
3. Your license number
4. List of services you offer
5. What you want to highlight

Reply to this email with those details, and we'll build your demo in 24 hours.

No payment. No pressure. Just a real website you can show to other contractors and decide if you want to go live.

Worth 10 minutes to see how this brings you more calls?

Thanks,
[Your Name]
Web Development Lead'''
    },
    
    'Plumbing': {
        'subject': '[Business] — Your Free Professional Website Demo',
        'body': '''Hi [Owner],

I'm [Your Name], Web Development Lead.

We built a professional website demo for [Business] — completely free, no obligation.

Here's what it includes:
✓ Professional homepage with "24/7 Emergency Service"
✓ Your services clearly listed
✓ Your license, insurance, and experience displayed
✓ Customer testimonials and reviews
✓ Clear pricing (no "call for quote" nonsense)
✓ Online service booking form
✓ Your phone number prominently displayed
✓ Mobile-friendly (customers can call with one tap)

Why we're doing this:
Most plumbers in Boston aren't getting found online. When someone's pipes burst at midnight, they Google "emergency plumber near me." If you don't have a website, they call the other guy.

The demo takes 10 minutes to review. It's a real, working website that gets you more calls.

Here's what we need from you:
1. Your company name, phone, address
2. 2-3 photos (team, work, truck, or office)
3. Your license number
4. List of services you offer
5. What you want to highlight

Reply to this email with those details, and we'll build your demo in 24 hours.

No payment. No pressure. Just a real website you can show to other plumbers and decide if you want to go live.

Worth 10 minutes to get more emergency calls?

Thanks,
[Your Name]
Web Development Lead'''
    },
    
    'HVAC': {
        'subject': '[Business] — Your Free Professional Website Demo',
        'body': '''Hi [Owner],

I'm [Your Name], Web Development Lead.

We built a professional website demo for [Business] — completely free, no obligation.

Here's what it includes:
✓ Professional homepage with "24/7 Emergency Service"
✓ Your services clearly listed
✓ Your license, insurance, and experience displayed
✓ Customer testimonials and reviews
✓ Clear pricing (no "call for quote" nonsense)
✓ Online service booking form
✓ Your phone number prominently displayed
✓ Mobile-friendly (customers can call with one tap)

Why we're doing this:
Most HVAC companies in Boston aren't getting found online. We want to show you what professional looks like—before you invest anything.

The demo takes 10 minutes to review. It's a real, working website that gets you more calls.

Here's what we need from you:
1. Your company name, phone, address
2. 2-3 photos (team, work, truck, or office)
3. Your license number
4. List of services you offer
5. What you want to highlight

Reply to this email with those details, and we'll build your demo in 24 hours.

No payment. No pressure. Just a real website you can show to other contractors and decide if you want to go live.

Worth 10 minutes to see how this brings you more business?

Thanks,
[Your Name]
Web Development Lead'''
    },
    
    'Auto Repair': {
        'subject': '[Business] — Your Free Professional Website Demo',
        'body': '''Hi [Owner],

I'm [Your Name], Web Development Lead.

We built a professional website demo for [Business] — completely free, no obligation.

Here's what it includes:
✓ Professional homepage
✓ Services clearly listed (oil change, brakes, transmission, etc.)
✓ Pricing transparency (no "call for quote")
✓ Before/after photos of your work
✓ Customer reviews
✓ Clear contact info, hours, location
✓ Online appointment booking
✓ Mobile-friendly

Why we're doing this:
Car owners search for repair shops online. If they can't find you with a professional website, they pick someone else. We want to show you what's possible.

The demo takes 10 minutes to review. It's a real website that brings you more customers.

Here's what we need from you:
1. 2-3 photos (shop interior, team, finished work)
2. List of services
3. Common pricing (oil change, brake job, etc.)
4. Hours and location
5. What you want to highlight

Reply to this email with those details, and we'll build your demo in 24 hours.

No payment. No pressure. Just a website you can show other shop owners and decide if you want to go live.

Worth 10 minutes to get more customers finding you?

Thanks,
[Your Name]
Web Development Lead'''
    },
    
    'Salon': {
        'subject': '[Business] — Your Free Professional Website Demo',
        'body': '''Hi [Owner],

I'm [Your Name], Web Development Lead.

We built a professional website demo for [Business] — completely free, no obligation.

Here's what it includes:
✓ Beautiful hero section with your salon photos
✓ Your services and pricing clearly displayed
✓ Team bios (let clients know who's cutting their hair)
✓ Online booking system (customers book appointments 24/7)
✓ Before/after photos of your best work
✓ Customer reviews and testimonials
✓ Hours, location, phone number
✓ Mobile-friendly (clients can book from their phone)

Why we're doing this:
Clients book appointments online. If you don't have a website, they book somewhere else. We want to show you what's possible—before you decide.

The demo takes 10 minutes to review. It's a real, working website.

Here's what we need from you:
1. 2-3 photos of your salon (interior, team, work)
2. List of services and pricing
3. Team member names (if you want)
4. Before/after photos of your best work
5. Hours of operation + location

Reply to this email with those details, and we'll build your demo in 24 hours.

No payment. No pressure. Just a website you can show clients and decide if you want to go live.

Worth 10 minutes to see what brings you more bookings?

Thanks,
[Your Name]
Web Development Lead'''
    },
    
    'Dentist': {
        'subject': '[Business] — Your Free Professional Website Demo',
        'body': '''Hi Dr./Owner [Name],

I'm [Your Name], Web Development Lead.

We built a professional website demo for [Business] — completely free, no obligation.

Here's what it includes:
✓ Professional homepage (builds trust immediately)
✓ Your credentials and background
✓ Services explained (in plain English, no jargon)
✓ New patient welcome message
✓ Before/after photos of your work
✓ Patient testimonials
✓ Clear contact info and hours
✓ Online appointment booking
✓ Mobile-friendly (patients can book from their phone)

Why we're doing this:
Patients research dentists online. If you're not coming up with a professional site, they pick someone else. We want to show you what's possible—before you invest.

The demo takes 10 minutes to review. It's a real website that brings you new patients.

Here's what we need from you:
1. Your background/credentials
2. 2-3 professional photos (office, team, you)
3. Before/after photos (smile transformations)
4. List of services you offer
5. Hours and location

Reply to this email with those details, and we'll build your demo in 24 hours.

No payment. No pressure. Just a website you can show to colleagues and decide if you want to go live.

Worth 10 minutes to attract more patients?

Thanks,
[Your Name]
Web Development Lead'''
    },
}

def load_businesses():
    """Load businesses from CSV."""
    businesses = []
    with open('/home/clawdbot/.openclaw/workspace/boston_167_LAUNCH_READY.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            businesses.append(row)
    return businesses

def get_owner_name(business_name):
    """Extract likely owner first name from business name."""
    words = business_name.split()
    # If first word is followed by apostrophe, it's likely owner name
    for word in words:
        if "'" in word:
            return word.replace("'s", "")
    # Otherwise, return first word
    return words[0] if words else "there"

def get_template(category):
    """Get email template for business category."""
    # Try exact match
    if category in TEMPLATES:
        return TEMPLATES[category]
    
    # Try partial match
    for key in TEMPLATES:
        if key.lower() in category.lower():
            return TEMPLATES[key]
    
    # Default to generic service template
    return TEMPLATES['Electrical']

def customize_email(template, business_name, owner_name, category, sender_name="Ryan"):
    """Customize email template with business info."""
    subject = template['subject'].replace('[Business]', business_name)
    body = template['body'].replace('[Business]', business_name)
    body = body.replace('[Owner]', owner_name)
    body = body.replace('[Your Name]', sender_name)
    
    return subject, body

def send_email(recipient_email, subject, body, sender_email, sender_password):
    """Send email via Gmail SMTP."""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        
        # Add body
        msg.attach(MIMEText(body, 'plain'))
        
        # Send via Gmail SMTP
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        
        return True, None
    except Exception as e:
        return False, str(e)

def main():
    print("=" * 80)
    print("SENDING FREE DEMO EMAILS TO 167 BOSTON BUSINESSES")
    print("=" * 80)
    
    # Gmail credentials
    sender_email = 'Andy.li.zhang2010@gmail.com'
    sender_password = 'xrxy hkrb agpz tgml'  # App password
    sender_name = 'Ryan'  # Your name
    
    # Load businesses
    businesses = load_businesses()
    print(f"\nLoaded {len(businesses)} businesses")
    print(f"Sending emails every 5 minutes...\n")
    
    # Tracking
    sent_log = []
    failed_log = []
    
    # Send emails
    for i, business in enumerate(businesses, 1):
        name = business['Name']
        email = business['Email']
        category = business['Category']
        
        # Get owner name
        owner_name = get_owner_name(name)
        
        # Get template
        template = get_template(category)
        
        # Customize
        subject, body = customize_email(template, name, owner_name, category, sender_name)
        
        # Send
        success, error = send_email(email, subject, body, sender_email, sender_password)
        
        if success:
            status = "✓ SENT"
            sent_log.append({
                'index': i,
                'name': name,
                'email': email,
                'category': category,
                'timestamp': datetime.now().isoformat(),
                'status': 'sent'
            })
        else:
            status = f"❌ FAILED: {error[:30]}"
            failed_log.append({
                'index': i,
                'name': name,
                'email': email,
                'error': error,
                'timestamp': datetime.now().isoformat()
            })
        
        # Print progress
        if i % 10 == 0 or i == len(businesses):
            print(f"[{i:3}/{len(businesses)}] {status} | {name:35} → {email}")
        
        # Wait 5 minutes (300 seconds) before next email
        if i < len(businesses):
            print(f"     Waiting 5 minutes before next send...")
            time.sleep(300)  # 5 minutes
    
    # Save logs
    print("\n" + "=" * 80)
    print("CAMPAIGN COMPLETE")
    print("=" * 80)
    
    sent_count = len(sent_log)
    failed_count = len(failed_log)
    
    print(f"\nTotal sent: {sent_count}")
    print(f"Total failed: {failed_count}")
    print(f"Success rate: {sent_count / len(businesses) * 100:.1f}%")
    
    # Save sent log
    with open('/home/clawdbot/.openclaw/workspace/sent_demo_emails.json', 'w') as f:
        json.dump(sent_log, f, indent=2)
    
    # Save failed log
    if failed_log:
        with open('/home/clawdbot/.openclaw/workspace/failed_demo_emails.json', 'w') as f:
            json.dump(failed_log, f, indent=2)
        print(f"\n[!] {failed_count} emails failed. See failed_demo_emails.json")
    
    print(f"\n[✓] Sent log saved: sent_demo_emails.json")
    print("\nNext steps:")
    print("1. Check Gmail labels (DEMO-PROSPECTS folder)")
    print("2. Look for DEMO-PHOTOS-SENT label (hottest leads)")
    print("3. Reply to those with photos immediately")
    print("4. Start building demos for 'ready' prospects")

if __name__ == '__main__':
    main()
