#!/bin/bash
# Ensambla el manifiesto unificado de la trilogía para agentes (ES y EN).
# La fuente de verdad son los manifiestos por libro; este artefacto es GENERADO.
# Uso: ./build-agentes.sh    → _dist/Trilogia-MundoAgentivo-agentes-{es,en}.md
set -euo pipefail
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SRC="$( dirname "$SCRIPT_DIR" )"
DIST="$SCRIPT_DIR/_dist"
mkdir -p "$DIST"

SEP_I="═══════════════════════════════════════════════════════════════════"

build_lang() {
  local header="$1" out="$2" p1="$3" p2="$4" p3="$5" t1="$6" t2="$7" t3="$8"
  {
    cat "$SCRIPT_DIR/$header"
    for entry in "$t1|$p1" "$t2|$p2" "$t3|$p3"; do
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
  postchat/para-agentes.md aura/para-agentes.md agencydomains/para-agentes.md \
  "PARTE I · POSTCHAT — manifiesto canónico (espejo de Postchat v0.3)" \
  "PARTE II · AURA — manifiesto canónico (espejo de AURA v0.3)" \
  "PARTE III · AGENCYDOMAINS — manifiesto canónico (espejo de AgencyDomains v0.5)"

build_lang header-agents.md "$DIST/AgentiveWorld-Trilogy-agents-en.md" \
  postchat/para-agents.md aura/para-agents.md agencydomains/para-agents.md \
  "PART I · POSTCHAT — canonical manifest (mirror of Postchat v0.3)" \
  "PART II · AURA — canonical manifest (mirror of AURA v0.3)" \
  "PART III · AGENCYDOMAINS — canonical manifest (mirror of AgencyDomains v0.5)"
