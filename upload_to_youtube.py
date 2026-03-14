#!/usr/bin/env python3
"""
Upload story video to YouTube using OAuth2 authentication.
"""

import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# YouTube API setup
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate_youtube():
    """Authenticate with YouTube API."""
    cred_file = '.gmail_credentials.json'
    token_file = '.youtube_token.json'
    
    # Check if we have a saved token
    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            creds_data = json.load(f)
        
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        
        creds = Credentials.from_authorized_user_info(creds_data, scopes=SCOPES)
        
        # Refresh if needed
        if creds.expired:
            creds.refresh(Request())
            with open(token_file, 'w') as f:
                f.write(creds.to_json())
        
        return creds
    
    # Otherwise, do OAuth flow
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        cred_file, scopes=SCOPES)
    
    try:
        creds = flow.run_local_server(port=0, open_browser=True)
    except:
        # Fallback for headless
        auth_url, _ = flow.authorization_url()
        print(f"\n🔗 Authorize here:\n{auth_url}\n")
        redirect_url = input("Paste redirect URL: ").strip()
        code = redirect_url.split('code=')[1].split('&')[0] if 'code=' in redirect_url else None
        
        if not code:
            print("❌ No auth code found")
            return None
        
        creds = flow.fetch_token(code=code)
    
    # Save token
    with open(token_file, 'w') as f:
        f.write(creds.to_json())
    
    return creds

def upload_video(video_file, title, description, tags, category_id="22", privacy_status="public"):
    """Upload video to YouTube."""
    
    creds = authenticate_youtube()
    if not creds:
        print("❌ Authentication failed")
        return None
    
    youtube = googleapiclient.discovery.build(
        YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=creds)
    
    print(f"📤 Uploading {video_file}...")
    
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": category_id,
                "defaultLanguage": "en",
                "defaultAudioLanguage": "en"
            },
            "status": {
                "privacyStatus": privacy_status,
                "madeForKids": False
            }
        },
        media_body=googleapiclient.http.MediaFileUpload(
            video_file, chunksize=-1, resumable=True)
    )
    
    response = None
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print(f"  Upload {int(status.progress() * 100)}%")
        except googleapiclient.errors.HttpError as e:
            print(f"❌ Upload error: {e}")
            return None
    
    video_id = response['id']
    print(f"\n✅ Upload complete!")
    print(f"Video ID: {video_id}")
    print(f"URL: https://www.youtube.com/watch?v={video_id}")
    
    return video_id

if __name__ == '__main__':
    video_file = "story_video_1_CINEMATIC.mp4"
    
    if not os.path.exists(video_file):
        print(f"❌ Video file not found: {video_file}")
        exit(1)
    
    title = "The Job Interview - A Dark Story | AI Story"
    description = """
I got hired in 3 minutes. That should've been my first warning.

A short dark fiction story about a suspicious job interview that leads to a terrifying discovery.

This is a work of fiction created for entertainment purposes using AI technology. All characters and events are entirely fictional.

---

📌 Subscribe for more AI-generated stories
🎬 New videos every week
💬 What would you have done?

#storytelling #horror #shortfilm #thriller #darkfiction #AI
"""
    
    tags = [
        "storytelling",
        "horror",
        "shortfilm", 
        "thriller",
        "darkstory",
        "creepy",
        "mystery",
        "AI",
        "scary",
        "fiction"
    ]
    
    video_id = upload_video(video_file, title, description, tags, privacy_status="public")
    
    if video_id:
        print(f"\n🎉 Success! Video is now on YouTube")
        print(f"Share: https://youtu.be/{video_id}")
