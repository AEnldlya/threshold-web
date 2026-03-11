#!/usr/bin/env python3
"""
Daily Prospect Report - 7 AM Task
Finds 50 new Boston companies without websites
Checks for responses from previous outreach
Formats report for user review
"""

import json
import os
from datetime import datetime
from pathlib import Path

# File paths
WORKSPACE = Path(os.path.expanduser('~/.openclaw/workspace'))
BOSTON_FILE = WORKSPACE / 'boston_167_VERIFIED_FINAL.csv'
TRACKER_FILE = WORKSPACE / 'outreach_tracker.csv'
SENT_LOG = WORKSPACE / 'sent_emails_log.json'
RESPONSES_FILE = WORKSPACE / 'daily_responses.json'

def load_boston_businesses():
    """Load the 167 verified Boston businesses"""
    businesses = []
    try:
        with open(BOSTON_FILE, 'r') as f:
            lines = f.readlines()[1:]  # Skip header
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) >= 7:
                    businesses.append({
                        'name': parts[0],
                        'phone': parts[1],
                        'category': parts[2],
                        'city': parts[3],
                        'email': parts[4],
                        'owner': parts[5],
                        'confidence': parts[6]
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

def get_unsent_businesses(all_businesses, sent_log):
    """Get 50 companies that haven't been contacted yet"""
    sent_emails = set(sent_log.keys()) if sent_log else set()
    unsent = [b for b in all_businesses if b['email'] not in sent_emails]
    
    # Sort by confidence (highest first)
    unsent.sort(key=lambda x: float(x['confidence'].rstrip('%')) if x['confidence'].endswith('%') else 0, reverse=True)
    
    return unsent[:50]

def format_report(unsent, responses):
    """Format the daily report"""
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    
    report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                    DAILY PROSPECT REPORT - 7 AM                           ║
║                         {now}                          ║
╚═══════════════════════════════════════════════════════════════════════════╝

📊 TODAY'S PROSPECTS (Top 50 by Confidence)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    
    # Group by category
    by_category = {}
    for b in unsent:
        cat = b['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(b)
    
    # Print by category with highest confidence first
    for i, (category, businesses) in enumerate(sorted(by_category.items()), 1):
        report += f"\n{i}. {category.upper()} ({len(businesses)} prospects)\n"
        report += "─" * 75 + "\n"
        
        for j, b in enumerate(businesses, 1):
            confidence = b['confidence'].rstrip('%') if b['confidence'].endswith('%') else b['confidence']
            report += f"   {j:2d}. {b['name']:<35} | {confidence:>3s}% | {b['email']}\n"
    
    # Add responses section
    if responses:
        report += f"\n\n✉️  RESPONSES RECEIVED ({len(responses)} total)\n"
        report += "━" * 75 + "\n"
        
        for email, info in responses.items():
            status = info.get('status', 'Pending')
            date = info.get('date', 'Unknown')
            report += f"   • {email:<40} | {status:<15} | {date}\n"
    else:
        report += f"\n\n✉️  RESPONSES RECEIVED\n"
        report += "━" * 75 + "\n"
        report += "   No responses yet. Check back after sending emails!\n"
    
    # Action section
    report += f"""

🚀 READY TO SEND?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When ready, reply with:
   "SEND"  - Send emails to all 50 prospects
   "INFO"  - Show more details about a prospect
   "SKIP"  - Skip these and see next batch
   "STATS" - Show campaign statistics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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
    
    # Load data
    businesses = load_boston_businesses()
    sent_log = load_sent_emails()
    responses = load_responses()
    
    print(f"Loaded {len(businesses)} total Boston businesses")
    print(f"Already sent: {len(sent_log)} emails")
    print(f"Responses: {len(responses)}")
    
    # Get unsent businesses
    unsent = get_unsent_businesses(businesses, sent_log)
    
    if not unsent:
        print("❌ No new prospects available! All 167 have been contacted.")
        return
    
    # Format report
    report = format_report(unsent, responses)
    
    # Print to console
    print(report)
    
    # Save report to file
    report_file = WORKSPACE / 'daily_report.txt'
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"\n✅ Report saved to: {report_file}")
    
    # Save pending batch
    save_pending_batch(unsent)
    
    # Return report for sending to user
    return report

if __name__ == '__main__':
    main()
