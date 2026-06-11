#!/bin/bash
# Construye la edición inglesa del libro AURA desde manifest-en.txt.
#   1. concat.sh manifest-en.txt -EN → _dist/AURA-EN-vX.Y.md
#   2. pandoc + xelatex → _dist/AURA-EN-vX.Y.pdf
#   3. web-build.py (compartido) → libro-web multipágina en _dist/web-en
# Requisitos: pandoc, xelatex, fuentes STIX Two + Source Code Pro (ver twin/src/_fonts),
#             y el header LaTeX compartido del libro AgencyDomains.
# Las figuras EN viven en specs/figuras-en/ (fuente specs/figuras-fuente-en/).
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
cd "$LIBRO_DIR"
bash "$SCRIPT_DIR/concat.sh" manifest-en.txt -EN
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" CHANGELOG.md | cut -d" " -f2)
MD="_dist/AURA-EN-${VERSION}.md"
PDF="_dist/AURA-EN-${VERSION}.pdf"
HEADER="$LIBRO_DIR/../agencydomains/_build/header-libro-extra.tex"
TMPSRC="$(mktemp -t aura-en-pdf-XXXXXX).md"
trap 'rm -f "$TMPSRC"' EXIT
# Del frontmatter solo sobrevive «La trilogía» (página propia); el resto vive en la portada.
{ awk '/^## The Trilogy/{f=1} /^# Prologue/{f=0} f' "$MD" | sed '1s/^## /# /'
  sed -n '/^# Prologue/,$p' "$MD"; } > "$TMPSRC"
sed -i '' 's|](figuras/|](figuras-en/|g' "$TMPSRC" 2>/dev/null || sed -i 's|](figuras/|](figuras-en/|g' "$TMPSRC"
pandoc "$TMPSRC" -o "$PDF" \
  --pdf-engine=xelatex -H "$HEADER" \
  --resource-path="$LIBRO_DIR/specs:$LIBRO_DIR" \
  --metadata title="AURA" --metadata subtitle="The Agentive Path" \
  --metadata author="César Obach-Renner" \
  --metadata date="Development draft ${VERSION} · June 2026" \
  --toc --toc-depth=2 \
  -V documentclass=book -V classoption=twoside -V geometry:margin=2.5cm \
  -V mainfont="STIX Two Text" -V mathfont="STIX Two Math" \
  -V monofont="Source Code Pro" -V monofontoptions:Scale=0.85 \
  -V fontsize=11pt -V lang=en --highlight-style=tango
echo "✓ $PDF"

# Libro-web inglés (servido como default en /aura/)
WEBBUILD="$LIBRO_DIR/../agencydomains/_build/web-build.py"
OUT="${1:-_dist/web-en}"
echo "→ libro-web (--lang en)…"
python3 "$WEBBUILD" \
  --md "$MD" --figuras "$LIBRO_DIR/specs/figuras-en" \
  --agents "$LIBRO_DIR/para-agents.md" --pdf "$PDF" \
  --name AURA --lang en --base /aura --out "$OUT" --version "$VERSION"
echo "✓ edición inglesa AURA: MD + PDF + web en $OUT"
