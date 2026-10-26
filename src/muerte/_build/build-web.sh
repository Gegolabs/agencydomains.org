#!/bin/bash
# Genera el libro-web MULTIPÁGINA del Libro I (edición ES), servido en /es/muerte-del-software/.
#   1. libro.sh es → _dist/MuerteDelSoftware-vX.Y.md (y el PDF)
#   2. web.sh es → web-build.py (compartido con AgencyDomains): páginas HTML + nav
# Uso:    ./build-web.sh [DIR_SALIDA]    (default: ../_dist/web-es)
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
DIST="$LIBRO_DIR/_dist"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" "$LIBRO_DIR/CHANGELOG.md" | cut -d" " -f2)
OUT="${1:-$DIST/web-es}"
PDF="$DIST/MuerteDelSoftware-${VERSION}.pdf"
[ -f "$PDF" ] || bash "$SCRIPT_DIR/libro.sh" es
bash "$SCRIPT_DIR/web.sh" es "$OUT"
