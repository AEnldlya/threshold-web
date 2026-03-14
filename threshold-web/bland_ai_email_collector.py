#!/usr/bin/env python3
"""
Bland AI Email Collector
Makes automated calls to Boston plumbing businesses to collect emails
"""

import requests
import json
import time
import os
from datetime import datetime
from pathlib import Path

# Get API key from environment
BLAND_API_KEY = os.getenv("BLAND_API_KEY")
BLAND_API_URL = "https://api.bland.ai/v1/calls"

WORKSPACE = Path.home() / '.openclaw' / 'workspace'

# Businesses to call
BUSINESSES = [
    {"name": "North End Plumbing", "phone": "+16177204950"},
    {"name": "Cassidy Plumbing", "phone": "+16172421575"},
    {"name": "Kellz Heating & Plumbing", "phone": "+16179394777"},
    {"name": "Baltic Plumbing & Heating", "phone": "+16172685050"},
    {"name": "Adra Plumbing & Heating", "phone": "+16175677777"},
    {"name": "Jackson Plumbing", "phone": "+17816039722"},
    {"name": "Gomes Plumbing & Heating", "phone": "+16178187601"},
    {"name": "Elliot Plumbing", "phone": "+16175232721"},
    {"name": "S&S Plumbing & Heating", "phone": "+16172663613"},
]

# Voice script
SCRIPT = """
Hi, this is an automated call from Andy's Web Solutions. 

I'm reaching out because we help local service businesses get professional websites, for just $500.

Quick question - what's the best email address to reach you or the owner at? 

Please say it slowly, and I'll record it.
"""

def make_call(business_name, phone_number):
    """Make a single call using Bland AI"""
    
    if not BLAND_API_KEY:
        print("❌ ERROR: BLAND_API_KEY not set!")
        print("   Set it with: export BLAND_API_KEY='your_key'")
        return None
    
    payload = {
        "phone_number": phone_number,
        "task": SCRIPT,
        "model": "premium",
        "language": "english",
        "voice": "maya",
        "first_sentence": f"Hi, I'm calling from Andy's Web Solutions about a website for {business_name}.",
        "record": True,
        "webhook": f"https://your-webhook.com/bland-callback",  # Optional: for real-time updates
    }
    
    headers = {
        "Authorization": BLAND_API_KEY,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(BLAND_API_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        
        call_data = response.json()
        print(f"✅ Call initiated to {business_name}")
        print(f"   Phone: {phone_number}")
        print(f"   Call ID: {call_data.get('call_id')}")
        
        return call_data
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to call {business_name}: {e}")
        return None

def check_call_status(call_id):
    """Check status of a call"""
    
    if not BLAND_API_KEY:
        return None
    
    url = f"https://api.bland.ai/v1/calls/{call_id}"
    headers = {"Authorization": BLAND_API_KEY}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error checking call status: {e}")
        return None

def main():
    print("=" * 80)
    print("BLAND AI EMAIL COLLECTOR")
    print("=" * 80)
    print()
    
    if not BLAND_API_KEY:
        print("❌ BLAND_API_KEY not set!")
        print()
        print("Setup Instructions:")
        print("1. Go to https://bland.ai and sign up")
        print("2. Get your API key from the dashboard")
        print("3. Set environment variable:")
        print("   export BLAND_API_KEY='sk-...'")
        print("4. Run this script again")
        print()
        return
    
    print(f"✅ BLAND_API_KEY configured")
    print(f"📞 Making {len(BUSINESSES)} calls...")
    print()
    
    call_results = []
    
    # Make all calls
    for i, business in enumerate(BUSINESSES, 1):
        print(f"[{i}/{len(BUSINESSES)}] Calling {business['name']}...")
        
        result = make_call(business['name'], business['phone'])
        
        if result:
            call_results.append({
                "business_name": business['name'],
                "phone": business['phone'],
                "call_id": result.get('call_id'),
                "status": "pending",
                "timestamp": datetime.now().isoformat(),
                "email": None
            })
        
        # Rate limit: 1 call per 2 seconds
        if i < len(BUSINESSES):
            time.sleep(2)
    
    print()
    print("=" * 80)
    print("CALL SUMMARY")
    print("=" * 80)
    print(f"Calls initiated: {len(call_results)}")
    print()
    print("Monitoring calls...")
    print("(Bland AI will record responses with emails)")
    print()
    
    # Save call results
    results_file = WORKSPACE / "bland_ai_call_results.json"
    with open(results_file, 'w') as f:
        json.dump(call_results, f, indent=2)
    
    print(f"✅ Results saved to: {results_file}")
    print()
    print("Next steps:")
    print("1. Calls are being made in background")
    print("2. AI will ask for email and record response")
    print("3. Check call status in ~5 minutes")
    print("4. Run: python3 check_bland_results.py")

if __name__ == '__main__':
    main()
