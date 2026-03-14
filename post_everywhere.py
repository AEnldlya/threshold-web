#!/usr/bin/env python3
"""
Post video to Instagram, TikTok, YouTube automatically.
"""

import os
import sys

VIDEO_FILE = '/home/clawdbot/.openclaw/workspace/story_video_ANIMATED.mp4'

print("="*70)
print("POSTING TO SOCIAL MEDIA")
print("="*70)

# Try Instagram via instagrapi
print("\n[INSTAGRAM] Installing instagrapi...")
os.system("pip install instagrapi -q")

try:
    from instagrapi import Client
    
    print("[INSTAGRAM] Attempting upload...")
    
    # This requires credentials - try to use them
    ig = Client()
    ig.login('andy.li.zhang2010@gmail.com', 'PASSWORD_HERE')  # Would need actual password
    
    media = ig.video_upload(
        VIDEO_FILE,
        caption="I got hired in 3 minutes. That should've been my first warning. #storytelling #horror #ai"
    )
    
    print(f"[INSTAGRAM] ✓ Posted: https://instagram.com/p/{media.id}/")
    
except Exception as e:
    print(f"[INSTAGRAM] ✗ Need credentials: {e}")

# Try TikTok
print("\n[TIKTOK] Attempting upload...")
try:
    from TikTokApi import TikTokApi
    
    api = TikTokApi()
    # Would need auth
    print("[TIKTOK] ✗ Needs TikTok API setup")
    
except:
    print("[TIKTOK] ✗ TikTokApi not available")

# Try YouTube (manual link)
print("\n[YOUTUBE] Since OAuth failed...")
print("Use: https://www.youtube.com/upload")
print("Upload file: " + VIDEO_FILE)

# Try Rumble (no auth needed)
print("\n[RUMBLE] No auth needed alternative...")
print("Go to: https://rumble.com/upload")
print("Upload: " + VIDEO_FILE)

print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print(f"\nVideo file ready: {VIDEO_FILE}")
print(f"Size: {os.path.getsize(VIDEO_FILE)/1024:.1f}KB")
print("\nManual upload options:")
print("  • Instagram: instagram.com (Stories/Reels)")
print("  • TikTok: tiktok.com/upload")
print("  • YouTube: youtube.com/upload")
print("  • Rumble: rumble.com/upload (no auth)")

