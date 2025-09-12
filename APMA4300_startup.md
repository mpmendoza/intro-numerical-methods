# 📋 APMA4300 – Daily Startup Checklist

### 1. Open Your Environment  
```bash
conda activate apma4300
cd /Users/mpm/Documents/Columbia/Coursework/Fall2025/APMA4300_NumericalMethods/git_repo/intro-numerical-methods
code .
```

### 2. Sync with Professor’s Repo  
Always start fresh with the latest lecture materials:  
```bash
git fetch upstream
git merge upstream/master
git push origin master
```

### 3. Prep Your Workspace  
- **Lecture prep**:  
  - Open today’s `.ipynb` from professor’s repo.  
  - Copy to `my_solutions/` if you want your own editable version.  

- **Homework**:  
  - Download assignment from Canvas.  
  - Place in `hwX/` folder (e.g., `hw1/`).  
  - ⚠️ Do not rename the file.  

### 4. Confirm Kernel in VS Code  
- Kernel should read:  
  ```
  apma4300 (Python 3.10.18)
  ```  
- If not, select it from the kernel picker.  

### 5. Learning Cycle  
- **Before class**: skim/run professor’s notebook, note 1–2 questions.  
- **During class**: follow along, mark confusing spots.  
- **After class**: work through your `my_solutions/` copy, add experiments.  

### 6. Save Your Progress  
```bash
git add .
git commit -m "Lecture X notes/practice"
git push origin master
```
