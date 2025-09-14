# 📋 APMA4300 – Daily Startup Checklist

### 1. Open Your Environment  
```bash
conda activate apma4300
cd /Users/mpm/documents/columbia/coursework/fall2025/APMA4300_NumericalMethods
code .
```

### 2. Sync with Professor’s Repo (optional, if new lecture content is available)  
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
  Python (apma4300)
  ```  
- If not, select it from the kernel picker.  
- Extra verification (in first notebook cell):  
  ```python
  import sys
  print(sys.executable)
  ```
  Expected: `/Users/mpm/anaconda3/envs/apma4300/bin/python`

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
