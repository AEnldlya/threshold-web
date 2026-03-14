#!/usr/bin/env python3
"""
Post video to Instagram and TikTok via Buffer API.
"""

import requests
import json
import os

BUFFER_TOKEN = "mbA4C_zaZdg1AdIVUrIcGDq1s47iPMLdp0NwkblKs-S"
VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_ANIMATED.mp4'

BASE_URL = "https://api.bufferapp.com/1"

def get_profiles():
    """Get connected social media profiles."""
    print("[1] Fetching your connected profiles...")
    
    url = f"{BASE_URL}/profiles.json"
    headers = {"Authorization": f"Bearer {BUFFER_TOKEN}"}
    
    resp = requests.get(url, headers=headers)
    
    if resp.status_code == 200:
        profiles = resp.json()
        print(f"✓ Found {len(profiles)} profiles:")
        for p in profiles:
            print(f"  - {p.get('service')}: {p.get('display_name')}")
        return profiles
    else:
        print(f"✗ Error: {resp.status_code}")
        print(resp.text)
        return []

def post_to_instagram(profile_id, video_path):
    """Post to Instagram via Buffer."""
    print("\n[2] Posting to Instagram...")
    
    url = f"{BASE_URL}/updates/create.json"
    headers = {"Authorization": f"Bearer {BUFFER_TOKEN}"}
    
    with open(video_path, 'rb') as f:
        files = {'media': f}
        data = {
            'profile_ids[]': profile_id,
            'text': 'I got hired in 3 minutes. That should\'ve been my first warning. #storytelling #horror #ai #darkstory',
            'shorten': 'true'
        }
        
        resp = requests.post(url, headers=headers, data=data, files=files)
    
    if resp.status_code == 200:
        result = resp.json()
        print(f"✓ Posted to Instagram!")
        print(f"  Update ID: {result.get('id')}")
        return True
    else:
        print(f"✗ Error: {resp.status_code}")
        print(resp.text)
        return False

def post_to_tiktok(profile_id, video_path):
    """Post to TikTok via Buffer."""
    print("\n[3] Posting to TikTok...")
    
    url = f"{BASE_URL}/updates/create.json"
    headers = {"Authorization": f"Bearer {BUFFER_TOKEN}"}
    
    with open(video_path, 'rb') as f:
        files = {'media': f}
        data = {
            'profile_ids[]': profile_id,
            'text': 'I got hired in 3 minutes. That should\'ve been my first warning. #storytelling #horror #ai #darkstory #thriller #mystery',
            'shorten': 'true'
        }
        
        resp = requests.post(url, headers=headers, data=data, files=files)
    
    if resp.status_code == 200:
        result = resp.json()
        print(f"✓ Posted to TikTok!")
        print(f"  Update ID: {result.get('id')}")
        return True
    else:
        print(f"✗ Error: {resp.status_code}")
        print(resp.text)
        return False

def main():
    print("="*70)
    print("POSTING VIA BUFFER API")
    print("="*70 + "\n")
    
    # Get profiles
    profiles = get_profiles()
    
    if not profiles:
        print("✗ No profiles found. Make sure to connect accounts in Buffer.")
        return False
    
    # Find Instagram and TikTok profiles
    ig_profile = None
    tt_profile = None
    
    for p in profiles:
        if p.get('service') == 'instagram':
            ig_profile = p.get('id')
            print(f"\n✓ Found Instagram: {p.get('display_name')}")
        elif p.get('service') == 'tiktok':
            tt_profile = p.get('id')
            print(f"✓ Found TikTok: {p.get('display_name')}")
    
    # Post to each platform
    results = []
    
    if ig_profile:
        results.append(post_to_instagram(ig_profile, VIDEO_FILE))
    else:
        print("\n⚠ Instagram profile not found in Buffer")
    
    if tt_profile:
        results.append(post_to_tiktok(tt_profile, VIDEO_FILE))
    else:
        print("\n⚠ TikTok profile not found in Buffer")
    
    # Summary
    print("\n" + "="*70)
    if all(results):
        print("✓✓✓ ALL POSTS SENT ✓✓✓")
        print("="*70)
        print("\nYour video is now scheduled on:")
        if ig_profile:
            print("  📸 Instagram")
        if tt_profile:
            print("  🎵 TikTok")
        print("\nCheck Buffer dashboard to confirm posting times.")
        return True
    else:
        print("⚠ Some posts failed - check details above")
        print("="*70)
        return False

if __name__ == '__main__':
    main()

