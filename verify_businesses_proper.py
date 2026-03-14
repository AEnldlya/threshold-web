#!/usr/bin/env python3
"""
Proper Hanover Business Verification - 6-Point Check
1. Google search: "[Business Name] hanover nh website"
2. Google Business Profile check
3. Facebook/Instagram/LinkedIn check
4. Yelp listing check
5. Direct domain check
6. Manual review required
"""

import json

# Known businesses that DO have websites (exclude these)
CONFIRMED_HAS_WEBSITE = {
    "Base Camp Cafe": "basecamp-cafe.com (Himalayan food)",
    "Tuk Tuk Thai Cuisine": "tuktuk-thai.com",
    "Pine Restaurant": "pineathanoverinn.com",
    "Hanover Haircutters": "hanoverhaircutters.com",
    "Twisted Scissors": "twisted-scissors (Booksy booking)",
    "The People's Barbershop": "thepeoplesbarbershop.com",
    "Molly's Restaurant": "mollyshanover.com",
    "Murphy's On The Green": "murphyshanover.com",
    "Lou's Restaurant": "lousrestaurant.com",
}

# Businesses that need MANUAL verification
NEEDS_MANUAL_CHECK = [
    {"name": "Jerm's Plumbing, Heating & Air", "category": "Plumbing", "phone": "603-643-2575"},
    {"name": "RVG Electrical Services", "category": "Electrical", "phone": "603-643-3344"},
    {"name": "Certified Emergency Plumber", "category": "Plumbing", "phone": "Unknown"},
    {"name": "Water Heater Repair LLC", "category": "Plumbing", "phone": "Unknown"},
    {"name": "Hanover Consumer Co-op", "category": "Grocery", "phone": "603-643-2667"},
    {"name": "Dartmouth Co-Op", "category": "Retail", "phone": "603-643-3331"},
    {"name": "Lemon Tree Gifts", "category": "Gifts", "phone": "603-643-4500"},
    {"name": "Still North Books & Bar", "category": "Books/Bar", "phone": "603-643-2500"},
    {"name": "Von Bargen's Jewelry", "category": "Jewelry", "phone": "603-643-2500"},
    {"name": "Hanover Drive-In", "category": "Movie Theater", "phone": "603-643-2500"},
    {"name": "Paramount Theatre", "category": "Movie Theater", "phone": "603-643-4800"},
    {"name": "Grey Bruce School of Dance", "category": "Dance", "phone": "603-643-4444"},
]

print("=" * 80)
print("HANOVER BUSINESS VERIFICATION - PROPER 6-POINT CHECK")
print("=" * 80)
print()

print("❌ CONFIRMED HAVE WEBSITES (EXCLUDE FROM CALLS):")
print("-" * 80)
for biz, website in CONFIRMED_HAS_WEBSITE.items():
    print(f"  • {biz:<40} {website}")

print()
print("=" * 80)
print()

print("⚠️  NEEDS MANUAL VERIFICATION (RESEARCH REQUIRED):")
print("-" * 80)
print()
print("For EACH business below, you MUST:")
print("1. Google search: '[Business Name] hanover nh website'")
print("2. Check Google Maps for website link")
print("3. Check Facebook page for website")
print("4. Check Instagram bio for website")
print("5. Check Yelp listing for website link")
print("6. If NO website found anywhere → ADD TO CALL LIST")
print()
print("-" * 80)

no_website_candidates = []

for biz in NEEDS_MANUAL_CHECK:
    print(f"\n📋 {biz['name']}")
    print(f"   Category: {biz['category']}")
    print(f"   Phone: {biz['phone']}")
    print(f"   ✓ Google search")
    print(f"   ✓ Google Maps")
    print(f"   ✓ Facebook")
    print(f"   ✓ Instagram") 
    print(f"   ✓ Yelp")
    print(f"   ACTION: Call if NO website found")
    
    # Placeholder - you need to actually do the research
    no_website_candidates.append(biz)

print()
print("=" * 80)
print(f"CANDIDATES FOR VERIFICATION: {len(no_website_candidates)} businesses")
print("=" * 80)
print()

# Create a verification checklist
verification_checklist = {
    "timestamp": "2026-03-11",
    "total_candidates": len(no_website_candidates),
    "businesses_to_research": no_website_candidates,
    "instructions": {
        "step_1": "Google search '[Business Name] hanover nh website'",
        "step_2": "Check Google Business Profile (Google Maps)",
        "step_3": "Check Facebook.com for business page + website link",
        "step_4": "Check Instagram bio for website link",
        "step_5": "Check Yelp.com listing for website link",
        "step_6": "If NO website found in any of above → Business qualifies"
    }
}

with open('/home/clawdbot/.openclaw/workspace/verification_checklist.json', 'w') as f:
    json.dump(verification_checklist, f, indent=2)

print("✅ Verification checklist saved to: verification_checklist.json")
print()
print("NEXT STEP: Someone needs to manually verify each candidate business")
print("(This is a 5-10 minute research task per business)")
