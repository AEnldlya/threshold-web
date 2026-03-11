#!/usr/bin/env python3

import asyncio
import json
import time
from datetime import datetime
from playwright.async_api import async_playwright

# Business data
businesses = [
    { "name": "McNally Plumbing & Heating", "url": "https://mcnallyplumbing.com", "contact_email": "contact@mcnallyplumbing.com" },
    { "name": "Downtown Cleaning Services", "url": "https://downtowncleaningservices.com", "contact_email": "contact@downtownclean.com" },
    { "name": "Harbor Auto Repair", "url": "https://harborautorepair.com", "contact_email": "harborauto@gmail.com" },
    { "name": "Bright Dental Studio", "url": "https://brightdental.boston", "contact_email": "info@brightdental.boston" },
    { "name": "Boston Tax & Accounting", "url": "https://bostontaxaccounting.com", "contact_email": "info@bostontaxaccounting.com" },
    { "name": "Harbor View Restaurant", "url": "https://harborview.boston", "contact_email": "reservations@harborview.boston" },
    { "name": "Chic Hair Salon", "url": "https://chichairsalon.com", "contact_email": "chichairsalon@gmail.com" },
    { "name": "Reliable Auto Service", "url": "https://reliableautoservice.com", "contact_email": "reliableauto@gmail.com" },
    { "name": "Guardian Insurance Partners", "url": "https://guardianinsurance.boston", "contact_email": "contact@guardianinsurance.boston" },
]

PITCH = """Hi there! We're a local Boston web design studio. We specialize in building professional websites for local businesses. Would you be interested in discussing a website redesign for your business? We typically build and deploy in 3-5 days for $500. Let's chat!

Send us a reply if you're interested and we can set up a quick call to discuss.

Thanks,
Website Design Studio"""

# Submission log
try:
    with open('form_submissions_log.json', 'r') as f:
        submissions_log = json.load(f)
except:
    submissions_log = []

async def fill_contact_form(page, business):
    """Try to fill a contact form on the business website"""
    try:
        print(f"\n📍 Visiting {business['name']}...")
        await page.goto(business['url'], timeout=15000, wait_until='networkidle')
        
        # Look for common contact form elements
        contact_form = None
        
        # Try to find contact form
        form_selectors = [
            'form',
            '[class*="contact"]',
            '[id*="contact"]',
            '[class*="form"]',
        ]
        
        for selector in form_selectors:
            try:
                form = await page.query_selector(selector)
                if form:
                    contact_form = form
                    break
            except:
                pass
        
        if not contact_form:
            print(f"  ⚠️  No contact form found on {business['url']}")
            log_submission(business, "no_form_found", None)
            return False
        
        # Try to find and fill text inputs
        inputs = await contact_form.query_selector_all('input[type="text"], textarea')
        
        # Find appropriate fields
        name_input = await contact_form.query_selector('input[placeholder*="ame"], input[name*="ame"]')
        email_input = await contact_form.query_selector('input[type="email"], input[placeholder*="mail"], input[name*="mail"]')
        message_input = await contact_form.query_selector('textarea, input[placeholder*="message"], input[placeholder*="Message"]')
        
        if name_input:
            await name_input.fill("Website Design Studio")
        
        if email_input:
            await email_input.fill("hello@websiteagency.boston")
        
        if message_input:
            await message_input.fill(PITCH)
        
        # Find and click submit button
        submit_btn = await contact_form.query_selector('button[type="submit"], input[type="submit"]')
        
        if submit_btn:
            print(f"  ✓ Submitting form for {business['name']}...")
            await submit_btn.click()
            await page.wait_for_timeout(2000)
            log_submission(business, "submitted", None)
            return True
        else:
            print(f"  ⚠️  No submit button found")
            log_submission(business, "no_submit_btn", None)
            return False
            
    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        log_submission(business, "error", str(e))
        return False

def log_submission(business, status, error):
    """Log form submission"""
    record = {
        "timestamp": datetime.now().isoformat(),
        "business": business['name'],
        "url": business['url'],
        "status": status,
        "error": error
    }
    submissions_log.append(record)
    
    with open('form_submissions_log.json', 'w') as f:
        json.dump(submissions_log, f, indent=2)

async def main():
    print("🤖 Starting form submission automation...\n")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        for business in businesses:
            page = await browser.new_page()
            await fill_contact_form(page, business)
            await page.close()
            
            # 5-minute delay between submissions
            time.sleep(300)
        
        await browser.close()
    
    print(f"\n✓ Form submissions complete. Check form_submissions_log.json for details.")

if __name__ == "__main__":
    asyncio.run(main())
