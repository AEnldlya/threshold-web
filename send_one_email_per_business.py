#!/usr/bin/env python3
"""
Send ONE email to each Boston business
With natural title about professional websites
Auto-responder built-in for replies
"""

import json
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

GMAIL_ADDRESS = 'Andy.li.zhang2010@gmail.com'
APP_PASSWORD = 'xrxy hkrb agpz tgml'

def load_businesses():
    """Load Boston businesses"""
    with open('boston_businesses_final.json', 'r') as f:
        return json.load(f)['businesses']

def get_subject_line(business_type):
    """Natural subject lines by business type"""
    subjects = {
        "Plumber": "We help local plumbers get online",
        "Salon": "Professional website for your salon",
        "Electrician": "Making it easier for customers to find you",
        "Restaurant": "Get more reservations online",
        "HVAC": "One idea for your HVAC business",
        "Cleaning": "Professional website for your service",
        "Pet Grooming": "Let customers book online",
        "Auto Repair": "More customers from online",
        "Real Estate": "Professional website for real estate",
        "Insurance": "Help clients find you online",
        "Bakery": "Professional website for your bakery",
        "Landscaping": "Show your best work online",
        "Contractor": "Professional website for contractors",
        "Dentist": "Modern website for your dental practice",
        "Gym": "Online signup for your gym",
        "Accountant": "Professional website for accountants",
        "Tax Preparation": "Help clients find you this tax season"
    }
    return subjects.get(business_type, "Professional website for your business")

def get_email_body(business_name, business_type):
    """Professional email body - NO PHONE NUMBER"""
    
    bodies = {
        "Plumber": f"""Dear {business_name.split()[0]},

I help local plumbers get professional websites.

I noticed {business_name} doesn't have a website yet. Most customers search online before they call, so you're missing those opportunities.

I build simple, professional sites that:
- Show your work and expertise
- Make it easy for customers to contact you
- Get you more service calls

Timeline: 3 days
Investment: $500

If you're interested, I can show you what it would look like for {business_name}.

Best regards,
Andy""",

        "Salon": f"""Dear {business_name.split()[0]},

I help salons get professional websites with online booking.

{business_name} has great reviews, but customers can't book you online. A website changes that.

I build sites that:
- Show your services and pricing
- Let customers book online
- Display your best photos

Timeline: 3 days
Investment: $500

Interested in seeing what it could do for your salon?

Best regards,
Andy""",

        "Restaurant": f"""Dear {business_name.split()[0]},

I help restaurants get professional websites.

{business_name} has fantastic reviews. A professional website with your menu and reservations would bring in more customers.

I build restaurant sites that:
- Display your menu
- Enable online reservations
- Show your best photos

Timeline: 3 days
Investment: $500

Want to explore this?

Best regards,
Andy""",

        "Electrician": f"""Dear {business_name.split()[0]},

I help electricians get professional websites.

{business_name} has great ratings, but customers searching for you online can't find much. A website changes that.

I build sites that:
- Show your credentials and expertise
- Make it easy to request service
- Build customer trust

Timeline: 3 days
Investment: $500

Interested in a professional website?

Best regards,
Andy""",

        "HVAC": f"""Dear {business_name.split()[0]},

I help HVAC contractors get professional websites.

{business_name} clearly does quality work. A professional website gets you more calls from customers searching online.

I build sites that:
- Show your services
- Enable service requests
- Build credibility

Timeline: 3 days
Investment: $500

Want to explore this?

Best regards,
Andy"""
    }
    
    # Default for other types
    default_body = f"""Dear {business_name.split()[0]},

I help local businesses get professional websites.

{business_name} has great reviews and clearly does quality work. A professional website would help more customers find you online.

I build sites that:
- Are professional and mobile-friendly
- Help customers find and contact you
- Increase your credibility

Timeline: 3 days
Investment: $500

If you're interested, I can show you what it would look like for your business.

Best regards,
Andy"""
    
    return bodies.get(business_type, default_body)

def create_email(to_email, subject, body):
    """Create email message"""
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = GMAIL_ADDRESS
    msg['To'] = to_email
    
    text_part = MIMEText(body, 'plain')
    msg.attach(text_part)
    
    return {'raw': __import__('base64').urlsafe_b64encode(msg.as_bytes()).decode()}

def send_email(to_email, subject, body):
    """Send one email"""
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = to_email
        
        text_part = MIMEText(body, 'plain')
        msg.attach(text_part)
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ADDRESS, APP_PASSWORD.replace(' ', ''))
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending to {to_email}: {e}")
        return False

def setup_auto_responder():
    """Create auto-responder template"""
    
    auto_reply = """
AUTO-RESPONDER SETUP GUIDE
==========================

When a business replies to your email, use this auto-reply:

SUBJECT: Re: [Their original subject]

BODY:

Dear [Their Name],

Thanks for getting back to me!

To get started, I'll need:

1. 5-8 photos:
   - Your storefront/space
   - Team members
   - Work samples or your best offerings
   
2. Basic information:
   - Your hours
   - Main services (2-3 sentences)
   - Phone and email
   - Address

Once I have these, I'll build your website and send you a preview link within 24-48 hours.

You'll review it, let me know any changes, and once approved, payment is $500.

Sound good?

Best regards,
Andy

---

HOW TO SEND AUTO-REPLY:

Option 1 (Gmail):
- Open their reply
- Click "Reply"
- Copy the above message
- Send

Option 2 (Gmail Filters):
- Settings → Filters and Blocked Addresses → Create new filter
- From: [their email]
- Create filter → Send template reply

Option 3 (Manual):
- Just copy-paste the reply message above to each respondent
"""
    
    with open('AUTO_RESPONDER_TEMPLATE.txt', 'w') as f:
        f.write(auto_reply)
    
    print("✓ Auto-responder template created")
    return auto_reply

def main():
    print()
    print("=" * 70)
    print("SENDING ONE EMAIL TO EACH BOSTON BUSINESS")
    print("=" * 70)
    print()
    
    businesses = load_businesses()
    
    print(f"Total businesses: {len(businesses)}\n")
    
    sent_count = 0
    failed_count = 0
    
    for i, business in enumerate(businesses, 1):
        name = business['name']
        email = business['email']
        btype = business['type']
        
        subject = get_subject_line(btype)
        body = get_email_body(name, btype)
        
        print(f"[{i}/{len(businesses)}] Sending to {name}")
        print(f"    Email: {email}")
        print(f"    Subject: {subject}")
        
        if send_email(email, subject, body):
            sent_count += 1
            print(f"    Status: ✓ SENT")
        else:
            failed_count += 1
            print(f"    Status: ✗ FAILED")
        
        print()
        
        # Rate limit: 5 seconds between emails
        if i < len(businesses):
            time.sleep(5)
    
    # Setup auto-responder
    print("\n" + "=" * 70)
    print("SETUP AUTO-RESPONDER")
    print("=" * 70 + "\n")
    setup_auto_responder()
    
    print("\nAuto-responder template saved to: AUTO_RESPONDER_TEMPLATE.txt")
    
    # Summary
    print()
    print("=" * 70)
    print("CAMPAIGN COMPLETE")
    print("=" * 70)
    print(f"Emails sent: {sent_count}")
    print(f"Failed: {failed_count}")
    print(f"Success rate: {sent_count/len(businesses)*100:.1f}%")
    print()
    print("NEXT STEPS:")
    print("1. Responses will arrive in your Gmail inbox")
    print("2. Use the auto-responder template to reply (asks for photos/info)")
    print("3. When they send photos, forward them to me and I'll build the site")
    print("=" * 70)

if __name__ == '__main__':
    main()
