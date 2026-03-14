# Instagram Reels Skill - Development Prompt

**Goal**: Create an OpenClaw skill that allows Claude agents to fetch, analyze, and extract design insights from Instagram reels.

**Status**: Ready for implementation

---

## Skill Overview

### Name
`instagram-reels`

### Description
Fetch Instagram reel URLs, extract metadata, download video/images, and analyze design patterns for web development inspiration.

### Use Cases
1. **Design Analysis**: Extract animations, color schemes, typography from reels
2. **Trend Tracking**: Monitor design trends across reels
3. **Content Download**: Save reel videos or screenshots locally
4. **Metadata Extraction**: Get description, likes, comments, creator info
5. **Batch Processing**: Analyze multiple reels at once

---

## Technical Architecture

### Dependencies Required
```
instagrapi >= 2.0.0  # Instagram private API (most reliable)
OR
instagram-scraper >= 1.12.0  # Alternative: public API
OR
playwright >= 1.40.0  # Browser automation (most robust)
```

### Recommended Approach
**Use Playwright browser automation** because:
- ✅ Bypasses Instagram's anti-scraping detection
- ✅ Gets full page content (videos, images, metadata)
- ✅ Handles dynamic content loading
- ✅ Works reliably across updates
- ⚠️ Slower but more stable than API-based approaches

---

## Skill Commands

### 1. `fetch_reel`
**Purpose**: Get metadata from a single reel URL

**Input**:
```python
{
  "url": "https://www.instagram.com/reel/DUHmsKkjZw0/?igsh=YTQ4YzNnNG50OGVt",
  "include_video": False,  # Download video file?
  "include_image": True,   # Download thumbnail?
  "extract_analysis": True # Run design analysis?
}
```

**Output**:
```json
{
  "success": true,
  "reel_id": "DUHmsKkjZw0",
  "creator": "design_inspiration",
  "description": "Beautiful fade-in animation on hero section...",
  "likes": 12500,
  "comments": 342,
  "video_url": "/tmp/reel_DUHmsKkjZw0.mp4",
  "thumbnail_url": "/tmp/reel_DUHmsKkjZw0.jpg",
  "duration_seconds": 15,
  "design_analysis": {
    "animations": ["fade-in", "slide-up"],
    "colors": ["#1a1a1a", "#ffffff", "#3b82f6"],
    "typography": "Sans-serif, bold headers",
    "layout": "Hero section with centered text",
    "techniques": ["Framer Motion", "CSS transforms"]
  }
}
```

---

### 2. `fetch_reels_batch`
**Purpose**: Get metadata from multiple reel URLs

**Input**:
```python
{
  "urls": [
    "https://www.instagram.com/reel/DUHmsKkjZw0/?...",
    "https://www.instagram.com/reel/DUplhdqAbNt/?...",
    "https://www.instagram.com/reel/ABC123/?..."
  ],
  "include_videos": False,
  "concurrent_limit": 3  # Download 3 at a time
}
```

**Output**:
```json
{
  "success": true,
  "total_reels": 3,
  "successful": 3,
  "failed": 0,
  "reels": [
    { "reel_id": "DUHmsKkjZw0", "design_analysis": {...} },
    { "reel_id": "DUplhdqAbNt", "design_analysis": {...} },
    { "reel_id": "ABC123", "design_analysis": {...} }
  ]
}
```

---

### 3. `fetch_account_reels`
**Purpose**: Get all reels from an Instagram account

**Input**:
```python
{
  "username": "design_inspiration",
  "limit": 10,  # Get last 10 reels
  "include_videos": False,
  "extract_analysis": True
}
```

**Output**:
```json
{
  "success": true,
  "account": "design_inspiration",
  "followers": 125000,
  "bio": "UI/UX design patterns and animations",
  "reels_fetched": 10,
  "reels": [...]
}
```

---

### 4. `search_reel_by_hashtag`
**Purpose**: Search reels by hashtag

**Input**:
```python
{
  "hashtag": "webdesign",
  "limit": 5,
  "extract_analysis": True
}
```

**Output**:
```json
{
  "success": true,
  "hashtag": "webdesign",
  "reels_found": 5,
  "reels": [...]
}
```

---

### 5. `analyze_reel_video`
**Purpose**: Deep video analysis using computer vision

**Input**:
```python
{
  "video_path": "/tmp/reel_DUHmsKkjZw0.mp4",
  "extract_frames": True,
  "frame_count": 5,  # Extract 5 key frames
  "analyze_motion": True,  # Detect animations
  "analyze_colors": True,
  "analyze_text": True
}
```

**Output**:
```json
{
  "success": true,
  "video_path": "/tmp/reel_DUHmsKkjZw0.mp4",
  "duration": 15,
  "fps": 30,
  "frames_extracted": 5,
  "color_palette": [
    {"hex": "#1a1a1a", "rgb": [26, 26, 26], "prominence": 0.35},
    {"hex": "#ffffff", "rgb": [255, 255, 255], "prominence": 0.40},
    {"hex": "#3b82f6", "rgb": [59, 130, 246], "prominence": 0.25}
  ],
  "motion_detected": {
    "type": "fade-in + slide-up",
    "intensity": "smooth",
    "duration_ms": 800
  },
  "text_detected": [
    {"text": "Welcome", "font_style": "bold", "position": "center"}
  ]
}
```

---

### 6. `save_reel_analysis_to_md`
**Purpose**: Save analysis to DESIGN_REFERENCES.md format

**Input**:
```python
{
  "reel_id": "DUHmsKkjZw0",
  "creator": "design_inspiration",
  "design_analysis": {...},
  "custom_notes": "Perfect for hero section animations",
  "output_file": "/home/clawdbot/.openclaw/workspace/DESIGN_REFERENCES.md"
}
```

**Output**:
```json
{
  "success": true,
  "entry_added": true,
  "file": "DESIGN_REFERENCES.md",
  "entry_format": "### [Date] - [Creator] - [Topic]\n\n**What I Found**: ...\n**Why It's Relevant**: ...\n**Implementation Notes**: ...\n**Link**: ...\n**Status**: [ ] Todo"
}
```

---

## Implementation Strategy

### Phase 1: Core Infrastructure
1. **Browser Session Manager**
   - Maintain Instagram session
   - Handle login if needed
   - Manage cookies/cache

2. **URL Parser**
   - Extract reel ID from URL
   - Validate Instagram URLs
   - Handle URL variations

3. **Data Fetcher**
   - Load reel page with Playwright
   - Extract JSON metadata from page
   - Parse video/image URLs

### Phase 2: Media Download
1. **Video Downloader**
   - Download MP4 from reel
   - Save to temp directory
   - Handle errors (private, deleted, etc.)

2. **Thumbnail Extractor**
   - Capture screenshot of reel
   - Save as JPEG
   - Size optimization

### Phase 3: Analysis Engine
1. **Design Pattern Recognition**
   - Detect animations (fade, slide, rotate, etc.)
   - Extract color palette
   - Identify typography
   - Recognize layout patterns

2. **Computer Vision**
   - Frame extraction
   - Motion detection
   - Text recognition (OCR)
   - Color analysis

### Phase 4: Markdown Integration
1. **Format Conversion**
   - Convert analysis to DESIGN_REFERENCES.md format
   - Create timestamped entries
   - Add links and metadata

---

## File Structure

```
~/.openclaw/workspace/skills/instagram-reels/
├── SKILL.md                          # Skill metadata
├── README.md                         # Documentation
├── instagram_reels.py                # Main CLI
├── src/
│   ├── __init__.py
│   ├── browser_manager.py            # Playwright browser control
│   ├── url_parser.py                 # Parse Instagram URLs
│   ├── data_fetcher.py               # Fetch reel metadata
│   ├── media_downloader.py           # Download videos/images
│   ├── design_analyzer.py            # Analyze design patterns
│   ├── video_analyzer.py             # Computer vision analysis
│   ├── markdown_formatter.py         # Format for DESIGN_REFERENCES.md
│   └── cache_manager.py              # Local cache of downloaded reels
├── references/
│   ├── playwright-guide.md           # Playwright setup
│   ├── color-analysis.md             # Color palette extraction
│   ├── motion-detection.md           # Animation detection
│   └── ocr-setup.md                  # Text recognition
├── examples/
│   ├── example_reel_fetch.py         # Example: fetch single reel
│   ├── example_batch_fetch.py        # Example: batch fetch
│   ├── example_account_fetch.py      # Example: fetch account reels
│   └── example_analysis.py           # Example: analyze video
└── requirements.txt
```

---

## Dependencies

### Required
```
playwright>=1.40.0           # Browser automation
pillow>=10.0.0              # Image processing
requests>=2.31.0            # HTTP requests
python-dotenv>=1.0.0        # Environment variables
```

### Optional (for advanced features)
```
opencv-python>=4.8.0        # Computer vision
pytesseract>=0.3.10         # Text recognition
colorspacious>=1.1.1        # Advanced color analysis
scikit-image>=0.21.0        # Image processing
```

---

## Usage Example (for agents)

```python
from skills.instagram_reels import instagram_reels

# Fetch a single reel
result = instagram_reels.fetch_reel(
    url="https://www.instagram.com/reel/DUHmsKkjZw0/",
    include_video=False,
    extract_analysis=True
)

# Analyze multiple reels at once
results = instagram_reels.fetch_reels_batch(
    urls=[
        "https://www.instagram.com/reel/DUHmsKkjZw0/",
        "https://www.instagram.com/reel/DUplhdqAbNt/"
    ],
    extract_analysis=True
)

# Save to DESIGN_REFERENCES.md
instagram_reels.save_reel_analysis_to_md(
    reel_id=result['reel_id'],
    creator=result['creator'],
    design_analysis=result['design_analysis'],
    custom_notes="Great hero animation example"
)
```

---

## Limitations & Workarounds

### Limitation 1: Instagram Rate Limiting
**Problem**: Instagram blocks rapid requests
**Solution**:
- Add random delays between requests (2-5 seconds)
- Implement exponential backoff on 429 errors
- Cache results locally to avoid re-fetching

### Limitation 2: Private/Deleted Reels
**Problem**: Can't access private accounts or deleted reels
**Solution**:
- Return error with "private_account" or "deleted_reel" flag
- Don't fail silently
- Suggest checking URL manually

### Limitation 3: Video Processing
**Problem**: Large video files slow down analysis
**Solution**:
- Download only first 30 seconds of reel
- Extract key frames instead of full analysis
- Use concurrent processing for multiple reels

### Limitation 4: Metadata Extraction
**Problem**: Instagram often changes HTML structure
**Solution**:
- Parse JSON embedded in page first
- Fall back to HTML scraping if needed
- Maintain fallback parsing logic

---

## Security Considerations

### Instagram Terms of Service
⚠️ Scraping Instagram violates ToS. However:
- Use only for personal/business research (not redistribution)
- Respect rate limits
- Don't republish content without credit
- Use browser automation (less detectable than API scraping)

### Credentials
- ❌ Do NOT store Instagram login credentials in code
- ✅ Use environment variables or .env file
- ✅ Prefer anonymous browsing (no login needed for public reels)

### Data Privacy
- Only save analysis (not full video/images in repos)
- Respect creator copyright
- Link back to original reel
- Don't modify or claim as own

---

## Testing

### Unit Tests
```python
def test_url_parser():
    """Test parsing various Instagram URL formats"""
    
def test_fetch_reel_valid():
    """Test fetching a valid public reel"""
    
def test_fetch_reel_private():
    """Test error handling for private reels"""
    
def test_design_analysis():
    """Test design pattern recognition"""
    
def test_color_extraction():
    """Test color palette extraction"""
```

### Integration Tests
```python
def test_full_workflow():
    """Test: Fetch reel → Download video → Analyze → Save to markdown"""
```

---

## Success Criteria

✅ **Skill is ready when**:
1. Can fetch metadata from Instagram reel URL
2. Can download video and thumbnail without errors
3. Can extract and analyze design patterns (colors, animations, layout)
4. Can save analysis to DESIGN_REFERENCES.md format
5. Can batch process multiple reels concurrently
6. Handles errors gracefully (private, deleted, rate-limited)
7. Respects Instagram rate limits (not blacklisted)
8. Works with various reel URL formats

---

## Future Enhancements

### Phase 2
- [ ] Store analyzed reels in local SQLite database
- [ ] Track design trends over time (most common animations, colors)
- [ ] Recommendation engine: "Reels similar to this one"
- [ ] Export reports: "Top 10 animations this week"

### Phase 3
- [ ] Real-time Instagram account monitoring
- [ ] Scheduled fetching (check account every day)
- [ ] Webhook notifications when new reel matches criteria
- [ ] Integration with website builder (auto-apply patterns)

### Phase 4
- [ ] AI-powered caption analysis (extract design tips from reel text)
- [ ] Clone detected animations to code
- [ ] Generate CSS/Framer Motion code from reel analysis
- [ ] Auto-generate design briefs from reel collections

---

## Implementation Checklist

**Core Implementation**:
- [ ] Browser manager (Playwright setup)
- [ ] URL parser (extract reel ID, validate)
- [ ] Data fetcher (extract JSON metadata)
- [ ] Media downloader (video + thumbnail)
- [ ] Design analyzer (detect patterns)
- [ ] Error handling (private, deleted, rate limits)
- [ ] Markdown formatter (save to DESIGN_REFERENCES.md)

**Testing**:
- [ ] Unit tests (each component)
- [ ] Integration tests (full workflow)
- [ ] Error case testing (private reels, rate limits)
- [ ] Concurrent request testing (batch processing)

**Documentation**:
- [ ] README with examples
- [ ] Setup guide (Playwright, dependencies)
- [ ] CLI usage examples
- [ ] API reference

**Performance**:
- [ ] Caching (avoid re-fetching)
- [ ] Concurrent downloads (parallel processing)
- [ ] Memory optimization (don't load full videos in RAM)
- [ ] Rate limit handling (delays, backoff)

---

## Next Steps

1. **Create skill directory**: `~/.openclaw/workspace/skills/instagram-reels/`
2. **Implement Phase 1**: Browser manager + data fetcher
3. **Test with real reels**: Verify metadata extraction works
4. **Add analysis engine**: Design pattern recognition
5. **Integrate with DESIGN_REFERENCES.md**: Save findings automatically
6. **Package and publish**: Share on ClawHub

---

## Questions for Implementation

1. **Authentication**: Should skill support private account access (requires Instagram login)?
2. **Storage**: Where to store downloaded videos? (Temp? Local cache?)
3. **Concurrency**: How many reels to download in parallel? (Default: 3)
4. **Analysis Depth**: Simple (colors + text) or advanced (motion + OCR)? (Default: advanced)
5. **Error Handling**: Fail silently or raise exceptions? (Default: raise with details)

---

**Skill Concept**: Complete and ready for development! 🚀

Follow this prompt to create a production-ready Instagram Reels skill for OpenClaw.
