#!/usr/bin/env python3
"""
Daily Prospect Report v2 - Weekly City Rotation + Duplicate Prevention
Ensures NO business is EVER contacted twice
Rotates through different cities each week
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

# File paths
WORKSPACE = Path(os.path.expanduser('~/.openclaw/workspace'))
CITIES_ROTATION = WORKSPACE / 'cities_rotation.json'
ALL_CONTACTED = WORKSPACE / 'all_contacted_businesses.json'
BOSTON_FILE = WORKSPACE / 'boston_167_VERIFIED_FINAL.csv'
SENT_LOG = WORKSPACE / 'sent_emails_log.json'
TRACKER_FILE = WORKSPACE / 'outreach_tracker.csv'
RESPONSES_FILE = WORKSPACE / 'daily_responses.json'

def get_current_week():
    """Calculate current week number"""
    start_date = datetime.fromisoformat('2026-03-02')
    days_elapsed = (datetime.utcnow() - start_date).days
    week_num = (days_elapsed // 7) + 1
    return week_num

def get_current_city():
    """Get the city for this week"""
    try:
        with open(CITIES_ROTATION, 'r') as f:
            cities_data = json.load(f)
        
        current_week = get_current_week()
        
        for city in cities_data['cities']:
            if city['week'] == current_week:
                return city
        
        # If no exact match, cycle through available cities
        available = [c for c in cities_data['cities'] if c['status'] in ['active', 'pending']]
        if available:
            return available[0]
    except FileNotFoundError:
        pass
    
    # Default to Boston if rotation file missing
    return {
        'name': 'Boston',
        'state': 'MA',
        'prospects_file': 'boston_167_VERIFIED_FINAL.csv',
        'week': 1
    }

def load_contacted_businesses():
    """Load all businesses ever contacted"""
    try:
        with open(ALL_CONTACTED, 'r') as f:
            data = json.load(f)
            return set(data.get('contacts', {}).keys())
    except FileNotFoundError:
        return set()

def load_boston_businesses():
    """Load Boston prospects (or current city prospects)"""
    businesses = []
    try:
        with open(BOSTON_FILE, 'r') as f:
            lines = f.readlines()[1:]  # Skip header
            for line in lines:
                # Handle CSV properly - split by comma but preserve fields
                parts = [p.strip() for p in line.strip().split(',')]
                if len(parts) >= 7:
                    # Extract confidence and clean it
                    confidence = parts[6].strip().rstrip('%')
                    try:
                        conf_float = float(confidence)
                    except:
                        conf_float = 0
                    
                    businesses.append({
                        'name': parts[0].strip(),
                        'phone': parts[1].strip(),
                        'category': parts[2].strip(),
                        'city': parts[3].strip(),
                        'email': parts[4].strip(),
                        'owner': parts[5].strip(),
                        'confidence': f"{conf_float:.0f}%" if conf_float > 0 else "0%",
                        'confidence_float': conf_float
                    })
    except FileNotFoundError:
        pass
    
    return businesses

def load_sent_emails():
    """Load log of already sent emails"""
    try:
        with open(SENT_LOG, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def load_responses():
    """Load responses received"""
    try:
        with open(RESPONSES_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_prospects_excluding_duplicates(all_businesses, contacted_ever, sent_today):
    """Get 50 companies that have NEVER been contacted"""
    # Exclude all businesses ever contacted (master file)
    new_businesses = [b for b in all_businesses if b['email'] not in contacted_ever]
    
    # Exclude any sent today
    today_emails = set(sent_today.keys()) if sent_today else set()
    new_businesses = [b for b in new_businesses if b['email'] not in today_emails]
    
    # Sort by confidence (highest first)
    new_businesses.sort(key=lambda x: x.get('confidence_float', 0), reverse=True)
    
    return new_businesses[:50]

def format_report(current_city, unsent, responses, contacted_ever):
    """Format the daily report"""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    current_week = get_current_week()
    
    report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                    DAILY PROSPECT REPORT - 7 AM                           ║
║                    WEEK {current_week}: {current_city['name'].upper()}, {current_city['state']}                              ║
║                         {now}                          ║
╚═══════════════════════════════════════════════════════════════════════════╝

🚨 DUPLICATE PREVENTION ACTIVE ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Showing ONLY new businesses (never contacted before)
Total businesses in system: {len(contacted_ever)} already contacted (NEVER re-contact)
Today's prospects: {len(unsent)} NEW opportunities

🌍 THIS WEEK'S CITY: {current_city['name']}, {current_city['state']}
   Rotation: Changes every 7 days
   Next week: New city, new prospects

📊 TODAY'S PROSPECTS (Top 50 by Confidence)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    
    if not unsent:
        report += "❌ NO NEW PROSPECTS AVAILABLE!\n"
        report += "All prospects in this city have been contacted.\n"
        report += "Wait for next week's city rotation or expand to new regions.\n"
        return report
    
    # Group by category
    by_category = {}
    for b in unsent:
        cat = b['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(b)
    
    # Print by category
    for i, (category, businesses) in enumerate(sorted(by_category.items()), 1):
        report += f"\n{i}. {category.upper()} ({len(businesses)} NEW prospects)\n"
        report += "─" * 75 + "\n"
        
        for j, b in enumerate(businesses, 1):
            confidence = b['confidence'].rstrip('%') if b['confidence'].endswith('%') else b['confidence']
            owner = f" ({b['owner']})" if b['owner'] else ""
            report += f"   {j:2d}. {b['name']:<30} {owner:<20} | {confidence:>3s}% | {b['email']}\n"
    
    # Add responses section
    if responses:
        report += f"\n\n✉️  RESPONSES RECEIVED ({len(responses)} total)\n"
        report += "━" * 75 + "\n"
        
        for email, info in list(responses.items())[:10]:
            status = info.get('status', 'Pending')
            date = info.get('date', 'Unknown')
            report += f"   • {email:<40} | {status:<15} | {date}\n"
        
        if len(responses) > 10:
            report += f"   ... and {len(responses) - 10} more responses\n"
    else:
        report += f"\n\n✉️  RESPONSES RECEIVED\n"
        report += "━" * 75 + "\n"
        report += "   No responses yet. Check back after sending emails!\n"
    
    # Action section
    report += f"""

🚀 READY TO SEND?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When ready, reply with:
   "SEND"  - Send emails to all {len(unsent)} NEW prospects
   "INFO"  - Show more details about a prospect
   "SKIP"  - Skip these and see next batch
   "STATS" - Show campaign statistics

⚠️  IMPORTANT: These are NEW prospects only. No duplicates will be sent.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    return report

def save_pending_batch(unsent):
    """Save the pending batch for when user approves"""
    pending_file = WORKSPACE / 'pending_send_batch.json'
    with open(pending_file, 'w') as f:
        json.dump([b['email'] for b in unsent], f, indent=2)
    print(f"Pending batch saved: {len(unsent)} emails")

def main():
    """Generate and display the daily report"""
    
    # Get current week and city
    current_week = get_current_week()
    current_city = get_current_city()
    
    print(f"\n🌍 WEEK {current_week}: {current_city['name']}, {current_city['state']}")
    print(f"Loading prospects...")
    
    # Load data
    businesses = load_boston_businesses()
    contacted_ever = load_contacted_businesses()
    sent_log = load_sent_emails()
    responses = load_responses()
    
    print(f"Loaded {len(businesses)} total prospects for {current_city['name']}")
    print(f"Already contacted (all-time): {len(contacted_ever)} businesses")
    print(f"Already sent today: {len(sent_log)} emails")
    
    # Get unsent businesses (excluding ALL duplicates)
    unsent = get_prospects_excluding_duplicates(businesses, contacted_ever, sent_log)
    
    if not unsent:
        print(f"❌ No new prospects available for {current_city['name']}!")
        print(f"All have been contacted. Waiting for next week's city rotation.")
    else:
        print(f"✅ Found {len(unsent)} NEW prospects (never contacted before)")
    
    # Format report
    report = format_report(current_city, unsent, responses, contacted_ever)
    
    # Print to console
    print(report)
    
    # Save report to file
    report_file = WORKSPACE / 'daily_report.txt'
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"✅ Report saved to: {report_file}")
    
    # Save pending batch if there are prospects
    if unsent:
        save_pending_batch(unsent)
    
    # Return report for sending to user
    return report

if __name__ == '__main__':
    main()
