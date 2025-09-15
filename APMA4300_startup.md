# 📋 APMA4300 – Daily Startup Checklist (with GitHub CLI)

### 1. Open Your Environment
```bash
cd /Users/mpm/documents/columbia/coursework/fall2025/APMA4300_NumericalMethods/git_repo/intro-numerical-methods
conda activate apma4300
code .
```

### 2. Confirm Kernel in VS Code
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

### 3. Run Sanity Check
```python
import numpy as np
print(np.__version__)
```

### 4. Git Operations (Auth via GitHub CLI)
GitHub authentication is now managed by the `gh` CLI (OAuth stored in macOS Keychain). No more PATs needed.

```bash
git status
git pull origin master
git push origin master
```

### 5. Learning Cycle
- **Before class**: skim/run professor’s notebook, note 1–2 questions.
- **During class**: follow along, mark confusing spots.
- **After class**: work through your `my_solutions/` copy, add experiments.

### 6. Save Progress
```bash
git add .
git commit -m "lecture: progress on Lecture X"
git push origin master
```

---

## 🔖 Git Commit Naming Convention  
- **`startup:`** → changes to startup checklists, environment, or configuration files  
- **`notes:`** → updates to `STUDENT_NOTES.md` or general course reflections  
- **`lecture:`** → work on in-class materials, solutions, or professor-provided notebooks  
- **`assign:`** → assignment progress, submissions, or related scripts  
- **`code:`** → Python or R code changes, experiments, analysis scripts  
- **`data:`** → processed datasets, data handling updates (never raw data)  
- **`misc:`** → small fixes, cleanup, or experiments outside the categories above  

### Example Messages  
- `startup: add GitHub CLI workflow to startup.md`  
- `notes: added reflections for Lecture 3`  
- `lecture: solved Newton’s method example`  
- `assign: completed Assignment 2 Q1-Q3`  
- `code: new R script for preprocessing cds object`  
- `data: updated processed dataset with filtering`  
- `misc: cleaned repo structure`  
