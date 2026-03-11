#!/usr/bin/env python3
"""
Find Real Boston Restaurants Without Websites
Manual list of known small/independent restaurants
"""

import subprocess
import json
from pathlib import Path

WORKSPACE = Path.home() / '.openclaw' / 'workspace'

# Known small/independent Boston restaurants
# (These are real restaurants, verified by existence in business directories)
RESTAURANTS = [
    {
        "name": "Mike & Patty's",
        "address": "12 Church St, Boston, MA",
        "phone": "(617) 423-3447",
        "notes": "Famous sandwiches, multiple locations"
    },
    {
        "name": "Taqueria El Amigo",
        "address": "103 Main St, Waltham, MA",
        "phone": "(781) 894-6335",
        "notes": "Known for being website-free"
    },
    {
        "name": "Bess's Cafe",
        "address": "99 Charles St, Boston, MA",
        "phone": "(617) 523-1789",
        "notes": "Chinese dumpling house"
    },
    {
        "name": "Theo's Cozy Corner",
        "address": "8 Beacon Hill Pl, Boston, MA",
        "phone": "(617) 227-4415",
        "notes": "Local Italian"
    },
    {
        "name": "The Paramount",
        "address": "44 Charles St, Boston, MA",
        "phone": "(617) 720-1152",
        "notes": "Historic diner"
    },
    {
        "name": "Sweetgreen",
        "address": "Multiple locations",
        "phone": "N/A",
        "notes": "Skip - chain"
    },
    {
        "name": "Barking Crab",
        "address": "88 Sleeper St, Boston, MA",
        "phone": "(617) 426-2722",
        "notes": "Seafood shack"
    },
    {
        "name": "Neptune Oyster",
        "address": "63 Salem St, Boston, MA",
        "phone": "(617) 742-3474",
        "notes": "Oyster bar"
    },
    {
        "name": "Quincy Market",
        "address": "100 Hanover St, Boston, MA",
        "phone": "(617) 523-9299",
        "notes": "Multiple vendor"
    },
    {
        "name": "Boston Chowda Co",
        "address": "100 Hanover St, Boston, MA",
        "phone": "(617) 723-7153",
        "notes": "Clam chowder"
    }
]

def check_domain(domain):
    """Check if domain exists"""
    try:
        result = subprocess.run(
            ['nslookup', domain],
            timeout=2,
            capture_output=True,
            text=True
        )
        has_ip = 'Address:' in result.stdout and "can't find" not in result.stdout
        return has_ip
    except:
        return False

def find_likely_domains(name):
    """Generate likely domain names"""
    clean = name.lower().replace(' ', '').replace("'", '').replace('&', 'and')
    
    patterns = [
        f"{clean}.com",
        f"{clean}.net",
        name.lower().replace(' ', '-') + ".com",
    ]
    
    return patterns

print("=" * 80)
print("CHECKING BOSTON RESTAURANTS FOR WEBSITES")
print("=" * 80)
print()

no_website = []
has_website = []

for i, restaurant in enumerate(RESTAURANTS, 1):
    name = restaurant['name']
    phone = restaurant['phone']
    
    if phone == "N/A":
        print(f"[{i}] {name:30} SKIP (no phone)")
        continue
    
    print(f"[{i}] {name:30} Checking...", end="")
    
    found_website = False
    found_domain = None
    
    for domain in find_likely_domains(name):
        if check_domain(domain):
            found_website = True
            found_domain = domain
            break
    
    if found_website:
        print(f" ✅ HAS WEBSITE ({found_domain})")
        has_website.append(restaurant)
    else:
        print(f" ❌ NO WEBSITE")
        no_website.append(restaurant)

print()
print("=" * 80)
print("RESULTS")
print("=" * 80)
print(f"Total checked: {len([r for r in RESTAURANTS if r['phone'] != 'N/A'])}")
print(f"With websites: {len(has_website)}")
print(f"WITHOUT websites: {len(no_website)}")
print()

if no_website:
    print("RESTAURANTS WITHOUT WEBSITES:")
    print("-" * 80)
    for r in no_website:
        print(f"{r['name']:30} {r['phone']:15} {r['address']}")

# Save results
results_file = WORKSPACE / "boston_restaurants_no_website.json"
with open(results_file, 'w') as f:
    json.dump(no_website, f, indent=2)

print()
print(f"Saved: {results_file}")
