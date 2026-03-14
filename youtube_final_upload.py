#!/usr/bin/env python3
"""
Final YouTube upload - fresh auth code generation.
User opens link, copies code, pastes here.
"""

import sys
import time
from google_auth_oauthlib.flow import Flow

CRED_FILE = '/home/clawdbot/.openclaw/workspace/.gmail_credentials.json'
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_fresh_code():
    """Generate fresh auth URL and wait for code."""
    
    flow = Flow.from_client_secrets_file(
        CRED_FILE,
        scopes=SCOPES,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )
    
    auth_url, _ = flow.authorization_url()
    
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "COPY AND PASTE THIS LINK INTO YOUR BROWSER:".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70)
    print(f"\n{auth_url}\n")
    print("█"*70)
    print("█" + " "*68 + "█")
    print("█" + "After clicking, you'll see an AUTHORIZATION CODE".center(68) + "█")
    print("█" + "Copy that code and paste it below:".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")
    
    code = input("Paste authorization code here: ").strip()
    
    if not code:
        print("✗ No code provided")
        return None
    
    return code, flow

def main():
    code, flow = get_fresh_code()
    
    if not code:
        return False
    
    print(f"\n→ Exchanging code for credentials...")
    
    try:
        creds = flow.fetch_token(code=code)
        print(f"✓ Got credentials!")
        
        # Now upload
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
        import os
        
        VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_1_CINEMATIC.mp4'
        
        youtube = build('youtube', 'v3', credentials=creds)
        
        body = {
            'snippet': {
                'title': 'The Job Interview - A Dark Story | AI Story',
                'description': '''I got hired in 3 minutes. That should've been my first warning.

A dark fiction story. #storytelling #horror #AI''',
                'tags': ['storytelling', 'horror', 'shortfilm', 'thriller', 'AI'],
                'categoryId': '24'
            },
            'status': {'privacyStatus': 'public', 'madeForKids': False}
        }
        
        print(f"\n→ Uploading video...")
        media = MediaFileUpload(VIDEO_FILE, chunksize=-1, resumable=True)
        req = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
        
        resp = None
        while resp is None:
            s, resp = req.next_chunk()
            if s:
                print(f"  {int(s.progress()*100)}%...", end='\r')
        
        vid = resp['id']
        print(f"\n\n✓✓✓ DONE ✓✓✓")
        print(f"\nhttps://youtu.be/{vid}\n")
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == '__main__':
    try:
        ok = main()
        sys.exit(0 if ok else 1)
    except Exception as e:
        print(f"✗ {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

