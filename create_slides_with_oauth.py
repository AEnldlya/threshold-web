#!/usr/bin/env python3
"""
Create Google Slides with automatic OAuth callback handling.
"""

import json
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/presentations'
]

auth_code = None
server = None

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        
        # Parse the redirect URL
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        if 'code' in params:
            auth_code = params['code'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Success!</h1><p>Authorization complete. You can close this window.</p></body></html>')
            print("\n✅ Authorization code received!")
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Error</h1><p>No authorization code received.</p></body></html>')
    
    def log_message(self, format, *args):
        pass  # Suppress logging

def authenticate_and_create_slides():
    """Authenticate with Google and create Slides."""
    global auth_code, server
    
    cred_file = '.gmail_credentials.json'
    token_file = '.google_token.json'
    
    try:
        flow = InstalledAppFlow.from_client_secrets_file(cred_file, scopes=SCOPES)
        
        # Start local server to listen for OAuth callback
        PORT = 8080
        server = HTTPServer(('localhost', PORT), OAuthCallbackHandler)
        
        print(f"📡 Starting OAuth callback server on port {PORT}...")
        
        # Run server in background thread
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()
        
        # Generate auth URL
        auth_url, _ = flow.authorization_url()
        print(f"\n🔗 Click or open this link in your browser:\n")
        print(f"{auth_url}\n")
        
        # Wait for authorization (max 300 seconds)
        import time
        timeout = 300
        start = time.time()
        
        while auth_code is None and (time.time() - start) < timeout:
            time.sleep(1)
        
        if auth_code is None:
            print("❌ Authorization timeout - no code received")
            return False
        
        # Exchange code for token
        creds = flow.fetch_token(code=auth_code)
        
        # Save token
        with open(token_file, 'w') as f:
            f.write(json.dumps(creds))
        
        print(f"✅ Token saved to {token_file}")
        
        # Create Slides presentation
        slides_service = build('slides', 'v1', credentials=flow.credentials)
        drive_service = build('drive', 'v3', credentials=flow.credentials)
        
        print("\n📝 Creating Google Slides presentation...")
        
        presentation = {'title': 'Boston Campaign & Projects - March 2026'}
        result = slides_service.presentations().create(body=presentation).execute()
        
        presentation_id = result['presentationId']
        url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
        
        print(f"✅ Created presentation: {presentation_id}")
        
        # Share with Andy
        print(f"📤 Sharing with Andy.li.zhang2010@gmail.com...")
        
        permission = {
            'type': 'user',
            'role': 'editor',
            'emailAddress': 'Andy.li.zhang2010@gmail.com'
        }
        
        drive_service.permissions().create(
            fileId=presentation_id,
            body=permission
        ).execute()
        
        print(f"✅ Shared!")
        print(f"\n🎉 SUCCESS!")
        print(f"\n🔗 GOOGLE SLIDES LINK:\n{url}\n")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        if server:
            server.shutdown()

if __name__ == '__main__':
    print("=" * 60)
    print("Creating Google Slides with OAuth Authentication")
    print("=" * 60 + "\n")
    
    authenticate_and_create_slides()
