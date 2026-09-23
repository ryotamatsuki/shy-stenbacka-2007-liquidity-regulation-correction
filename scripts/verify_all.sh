#!/usr/bin/env bash
set -euo pipefail
python -m compileall -q code
python code/stage04_symbolic.py
python code/stage04a_independent.py
if command -v lake >/dev/null 2>&1; then
  lake build
else
  echo "lake not installed: Lean build is enforced in GitHub Actions" >&2
fi
if [ -f manuscript/main.tex ]; then
  if command -v latexmk >/dev/null 2>&1; then
    (cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
  else
    echo "latexmk not installed: manuscript compilation skipped locally" >&2
  fi
fi
