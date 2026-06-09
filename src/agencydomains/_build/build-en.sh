#!/bin/bash
# Construye los entregables de la EDICIÓN INGLESA desde contenido-en/.
#   1. concat contenido-en/ (orden de manifest.txt) → _dist/AgencyDomains-vX.Y-en.md (MD único)
#   2. pandoc + xelatex → _dist/AgencyDomains-vX.Y-en.pdf (PDF de revisión, figuras embebidas)
#   3. web-build.py --lang en → libro-web multipágina en OUT (default _dist/web-en)
#
# Uso:    ./build-en.sh [DIR_SALIDA_WEB]
# Nota:   borrador de revisión. Incluye el front matter traducido (no usa frontmatter.tex,
#         que está en español). Las figuras se embeben aún en español (texto primero).
# Requisitos: pandoc, xelatex, python3 + fuentes STIX Two Text · STIX Two Math · Menlo.
set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
DIST="$LIBRO_DIR/_dist"
CONT_EN="$LIBRO_DIR/contenido-en"
MANIFEST="$SCRIPT_DIR/manifest.txt"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" "$LIBRO_DIR/CHANGELOG.md" | cut -d" " -f2)
OUT="${1:-$DIST/web-en}"

mkdir -p "$DIST"
MD="$DIST/AgencyDomains-${VERSION}-en.md"
: > "$MD"
echo "→ concat (contenido-en → MD único)…"
while IFS= read -r rel; do
  [ -z "$rel" ] && continue
  case "$rel" in \#*) continue ;; esac
  src="$CONT_EN/$rel"
  if [ ! -f "$src" ]; then echo "ERROR: falta $src (en manifest.txt)" >&2; exit 1; fi
  cat "$src" >> "$MD"
  printf '\n\n' >> "$MD"
done < "$MANIFEST"
echo "  ✓ $MD"

# PDF de revisión (incluye el front matter traducido; metadatos en inglés)
PDF="$DIST/AgencyDomains-${VERSION}-en.pdf"
HEADER="$SCRIPT_DIR/header-libro-extra.tex"
cd "$LIBRO_DIR"
echo "→ PDF (xelatex)…"
if pandoc "$MD" -o "$PDF" \
    --pdf-engine=xelatex -H "$HEADER" \
    --metadata title="AgencyDomains" \
    --metadata subtitle="Architecture of the Agentive World" \
    --metadata author="César Obach-Renner" \
    --metadata date="Development draft ${VERSION} · June 2026" \
    --toc --toc-depth=2 \
    -V documentclass=book -V classoption=twoside -V geometry:margin=2.5cm \
    -V mainfont="STIX Two Text" -V mathfont="STIX Two Math" \
    -V monofont="Menlo" -V monofontoptions:Scale=0.85 \
    -V fontsize=11pt -V lang=en --highlight-style=tango; then
  echo "  ✓ $PDF"
else
  echo "  AVISO: falló el PDF (¿xelatex/fuentes?). El MD único quedó igual."
  PDF=""
fi

# Libro-web inglés
echo "→ libro-web (--lang en)…"
python3 "$SCRIPT_DIR/web-build.py" \
  --md "$MD" --figuras "$LIBRO_DIR/figuras" \
  --agents "$LIBRO_DIR/para-agents.md" ${PDF:+--pdf "$PDF"} \
  --lang en --base /agencydomains --out "$OUT"
echo "✓ edición inglesa: MD + ${PDF:+PDF + }web en $OUT"
