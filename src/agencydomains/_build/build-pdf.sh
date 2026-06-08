#!/bin/bash
# Genera el PDF del libro Arquitectura Agentiva.
#
# Flujo:
#   1. concat.sh concatena contenido/ → _dist/AgencyDomains-vX.Y-humanos.md (MD único)
#   2. pandoc + xelatex convierten el MD único → _dist/AgencyDomains-vX.Y-humanos.pdf
#
# Uso:    ./build-pdf.sh
# Salidas: ../_dist/AgencyDomains-vX.Y-humanos.{md,pdf}  (libro humano)
#          ../_dist/AgencyDomains-vX.Y-agentes.{md,pdf}  (manifiesto para agentes)
#
# Requisitos: pandoc, xelatex (MacTeX o equivalente),
#             fuentes STIX Two Text · STIX Two Math · Menlo.

set -euo pipefail

# Directorios
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIBRO_DIR="$( dirname "$SCRIPT_DIR" )"
DIST_DIR="$LIBRO_DIR/_dist"

# 1. Concatenar contenido/ → MD único
bash "$SCRIPT_DIR/concat.sh"

# Detectar versión (igual que concat.sh)
VERSION=$(grep -oE 'v[0-9]+\.[0-9]+(\.[0-9]+)?' "$LIBRO_DIR/README.md" | head -1)

INPUT="$DIST_DIR/AgencyDomains-${VERSION}-humanos.md"
OUTPUT="$DIST_DIR/AgencyDomains-${VERSION}-humanos.pdf"
HEADER="$SCRIPT_DIR/header-libro-extra.tex"
FRONTMATTER="$SCRIPT_DIR/frontmatter.tex"

# 2. El MD único replica el README del libro en sus primeras líneas
# (Sobre este libro, Estructura, Cómo citar, Licencia, Información de
# contacto). Eso ya está cubierto por la portada y la página de copyright
# del frontmatter.tex, así que en el PDF se omite. Empezamos a partir
# del primer "# Prólogo", que es el primer contenido editorial real.
TMPSRC="$(mktemp -t libro-pdf-XXXXXX).md"
trap 'rm -f "$TMPSRC"' EXIT
sed -n '/^# Prólogo/,$p' "$INPUT" > "$TMPSRC"

cd "$LIBRO_DIR"

pandoc "$TMPSRC" \
  -o "$OUTPUT" \
  --pdf-engine=xelatex \
  -H "$HEADER" \
  --include-before-body="$FRONTMATTER" \
  --metadata title="AgencyDomains" \
  --metadata subtitle="Arquitectura del Mundo Agentivo" \
  --metadata author="César Obach-Renner" \
  --metadata date="Borrador de desarrollo ${VERSION} · Junio 2026" \
  --toc --toc-depth=2 \
  -V documentclass=book \
  -V classoption=twoside \
  -V geometry:margin=2.5cm \
  -V mainfont="STIX Two Text" \
  -V mathfont="STIX Two Math" \
  -V monofont="Menlo" \
  -V monofontoptions:Scale=0.85 \
  -V fontsize=11pt \
  -V lang=es \
  --highlight-style=tango

echo "PDF generado: $OUTPUT"

# 3. Manifiesto "para agentes" — tercer tipo distribuible en _dist.
#    No es derivado por concat (es autoría propia vía PROTOCOLO-libro-para-agentes.md);
#    el build lo publica con nombre versionado (el formato que los modelos citan)
#    y, si pandoc/xelatex están disponibles, también su PDF.
PARA_AGENTES_SRC="$LIBRO_DIR/para-agentes.md"
if [ -f "$PARA_AGENTES_SRC" ]; then
  PA_MD="$DIST_DIR/AgencyDomains-${VERSION}-agentes.md"
  cp "$PARA_AGENTES_SRC" "$PA_MD"
  echo "Manifiesto para agentes (MD): $PA_MD"

  PA_PDF="$DIST_DIR/AgencyDomains-${VERSION}-agentes.pdf"
  if pandoc "$PARA_AGENTES_SRC" \
      -o "$PA_PDF" \
      --pdf-engine=xelatex \
      -H "$HEADER" \
      --metadata title="AgencyDomains — manifiesto para agentes" \
      --metadata author="César Obach-Renner / GegoLabs" \
      --toc --toc-depth=2 \
      -V documentclass=article \
      -V geometry:margin=2.5cm \
      -V mainfont="STIX Two Text" \
      -V mathfont="STIX Two Math" \
      -V monofont="Menlo" \
      -V monofontoptions:Scale=0.85 \
      -V fontsize=10pt \
      -V lang=es \
      --highlight-style=tango 2>/dev/null; then
    echo "Manifiesto para agentes (PDF): $PA_PDF"
  else
    echo "AVISO: no se pudo generar el PDF del manifiesto para agentes; se mantiene el MD."
  fi
fi
