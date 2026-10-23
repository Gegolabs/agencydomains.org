#!/bin/bash
# Construye el interior de imprenta de La Empresa en Tiempo Real (edición ES)
# para impresión bajo demanda en Amazon KDP: trim 6×9 pulgadas (15,24 × 22,86 cm),
# sin sangrado, twoside con capítulos en recto, FDL 1.3 íntegra como apéndice y
# portadilla con el lugar del DOI-concepto. Mismo Markdown que build-pdf.sh.
#
# Márgenes (KDP, «Set trim size, bleed, and margins»,
# https://kdp.amazon.com/help/topic/GVBQ3CMEQW3W2VL6, consultado 2026-10-23):
# el margen interior mínimo depende del número de páginas; exterior, superior e
# inferior ≥ 0,25" sin sangrado. Aquí el interior es el mínimo de KDP más
# HOLGURA_LOMO (lectura cerca del lomo) y la caja incluye cabecera y pie, así
# que nada impreso queda fuera de los márgenes. Como el mínimo depende de las
# páginas y las páginas del margen, se compila hasta que el tramo se estabiliza.
#
# Lomo (KDP, «Create a Paperback Cover», https://kdp.amazon.com/help/topic/G201953020):
# páginas × 0,002252" en papel blanco y × 0,0025" en papel crema.
#
# Campos aún inexistentes (vacíos → hueco marcado «PENDIENTE» en la portadilla):
#   DOI_CONCEPTO=10.5281/zenodo.NNN  ISBN=978-...  COPYRIGHT='© 2026 …'
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
IMPRENTA="$( cd "$LIBRO_DIR/../_imprenta" && pwd )"
cd "$LIBRO_DIR"
bash "$SCRIPT_DIR/concat.sh"
VERSION=$(grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" CHANGELOG.md | cut -d" " -f2)
MD="_dist/EmpresaTiempoReal-${VERSION}.md"
PDF="_dist/EmpresaTiempoReal-imprenta-6x9-${VERSION}.pdf"
HEADER="$LIBRO_DIR/../agencydomains/_build/header-libro-extra.tex"
HOLGURA_LOMO="0.25"   # pulgadas sobre el mínimo de KDP
EXTERIOR="0.625"; SUPERIOR="0.5"; INFERIOR="0.5"   # todos ≥ 0,25" (KDP)
TMPSRC="$(mktemp -t rte-print-XXXXXX).md"
TMPPRE="$(mktemp -t rte-print-pre-XXXXXX).tex"
TMPPOST="$(mktemp -t rte-print-post-XXXXXX).tex"
trap 'rm -f "$TMPSRC" "$TMPPRE" "$TMPPOST"' EXIT

# El cuerpo: idéntico a build-pdf.sh (la trilogía + el libro desde el Prólogo,
# teasers → cajateaser).
{ awk '/^## La trilogía/{f=1} /^# Prólogo/{f=0} f' "$MD" | sed '1s/^## /# /'
  sed -n '/^# Prólogo/,$p' "$MD"; } > "$TMPSRC"
perl -0777 -i -pe 's{^> \*\*Lo que acabas de ver:\*\*\n>\n> ([^\n]*)\n>\n> \*(El comentario de esta escena: [^\n]*?)\.?\*\n}{::: {.cajateaser comentario="$2"}\n$1\n:::\n}gm' "$TMPSRC"

# Portadilla y créditos: los datos del libro y luego la plantilla compartida.
{ cat <<EOF
\\newcommand*{\\imprTitulo}{La Empresa en Tiempo Real}
\\newcommand*{\\imprSubtitulo}{Mundo Agentivo}
\\newcommand*{\\imprAutor}{César Obach-Renner}
\\newcommand*{\\imprEditor}{GegoLabs}
\\newcommand*{\\imprEdicion}{Primera edición ${VERSION} · Agosto 2026}
\\newcommand*{\\imprCita}{Obach-Renner, César. \\emph{La Empresa en Tiempo Real: Mundo Agentivo}. Primera edición ${VERSION}. GegoLabs, 2026.}
\\newcommand*{\\imprDOI}{${DOI_CONCEPTO:-}}
\\newcommand*{\\imprISBN}{${ISBN:-}}
\\newcommand*{\\imprCopyright}{${COPYRIGHT:-}}
EOF
  cat "$IMPRENTA/portadilla.tex"; } > "$TMPPRE"
sed "s|@FDL@|$IMPRENTA/fdl-1.3.tex|" "$IMPRENTA/apendice-fdl.tex" > "$TMPPOST"

# Mínimo de KDP para el margen interior según páginas (pulgadas).
gutter_kdp() {
  local p=$1
  if   [ "$p" -le 150 ]; then echo 0.375
  elif [ "$p" -le 300 ]; then echo 0.5
  elif [ "$p" -le 500 ]; then echo 0.625
  elif [ "$p" -le 700 ]; then echo 0.75
  else                        echo 0.875; fi
}

compilar() {   # $1 = margen interior en pulgadas
  pandoc "$TMPSRC" -o "$PDF" \
    --pdf-engine=xelatex -H "$HEADER" -H "$SCRIPT_DIR/header-fusion.tex" \
    -H "$IMPRENTA/header-imprenta.tex" -B "$TMPPRE" -A "$TMPPOST" \
    --lua-filter="$SCRIPT_DIR/teaser.lua" \
    -V title-meta="La Empresa en Tiempo Real" -V author-meta="César Obach-Renner" \
    --toc --toc-depth=1 \
    -V documentclass=book -V classoption=twoside -V classoption=openright \
    -V geometry:paperwidth=6in -V geometry:paperheight=9in \
    -V geometry:inner=${1}in -V geometry:outer=${EXTERIOR}in \
    -V geometry:top=${SUPERIOR}in -V geometry:bottom=${INFERIOR}in \
    -V geometry:includeheadfoot \
    -V mainfont="STIX Two Text" -V mathfont="STIX Two Math" \
    -V monofont="Source Code Pro" -V monofontoptions:Scale=0.85 \
    -V fontsize=11pt -V lang=es --highlight-style=tango
}

paginas() { pdfinfo "$PDF" | awk '/^Pages:/{print $2}'; }

MIN=0.375; INTERIOR=""
for intento in 1 2 3; do
  INTERIOR=$(printf '%.3f' "$(echo "$MIN + $HOLGURA_LOMO" | bc -l)")
  compilar "$INTERIOR"
  P=$(paginas)
  NUEVO=$(gutter_kdp "$P")
  echo "  pasada $intento: interior ${INTERIOR}\" (mínimo KDP ${MIN}\") → $P páginas"
  [ "$NUEVO" = "$MIN" ] && break
  MIN=$NUEVO
done
[ "$(gutter_kdp "$P")" = "$MIN" ] || { echo "ERROR: el margen interior no converge" >&2; exit 1; }

LOMO_BLANCO=$(echo "$P * 0.002252" | bc -l)
LOMO_CREMA=$(echo "$P * 0.0025" | bc -l)
echo "✓ $PDF"
printf '  páginas: %s · trim 6×9" · interior %.3f" (mínimo KDP %.3f" para %s páginas)\n' "$P" "$INTERIOR" "$MIN" "$P"
printf '  lomo: blanco %.4f" (%.2f mm) · crema %.4f" (%.2f mm)\n' \
  "$LOMO_BLANCO" "$(echo "$LOMO_BLANCO * 25.4" | bc -l)" "$LOMO_CREMA" "$(echo "$LOMO_CREMA * 25.4" | bc -l)"
for campo in DOI_CONCEPTO ISBN COPYRIGHT; do
  [ -n "${!campo:-}" ] || echo "  pendiente: $campo (hueco marcado en la portadilla)"
done
