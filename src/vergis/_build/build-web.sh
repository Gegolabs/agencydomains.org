#!/bin/bash
# Vergis en el sitio: sus documentos (cada uno con su build: PDF y edición web) y sus páginas
# (qué es Vergis, la colección, la biblioteca), en español y en inglés.
#
# Uso:     ./build-web.sh
# Salidas: ../_dist/web-en  (servida en /vergis/)  ·  ../_dist/web-es  (servida en /es/vergis/)
# Requisitos: los de cada documento (yava/_build/build-pdf.sh: pandoc, xelatex, WeasyPrint o uvx,
#             pdfinfo; fuentes STIX Two y Source Code Pro) y python3.
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VERGIS_DIR="$( dirname "$SCRIPT_DIR" )"

# los documentos de la colección, en su orden
for d in $(python3 -c "import json,sys; print(' '.join(x['id'] for x in json.load(open(sys.argv[1]))['documentos']))" "$VERGIS_DIR/sitio/documentos.json"); do
  echo "→ $d: PDF (es · en)"
  bash "$VERGIS_DIR/$d/_build/build-pdf.sh"
  echo "→ $d: edición web (es · en)"
  bash "$VERGIS_DIR/$d/_build/build-web.sh"
done

echo "→ páginas de Vergis"
python3 "$SCRIPT_DIR/build-sitio.py" "$VERGIS_DIR" "$VERGIS_DIR/_dist"
echo "✓ Vergis en $VERGIS_DIR/_dist/web-{en,es}"
