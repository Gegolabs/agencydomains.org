#!/bin/bash
# Renderiza la portada de un libro a PDF de una página (carta, a sangre) y
# escribe al lado el encabezado LaTeX que la mete como página 1.
# Uso: render.sh <rte|aura|agencydomains> <es|en> <salida.pdf>
#   → <salida.pdf> y <salida>.tex, que el build pasa a pandoc con -H.
# La plantilla de pandoc pone include-before DESPUÉS de \maketitle, así que la
# portada entra por \AtBeginDocument: va antes de \frontmatter y del título,
# que queda detrás como portadilla. La portada se numera «A» (Alph) para que su
# ancla no choque con la página 1 del cuerpo; \frontmatter vuelve a romanos.
# En los libros twoside, \frontmatter deja en blanco el dorso de la portada y
# la portadilla y los capítulos conservan su paridad de recto.
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO="$1"; LANG_="$2"; OUT="$3"
HTML="$SCRIPT_DIR/$LIBRO-$LANG_.html"
[ -f "$HTML" ] || { echo "✗ no hay portada $HTML" >&2; exit 1; }
if command -v weasyprint >/dev/null; then WP=(weasyprint)
elif command -v uvx >/dev/null; then WP=(uvx --from weasyprint weasyprint)
else echo "✗ falta WeasyPrint (apt install weasyprint · o uvx)" >&2; exit 1; fi
"${WP[@]}" -q "$HTML" "$OUT"
# una portada que se desborda a una segunda página correría el libro entero
if command -v pdfinfo >/dev/null; then
  N=$(pdfinfo "$OUT" | awk '/^Pages:/{print $2}')
  [ "$N" = 1 ] || { echo "✗ la portada $LIBRO-$LANG_ salió con $N páginas" >&2; exit 1; }
fi
cat > "${OUT%.pdf}.tex" <<TEX
\\usepackage{pdfpages}
\\AtBeginDocument{\\pagenumbering{Alph}\\includepdf[pages=1,pagecommand={\\thispagestyle{empty}}]{$(cd "$(dirname "$OUT")" && pwd)/$(basename "$OUT")}}
TEX
echo "✓ portada $OUT"
