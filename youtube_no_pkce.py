#!/usr/bin/env python3
"""
YouTube upload without PKCE - simpler, more reliable.
"""

import sys
import json
import os
from requests_oauthlib import OAuth2Session
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

CLIENT_ID = '375341066442-04699vodntvs9gmiqomchub0bn5lnh71.apps.googleusercontent.com'
CLIENT_SECRET = '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'
TOKEN_URI = 'https://oauth2.googleapis.com/token'
AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

TOKEN_FILE = '/home/clawdbot/.openclaw/workspace/.youtube_token.json'
VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_1_CINEMATIC.mp4'

def get_auth_code():
    """Get authorization code via manual flow."""
    
    # Build auth URL manually (no PKCE)
    auth_url = f"{AUTH_URI}?response_type=code&client_id={CLIENT_ID}&scope={'+'.join(SCOPES)}&redirect_uri={REDIRECT_URI}&access_type=offline"
    
    print("\n" + "="*70)
    print("AUTHORIZATION (NO PKCE)")
    print("="*70)
    print(f"\nOpen this link:\n{auth_url}\n")
    print("="*70 + "\n")
    
    code = input("Paste the authorization code: ").strip()
    return code

def exchange_code(code):
    """Exchange code for token."""
    
    print("\n→ Exchanging code for token...")
    
    # Use requests directly to exchange (no PKCE)
    import requests
    
    data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    
    try:
        resp = requests.post(TOKEN_URI, data=data, timeout=10)
        resp.raise_for_status()
        token_data = resp.json()
        
        # Save token
        with open(TOKEN_FILE, 'w') as f:
            json.dump(token_data, f)
        
        print("✓ Got token")
        return token_data
        
    except Exception as e:
        print(f"✗ Error: {e}")
        if hasattr(e, 'response'):
            print(f"  Response: {e.response.text}")
        return None

def upload(token_data):
    """Upload video using token."""
    
    print("\n→ Uploading video...")
    
    from google.oauth2.credentials import Credentials
    
    # Create credentials from token
    creds = Credentials(
        token=token_data['access_token'],
        refresh_token=token_data.get('refresh_token'),
        token_uri=TOKEN_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    
    youtube = build('youtube', 'v3', credentials=creds)
    
    body = {
        'snippet': {
            'title': 'The Job Interview - A Dark Story | AI Story',
            'description': '''I got hired in 3 minutes. That should've been my first warning.

A short dark fiction story about a suspicious job interview that leads to a terrifying discovery.

#storytelling #horror #AI''',
            'tags': ['storytelling', 'horror', 'shortfilm', 'thriller', 'AI'],
            'categoryId': '24'
        },
        'status': {'privacyStatus': 'public', 'madeForKids': False}
    }
    
    media = MediaFileUpload(VIDEO_FILE, chunksize=-1, resumable=True)
    req = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
    
    resp = None
    while resp is None:
        s, resp = req.next_chunk()
        if s:
            print(f"  {int(s.progress()*100)}%...", end='\r')
    
    vid = resp['id']
    print(f"\n\n" + "="*70)
    print("SUCCESS!")
    print("="*70)
    print(f"\nhttps://youtu.be/{vid}\n")
    print("="*70 + "\n")
    return True

def main():
    code = get_auth_code()
    if not code:
        return False
    
    token = exchange_code(code)
    if not token:
        return False
    
    return upload(token)

if __name__ == '__main__':
    try:
        ok = main()
        sys.exit(0 if ok else 1)
    except Exception as e:
        print(f"✗ {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

