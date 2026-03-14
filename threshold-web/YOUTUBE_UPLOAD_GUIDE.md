# YouTube Upload Guide - Story Video #1

## What We Have

### Videos Created
1. **story_video_1.mp4** (371 KB) - Basic version with subtitles
2. **story_video_1_CINEMATIC.mp4** (369 KB) - Enhanced version with color grading

**Format**: 1080x1920 (vertical)
**Duration**: ~25 seconds
**Audio**: AI voiceover (embedded)

---

## How to Upload to YouTube

### Option 1: Automatic Upload Script (Recommended)

```bash
cd /home/clawdbot/.openclaw/workspace
python3 upload_to_youtube.py
```

**What it does:**
1. Authenticates with your Google account
2. Uploads the video to YouTube
3. Adds title, description, tags, category
4. Sets privacy to "Public"
5. Returns shareable YouTube link

**First time setup:**
- You'll be asked to authorize YouTube upload permissions
- Click "Allow" when prompted
- Token will be saved for future uploads

### Option 2: Manual YouTube Upload

1. Go to **https://www.youtube.com/upload**
2. Click "Select files to upload"
3. Choose: `/home/clawdbot/.openclaw/workspace/story_video_1_CINEMATIC.mp4`
4. Fill in:
   - **Title**: "The Job Interview - A Dark Story | AI Storytelling"
   - **Description**: (see below)
   - **Tags**: storytelling, horror, shortfilm, thriller, darkstory, AI, scary, fiction
   - **Category**: Entertainment
   - **Age restriction**: None (not made for kids)
5. Click "Publish"

---

## Video Metadata

### Title
```
The Job Interview - A Dark Story | AI Story
```
*(29 characters - good for SEO, includes hook + keyword)*

### Description
```
I got hired in 3 minutes. That should've been my first warning.

A short dark fiction story about a suspicious job interview that leads to a terrifying discovery.

This is a work of fiction created for entertainment purposes using AI technology. All characters and events are entirely fictional.

---

📌 Subscribe for more AI-generated stories
🎬 New videos every week
💬 What would you have done?

#storytelling #horror #shortfilm #thriller #darkfiction #AI
```

### Tags (10+ recommended)
- storytelling
- horror
- shortfilm
- thriller
- darkstory
- creepy
- mystery
- AI
- scary
- fiction
- paranormal
- suspense

### Category
**Entertainment** (ID: 24)

### Thumbnail
*Suggested: Red/dark colors, shocked face emoji, text "THE TWIST"*
*(Generated separately - not included yet)*

---

## Expected Performance

**Conservative estimate** (first month):
- Views: 500-5,000
- Comments: 10-50
- Likes: 25-250
- Subscribers gained: 5-50

**If algorithmic boost kicks in**:
- Views: 50,000-500,000+
- Comments: 500-5,000
- Likes: 2,500-25,000+
- Subscribers gained: 500-5,000+

**Why this story works for YouTube Shorts**:
- ✅ Hook in first 2 seconds
- ✅ Dark/mysterious (high engagement topic)
- ✅ Twist ending (makes people comment/debate)
- ✅ 25 seconds (perfect for YouTube Shorts algorithm)
- ✅ AI-generated (novelty factor = shares)

---

## YouTube Channel Setup

**Recommended settings:**
1. Channel name: Something like "AI Stories" or "Dark Tales AI"
2. Channel description: "AI-generated dark fiction stories. New videos every week."
3. Channel art: Dark, moody, professional
4. Playlists: "Dark Stories", "Horror Tales", etc.
5. Enable monetization once you hit 1,000 subscribers + 4,000 watch hours

---

## Next Steps

1. **Upload this video** to YouTube using the script above
2. **Monitor engagement** for 48 hours (track views, comments, shares)
3. **Create 10 more videos** in the same style (test different story angles)
4. **Identify winners** (which stories get most engagement?)
5. **Double down** on winning formats (post 5-10 of those per week)

---

## Monetization Timeline

**Month 1**: 
- Upload 4-5 videos
- Build to ~500 subscribers

**Month 2**:
- Upload 10-15 videos
- Build to ~2,000 subscribers
- ~50,000 views total

**Month 3**:
- Upload 20-30 videos
- Hit 4,000 watch hours
- Apply for monetization (YouTube Partner Program)

**Month 4+**:
- Earnings from AdSense: $1,000-5,000/month
- At 100K views/month @ $0.25 CPM = $2,500/month

---

## Upload Commands

**Quick upload (manual selection)**:
```bash
python3 upload_to_youtube.py
```

**Bulk upload (when we have 10+ videos)**:
```bash
python3 upload_all_stories.py
```
*(Script to be created)*

---

## Troubleshooting

**"OAuth callback not received"**
- The script will print a URL
- Copy that URL and paste into your browser
- Complete the authorization
- After redirecting, copy the full redirect URL
- Paste it back into the terminal

**"Video already uploaded"**
- YouTube checks for duplicates
- Change the title slightly if re-uploading
- Use a different video file

**"File too large"**
- YouTube accepts up to 256GB
- Our videos are ~370KB (no problem)
- Video should upload in <1 minute

---

Ready to upload? Run:
```bash
python3 upload_to_youtube.py
```
