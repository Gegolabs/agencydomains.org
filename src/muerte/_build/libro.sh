#!/bin/bash
# Arma el Libro I en un idioma: el Markdown único y el PDF (WeasyPrint).
# Uso: libro.sh <es|en>  → _dist/<Nombre>-vX.Y.md y _dist/<Nombre>-vX.Y.pdf
#   es → MuerteDelSoftware · en → DeathOfSoftware
# El PDF sale del mismo armado con que se depositan las versiones en Zenodo
# (pandoc → HTML con libro.css y la portada del tomo I → WeasyPrint): carta,
# índice, la dedicatoria en página propia, un capítulo por página y notas al pie
# de página. Los otros libros se arman con XeLaTeX; este no, para que el PDF del
# sitio sea el del registro.
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
cd "$LIBRO_DIR"
L="${1:-es}"
case "$L" in
  es) C=contenido;    NAME=MuerteDelSoftware; PORTADA=portada.html;    TITULO="La muerte del software como lo conocemos"; TOC="Contenido"; ANCLA="la-trilogía"; LANG_META=();;
  en) C=contenido-en; NAME=DeathOfSoftware;   PORTADA=portada-en.html; TITULO="The Death of Software as We Know It";      TOC="Contents";  ANCLA="the-trilogy"; LANG_META=(--metadata lang=en);;  # lang=en activa la división de palabras del CSS; la edición en español se arma sin lang, como la publicada
  *) echo "uso: libro.sh <es|en>" >&2; exit 2;;
esac
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" CHANGELOG.md | cut -d" " -f2)
mkdir -p _dist
MD="_dist/$NAME-$VERSION.md"; HTML="_dist/$NAME-$VERSION.html"; PDF="_dist/$NAME-$VERSION.pdf"
: > "$MD"
for f in $C/00-frontmatter.md $C/dedicatoria.md $C/prefacio.md $C/0[1-9]-*.md $C/epilogo.md $C/glosario.md $C/referencias.md $C/colofon.md; do
  cat "$f" >> "$MD"; printf '\n\n' >> "$MD"
done
# Las figuras quedan relativas a _dist/ (../figuras/), donde vive el HTML del PDF.
sed -i 's#<!--.*-->##g' "$MD"
pandoc "$MD" -f markdown-tex_math_dollars -t html5 -s --toc --toc-depth=1 --lua-filter=notas-al-pie.lua \
  --metadata title="$TITULO" "${LANG_META[@]}" -c ../libro.css -o "$HTML"
PORTADA="$PORTADA" ANCLA="$ANCLA" TOC="$TOC" HTML="$HTML" python3 - <<'PY'
import re, os; b=open(os.environ['HTML']).read()
b=re.sub(r'<header id="title-block-header">.*?</header>','',b,flags=re.S)
b=b.replace('<body>','<body>\n'+open(os.environ['PORTADA']).read(),1)  # la portada: el tomo I de la pila
m=re.search(r'<nav id="TOC".*?</nav>',b,flags=re.S)
if m:
    nav=m.group(0); b=b.replace(nav,'',1)
    i=b.find('<h2 id="%s"' % os.environ['ANCLA']); b=b[:i]+nav+b[i:] if i>=0 else b
# el rótulo del índice en el idioma de la edición
b=b.replace('</head>','<style>nav#TOC::before { content: "%s"; }</style>\n</head>' % os.environ['TOC'],1)
open(os.environ['HTML'],'w').write(b)
PY
if command -v weasyprint >/dev/null; then WP=(weasyprint)
elif command -v uvx >/dev/null; then WP=(uvx --from weasyprint weasyprint)
else echo "✗ falta WeasyPrint (pipx install weasyprint · o uvx)" >&2; exit 1; fi
"${WP[@]}" -q "$HTML" "$PDF"
echo "✓ $PDF"
