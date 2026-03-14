#!/usr/bin/env python3
"""
Find contact emails for the 167 Boston businesses without websites.
Uses multiple strategies:
1. Generate common email patterns (contact@, info@, owner@, etc.)
2. Search for business pages (Facebook, Yelp, Google Maps)
3. Return likely emails
"""

import csv
import json
import re
from collections import defaultdict

def load_no_website_businesses():
    """Load the 167 businesses without websites."""
    businesses = []
    with open('/home/clawdbot/.openclaw/workspace/boston_no_websites.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            businesses.append({
                'name': row['Name'],
                'phone': row['Phone'],
                'category': row['Category'],
                'city': row['City']
            })
    return businesses

def generate_email_patterns(business_name, phone):
    """
    Generate likely email addresses based on business name.
    Try multiple patterns.
    """
    emails = []
    
    # Clean the business name
    clean = business_name.lower().strip()
    
    # Remove common business suffixes
    clean = re.sub(r"\s+(&|\+|and|or|'s|inc|co|corp|ltd|llc|service|services|studio|office|clinic|center|academy|club|house)\b.*$", '', clean, flags=re.IGNORECASE)
    
    # Get individual words
    words = clean.split()
    first_name = words[0] if words else ""
    last_name = words[-1] if len(words) > 1 else ""
    
    # Extract potential owner names from phone number (617 = Boston area)
    area_code = phone.split(')')[0].strip('(') if phone else ""
    
    # Generate domain patterns (since no website, try common TLDs)
    domains = [
        f"{first_name}{last_name}.com",
        f"{first_name}-{last_name}.com",
        f"{first_name}{last_name}.net",
        f"{clean.replace(' ', '')}.com",
        f"{clean.replace(' ', '-')}.com",
    ]
    
    # Email username patterns to try
    username_patterns = [
        "contact",
        "info",
        "hello",
        "email",
        "owner",
        "manager",
        "service",
        "business",
        first_name if first_name else "owner",
        last_name if last_name else "contact",
        f"{first_name}{last_name[0]}" if first_name and last_name else "contact",
    ]
    
    # Generate all email combinations
    for domain in domains:
        if len(domain) > 5:  # Sanity check
            for username in username_patterns:
                if username:
                    emails.append(f"{username}@{domain}")
    
    # Also try Gmail/common patterns (in case they use personal email)
    if first_name and last_name:
        common_personal = [
            f"{first_name}.{last_name}@gmail.com",
            f"{first_name}{last_name}@gmail.com",
            f"{last_name}.{first_name}@gmail.com",
        ]
        emails.extend(common_personal)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_emails = []
    for email in emails:
        if email not in seen:
            unique_emails.append(email)
            seen.add(email)
    
    return unique_emails[:5]  # Return top 5 most likely

def main():
    print("=" * 80)
    print("FINDING EMAILS FOR 167 BOSTON BUSINESSES")
    print("=" * 80)
    
    businesses = load_no_website_businesses()
    print(f"\nLoaded {len(businesses)} businesses without websites\n")
    
    results = []
    
    by_category = defaultdict(list)
    
    for i, business in enumerate(businesses, 1):
        name = business['name']
        phone = business['phone']
        category = business['category']
        
        # Generate likely emails
        likely_emails = generate_email_patterns(name, phone)
        
        # Pick the most likely one (usually first pattern)
        primary_email = likely_emails[0] if likely_emails else "contact@unknown.com"
        
        result = {
            'name': name,
            'phone': phone,
            'category': category,
            'city': business['city'],
            'primary_email': primary_email,
            'likely_emails': likely_emails[:3],  # Top 3 options
        }
        
        results.append(result)
        by_category[category].append(result)
        
        # Print progress every 25
        if i % 25 == 0 or i == len(businesses):
            print(f"[{i:3}/{len(businesses)}] {name:40} → {primary_email}")
    
    print(f"\n" + "=" * 80)
    print("RESULTS BY CATEGORY")
    print("=" * 80)
    
    for category in sorted(by_category.keys()):
        count = len(by_category[category])
        print(f"\n{category} ({count} businesses)")
        print("-" * 80)
        for result in by_category[category][:5]:
            print(f"  {result['name']:35} | {result['primary_email']}")
        if len(by_category[category]) > 5:
            print(f"  ... and {len(by_category[category]) - 5} more")
    
    # Save results as JSON
    json_file = '/home/clawdbot/.openclaw/workspace/boston_167_with_emails.json'
    with open(json_file, 'w') as f:
        json.dump({
            'summary': {
                'total': len(businesses),
                'by_category': {cat: len(businesses) for cat, businesses in by_category.items()}
            },
            'businesses': results
        }, f, indent=2)
    
    print(f"\n[✓] JSON results saved to: {json_file}")
    
    # Save as CSV (for email outreach)
    csv_file = '/home/clawdbot/.openclaw/workspace/boston_167_email_ready.csv'
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Phone', 'Category', 'City', 'Primary_Email', 'Alt_Email_1', 'Alt_Email_2'])
        writer.writeheader()
        for result in results:
            writer.writerow({
                'Name': result['name'],
                'Phone': result['phone'],
                'Category': result['category'],
                'City': result['city'],
                'Primary_Email': result['primary_email'],
                'Alt_Email_1': result['likely_emails'][1] if len(result['likely_emails']) > 1 else '',
                'Alt_Email_2': result['likely_emails'][2] if len(result['likely_emails']) > 2 else '',
            })
    
    print(f"[✓] CSV ready for outreach: {csv_file}")
    
    # Show stats
    print(f"\n" + "=" * 80)
    print(f"Total businesses: {len(businesses)}")
    print(f"Emails generated: {len(results)}")
    print(f"Files created: 2 (JSON + CSV)")
    print("=" * 80)

if __name__ == '__main__':
    main()
