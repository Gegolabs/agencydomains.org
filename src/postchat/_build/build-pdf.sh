#!/bin/bash
# Construye el PDF del libro Postchat v0.2 (fusión película + comentario).
# Edición online: oneside, SIN páginas en blanco (R7 del análisis de Vitor).
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
cd "$LIBRO_DIR"
bash "$SCRIPT_DIR/concat.sh"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" CHANGELOG.md | cut -d" " -f2)
MD="_dist/Postchat-${VERSION}.md"
PDF="_dist/Postchat-${VERSION}.pdf"
HEADER="$LIBRO_DIR/../agencydomains/_build/header-libro-extra.tex"
TMPSRC="$(mktemp -t postchat-pdf-XXXXXX).md"
trap 'rm -f "$TMPSRC"' EXIT
# Del frontmatter solo sobrevive «La trilogía» (promovida a página propia);
# el resto vive en la portada. Luego el libro desde el Prólogo.
{ awk '/^## La trilogía/{f=1} /^# Prólogo/{f=0} f' "$MD" | sed '1s/^## /# /'
  sed -n '/^# Prólogo/,$p' "$MD"; } > "$TMPSRC"
# Los teasers de escena (blockquote «Lo que acabas de ver:») se convierten en
# divs ::: cajateaser ::: que el filtro teaser.lua envuelve en el entorno
# LaTeX homónimo (header-fusion.tex); el título del blockquote pasa a ser el
# título sobre el borde de la caja.
perl -0777 -i -pe 's{^> \*\*Lo que acabas de ver:\*\*\n>\n> ([^\n]*)\n>\n> \*(El comentario de esta escena: [^\n]*?)\.?\*\n}{::: {.cajateaser comentario="$2"}\n$1\n:::\n}gm' "$TMPSRC"
pandoc "$TMPSRC" -o "$PDF" \
  --pdf-engine=xelatex -H "$HEADER" -H "$SCRIPT_DIR/header-fusion.tex" \
  --lua-filter="$SCRIPT_DIR/teaser.lua" \
  --metadata title="Postchat" --metadata subtitle="Mundo Agentivo" \
  --metadata author="César Obach-Renner" \
  --metadata date="Borrador de desarrollo ${VERSION} · Junio 2026" \
  --toc --toc-depth=1 \
  -V documentclass=book -V classoption=oneside -V geometry:margin=2.5cm \
  -V mainfont="STIX Two Text" -V mathfont="STIX Two Math" \
  -V monofont="Source Code Pro" -V monofontoptions:Scale=0.85 \
  -V fontsize=11pt -V lang=es --highlight-style=tango
echo "✓ $PDF"
