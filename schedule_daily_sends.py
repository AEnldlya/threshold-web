#!/usr/bin/env python3
"""
Automated Daily Email Scheduler
Sends 50 emails per day automatically at specified time
"""

import schedule
import time
import json
import subprocess
import os
from datetime import datetime

SEND_SCRIPT = '/home/clawdbot/.openclaw/workspace/send_outreach.py'
SENT_LOG = '/home/clawdbot/.openclaw/workspace/sent_emails_log.json'
SCHEDULE_LOG = '/home/clawdbot/.openclaw/workspace/schedule_log.json'

def load_schedule_log():
    """Load schedule history"""
    if os.path.exists(SCHEDULE_LOG):
        with open(SCHEDULE_LOG, 'r') as f:
            return json.load(f)
    return {'last_send': None, 'total_sent': 0, 'batches': []}

def save_schedule_log(log):
    """Save schedule history"""
    with open(SCHEDULE_LOG, 'w') as f:
        json.dump(log, f, indent=2)

def load_sent_log():
    """Check how many already sent"""
    if os.path.exists(SENT_LOG):
        with open(SENT_LOG, 'r') as f:
            data = json.load(f)
            return len(data.get('sent', []))
    return 0

def send_daily_batch():
    """Send 50 emails daily"""
    schedule_log = load_schedule_log()
    already_sent = load_sent_log()
    
    print()
    print("=" * 70)
    print(f"DAILY EMAIL SEND - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Calculate batch number
    batch_num = (already_sent // 50) + 1
    start_index = already_sent
    batch_size = 50
    
    print(f"Batch #{batch_num}")
    print(f"Starting index: {start_index}")
    print(f"Batch size: {batch_size}")
    print(f"Already sent total: {already_sent}")
    print()
    
    # Run the send script
    try:
        print("Executing send_outreach.py...")
        result = subprocess.run(
            ['python3', SEND_SCRIPT, str(batch_size), str(start_index)],
            cwd='/home/clawdbot/.openclaw/workspace',
            capture_output=True,
            text=True,
            timeout=600  # 10 minute timeout
        )
        
        print(result.stdout)
        
        if result.returncode == 0:
            print("✓ Batch sent successfully!")
            
            # Update log
            schedule_log['last_send'] = datetime.now().isoformat()
            schedule_log['total_sent'] = load_sent_log()
            schedule_log['batches'].append({
                'batch_num': batch_num,
                'sent_date': datetime.now().isoformat(),
                'count': batch_size,
                'start_index': start_index
            })
            save_schedule_log(schedule_log)
        else:
            print("✗ Error sending emails:")
            print(result.stderr)
    
    except subprocess.TimeoutExpired:
        print("✗ Script timeout (took more than 10 minutes)")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("=" * 70)
    print()

def start_scheduler(send_time='09:00'):
    """
    Start the daily scheduler
    
    Args:
        send_time: Time to send daily (default 09:00 = 9 AM)
    """
    print("=" * 70)
    print("DAILY EMAIL SCHEDULER STARTED")
    print("=" * 70)
    print()
    print(f"Schedule: Every day at {send_time}")
    print(f"Batch size: 50 emails per day")
    print()
    print("Scheduler is running. Press Ctrl+C to stop.")
    print()
    
    # Schedule daily send
    schedule.every().day.at(send_time).do(send_daily_batch)
    
    # Keep scheduler running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute if task is due

if __name__ == '__main__':
    import sys
    
    send_time = '09:00'  # Default 9 AM
    
    if len(sys.argv) > 1:
        send_time = sys.argv[1]
    
    try:
        start_scheduler(send_time=send_time)
    except KeyboardInterrupt:
        print("\n\nScheduler stopped by user")
        print("Total emails sent logged in: schedule_log.json")
