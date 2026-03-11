#!/usr/bin/env python3
"""
YouTube upload - minimal, robust, works.
"""
import os, sys, json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

TOKEN_FILE = '/home/clawdbot/.openclaw/workspace/.youtube_token.json'
VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_1_CINEMATIC.mp4'

def upload():
    # Try to load any existing valid token
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE) as f:
                token_data = json.load(f)
            creds = Credentials.from_authorized_user_info(token_data)
            if creds.valid:
                print("Using existing token")
            elif creds.refresh_token:
                print("Refreshing token...")
                creds.refresh(Request())
                with open(TOKEN_FILE, 'w') as f:
                    json.dump(json.loads(creds.to_json()), f)
            else:
                creds = None
        except:
            creds = None
    else:
        creds = None
    
    if not creds:
        print("No credentials found. Please run:")
        print("  python3 /home/clawdbot/.openclaw/workspace/youtube_final_upload.py")
        return False
    
    print("Uploading to YouTube...")
    youtube = build('youtube', 'v3', credentials=creds)
    
    body = {
        'snippet': {
            'title': 'The Job Interview - A Dark Story | AI Story',
            'description': 'Dark fiction story. #storytelling #horror #AI',
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
            print(f"  {int(s.progress()*100)}%", end='\r')
    
    vid = resp['id']
    print(f"\nDone: https://youtu.be/{vid}")
    return True

if __name__ == '__main__':
    upload()

