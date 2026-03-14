#!/usr/bin/env python3
"""
Send emails via Gmail SMTP using App Password
No OAuth needed
"""

import json
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Gmail credentials
GMAIL_ADDRESS = 'Andy.li.zhang2010@gmail.com'
APP_PASSWORD = 'xrxy hkrb agpz tgml'  # Without spaces for SMTP

# Load emails
def load_emails():
    with open('/home/clawdbot/.openclaw/workspace/personalized_emails.json', 'r') as f:
        return json.load(f)

def load_sent_log():
    try:
        with open('/home/clawdbot/.openclaw/workspace/sent_emails_log.json', 'r') as f:
            return json.load(f)
    except:
        return {'sent': []}

def save_sent_log(log):
    with open('/home/clawdbot/.openclaw/workspace/sent_emails_log.json', 'w') as f:
        json.dump(log, f, indent=2)

def send_email(to_email, subject, body):
    """Send email via Gmail SMTP"""
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = GMAIL_ADDRESS
        msg['To'] = to_email
        
        # Add body
        text_part = MIMEText(body, 'plain')
        msg.attach(text_part)
        
        # Connect to Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ADDRESS, APP_PASSWORD.replace(' ', ''))
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending to {to_email}: {e}")
        return False

def send_batch(batch_size=50):
    """Send batch of emails"""
    print()
    print("=" * 70)
    print("GMAIL OUTREACH CAMPAIGN - BATCH SENDER")
    print("=" * 70)
    print()
    
    # Load emails and log
    emails = load_emails()
    sent_log = load_sent_log()
    already_sent = set(sent_log['sent'])
    
    print(f"Total emails available: {len(emails)}")
    print(f"Already sent: {len(already_sent)}")
    print()
    
    # Prepare batch
    batch_emails = []
    for email in emails:
        if email['to'] not in already_sent:
            batch_emails.append(email)
            if len(batch_emails) >= batch_size:
                break
    
    print(f"Sending batch of {len(batch_emails)} emails")
    print()
    
    sent_count = 0
    failed_count = 0
    
    for i, email_data in enumerate(batch_emails):
        recipient = email_data['to']
        subject = email_data['subject']
        body = email_data['body']
        
        print(f"[{i+1}/{len(batch_emails)}] Sending to {recipient}...", end=' ')
        
        if send_email(recipient, subject, body):
            sent_count += 1
            already_sent.add(recipient)
            sent_log['sent'].append(recipient)
            print("✓")
        else:
            failed_count += 1
            print("✗")
        
        # Rate limit: 5-second delay between emails to avoid spam filters
        if i < len(batch_emails) - 1:
            time.sleep(5)
    
    # Save log
    save_sent_log(sent_log)
    
    # Summary
    print()
    print("=" * 70)
    print("BATCH COMPLETE")
    print("=" * 70)
    print(f"Sent: {sent_count}")
    print(f"Failed: {failed_count}")
    print(f"Total sent in campaign: {len(already_sent)}")
    print(f"Emails remaining: {len(emails) - len(already_sent)}")
    print("=" * 70)
    print()

if __name__ == '__main__':
    send_batch(50)
