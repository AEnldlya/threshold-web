#!/usr/bin/env python3

import json
import time
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Business data with industry type
businesses = [
    {"name": "McNally Plumbing & Heating", "email": "contact@mcnallyplumbing.com", "type": "Plumber", "city": "Boston", "reviews": "4.8 stars, 45 reviews"},
    {"name": "Salon Bella", "email": "salelbella@gmail.com", "type": "Salon", "city": "Boston", "reviews": "4.9 stars, 67 reviews"},
    {"name": "City Electric Services", "email": "cityelectric@yahoo.com", "type": "Electrician", "city": "Boston", "reviews": "4.7 stars, 52 reviews"},
    {"name": "North End Pizzeria", "email": "info@northendpizzeria.com", "type": "Restaurant", "city": "Boston", "reviews": "4.8 stars, 134 reviews"},
    {"name": "Boston HVAC Solutions", "email": "info@bostonhvacsolutions.com", "type": "HVAC", "city": "Boston", "reviews": "4.6 stars, 38 reviews"},
    {"name": "Downtown Cleaning Services", "email": "contact@downtownclean.com", "type": "Cleaning", "city": "Revere", "reviews": "4.9 stars, 89 reviews"},
    {"name": "Perfect Paws Grooming", "email": "perfectpaws.boston@gmail.com", "type": "Pet Grooming", "city": "Boston", "reviews": "4.8 stars, 76 reviews"},
    {"name": "Harbor Auto Repair", "email": "harborauto@gmail.com", "type": "Auto Repair", "city": "Boston", "reviews": "4.7 stars, 93 reviews"},
    {"name": "Urban Real Estate Group", "email": "info@urbanrealty.boston", "type": "Real Estate", "city": "Boston", "reviews": "4.9 stars, 156 reviews"},
    {"name": "Trinity Insurance Agency", "email": "contact@trinityinsurance.com", "type": "Insurance", "city": "Boston", "reviews": "4.8 stars, 64 reviews"},
    {"name": "Sweet Creations Bakery", "email": "sweetcreations.boston@gmail.com", "type": "Bakery", "city": "Boston", "reviews": "4.9 stars, 128 reviews"},
    {"name": "Boston Landscaping & Design", "email": "iabcd7@gmail.com", "type": "Landscaping", "city": "Boston", "reviews": "4.8 stars, 71 reviews"},
    {"name": "The Urban Gardener Landscape", "email": "info@theurbangardenerlandscape.com", "type": "Landscaping", "city": "Boston", "reviews": "4.7 stars, 45 reviews"},
    {"name": "Boston Contractors & Developers", "email": "iabcd7@gmail.com", "type": "Contractor", "city": "Boston", "reviews": "4.8 stars, 82 reviews"},
    {"name": "Bright Dental Studio", "email": "info@brightdental.boston", "type": "Dentist", "city": "Boston", "reviews": "4.9 stars, 167 reviews"},
    {"name": "Fitness First Gym", "email": "contact@fitnessfirst.boston", "type": "Gym", "city": "Boston", "reviews": "4.6 stars, 112 reviews"},
    {"name": "Boston Tax & Accounting", "email": "info@bostontaxaccounting.com", "type": "Accountant", "city": "Boston", "reviews": "4.8 stars, 54 reviews"},
    {"name": "Harbor View Restaurant", "email": "reservations@harborview.boston", "type": "Restaurant", "city": "Boston", "reviews": "4.8 stars, 189 reviews"},
    {"name": "Quick Tax Solutions", "email": "contact@quicktax.boston", "type": "Tax Preparation", "city": "Boston", "reviews": "4.7 stars, 41 reviews"},
    {"name": "Eastern Electric Co", "email": "info@easternelectric.boston", "type": "Electrician", "city": "Boston", "reviews": "4.8 stars, 98 reviews"},
    {"name": "Premier Plumbing Boston", "email": "service@premierplumbing.boston", "type": "Plumber", "city": "Boston", "reviews": "4.9 stars, 73 reviews"},
    {"name": "Chic Hair Salon", "email": "chichairsalon@gmail.com", "type": "Salon", "city": "Boston", "reviews": "4.8 stars, 145 reviews"},
    {"name": "Italian Kitchen Restaurant", "email": "info@italiankitchen.boston", "type": "Restaurant", "city": "Boston", "reviews": "4.8 stars, 167 reviews"},
    {"name": "Professional HVAC Services", "email": "info@professionalhvac.boston", "type": "HVAC", "city": "Boston", "reviews": "4.7 stars, 62 reviews"},
    {"name": "Green Clean Services", "email": "contact@greenclean.boston", "type": "Cleaning", "city": "Boston", "reviews": "4.9 stars, 104 reviews"},
    {"name": "Pooch Palace Grooming", "email": "poochpalace.boston@gmail.com", "type": "Pet Grooming", "city": "Boston", "reviews": "4.8 stars, 91 reviews"},
    {"name": "Reliable Auto Service", "email": "reliableauto@gmail.com", "type": "Auto Repair", "city": "Boston", "reviews": "4.7 stars, 127 reviews"},
    {"name": "Boston Properties Realty", "email": "info@bostonproperties.realty", "type": "Real Estate", "city": "Boston", "reviews": "4.8 stars, 189 reviews"},
    {"name": "Guardian Insurance Partners", "email": "contact@guardianinsurance.boston", "type": "Insurance", "city": "Boston", "reviews": "4.9 stars, 48 reviews"},
    {"name": "Artisan Bakehouse", "email": "artisan.bakehouse.boston@gmail.com", "type": "Bakery", "city": "Boston", "reviews": "4.9 stars, 156 reviews"}
]

# Personalized email templates by industry
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
Website Design Studio
Boston, MA"""
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
Website Design Studio
Boston, MA"""
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
Website Design Studio
Boston, MA"""
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
Website Design Studio
Boston, MA"""
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
Website Design Studio
Boston, MA"""
    }
}

# Default template for other industries
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
Website Design Studio
Boston, MA"""
}

# Outreach log
try:
    with open('outreach_log.json', 'r') as f:
        outreach_log = json.load(f)
except:
    outreach_log = []

def get_email_template(business_type):
    """Get personalized template based on business type"""
    return EMAIL_TEMPLATES.get(business_type, DEFAULT_TEMPLATE)

def craft_email(business):
    """Craft personalized email for a business"""
    template = get_email_template(business['type'])
    
    subject = template['subject'].format(name=business['name'])
    body = template['body'].format(
        name=business['name'],
        reviews=business['reviews']
    )
    
    return subject, body

def log_outreach(business, status, error=None):
    """Log outreach attempt"""
    record = {
        "timestamp": datetime.now().isoformat(),
        "business": business['name'],
        "email": business['email'],
        "type": business['type'],
        "status": status,
        "error": error
    }
    outreach_log.append(record)
    
    with open('outreach_log.json', 'w') as f:
        json.dump(outreach_log, f, indent=2)

def should_skip(business):
    """Check if we've already sent to this business"""
    return any(log['email'] == business['email'] and log['status'] == 'sent' for log in outreach_log)

def print_preview(business):
    """Print email preview (for testing)"""
    subject, body = craft_email(business)
    print(f"\n📧 Email to: {business['email']}")
    print(f"Subject: {subject}")
    print(f"\nBody:\n{body}")
    print("-" * 60)

# Main
if __name__ == "__main__":
    print("🤖 Personalized Email Outreach Automation\n")
    
    # Print previews for first 3 businesses (testing)
    print("Preview of emails:\n")
    for business in businesses[:3]:
        print_preview(business)
    
    print(f"\n✓ Generated {len(businesses)} personalized emails")
    print("Ready to send with Gmail API + 5-min delays")
    print("\nNext: Import Gmail credentials and execute sends")
