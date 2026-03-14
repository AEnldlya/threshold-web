#!/usr/bin/env python3
"""
Direct YouTube upload using known OAuth credentials.
Simplest possible approach.
"""

import os
import json
import sys
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

CRED_FILE = '/home/clawdbot/.openclaw/workspace/.gmail_credentials.json'
TOKEN_FILE = '/home/clawdbot/.openclaw/workspace/.youtube_device_token.json'
VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_1_CINEMATIC.mp4'

def try_upload():
    """Try to upload using any available credentials."""
    
    print("\n" + "="*70)
    print("YOUTUBE DIRECT UPLOAD")
    print("="*70 + "\n")
    
    # Check files
    if not os.path.exists(VIDEO_FILE):
        print(f"✗ Video not found")
        return False
    
    print(f"✓ Video ready: {os.path.basename(VIDEO_FILE)}")
    
    # Try to find any saved token
    token_files = [
        '/home/clawdbot/.openclaw/workspace/.youtube_token.json',
        '/home/clawdbot/.openclaw/workspace/.youtube_device_token.json',
        '/home/clawdbot/.openclaw/workspace/.google_token.json'
    ]
    
    creds = None
    for token_file in token_files:
        if os.path.exists(token_file):
            print(f"\n→ Found token: {os.path.basename(token_file)}")
            try:
                with open(token_file, 'r') as f:
                    token_data = json.load(f)
                
                creds = Credentials.from_authorized_user_info(
                    token_data,
                    scopes=['https://www.googleapis.com/auth/youtube.upload']
                )
                
                if creds.valid:
                    print(f"✓ Token is valid")
                    break
                    
            except Exception as e:
                print(f"⚠ Token error: {e}")
                creds = None
    
    if not creds:
        print(f"\n✗ No valid credentials found")
        print(f"\nCreated upload script saved to:")
        print(f"  {VIDEO_FILE}")
        print(f"\nManually authorize with:")
        print(f"  python3 /home/clawdbot/.openclaw/workspace/youtube_device_auth.py")
        return False
    
    # Upload
    print(f"\n→ Building YouTube client...")
    youtube = build('youtube', 'v3', credentials=creds)
    
    body = {
        'snippet': {
            'title': 'The Job Interview - A Dark Story | AI Story',
            'description': '''I got hired in 3 minutes. That should've been my first warning.

A short dark fiction story about a suspicious job interview that leads to a terrifying discovery.

This is a work of fiction created for entertainment purposes using AI technology. All characters and events are entirely fictional.

Subscribe for more AI-generated stories. New videos every week.

#storytelling #horror #shortfilm #thriller #darkfiction #AI''',
            'tags': ['storytelling', 'horror', 'shortfilm', 'thriller', 'darkstory', 'creepy', 'mystery', 'AI', 'scary', 'fiction'],
            'categoryId': '24',
            'defaultLanguage': 'en'
        },
        'status': {
            'privacyStatus': 'public',
            'madeForKids': False
        }
    }
    
    print(f"→ Uploading video ({os.path.getsize(VIDEO_FILE)/1024:.1f}KB)...")
    
    media = MediaFileUpload(VIDEO_FILE, chunksize=-1, resumable=True)
    request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)
    
    response = None
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                pct = int(status.progress() * 100)
                print(f"  {pct}%...", end='\r')
        except Exception as e:
            print(f"\n✗ Error: {e}")
            return False
    
    if response and 'id' in response:
        vid_id = response['id']
        
        print(f"\n\n" + "="*70)
        print(f"✓✓✓ UPLOADED! ✓✓✓")
        print(f"="*70)
        print(f"\n📺 https://youtu.be/{vid_id}")
        print(f"\n" + "="*70 + "\n")
        
        return True
    
    print(f"\n✗ Invalid response")
    return False

if __name__ == '__main__':
    try:
        ok = try_upload()
        sys.exit(0 if ok else 1)
    except Exception as e:
        print(f"\n✗ {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

