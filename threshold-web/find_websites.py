#!/usr/bin/env python3

import json
import requests
import time
from datetime import datetime

# Load business data
with open('boston_businesses_final.json', 'r') as f:
    data = json.load(f)
    businesses = data['businesses']

# Try to load existing results
try:
    with open('business_websites.json', 'r') as f:
        websites_db = json.load(f)
except:
    websites_db = {}

def find_website(business_name, city="Boston, MA"):
    """Search for business website"""
    if business_name in websites_db:
        return websites_db[business_name]
    
    # Use Gemini + Google Search via web_search capability
    # For now, just log that we need to search
    print(f"Need to search: {business_name}")
    return None

# Print businesses that need website searches
for business in businesses:
    name = business['name']
    result = find_website(name)
    if not result:
        print(f"  - {name}")
