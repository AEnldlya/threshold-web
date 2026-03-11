# HapLink Images - Setup Guide

## Image Folder Structure

Create this folder structure and add your images:

```
haplink-multipage/
├── images/
│   ├── team/
│   │   ├── kastner-anderson.jpg
│   │   ├── elizabeth-anderson.jpg
│   │   ├── jacob-hannan.jpg
│   │   ├── grayson-lyall.jpg
│   │   ├── owen-osterberg.jpg
│   │   ├── alan-zhang.jpg
│   │   ├── andy-zhang.jpg
│   │   ├── ella-zhang.jpg
│   │   ├── erich-osterberg.jpg
│   │   └── yu-zhang.jpg
│   │
│   ├── robot/
│   │   ├── robot-assembly.jpg
│   │   ├── robot-motors.jpg
│   │   └── robot-electronics.jpg
│   │
│   └── highlights/
│       ├── competition-team.jpg
│       ├── crowd-energy.jpg
│       ├── team-celebration.jpg
│       ├── media-moment.jpg
│       └── robot-performance.jpg
│
├── index.html
├── team.html
├── robot.html
├── 2024-highlights.html
├── 2023-fll.html
├── 2024-worlds.html
├── 2025.html
├── donate.html
├── styles.css
└── script.js
```

## Where to Find Images

### From Original HapLink.net:
- **Team members:** Individual headshots
- **Robot photos:** Assembly, motor systems, electronics
- **Competition photos:** Team in action, crowd, celebrations
- **Videos:** Can be embedded with <video> tags

## How to Add Images

### For Team Members:
Replace this:
```html
<img src="images/kastner-anderson.jpg" alt="Kastner Anderson">
```

### For Robot/Gallery:
Replace this:
```html
<img src="images/robot-assembly.jpg" alt="Full Robot Build">
```

## Temporary Workaround (If No Images Yet)

If you don't have images yet, the site still works! The image references are there - just add images later:

1. Create `images/` folder
2. Add your .jpg or .png files
3. Netlify will serve them automatically

## Image Requirements

- **Format:** JPG or PNG
- **Size:** Keep under 500KB per image (compress if needed)
- **Dimensions:** 
  - Team photos: 300×400px (portrait)
  - Gallery: 16:9 aspect ratio (800×450px recommended)
- **Quality:** 72 DPI is fine for web

## Tools to Compress Images

Before uploading:
- **TinyPNG.com** (free, drag & drop)
- **ImageOptim** (Mac, free)
- **FileOptimizer** (Windows, free)

Compression keeps load time fast (<3 seconds).

## Deploy to Netlify (With or Without Images)

The website works whether or not you have images yet:

1. Drag the `haplink-multipage/` folder to Netlify
2. Site goes live immediately
3. Add images to the `/images/` folder later
4. Redeploy by dragging folder again

Images will appear once added and redeployed.

---

**Ready to deploy? Follow the DEPLOYMENT_GUIDE.md**
