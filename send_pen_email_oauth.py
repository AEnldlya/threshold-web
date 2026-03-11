#!/usr/bin/env python3

import base64
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def send_pen_email():
    """Send email using Gmail API"""
    
    creds = None
    
    try:
        # Load existing credentials
        creds = Credentials.from_authorized_user_file('.gmail_credentials.json', SCOPES)
    except:
        print("❌ Need to authenticate first. Running OAuth flow...")
        flow = InstalledAppFlow.from_client_secrets_file(
            '.gmail_credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    
    try:
        service = build('gmail', 'v1', credentials=creds)
        
        # Email content
        sender = "Andy.li.zhang2010@gmail.com"
        recipient = "liamglenny@hanovernorwichschools.org"
        subject = "Yo, give me my pen back"
        body = """Liam,

Still waiting on that pen. Not sure what you're doing with it, but it's mine. Return it before I send the authorities.

Thanks,
Andy"""
        
        # Create message
        message = f"""From: {sender}
To: {recipient}
Subject: {subject}

{body}"""
        
        raw_message = base64.urlsafe_b64encode(message.encode()).decode()
        
        send_message = {
            'raw': raw_message
        }
        
        print(f"📧 Sending email to {recipient}...")
        result = service.users().messages().send(userId='me', body=send_message).execute()
        
        print(f"✓ Email sent successfully!")
        print(f"\nFrom: {sender}")
        print(f"To: {recipient}")
        print(f"Subject: {subject}")
        print(f"Message ID: {result['id']}")
        print(f"Sent at: {datetime.now().isoformat()}")
        
        return True
        
    except HttpError as error:
        print(f"❌ Error: {error}")
        return False

if __name__ == "__main__":
    send_pen_email()
