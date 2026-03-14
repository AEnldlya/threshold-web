#!/usr/bin/env python3
"""
YouTube upload handler - clean, robust, takes its time.
"""

import os
import json
import sys
import time
import socket
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Config
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CRED_FILE = '/home/clawdbot/.openclaw/workspace/.gmail_credentials.json'
TOKEN_FILE = '/home/clawdbot/.openclaw/workspace/.youtube_token.json'
VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_1_CINEMATIC.mp4'

# Global
auth_code = None
server = None

def find_port():
    """Find available port."""
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

CALLBACK_PORT = find_port()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        q = parse_qs(urlparse(self.path).query)
        if 'code' in q:
            auth_code = q['code'][0]
            print(f"\n✓ Got auth code")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Done</h1>')
        else:
            self.send_response(400)
            self.end_headers()
    def log_message(self, *a): pass

def start_server():
    global server
    print(f"→ Server starting on port {CALLBACK_PORT}...")
    server = HTTPServer(('127.0.0.1', CALLBACK_PORT), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    time.sleep(0.5)
    print(f"✓ Server ready")

def authorize():
    global auth_code
    print("\n" + "="*70)
    print("AUTHORIZATION")
    print("="*70)
    
    flow = InstalledAppFlow.from_client_secrets_file(CRED_FILE, scopes=SCOPES)
    auth_url, _ = flow.authorization_url()
    
    print(f"\nOPEN THIS LINK:\n{auth_url}\n")
    print("="*70)
    
    print(f"\nWaiting (10 min timeout)...")
    
    for i in range(600):
        if auth_code:
            break
        time.sleep(1)
        if (i+1) % 60 == 0:
            print(f"  {i+1}s...")
    
    if not auth_code:
        print("✗ Timeout")
        return None
    
    print(f"→ Getting credentials...")
    creds = flow.fetch_token(code=auth_code)
    
    with open(TOKEN_FILE, 'w') as f:
        json.dump(creds, f)
    print(f"✓ Credentials saved")
    
    return creds

def upload(creds):
    print("\n" + "="*70)
    print("UPLOADING")
    print("="*70 + "\n")
    
    yt = build('youtube', 'v3', credentials=creds)
    
    body = {
        'snippet': {
            'title': 'The Job Interview - A Dark Story | AI Story',
            'description': 'Dark fiction story. #storytelling #horror #AI',
            'tags': ['storytelling', 'horror', 'shortfilm', 'thriller', 'AI'],
            'categoryId': '24'
        },
        'status': {
            'privacyStatus': 'public',
            'madeForKids': False
        }
    }
    
    media = MediaFileUpload(VIDEO_FILE, chunksize=-1, resumable=True)
    req = yt.videos().insert(part='snippet,status', body=body, media_body=media)
    
    print(f"→ Uploading {os.path.getsize(VIDEO_FILE)/1024:.1f}KB...")
    
    resp = None
    while resp is None:
        s, resp = req.next_chunk()
        if s:
            print(f"  {int(s.progress()*100)}%...", end='\r')
    
    vid_id = resp['id']
    
    print(f"\n\n" + "="*70)
    print(f"✓ SUCCESS!")
    print(f"="*70)
    print(f"\nVideo: https://youtu.be/{vid_id}\n")
    print("="*70 + "\n")
    
    return True

def main():
    print("\n" + "="*70)
    print("YOUTUBE UPLOAD")
    print("="*70 + "\n")
    
    if not os.path.exists(CRED_FILE):
        print(f"✗ No credentials: {CRED_FILE}")
        return False
    
    if not os.path.exists(VIDEO_FILE):
        print(f"✗ No video: {VIDEO_FILE}")
        return False
    
    print(f"✓ Files ready")
    print(f"  Video: {os.path.basename(VIDEO_FILE)}")
    
    start_server()
    creds = authorize()
    
    if not creds:
        print("✗ Auth failed")
        return False
    
    return upload(creds)

if __name__ == '__main__':
    try:
        ok = main()
        sys.exit(0 if ok else 1)
    except Exception as e:
        print(f"✗ {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        if server:
            server.shutdown()
