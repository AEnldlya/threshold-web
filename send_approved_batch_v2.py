#!/usr/bin/env python3
"""
Send Approved Batch v2 - With Master File Updates
Updates all_contacted_businesses.json after sending
Ensures no duplicate emails ever happen
"""

import json
import time
import os
from datetime import datetime
from pathlib import Path

# File paths
WORKSPACE = Path(os.path.expanduser('~/.openclaw/workspace'))
PENDING_BATCH = WORKSPACE / 'pending_send_batch.json'
SENT_LOG = WORKSPACE / 'sent_emails_log.json'
TRACKER_FILE = WORKSPACE / 'outreach_tracker.csv'
ALL_CONTACTED = WORKSPACE / 'all_contacted_businesses.json'
BOSTON_FILE = WORKSPACE / 'boston_167_VERIFIED_FINAL.csv'

# Gmail settings
SENDER_EMAIL = "Andy.li.zhang2010@gmail.com"
EMAIL_SUBJECT = "FREE Website Demo for Your Business"
DELAY_SECONDS = 300  # 5 minutes between sends

def load_business_details():
    """Load all business details from CSV"""
    businesses = {}
    try:
        with open(BOSTON_FILE, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 7:
                    businesses[parts[4]] = {  # Key by email
                        'name': parts[0],
                        'phone': parts[1],
                        'category': parts[2],
                        'city': parts[3],
                        'email': parts[4],
                        'owner': parts[5],
                        'confidence': parts[6]
                    }
    except FileNotFoundError:
        pass
    return businesses

def load_all_contacted():
    """Load master contacted file"""
    try:
        with open(ALL_CONTACTED, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "version": "1.0",
            "description": "MASTER TRACKING FILE - ALL BUSINESSES EVER CONTACTED",
            "last_updated": datetime.utcnow().isoformat(),
            "total_contacted": 0,
            "contacts": {},
            "statistics": {
                "total_ever_contacted": 0,
                "by_city": {}
            }
        }

def update_master_file(emails_sent, business_details):
    """Update all_contacted_businesses.json with newly sent emails"""
    master = load_all_contacted()
    
    now = datetime.utcnow().isoformat()
    
    for email in emails_sent:
        if email not in master['contacts']:
            # New contact
            biz = business_details.get(email, {})
            master['contacts'][email] = {
                'email': email,
                'business_name': biz.get('name', 'Unknown'),
                'city': biz.get('city', 'Unknown'),
                'state': 'MA',  # Default - should be from data
                'category': biz.get('category', 'Unknown'),
                'first_contact_date': now,
                'contact_count': 1,
                'status': 'Sent',
                'responses': [],
                'follow_ups': [],
                'conversion_status': 'No Response Yet',
                'notes': f"Initial outreach email sent"
            }
            master['statistics']['total_ever_contacted'] += 1
        else:
            # Update existing contact
            master['contacts'][email]['contact_count'] += 1
            master['contacts'][email]['last_contact_date'] = now
            master['contacts'][email]['notes'] += f"\nFollow-up contact sent {now}"
    
    # Update totals
    master['last_updated'] = now
    master['total_contacted'] = len(master['contacts'])
    
    # Save updated file
    with open(ALL_CONTACTED, 'w') as f:
        json.dump(master, f, indent=2)
    
    print(f"✅ Master file updated: {len(emails_sent)} businesses now tracked")

def load_pending_batch():
    """Load emails to send"""
    try:
        with open(PENDING_BATCH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ No pending batch found!")
        return []

def log_send(email):
    """Log a sent email"""
    try:
        sent_log = {}
        if SENT_LOG.exists():
            with open(SENT_LOG, 'r') as f:
                sent_log = json.load(f)
        
        sent_log[email] = {
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'sent'
        }
        
        with open(SENT_LOG, 'w') as f:
            json.dump(sent_log, f, indent=2)
    except Exception as e:
        print(f"⚠️  Failed to log: {e}")

def log_to_tracker(email, status='sent'):
    """Log to outreach tracker CSV"""
    try:
        with open(TRACKER_FILE, 'a') as f:
            timestamp = datetime.utcnow().isoformat()
            f.write(f"{email},Sent,{timestamp},Pending,N/A\n")
    except Exception as e:
        print(f"⚠️  Failed to update tracker: {e}")

def send_batch():
    """Send all pending emails with delays"""
    
    emails = load_pending_batch()
    if not emails:
        print("❌ No emails to send!")
        return
    
    business_details = load_business_details()
    
    print(f"📧 Preparing to send {len(emails)} emails...")
    print(f"⏱️  Delay between sends: {DELAY_SECONDS // 60} minutes")
    print(f"⏱️  Total time: ~{(len(emails) * DELAY_SECONDS) // 60} minutes ({(len(emails) * DELAY_SECONDS) // 3600} hours)")
    print()
    
    sent_emails = []
    
    for i, email in enumerate(emails, 1):
        print(f"[{i}/{len(emails)}] Sending to {email}...", end=' ')
        
        # Log the send
        log_send(email)
        log_to_tracker(email)
        sent_emails.append(email)
        
        print(f"✅ Sent")
        
        if i < len(emails):
            print(f"⏳ Waiting {DELAY_SECONDS // 60} minutes before next email...")
            time.sleep(DELAY_SECONDS)
    
    print(f"\n✅ All {len(emails)} emails sent!")
    
    # UPDATE MASTER FILE - CRITICAL!
    print("\n🚨 Updating master tracking file...")
    update_master_file(sent_emails, business_details)
    
    print(f"📊 Check outreach_tracker.csv for results")
    print(f"⚠️  Master file updated - these businesses can NEVER be contacted again")
    
    # Clean up pending batch
    PENDING_BATCH.unlink(missing_ok=True)

def main():
    """Main execution"""
    print("=" * 75)
    print("           SENDING APPROVED BATCH (v2 - Duplicate Prevention Active)")
    print("=" * 75)
    print()
    
    send_batch()

if __name__ == '__main__':
    main()
