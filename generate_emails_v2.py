#!/usr/bin/env python3
"""
Generate emails with:
- Titles about what we do
- No phone numbers
- Never send duplicate to same person
"""

import json

# Email templates - focus on WHAT WE DO, not salesy angles
TEMPLATES = {
    "Plumber": {
        "subject_template": "Professional Website for {name}",
        "body_template": """Hey {owner},

I help local businesses get professional websites.

I noticed {name} on Google - you've got {reviews}, but no website. A lot of people search before they call, so you're missing those moments.

I build simple sites that show your work and make it easy for customers to find and reach you. Most plumbers I work with see more calls pretty quickly.

If you're interested in seeing what that would look like for your business, I can put something together and send it over. No obligation.

Let me know if you want to explore it.

Best,
Andy"""
    },
    
    "Salon": {
        "subject_template": "Get Your Salon Online",
        "body_template": """Hi {owner},

I build professional websites for local businesses.

I was looking at {name} and noticed you don't have a website - even though you've got {reviews} and your Instagram looks great. A lot of people want to book online but can't.

I could build you a simple site with online booking. Takes about 3 days, costs $500.

Want to see what it would look like for {name}?

Best,
Andy"""
    },
    
    "Restaurant": {
        "subject_template": "Website for {name}",
        "body_template": """Hey {owner},

I build websites for local restaurants.

I noticed {name} has {reviews} but when people search for you, they can't see your menu or book online. That's leaving money on the table.

I help restaurants get simple sites with menus, hours, and online reservations. Most see a boost in bookings pretty quickly.

Want to see what that would look like?

Best,
Andy"""
    },
    
    "Electrician": {
        "subject_template": "Professional Website for Your Business",
        "body_template": """Hey {owner},

I help local service businesses get online.

{name} has {reviews} on Google, which is great. But when people search for electricians in {city}, they need more than just a Google listing - they want to see who they're hiring.

A website builds trust and gets you more calls. I can build you one in 3 days for $500.

Want to check it out?

Best,
Andy"""
    },
    
    "HVAC": {
        "subject_template": "Get Found Online - HVAC Business",
        "body_template": """Hi {owner},

I build websites for HVAC contractors.

{name} has {reviews}, which shows you do great work. But a lot of people searching for HVAC services don't find you - they find competitors with websites.

A simple site changes that. You show up more in searches, customers feel more confident, you get more calls.

Interested in seeing what that could look like?

Best,
Andy"""
    },
    
    "Gym": {
        "subject_template": "Website for Your Fitness Studio",
        "body_template": """Hey {owner},

I build websites for gyms and fitness studios.

{name} has {reviews} and clearly people love what you're doing. But when they search for gyms in {city}, they can't sign up online or see your classes easily.

A website with online signup usually brings in more members. 3 days to build, $500.

Want to see what it could do for you?

Best,
Andy"""
    },
    
    "Accountant": {
        "subject_template": "Professional Website for Accountants",
        "body_template": """Hey {owner},

I build websites for accounting firms.

{name} has {reviews}, but I noticed there's no website. For accountants, that's a missed opportunity - clients want to see you're professional and established before they reach out.

A website builds trust and brings in new clients. Most accountants I work with find it pays for itself in a month.

Want to explore it?

Best,
Andy"""
    },
    
    "Auto Repair": {
        "subject_template": "Website for Your Auto Shop",
        "body_template": """Hey {owner},

I build websites for auto repair shops.

{name} has {reviews} - customers clearly trust you. But when people search for auto repair, they can't find you or see what you offer.

A website gets you more visibility and more customers. Simple, professional, shows your work.

Interested in seeing what that looks like?

Best,
Andy"""
    },

    "Cleaning Service": {
        "subject_template": "Get More Cleaning Jobs - Website",
        "body_template": """Hey {owner},

I help cleaning services get online.

{name} has {reviews}, which is fantastic. But people who need cleaning can't book you online - they have to call or message.

A website with online booking usually brings in more jobs. 3 days, $500.

Want to see what it could do for your business?

Best,
Andy"""
    },

    "Pet Grooming": {
        "subject_template": "Website for Your Pet Grooming Business",
        "body_template": """Hi {owner},

I build websites for pet groomers.

{name} has {reviews} and pet owners clearly love you. But when they search for grooming, they can't book online easily.

A website with online booking gets you more bookings. Most groomers see results pretty quickly.

Want to check it out?

Best,
Andy"""
    },

    "Dentist": {
        "subject_template": "Professional Website for Your Dental Practice",
        "body_template": """Hi {owner},

I build websites for dental practices.

{name} has {reviews} but no website. When people search for dentists, they want to see your team and feel confident before they book.

A professional website brings in new patients. Most practices see results within the first month.

Want to explore it?

Best,
Andy"""
    },
    
    "Contractor": {
        "subject_template": "Website for Your Construction Business",
        "body_template": """Hey {owner},

I build websites for contractors and builders.

{name} has {reviews} - you clearly do quality work. But a lot of potential clients can't find you or see your portfolio online.

A website with your work samples brings in more jobs and bigger deals. 3 days, $500.

Want to see what that could look like?

Best,
Andy"""
    }
}

def generate_email(business):
    """Generate personalized email for a business"""
    biz_type = business['type']
    
    if biz_type in TEMPLATES:
        template = TEMPLATES[biz_type]
    else:
        # Generic template
        template = {
            "subject_template": "Professional Website for {name}",
            "body_template": """Hey {owner},

I help local businesses get professional websites.

{name} has {reviews} but no website. Most customers search before they call, so you're missing those opportunities.

I build simple sites that showcase your business and make it easy for customers to find and contact you.

Want to see what that would look like for your business?

Best,
Andy"""
        }
    
    subject = template["subject_template"].format(
        name=business['name'],
        owner=business['owner']
    )
    
    body = template["body_template"].format(
        owner=business['owner'],
        name=business['name'],
        reviews=business['google_reviews'],
        city=business['city']
    )
    
    return {
        'to': business['email'],
        'subject': subject,
        'body': body,
        'business_name': business['name'],
        'owner': business['owner'],
        'city': business['city']
    }

def main():
    # Load business list
    with open('/home/clawdbot/.openclaw/workspace/business_outreach_list.json', 'r') as f:
        data = json.load(f)
    
    # Generate emails
    emails = []
    seen_emails = set()
    
    for business in data['businesses']:
        email_addr = business['email']
        
        # Skip duplicates
        if email_addr in seen_emails:
            print(f"⚠️  Skipping duplicate: {email_addr}")
            continue
        
        seen_emails.add(email_addr)
        email = generate_email(business)
        emails.append(email)
    
    # Save to file
    with open('/home/clawdbot/.openclaw/workspace/personalized_emails.json', 'w') as f:
        json.dump(emails, f, indent=2)
    
    print(f"✓ Generated {len(emails)} emails")
    print(f"✓ No duplicates (checking email addresses)")
    print(f"✓ No phone numbers in emails")
    print(f"✓ Subject lines focus on what we do")
    print()
    print("--- EXAMPLE EMAIL ---")
    print()
    if emails:
        print(f"To: {emails[0]['to']}")
        print(f"Subject: {emails[0]['subject']}")
        print()
        print(emails[0]['body'])

if __name__ == '__main__':
    main()
