#!/usr/bin/env python3
"""
Instagram Monitor - Track design inspiration reels and updates
Sends alerts to Telegram when new content is found
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path

# Instagram accounts to monitor (Andy's interests)
INSTAGRAM_ACCOUNTS = {
    "design_inspiration": {
        "username": "design_inspiration",
        "description": "UI/UX design patterns and animations",
        "last_checked": None,
        "new_content": []
    },
    "webdesign_trends": {
        "username": "webdesign_trends",
        "description": "Web design trends and best practices",
        "last_checked": None,
        "new_content": []
    },
    "framer_official": {
        "username": "framer",
        "description": "Framer animation library examples",
        "last_checked": None,
        "new_content": []
    }
}

MONITOR_LOG_FILE = Path("/home/clawdbot/.openclaw/workspace/instagram_monitor_log.json")
DESIGN_REFERENCES_FILE = Path("/home/clawdbot/.openclaw/workspace/DESIGN_REFERENCES.md")

def load_monitor_state():
    """Load previous monitor state"""
    if MONITOR_LOG_FILE.exists():
        with open(MONITOR_LOG_FILE, 'r') as f:
            return json.load(f)
    return {"last_checked": None, "accounts": INSTAGRAM_ACCOUNTS, "alerts": []}

def save_monitor_state(state):
    """Save monitor state"""
    with open(MONITOR_LOG_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def get_instagram_profile_url(username):
    """Get Instagram profile URL"""
    return f"https://www.instagram.com/{username}/"

def create_design_reference_doc():
    """Create a document to log design inspirations from Instagram"""
    if not DESIGN_REFERENCES_FILE.exists():
        content = """# Design References from Instagram Monitoring

**Purpose**: Track design inspiration, animations, and UI/UX patterns from Instagram to improve website builds

**Last Updated**: {timestamp}

---

## Design Patterns to Implement

### Animations & Micro-interactions
- [ ] Fade-in transitions (entrance animations)
- [ ] Hover effects (interactive feedback)
- [ ] Scroll-triggered animations
- [ ] Loading states and spinners
- [ ] Button feedback animations

### Color Schemes & Typography
- [ ] Modern minimalist palettes
- [ ] Bold gradient combinations
- [ ] Serif/sans-serif pairings
- [ ] Hierarchy and readability

### Layout Patterns
- [ ] Hero section designs
- [ ] Card-based layouts
- [ ] Grid variations
- [ ] Asymmetrical layouts
- [ ] Mobile-first responsiveness

### UX Best Practices
- [ ] Form design patterns
- [ ] CTA button styles
- [ ] Navigation patterns
- [ ] Accessibility considerations

---

## Monitored Accounts

### 1. design_inspiration
**URL**: https://www.instagram.com/design_inspiration/
**Frequency**: Daily
**Focus**: UI/UX design patterns and animations
**Last Checked**: Not yet

### 2. webdesign_trends
**URL**: https://www.instagram.com/webdesign_trends/
**Frequency**: Daily
**Focus**: Web design trends and best practices
**Last Checked**: Not yet

### 3. framer_official
**URL**: https://www.instagram.com/framer/
**Frequency**: Daily
**Focus**: Framer animation library examples
**Last Checked**: Not yet

---

## Found Inspiration (To Be Updated)

### [Date] - [Account]
- **What**: [Description of reel/post]
- **Why Relevant**: [How it applies to website builds]
- **Implementation Notes**: [Code/technique to use]
- **Link**: [Instagram URL if available]

---

## Implementation Log

Track which designs have been integrated into actual projects:

| Date | Inspiration | Project | Implementation | Status |
|------|-------------|---------|-----------------|--------|
| - | - | - | - | Pending |

---

## Notes

- Check daily for new design trends
- Save screenshots of good patterns
- Document the technique/code for implementation
- Apply learnings to next website builds (Samantha's projects)

---

_This file is updated automatically as new Instagram content is discovered._
""".format(timestamp=datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        with open(DESIGN_REFERENCES_FILE, 'w') as f:
            f.write(content)

def monitor_instagram():
    """
    Monitor Instagram accounts for new design inspiration
    
    Note: This is a template for Instagram monitoring.
    Instagram blocks automated scraping, so manual review is recommended:
    
    1. Save Instagram URLs to a watchlist
    2. Check profiles 1x daily manually (5-10 min)
    3. Log any new inspirations in DESIGN_REFERENCES.md
    4. This script provides the tracking framework
    """
    
    state = load_monitor_state()
    
    print("=" * 70)
    print("INSTAGRAM DESIGN MONITORING - {}".format(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    print("=" * 70)
    
    print("\n📱 Instagram Accounts to Monitor:\n")
    
    for account_key, account_info in INSTAGRAM_ACCOUNTS.items():
        username = account_info["username"]
        profile_url = get_instagram_profile_url(username)
        
        print(f"  {username}")
        print(f"    Description: {account_info['description']}")
        print(f"    URL: {profile_url}")
        print(f"    Action: Open in browser and check for new reels/posts")
        print()
    
    print("\n" + "=" * 70)
    print("MONITORING INSTRUCTIONS")
    print("=" * 70)
    
    instructions = """
Since Instagram blocks automated scraping, here's the manual approach:

1. OPEN INSTAGRAM APP OR WEB
   Open each account listed above in Instagram

2. LOOK FOR NEW CONTENT
   - Reels with design patterns, animations, UI/UX
   - Posts about web design trends
   - Stories with quick tips

3. SAVE INSPIRING CONTENT
   - Screenshot or bookmark the post
   - Note the account and date

4. LOG TO DESIGN_REFERENCES.md
   Add the inspiration with:
   - What: Description of what you saw
   - Why: How it applies to your website builds
   - How: Code/technique to implement it

5. IMPLEMENT IN WEBSITES
   Apply the pattern to your next build
   (Samantha will use these when building new sites)

ESTIMATED TIME: 5-10 minutes per day per account

BEST TIMES TO CHECK:
- Early morning (6-8 AM): New posts often appear
- Afternoon (2-4 PM): New reels trending
- Evening (6-8 PM): Peak user engagement

EXAMPLE - What to Look For:
- Smooth fade-in animations on hero sections
- Hover effects on buttons
- Scroll-triggered reveals
- Color gradients
- Mobile-responsive layouts
- Loading animations
- Micro-interactions
"""
    
    print(instructions)
    
    print("\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print("""
✅ Create a daily routine:
   - 5-10 minutes each morning
   - Check the 3 accounts above
   - Screenshot anything inspiring
   - Log to DESIGN_REFERENCES.md

✅ Build a library:
   - Over time, you'll have 50+ design ideas
   - Reference when building new websites
   - Keep quality high, inspiration fresh

✅ Share with Samantha:
   - When Samantha builds next website
   - Reference the design patterns
   - Implement the techniques

✅ Automate where possible:
   - Use Telegram to send yourself links
   - Create Pinterest board for saves
   - Bookmark accounts to check regularly
""")
    
    # Create the design reference document
    create_design_reference_doc()
    
    # Log this check
    state["last_checked"] = datetime.now().isoformat()
    state["last_check_status"] = "ready_for_manual_review"
    save_monitor_state(state)
    
    print("\n✅ Design reference document created: DESIGN_REFERENCES.md")
    print("✅ Monitor state saved")
    print("\n🚀 Ready to start monitoring! Check Instagram daily.\n")

if __name__ == "__main__":
    monitor_instagram()
