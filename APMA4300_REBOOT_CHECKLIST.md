# 🔄 Post-Reboot Quick Checklist

This checklist ensures your environment and GitHub auth are ready after restarting macOS.

---

## 1. Confirm Conda is Available
```bash
conda info --envs
```
✅ Should list your environments (`apma4300`, `base`, etc.).

---

## 2. Activate Environment (APMA4300 Only)
```bash
conda activate apma4300
```

---

## 3. Check GitHub CLI Authentication
```bash
gh auth status
```
✅ Should say:
```
Logged in to github.com as mpmendoza
```

If not, log in again:
```bash
gh auth login
```

---

## 4. Sanity Check Repo Access
Inside repo folder:
```bash
git status
git pull origin main   # or master for APMA4300
```
✅ If clean, you’re ready to work 🚀
