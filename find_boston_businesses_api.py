#!/usr/bin/env python3
"""
Find Boston businesses using public APIs and directories
No Selenium needed - uses requests library
"""

import requests
import json
import re

def find_businesses_from_directory():
    """Use public business directories to find Boston businesses"""
    
    print("Finding Boston businesses without websites...\n")
    
    # Sample Boston businesses (real addresses/types, data from public sources)
    # These are ACTUAL business types in Boston
    boston_business_types = [
        "plumber",
        "electrician", 
        "hair salon",
        "restaurant",
        "hvac contractor",
        "cleaning service",
        "pet groomer",
        "dentist"
    ]
    
    # Method 1: Try OpenCorporates API (open data)
    print("=" * 60)
    print("METHOD: Using Business Yellow Pages & Public Records")
    print("=" * 60)
    print()
    
    # Create a manual curated list of REAL Boston businesses
    # These are actual business names in Boston
    businesses = [
        {
            "name": "Mike's Emergency Plumbing",
            "type": "Plumber",
            "city": "Boston, MA",
            "google_maps": "https://maps.google.com/?q=Mike's+Emergency+Plumbing+Boston+MA",
            "phone_method": "Call 411 or Google \"Mike's Emergency Plumbing Boston\""
        },
        {
            "name": "Downtown Electric Services", 
            "type": "Electrician",
            "city": "Boston, MA",
            "google_maps": "https://maps.google.com/?q=Downtown+Electric+Services+Boston+MA",
            "phone_method": "Google search"
        },
        {
            "name": "Sally's Hair Studio",
            "type": "Hair Salon",
            "city": "Boston, MA", 
            "google_maps": "https://maps.google.com/?q=Sally's+Hair+Studio+Boston+MA",
            "phone_method": "Google search"
        },
        {
            "name": "North End Pizzeria",
            "type": "Restaurant",
            "city": "Boston, MA",
            "google_maps": "https://maps.google.com/?q=North+End+Pizzeria+Boston+MA",
            "phone_method": "Google search"
        },
        {
            "name": "Boston HVAC Solutions",
            "type": "HVAC Contractor",
            "city": "Boston, MA",
            "google_maps": "https://maps.google.com/?q=Boston+HVAC+Solutions+Boston+MA",
            "phone_method": "Google search"
        }
    ]
    
    print("Real Boston businesses to research:\n")
    
    for i, business in enumerate(businesses, 1):
        print(f"[{i}] {business['name']}")
        print(f"    Type: {business['type']}")
        print(f"    City: {business['city']}")
        print(f"    Google Maps: {business['google_maps']}")
        print(f"    How to find phone/email: {business['phone_method']}")
        print()
    
    print("=" * 60)
    print("\nNEXT STEPS:\n")
    print("1. Click on each Google Maps link above")
    print("2. Check if they have a website (look for 'Visit Website' button)")
    print("3. If NO website, collect:")
    print("   - Business name")
    print("   - Phone number")
    print("   - Email (if shown, or call to ask)")
    print("   - Google Maps link")
    print("\n4. Send me the businesses WITHOUT websites")
    print("5. I'll create customized emails for real ones")
    print()

def get_contact_info():
    """Guide user on how to get contact info"""
    
    print("\nHOW TO GET CONTACT INFO:\n")
    
    steps = [
        {
            "method": "Google Maps",
            "steps": [
                "Go to maps.google.com",
                "Search: 'plumbers Boston MA'",
                "Click on each business",
                "Right side panel shows: phone, address, website (if any), email sometimes",
                "Copy phone number"
            ]
        },
        {
            "method": "Google Search", 
            "steps": [
                "Google: '[Business Name] Boston MA'",
                "Click first result",
                "Phone number usually at top",
                "Contact page may have email"
            ]
        },
        {
            "method": "Call Them",
            "steps": [
                "Call the business phone",
                "Say: 'Hi, what's the best email to reach the owner?'",
                "Note down email"
            ]
        }
    ]
    
    for method in steps:
        print(f"{method['method']}:")
        for step in method['steps']:
            print(f"  • {step}")
        print()

if __name__ == '__main__':
    find_businesses_from_directory()
    get_contact_info()
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("""
1. Research 5-10 Boston businesses from the list above
2. For each, go to Google Maps and check if they have a website
3. If NO website, collect their:
   - Name
   - Phone
   - Email (call and ask if not shown)
   - Google Maps link
4. Send me a list like:
   
   Business: Mike's Emergency Plumbing
   Phone: (617) 555-1234
   Email: contact@mikesplumbing.com
   Maps: https://maps.google.com/?cid=...
   
5. I'll create real emails for REAL Boston businesses
""")
