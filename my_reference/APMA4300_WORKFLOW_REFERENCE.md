# 🚀 APMA4300 – Workflow Reference

This document is a long-form **reference guide** for APMA4300.  
For daily work and reboots, use [`APMA4300_QUICKREF.md`](./APMA4300_QUICKREF.md).  

---

## 1. Authentication
- Use **GitHub CLI (`gh`)** → no PATs, no Keychain juggling.  
- Confirm login anytime:  
  ```bash
  gh auth status
  ```
- If needed:  
  ```bash
  gh auth login
  ```
  → Choose *GitHub.com → HTTPS → Yes to authenticate Git → browser login*.  

---

## 2. Repo Setup (already done)
- **APMA4300** → Python + VS Code + Jupyter  
  `/Users/mpm/Documents/Columbia/Coursework/Fall2025/APMA4300/intro-numerical-methods`  

Repo includes:  
- `APMA4300_STUDENT_NOTES.md` → reflections & practice  
- `EVERYN_PRINCIPLES.md` → how we collaborate  
- `APMA4300_QUICKREF.md` → daily + reboot checklist  
- `.gitignore` → protects repo from junk files  

---

## 3. Daily Workflow (Big Picture)
1. Open Terminal  
2. Run:  
   ```bash
   start4300
   ```  
   → Activates env, cd into repo, opens VS Code.  
3. Sync with GitHub:  
   ```bash
   syncapma
   ```  
   → Ensures you’re on `master`, pulls professor’s repo (`upstream`), pushes to your fork (`origin`).  
4. Work on code, notes, assignments.  
5. Save progress:  
    ### Best practice: check what changed first
    git status

    ### Stage, commit, and push
    git add filename.ipynb     # add specific file(s)
    git commit -m "prefix: short description"
    git push origin master

---

## 4. Commit Naming Convention
- `startup:` → checklists, environments, configs  
- `notes:` → STUDENT_NOTES or reflections  
- `lecture:` → in-class materials, solutions, notebooks  
- `assign:` → assignment progress or submissions  
- `code:` → Python code, experiments, scripts  
- `data:` → processed datasets or handling updates  
- `misc:` → small fixes, cleanup  

Examples:  
- `startup: add GitHub CLI workflow`  
- `lecture: solved Newton’s method example`  
- `assign: HW2 progress Q1-Q3`  

---

## 5. Keeping Repo Clean
- `.gitignore` prevents junk (caches, Jupyter checkpoints, macOS files, raw datasets).  
- If you suspect junk got tracked:  
  ```bash
  git ls-files | grep -E '.DS_Store|.ipynb_checkpoints|.Rhistory|.RData|.Rproj.user|.slides.html|peer_review.html|template.ipynb'
  ```  
  - Nothing prints → ✅ all clean.  
  - If something prints → remove once:  
    ```bash
    git rm --cached filename
    git commit -m "cleanup: remove ignored files"
    git push origin branch
    ```  

---

## 6. Special Sync with Professor’s Repo
Professor’s repo is set as `upstream`.  
To sync manually (alias `syncapma` already does this):  
```bash
git fetch upstream
git merge upstream/master
git push origin master
```

---

## 7. After a Reboot
For APMA, use the **QuickRef** instead of this doc:  
- [`APMA4300_QUICKREF.md`](./APMA4300_QUICKREF.md)  

---

✅ With this reference:  
- Repo stays consistent and clean.  
- GitHub auth is simple and secure.  
- No junk files get pushed.  
- QuickRef handles daily steps; this file is your background reference.  
