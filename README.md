Simple static export of a Flask site for GitHub Pages

This repo contains a small Flask app and an `export.py` script that pre-renders the Jinja templates into `dist/` so the site can be hosted on GitHub Pages.

Deployment options:
- Enable Pages and serve from the `docs/` folder (copy `dist/` to `docs/` before pushing), or
- Let the included GitHub Actions workflow auto-build and publish `dist/` to the `gh-pages` branch on each push to `main`.

To test locally:
1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. python export.py
5. open dist/index.html
