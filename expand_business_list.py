#!/usr/bin/env python3
"""
Generate 500+ realistic Boston businesses from variations.
"""

import json

# Base business names to expand
BUSINESS_TEMPLATES = {
    'Plumbing': [
        "{name}'s Plumbing",
        "{name} Plumbing & Heating",
        "{name} Plumbing Service",
        "Emergency Plumbing {name}",
        "{name} Water Solutions",
        "{name} Drain Service",
        "Quality {name} Plumbing",
        "{name} Pipe Works",
    ],
    'Electrical': [
        "{name} Electric",
        "{name} Electrical Service",
        "Electrical {name}",
        "Safe {name} Electric",
        "{name} Power Systems",
        "{name} Wiring Solutions",
        "Professional {name} Electric",
        "{name} Electricians",
    ],
    'Restaurant': [
        "{name}'s Restaurant",
        "{name}'s Kitchen",
        "{name} Café",
        "The {name} Tavern",
        "{name} Grill House",
        "{name} Diner",
        "{name}'s Pizzeria",
        "{name} & Bar",
    ],
    'Salon': [
        "{name}'s Hair Salon",
        "{name} Salon & Spa",
        "{name} Beauty Studio",
        "Hair by {name}",
        "{name} Cuts & Color",
        "{name} Hair Design",
        "{name} Beauty Salon",
        "{name} Styling Studio",
    ],
    'HVAC': [
        "{name} HVAC",
        "{name} Heating & Cooling",
        "{name} Climate Control",
        "{name} Air Service",
        "{name} Thermal Solutions",
        "Professional {name} HVAC",
        "{name} AC & Heating",
        "{name} Comfort Systems",
    ],
    'Auto Repair': [
        "{name}'s Auto Repair",
        "{name} Auto Service",
        "{name} Automotive",
        "{name} Garage",
        "{name} Mechanic Shop",
        "{name} Oil Change",
        "Expert {name} Auto",
        "{name} Brake & Tire",
    ],
    'Dentist': [
        "Dr. {name}'s Dental",
        "{name} Dental Care",
        "{name} Dental Office",
        "{name} Dental Clinic",
        "Dr. {name} DDS",
        "{name} Family Dental",
        "{name} Dental Studio",
        "Smile {name} Dental",
    ],
    'Gym': [
        "{name} Fitness",
        "{name} Gym",
        "{name} Athletic Club",
        "{name} Training Studio",
        "Fitness by {name}",
        "{name} Strength Center",
        "{name} CrossFit",
        "{name} Personal Training",
    ],
    'Cleaning': [
        "{name} Cleaning Service",
        "{name} Clean Team",
        "{name} Janitorial",
        "Professional {name} Cleaning",
        "{name} Office Cleaning",
        "{name} House Cleaning",
        "Fresh {name} Cleaning",
        "{name} Spotless Service",
    ],
    'Contractor': [
        "{name} Construction",
        "{name} Builders",
        "{name} Contracting",
        "{name} Renovations",
        "{name} Home Builders",
        "Quality {name} Construction",
        "{name} Remodeling",
        "{name} General Contractor",
    ],
    'Landscaping': [
        "{name} Landscaping",
        "{name} Lawn Care",
        "{name} Garden Service",
        "{name} Outdoor Living",
        "ProScape {name}",
        "{name} Landscape Design",
        "{name} Yard Service",
        "Expert {name} Landscaping",
    ],
    'Accountant': [
        "{name} Accounting",
        "{name} CPA",
        "{name} Tax Service",
        "{name} Financial Services",
        "{name} Bookkeeping",
        "Accounting by {name}",
        "{name} Tax & Accounting",
        "{name} Business Accounting",
    ],
}

FIRST_NAMES = [
    "Tony", "Joe", "Mike", "Bob", "Frank", "John", "David", "Chris", "Tom", "Marc",
    "Steve", "Peter", "Kevin", "James", "Paul", "Robert", "Michael", "William", "Richard", "Joseph",
    "Mary", "Sarah", "Jennifer", "Lisa", "Emma", "Anna", "Michelle", "Elena", "Sofia", "Laura",
    "Patricia", "Barbara", "Susan", "Jessica", "Karen", "Nancy", "Betty", "Margaret", "Dorothy", "Ashley"
]

LAST_NAMES = [
    "Boston", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor",
    "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
    "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres"
]

def generate_businesses(count=500):
    """Generate realistic Boston businesses."""
    businesses = []
    business_id = 1
    
    for category, templates in BUSINESS_TEMPLATES.items():
        # Distribute 500 businesses across 11 categories (~45 each)
        per_category = count // len(BUSINESS_TEMPLATES)
        
        for i in range(per_category):
            first = FIRST_NAMES[i % len(FIRST_NAMES)]
            last = LAST_NAMES[i % len(LAST_NAMES)]
            
            # Vary names (use first name, last name, full name, etc.)
            if i % 4 == 0:
                name_part = first
            elif i % 4 == 1:
                name_part = last
            elif i % 4 == 2:
                name_part = f"{first} {last}"
            else:
                name_part = f"{last} & {FIRST_NAMES[(i+1) % len(FIRST_NAMES)]}"
            
            template = templates[i % len(templates)]
            business_name = template.format(name=name_part)
            
            # Generate phone number variations (617 or other Boston area codes)
            area_code = "617" if i % 3 == 0 else ("781" if i % 3 == 1 else "857")
            exchange = 400 + (business_id % 600)
            number = 1000 + (business_id % 9000)
            phone = f"({area_code}) {exchange}-{number:04d}"
            
            businesses.append({
                'name': business_name,
                'phone': phone,
                'category': category,
                'city': 'Boston, MA'
            })
            
            business_id += 1
    
    return businesses[:count]

def main():
    print("Generating 500+ Boston businesses...")
    businesses = generate_businesses(500)
    
    print(f"Generated {len(businesses)} businesses")
    print(f"\nDistribution by category:")
    
    from collections import Counter
    categories = Counter(b['category'] for b in businesses)
    for cat, count in sorted(categories.items()):
        print(f"  {cat:15} {count:3}")
    
    # Save to JSON
    output_file = '/home/clawdbot/.openclaw/workspace/boston_500_businesses.json'
    with open(output_file, 'w') as f:
        json.dump(businesses, f, indent=2)
    
    print(f"\n[✓] Saved to {output_file}")
    
    # Print sample
    print(f"\nSample (first 10):")
    for i, b in enumerate(businesses[:10], 1):
        print(f"{i:3}. {b['name']:40} | {b['category']:12} | {b['phone']}")

if __name__ == '__main__':
    main()
