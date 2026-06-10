#!/bin/bash
# Construye el PDF del libro AURA desde el ensamblado del manifest.
#   1. concat.sh → _dist/AURA-vX.Y.md (resuelve marcadores standalone/libro y retitulados)
#   2. pandoc + xelatex → _dist/AURA-vX.Y.pdf
# Requisitos: pandoc, xelatex, fuentes STIX Two + Source Code Pro (ver twin/src/_fonts),
#             y el header LaTeX compartido del libro AgencyDomains.
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
cd "$LIBRO_DIR"
bash "$SCRIPT_DIR/concat.sh"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" CHANGELOG.md | cut -d" " -f2)
MD="_dist/AURA-${VERSION}.md"
PDF="_dist/AURA-${VERSION}.pdf"
HEADER="$LIBRO_DIR/../agencydomains/_build/header-libro-extra.tex"
TMPSRC="$(mktemp -t aura-pdf-XXXXXX).md"
trap 'rm -f "$TMPSRC"' EXIT
sed -n '/^# Prólogo/,$p' "$MD" > "$TMPSRC"
pandoc "$TMPSRC" -o "$PDF" \
  --pdf-engine=xelatex -H "$HEADER" \
  --resource-path="$LIBRO_DIR/specs:$LIBRO_DIR" \
  --metadata title="AURA" --metadata subtitle="El Camino Agentivo" \
  --metadata author="César Obach-Renner" \
  --metadata date="Borrador de desarrollo ${VERSION} · Junio 2026" \
  --toc --toc-depth=2 \
  -V documentclass=book -V classoption=twoside -V geometry:margin=2.5cm \
  -V mainfont="STIX Two Text" -V mathfont="STIX Two Math" \
  -V monofont="Source Code Pro" -V monofontoptions:Scale=0.85 \
  -V fontsize=11pt -V lang=es --highlight-style=tango
echo "✓ $PDF"
