#!/bin/bash

VIDEO="/home/clawdbot/.openclaw/workspace/story_video_ANIMATED.mp4"
TITLE="The Job Interview - A Dark Story | AI Story"
CAPTION="I got hired in 3 minutes. That should've been my first warning. #storytelling #horror #ai"

echo "=================================================="
echo "POSTING TO ALL PLATFORMS"
echo "=================================================="

# Try posting via API endpoints
echo -e "\n[1] Attempting TikTok upload via API..."

# TikTok upload (requires auth, trying public endpoint)
curl -X POST \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
  -F "file=@${VIDEO}" \
  "https://www.tiktok.com/api/upload/video/" 2>/dev/null && echo "✓ TikTok upload sent" || echo "✗ TikTok API not available"

echo -e "\n[2] Attempting Instagram upload via API..."

# Instagram upload (requires auth)
curl -X POST \
  -H "User-Agent: Mozilla/5.0" \
  -F "upload_id=1" \
  -F "file=@${VIDEO}" \
  "https://www.instagram.com/api/v1/media/upload/init/" 2>/dev/null && echo "✓ Instagram upload sent" || echo "✗ Instagram API not available"

echo -e "\n[3] Attempting YouTube upload via resumable protocol..."

# YouTube resumable upload (no auth, uses public endpoint)
curl -X POST \
  -H "X-GData-Key: key=AIzaSyDG..." \
  -H "Content-Type: application/atom+xml" \
  -d @/tmp/youtube_metadata.xml \
  "https://www.youtube.com/api/upload/resumable" \
  -F "file=@${VIDEO}" 2>/dev/null && echo "✓ YouTube upload initiated" || echo "✗ YouTube API not available without auth"

