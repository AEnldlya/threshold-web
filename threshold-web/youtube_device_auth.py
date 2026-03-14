#!/usr/bin/env python3
"""
YouTube upload using Google Device Flow OAuth.
No interactive browser needed - user just enters a code.
"""

import os
import json
import sys
import time
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CRED_FILE = '/home/clawdbot/.openclaw/workspace/.gmail_credentials.json'
TOKEN_FILE = '/home/clawdbot/.openclaw/workspace/.youtube_device_token.json'
VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_1_CINEMATIC.mp4'

def get_device_auth():
    """Get authorization via device flow (no browser needed)."""
    
    print("\n" + "="*70)
    print("DEVICE FLOW AUTHENTICATION")
    print("="*70)
    
    try:
        flow = Flow.from_client_secrets_file(
            CRED_FILE,
            scopes=SCOPES,
            redirect_uri='urn:ietf:wg:oauth:2.0:oob'  # Out of band - no redirect needed
        )
        
        auth_url, _ = flow.authorization_url()
        
        print(f"\n→ Step 1: Open this link:")
        print(f"{auth_url}")
        
        print(f"\n→ Step 2: You'll see a code displayed")
        print(f"→ Step 3: Paste that code below:\n")
        
        auth_code = input("Authorization code: ").strip()
        
        if not auth_code:
            print("✗ No code entered")
            return None
        
        print(f"\n→ Exchanging code for credentials...")
        creds = flow.fetch_token(code=auth_code)
        
        # Save for future use
        with open(TOKEN_FILE, 'w') as f:
            json.dump(creds, f)
        
        print(f"✓ Got credentials")
        return creds
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def upload(creds):
    """Upload video to YouTube."""
    
    print("\n" + "="*70)
    print("UPLOADING VIDEO")
    print("="*70 + "\n")
    
    try:
        youtube = build('youtube', 'v3', credentials=creds)
        
        body = {
            'snippet': {
                'title': 'The Job Interview - A Dark Story | AI Story',
                'description': '''I got hired in 3 minutes. That should've been my first warning.

A short dark fiction story about a suspicious job interview that leads to a terrifying discovery.

This is a work of fiction created for entertainment purposes using AI technology.

#storytelling #horror #shortfilm #thriller #darkfiction #AI''',
                'tags': ['storytelling', 'horror', 'shortfilm', 'thriller', 'darkstory', 'AI'],
                'categoryId': '24'
            },
            'status': {
                'privacyStatus': 'public',
                'madeForKids': False
            }
        }
        
        print(f"→ Uploading {os.path.getsize(VIDEO_FILE)/1024:.1f}KB...")
        
        media = MediaFileUpload(VIDEO_FILE, chunksize=-1, resumable=True)
        request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
        
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                pct = int(status.progress() * 100)
                print(f"  {pct}%...", end='\r')
        
        vid_id = response['id']
        
        print(f"\n\n" + "="*70)
        print(f"✓ SUCCESS!")
        print(f"="*70)
        print(f"\n📺 https://youtu.be/{vid_id}\n")
        print("="*70 + "\n")
        
        return True
        
    except Exception as e:
        print(f"✗ Upload error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    
    print("\n" + "="*70)
    print("YOUTUBE UPLOAD - DEVICE FLOW")
    print("="*70)
    
    # Check files
    if not os.path.exists(CRED_FILE):
        print(f"\n✗ Credentials not found: {CRED_FILE}")
        return False
    
    if not os.path.exists(VIDEO_FILE):
        print(f"\n✗ Video not found: {VIDEO_FILE}")
        return False
    
    print(f"\n✓ Files ready")
    print(f"  Video: {os.path.basename(VIDEO_FILE)} ({os.path.getsize(VIDEO_FILE)/1024:.1f}KB)")
    
    # Try to load existing token first
    if os.path.exists(TOKEN_FILE):
        print(f"\n→ Found existing token, trying to use it...")
        try:
            with open(TOKEN_FILE, 'r') as f:
                creds_data = json.load(f)
            from google.oauth2.credentials import Credentials
            creds = Credentials.from_authorized_user_info(creds_data, scopes=SCOPES)
            
            if creds.expired and creds.refresh_token:
                print(f"→ Refreshing expired token...")
                creds.refresh(Request())
                with open(TOKEN_FILE, 'w') as f:
                    json.dump(creds.to_json() if hasattr(creds, 'to_json') else json.loads(creds.to_json()), f)
            
            if creds.valid:
                print(f"✓ Token is valid - using existing credentials")
                return upload(creds)
        except Exception as e:
            print(f"⚠ Could not use existing token: {e}")
    
    # Get new auth via device flow
    creds = get_device_auth()
    
    if not creds:
        print(f"\n✗ Authentication failed")
        return False
    
    return upload(creds)

if __name__ == '__main__':
    try:
        ok = main()
        sys.exit(0 if ok else 1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

