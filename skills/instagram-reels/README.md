# Instagram Reels Skill

Extract design inspiration and analyze patterns from Instagram reels for web development.

## Features

- ✅ Fetch reel metadata (creator, description, likes, comments)
- ✅ Download video and thumbnail files
- ✅ Extract design patterns (animations, colors, typography, layout)
- ✅ Batch process multiple reels concurrently
- ✅ Local caching to avoid re-fetching
- ✅ Export analysis to DESIGN_REFERENCES.md format
- ✅ Error handling (private reels, deleted content, rate limits)

## Installation

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Install the skill**:
```bash
mkdir -p ~/.openclaw/workspace/skills/instagram-reels
cd ~/.openclaw/workspace/skills/instagram-reels
git clone https://clawhub.com/instagram-reels .
# or copy this directory
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install Playwright browsers**:
```bash
playwright install chromium
```

4. **Configure environment** (optional):
```bash
cp .env.example .env
# Edit .env with your Instagram credentials (if needed)
```

## Configuration

Create `.env` file in the skill directory:

```env
# Instagram Credentials (optional - public reels don't need these)
INSTAGRAM_USERNAME=optional_username
INSTAGRAM_PASSWORD=optional_password

# Cache Configuration
CACHE_DIR=~/.openclaw/workspace/.cache/instagram-reels
TEMP_DIR=/tmp/instagram-reels

# Download Configuration
MAX_CONCURRENT_DOWNLOADS=3
REQUEST_DELAY_SECONDS=2
RATE_LIMIT_BACKOFF_SECONDS=60
```

## Quick Start

### Fetch a Single Reel

```python
from skills.instagram_reels import InstagramReelsSkill

skill = InstagramReelsSkill()

# Fetch reel metadata
result = await skill.fetch_reel(
    url="https://www.instagram.com/reel/DUHmsKkjZw0/",
    include_image=True,
    extract_analysis=True
)

print(result)
# Output:
# {
#   "success": true,
#   "reel_id": "DUHmsKkjZw0",
#   "creator": "design_inspiration",
#   "description": "Beautiful fade-in animation...",
#   "likes": 12500,
#   "comments": 342,
#   "design_analysis": {
#     "animations": ["fade-in", "slide-up"],
#     "layout": "hero",
#     "colors": ["#1a1a1a", "#ffffff"],
#     ...
#   }
# }
```

### Batch Fetch Multiple Reels

```python
urls = [
    "https://www.instagram.com/reel/DUHmsKkjZw0/",
    "https://www.instagram.com/reel/DUplhdqAbNt/",
    "https://www.instagram.com/reel/ABC123/"
]

result = await skill.fetch_reels_batch(
    urls=urls,
    concurrent_limit=3,
    extract_analysis=True
)

print(f"Fetched {result['successful']} reels successfully")
```

### Save Analysis to Markdown

```python
# Save single reel to DESIGN_REFERENCES.md
await skill.save_reel_to_markdown(
    reel_id="DUHmsKkjZw0",
    creator="design_inspiration",
    design_analysis=result['design_analysis'],
    description="Beautiful fade-in animation on hero section",
    custom_notes="Perfect for landing page inspiration"
)
```

## Command Line Interface

### Fetch a Reel
```bash
python instagram_reels.py fetch-reel \
    --url "https://www.instagram.com/reel/DUHmsKkjZw0/" \
    --extract-analysis \
    --format json
```

### Batch Fetch
```bash
python instagram_reels.py fetch-batch \
    --urls "https://www.instagram.com/reel/ABC123/" \
    --urls "https://www.instagram.com/reel/DEF456/" \
    --limit 3
```

### Save to Markdown
```bash
python instagram_reels.py save-to-md \
    --reel-id "DUHmsKkjZw0" \
    --creator "design_inspiration" \
    --description "Amazing hero animation" \
    --custom-notes "Reference for upcoming project"
```

### Cache Management
```bash
# View cache stats
python instagram_reels.py cache-status

# Clear all cache
python instagram_reels.py cache-clear
```

## Design Analysis Output

The skill extracts the following design patterns:

```json
{
  "animations": ["fade-in", "slide-up", "scale"],
  "layout": "hero",
  "typography": "sans-serif",
  "colors": ["#1a1a1a", "#ffffff", "#3b82f6"],
  "techniques": ["framer", "react", "gsap"],
  "ui_elements": ["button", "header", "card"],
  "interactions": ["hover", "click", "scroll"]
}
```

## Caching System

The skill automatically caches:

- **Metadata**: Reel information (creator, description, stats)
- **Images**: Thumbnail files (optimized JPEG)
- **Videos**: Full video files (if downloaded)

Cache location: `~/.openclaw/workspace/.cache/instagram-reels/`

### Cache Management
```python
# Check cache size
stats = await skill.cache_stats()
print(stats)
# {'total_entries': 42, 'total_size_mb': 1250.5}

# Clear cache
await skill.clear_cache()
```

## Error Handling

All functions return structured responses with error types:

```json
{
  "success": false,
  "error": "Error message",
  "error_type": "private_reel|deleted_reel|rate_limited|network_error"
}
```

### Error Types
- `private_reel`: Account or reel is private
- `deleted_reel`: Reel has been deleted
- `rate_limited`: Instagram rate limit hit
- `network_error`: Connection/timeout issues
- `parsing_error`: Failed to parse reel data
- `invalid_url`: Not a valid Instagram reel URL

## Architecture

### Core Modules

- **url_parser.py**: Parse and validate Instagram URLs
- **browser_manager.py**: Playwright browser session management
- **data_fetcher.py**: Extract reel metadata from page
- **media_downloader.py**: Download videos and images
- **design_analyzer.py**: Detect design patterns
- **markdown_formatter.py**: Format analysis for markdown
- **cache_manager.py**: Local caching system

## Performance Tips

### Optimize Batch Processing
```python
# Process 5 reels in batches of 2
result = await skill.fetch_reels_batch(
    urls=list_of_5_urls,
    concurrent_limit=2,  # Lower for rate limit safety
    extract_analysis=True
)
```

### Use Caching
```python
# First call fetches from Instagram
result = await skill.fetch_reel(url)

# Second call uses cache (much faster)
result = await skill.fetch_reel(url)
```

### Disable Unnecessary Features
```python
# Faster if you don't need video/images
result = await skill.fetch_reel(
    url=url,
    include_video=False,
    include_image=False,
    extract_analysis=True
)
```

## Limitations

### Rate Limiting
Instagram limits requests. The skill:
- Adds 2-5 second delays between requests
- Implements exponential backoff on errors
- Respects Instagram's rate limits

### Private Reels
Cannot access private accounts without credentials:
```python
# Set credentials in .env or manually
import os
os.environ['INSTAGRAM_USERNAME'] = 'your_username'
os.environ['INSTAGRAM_PASSWORD'] = 'your_password'
```

### Deleted Content
Returns error gracefully:
```python
result = await skill.fetch_reel(url)
if result['error_type'] == 'deleted_reel':
    print("This reel has been deleted")
```

## Security & Privacy

✅ **Safe Practices**:
- Credentials stored in .env (not in code)
- Respects Instagram ToS (personal research)
- Credits original creators
- Doesn't republish content

⚠️ **Important**:
- Don't use for commercial scraping
- Don't redistribute downloaded videos
- Respect creator copyright
- Use responsibly

## Troubleshooting

### Issue: Browser won't launch
```bash
# Install Playwright browsers
playwright install chromium

# Check if already installed
playwright install-deps
```

### Issue: Rate limited
The skill automatically handles this with backoff. If you get consistent rate limits:
- Increase `REQUEST_DELAY_SECONDS` in .env
- Reduce `MAX_CONCURRENT_DOWNLOADS`
- Wait a few hours before trying again

### Issue: Private reel error
Set your Instagram credentials in .env:
```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

### Issue: Memory usage high
The skill caches media files. Clean up:
```python
# Clear cache
await skill.clear_cache()

# Or clean files older than 7 days
cache = skill.cache_manager
cache.cleanup_old(days=7)
```

## Examples

### Example 1: Analyze Competitor Designs
```python
competitor_urls = [
    "https://www.instagram.com/reel/ABC123/",
    "https://www.instagram.com/reel/DEF456/",
    "https://www.instagram.com/reel/GHI789/"
]

result = await skill.fetch_reels_batch(
    urls=competitor_urls,
    extract_analysis=True
)

# Find most common animations
animations = {}
for reel in result['reels']:
    if reel.get('design_analysis'):
        for anim in reel['design_analysis'].get('animations', []):
            animations[anim] = animations.get(anim, 0) + 1

print("Most popular animations:", animations)
```

### Example 2: Build Design Reference Library
```python
design_reels = [
    "https://www.instagram.com/reel/ABC123/",
    # ... more reel URLs
]

for url in design_reels:
    result = await skill.fetch_reel(url, extract_analysis=True)
    
    if result['success']:
        # Save to markdown
        await skill.save_reel_to_markdown(
            reel_id=result['reel_id'],
            creator=result['creator'],
            design_analysis=result['design_analysis'],
            custom_notes="Saved from design analysis"
        )

# View all saved designs
with open(Path.home() / ".openclaw/workspace/DESIGN_REFERENCES.md") as f:
    print(f.read())
```

### Example 3: Extract Color Palettes
```python
result = await skill.fetch_reel(url, extract_analysis=True)

colors = result['design_analysis'].get('colors', [])
print(f"Color palette: {colors}")

# Save for use in projects
import json
with open('palette.json', 'w') as f:
    json.dump({'colors': colors}, f)
```

## Contributing

To improve the skill:

1. Test with various reel URLs
2. Report bugs and edge cases
3. Suggest new features
4. Improve design pattern detection

## License

MIT License - Use freely for personal and commercial projects

## Support

For issues:
1. Check [Troubleshooting](#troubleshooting)
2. Review [error types](#error-handling)
3. Check browser console logs
4. Verify .env configuration

---

**Happy designing! 🎨**

Built with ❤️ for web developers and designers discovering Instagram design inspiration.
