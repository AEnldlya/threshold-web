#!/usr/bin/env python3
"""
Clean YouTube upload with OAuth2 callback server.
Takes time, does it right.
"""

import os
import json
import sys
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Configuration
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CRED_FILE = '/home/clawdbot/.openclaw/workspace/.gmail_credentials.json'
TOKEN_FILE = '/home/clawdbot/.openclaw/workspace/.youtube_token.json'
VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_1_CINEMATIC.mp4'
# Use port 0 to let OS choose an available port
CALLBACK_PORT = 0

# Global state
auth_code = None
server = None

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """Handle OAuth2 callback."""
    
    def do_GET(self):
        global auth_code
        
        # Parse query parameters
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)
        
        if 'code' in params:
            auth_code = params['code'][0]
            print(f"\n✓ Authorization code received")
            
            # Send success response
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            html = '<html><body style="text-align:center;padding:50px;font-family:Arial"><h1>✓ Success</h1><p>Authorization complete. Uploading video...</p></body></html>'
            self.wfile.write(html.encode('utf-8'))
        else:
            # Error response
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Error: No authorization code</h1>')
    
    def log_message(self, format, *args):
        """Suppress HTTP server logging."""
        pass

def start_callback_server():
    """Start HTTP server for OAuth callback."""
    global server
    
    print(f"→ Starting callback server on localhost:{CALLBACK_PORT}...")
    
    server = HTTPServer(('127.0.0.1', CALLBACK_PORT), OAuthCallbackHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    
    time.sleep(1)
    print(f"✓ Server ready")

def get_auth_code():
    """Get authorization code via OAuth flow."""
    global auth_code
    
    print("\n" + "="*70)
    print("YOUTUBE AUTHORIZATION")
    print("="*70)
    
    print(f"\n→ Creating OAuth flow...")
    flow = InstalledAppFlow.from_client_secrets_file(CRED_FILE, scopes=SCOPES)
    
    print(f"→ Generating authorization URL...")
    auth_url, state = flow.authorization_url()
    
    print(f"\n" + "="*70)
    print("OPEN THIS LINK IN YOUR BROWSER:")
    print("="*70)
    print(f"\n{auth_url}\n")
    print("="*70)
    
    print(f"\n→ Waiting for authorization...")
    
    # Wait up to 10 minutes for user to authorize
    max_wait = 600
    elapsed = 0
    
    while auth_code is None and elapsed < max_wait:
        time.sleep(1)
        elapsed += 1
        
        # Print status every 30 seconds
        if elapsed % 30 == 0:
            remaining = max_wait - elapsed
            print(f"  ... waiting ({remaining}s remaining)")
    
    if auth_code is None:
        print(f"\n✗ Authorization timeout - no code received")
        return None, None
    
    print(f"✓ Authorization received\n")
    
    # Exchange code for credentials
    print(f"→ Exchanging code for credentials...")
    
    try:
        credentials = flow.fetch_token(code=auth_code)
        print(f"✓ Got credentials")
        return credentials, flow
    except Exception as e:
        print(f"✗ Error exchanging code: {e}")
        return None, None

def upload_video(credentials):
    """Upload video to YouTube."""
    
    print("\n" + "="*70)
    print("UPLOADING TO YOUTUBE")
    print("="*70)
    
    print(f"\n→ Building YouTube API client...")
    youtube = build('youtube', 'v3', credentials=credentials)
    
    print(f"→ Preparing video upload...")
    
    title = "The Job Interview - A Dark Story | AI Story"
    description = """I got hired in 3 minutes. That should've been my first warning.

A short dark fiction story about a suspicious job interview that leads to a terrifying discovery.

This is a work of fiction created for entertainment purposes using AI technology. All characters and events are entirely fictional.

---

📌 Subscribe for more AI-generated stories
🎬 New videos every week
💬 What would you have done?

#storytelling #horror #shortfilm #thriller #darkfiction #AI"""

    tags = [
        "storytelling", "horror", "shortfilm", "thriller", "darkstory",
        "creepy", "mystery", "AI", "scary", "fiction"
    ]
    
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '24',
            'defaultLanguage': 'en',
            'defaultAudioLanguage': 'en'
        },
        'status': {
            'privacyStatus': 'public',
            'madeForKids': False,
            'selfDeclaredMadeForKids': False
        }
    }
    
    print(f"  Title: {title}")
    print(f"  Tags: {', '.join(tags[:5])}...")
    
    media = MediaFileUpload(VIDEO_FILE, chunksize=-1, resumable=True)
    
    print(f"\n→ Uploading file ({os.path.getsize(VIDEO_FILE) / 1024:.1f} KB)...")
    
    request = youtube.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media
    )
    
    # Upload with progress
    response = None
    retry_count = 0
    max_retries = 3
    
    while response is None:
        try:
            status, response = request.next_chunk()
            
            if status:
                progress = int(status.progress() * 100)
                print(f"  {progress}% uploaded...", end='\r')
            
            retry_count = 0
            
        except Exception as e:
            retry_count += 1
            
            if retry_count > max_retries:
                print(f"\n✗ Upload failed after {max_retries} retries: {e}")
                return None
            
            print(f"\n⚠ Retry {retry_count}/{max_retries}: {e}")
            time.sleep(2 ** retry_count)
    
    if response and 'id' in response:
        video_id = response['id']
        print(f"\n✓ Upload complete!")
        return video_id
    else:
        print(f"\n✗ Invalid response: {response}")
        return None

def main():
    """Main upload flow."""
    
    print("\n" + "="*70)
    print("YOUTUBE VIDEO UPLOAD - TAKE YOUR TIME")
    print("="*70)
    
    # Validate files exist
    print(f"\n→ Checking files...")
    if not os.path.exists(CRED_FILE):
        print(f"✗ Credentials not found: {CRED_FILE}")
        return False
    
    if not os.path.exists(VIDEO_FILE):
        print(f"✗ Video not found: {VIDEO_FILE}")
        return False
    
    print(f"✓ Files ready")
    print(f"  Video: {os.path.basename(VIDEO_FILE)} ({os.path.getsize(VIDEO_FILE) / 1024:.1f} KB)")
    
    # Start callback server
    start_callback_server()
    
    # Get authorization
    credentials, flow = get_auth_code()
    
    if credentials is None:
        print(f"\n✗ Failed to get authorization")
        return False
    
    # Save token for future use
    print(f"\n→ Saving token for future use...")
    with open(TOKEN_FILE, 'w') as f:
        json.dump(credentials, f)
    print(f"✓ Token saved")
    
    # Upload video
    video_id = upload_video(credentials)
    
    if video_id:
        print(f"\n" + "="*70)
        print(f"SUCCESS!")
        print(f"="*70)
        print(f"\nVideo ID: {video_id}")
        print(f"\n📺 Watch: https://www.youtube.com/watch?v={video_id}")
        print(f"📱 Share: https://youtu.be/{video_id}")
        print(f"\n" + "="*70 + "\n")
        return True
    else:
        print(f"\n✗ Upload failed")
        return False

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        if server:
            server.shutdown()
