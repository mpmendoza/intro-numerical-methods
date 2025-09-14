# 📝 APMA4300 Student Notes  
This document is my personal record of learning, reflections, and problem-solving for the course.  

---

## 📑 Table of Contents  
- [📅 Lecture Notes](#-lecture-notes)  
- [🔑 Key Concepts to Master](#-key-concepts-to-master)  
- [🧪 Practice & Experiments](#-practice--experiments)  
- [📚 Homework Reflections](#-homework-reflections)  
- [❓ Questions for Office Hours / Review](#-questions-for-office-hours--review)  
- [✅ End-of-Week Wrap-Up](#-end-of-week-wrap-up)  
- [⚡ Startup Checklist](#-startup-checklist)  
- [📦 Environment Details](#-environment-details)  
- [🔄 Sync with Professor’s Repo](#-sync-with-professors-repo)  
- [🛠️ Troubleshooting](#-troubleshooting)  
- [🔖 Git Commit Naming Convention](#-git-commit-naming-convention)  
- [🛠️ Git Command Cheat Sheet](#️-git-command-cheat-sheet)  

---

## 📅 Lecture Notes  
**Lecture X – Title (Date)**  
- **Main topics covered:**  
- **Key formulas / concepts:**  
- **Professor’s examples to revisit:**  
- **Points of confusion to review later:**  

---

## 🔑 Key Concepts to Master  
- Concept 1 (ex: Floating-point error)  
- Concept 2 (ex: Newton’s method convergence)  
- Concept 3  

---

## 🧪 Practice & Experiments  
- Code snippets I wrote while exploring:  
  ```python
  # Example: testing Newton's method with f(x) = x^2 - 5
  ```
- Observations / results:  

---

## 📚 Homework Reflections  
**Homework X – Title**  
- What I found straightforward:  
- What challenged me:  
- Errors I ran into and how I solved them:  
- Takeaway for next time:  

---

## ❓ Questions for Office Hours / Review  
- Question 1  
- Question 2  
- Question 3  

---

## ✅ End-of-Week Wrap-Up  
- Biggest insight this week:  
- Still confusing:  
- Plan for next week:  

---

## ⚡ Startup Checklist  
For the **full daily checklist**, see [`APMA4300_startup.md`](APMA4300_startup.md).  

Quick high-level flow:  
1. Open terminal → `cd /Users/mpm/documents/columbia/coursework/fall2025/APMA4300_NumericalMethods`  
2. Activate env → `conda activate apma4300`  
3. Open repo in VS Code → `code .`  
4. Confirm kernel (`Python (apma4300)`) and run a quick test (`sys.executable`, `numpy.__version__`)  
5. Run `git status` before/after work  

---

## 📦 Environment Details  
- Python 3.10+  
- Core libraries:  
  - `numpy`  
  - `scipy`  
  - `matplotlib`  
  - `pandas`  
  - `sympy`  

Export environment if needed:  
```bash
conda env export > environment.yml
```

Recreate environment on another system:  
```bash
conda env create -f environment.yml
```

---

## 🔄 Sync with Professor’s Repo  
Make sure `upstream` remote is configured:  
```bash
git remote -v
```

To sync:  
```bash
git fetch upstream
git merge upstream/master
git push origin master
```

---

## 🛠️ Troubleshooting  
- **Kernel not showing in VS Code**  
  ```bash
  python3 -m ipykernel install --user --name=apma4300 --display-name "Python (apma4300)"
  ```

- **Environment not activating**  
  ```bash
  conda info --envs
  ```

- **Git won’t push**  
  - Check branch: `git branch`  
  - Check PAT validity  
  - Check remotes: `git remote -v`  

---

## 🔖 Git Commit Naming Convention  
- **`notes:`** → updates to `STUDENT_NOTES.md` or reflections  
- **`startup:`** → changes to startup instructions or environment  
- **`lecture:`** → work in `my_solutions/`  
- **`hw:`** → homework progress  
- **`misc:`** → fixes, cleanup, experiments  

---

# 🛠️ Git Command Cheat Sheet  

### Stage, commit, push  
```bash
git add .
git commit -m "prefix: short description"
git push origin master
```

### Check repo status  
```bash
git status
```

### View recent commits  
```bash
git log --oneline -5
```

### Sync with professor’s repo  
```bash
git fetch upstream
git merge upstream/master
git push origin master
```

---

_Last updated: September 14, 2025_
