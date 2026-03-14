#!/usr/bin/env python3

import json
import time
import base64
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Business data
businesses = [
    {"name": "McNally Plumbing & Heating", "email": "contact@mcnallyplumbing.com", "phone": "6173581200", "type": "Plumber", "reviews": "4.8 stars, 45 reviews"},
    {"name": "Salon Bella", "email": "salelbella@gmail.com", "phone": None, "type": "Salon", "reviews": "4.9 stars, 67 reviews"},
    {"name": "City Electric Services", "email": "cityelectric@yahoo.com", "phone": None, "type": "Electrician", "reviews": "4.7 stars, 52 reviews"},
    {"name": "North End Pizzeria", "email": "info@northendpizzeria.com", "phone": "6178031111", "type": "Restaurant", "reviews": "4.8 stars, 134 reviews"},
    {"name": "Boston HVAC Solutions", "email": "info@bostonhvacsolutions.com", "phone": None, "type": "HVAC", "reviews": "4.6 stars, 38 reviews"},
    {"name": "Downtown Cleaning Services", "email": "contact@downtownclean.com", "phone": "6172941810", "type": "Cleaning", "reviews": "4.9 stars, 89 reviews"},
    {"name": "Perfect Paws Grooming", "email": "perfectpaws.boston@gmail.com", "phone": None, "type": "Pet Grooming", "reviews": "4.8 stars, 76 reviews"},
    {"name": "Harbor Auto Repair", "email": "harborauto@gmail.com", "phone": None, "type": "Auto Repair", "reviews": "4.7 stars, 93 reviews"},
    {"name": "Urban Real Estate Group", "email": "info@urbanrealty.boston", "phone": None, "type": "Real Estate", "reviews": "4.9 stars, 156 reviews"},
    {"name": "Trinity Insurance Agency", "email": "contact@trinityinsurance.com", "phone": None, "type": "Insurance", "reviews": "4.8 stars, 64 reviews"},
    {"name": "Sweet Creations Bakery", "email": "sweetcreations.boston@gmail.com", "phone": None, "type": "Bakery", "reviews": "4.9 stars, 128 reviews"},
    {"name": "Boston Landscaping & Design", "email": "iabcd7@gmail.com", "phone": None, "type": "Landscaping", "reviews": "4.8 stars, 71 reviews"},
    {"name": "The Urban Gardener Landscape", "email": "info@theurbangardenerlandscape.com", "phone": None, "type": "Landscaping", "reviews": "4.7 stars, 45 reviews"},
    {"name": "Boston Contractors & Developers", "email": "iabcd7@gmail.com", "phone": None, "type": "Contractor", "reviews": "4.8 stars, 82 reviews"},
    {"name": "Bright Dental Studio", "email": "info@brightdental.boston", "phone": None, "type": "Dentist", "reviews": "4.9 stars, 167 reviews"},
    {"name": "Fitness First Gym", "email": "contact@fitnessfirst.boston", "phone": None, "type": "Gym", "reviews": "4.6 stars, 112 reviews"},
    {"name": "Boston Tax & Accounting", "email": "info@bostontaxaccounting.com", "phone": None, "type": "Accountant", "reviews": "4.8 stars, 54 reviews"},
    {"name": "Harbor View Restaurant", "email": "reservations@harborview.boston", "phone": None, "type": "Restaurant", "reviews": "4.8 stars, 189 reviews"},
    {"name": "Quick Tax Solutions", "email": "contact@quicktax.boston", "phone": None, "type": "Tax Preparation", "reviews": "4.7 stars, 41 reviews"},
    {"name": "Eastern Electric Co", "email": "info@easternelectric.boston", "phone": None, "type": "Electrician", "reviews": "4.8 stars, 98 reviews"},
    {"name": "Premier Plumbing Boston", "email": "service@premierplumbing.boston", "phone": None, "type": "Plumber", "reviews": "4.9 stars, 73 reviews"},
    {"name": "Chic Hair Salon", "email": "chichairsalon@gmail.com", "phone": None, "type": "Salon", "reviews": "4.8 stars, 145 reviews"},
    {"name": "Italian Kitchen Restaurant", "email": "info@italiankitchen.boston", "phone": None, "type": "Restaurant", "reviews": "4.8 stars, 167 reviews"},
    {"name": "Professional HVAC Services", "email": "info@professionalhvac.boston", "phone": None, "type": "HVAC", "reviews": "4.7 stars, 62 reviews"},
    {"name": "Green Clean Services", "email": "contact@greenclean.boston", "phone": None, "type": "Cleaning", "reviews": "4.9 stars, 104 reviews"},
    {"name": "Pooch Palace Grooming", "email": "poochpalace.boston@gmail.com", "phone": None, "type": "Pet Grooming", "reviews": "4.8 stars, 91 reviews"},
    {"name": "Reliable Auto Service", "email": "reliableauto@gmail.com", "phone": None, "type": "Auto Repair", "reviews": "4.7 stars, 127 reviews"},
    {"name": "Boston Properties Realty", "email": "info@bostonproperties.realty", "phone": None, "type": "Real Estate", "reviews": "4.8 stars, 189 reviews"},
    {"name": "Guardian Insurance Partners", "email": "contact@guardianinsurance.boston", "phone": None, "type": "Insurance", "reviews": "4.9 stars, 48 reviews"},
    {"name": "Artisan Bakehouse", "email": "artisan.bakehouse.boston@gmail.com", "phone": None, "type": "Bakery", "reviews": "4.9 stars, 156 reviews"}
]

# Email templates by industry
EMAIL_TEMPLATES = {
    "Plumber": {
        "subject": "{name} - Professional Website for Your Plumbing Business",
        "body": """Hi there,

I noticed {name} on Google and saw you've got {reviews} - that's excellent work in the plumbing space.

We're a Boston web design studio, and we specialize in building professional websites for service businesses like plumbing companies. A lot of plumbing businesses miss out on online visibility, and a solid website can bring in steady leads.

We offer:
- Professional, mobile-friendly website design
- Fast turnaround (3-5 days)
- $500 one-time fee (no ongoing contracts)
- Optional $40/month maintenance

Would you be interested in discussing a website redesign for {name}? I can show you a live demo in our temp environment first, and you only pay if you're happy with it.

Let me know if you'd like to chat.

Best,
Andy
Website Design Studio
Boston, MA
Andy.li.zhang2010@gmail.com"""
    },
    "Salon": {
        "subject": "{name} - Beautiful Website to Drive Salon Bookings",
        "body": """Hi there,

I came across {name} - {reviews} is impressive in a competitive market like salons!

We're a Boston-based web design studio that specializes in creating beautiful, modern websites for salons and beauty businesses. A professional website can really help with bookings and client retention.

What we offer:
- Modern, booking-friendly design
- Fast build (3-5 days)
- Mobile-responsive
- $500 one-time investment

I'd love to show you what a website redesign could look like for {name}. We can build a live demo first, so you can see exactly what you'd get before paying anything.

Interested in a quick conversation?

Best,
Andy
Website Design Studio
Boston, MA
Andy.li.zhang2010@gmail.com"""
    },
    "Restaurant": {
        "subject": "{name} - Professional Website to Attract More Diners",
        "body": """Hi there,

I found {name} on Google - {reviews}! That's fantastic in the restaurant business.

We're a Boston web design studio, and we work with restaurants to build professional websites that attract diners. A modern website with your menu, hours, and easy reservation info can really drive foot traffic.

Here's what we do:
- Professional restaurant website
- Menu integration
- Reservation system ready
- Mobile-optimized
- $500 (3-5 day turnaround)

I'd love to show you a live demo of what we could build for {name}. No pressure - you only pay if you love it.

Let me know if you're open to chatting.

Best,
Andy
Website Design Studio
Boston, MA
Andy.li.zhang2010@gmail.com"""
    },
    "Electrician": {
        "subject": "{name} - Professional Website to Generate Service Calls",
        "body": """Hi there,

I came across {name} and noticed your {reviews} rating - that's great reputation in the electrical industry.

We're a Boston web design studio specializing in professional websites for electricians and trade businesses. A solid online presence can bring in consistent service calls.

What we build for electricians:
- Professional service website
- Service area map
- Testimonial showcase
- Mobile-friendly
- $500 (3-5 days)

Would you be interested in seeing a live demo of a website redesign for {name}? I can build it in our temp environment first.

Let me know,
Andy
Website Design Studio
Boston, MA
Andy.li.zhang2010@gmail.com"""
    },
    "HVAC": {
        "subject": "{name} - Website to Boost HVAC Service Inquiries",
        "body": """Hi there,

Found {name} on Google - {reviews} is solid in HVAC!

We're a Boston web design studio that builds professional websites for HVAC companies. A good website can really help generate steady service inquiries.

Here's our offer:
- Professional HVAC service site
- Service areas & contact form
- Fast build (3-5 days)
- Mobile-optimized
- $500 one-time

I'd love to show you what a website redesign could do for {name}. We build a live demo first, so you can see it before committing.

Interested?

Best,
Andy
Website Design Studio
Boston, MA
Andy.li.zhang2010@gmail.com"""
    }
}

DEFAULT_TEMPLATE = {
    "subject": "{name} - Professional Website Redesign",
    "body": """Hi there,

I came across {name} on Google and was impressed by your {reviews} rating.

We're a Boston-based web design studio, and we specialize in creating professional, modern websites for local businesses. Whether you need a new website or a redesign, we can help.

What we offer:
- Professional, modern design
- Mobile-responsive
- Fast turnaround (3-5 days)
- $500 one-time fee

I'd love to show you a live demo of what a website could look like for {name}. There's no obligation - you only pay if you're happy with it.

Would you be open to a quick chat?

Best,
Andy
Website Design Studio
Boston, MA
Andy.li.zhang2010@gmail.com"""
}

# SMS template
SMS_TEMPLATE = """Hi {name}, we're a Boston web design studio. We build professional websites for local businesses in 3-5 days for $500. Interested in discussing a website for your business? Reply YES to chat."""

# Outreach log
try:
    with open('outreach_log.json', 'r') as f:
        outreach_log = json.load(f)
except:
    outreach_log = []

def get_template(business_type):
    """Get email template by industry"""
    return EMAIL_TEMPLATES.get(business_type, DEFAULT_TEMPLATE)

def craft_email(business):
    """Craft personalized email"""
    template = get_template(business['type'])
    subject = template['subject'].format(name=business['name'])
    body = template['body'].format(
        name=business['name'],
        reviews=business['reviews']
    )
    return subject, body

def send_email_smtp(recipient, subject, body):
    """Send email via SMTP (Gmail)"""
    try:
        # Gmail SMTP
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "Andy.li.zhang2010@gmail.com"
        
        # Read app password from file (need to set this up first)
        try:
            with open('.gmail_app_password', 'r') as f:
                app_password = f.read().strip()
        except:
            print("❌ Gmail app password not found. Create .gmail_app_password file first.")
            return False
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Send
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"   Error sending email: {str(e)}")
        return False

def log_outreach(business, method, status, error=None):
    """Log outreach attempt"""
    record = {
        "timestamp": datetime.now().isoformat(),
        "business": business['name'],
        "contact": business.get('email') or business.get('phone'),
        "method": method,
        "type": business['type'],
        "status": status,
        "error": error
    }
    outreach_log.append(record)
    
    with open('outreach_log.json', 'w') as f:
        json.dump(outreach_log, f, indent=2)

def should_skip(contact):
    """Skip if already contacted"""
    return any(log['contact'] == contact and log['status'] == 'sent' for log in outreach_log)

def run_outreach(limit=None):
    """Run email outreach with SMS fallback"""
    print("🤖 Starting Personalized Outreach Campaign\n")
    print(f"Sender: Andy.li.zhang2010@gmail.com")
    print(f"Method: Email (primary), SMS (fallback for phone-only)\n")
    print("-" * 60 + "\n")
    
    count = 0
    
    for business in businesses:
        if limit and count >= limit:
            break
        
        has_email = business.get('email')
        has_phone = business.get('phone')
        
        # Use email if available
        if has_email:
            if should_skip(has_email):
                print(f"✓ Already sent to {business['name']}, skipping")
                continue
            
            subject, body = craft_email(business)
            
            print(f"📧 Email → {business['name']}")
            print(f"   To: {has_email}")
            
            if send_email_smtp(has_email, subject, body):
                print(f"   ✓ Sent\n")
                log_outreach(business, "email", "sent")
                count += 1
            else:
                print(f"   ✗ Failed\n")
                log_outreach(business, "email", "failed")
        
        # Fallback to SMS if no email
        elif has_phone:
            if should_skip(has_phone):
                print(f"✓ Already contacted {business['name']}, skipping")
                continue
            
            sms_body = SMS_TEMPLATE.format(name=business['name'])
            
            print(f"💬 SMS → {business['name']}")
            print(f"   To: +1{has_phone}")
            print(f"   Message: {sms_body[:50]}...\n")
            
            # SMS would go here (requires Twilio API)
            print(f"   ⚠️  SMS sending not configured yet. Requires Twilio API.\n")
            log_outreach(business, "sms", "pending_twilio_setup")
        
        else:
            print(f"⚠️  {business['name']} - No contact info available\n")
            log_outreach(business, "none", "no_contact_info")
        
        # 5-minute delay between sends
        if count < len(businesses) and has_email:
            print(f"   ⏳ Waiting 5 minutes before next email...\n")
            time.sleep(300)
    
    print(f"\n{'='*60}")
    print(f"✓ Outreach complete. {count} emails sent.")
    print(f"Check outreach_log.json for full tracking")
    print(f"{'='*60}")

if __name__ == "__main__":
    run_outreach()
