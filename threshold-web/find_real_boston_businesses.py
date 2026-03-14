#!/usr/bin/env python3
"""
Find Real Boston Businesses Without Websites
Interactive research tool to manually verify + collect contact info
"""

import json
import csv
import subprocess
from datetime import datetime
from pathlib import Path

WORKSPACE = Path.home() / '.openclaw' / 'workspace'
OUTPUT_FILE = WORKSPACE / 'REAL_BOSTON_BUSINESSES_VERIFIED.csv'
JSON_FILE = WORKSPACE / 'real_boston_research.json'

def check_website_exists(business_name, domain_hint=None):
    """
    Check if a domain exists using nslookup
    domain_hint: optional domain to try first
    """
    domains_to_try = []
    
    if domain_hint:
        domains_to_try.append(domain_hint)
    
    # Generate patterns from business name
    clean = business_name.lower().replace(' ', '').replace("'", "")
    domains_to_try.extend([
        f"{clean}.com",
        f"{clean}.net",
        business_name.lower().replace(' ', '-') + ".com",
        business_name.lower().replace(' ', '-') + ".net",
    ])
    
    for domain in domains_to_try:
        try:
            result = subprocess.run(
                ['nslookup', domain],
                timeout=1,
                capture_output=True,
                text=True
            )
            if 'Address:' in result.stdout and "can't find" not in result.stdout:
                return True, domain
        except:
            pass
    
    return False, None

def search_email(business_name, category):
    """
    Provide guidance on finding email for a business
    """
    print("\n📧 EMAIL SEARCH GUIDANCE:")
    print("=" * 60)
    print(f"Business: {business_name}")
    print(f"Category: {category}")
    print()
    print("Try these sources (in order):")
    print("1. Business website (Contact page)")
    print("2. Google search: '[Business Name] email contact'")
    print("3. Facebook page (contact info section)")
    print("4. Yelp listing (Business contact section)")
    print("5. Call the business and ask for email")
    print()
    print("Common patterns for small businesses:")
    
    if category in ['Restaurant', 'Salon', 'Dentist']:
        print(f"  - owner@[businessname].com")
        print(f"  - contact@[businessname].com")
        print(f"  - info@[businessname].com")
    elif category in ['Plumbing', 'Electrical', 'HVAC', 'Auto Repair']:
        print(f"  - contact@[businessname].com")
        print(f"  - service@[businessname].com")
        print(f"  - owner@gmail.com (personal email)")
    else:
        print(f"  - info@[businessname].com")
        print(f"  - contact@[businessname].com")
    
    print()

def add_business():
    """
    Interactive form to add a single business
    """
    print("\n" + "=" * 80)
    print("ADD NEW BUSINESS")
    print("=" * 80)
    
    # Get basic info
    name = input("Business name: ").strip()
    if not name:
        print("❌ Business name required")
        return None
    
    phone = input("Phone number (e.g., 617-555-1234): ").strip()
    if not phone:
        print("❌ Phone number required")
        return None
    
    # Category selection
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
    
    city = input("City (default: Boston, MA): ").strip() or "Boston, MA"
    
    # Check for website
    print(f"\n🌐 Checking for website...")
    has_website, domain = check_website_exists(name)
    
    if has_website:
        print(f"⚠️  WARNING: Domain found: {domain}")
        keep_going = input("   Keep this business anyway? (y/n): ").strip().lower()
        if keep_going != 'y':
            print("❌ Business skipped (has website)")
            return None
    else:
        print(f"✅ No website found (good candidate)")
    
    # Search email guidance
    search_email(name, category)
    
    # Get email
    email = input("Email address (or press Enter to skip): ").strip()
    owner = input("Owner name (optional): ").strip()
    confidence = input("Confidence % (e.g., 75): ").strip()
    notes = input("Notes (optional): ").strip()
    
    business = {
        'name': name,
        'phone': phone,
        'category': category,
        'city': city,
        'email': email or 'NOT FOUND',
        'owner': owner or 'Unknown',
        'confidence': confidence or '65',
        'has_website': has_website,
        'domain_found': domain or 'None',
        'notes': notes,
        'date_added': datetime.now().isoformat(),
        'verified': True  # Manually verified
    }
    
    return business

def save_business(business):
    """
    Save business to CSV + JSON
    """
    if not business:
        return
    
    # Append to CSV
    file_exists = OUTPUT_FILE.exists()
    
    with open(OUTPUT_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'name', 'phone', 'category', 'city', 'email', 'owner', 
            'confidence', 'has_website', 'domain_found', 'notes', 'date_added'
        ])
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(business)
    
    # Also save to JSON for reference
    all_businesses = []
    if JSON_FILE.exists():
        with open(JSON_FILE, 'r') as f:
            all_businesses = json.load(f)
    
    all_businesses.append(business)
    
    with open(JSON_FILE, 'w') as f:
        json.dump(all_businesses, f, indent=2)
    
    print(f"\n✅ Saved: {business['name']}")
    print(f"   Email: {business['email']}")
    print(f"   Confidence: {business['confidence']}%")

def show_progress():
    """
    Show how many businesses have been added
    """
    if not OUTPUT_FILE.exists():
        print("0 businesses added yet")
        return
    
    with open(OUTPUT_FILE, 'r') as f:
        count = sum(1 for line in f) - 1  # Subtract header
    
    print(f"✅ {count} / 50 businesses verified")
    
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
            print(f"  {cat:15} {by_category[cat]}")

def export_for_outreach():
    """
    Export verified businesses for email campaign
    """
    if not OUTPUT_FILE.exists():
        print("❌ No businesses added yet")
        return
    
    with open(OUTPUT_FILE, 'r') as f:
        businesses = list(csv.DictReader(f))
    
    # Filter out those without emails
    with_emails = [b for b in businesses if b['email'] != 'NOT FOUND']
    
    print(f"\n📊 EXPORT SUMMARY")
    print(f"=" * 60)
    print(f"Total verified:        {len(businesses)}")
    print(f"With email addresses:  {len(with_emails)}")
    print(f"Without email:         {len(businesses) - len(with_emails)}")
    print(f"\nReady for outreach:    {len(with_emails)} businesses")
    
    if len(with_emails) > 0:
        print(f"\n✅ Export to: {OUTPUT_FILE}")
        print(f"   Use for: send_approved_batch_v2.py")

def main():
    print("=" * 80)
    print("FIND REAL BOSTON BUSINESSES WITHOUT WEBSITES")
    print("Interactive Research Tool")
    print("=" * 80)
    print()
    print("This tool helps you manually research and verify real Boston businesses")
    print("that don't have websites. Takes ~4-5 min per business.")
    print()
    
    while True:
        print("\n" + "=" * 80)
        print("MENU")
        print("=" * 80)
        show_progress()
        print()
        print("Options:")
        print("  1. Add a new business")
        print("  2. View businesses added so far")
        print("  3. Export for email campaign")
        print("  4. Exit")
        print()
        
        choice = input("Select (1-4): ").strip()
        
        if choice == '1':
            business = add_business()
            if business:
                save_business(business)
        
        elif choice == '2':
            if OUTPUT_FILE.exists():
                print("\nBUSINESSES ADDED:")
                print("-" * 80)
                with open(OUTPUT_FILE, 'r') as f:
                    reader = csv.DictReader(f)
                    for i, row in enumerate(reader, 1):
                        email_status = "✅" if row['email'] != 'NOT FOUND' else "❌"
                        print(f"{i:2}. {email_status} {row['name']:40} | {row['category']:15}")
            else:
                print("No businesses added yet")
        
        elif choice == '3':
            export_for_outreach()
        
        elif choice == '4':
            print("\n✅ Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")

if __name__ == '__main__':
    main()
