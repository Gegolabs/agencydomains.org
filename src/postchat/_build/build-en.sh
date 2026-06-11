#!/bin/bash
# Construye el PDF de la edición inglesa de Postchat v0.2 (the film + the commentary).
# Mismo diseño que la edición ES (build-pdf.sh): oneside, sin páginas en blanco.
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
cd "$LIBRO_DIR"
bash "$SCRIPT_DIR/concat.sh" "manifest-en.txt" "-EN"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" CHANGELOG.md | cut -d" " -f2)
MD="_dist/Postchat-EN-${VERSION}.md"
PDF="_dist/Postchat-EN-${VERSION}.pdf"
HEADER="$LIBRO_DIR/../agencydomains/_build/header-libro-extra.tex"
TMPSRC="$(mktemp -t postchat-pdf-en-XXXXXX).md"
TMPHDR="$(mktemp -t postchat-hdr-en-XXXXXX).tex"
trap 'rm -f "$TMPSRC" "$TMPHDR"' EXIT
# Título de la caja del teaser en inglés (redefine el default ES de header-fusion.tex).
printf '\\renewcommand{\\cajateasertitulo}{What you just saw}\n' > "$TMPHDR"
# Del frontmatter solo sobrevive «The Trilogy» (promovida a página propia);
# el resto vive en la portada. Luego el libro desde el Prologue.
{ awk '/^## The Trilogy/{f=1} /^# Prologue/{f=0} f' "$MD" | sed '1s/^## /# /'
  sed -n '/^# Prologue/,$p' "$MD"; } > "$TMPSRC"
# Teasers de escena → caja cajateaser (ver build-pdf.sh para el detalle).
perl -0777 -i -pe 's{^> \*\*What you just saw:\*\*\n>\n> ([^\n]*)\n>\n> \*(The commentary for this scene: [^\n]*?)\.?\*\n}{::: {.cajateaser comentario="$2"}\n$1\n:::\n}gm' "$TMPSRC"
pandoc "$TMPSRC" -o "$PDF" \
  --pdf-engine=xelatex -H "$HEADER" -H "$SCRIPT_DIR/header-fusion.tex" -H "$TMPHDR" \
  --lua-filter="$SCRIPT_DIR/teaser.lua" \
  --metadata title="Postchat" --metadata subtitle="The Agentive World" \
  --metadata author="César Obach-Renner" \
  --metadata date="Development draft ${VERSION} · June 2026" \
  --toc --toc-depth=1 \
  -V documentclass=book -V classoption=oneside -V geometry:margin=2.5cm \
  -V mainfont="STIX Two Text" -V mathfont="STIX Two Math" \
  -V monofont="Source Code Pro" -V monofontoptions:Scale=0.85 \
  -V fontsize=11pt -V lang=en --highlight-style=tango
echo "✓ $PDF"

# Libro-web inglés (servido como default en /postchat/)
WEBBUILD="$LIBRO_DIR/../agencydomains/_build/web-build.py"
OUT="${1:-_dist/web-en}"
echo "→ libro-web (--lang en)…"
python3 "$WEBBUILD" \
  --md "$MD" --figuras "$LIBRO_DIR/figuras" \
  --agents "$LIBRO_DIR/para-agents.md" --pdf "$PDF" \
  --name Postchat --lang en --base /postchat --out "$OUT" --version "$VERSION"
echo "✓ edición inglesa Postchat: MD + PDF + web en $OUT"
