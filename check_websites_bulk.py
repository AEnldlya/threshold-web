#!/usr/bin/env python3
"""
Check 492 Boston businesses for websites (improved version).
Uses more accurate detection.
"""

import json
import subprocess
import time
import re
from collections import defaultdict

def check_nslookup(domain):
    """More reliable DNS check using nslookup."""
    try:
        result = subprocess.run(
            ['nslookup', domain],
            timeout=1,
            capture_output=True,
            text=True
        )
        # Domain exists if we get an IP address back (not "can't find")
        has_ip = 'Address:' in result.stdout and 'can\'t find' not in result.stdout
        return has_ip
    except:
        return False

def check_domain_patterns(business_name):
    """
    Generate domain patterns and check them.
    Be MORE selective - only accept exact/close matches.
    """
    # Clean the business name
    clean = business_name.lower().strip()
    
    # Remove common suffixes
    clean = re.sub(r'\s+(inc|co|corp|ltd|llc|&|\w+\s+service|studio|dds|office|center|club|academy).*$', '', clean, flags=re.IGNORECASE)
    
    # Generate patterns
    patterns = []
    words = clean.split()
    
    # Pattern 1: Full name no spaces
    patterns.append(clean.replace(' ', '') + '.com')
    
    # Pattern 2: Full name with hyphens
    patterns.append(clean.replace(' ', '-') + '.com')
    
    # Pattern 3: First 2 words
    if len(words) >= 2:
        patterns.append((words[0] + words[1]).lower() + '.com')
        patterns.append(words[0] + '-' + words[1] + '.com')
    
    # Pattern 4: .net versions
    patterns.append(clean.replace(' ', '') + '.net')
    patterns.append(clean.replace(' ', '-') + '.net')
    
    # Try each pattern
    for domain in patterns:
        if domain and len(domain) > 5:  # Sanity check
            if check_nslookup(domain):
                return True, domain
    
    return False, None

def load_businesses():
    """Load the 492 businesses."""
    with open('/home/clawdbot/.openclaw/workspace/boston_500_businesses.json', 'r') as f:
        return json.load(f)

def main():
    print("=" * 75)
    print("CHECKING 492 BOSTON BUSINESSES FOR WEBSITES")
    print("=" * 75)
    
    businesses = load_businesses()
    print(f"\nLoaded {len(businesses)} businesses\n")
    
    no_website_list = []
    has_website_list = []
    
    start_time = time.time()
    
    for i, business in enumerate(businesses, 1):
        name = business['name']
        category = business['category']
        phone = business['phone']
        
        found, domain = check_domain_patterns(name)
        
        if found:
            has_website_list.append({
                'name': name,
                'phone': phone,
                'category': category,
                'city': business['city'],
                'domain': domain,
                'has_website': True
            })
            status = f"✓ {domain}"
        else:
            no_website_list.append({
                'name': name,
                'phone': phone,
                'category': category,
                'city': business['city'],
                'has_website': False
            })
            status = "❌ NO WEBSITE"
        
        # Print every 50 for progress
        if i % 50 == 0 or i == len(businesses):
            elapsed = time.time() - start_time
            rate = i / elapsed
            remaining = (len(businesses) - i) / rate if rate > 0 else 0
            print(f"[{i:3}/{len(businesses)}] {status:25} | {name:40} | ETA: {remaining:.0f}s")
    
    elapsed = time.time() - start_time
    
    print("\n" + "=" * 75)
    print(f"RESULTS")
    print("=" * 75)
    print(f"Total checked: {len(businesses)}")
    print(f"With websites: {len(has_website_list)}")
    print(f"WITHOUT websites: {len(no_website_list)}")
    print(f"Time elapsed: {elapsed:.1f}s")
    print(f"Rate: {len(businesses)/elapsed:.1f} businesses/sec")
    print("=" * 75)
    
    # Breakdown by category
    print("\nBREAKDOWN BY CATEGORY (no websites):")
    by_category = defaultdict(int)
    for b in no_website_list:
        by_category[b['category']] += 1
    
    for cat in sorted(by_category.keys()):
        count = by_category[cat]
        total = sum(1 for b in businesses if b['category'] == cat)
        pct = (count / total * 100) if total > 0 else 0
        print(f"  {cat:15} {count:3} / {total:3} ({pct:5.1f}%)")
    
    # Save full results
    results = {
        'summary': {
            'total': len(businesses),
            'with_website': len(has_website_list),
            'without_website': len(no_website_list),
            'percentage_without': round(len(no_website_list) / len(businesses) * 100, 1)
        },
        'no_website_businesses': no_website_list,
    }
    
    output_file = '/home/clawdbot/.openclaw/workspace/boston_492_results.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n[✓] Full results saved to: {output_file}")
    
    # Save CSV for easier viewing
    csv_file = '/home/clawdbot/.openclaw/workspace/boston_no_websites.csv'
    with open(csv_file, 'w') as f:
        f.write("Name,Phone,Category,City\n")
        for b in no_website_list:
            f.write(f'"{b["name"]}","{b["phone"]}","{b["category"]}","{b["city"]}"\n')
    
    print(f"[✓] CSV list saved to: {csv_file}")
    
    # Print sample of no-website businesses
    if no_website_list:
        print(f"\n[SAMPLE] First 30 businesses WITHOUT websites:")
        print("-" * 75)
        for i, b in enumerate(no_website_list[:30], 1):
            print(f"{i:3}. {b['name']:40} | {b['category']:12} | {b['phone']}")

if __name__ == '__main__':
    main()
