# ⚡ APMA4300 – Quick Reference

## Daily Workflow
1. Run startup alias  
   ```bash
   start4300
   ```  
   ✅ Activates `apma4300` env, cd into repo, opens VS Code  

2. Sync with professor and update your fork  
   ```bash
   syncapma
   ```  
   ✅ Ensures you’re on `master`, pulls `upstream`, pushes to `origin`  

3. Work on code, notes, or assignments  

4. Save progress  
   ### Best practice: check what changed first
   ```bash
   git status
   ```

   ### Stage, commit, and push
   ```bash
   git add filename.ipynb     # add specific file(s)
   git commit -m "prefix: short description"
   git push origin master
   ```

   📌 Homework notebooks should be copied into a root-level folder `hw1/`, `hw2/`, etc.  
   Example for HW1:
   ```
   intro-numerical-methods/hw1/HW1_error.ipynb
   ```

---

## Commit Prefixes
- **`startup:`** → checklists, environments, configs  
- **`notes:`** → STUDENT_NOTES, reflections  
- **`lecture:`** → class work, solutions, professor notebooks  
- **`assign:`** → assignments, submissions, related scripts  
- **`code:`** → Python code, experiments, analysis scripts  
- **`data:`** → processed datasets (never raw data)  
- **`misc:`** → cleanup, small fixes  

### Examples
- `startup: add GitHub CLI workflow`  
- `notes: reflections for Lecture 3`  
- `lecture: solved Newton’s method example`  
- `assign: completed Assignment 2 Q1-Q3`  
- `code: add R script for preprocessing cds object`  
- `data: updated processed dataset with filtering`  
- `misc: clean repo structure`  

---

# 🔄 APMA4300 Post-Reboot Checklist

This checklist ensures your Conda environment is active, your repo is synced with the professor, and you’re ready to start HW.

---

## 0. Confirm Conda is Available
```bash
conda info --envs
```
✅ Should list your environments (`apma4300`, `base`, etc.).

---

## 1. Open Terminal

---

## 2. Run Startup Alias
```bash
start4300
```
✅ Activates `apma4300` Conda environment, jumps into repo, and opens VS Code.

---

## 3. Sync with Professor + Update Fork
```bash
syncapma
```
✅ Ensures you’re on `master`, pulls professor’s updates (`upstream`), and pushes them to your fork (`origin`).

---

## 4. (Optional) Sanity Check
```bash
git status
```
Should say:
```
On branch master
Your branch is up to date with 'origin/master'.
nothing to commit, working tree clean
```

---

## 🔧 Troubleshooting (Only if Needed)

- **Check Conda environments:**
  ```bash
  conda info --envs
  ```

- **Check GitHub auth if push/pull fails:**
  ```bash
  gh auth status
  ```
  If not logged in:
  ```bash
  gh auth login
  ```

---

## Sanity Check in VS Code
- Kernel dropdown should read:
  ```
  Python (apma4300)
  ```
- Verify in notebook:
  ```python
  import sys
  print(sys.executable)
  ```
  Expected: `/Users/mpm/anaconda3/envs/apma4300/bin/python`

- Quick package test:
  ```python
  import numpy as np
  print(np.__version__)
  ```

---

🚀 **Workflow Summary:** `start4300 → syncapma → work → commit/push`

__last updated: Thu Sep 18, 2025__
