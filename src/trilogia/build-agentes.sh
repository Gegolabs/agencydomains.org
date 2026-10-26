#!/bin/bash
# Ensambla el manifiesto unificado de la trilogía para agentes (ES y EN).
# La fuente de verdad son los manifiestos por libro; este artefacto es GENERADO.
# Uso: ./build-agentes.sh    → _dist/Trilogia-MundoAgentivo-agentes-{es,en}.md
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SRC="$( dirname "$SCRIPT_DIR" )"
DIST="$SCRIPT_DIR/_dist"
mkdir -p "$DIST"

ver() { grep -m1 -oE "^## v[0-9]+\.[0-9]+(\.[0-9]+)?" "$SRC/$1/CHANGELOG.md" | cut -d" " -f2; }
MUERTE_V=$(ver muerte); RTE_V=$(ver rte); AURA_V=$(ver aura); AGD_V=$(ver agencydomains)

SEP_I="═══════════════════════════════════════════════════════════════════"

# build_lang <cabecera> <salida> "<título>|<manifiesto>"… — las partes, en el orden de la trilogía
build_lang() {
  local header="$1" out="$2"; shift 2
  {
    cat "$SCRIPT_DIR/$header"
    for entry in "$@"; do
      local titulo="${entry%%|*}" archivo="${entry#*|}"
      echo ""
      echo "$SEP_I"
      echo "$SEP_I"
      echo "## $titulo"
      echo "$SEP_I"
      echo "$SEP_I"
      echo ""
      cat "$SRC/$archivo"
    done
  } > "$out"
  echo "✓ $out ($(wc -l < "$out" | tr -d ' ') líneas, $(wc -w < "$out" | tr -d ' ') palabras)"
}

build_lang cabecera-agentes.md "$DIST/Trilogia-MundoAgentivo-agentes-es.md" \
  "PARTE I · LA MUERTE DEL SOFTWARE COMO LO CONOCEMOS — manifiesto canónico (espejo de La muerte del software como lo conocemos $MUERTE_V)|muerte/para-agentes.md" \
  "PARTE II · LA EMPRESA EN TIEMPO REAL — manifiesto canónico (espejo de La Empresa en Tiempo Real $RTE_V)|rte/para-agentes.md" \
  "PARTE III · AURA — manifiesto canónico (espejo de AURA $AURA_V)|aura/para-agentes.md" \
  "PARTE IV · AGENCYDOMAINS — manifiesto canónico (espejo de AgencyDomains $AGD_V)|agencydomains/para-agentes.md"

build_lang header-agents.md "$DIST/AgentiveWorld-Trilogy-agents-en.md" \
  "PART I · THE DEATH OF SOFTWARE AS WE KNOW IT — canonical manifest (mirror of The Death of Software as We Know It $MUERTE_V)|muerte/para-agents.md" \
  "PART II · THE REAL-TIME ENTERPRISE — canonical manifest (mirror of The Real-Time Enterprise $RTE_V)|rte/para-agents.md" \
  "PART III · AURA — canonical manifest (mirror of AURA $AURA_V)|aura/para-agents.md" \
  "PART IV · AGENCYDOMAINS — canonical manifest (mirror of AgencyDomains $AGD_V)|agencydomains/para-agents.md"
