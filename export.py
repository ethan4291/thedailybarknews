from app import app, dogs
from flask import render_template
import os

# By default write into the `docs/` folder so the output is ready for GitHub Pages
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "docs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with app.app_context():
    # Render homepage
    html = render_template("index.html", dogs=dogs)

    # Write to OUTPUT_DIR/index.html
    out_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

# Copy static folder to OUTPUT_DIR/static
import shutil
if os.path.exists("static"):
    shutil.copytree("static", os.path.join(OUTPUT_DIR, "static"), dirs_exist_ok=True)

print(f"Export complete! Files written to: {OUTPUT_DIR}/")
print("Push the contents of this folder to GitHub (commit + push). If you use GitHub Pages from `docs/`, it's ready to go.")
