#!/bin/bash
# Libro-web del Libro I en un idioma, desde el Markdown único que deja libro.sh.
# Uso: web.sh <es|en> <DIR_SALIDA>
# La portada del PDF (página 1) se guarda también como portada.png del libro-web:
# la usa la tarjeta del libro en la portada del sitio.
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
DIST="$LIBRO_DIR/_dist"
WEBBUILD="$LIBRO_DIR/../agencydomains/_build/web-build.py"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" "$LIBRO_DIR/CHANGELOG.md" | cut -d" " -f2)
L="$1"; OUT="$2"
case "$L" in
  es) NAME=MuerteDelSoftware; TITLE="La muerte del software como lo conocemos"; BASE=/es/muerte-del-software; AGENTS=para-agentes.md;;
  en) NAME=DeathOfSoftware;   TITLE="The Death of Software as We Know It";      BASE=/death-of-software;     AGENTS=para-agents.md;;
  *) echo "uso: web.sh <es|en> <DIR_SALIDA>" >&2; exit 2;;
esac
MD="$DIST/$NAME-$VERSION.md"; PDF="$DIST/$NAME-$VERSION.pdf"
WMD="$DIST/$NAME-$VERSION-web.md"
sed 's#(\.\./figuras/#(figuras/#g' "$MD" > "$WMD"   # web-build.py sirve las figuras en <base>/figuras/
python3 "$WEBBUILD" \
  --md "$WMD" --figuras "$LIBRO_DIR/figuras" \
  --agents "$LIBRO_DIR/$AGENTS" --pdf "$PDF" \
  --name "$NAME" --title "$TITLE" --lang "$L" --base "$BASE" --out "$OUT" --version "$VERSION"
pdftoppm -png -r 60 -f 1 -l 1 -singlefile "$PDF" "$OUT/portada"
echo "✓ libro-web $TITLE ($L) en: $OUT"
