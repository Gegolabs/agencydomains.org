#!/bin/bash
# La edición web de Yava (una página por capítulo), en español y en inglés, con la plantilla de los
# libros del sitio (src/agencydomains/_build/web-build.py). Necesita los PDF de build-pdf.sh, que
# copia junto a las páginas con el Markdown publicado.
#
# Uso:     ./build-web.sh [es|en]        (sin argumento: los dos)
# Salidas: ../_dist/web-es  (servida en /es/vergis/yava/)  ·  ../_dist/web-en  (servida en /vergis/yava/)
# Requisitos: pandoc, python3.
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
YAVA_DIR="$( dirname "$SCRIPT_DIR" )"
DIST="$YAVA_DIR/_dist"
WEBBUILD="$YAVA_DIR/../../agencydomains/_build/web-build.py"
VERSION="v$(grep -m1 -oE '^\| \*\*(Versión|Version)\*\* \| [0-9.]+' "$YAVA_DIR/es/yava.md" | grep -oE '[0-9.]+$')"

construir() {
  local L="$1" BASE HOME_URL HOME_LABEL
  if [ "$L" = es ]; then BASE=/es/vergis/yava; HOME_URL=/es/vergis/documentos/; HOME_LABEL="← Vergis · documentos"
  else BASE=/vergis/yava; HOME_URL=/vergis/documents/; HOME_LABEL="← Vergis · documents"; fi
  local PDF="$DIST/Yava-$VERSION-$L.pdf" MD="$DIST/Yava-$VERSION-$L.md" OUT="$DIST/web-$L"
  [ -f "$PDF" ] && [ -f "$MD" ] || { echo "✗ falta $PDF o $MD: corre antes ./build-pdf.sh $L" >&2; exit 1; }
  python3 "$SCRIPT_DIR/web.py" md "$L" "$YAVA_DIR/$L/yava.md" "$DIST/web-$L.md" "$VERSION"
  rm -rf "$OUT"
  python3 "$WEBBUILD" --md "$DIST/web-$L.md" --figuras "$YAVA_DIR/$L/figuras" --pdf "$PDF" \
    --name Yava --title Yava --lang "$L" --base "$BASE" --out "$OUT" --version "$VERSION" \
    --home "$HOME_URL" --home-label "$HOME_LABEL"
  cp "$MD" "$OUT/"
  cp "$PDF" "$OUT/Yava-$L.pdf"   # alias sin versión: el enlace que se comparte no caduca
  python3 "$SCRIPT_DIR/web.py" enlaces "$OUT" "$BASE"
  echo "✓ Yava web ($L) en $OUT"
}

for L in ${1:-es en}; do construir "$L"; done
