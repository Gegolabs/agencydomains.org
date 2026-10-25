#!/bin/bash
# Ensambla el sitio en _site/: el shell (site/, plantillas *.in) + los libros ya
# construidos en sus rutas URL + manifiestos y alias. Lo corre el workflow
# (publish.yml, paso «Ensamblar sitio») y cualquier build en seco: el mismo código.
# Requiere AGD_VERSION · AURA_VERSION · RTE_VERSION en el entorno y los _dist/ de
# los tres libros y de la trilogía. La casa se lee de casa.json (casa.py).
set -euo pipefail
: "${AGD_VERSION:?}" "${AURA_VERSION:?}" "${RTE_VERSION:?}"
DIST=src/agencydomains/_dist
ADIST=src/aura/_dist
RDIST=src/rte/_dist
mkdir -p _site
cp -R site/. _site/
# NO debe existir site/CNAME: el dominio lo sirve CloudFront y Pages
# publica sin custom domain. Un CNAME en el artefacto puede reponer el
# custom domain y meter al visitante en un bucle de redirects.
# Ver work/cloudfront-analytics/RUNBOOK.md §9 (repo agencydomains-org).
rm -f _site/CNAME
touch _site/.nojekyll
# El shell sale de plantillas (*.in): la casa (casa.json) y las versiones NO se
# escriben a mano. Las URLs del sitio llevan @SITIO@@BASE@ y los enlaces raíz
# @BASE@/, así que mudar la casa no toca el shell. llms.txt nombra cada
# manifiesto con su versión: el texto que lo describe y el enlace que lo acompaña
# salen del mismo lugar, así que no pueden divergir (llegaron a hacerlo: el texto
# decía v1.0 enlazando v1.2). La prosa sigue siendo editorial y se escribe.
SITIO=$(python3 .github/scripts/casa.py sitio)
BASE=$(python3 .github/scripts/casa.py base)
find _site -name '*.in' | while read -r f; do
  sed -e "s|@SITIO@|${SITIO}|g" -e "s|@BASE@|${BASE}|g" \
      -e "s/@AGD_VERSION@/${AGD_VERSION}/g" \
      -e "s/@AURA_VERSION@/${AURA_VERSION}/g" \
      -e "s/@RTE_VERSION@/${RTE_VERSION}/g" \
      "$f" > "${f%.in}"
  rm "$f"
done
if grep -rnE '@[A-Z_]+@' _site --include='*.html' --include='*.txt'; then
  echo "::error::quedaron marcadores sin sustituir en el shell — falta una variable en el sed."
  exit 1
fi
# los libros reemplazan cualquier placeholder del shell en su ruta
rm -rf _site/agencydomains _site/es/agencydomains _site/aura _site/es/aura _site/real-time-enterprise _site/es/empresa-tiempo-real
# AgencyDomains: EN → /agencydomains/ · ES → /es/agencydomains/
cp -R "$DIST/web-en" _site/agencydomains
cp -R "$DIST/web-es" _site/es/agencydomains
# AURA: EN → /aura/ · ES → /es/aura/
cp -R "$ADIST/web-en" _site/aura
cp -R "$ADIST/web-es" _site/es/aura
# La Empresa en Tiempo Real: EN → /real-time-enterprise/ · ES → /es/empresa-tiempo-real/
cp -R "$RDIST/web-en" _site/real-time-enterprise
cp -R "$RDIST/web-es" _site/es/empresa-tiempo-real
# manifiestos para agentes → raíz de cada idioma
mv _site/agencydomains/AgencyDomains-${AGD_VERSION}-agents-en.md  _site/
mv _site/agencydomains/AgencyDomains-${AGD_VERSION}-agents-en.txt _site/
mv _site/es/agencydomains/AgencyDomains-${AGD_VERSION}-agents-es.md  _site/es/
mv _site/es/agencydomains/AgencyDomains-${AGD_VERSION}-agents-es.txt _site/es/
mv _site/aura/AURA-${AURA_VERSION}-agents-en.md  _site/
mv _site/aura/AURA-${AURA_VERSION}-agents-en.txt _site/
mv _site/es/aura/AURA-${AURA_VERSION}-agents-es.md  _site/es/
mv _site/es/aura/AURA-${AURA_VERSION}-agents-es.txt _site/es/
mv _site/real-time-enterprise/RealTimeEnterprise-${RTE_VERSION}-agents-en.md  _site/
mv _site/real-time-enterprise/RealTimeEnterprise-${RTE_VERSION}-agents-en.txt _site/
mv _site/es/empresa-tiempo-real/EmpresaTiempoReal-${RTE_VERSION}-agents-es.md  _site/es/
mv _site/es/empresa-tiempo-real/EmpresaTiempoReal-${RTE_VERSION}-agents-es.txt _site/es/
# alias estables sin versión — siempre la edición vigente (los versionados quedan para cita exacta)
for ext in md txt; do
  cp _site/AgencyDomains-${AGD_VERSION}-agents-en.$ext      _site/AgencyDomains-agents-en.$ext
  cp _site/AURA-${AURA_VERSION}-agents-en.$ext              _site/AURA-agents-en.$ext
  cp _site/RealTimeEnterprise-${RTE_VERSION}-agents-en.$ext _site/RealTimeEnterprise-agents-en.$ext
  cp _site/es/AgencyDomains-${AGD_VERSION}-agents-es.$ext   _site/es/AgencyDomains-agents-es.$ext
  cp _site/es/AURA-${AURA_VERSION}-agents-es.$ext           _site/es/AURA-agents-es.$ext
  cp _site/es/EmpresaTiempoReal-${RTE_VERSION}-agents-es.$ext _site/es/EmpresaTiempoReal-agents-es.$ext
done
# alias estables para los PDF — el enlace que se comparte no debe caducar.
# Medido el 2026-09-08: 1.351 peticiones 404 a distribuibles de ediciones
# retiradas, 642 de ellas a AgencyDomains-v0.4-en.pdf.
cp _site/agencydomains/AgencyDomains-${AGD_VERSION}-en.pdf                _site/agencydomains/AgencyDomains-en.pdf
cp _site/es/agencydomains/AgencyDomains-${AGD_VERSION}-es.pdf             _site/es/agencydomains/AgencyDomains-es.pdf
cp _site/aura/AURA-${AURA_VERSION}-en.pdf                                 _site/aura/AURA-en.pdf
cp _site/es/aura/AURA-${AURA_VERSION}-es.pdf                              _site/es/aura/AURA-es.pdf
cp _site/real-time-enterprise/RealTimeEnterprise-${RTE_VERSION}-en.pdf    _site/real-time-enterprise/RealTimeEnterprise-en.pdf
cp _site/es/empresa-tiempo-real/EmpresaTiempoReal-${RTE_VERSION}-es.pdf   _site/es/empresa-tiempo-real/EmpresaTiempoReal-es.pdf
# manifiesto unificado de la trilogía (URL estable, sin versión en el nombre)
cp src/trilogia/_dist/AgentiveWorld-Trilogy-agents-en.md  _site/
cp src/trilogia/_dist/AgentiveWorld-Trilogy-agents-en.md  _site/AgentiveWorld-Trilogy-agents-en.txt
cp src/trilogia/_dist/Trilogia-MundoAgentivo-agentes-es.md _site/es/
cp src/trilogia/_dist/Trilogia-MundoAgentivo-agentes-es.md _site/es/Trilogia-MundoAgentivo-agentes-es.txt
# alias corto: el nombre que la portada muestra es la URL
cp src/trilogia/_dist/AgentiveWorld-Trilogy-agents-en.md  _site/trilogy.md
cp src/trilogia/_dist/Trilogia-MundoAgentivo-agentes-es.md _site/es/trilogia.md
echo "=== contenido del artefacto ===" && find _site -maxdepth 2 | sort
