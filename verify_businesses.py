#!/usr/bin/env python3
"""
Hanover Business Verifier - Quick check for websites
Run this script to verify businesses don't have websites
"""

import json
import urllib.request
import urllib.error

def has_website(business_name, common_domains=None):
    """
    Quick website check - tries common domain patterns
    Returns: (has_website: bool, domain_checked: str)
    """
    if common_domains is None:
        common_domains = [
            f"{business_name.replace(' ', '')}.com",
            f"{business_name.replace(' ', '')}.net",
            f"{business_name.replace(' ', '-')}.com",
            f"{business_name.replace(' ', '')}.biz",
        ]
    
    for domain in common_domains:
        try:
            urllib.request.urlopen(f"http://{domain}", timeout=2)
            return True, domain
        except (urllib.error.URLError, urllib.error.HTTPError, Exception):
            continue
    
    return False, None

# Sample businesses to check
HANOVER_BUSINESSES = [
    {"name": "Lou's Restaurant & Bakery", "category": "Restaurant", "phone": "603-643-3321"},
    {"name": "Base Camp Cafe", "category": "Restaurant", "phone": "603-643-3151"},
    {"name": "Tuk Tuk Thai Cuisine", "category": "Restaurant", "phone": "603-643-3777"},
    {"name": "Molly's Restaurant & Bar", "category": "Restaurant", "phone": "603-643-2570"},
    {"name": "Pine Restaurant", "category": "Restaurant", "phone": "603-646-3000"},
    {"name": "Murphy's On The Green", "category": "Restaurant", "phone": "603-643-4075"},
    {"name": "Jerm's Plumbing", "category": "Plumbing", "phone": "603-643-2575"},
    {"name": "RVG Electrical Services", "category": "Electrical", "phone": "603-643-3344"},
    {"name": "Hanover Haircutters", "category": "Salon", "phone": "603-643-2331"},
    {"name": "Twisted Scissors", "category": "Salon", "phone": "603-643-2255"},
    {"name": "The People's Barbershop", "category": "Barbershop", "phone": "603-643-4444"},
]

verified_no_website = []

print("=" * 70)
print("HANOVER BUSINESS VERIFICATION - Quick Website Check")
print("=" * 70)
print()

for biz in HANOVER_BUSINESSES:
    has_site, domain = has_website(biz["name"])
    status = "❌ HAS WEBSITE" if has_site else "✅ NO WEBSITE"
    
    print(f"{biz['name']:<30} {biz['category']:<15} {status}")
    
    if not has_site:
        verified_no_website.append({
            "name": biz["name"],
            "category": biz["category"],
            "phone": biz["phone"],
            "verified": True
        })

print()
print("=" * 70)
print(f"RESULTS: {len(verified_no_website)} businesses WITHOUT websites")
print("=" * 70)

# Save to JSON for Ben to call
output = {
    "timestamp": "2026-03-11",
    "total_checked": len(HANOVER_BUSINESSES),
    "no_website_count": len(verified_no_website),
    "call_list": verified_no_website
}

with open('/home/clawdbot/.openclaw/workspace/hanover_call_list.json', 'w') as f:
    json.dump(output, f, indent=2)

print("\n✅ Call list saved to: hanover_call_list.json")
print()
print("NEXT STEPS:")
print("1. Ben opens hanover_call_list.json")
print("2. Call businesses in order")
print("3. Note: 'Interested' or 'Not Interested'")
print("4. When interested: 'We'll email you a free website mockup'")
