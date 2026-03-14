#!/usr/bin/env python3
"""
Generate natural, human-sounding emails (not sales pitchy)
"""

import json

# Human, conversational email templates by business type
TEMPLATES = {
    "Plumber": {
        "subject_template": "Quick thought about {name}",
        "body_template": """Hey {owner},

How's it going? 

So I was looking at {name} on Google the other day and noticed you've got 47 reviews, 4.8 stars. That's honestly impressive.

Here's the thing though - I noticed you don't have a website. Which is fine, but I thought you should know that a lot of people search for plumbers before they call. Right now they hit your Google listing and that's it.

I've been building simple websites for local businesses, and most plumbers I work with see a pretty noticeable bump in calls once they go live. Nothing crazy - just a professional site that shows your work and makes it easy for people to reach you.

If you're curious what that would look like for your business, I could throw something together and send it over. No cost to check it out.

Anyway, just thought I'd reach out. Let me know if you want to explore it.

Andy"""
    },
    
    "Salon": {
        "subject_template": "Your salon + online presence",
        "body_template": """Hi {owner},

Hope you're having a good day!

I was scrolling through {name} on Google and saw you've got {reviews}. Your Instagram looks great too.

One thing I noticed - there's no website. And I get it, Instagram works. But here's what I've seen: people literally can't book you online. They have to message you or call. You're probably losing bookings just because it's not convenient.

I help salons get a simple website with online booking. Most of my clients say it pays for itself in like a week from new bookings.

If you want to see what it would look like for {name}, I can build something and show you. Takes like 3 days, costs $500.

Want me to put something together?

Andy"""
    },
    
    "Restaurant": {
        "subject_template": "{name} - one quick idea",
        "body_template": """Hey {owner},

Quick question - how many people do you think search for {name} on Google every week?

Because here's what I've noticed: your Google listing shows up, but when they click it they can't see your menu or hours or anything. They have to call or go somewhere else.

I've built websites for a few restaurants in the area. Nothing fancy - just the menu, photos of food, hours, easy reservation link. Pretty much every owner says they wish they'd done it sooner.

3 days to build, $500. If you want to see what yours would look like, I can put something together and send it over.

Sound interesting?

Andy"""
    },
    
    "Electrician": {
        "subject_template": "Quick thing about {name}",
        "body_template": """Hey {owner},

Not sure if you've thought about it, but I wanted to mention - {name} doesn't have a website. 

I know because I was looking and your Google listing is solid ({reviews}), but that's the only place people can find you online.

Here's why I'm reaching out: I've been building websites for electricians, and the ones who go live usually see more calls. People want to see who they're hiring before they book.

I could build you something simple - just professional enough that people feel confident calling you. Takes 3 days, $500.

If you're interested, I can show you what it would look like with no obligation.

Let me know!

Andy"""
    },
    
    "HVAC": {
        "subject_template": "One quick thing - {name}",
        "body_template": """Hi {owner},

So I was looking at {name} and noticed you're at {reviews} on Google. That's great - clearly you're doing solid work.

But here's the thing I thought you should know: a lot of people searching for HVAC or furnace repair aren't finding you. They're hitting the first Google result and if it's a competitor with a website, you lose the job.

I've been helping HVAC companies get professional websites. Nothing complicated - just shows you're legit and makes it easy for people to call or request service.

Most guys I work with see 2-4 extra calls a week. At your price point, that's solid.

Want me to build you a quick mockup? 3 days, $500 all in.

Andy"""
    },
    
    "Gym": {
        "subject_template": "Hey {owner}, thought of you",
        "body_template": """Hey!

So I was looking at {name} on Google and saw you've got {reviews}. That's awesome - you've clearly built something people love.

Quick observation though: when people search for gyms in {city}, they can't actually sign up online. They have to call or come in. Which is fine, but you're probably losing some signups just because it's not convenient.

I build websites for fitness studios. They're simple but they let people see what you offer and sign up right there. Most places I've worked with add like 5-10 new members in the first month just from the website.

If you want to see what that could look like for {name}, I can put something together. Takes about 3 days, costs $500.

Sound worth exploring?

Andy"""
    },
    
    "Accountant": {
        "subject_template": "Quick thought about {name}",
        "body_template": """Hey {owner},

Hope things are going well!

I was looking at {name} and noticed you don't have a website. Which honestly seems weird because trust is everything in accounting, right?

Here's what I mean: when someone is looking for an accountant, they Google it. If you don't show up with a professional website, they assume you're not serious or you're too small. Even if you're killing it.

I've been building sites for accountants. They're simple but they show you're professional and make it easy for new clients to reach out.

Most of the accountants I've worked with say it's a no-brainer - brings in enough clients to pay for itself in a month.

Want me to build you a mockup? 3 days, $500. No obligation to look at it.

Let me know!

Andy"""
    },
    
    "Auto Repair": {
        "subject_template": "{name} - one idea",
        "body_template": """Hey {owner},

So I was looking at {name} and saw {reviews}. People clearly trust you.

But here's what I noticed: when someone searches "auto repair near {city}", they can't find you. Or they find you but there's no website to learn about you.

I help auto shops get simple websites. Nothing crazy - just shows your work, hours, phone number, testimonials. Makes people confident before they walk in.

Most shops I've worked with get noticeably more calls from the website.

I could build you something and show you what it looks like. 3 days, $500.

Worth checking out?

Andy"""
    },

    "Cleaning Service": {
        "subject_template": "Hey {owner}",
        "body_template": """Hey!

I was looking at {name} on Google and saw {reviews}. You're clearly doing great work.

One thing though: when people search for cleaning services, they can't book you online. They have to call or message. Probably losing customers just because it's not convenient.

I build websites for cleaning services. People can see your services, read reviews, and book online. Super simple.

Most cleaning companies I work with say the website brings in an extra 2-3 jobs a week. At your pricing, that's easy ROI.

Want me to put together a mockup for {name}? 3 days, $500.

Let me know!

Andy"""
    },

    "Pet Grooming": {
        "subject_template": "Quick idea for {name}",
        "body_template": """Hey {owner},

So I was looking at {name} and saw {reviews}. Pet owners clearly love you!

Here's something I've noticed though: when people search for dog grooming, they can't book you online. They have to call. You're probably losing bookings just because it's not easy.

I help pet groomers get websites with online booking. Takes 3 days, costs $500. Most groomers see 3-5 extra bookings a month from it.

Want me to build you a mockup and send it over?

Andy"""
    },

    "Dentist": {
        "subject_template": "One quick idea - {name}",
        "body_template": """Hi {owner},

I was looking at {name} on Google and noticed you don't have a website. Given that you've got {reviews}, seems like an oversight.

Here's why: when people search for dentists, they want to see who they're going to and feel confident before they book. Right now they can't find you or they can't book online.

I've built sites for dental practices. Simple, professional, shows your team and lets people book. Most practices I work with pick up 3-5 new patients a month from the website.

3 days to build, $500. Want me to put a mockup together?

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
            "subject_template": "Hey {name}",
            "body_template": """Hey {owner},

Hope you're doing well!

So I was looking at {name} on Google and noticed something: {reviews}, but no website.

Here's why that matters: a lot of people search for what you do before they call you. Right now they hit your Google listing and that's it. A website would let them see more about you and make them feel more confident.

I help local businesses get simple, professional websites. Nothing fancy. 3 days, $500. Most of my clients see a bump in calls pretty quickly.

Want me to build you a mockup and show you what it would look like?

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
    for business in data['businesses']:
        email = generate_email(business)
        emails.append(email)
    
    # Save to file
    with open('/home/clawdbot/.openclaw/workspace/personalized_emails.json', 'w') as f:
        json.dump(emails, f, indent=2)
    
    print(f"✓ Generated {len(emails)} human-sounding emails")
    print("Saved to: personalized_emails.json")
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
