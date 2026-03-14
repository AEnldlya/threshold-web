# Deploy HapLink to Netlify (30 Seconds)

## Method 1: Drag & Drop (Easiest)

### Step 1: Go to Netlify Drop
Open: **https://app.netlify.com/drop**

### Step 2: Sign In
- Click "Sign up" or "Login"
- Use GitHub (free account if needed)
- Takes 2 minutes first time

### Step 3: Drag & Drop Folder
1. Open your file explorer
2. Navigate to: `/home/clawdbot/.openclaw/workspace/haplink-multipage/`
3. Drag the **haplink-multipage** folder
4. Drop it onto the Netlify drop zone
5. Wait 10 seconds

### Step 4: You're Live!
You'll get a URL like:
```
https://happy-haptic-doctors.netlify.app
```

**Share this URL immediately!**

---

## Method 2: GitHub (For Updates)

### Step 1: Create GitHub Repo
```bash
cd haplink-multipage
git init
git add .
git commit -m "HapLink website redesign"
```

### Step 2: Push to GitHub
```bash
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/haplink.git
git push -u origin main
```

### Step 3: Connect to Netlify
1. Go to https://app.netlify.com
2. Click "New site from Git"
3. Select GitHub repo
4. Click "Deploy"

**Now every push auto-deploys!**

---

## Method 3: Upload Files Directly

1. Go to https://app.netlify.com
2. Click "New site from upload"
3. Drag folder or select files
4. Done

---

## After Deployment

### Test Your Site
- ✓ Open the Netlify URL
- ✓ Test all 8 pages (Home, Team, Robot, etc.)
- ✓ Check navigation
- ✓ Test on mobile (responsive)
- ✓ Verify animations smooth

### Custom Domain (Optional)
If you want `haplink.net`:
1. Go to Netlify Site Settings
2. Domain Management
3. Add custom domain
4. Update DNS in your registrar
5. Wait 24-48 hours

---

## Your Live URL

Once deployed, share:
```
https://happy-haptic-doctors.netlify.app
```

This is your production site. Update by:
1. Edit HTML/CSS files locally
2. Drag to Netlify again
3. Site updates in 30 seconds

---

## Add Images Later

1. Create `/images/` folder in `haplink-multipage/`
2. Add your JPG/PNG files
3. Drag updated folder to Netlify
4. Images appear immediately

---

## Troubleshooting

**Site doesn't load?**
- Check file structure (index.html at root)
- Verify all HTML files present
- Check CSS/JS file paths

**Animations not working?**
- Make sure script.js is present
- Check browser console for errors

**Images not showing?**
- Create `/images/` folder
- Add JPG/PNG files
- Redeploy folder

---

## You're Ready!

**Right now, deploy HapLink:**

1. Open https://app.netlify.com/drop
2. Drag `haplink-multipage/` folder
3. Share the URL with team

**That's it. Everything else is optional.**
