#!/usr/bin/env python3
"""
Generate daily 15-business call batch from verified no-website list.
Rotates through all 18 businesses, repeating as needed.
"""

import json
from datetime import datetime

# All 18 verified businesses
ALL_BUSINESSES = [
    {"name": "Lower Roxbury Plumbing", "phone": "617-203-6199", "category": "Plumbing"},
    {"name": "Callahan Plumbing", "phone": "617-404-3689", "category": "Plumbing"},
    {"name": "Possick Plumbing, Heating & Cooling", "phone": "617-243-9999", "category": "Plumbing"},
    {"name": "Dice Licensed Electricians", "phone": "617-702-2888", "category": "Electrical"},
    {"name": "Licensed Electricians Jamaica Plain", "phone": "888-512-6801", "category": "Electrical"},
    {"name": "Dirty Water Dough Company", "phone": "617-262-0090", "category": "Restaurant"},
    {"name": "Parish Café", "phone": "617-247-4777", "category": "Restaurant"},
    {"name": "Yvonne's Restaurant", "phone": "617-267-0047", "category": "Restaurant"},
    {"name": "Summer Street Barber Shop", "phone": "617-345-9300", "category": "Barber/Salon"},
    {"name": "Skips Barbershop South Boston", "phone": "617-269-2227", "category": "Barber/Salon"},
    {"name": "Junior's iCuts", "phone": "617-250-8915", "category": "Barber/Salon"},
    {"name": "AGOSTINO SALON", "phone": "617-262-2029", "category": "Barber/Salon"},
    {"name": "Lapels Cleaners South End", "phone": "617-236-0098", "category": "Cleaners"},
    {"name": "Alpha Dogs Boston", "phone": "617-514-6745", "category": "Pet Grooming"},
    {"name": "LaChic Professional Pet Grooming", "phone": "617-242-0300", "category": "Pet Grooming"},
    {"name": "Pawsh Dog Boutique", "phone": "617-391-0880", "category": "Pet Grooming"},
    {"name": "The Modern Dog Boston", "phone": "617-481-5621", "category": "Pet Grooming"},
    {"name": "Paws & Purrfection Company", "phone": "857-261-7998", "category": "Pet Grooming"},
]

def generate_batch(day_offset=0):
    """Generate a batch of 15 businesses for the day."""
    # Cycle through all 18, getting 15 per day
    start_index = (day_offset * 15) % 18
    batch = []
    
    for i in range(15):
        idx = (start_index + i) % 18
        batch.append(ALL_BUSINESSES[idx])
    
    return batch

# Generate today's batch (day 0)
today_batch = generate_batch(0)

# Print formatted output
print("=" * 80)
print(f"CALL LIST - {datetime.now().strftime('%B %d, %Y').upper()}")
print("=" * 80)
print()

category_map = {}
for i, biz in enumerate(today_batch, 1):
    cat = biz["category"]
    if cat not in category_map:
        category_map[cat] = []
    category_map[cat].append((i, biz))

# Print by category
num = 1
for category in ["Plumbing", "Electrical", "Restaurant", "Barber/Salon", "Cleaners", "Pet Grooming"]:
    if category in category_map:
        print(f"{category.upper()} ({len(category_map[category])})")
        for idx, biz in category_map[category]:
            print(f"{idx:2d}. {biz['name']:<40} {biz['phone']:<15}")
        print()

print("=" * 80)
print("PITCH: 'Hi, is the owner available? This is Andy. I noticed you don't have'")
print("a website and we just built one for [similar business]. Interested in seeing")
print("a quick example? Takes 2 minutes.'")
print("=" * 80)
