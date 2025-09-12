# APMA 4300E — Computational Math: Introduction to Numerical Methods  
**Fall 2025 | Columbia University**  
**Instructor:** Prof. Marc Spiegelman  
**Schedule:** Tu/Th 10:10–11:25 AM | Schermerhorn 614  

---

## 🧠 Course Overview

This course introduces the design and implementation of numerical algorithms for solving mathematical problems in science and engineering. Emphasis is placed on:
- Precision, accuracy, and error analysis
- Algorithmic implementation using Python and Jupyter notebooks
- Applied problem-solving for rootfinding, interpolation, differentiation, integration, ODEs, and linear algebra
- A final numerical methods project incorporating Finite Element Method (FEM) modeling

You are expected to use Python (NumPy, SciPy, Matplotlib) and write up results using **LaTeX or Markdown**.  

---

## 🗂️ Folder Structure

| Folder | Description |
|--------|-------------|
| `problem_sets/` | All eight assignments, organized by topic (see below) |
| `project/` | Final FEM-based project: proposal, code, figures, results, and write-up |
| `lectures/` | Cloned content from Prof. Spiegelman’s GitHub repo |
| `notes/` | Summaries and cheat sheets in Markdown or LaTeX |
| `environment/` | Python package requirements and FEM software setup notes |

---

## 📆 Problem Sets (Coding + Writeup)

| PS | Topic | Folder |
|----|-------|--------|
| PS0 | Python, NumPy, Jupyter basics | `ps0_intro/` |
| PS1 | Error types (model, truncation, floating point) | `ps1_error_analysis/` |
| PS2 | Rootfinding & Optimization | `ps2_rootfinding/` |
| PS3 | Interpolation methods | `ps3_interpolation/` |
| PS4 | Numerical differentiation and quadrature | `ps4_quadrature/` |
| PS5 | ODE initial value problems | `ps5_ODE_ivp/` |
| PS6 | Boundary value problems + FEM intro | `ps6_ODE_bvp/` |
| PS7 | Linear algebra basics | `ps7_lin_alg_intro/` |
| PS8 | QR, Eigen, and SVD applications | `ps8_qr_svd/` |

Each folder should contain:
- `solution.ipynb` — Python notebook
- `writeup.md` or `writeup.tex` — LaTeX/Markdown explanation
- `README.md` — (Optional) Notes to self, reflections

---

## 🧪 Final Project

The project includes algorithmic development, analysis, and comparison with FEM software such as **COMSOL** or **FEBio**. Your deliverables include:
- **Proposal** — problem description, goals
- **Code** — numerical solution implementation
- **Figures** — visual results, convergence plots, etc.
- **Results** — tables, performance metrics
- **Report** — final analysis written in LaTeX

All project materials live in the `project/` folder and its subfolders.

---

## 🛠️ Environment & Tools

This course relies on:

- **Python 3.10+**
- Core libraries: `numpy`, `scipy`, `matplotlib`, `pandas`, `sympy`
- Jupyter Notebooks
- LaTeX for formal writeups
- FEM software (COMSOL or FEBio)

Track your setup details and dependencies in:
- `environment/requirements.txt`  
- `environment/install_guides/` — for FEM tools, licensing, etc.

---

## 📝 Notes & Cheat Sheets

Markdown or LaTeX files summarizing:
- Key concepts
- Algorithm pseudocode
- Derivations
- LaTeX formatting templates

Use `notes/summaries/` for weekly concepts, and `notes/cheat_sheets/` for quick-access references during assignments or the final.

---

## 🧭 Study Goals

- [ ] Stay 1 lecture ahead with notebook walkthroughs
- [ ] Keep assignment folders clean and modular
- [ ] Use Git commits to track each major problem-solving step
- [ ] Reuse project structure for future research efforts (e.g., Biomechanics or ODE-based modeling)

---
his document is my personal record of learning, reflections, and problem-solving for the course.  

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

_Last updated: September 11, 2025_
# 🛠️ Git Command Cheat Sheet  

### 1. Stage, commit, and push in one go  
```bash
git add .
git commit -m "prefix: short description"
git push origin master
```

- Replace **`prefix: short description`** with one of my commit prefixes:  
  - `notes:` → for updates to STUDENT_NOTES.md  
  - `startup:` → for APMA4300_startup.md changes  
  - `lecture:` → for my_solutions/ work  
  - `hw:` → for homework progress  
  - `misc:` → for fixes or experiments  

---

### 2. Check repo status  
```bash
git status
```

---

### 3. View recent commits  
```bash
git log --oneline -5
```

---

### 4. Sync with professor’s repo  
```bash
git fetch upstream
git merge upstream/master
git push origin master
```

---
