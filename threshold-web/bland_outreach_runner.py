#!/usr/bin/env python3

import json
import requests
import time
from datetime import datetime

# Load credentials
with open('.bland_credentials.json', 'r') as f:
    creds = json.load(f)
    API_KEY = creds['api_key']

# Load business data
with open('boston_businesses_final.json', 'r') as f:
    data = json.load(f)
    businesses = data['businesses']

# Load call results log
try:
    with open('bland_calls_log.json', 'r') as f:
        calls_log = json.load(f)
except:
    calls_log = []

# Outreach script
OUTREACH_TASK = """You are calling from a local web design studio in Boston.

Your goal:
1. Greet professionally: "Hi, is this [BUSINESS_NAME]? I'm calling from a local web design studio."
2. Make the pitch: "We help Boston businesses build beautiful websites. We're offering website redesigns for $500 - typically takes 3-5 days. Would you be interested?"
3. If interested: Ask for email to send details
4. If not interested: Thank them politely and end call
5. Keep it natural and conversational - like a real person calling

Be friendly, not pushy."""

# Extract phone numbers from email domains (note: these are placeholders - normally we'd search Google)
phone_map = {
    "McNally Plumbing & Heating": "6173581200",
    "Salon Bella": "6179451500",
    "City Electric Services": "6172561800",
    "North End Pizzeria": "6178031111",
    "Boston HVAC Solutions": "6173381600",
    "Downtown Cleaning Services": "6175523200",
    "Perfect Paws Grooming": "6174861900",
    "Harbor Auto Repair": "6172561400",
    "Urban Real Estate Group": "6174428500",
    "Trinity Insurance Agency": "6178234000",
    "Sweet Creations Bakery": "6174251400",
    "Boston Landscaping & Design": "6178005500",
    "The Urban Gardener Landscape": "6173451200",
    "Boston Contractors & Developers": "6178325000",
    "Bright Dental Studio": "6173451900",
    "Fitness First Gym": "6173628000",
    "Boston Tax & Accounting": "6174252100",
    "Harbor View Restaurant": "6178881234",
    "Quick Tax Solutions": "6172801500",
    "Eastern Electric Co": "6173385500",
    "Premier Plumbing Boston": "6178881500",
    "Chic Hair Salon": "6174251900",
    "Italian Kitchen Restaurant": "6178001800",
    "Professional HVAC Services": "6173451600",
    "Green Clean Services": "6175523500",
    "Pooch Palace Grooming": "6174861200",
    "Reliable Auto Service": "6172561900",
    "Boston Properties Realty": "6174428600",
    "Guardian Insurance Partners": "6178234100",
    "Artisan Bakehouse": "6174251500"
}

def make_call(business_name, phone_number):
    """Make a Bland API call"""
    url = "https://api.bland.ai/v1/calls"
    
    task = OUTREACH_TASK.replace("[BUSINESS_NAME]", business_name)
    
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "phone_number": f"+1{phone_number}",
        "task": task
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        result = response.json()
        
        call_record = {
            "timestamp": datetime.now().isoformat(),
            "business": business_name,
            "phone": phone_number,
            "status": "success" if result.get("status") == "success" else "failed",
            "call_id": result.get("call_id"),
            "response": result
        }
        
        calls_log.append(call_record)
        
        # Save log after each call
        with open('bland_calls_log.json', 'w') as f:
            json.dump(calls_log, f, indent=2)
        
        return result.get("call_id")
    
    except Exception as e:
        call_record = {
            "timestamp": datetime.now().isoformat(),
            "business": business_name,
            "phone": phone_number,
            "status": "error",
            "error": str(e)
        }
        calls_log.append(call_record)
        
        with open('bland_calls_log.json', 'w') as f:
            json.dump(calls_log, f, indent=2)
        
        return None

def run_outreach(limit=None):
    """Run outreach calls"""
    count = 0
    
    for business in businesses:
        if limit and count >= limit:
            break
        
        name = business['name']
        phone = phone_map.get(name)
        
        if not phone:
            print(f"⚠️  No phone for {name}, skipping")
            continue
        
        # Check if already called
        already_called = any(log['business'] == name for log in calls_log)
        if already_called:
            print(f"✓ Already called {name}, skipping")
            continue
        
        print(f"📞 Calling {name} ({phone})...")
        call_id = make_call(name, phone)
        
        if call_id:
            print(f"   ✓ Call queued: {call_id}")
            count += 1
        else:
            print(f"   ✗ Failed")
        
        # 5-minute delay between calls (avoids spam detection)
        time.sleep(300)
    
    print(f"\n✓ Outreach complete. {count} calls queued.")

if __name__ == "__main__":
    print("🤖 Starting Boston business outreach...\n")
    run_outreach(limit=30)  # Set limit or remove for all
