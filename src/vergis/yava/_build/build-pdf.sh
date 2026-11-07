#!/bin/bash
# Construye el libro de Yava (Vergis · Tecnología Agentiva · A) en PDF, en español o en inglés,
# con la plantilla de los libros del sitio: la portada de la maqueta de la trilogía (aquí en el color
# de Vergis), la cabecera de los libros (src/agencydomains/_build/header-libro-extra.tex), STIX Two,
# pandoc + xelatex.
#
# Uso:     ./build-pdf.sh [es|en]        (sin argumento: los dos)
# Salidas: ../_dist/Yava-v<versión>-<es|en>.pdf  y  ../_dist/Yava-v<versión>-<es|en>.md (lo publicado, en MD)
# Requisitos: pandoc, xelatex, WeasyPrint (o uvx), pdfinfo; fuentes STIX Two Text · STIX Two Math · Source Code Pro.
#
# Tablas: pandoc las escribe como longtable, que repite su cabecera en cada página. Las que caben en una
# página no se rompen: posproceso.py cambia sus fines de fila por \\* (sin corte de página permitido).
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
YAVA_DIR="$( dirname "$SCRIPT_DIR" )"
SRC_DIR="$( cd "$YAVA_DIR/../.." && pwd )"
LIBROS_BUILD="$SRC_DIR/agencydomains/_build"
DIST="$YAVA_DIR/_dist"
VERSION="v$(grep -m1 -oE '^\| \*\*(Versión|Version)\*\* \| [0-9.]+' "$YAVA_DIR/es/yava.md" | grep -oE '[0-9.]+$')"
mkdir -p "$DIST"

if command -v weasyprint >/dev/null; then WP=(weasyprint)
elif command -v uvx >/dev/null; then WP=(uvx --from weasyprint weasyprint)
else echo "✗ falta WeasyPrint (o uvx)" >&2; exit 1; fi

construir() {
  local L="$1" W="$DIST/tmp-$1"
  rm -rf "$W"; mkdir -p "$W"
  local TITLE SUBTITLE DATE AUTH1 AUTH2
  if [ "$L" = es ]; then
    SUBTITLE="Arquitectura de lo determinista del AgencyDomain"; DATE="Versión ${VERSION#v} · Noviembre 2026"
  else
    SUBTITLE="Architecture of the deterministic part of the AgencyDomain"; DATE="Version ${VERSION#v} · November 2026"
  fi

  # 1. Portada (página 1, a sangre) desde la maqueta, en el color de Vergis
  local PORTADA="$W/portada-$L.pdf"
  "${WP[@]}" -q "$YAVA_DIR/portada/yava-$L.html" "$PORTADA"
  [ "$(pdfinfo "$PORTADA" | awk '/^Pages:/{print $2}')" = 1 ] || { echo "✗ la portada $L no salió en una página" >&2; exit 1; }
  cat > "$W/portada.tex" <<TEX
\\usepackage{pdfpages}
\\AtBeginDocument{\\pagenumbering{Alph}\\includepdf[pages=1,pagecommand={\\thispagestyle{empty}}]{$PORTADA}}
TEX

  # 2. Markdown: ficha, cuerpo y lo publicado
  python3 "$SCRIPT_DIR/prepara.py" "$L" "$YAVA_DIR/$L/yava.md" "$W" "$VERSION"
  cp "$W/Yava-$VERSION-$L.md" "$DIST/"

  # 3. Página de créditos: la ficha del documento, cómo citar y el contacto
  {
    echo '\clearpage'; echo '\thispagestyle{empty}'; echo '{\small'
    pandoc "$W/ficha-$L.md" -t latex
    echo '}'; echo '\clearpage'
  } > "$W/creditos.tex"

  # 4. pandoc → .tex
  cd "$YAVA_DIR/$L"
  pandoc "$W/cuerpo-$L.md" -s -o "$W/yava.tex" \
    -f markdown-implicit_figures+autolink_bare_uris \
    -H "$LIBROS_BUILD/header-libro-extra.tex" -H "$SCRIPT_DIR/header-yava.tex" -H "$W/portada.tex" \
    --include-before-body="$W/creditos.tex" \
    --metadata title="Yava" --metadata subtitle="$SUBTITLE" \
    --metadata author="César Obach-Renner · Simón Alero" --metadata date="$DATE" \
    --toc --toc-depth=2 --number-sections --shift-heading-level-by=-1 --top-level-division=section \
    -V documentclass=book -V classoption=twoside -V papersize=letter -V geometry:margin=2.5cm \
    -V mainfont="STIX Two Text" -V mathfont="STIX Two Math" \
    -V monofont="Source Code Pro" -V monofontoptions:Scale=0.85 \
    -V fontsize=11pt -V lang="$L" -V colorlinks=true -V linkcolor=black -V urlcolor=vergis -V toccolor=black \
    --highlight-style=tango
  python3 "$SCRIPT_DIR/posproceso.py" "$W/yava.tex"

  # 5. xelatex (tres pasadas: índice y referencias)
  for _ in 1 2 3; do
    xelatex -interaction=nonstopmode -halt-on-error -output-directory="$W" "$W/yava.tex" > "$W/xelatex.log" 2>&1 \
      || { tail -40 "$W/xelatex.log" >&2; echo "✗ xelatex falló ($L)" >&2; exit 1; }
  done
  # 6. Lo que xelatex reporta y no detiene el build: se cuenta y se dice. Un glifo que falta sale como
  #    un cuadro vacío en la página, así que un «Missing character» detiene el build.
  local HB VB MC HH
  HB=$(grep -c 'Overfull \\hbox' "$W/yava.log" || true)
  VB=$(grep -c 'Overfull \\vbox' "$W/yava.log" || true)
  MC=$(grep -c 'Missing character' "$W/yava.log" || true)
  HH=$(grep -c 'headheight is too small' "$W/yava.log" || true)
  echo "  log de xelatex ($L): Overfull \\hbox $HB · Overfull \\vbox $VB · Missing character $MC · \\headheight corto $HH"
  grep -A1 'Overfull \\hbox' "$W/yava.log" | grep -v '^--' | sed 's/^/    /' | head -20 || true
  [ "$MC" = 0 ] || { grep 'Missing character' "$W/yava.log" | sort | uniq -c >&2; echo "✗ faltan glifos ($L)" >&2; exit 1; }
  cp "$W/yava.pdf" "$DIST/Yava-$VERSION-$L.pdf"
  echo "✓ $DIST/Yava-$VERSION-$L.pdf · $(pdfinfo "$DIST/Yava-$VERSION-$L.pdf" | awk '/^Pages:/{print $2}') páginas"
}

for L in ${1:-es en}; do construir "$L"; done
