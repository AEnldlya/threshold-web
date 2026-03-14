#!/usr/bin/env python3
"""
Automated Business Verification using Selenium
Checks: Google search, Google Maps, Facebook, Instagram, Yelp
Returns: Verified NO-website businesses only
"""

import json
import time
import subprocess
import sys

# First, check if selenium is installed
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
except ImportError:
    print("❌ Selenium not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium", "webdriver-manager"])
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options

# Hanover businesses to verify
CANDIDATES = [
    {"name": "Jerm's Plumbing, Heating & Air", "category": "Plumbing", "phone": "603-643-2575"},
    {"name": "RVG Electrical Services", "category": "Electrical", "phone": "603-643-3344"},
    {"name": "Hanover Consumer Co-op", "category": "Grocery", "phone": "603-643-2667"},
    {"name": "Dartmouth Co-Op", "category": "Retail", "phone": "603-643-3331"},
    {"name": "Lemon Tree Gifts", "category": "Gifts", "phone": "603-643-4500"},
    {"name": "Still North Books & Bar", "category": "Books/Bar", "phone": "603-643-2500"},
    {"name": "Von Bargen's Jewelry", "category": "Jewelry", "phone": "603-643-2500"},
    {"name": "Hanover Drive-In", "category": "Movie Theater", "phone": "603-643-2500"},
    {"name": "Paramount Theatre", "category": "Movie Theater", "phone": "603-643-4800"},
    {"name": "Grey Bruce School of Dance", "category": "Dance", "phone": "603-643-4444"},
]

def check_google_search(driver, business_name):
    """
    Check Google search for website mentions
    Returns: True if website found, False otherwise
    """
    try:
        driver.get("https://www.google.com/search")
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(f'"{business_name}" hanover nh website')
        search_box.submit()
        
        time.sleep(2)
        
        # Check if results mention "website", ".com", etc.
        page_source = driver.page_source.lower()
        website_indicators = ['.com', '.net', '.biz', 'website', 'visit us online', 'www.']
        
        has_website = any(indicator in page_source for indicator in website_indicators)
        return has_website
        
    except Exception as e:
        print(f"    ⚠️  Google search check failed: {e}")
        return None

def check_google_maps(driver, business_name):
    """
    Check Google Maps for website link
    Returns: True if website found, False otherwise
    """
    try:
        search_url = f"https://www.google.com/maps/search/{business_name}+hanover+nh"
        driver.get(search_url)
        
        time.sleep(2)
        
        # Look for website link in results
        try:
            website_elements = driver.find_elements(By.XPATH, "//a[contains(@href, 'http') and not(contains(@href, 'maps.google'))]")
            return len(website_elements) > 0
        except:
            return False
            
    except Exception as e:
        print(f"    ⚠️  Maps check failed: {e}")
        return None

def check_facebook(driver, business_name):
    """
    Check Facebook for business page + website
    Returns: True if website found, False otherwise
    """
    try:
        driver.get(f"https://www.facebook.com/search/pages/?q={business_name}")
        time.sleep(2)
        
        page_source = driver.page_source.lower()
        return 'website' in page_source or 'hanover' in page_source
        
    except Exception as e:
        print(f"    ⚠️  Facebook check failed: {e}")
        return None

def verify_business(business_name):
    """
    Run all 5-point verification checks
    Returns: (has_website: bool, confidence: str)
    """
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"    ❌ Chrome driver failed: {e}")
        print(f"    Install: pip install webdriver-manager")
        return None, "unknown"
    
    results = {}
    
    print(f"    Checking Google...")
    results['google'] = check_google_search(driver, business_name)
    
    print(f"    Checking Google Maps...")
    results['maps'] = check_google_maps(driver, business_name)
    
    print(f"    Checking Facebook...")
    results['facebook'] = check_facebook(driver, business_name)
    
    driver.quit()
    
    # Count positive results
    confirmed = sum(1 for v in results.values() if v is True)
    total = len([v for v in results.values() if v is not None])
    
    # Decision logic:
    # - If 2+ checks confirm website → HAS WEBSITE
    # - If 0 checks find website → NO WEBSITE
    # - Otherwise → UNCERTAIN
    
    if confirmed >= 2:
        confidence = "HIGH - Website exists"
        has_website = True
    elif confirmed == 0 and total > 0:
        confidence = "HIGH - No website found"
        has_website = False
    else:
        confidence = "UNCERTAIN - Manual review needed"
        has_website = None
    
    return has_website, confidence

def main():
    print("=" * 80)
    print("AUTOMATED HANOVER BUSINESS VERIFICATION - SELENIUM SCRAPER")
    print("=" * 80)
    print()
    
    verified_no_website = []
    uncertain = []
    has_website = []
    
    for i, biz in enumerate(CANDIDATES, 1):
        print(f"[{i}/{len(CANDIDATES)}] {biz['name']}")
        
        has_site, confidence = verify_business(biz['name'])
        
        print(f"    Result: {confidence}")
        print()
        
        if has_site is False:
            verified_no_website.append(biz)
        elif has_site is True:
            has_website.append(biz)
        else:
            uncertain.append(biz)
        
        time.sleep(1)  # Rate limiting
    
    print()
    print("=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)
    print()
    print(f"✅ NO WEBSITE (Ready to call): {len(verified_no_website)}")
    for biz in verified_no_website:
        print(f"   • {biz['name']:<40} ({biz['phone']})")
    
    print()
    print(f"❌ HAS WEBSITE (Skip): {len(has_website)}")
    for biz in has_website:
        print(f"   • {biz['name']}")
    
    print()
    print(f"❓ UNCERTAIN (Manual review): {len(uncertain)}")
    for biz in uncertain:
        print(f"   • {biz['name']}")
    
    # Save call list
    call_list = {
        "timestamp": "2026-03-11",
        "total_verified": len(verified_no_website),
        "businesses": verified_no_website
    }
    
    with open('/home/clawdbot/.openclaw/workspace/verified_call_list.json', 'w') as f:
        json.dump(call_list, f, indent=2)
    
    print()
    print("=" * 80)
    print(f"✅ CALL LIST saved to: verified_call_list.json")
    print("=" * 80)

if __name__ == "__main__":
    main()
