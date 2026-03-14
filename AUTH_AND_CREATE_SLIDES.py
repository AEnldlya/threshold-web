#!/usr/bin/env python3
"""
One-time OAuth authentication to create Google Slides.
Run this once to authenticate, then create_slides.py will work without prompting.
"""

import json
import os
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/presentations'
]

def authenticate():
    """Perform OAuth2 authentication and save token."""
    cred_file = '.gmail_credentials.json'
    token_file = '.google_token.json'
    
    try:
        flow = InstalledAppFlow.from_client_secrets_file(cred_file, scopes=SCOPES)
        
        # Try to open browser, but don't fail if it doesn't work
        try:
            creds = flow.run_local_server(port=0, open_browser=True)
        except:
            # Fallback: print auth URL for manual entry
            auth_url, _ = flow.authorization_url()
            print("\n🔗 Open this link in your browser:\n")
            print(auth_url)
            print("\n✅ After granting access, you'll be redirected to localhost with an auth code.")
            print("📋 Copy the full redirect URL and we'll extract the code.\n")
            
            redirect_url = input("Paste the redirect URL here: ").strip()
            
            # Extract auth code from redirect URL
            if 'code=' in redirect_url:
                code = redirect_url.split('code=')[1].split('&')[0]
                creds = flow.fetch_token(code=code)
            else:
                print("ERROR: Could not find auth code in redirect URL")
                return False
        
        # Save token
        with open(token_file, 'w') as f:
            f.write(creds.to_json())
        
        print(f"✅ Authentication successful! Token saved to {token_file}")
        return True
        
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return False

def create_slides():
    """Create Google Slides presentation and share it."""
    token_file = '.google_token.json'
    
    if not os.path.exists(token_file):
        print("ERROR: Token file not found. Run authentication first.")
        return False
    
    try:
        from google.oauth2.credentials import Credentials
        
        # Load token
        with open(token_file, 'r') as f:
            creds_data = json.load(f)
        
        creds = Credentials.from_authorized_user_info(creds_data, scopes=SCOPES)
        
        # Create services
        drive_service = build('drive', 'v3', credentials=creds)
        slides_service = build('slides', 'v1', credentials=creds)
        
        # Create presentation
        presentation = {'title': 'Boston Campaign & Projects - March 2026'}
        result = slides_service.presentations().create(body=presentation).execute()
        
        presentation_id = result['presentationId']
        url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
        
        print(f"\n✅ Created Google Slides presentation")
        print(f"ID: {presentation_id}")
        
        # Share with Andy's email
        permission = {
            'type': 'user',
            'role': 'editor',
            'emailAddress': 'Andy.li.zhang2010@gmail.com'
        }
        
        drive_service.permissions().create(
            fileId=presentation_id,
            body=permission
        ).execute()
        
        print(f"✅ Shared with Andy.li.zhang2010@gmail.com")
        print(f"\n🔗 GOOGLE SLIDES LINK:\n{url}\n")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating slides: {e}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("Google Slides Creation - Step 1: Authentication")
    print("=" * 60)
    
    if authenticate():
        print("\n" + "=" * 60)
        print("Step 2: Creating Google Slides")
        print("=" * 60)
        create_slides()
    else:
        print("\n❌ Authentication failed. Cannot proceed.")
