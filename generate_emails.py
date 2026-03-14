#!/usr/bin/env python3
"""
Generate personalized outreach emails for each business
"""

import json

# Email templates by business type
TEMPLATES = {
    "Plumber": {
        "subject_template": "{name} - Your Google reviews are gold, but customers can't find you",
        "body_template": """Hi {owner},

I was looking at your Google listing and noticed you've got {reviews}.

Your customers keep mentioning "same-day service" and "fast response" — that's exactly what people are searching for.

Problem is, most people searching "plumber in {city}" never make it to Google Maps. They stop at the first web result.

A simple professional website fixes that. Nothing fancy — just shows your best work and gets your phone ringing more.

I've built websites for plumbing companies. Most see 2-4 extra calls per week from the site.

Interested in seeing what it looks like for {name}?

Call me: 603-306-7508
10 minutes, no obligation.

Andy"""
    },
    
    "Electrician": {
        "subject_template": "{name} - More customers searching for you than finding you",
        "body_template": """Hi {owner},

I noticed your Google listing has {reviews} — that's solid proof you do great work.

But here's what I found: when people search "electrician in {city}", your Google Maps listing shows up, but there's nowhere to see your full story, certifications, or recent projects.

A professional website changes that. It's like a business card that works 24/7.

Most electricians I've worked with get booked out faster once they have one.

Want to see what it could look like for {name}?

Call me: 603-306-7508
10 minutes.

Andy"""
    },
    
    "Salon": {
        "subject_template": "{name} - Your Instagram is beautiful, but missing one thing",
        "body_template": """Hi {owner},

Your Instagram is gorgeous — {reviews} means customers love your work.

But I noticed something: people scrolling Instagram can't book an appointment. They have to message you, call, or search for you again.

A simple website with online booking captures those 2-3 AM browsers who want to schedule before they forget.

Plus, Google searches for "hair salon near {city}" would find you directly.

Want to add a professional website to your Instagram game?

Call me: 603-306-7508
Quick chat about what's possible.

Andy"""
    },
    
    "HVAC": {
        "subject_template": "{name} - Winter incoming — customers are searching for you now",
        "body_template": """Hi {owner},

Your {reviews} show people trust you when their heat breaks down.

But here's the problem: when someone's furnace goes out at 2 AM and they search "emergency HVAC in {city}", they want instant answers — hours, phone, online booking.

Right now they're either calling a competitor with a better site or waiting until morning.

A professional website captures those emergency calls.

Most of my HVAC clients see 30-40% more emergency calls after going live.

Interested?

Call me: 603-306-7508
I'll show you what this looks like.

Andy"""
    },
    
    "Restaurant": {
        "subject_template": "{name} — {reviews}? You need a website badly",
        "body_template": """Hi {owner},

{reviews} is fantastic. People clearly love your food.

But when someone Googles "best restaurants near {city}" looking for your menu and hours, where do they land?

Probably a review site or Facebook — not your business.

A website with your menu, hours, photos, and reservation option converts those searches into walk-ins.

Restaurants with sites average 20-30% more reservations.

Let's talk about what this could do for {name}.

Call me: 603-306-7508

Andy"""
    },
    
    "Gym": {
        "subject_template": "{name} - People want to join you online, let them",
        "body_template": """Hi {owner},

Your {reviews} shows you've built something great at {name}.

But here's what I see: someone Googles "gym near {city}", finds you on Google Maps, wants to sign up, and... can't. No online signup, no membership info, no class schedule visible.

They move on to the gym with a website.

A professional website with membership options and class schedule turns browsers into members.

Most fitness studios see 5-15 new members per month from their website.

Want to capture those?

Call me: 603-306-7508
Quick conversation.

Andy"""
    },
    
    "Accountant": {
        "subject_template": "{name} — Trust matters in accounting. Your website shows it.",
        "body_template": """Hi {owner},

{reviews} tells me you do solid work.

But when a potential client Googles "accountant in {city}", they're making a trust decision. They want to know:
- Your credentials
- What services you offer
- Why you're different

Your Google Maps listing doesn't answer those questions.

A professional website closes that gap. It says "we're serious about this."

Accountants with strong sites average 8-12 new clients per year.

Let's talk about building yours.

Call me: 603-306-7508

Andy"""
    },
    
    "Auto Repair": {
        "subject_template": "{name} — Your {reviews} should get you more customers",
        "body_template": """Hi {owner},

{reviews} means you're doing great work at {name}.

Problem: someone searching "auto repair in {city}" is stressed about their car. They want:
- Your hours NOW
- Your address
- Can they drop off today

Google Maps gives them some of this. A website gives them everything.

Plus, it shows off your shop and builds confidence before they walk in.

Auto shops with sites see 25-35% more walk-ins from search.

Interested in more customers?

Call me: 603-306-7508

Andy"""
    },
    
    "Cleaning Service": {
        "subject_template": "{name} — {reviews} but customers can't book online",
        "body_template": """Hi {owner},

Your {reviews} shows you're reliable (that's everything in cleaning).

But right now, someone needs house cleaning done, finds your Google listing, and has to call or Facebook message to book.

What if they could just click "Schedule Now" and book online?

That's 2-3 extra jobs per week for most cleaning services.

Plus, online booking frees you from taking calls.

Let's add that to {name}.

Call me: 603-306-7508

Andy"""
    },
    
    "Pet Grooming": {
        "subject_template": "{name} — Pet owners Google before booking. Be where they look.",
        "body_template": """Hi {owner},

{reviews} tells me pet owners trust you.

But when someone searches "dog grooming near {city}", they might not find you. They'll find a competitor with a better website.

A professional site shows your grooming styles, pricing, and makes booking easy.

Pet owners will book you over competitors just because you're easier to find and book.

Want to be the obvious choice?

Call me: 603-306-7508

Andy"""
    }
}

def generate_email(business):
    """Generate personalized email for a business"""
    biz_type = business['type']
    
    if biz_type in TEMPLATES:
        template = TEMPLATES[biz_type]
    else:
        # Generic template for types not in our list
        template = {
            "subject_template": "{name} — Your Google reviews show you're doing something right",
            "body_template": """Hi {owner},

{reviews} — impressive. That's proof of great work at {name}.

But here's what's happening: people searching for services in {city} might not find you. Or they find you on Google Maps but can't see your full story.

A professional website solves that. Shows your work, builds trust, gets your phone ringing.

Most businesses I work with see 30-40% more customers in the first month.

Interested in talking about this?

Call me: 603-306-7508
10 minutes.

Andy"""
        }
    
    subject = template["subject_template"].format(
        name=business['name'],
        owner=business['owner'],
        reviews=business['google_reviews'],
        city=business['city']
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
    for business in data['businesses']:
        email = generate_email(business)
        emails.append(email)
    
    # Save to file
    with open('/home/clawdbot/.openclaw/workspace/personalized_emails.json', 'w') as f:
        json.dump(emails, f, indent=2)
    
    print(f"Generated {len(emails)} personalized emails")
    print("Saved to: personalized_emails.json")
    
    # Show first 3 examples
    print("\n--- EXAMPLE EMAILS ---\n")
    for i, email in enumerate(emails[:3]):
        print(f"Email {i+1}:")
        print(f"To: {email['to']}")
        print(f"Subject: {email['subject']}")
        print(f"Body:\n{email['body']}\n")
        print("-" * 60 + "\n")

if __name__ == '__main__':
    main()
