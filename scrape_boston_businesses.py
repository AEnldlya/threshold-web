#!/usr/bin/env python3
"""
Scrape real Boston businesses without websites
Run this locally on your computer with: python3 scrape_boston_businesses.py
"""

# OPTION 1: Use Selenium + Chrome to scrape Google Maps
# Install: pip install selenium webdriver-manager

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    import json
    
    def scrape_google_maps(search_query, city="Boston, MA"):
        """Scrape Google Maps for businesses without websites"""
        
        # Setup Chrome driver
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Uncomment for headless mode
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        try:
            # Search on Google Maps
            search_url = f"https://www.google.com/maps/search/{search_query}+{city}"
            driver.get(search_url)
            
            print(f"Searching: {search_query} in {city}")
            print(f"URL: {search_url}")
            print()
            
            # Wait for results to load
            time.sleep(3)
            
            businesses = []
            
            # Get all business cards
            business_cards = driver.find_elements(By.CLASS_NAME, "Nv2PK")
            
            print(f"Found {len(business_cards)} businesses")
            print()
            
            for i, card in enumerate(business_cards[:10]):  # Get first 10
                try:
                    # Click the card to open details
                    card.click()
                    time.sleep(2)
                    
                    # Get business info from the right panel
                    try:
                        name = driver.find_element(By.CLASS_NAME, "DUwDvf").text
                    except:
                        name = "N/A"
                    
                    try:
                        rating = driver.find_element(By.CLASS_NAME, "e4rZib").text
                    except:
                        rating = "N/A"
                    
                    try:
                        reviews = driver.find_element(By.CLASS_NAME, "gm2-caption").text
                    except:
                        reviews = "N/A"
                    
                    try:
                        phone = driver.find_element(By.XPATH, "//button[contains(@data-tooltip, 'Call')]").text
                    except:
                        phone = "N/A"
                    
                    # Check if has website
                    try:
                        website_button = driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Website')]")
                        has_website = True
                        website = website_button.get_attribute('href')
                    except:
                        has_website = False
                        website = None
                    
                    # Get Google Maps link
                    try:
                        maps_link = driver.find_element(By.XPATH, "//a[contains(@href, 'maps')]").get_attribute('href')
                    except:
                        maps_link = driver.current_url
                    
                    # Try to find email
                    email = "N/A"
                    try:
                        email_element = driver.find_element(By.XPATH, "//a[contains(@href, 'mailto:')]")
                        email = email_element.get_attribute('href').replace('mailto:', '')
                    except:
                        pass
                    
                    business = {
                        'name': name,
                        'rating': rating,
                        'reviews': reviews,
                        'phone': phone,
                        'has_website': has_website,
                        'website': website,
                        'maps_link': maps_link,
                        'email': email
                    }
                    
                    # Only add if NO website
                    if not has_website:
                        businesses.append(business)
                        
                        print(f"[{len(businesses)}] {name}")
                        print(f"    Rating: {rating} ({reviews})")
                        print(f"    Phone: {phone}")
                        print(f"    Email: {email}")
                        print(f"    Website: NONE ✓")
                        print(f"    Maps: {maps_link}")
                        print()
                
                except Exception as e:
                    print(f"Error processing business {i}: {e}")
                    continue
            
            # Save to file
            with open('boston_businesses_no_website.json', 'w') as f:
                json.dump(businesses, f, indent=2)
            
            print()
            print(f"✓ Found {len(businesses)} businesses WITHOUT websites")
            print("✓ Saved to: boston_businesses_no_website.json")
            
            return businesses
        
        finally:
            driver.quit()
    
    # Run searches for different business types
    if __name__ == '__main__':
        searches = [
            'plumbers',
            'hair salons',
            'electricians',
            'restaurants',
            'hvac contractors'
        ]
        
        all_businesses = []
        
        for search in searches:
            print(f"\n{'='*60}")
            print(f"SEARCHING: {search.upper()}")
            print(f"{'='*60}\n")
            
            results = scrape_google_maps(search)
            all_businesses.extend(results)
            
            time.sleep(2)  # Pause between searches
        
        print(f"\n{'='*60}")
        print(f"TOTAL FOUND: {len(all_businesses)} businesses without websites")
        print(f"{'='*60}")

except ImportError:
    print("ERROR: Selenium not installed")
    print()
    print("To scrape Google Maps, install:")
    print("  pip install selenium webdriver-manager")
    print()
    print("Then run: python3 scrape_boston_businesses.py")
