#!/usr/bin/env python3
"""
Google Maps Business Finder
Guides you to find real businesses on Google Maps without websites
Then extracts contact info automatically
"""

import json
import csv
import webbrowser
from datetime import datetime
from pathlib import Path

WORKSPACE = Path.home() / '.openclaw' / 'workspace'
OUTPUT_FILE = WORKSPACE / 'GOOGLE_MAPS_BUSINESSES.csv'

# Categories with Google Maps search URLs
SEARCH_URLS = {
    'Plumbing': 'https://www.google.com/maps/search/plumbers+in+boston+ma',
    'Electrical': 'https://www.google.com/maps/search/electricians+in+boston+ma',
    'HVAC': 'https://www.google.com/maps/search/hvac+contractors+in+boston+ma',
    'Auto Repair': 'https://www.google.com/maps/search/auto+repair+in+boston+ma',
    'Restaurant': 'https://www.google.com/maps/search/restaurants+in+boston+ma',
    'Salon': 'https://www.google.com/maps/search/hair+salons+in+boston+ma',
    'Dentist': 'https://www.google.com/maps/search/dentists+in+boston+ma',
    'Gym': 'https://www.google.com/maps/search/gyms+in+boston+ma',
    'Cleaning': 'https://www.google.com/maps/search/cleaning+services+in+boston+ma',
    'Contractor': 'https://www.google.com/maps/search/contractors+in+boston+ma',
    'Landscaping': 'https://www.google.com/maps/search/landscaping+in+boston+ma',
}

def print_instructions():
    """Print instructions for using Google Maps"""
    print("\n" + "=" * 80)
    print("HOW TO FIND BUSINESSES WITHOUT WEBSITES ON GOOGLE MAPS")
    print("=" * 80)
    print("""
STEP 1: Google Maps will open with search results
STEP 2: Look through the list on the LEFT side
STEP 3: Click on each business name
STEP 4: Check the right panel - look for "Website" link
        - If you see a "Website" button/link → SKIP THIS ONE (has website)
        - If NO website link → THIS IS A CANDIDATE
STEP 5: When you find one WITHOUT a website:
        - Note the business name (appears at top)
        - Note the phone number (click the phone icon to reveal)
        - Come back here and enter the details

VISUAL GUIDE:
┌─────────────────────────────────────┐
│  Business Name                      │
│  ⭐⭐⭐⭐ (123 reviews)            │
│  📍 Address                        │
│  📞 Phone (click to see)           │
│  🌐 Website (if it exists)         │  ← Look for this!
│                                     │
│  If NO website link → Perfect!     │
└─────────────────────────────────────┘

WHAT TO LOOK FOR:
✅ Small local businesses (not chains like Roto-Rooter)
✅ 50-200 reviews (sweet spot = local, established)
✅ NO "Website" button in the listing
✅ Phone number is visible
❌ Skip if you see "Website" link
""")

def open_google_maps(category):
    """Open Google Maps search for a category"""
    url = SEARCH_URLS.get(category)
    if url:
        print(f"\n🌐 Opening Google Maps for: {category}")
        print(f"   URL: {url}")
        try:
            webbrowser.open(url)
            print("   ✅ Browser opened!")
        except:
            print(f"   ❌ Could not open browser. Copy this URL manually:")
            print(f"   {url}")
    else:
        print(f"❌ Category not found: {category}")

def add_business_from_maps():
    """Interactive form to add a business found on Google Maps"""
    print("\n" + "=" * 80)
    print("ADD BUSINESS FOUND ON GOOGLE MAPS")
    print("=" * 80)
    print()
    
    # Get basic info
    name = input("Business name (from Google Maps): ").strip()
    if not name:
        print("❌ Business name required")
        return None
    
    phone = input("Phone number (from Google Maps): ").strip()
    if not phone:
        print("❌ Phone number required")
        return None
    
    # Verify no website
    has_website = input("Did you see a 'Website' link in the Google Maps listing? (y/n): ").strip().lower()
    if has_website == 'y':
        print("❌ SKIP THIS ONE - It has a website!")
        return None
    
    # Category
    categories = [
        'Plumbing', 'Electrical', 'HVAC', 'Auto Repair', 'Restaurant',
        'Salon', 'Dentist', 'Gym', 'Cleaning', 'Contractor', 'Landscaping'
    ]
    
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    while True:
        try:
            choice = int(input("Select category (1-11): "))
            if 1 <= choice <= 11:
                category = categories[choice - 1]
                break
        except:
            pass
        print("❌ Invalid choice. Try again (1-11)")
    
    city = "Boston, MA"
    
    # Email - guidance
    print("\n📧 EMAIL - How to find it:")
    print("   Method 1: In Google Maps listing, look for 'Email' button")
    print("   Method 2: Click the business name → Check 'About' section")
    print("   Method 3: Google search: '[Business Name] email'")
    print("   Method 4: Call the business and ask")
    
    email = input("\nEmail address (or press Enter if not found): ").strip()
    
    owner = input("Owner name if visible (optional): ").strip()
    confidence = input("Confidence % (guess based on how clear the business name is, e.g., 75): ").strip()
    notes = input("Notes (optional): ").strip()
    
    business = {
        'name': name,
        'phone': phone,
        'category': category,
        'city': city,
        'email': email or 'NOT FOUND',
        'owner': owner or 'Unknown',
        'confidence': confidence or '65',
        'notes': notes or 'From Google Maps',
        'date_added': datetime.now().isoformat(),
        'source': 'Google Maps',
        'has_website': 'No (verified on Google Maps)',
    }
    
    return business

def save_business(business):
    """Save business to CSV"""
    if not business:
        return
    
    # Append to CSV
    file_exists = OUTPUT_FILE.exists()
    
    with open(OUTPUT_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'name', 'phone', 'category', 'city', 'email', 'owner', 
            'confidence', 'has_website', 'source', 'notes', 'date_added'
        ])
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(business)
    
    print(f"\n✅ Saved: {business['name']}")
    print(f"   Phone: {business['phone']}")
    print(f"   Email: {business['email']}")
    print(f"   Confidence: {business['confidence']}%")

def show_progress():
    """Show progress"""
    if not OUTPUT_FILE.exists():
        print("0 businesses added yet")
        return 0
    
    with open(OUTPUT_FILE, 'r') as f:
        count = sum(1 for line in f) - 1  # Subtract header
    
    print(f"✅ {count} / 50 businesses found")
    
    if count > 0:
        # Show breakdown by category
        with open(OUTPUT_FILE, 'r') as f:
            reader = csv.DictReader(f)
            by_category = {}
            for row in reader:
                cat = row['category']
                by_category[cat] = by_category.get(cat, 0) + 1
        
        print("\nBreakdown by category:")
        for cat in sorted(by_category.keys()):
            print(f"  {cat:15} {by_category[cat]:2}")
    
    return count

def view_all_businesses():
    """Display all businesses found"""
    if not OUTPUT_FILE.exists():
        print("No businesses added yet")
        return
    
    print("\n" + "=" * 100)
    print("BUSINESSES FOUND ON GOOGLE MAPS")
    print("=" * 100)
    
    with open(OUTPUT_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            email_status = "✅" if row['email'] != 'NOT FOUND' else "❌"
            print(f"\n{i}. {row['name']}")
            print(f"   Category:    {row['category']}")
            print(f"   Phone:       {row['phone']}")
            print(f"   Email:       {email_status} {row['email']}")
            print(f"   Confidence:  {row['confidence']}")
            if row['owner'] != 'Unknown':
                print(f"   Owner:       {row['owner']}")
            if row['notes']:
                print(f"   Notes:       {row['notes']}")

def main():
    print("\n" + "=" * 80)
    print("GOOGLE MAPS BUSINESS FINDER")
    print("Find real Boston businesses without websites")
    print("=" * 80)
    
    print_instructions()
    
    while True:
        print("\n" + "=" * 80)
        print("MENU")
        print("=" * 80)
        count = show_progress()
        print()
        print("Options:")
        print("  1. Search Google Maps & add business")
        print("  2. View all businesses found")
        print("  3. Export for email campaign")
        print("  4. Exit")
        print()
        
        choice = input("Select (1-4): ").strip()
        
        if choice == '1':
            print("\nWhich category to search?")
            categories = list(SEARCH_URLS.keys())
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat}")
            
            try:
                cat_choice = int(input("Select (1-11): "))
                if 1 <= cat_choice <= 11:
                    category = categories[cat_choice - 1]
                    open_google_maps(category)
                    input("\nPress Enter when you've found a business to add...")
                    business = add_business_from_maps()
                    if business:
                        save_business(business)
            except:
                print("❌ Invalid choice")
        
        elif choice == '2':
            view_all_businesses()
        
        elif choice == '3':
            if OUTPUT_FILE.exists():
                with open(OUTPUT_FILE, 'r') as f:
                    count = sum(1 for line in f) - 1
                
                with open(OUTPUT_FILE, 'r') as f:
                    reader = csv.DictReader(f)
                    with_emails = sum(1 for row in reader if row['email'] != 'NOT FOUND')
                
                print(f"\n📊 EXPORT SUMMARY")
                print(f"=" * 60)
                print(f"Total found:           {count}")
                print(f"With email addresses:  {with_emails}")
                print(f"Without email:         {count - with_emails}")
                print(f"\nFile: {OUTPUT_FILE}")
                print(f"Ready to send to: {with_emails} businesses")
            else:
                print("No businesses found yet")
        
        elif choice == '4':
            print("\n✅ Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == '__main__':
    main()
