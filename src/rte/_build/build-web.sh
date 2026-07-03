#!/bin/bash
# Genera el libro-web MULTIPÁGINA de La Empresa en Tiempo Real (edición ES).
#   1. concat.sh → _dist/EmpresaTiempoReal-vX.Y.md
#   2. web-build.py (compartido con AgencyDomains) → páginas HTML + nav + partes
# Uso:    ./build-web.sh [DIR_SALIDA]    (default: ../_dist/web-es, servido en /es/empresa-tiempo-real/)
# Requisitos: pandoc, python3. (El PDF se construye aparte con build-pdf.sh.)
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
DIST="$LIBRO_DIR/_dist"
WEBBUILD="$LIBRO_DIR/../agencydomains/_build/web-build.py"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" "$LIBRO_DIR/CHANGELOG.md" | cut -d" " -f2)
OUT="${1:-$DIST/web-es}"

echo "→ concat (Markdown único)…"
bash "$SCRIPT_DIR/concat.sh" >/dev/null

MD="$DIST/EmpresaTiempoReal-${VERSION}.md"
PDF="$DIST/EmpresaTiempoReal-${VERSION}.pdf"      # si existe (build-pdf.sh)
[ -f "$PDF" ] || PDF=""

echo "→ build-web (multipágina)…"
python3 "$WEBBUILD" \
  --md "$MD" --figuras "$LIBRO_DIR/figuras" \
  --agents "$LIBRO_DIR/para-agentes.md" ${PDF:+--pdf "$PDF"} \
  --name EmpresaTiempoReal --title "La Empresa en Tiempo Real" --lang es --base /es/empresa-tiempo-real --out "$OUT" --version "$VERSION"
echo "✓ libro-web La Empresa en Tiempo Real (ES) en: $OUT"
