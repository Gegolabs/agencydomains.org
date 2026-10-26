#!/bin/bash
# Construye la edición inglesa del Libro I, The Death of Software as We Know It:
# PDF (libro.sh en) + libro-web, servido como default en /death-of-software/.
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
bash "$SCRIPT_DIR/libro.sh" en
bash "$SCRIPT_DIR/web.sh" en "${1:-$LIBRO_DIR/_dist/web-en}"
echo "✓ edición inglesa The Death of Software as We Know It: MD + PDF + web"
