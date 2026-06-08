#!/bin/bash
# Concatena los archivos de contenido/ en el orden definido por manifest.txt
# y produce el MD único distribuible en _dist/.
#
# Uso:    ./concat.sh
# Salida: ../_dist/AgencyDomains-vX.Y-humanos.md
#
# Variable VERSION del MD único se toma del README.md (línea "**Edición:**").

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
CONTENIDO_DIR="$LIBRO_DIR/contenido"
DIST_DIR="$LIBRO_DIR/_dist"
MANIFEST="$SCRIPT_DIR/manifest.txt"

# Detectar versión desde README (línea "**Edición:** ... · vX.Y")
VERSION=$(grep -oE 'v[0-9]+\.[0-9]+(\.[0-9]+)?' "$LIBRO_DIR/README.md" | head -1)
if [ -z "$VERSION" ]; then
  echo "ERROR: no se pudo detectar la versión desde README.md" >&2
  exit 1
fi

OUTPUT="$DIST_DIR/AgencyDomains-${VERSION}-humanos.md"

mkdir -p "$DIST_DIR"
: > "$OUTPUT"

while IFS= read -r relpath; do
  # Saltar líneas vacías y comentarios
  [ -z "$relpath" ] && continue
  case "$relpath" in \#*) continue ;; esac

  src="$CONTENIDO_DIR/$relpath"
  if [ ! -f "$src" ]; then
    echo "ERROR: no existe $src (referenciado en manifest.txt)" >&2
    exit 1
  fi

  cat "$src" >> "$OUTPUT"
  # Separar archivos con una LÍNEA EN BLANCO, no solo un salto de línea. Un
  # heading ATX (`# ...`) al inicio del archivo siguiente necesita una línea en
  # blanco antes; si queda pegado al último párrafo del archivo previo, pandoc
  # lo trata como continuación del párrafo (el `#` queda literal y el capítulo
  # desaparece del índice). Dos `\n` garantizan el separador sin importar cómo
  # termine cada fuente (las líneas en blanco extra son inocuas para pandoc).
  printf '\n\n' >> "$OUTPUT"
done < "$MANIFEST"

echo "MD único generado: $OUTPUT"
