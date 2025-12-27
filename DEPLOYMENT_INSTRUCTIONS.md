# 📋 FRESH START DEPLOYMENT INSTRUCTIONS

## ✅ STEP 1: Create New GitHub Repository

1. Go to: https://github.com/new
2. **Repository name:** `library-events-v2`
3. **Description:** "Bay Area family events scraper"
4. Select **Public**
5. **DO NOT** check any boxes (no README, no .gitignore, no license)
6. Click **"Create repository"**

---

## ✅ STEP 2: Upload Files to GitHub

**After creating the repo, you'll see a page with upload instructions.**

### Option A: Upload via Web Interface (EASIEST)

1. On the "Quick setup" page, click **"uploading an existing file"**
2. Download ALL these files from Claude:
   - `library_website.py`
   - `index.html`
   - `README.md`
   - `.github/workflows/update-website.yml`
3. Drag ALL files into the upload box
4. **Important:** Keep the folder structure! The workflow file MUST be in `.github/workflows/`
5. Scroll down and click **"Commit changes"**

### Option B: Upload via Command Line

```bash
# In your terminal (if you have the files locally)
cd /path/to/fresh-start
git init
git add .
git commit -m "Initial commit with Tracy Veterans Park events"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/library-events-v2.git
git push -u origin main
```

---

## ✅ STEP 3: Enable GitHub Pages

1. Go to your repo: `https://github.com/YOUR-USERNAME/library-events-v2`
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Build and deployment":
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes

---

## ✅ STEP 4: Test the Workflow

1. Go to **Actions** tab in your repo
2. Click **"Update Events Daily"** on the left
3. Click **"Run workflow"** dropdown (right side)
4. Click green **"Run workflow"** button
5. Wait 30 seconds
6. Click on the workflow run to see logs
7. Verify it says "✅ index.html exists" and "Tracy Veterans Park mentions: 4"

---

## ✅ STEP 5: View Your Live Site!

Your site will be live at:
**https://YOUR-USERNAME.github.io/library-events-v2/**

Replace `YOUR-USERNAME` with your actual GitHub username.

---

## 🎉 SUCCESS CHECKLIST

- [ ] Repository created
- [ ] All files uploaded (with correct folder structure)
- [ ] GitHub Pages enabled
- [ ] Workflow ran successfully
- [ ] Site is live and shows Tracy Veterans Park events

---

## 🔧 If Something Goes Wrong

**Workflow fails?**
- Check that `.github/workflows/update-website.yml` is in the correct folder
- Make sure the workflow file has no syntax errors

**Site not showing?**
- Wait 2-3 minutes after enabling GitHub Pages
- Try hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

**Tracy Veterans Park events not showing?**
- Check the date filter is set to "All Dates"
- Check the location filter is set to "All Locations"

---

## 📝 File Structure Should Look Like This:

```
library-events-v2/
├── .github/
│   └── workflows/
│       └── update-website.yml
├── library_website.py
├── index.html
└── README.md
```

---

## ⏰ Automatic Updates

The workflow runs automatically every day at midnight PST to fetch fresh events!
