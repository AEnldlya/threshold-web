#!/usr/bin/env python3
"""
Extract Emails from Bland AI Call Transcripts
"""

import requests
import json
import re
import csv
from datetime import datetime
from pathlib import Path

ORG_ID = "org_ee4e630d8f9c9e87977d81989524af7338e9201db3754a625b29cbf6ea4e5c6c9881376e9162051faab869"
WORKSPACE = Path.home() / '.openclaw' / 'workspace'

def extract_email(text):
    """Extract email from text"""
    if not text:
        return None
    
    # Standard email pattern
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    matches = re.findall(email_pattern, text.lower())
    
    if matches:
        return matches[0]
    
    # Spoken email pattern: "info at business dot com"
    spoken = re.search(r'(\w+)\s+at\s+(\w+)\s+dot\s+(\w+)', text.lower())
    if spoken:
        return f"{spoken.group(1)}@{spoken.group(2)}.{spoken.group(3)}"
    
    return None

def get_call_details(call_id):
    """Get call details from Bland AI"""
    headers = {"Authorization": ORG_ID}
    url = f"https://api.bland.ai/v1/calls/{call_id}"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    
    return None

def main():
    results_file = WORKSPACE / "bland_calls_initiated.json"
    
    if not results_file.exists():
        print("❌ No calls initiated yet!")
        return
    
    with open(results_file) as f:
        calls = json.load(f)
    
    print("=" * 80)
    print("EXTRACTING EMAILS FROM BLAND AI CALLS")
    print("=" * 80)
    print()
    
    emails_found = []
    
    for i, call in enumerate(calls, 1):
        business_name = call['business_name']
        call_id = call['call_id']
        phone = call['phone']
        
        print(f"[{i}/9] {business_name}...")
        
        details = get_call_details(call_id)
        
        if not details:
            print(f"     ⏳ Call not ready yet")
            continue
        
        status = details.get('status')
        transcript = details.get('transcript', '')
        
        print(f"     Status: {status}")
        
        if transcript:
            email = extract_email(transcript)
            
            if email:
                print(f"     ✅ Email: {email}")
                emails_found.append({
                    "business_name": business_name,
                    "phone": phone,
                    "email": email,
                    "status": "success",
                    "transcript_excerpt": transcript[:150]
                })
            else:
                print(f"     ❌ No email found")
                print(f"        Transcript: {transcript[:100]}...")
                emails_found.append({
                    "business_name": business_name,
                    "phone": phone,
                    "email": None,
                    "status": "no_email_in_response",
                    "transcript_excerpt": transcript[:150]
                })
        else:
            print(f"     ⏳ Still transcribing...")
        
        print()
    
    # Save results
    if emails_found:
        csv_file = WORKSPACE / "bland_collected_emails.csv"
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'business_name', 'phone', 'email', 'status', 'transcript_excerpt'
            ])
            writer.writeheader()
            writer.writerows(emails_found)
        
        success_count = sum(1 for e in emails_found if e['email'])
        
        print("=" * 80)
        print("RESULTS")
        print("=" * 80)
        print(f"Emails collected: {success_count}/{len(emails_found)}")
        print()
        
        if success_count > 0:
            print("✅ EMAILS FOUND:")
            print("-" * 80)
            for item in emails_found:
                if item['email']:
                    print(f"{item['business_name']:30} {item['email']}")
        
        print()
        print(f"📁 Saved to: {csv_file}")

if __name__ == '__main__':
    main()
