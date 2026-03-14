#!/usr/bin/env python3
"""
Automated Email Responder
Monitors inbox for campaign replies and auto-responds intelligently
"""

import json
import base64
import os
import sys
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery as discovery

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
CREDENTIALS_FILE = '/home/clawdbot/.openclaw/workspace/.gmail_credentials.json'
TOKEN_FILE = '/home/clawdbot/.openclaw/workspace/token.json'
RESPONSE_LOG = '/home/clawdbot/.openclaw/workspace/email_responses_log.json'
DEMO_SITE = 'https://flat-lies-fold.loca.lt'  # Example demo site

# Email templates
TEMPLATES = {
    'initial_interest': {
        'subject': 'Re: {original_subject}',
        'body': '''Hi {name},

Thanks for getting back to me!

I help local businesses get professional websites without the hassle.
Here's the deal:

**Website: $500**
- Professional design (mobile-friendly)
- Your business info + reviews
- Contact form for customers
- You own the domain

**Optional Maintenance: $40/month**
- Updates + monitoring
- Email support

Most clients see 2-4 extra calls per week from the website.

Here's an example of what I build:
{demo_site}

If you want to see what it would look like for your business, 
just send me:
- 5-8 photos (storefront, team, work samples)
- Business hours
- Main services (2-3 sentences)
- Phone number + address

I'll build it and show you. No money upfront.

What do you think?

Andy
603-306-7508
'''
    },
    
    'photos_received': {
        'subject': 'Re: {original_subject}',
        'body': '''Hi {name},

Got your photos and business info! Building your website now.

I'll have it ready to review within 24 hours. You'll see it live 
before any money changes hands.

I'll send you a link to review. Let me know if you want any changes.

Talk soon!

Andy
'''
    },
    
    'payment_sent': {
        'subject': 'Re: {original_subject}',
        'body': '''Hi {name},

Perfect! I see your payment came through.

Now registering your domain and moving your website to permanent. 
Should be live within a few hours.

I'll send you the final link as soon as it's ready.

Thanks for your business!

Andy
'''
    },
    
    'approved': {
        'subject': 'Re: {original_subject}',
        'body': '''Hi {name},

Awesome! Glad you love it.

Here's the payment link: [USER_WILL_ADD_PAYPAL_LINK]

Click to pay $500. Once I see the payment, I'll register your 
domain and get it live.

Andy
'''
    }
}

def authenticate():
    """Authenticate with Gmail API"""
    creds = None
    
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    
    return creds

def get_email_body(email_id, service):
    """Extract email body from message"""
    try:
        message = service.users().messages().get(userId='me', id=email_id, format='full').execute()
        headers = message['payload']['headers']
        
        # Get subject and from
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        from_email = next((h['value'] for h in headers if h['name'] == 'From'), '')
        
        # Extract body
        body = ''
        if 'parts' in message['payload']:
            for part in message['payload']['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part['body'].get('data', '')
                    if data:
                        body = base64.urlsafe_b64decode(data).decode('utf-8')
                    break
        else:
            data = message['payload']['body'].get('data', '')
            if data:
                body = base64.urlsafe_b64decode(data).decode('utf-8')
        
        return {
            'subject': subject,
            'from': from_email,
            'body': body,
            'message_id': email_id
        }
    except Exception as e:
        print(f"Error reading email: {e}")
        return None

def extract_name(email_from):
    """Extract name from email"""
    # Format: "Bob Smith <bob@example.com>" or just "bob@example.com"
    if '<' in email_from:
        name = email_from.split('<')[0].strip()
    else:
        name = email_from.split('@')[0]
    
    return name.split()[0] if name else 'there'

def classify_email(body, subject):
    """Classify email intent based on content"""
    body_lower = body.lower()
    
    if any(phrase in body_lower for phrase in ['photos', 'attached', 'pictures', 'sending']):
        return 'photos_received'
    
    if any(phrase in body_lower for phrase in ['approved', 'looks great', 'awesome', 'perfect', 'love it', 'approval']):
        return 'approved'
    
    if any(phrase in body_lower for phrase in ['paid', 'payment sent', 'transferred', 'money sent']):
        return 'payment_sent'
    
    if any(phrase in body_lower for phrase in ['how much', 'price', 'cost', 'interested', 'tell me more']):
        return 'initial_interest'
    
    return None

def create_reply_message(sender, to, subject, body, in_reply_to_id=None):
    """Create reply message"""
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = to
    
    if in_reply_to_id:
        message['In-Reply-To'] = in_reply_to_id
    
    text_part = MIMEText(body, 'plain')
    message.attach(text_part)
    
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_reply(service, sender, to, subject, body, in_reply_to_id=None):
    """Send email reply"""
    try:
        message = create_reply_message(sender, to, subject, body, in_reply_to_id)
        result = service.users().messages().send(userId='me', body=message).execute()
        return True, result.get('id')
    except Exception as e:
        return False, str(e)

def load_response_log():
    """Load log of responses sent"""
    if os.path.exists(RESPONSE_LOG):
        with open(RESPONSE_LOG, 'r') as f:
            return json.load(f)
    return {'responses': []}

def save_response_log(log):
    """Save log of responses sent"""
    with open(RESPONSE_LOG, 'w') as f:
        json.dump(log, f, indent=2)

def process_emails():
    """Monitor inbox and auto-respond to campaign replies"""
    
    print("=" * 70)
    print("EMAIL AUTO-RESPONDER")
    print("=" * 70)
    print()
    
    try:
        creds = authenticate()
        service = discovery.build('gmail', 'v1', credentials=creds)
    except Exception as e:
        print(f"Authentication failed: {e}")
        return
    
    # Load response log
    response_log = load_response_log()
    already_replied = set(r['message_id'] for r in response_log['responses'])
    
    print("Checking inbox for campaign replies...")
    
    try:
        # Search for emails matching campaign keywords
        query = 'subject:(Google reviews OR professional website OR website thing) is:unread'
        results = service.users().messages().list(userId='me', q=query, maxResults=10).execute()
        
        messages = results.get('messages', [])
        
        if not messages:
            print("No new campaign replies found.")
            return
        
        print(f"Found {len(messages)} unread messages")
        print()
        
        for msg in messages:
            email_id = msg['id']
            
            # Skip if already replied
            if email_id in already_replied:
                print(f"✓ SKIP (already replied): {email_id}")
                continue
            
            # Read email
            email = get_email_body(email_id, service)
            if not email:
                continue
            
            print(f"Processing email from: {email['from']}")
            
            # Extract info
            name = extract_name(email['from'])
            body = email['body']
            subject = email['subject']
            
            # Classify intent
            intent = classify_email(body, subject)
            
            if not intent:
                print(f"  → SKIP (unclear intent)")
                print()
                continue
            
            print(f"  → Detected: {intent}")
            
            # Get template
            if intent not in TEMPLATES:
                print(f"  → SKIP (no template for {intent})")
                print()
                continue
            
            template = TEMPLATES[intent]
            
            # Prepare response
            reply_subject = template['subject'].format(original_subject=subject)
            reply_body = template['body'].format(
                name=name,
                demo_site=DEMO_SITE
            )
            
            # Send reply
            success, result = send_reply(
                service,
                'Andy.li.zhang2010@gmail.com',
                email['from'],
                reply_subject,
                reply_body,
                email_id
            )
            
            if success:
                print(f"  ✓ SENT: {intent}")
                
                # Log response
                response_log['responses'].append({
                    'date': datetime.now().isoformat(),
                    'from': email['from'],
                    'subject': subject,
                    'intent': intent,
                    'message_id': email_id,
                    'status': 'sent'
                })
                save_response_log(response_log)
            else:
                print(f"  ✗ FAILED: {result}")
            
            print()
            
            # Rate limiting
            time.sleep(1)
        
        print("=" * 70)
        print(f"Processed {len(messages)} emails")
        print(f"Total auto-responses sent: {len(response_log['responses'])}")
        print("=" * 70)
    
    except Exception as e:
        print(f"Error processing emails: {e}")

if __name__ == '__main__':
    process_emails()
