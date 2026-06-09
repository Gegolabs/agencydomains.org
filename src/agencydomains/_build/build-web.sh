#!/bin/bash
# Genera el libro-web MULTIPÁGINA (una página por capítulo) desde la fuente Markdown.
#   1. concat.sh → Markdown único en _dist/
#   2. web-build.py → páginas HTML por capítulo + barra lateral + prev/next
# Uso:    ./build-web.sh [DIR_SALIDA]
#   DIR_SALIDA por defecto: ../../agencydomains.org/agencydomains  (el sitio publicado)
# Requisitos: pandoc, python3. (El PDF se construye aparte con build-pdf.sh.)
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
DIST="$LIBRO_DIR/_dist"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" "$LIBRO_DIR/CHANGELOG.md" | cut -d" " -f2)
OUT="${1:-$LIBRO_DIR/../../agencydomains}"

echo "→ concat (Markdown único)…"
bash "$SCRIPT_DIR/concat.sh" >/dev/null

MD="$DIST/AgencyDomains-${VERSION}-humanos.md"
PDF="$DIST/AgencyDomains-${VERSION}-humanos.pdf"      # si existe (build-pdf.sh)
AGENTS="$LIBRO_DIR/para-agentes.md"

echo "→ build-web (multipágina)…"
python3 "$SCRIPT_DIR/web-build.py" \
  --md "$MD" --figuras "$LIBRO_DIR/figuras" \
  --agents "$AGENTS" ${PDF:+--pdf "$PDF"} \
  --out "$OUT"
echo "✓ libro-web en: $OUT"
