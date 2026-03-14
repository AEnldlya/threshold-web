# Instagram Reels Skill

**ID**: `instagram-reels`

**Version**: `1.0.0`

**Author**: Claude Code (Agent Development)

**Description**: Fetch Instagram reel URLs, extract metadata, download video/images, and analyze design patterns for web development inspiration. Includes design pattern recognition, color palette extraction, and markdown export to DESIGN_REFERENCES.md.

## Features

- ✅ Fetch metadata from Instagram reel URLs
- ✅ Download video and thumbnail files
- ✅ Extract design patterns (colors, animations, typography, layout)
- ✅ Batch process multiple reels concurrently
- ✅ Account reel fetching (all reels from a user)
- ✅ Hashtag search functionality
- ✅ Deep video analysis with computer vision
- ✅ Export analysis to DESIGN_REFERENCES.md format
- ✅ Local caching to avoid re-fetching
- ✅ Robust error handling (private reels, deleted content, rate limits)

## Commands

### `fetch_reel`
Get metadata from a single reel URL
```bash
instagram_reels fetch_reel --url "https://www.instagram.com/reel/DUHmsKkjZw0/" --extract-analysis --include-video false
```

### `fetch_reels_batch`
Get metadata from multiple reel URLs
```bash
instagram_reels fetch_reels_batch --urls "url1" "url2" "url3" --concurrent-limit 3
```

### `fetch_account_reels`
Get all reels from an Instagram account
```bash
instagram_reels fetch_account_reels --username "design_inspiration" --limit 10 --extract-analysis
```

### `search_reel_by_hashtag`
Search reels by hashtag
```bash
instagram_reels search_reel_by_hashtag --hashtag "webdesign" --limit 5
```

### `analyze_reel_video`
Deep video analysis using computer vision
```bash
instagram_reels analyze_reel_video --video-path "/tmp/reel.mp4" --extract-frames 5 --analyze-motion --analyze-colors --analyze-text
```

### `save_reel_analysis_to_md`
Save analysis to DESIGN_REFERENCES.md format
```bash
instagram_reels save_reel_analysis_to_md --reel-id "DUHmsKkjZw0" --creator "design_inspiration" --output-file "DESIGN_REFERENCES.md"
```

## Requirements

- Python 3.8+
- Playwright >= 1.40.0
- Pillow >= 10.0.0
- requests >= 2.31.0
- python-dotenv >= 1.0.0
- opencv-python >= 4.8.0 (for video analysis)
- pytesseract >= 0.3.10 (for OCR)
- colorspacious >= 1.1.1 (for color analysis)

## Installation

1. Clone this skill from ClawHub or copy to ~/.openclaw/workspace/skills/instagram-reels/
2. Install dependencies: `pip install -r requirements.txt`
3. Install Playwright browsers: `playwright install chromium`
4. Configure environment (see README.md)

## Usage Example

```python
from skills.instagram_reels import instagram_reels

# Fetch a single reel
result = instagram_reels.fetch_reel(
    url="https://www.instagram.com/reel/DUHmsKkjZw0/",
    include_video=False,
    extract_analysis=True
)
print(result)

# Save to DESIGN_REFERENCES.md
instagram_reels.save_reel_analysis_to_md(
    reel_id=result['reel_id'],
    creator=result['creator'],
    design_analysis=result['design_analysis'],
    custom_notes="Great hero animation example"
)
```

## Configuration

Create `.env` file in skill root:
```
INSTAGRAM_USERNAME=optional_username
INSTAGRAM_PASSWORD=optional_password
CACHE_DIR=~/.openclaw/workspace/.cache/instagram-reels
TEMP_DIR=/tmp/instagram-reels
MAX_CONCURRENT_DOWNLOADS=3
REQUEST_DELAY_SECONDS=2
RATE_LIMIT_BACKOFF_SECONDS=60
```

## Limitations

- **Rate Limiting**: Instagram limits requests. Skill implements delays and backoff.
- **Private Reels**: Cannot access private accounts (requires manual access)
- **Deleted Reels**: Gracefully handles deleted content with error flags
- **Terms of Service**: Scraping Instagram violates ToS. Use for personal/research only, not redistribution.

## Error Handling

All functions return structured responses:
```json
{
  "success": true/false,
  "error": "error message if failed",
  "error_type": "private_reel|deleted_reel|rate_limited|network_error|parsing_error",
  "data": {...}
}
```

## Caching

Downloaded reels are cached locally to avoid re-fetching:
- Cache location: `~/.openclaw/workspace/.cache/instagram-reels/`
- Metadata cache: `.cache/metadata/`
- Video cache: `.cache/videos/`
- Image cache: `.cache/images/`

## Security

- ❌ Never store credentials in code
- ✅ Use environment variables for credentials
- ✅ Respects Instagram rate limits
- ✅ Credits original creators
- ✅ Doesn't modify or redistribute content

## Support

For issues, documentation, or contributions:
- See README.md for detailed guide
- Check examples/ for usage patterns
- Review references/ for technical details

---

**Ready to build websites?** Use this skill to find design inspiration and analyze trends before coding!
