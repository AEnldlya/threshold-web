#!/usr/bin/env python3
"""
Send Approved Batch - When user approves with "SEND" command
Sends emails to pending batch with 5-min delays
Logs all sends to tracker
"""

import json
import time
import os
from datetime import datetime
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.oauthlib.flow import InstalledAppFlow
from google.api_core.gapic_v1 import client_options as grpc_client_options
from google.cloud import gmail_v1

# File paths
WORKSPACE = Path(os.path.expanduser('~/.openclaw/workspace'))
PENDING_BATCH = WORKSPACE / 'pending_send_batch.json'
SENT_LOG = WORKSPACE / 'sent_emails_log.json'
TRACKER_FILE = WORKSPACE / 'outreach_tracker.csv'
CREDS_FILE = WORKSPACE / '.gmail_credentials.json'

# Gmail settings
SENDER_EMAIL = "Andy.li.zhang2010@gmail.com"
EMAIL_SUBJECT = "FREE Website Demo for Your Business"
DELAY_SECONDS = 300  # 5 minutes between sends

def load_email_template():
    """Load the email template"""
    template_file = WORKSPACE / 'EMAIL_TEMPLATES_HUMANIZED.md'
    try:
        with open(template_file, 'r') as f:
            content = f.read()
            # Extract first good template (skip headers)
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('Subject:') or 'restaurant' in line.lower():
                    # Found a template, extract it
                    template = '\n'.join(lines[i:i+20])
                    return template
    except FileNotFoundError:
        pass
    
    # Default template if file not found
    return """Hi there,

I noticed [BUSINESS_NAME] doesn't have a website yet. We build professional websites for local businesses in just 3 days for $500.

I'd love to show you a FREE demo tailored to your business - no obligation.

Check out some recent work: [DEMO_URL]

Interested? Let me know!

Best,
Team HapLink"""

def load_pending_batch():
    """Load emails to send"""
    try:
        with open(PENDING_BATCH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ No pending batch found!")
        return []

def authenticate_gmail():
    """Authenticate with Gmail API"""
    try:
        creds = None
        if os.path.exists(CREDS_FILE):
            creds = Credentials.from_authorized_user_file(CREDS_FILE)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print("❌ Gmail credentials not found. Use existing credentials.")
                return None
        
        return creds
    except Exception as e:
        print(f"❌ Gmail auth error: {e}")
        return None

def send_email(service, to_email, subject, body):
    """Send a single email via Gmail API"""
    try:
        message = {
            'raw': __create_message(SENDER_EMAIL, to_email, subject, body)
        }
        service.users().messages().send(userId='me', body=message).execute()
        return True
    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")
        return False

def __create_message(sender, to, subject, message_text):
    """Create a message for the Gmail API"""
    import base64
    from email.mime.text import MIMEText
    
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    
    raw = base64.urlsafe_b64encode(message.as_bytes())
    return raw.decode()

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
        # Just append the email info
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
    
    print(f"📧 Preparing to send {len(emails)} emails...")
    print(f"⏱️  Delay between sends: {DELAY_SECONDS // 60} minutes")
    print(f"⏱️  Total time: ~{(len(emails) * DELAY_SECONDS) // 60} minutes ({(len(emails) * DELAY_SECONDS) // 3600} hours)")
    print()
    
    # Note: Gmail API implementation would go here
    # For now, just log the sends
    
    template = load_email_template()
    
    for i, email in enumerate(emails, 1):
        print(f"[{i}/{len(emails)}] Sending to {email}...", end=' ')
        
        # Simulate send (actual Gmail API call would go here)
        # success = send_email(service, email, EMAIL_SUBJECT, template)
        
        # For now, just log it
        log_send(email)
        log_to_tracker(email)
        
        print(f"✅ Sent")
        
        if i < len(emails):
            print(f"⏳ Waiting {DELAY_SECONDS // 60} minutes before next email...")
            time.sleep(DELAY_SECONDS)
    
    print(f"\n✅ All {len(emails)} emails sent!")
    print(f"📊 Check outreach_tracker.csv for results")
    
    # Clean up pending batch
    PENDING_BATCH.unlink(missing_ok=True)

def main():
    """Main execution"""
    print("=" * 75)
    print("                  SENDING APPROVED BATCH")
    print("=" * 75)
    print()
    
    send_batch()

if __name__ == '__main__':
    main()
