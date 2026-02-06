# How to Upload Your Project to GitHub - Step by Step

## Quick Upload (Easiest Method) ⚡

### Step 1: Create GitHub Account
1. Go to https://github.com
2. Click "Sign up"
3. Create your account

### Step 2: Create New Repository
1. Click "+" (top right) → "New repository"
2. **Repository name**: `ai-summarizer-static-prompt`
3. **Description**: "Learning project - Understanding static prompts in AI using HuggingFace API"
4. Choose **Public**
5. **Don't check** "Add a README" (we have our own!)
6. Click "Create repository"

### Step 3: Upload Files
1. Click "uploading an existing file"
2. Upload these **5 files**:
   - ✅ `app.py`
   - ✅ `README.md`
   - ✅ `requirements.txt`
   - ✅ `.gitignore`
   - ✅ `screenshot.png` (your app screenshot)
3. Write: "Initial commit - Static prompt learning project"
4. Click "Commit changes"

### Step 4: Done! 🎉
Your project is live! Share the link!

---

## Using Git Commands (For Learning Git)

### First Time Setup
```bash
# Install Git first (if not installed)
# Windows: https://git-scm.com/download/win
# Mac: brew install git
# Linux: sudo apt install git

# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Upload Your Project
```bash
# 1. Go to your project folder
cd path/to/your/project

# 2. Initialize git
git init

# 3. Add all files
git add .

# 4. Commit
git commit -m "Initial commit - Static prompt learning project"

# 5. Connect to GitHub (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/ai-summarizer-static-prompt.git

# 6. Push to GitHub
git branch -M main
git push -u origin main
```

---

## After Upload - Make It Look Professional

### 1. Add Screenshot
- Upload `screenshot.png` to your repository
- It will automatically show in README

### 2. Add Topics/Tags
1. Click "⚙️" next to "About" (right side)
2. Add topics: `ai`, `machine-learning`, `python`, `streamlit`, `huggingface`, `learning-project`
3. Save

### 3. Pin to Profile
1. Go to your GitHub profile
2. Click "Customize your pins"
3. Select this repository
4. Save

---

## Good Repository Names

- `ai-summarizer-static-prompt` ⭐ (Recommended)
- `static-prompt-learning`
- `ai-text-summarizer`
- `huggingface-static-prompt`

---

## Common Issues

**"Permission denied"**
→ Make sure you're logged into GitHub

**"Repository already exists"**
→ Choose a different name

**"Can't upload .gitignore"**
→ No problem, just skip it for now

---

## Your Project URL
After upload: `https://github.com/YOUR-USERNAME/ai-summarizer-static-prompt`

Share it on LinkedIn to show your learning! 🚀
