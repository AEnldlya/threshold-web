#!/usr/bin/env python3
"""
Generate professional, official business emails
"""

import json

# Professional email templates
TEMPLATES = {
    "Plumber": {
        "subject_template": "Professional Website Development - {name}",
        "body_template": """Dear {owner},

I am reaching out regarding professional website development services for {name}.

I have reviewed your business profile and noticed that while you maintain a strong reputation with {reviews} on Google, you currently do not have a dedicated website. This represents a significant opportunity for growth.

I specialize in developing professional websites for service-based businesses. A properly designed website will:

- Increase your online visibility and search rankings
- Provide potential customers with essential business information
- Generate additional service inquiries and appointments
- Establish professional credibility

I offer a streamlined development process with a 3-day timeline and transparent pricing. I would be pleased to discuss how a professional website could benefit {name}.

If you would like to explore this opportunity, please feel free to reach out.

Best regards,
Andy"""
    },
    
    "Salon": {
        "subject_template": "Website Development for {name}",
        "body_template": """Dear {owner},

I am contacting you regarding professional website development for {name}.

With {reviews} on Google and strong social media presence, your business has demonstrated significant market success. A professional website would complement these efforts and provide clients with a centralized booking platform.

My services include:

- Professional website design and development
- Online appointment booking system
- Mobile-responsive design
- SEO optimization

The typical timeline is 3 days with all-inclusive pricing. I would welcome the opportunity to discuss how this could enhance {name}'s online presence.

Please let me know if you would like to explore this further.

Best regards,
Andy"""
    },
    
    "Restaurant": {
        "subject_template": "Website Development Services - {name}",
        "body_template": """Dear {owner},

I am writing to introduce professional website development services tailored for restaurants.

{name} has established an excellent reputation with {reviews}. However, customers seeking your business online are unable to view your menu, hours, or make reservations through a dedicated website.

I develop professional restaurant websites that include:

- Digital menu display
- Operating hours and location information
- Online reservation system
- Photo gallery of signature dishes

Development timeline: 3 days
Investment: $500

I would be glad to discuss how a professional website could drive additional business for {name}.

Best regards,
Andy"""
    },
    
    "Electrician": {
        "subject_template": "Professional Website Services - {name}",
        "body_template": """Dear {owner},

I am reaching out to discuss professional website development for {name}.

Your business has established strong credibility with {reviews} on Google. A professional website would further strengthen your market position by:

- Showcasing your work and certifications
- Providing 24/7 customer access to business information
- Generating service inquiries from online searches
- Building trust through professional presentation

I specialize in developing professional websites for service contractors. Services include:

- Professional design and development
- Mobile optimization
- Service portfolio display
- Customer testimonial integration

Timeline: 3 business days
Investment: $500

I would welcome discussing this opportunity with you.

Best regards,
Andy"""
    },
    
    "HVAC": {
        "subject_template": "Website Development for HVAC Services - {name}",
        "body_template": """Dear {owner},

I am contacting you regarding professional website development for {name}.

Your business maintains {reviews} on Google, demonstrating consistent customer satisfaction. A professional website would enhance your market visibility and customer acquisition strategy.

Website benefits for HVAC contractors:

- Increased visibility in local search results
- Online service request capabilities
- 24/7 availability for customer inquiries
- Professional credibility enhancement

I provide complete website development with a 3-day timeline and transparent pricing of $500.

I would be pleased to discuss how this service could benefit {name}.

Best regards,
Andy"""
    },
    
    "Gym": {
        "subject_template": "Website Development for Fitness Facilities - {name}",
        "body_template": """Dear {owner},

I am writing regarding professional website development services for {name}.

With {reviews} on Google, your facility has established strong market presence. A professional website would enable:

- Online membership enrollment
- Class schedule and pricing information
- Facility tour and amenities showcase
- Increased lead generation from online searches

I specialize in fitness industry website development. Standard features include:

- Professional design
- Online registration system
- Mobile responsiveness
- Search engine optimization

Timeline: 3 days
Investment: $500

I would welcome the opportunity to discuss this with you.

Best regards,
Andy"""
    },
    
    "Accountant": {
        "subject_template": "Professional Website Development - {name}",
        "body_template": """Dear {owner},

I am reaching out to discuss professional website development for {name}.

In the accounting industry, a professional online presence is essential for client acquisition and credibility. While your business maintains {reviews} on Google, a dedicated website would:

- Establish professional credibility
- Provide service descriptions and expertise information
- Enable client inquiries and consultations
- Improve search visibility

I develop professional websites specifically for accounting and tax services, including:

- Service overview and pricing
- Team credentials and background
- Client testimonials
- Contact and appointment request capabilities

Timeline: 3 business days
Investment: $500

I would be glad to discuss how this could benefit {name}.

Best regards,
Andy"""
    },
    
    "Auto Repair": {
        "subject_template": "Website Development - {name} Auto Services",
        "body_template": """Dear {owner},

I am contacting you regarding professional website development for {name}.

Your business has earned {reviews} on Google, indicating strong customer satisfaction. A professional website would further enhance your market position by:

- Showcasing your work and service expertise
- Providing repair and maintenance information
- Enabling online service appointment booking
- Improving search visibility for local customers

Website services include:

- Professional design and development
- Service portfolio and pricing display
- Online appointment scheduling
- Mobile optimization

Timeline: 3 business days
Investment: $500

I would welcome discussing this opportunity.

Best regards,
Andy"""
    },

    "Cleaning Service": {
        "subject_template": "Website Development for Cleaning Services - {name}",
        "body_template": """Dear {owner},

I am writing to introduce professional website development services for {name}.

Your business maintains {reviews} on Google, demonstrating consistent customer satisfaction. A professional website would enable clients to:

- View available cleaning services and pricing
- Schedule appointments online
- Access service areas and availability
- Request quotations electronically

Website features:

- Professional design
- Online booking system
- Service descriptions and pricing
- Mobile-responsive design

Timeline: 3 business days
Investment: $500

I would be pleased to discuss this further.

Best regards,
Andy"""
    },

    "Pet Grooming": {
        "subject_template": "Website Development - {name} Pet Services",
        "body_template": """Dear {owner},

I am reaching out regarding professional website development for {name}.

With {reviews} on Google, your grooming services have established strong reputation. A professional website would:

- Display grooming services and pricing
- Enable online appointment booking
- Showcase before and after photos
- Improve visibility in local searches

Services provided:

- Professional web design
- Online appointment scheduling
- Service portfolio display
- Mobile optimization

Timeline: 3 business days
Investment: $500

I would welcome the opportunity to assist {name}.

Best regards,
Andy"""
    },

    "Dentist": {
        "subject_template": "Professional Website Development - {name} Dental",
        "body_template": """Dear {owner},

I am contacting you regarding professional website development for {name}.

Your practice has earned {reviews} on Google. A professional website is essential for dental practices to:

- Display practice information and credentials
- Enable online appointment scheduling
- Showcase team members and specialties
- Improve patient acquisition through search visibility

Website includes:

- Professional design
- Appointment booking system
- Service descriptions
- Patient testimonials
- Mobile responsiveness

Timeline: 3 business days
Investment: $500

I would be glad to discuss this with you.

Best regards,
Andy"""
    },

    "Contractor": {
        "subject_template": "Website Development Services - {name}",
        "body_template": """Dear {owner},

I am writing to discuss professional website development for {name}.

Your business maintains {reviews} on Google, reflecting strong customer satisfaction. A professional website would:

- Display your project portfolio and expertise
- Provide service descriptions and pricing
- Generate leads from online searches
- Establish professional credibility

Construction and contracting websites include:

- Project portfolio and case studies
- Service information
- Licensing and credentials display
- Client testimonials
- Contact and quote request capabilities

Timeline: 3 business days
Investment: $500

I would welcome discussing this opportunity.

Best regards,
Andy"""
    }
}

def generate_email(business):
    """Generate professional email"""
    biz_type = business['type']
    
    if biz_type in TEMPLATES:
        template = TEMPLATES[biz_type]
    else:
        template = {
            "subject_template": "Professional Website Development - {name}",
            "body_template": """Dear {owner},

I am reaching out regarding professional website development services for {name}.

Your business has established strong market presence with {reviews} on Google. A professional website would enhance your online visibility and customer acquisition capabilities.

I specialize in developing professional websites for local businesses, including:

- Professional design and development
- Mobile optimization
- Search engine visibility
- Online customer engagement features

Timeline: 3 business days
Investment: $500

I would be pleased to discuss how this service could benefit {name}.

Best regards,
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
        
        if email_addr in seen_emails:
            continue
        
        seen_emails.add(email_addr)
        email = generate_email(business)
        emails.append(email)
    
    # Save to file
    with open('/home/clawdbot/.openclaw/workspace/personalized_emails.json', 'w') as f:
        json.dump(emails, f, indent=2)
    
    print(f"✓ Generated {len(emails)} professional emails")
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
