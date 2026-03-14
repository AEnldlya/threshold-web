#!/usr/bin/env python3
"""
Check Bland AI Call Results and Extract Emails
Polls call status and parses transcripts for email addresses
"""

import requests
import json
import re
import os
import csv
from datetime import datetime
from pathlib import Path

BLAND_API_KEY = os.getenv("BLAND_API_KEY")
WORKSPACE = Path.home() / '.openclaw' / 'workspace'

def extract_email_from_text(text):
    """Extract email address from transcribed text"""
    if not text:
        return None
    
    # Look for standard email pattern
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    matches = re.findall(email_pattern, text)
    
    if matches:
        return matches[0]  # Return first match
    
    # If no standard email, try to parse spoken email
    # "info at business dot com" → "info@business.com"
    text_lower = text.lower()
    
    # Pattern: "something at something dot com"
    spoken_pattern = r'(\w+)\s+at\s+(\w+)\s+dot\s+(\w+)'
    spoken_matches = re.findall(spoken_pattern, text_lower)
    
    if spoken_matches:
        user, domain, tld = spoken_matches[0]
        return f"{user}@{domain}.{tld}"
    
    return None

def get_call_details(call_id):
    """Get details for a specific call from Bland AI"""
    
    if not BLAND_API_KEY:
        return None
    
    url = f"https://api.bland.ai/v1/calls/{call_id}"
    headers = {"Authorization": BLAND_API_KEY}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error fetching call {call_id}: {e}")
        return None

def check_all_calls():
    """Check status of all calls and extract emails"""
    
    results_file = WORKSPACE / "bland_ai_call_results.json"
    
    if not results_file.exists():
        print("❌ No call results file found!")
        print(f"   Run: python3 bland_ai_email_collector.py first")
        return
    
    with open(results_file, 'r') as f:
        calls = json.load(f)
    
    print("=" * 80)
    print("BLAND AI RESULTS - EMAIL EXTRACTION")
    print("=" * 80)
    print()
    
    collected_emails = []
    
    for i, call in enumerate(calls, 1):
        call_id = call['call_id']
        business_name = call['business_name']
        phone = call['phone']
        
        print(f"[{i}/{len(calls)}] {business_name}...")
        
        # Get call details
        details = get_call_details(call_id)
        
        if not details:
            print(f"  ⏳ Call still in progress or not found")
            print(f"     Status: {details.get('status') if details else 'unknown'}")
            continue
        
        status = details.get('status')
        print(f"  Status: {status}")
        
        # Extract transcript
        transcript = details.get('transcript', '')
        
        if transcript:
            email = extract_email_from_text(transcript)
            
            if email:
                print(f"  ✅ Email found: {email}")
                collected_emails.append({
                    "business_name": business_name,
                    "phone": phone,
                    "email": email,
                    "transcript": transcript[:200],  # Store first 200 chars
                    "call_id": call_id,
                    "status": "success",
                    "collected_at": datetime.now().isoformat()
                })
            else:
                print(f"  ❌ No email found in transcript")
                print(f"     Transcript: {transcript[:100]}...")
                collected_emails.append({
                    "business_name": business_name,
                    "phone": phone,
                    "email": None,
                    "transcript": transcript[:200],
                    "call_id": call_id,
                    "status": "no_email",
                    "collected_at": datetime.now().isoformat()
                })
        else:
            print(f"  ⏳ No transcript yet (call still processing)")
            print(f"     Check again in 2 minutes")
        
        print()
    
    # Save collected emails to CSV
    if collected_emails:
        csv_file = WORKSPACE / "bland_ai_collected_emails.csv"
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'business_name', 'phone', 'email', 'status', 'transcript', 'call_id', 'collected_at'
            ])
            writer.writeheader()
            writer.writerows(collected_emails)
        
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)
        
        success_count = sum(1 for e in collected_emails if e['email'])
        print(f"Emails collected: {success_count}/{len(collected_emails)}")
        
        if success_count > 0:
            print("\n✅ Collected emails:")
            for item in collected_emails:
                if item['email']:
                    print(f"  {item['business_name']:30} {item['email']}")
        
        print(f"\n📁 Results saved to: {csv_file}")
    
    return collected_emails

def main():
    print("Checking Bland AI call results...")
    print()
    
    if not BLAND_API_KEY:
        print("❌ BLAND_API_KEY not set!")
        print("   Set with: export BLAND_API_KEY='sk-...'")
        return
    
    check_all_calls()

if __name__ == '__main__':
    main()
