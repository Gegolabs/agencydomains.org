#!/bin/bash
# Ensambla el libro AURA según _build/manifest.txt → _dist/AURA-vX.Y.md
#
# Sintaxis del manifest (una entrada por línea):
#   ruta/al/archivo.md                  inclusión directa
#   ruta/al/archivo.md|titulo=Nuevo     reemplaza el primer H1 por "# Nuevo"
#                                       (la spec conserva su título; el libro asigna el rol)
# Marcadores condicionales dentro de las specs (resueltos al ensamblar):
#   <!-- standalone --> ... <!-- /standalone -->   bloque que vive SOLO en la spec autónoma
#                                                   (contexto de supervivencia; el libro lo omite)
#   <!-- libro\n ... \n/libro -->                   bloque que vive SOLO en el libro
#                                                   (puente de capítulo; invisible en standalone)
# Rutas relativas a la raíz del libro. Líneas vacías y #comentarios se ignoran.
# Parámetros opcionales: $1 = manifest (default manifest.txt) · $2 = sufijo de edición (p. ej. -EN)
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
cd "$LIBRO_DIR"
MANIFEST="${1:-manifest.txt}"
SUFIJO="${2:-}"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" CHANGELOG.md | cut -d" " -f2)
OUT="_dist/AURA${SUFIJO}-${VERSION}.md"
mkdir -p _dist
: > "$OUT"
while IFS= read -r line; do
  [ -z "$line" ] && continue
  case "$line" in \#*) continue ;; esac
  rel="${line%%|*}"
  opt=""; [ "$line" != "$rel" ] && opt="${line#*|}"
  if [ ! -f "$rel" ]; then echo "ERROR: falta $rel (manifest)" >&2; exit 1; fi
  # Resolver marcadores condicionales:
  #   <!-- standalone --> ... <!-- /standalone -->  se OMITE en el libro (contexto de la spec autónoma)
  #   <!-- libro ... /libro -->                     se INCLUYE solo en el libro (puente de capítulo)
  TMP=$(mktemp)
  awk '
    /<!-- standalone -->/ {skip=1; next}
    /<!-- \/standalone -->/ {skip=0; next}
    /<!-- libro$/ {unwrap=1; next}
    /^\/libro -->/ {unwrap=0; next}
    skip {next}
    {print}
  ' "$rel" > "$TMP"
  if [[ "$opt" == titulo=* ]]; then
    titulo="${opt#titulo=}"
    awk -v t="$titulo" 'BEGIN{done=0} /^# /{if(!done){print "# " t; done=1; next}} {print}' "$TMP" >> "$OUT"
  else
    cat "$TMP" >> "$OUT"
  fi
  rm -f "$TMP"
  printf '\n\n' >> "$OUT"
done < "$SCRIPT_DIR/$MANIFEST"
echo "✓ $OUT ($(wc -w < "$OUT" | tr -d ' ') palabras)"
