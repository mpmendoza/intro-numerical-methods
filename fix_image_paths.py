import json
from pathlib import Path
import shutil

solutions_dir = Path("my_solutions")

def fix_text(s: str) -> str:
    # Rewrite both Markdown and HTML patterns
    # Markdown: ](images/...) or ](./images/...)
    s2 = s.replace("](./images/", "](../images/")
    s2 = s2.replace("](images/",  "](../images/")
    # HTML: src="images/..." or src="./images/..."
    s2 = s2.replace('src="./images/', 'src="../images/')
    s2 = s2.replace('src="images/',   'src="../images/')
    # Single-quoted variants (rare but safe to handle)
    s2 = s2.replace("src='./images/", "src='../images/")
    s2 = s2.replace("src='images/",   "src='../images/")
    return s2

for nb_file in solutions_dir.glob("*.ipynb"):
    with open(nb_file, "r", encoding="utf-8") as f:
        nb = json.load(f)

    changed = False

    # Fix markdown + raw sources
    for cell in nb.get("cells", []):
        ctype = cell.get("cell_type")
        if ctype in ("markdown", "raw"):
            src = cell.get("source", [])
            if isinstance(src, list):
                new_src = []
                for line in src:
                    fixed = fix_text(line)
                    if fixed != line: changed = True
                    new_src.append(fixed)
                cell["source"] = new_src
            elif isinstance(src, str):
                fixed = fix_text(src)
                if fixed != src: changed = True
                cell["source"] = fixed

        # Fix HTML inside outputs (execute_result / display_data)
        if ctype == "code":
            for out in cell.get("outputs", []):
                data = out.get("data", {})
                # text/html can be a string or a list of strings
                if "text/html" in data:
                    html = data["text/html"]
                    if isinstance(html, list):
                        new_list = []
                        for chunk in html:
                            fixed = fix_text(chunk)
                            if fixed != chunk: changed = True
                            new_list.append(fixed)
                        data["text/html"] = new_list
                    elif isinstance(html, str):
                        fixed = fix_text(html)
                        if fixed != html: changed = True
                        data["text/html"] = fixed

    if changed:
        # backup once per file for safety
        backup = nb_file.with_suffix(".ipynb.bak")
        if not backup.exists():
            shutil.copy2(nb_file, backup)
        with open(nb_file, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print(f"✅ Fixed paths in {nb_file} (backup: {backup.name})")
    else:
        print(f"— No changes needed in {nb_file}")
