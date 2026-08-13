# AURA — El Camino Agentivo

### Libro II de la trilogía del Mundo Agentivo

**Autor:** César Obach-Renner · **Editor:** GegoLabs
**Edición:** Primera edición · v1.0 · Agosto 2026

## Composición

La **Visión de AURA es la semilla del libro**: su contenido vive aquí como voz propia
(`contenido/introduccion.md`), no como spec referenciada. Las **5 specs componentes**
de la biblioteca `specs/` (que mantienen vida independiente como documentos
autónomos) entran como capítulos **por referencia**, envueltas por el hilado del libro.
El orden de concatenación vive en `_build/manifest.txt`; ensambla `_build/concat.sh`
(soporta `ruta|titulo=Rol` para retitular al componer sin tocar la spec).

```
Prefacio                        contenido/  (hilado)
Introducción                    contenido/  (la Visión de AURA, absorbida)
PARTE I · EL SABER              contenido/  (hilado)
  IRIS — 10 etapas              specs/1
  Data Canon                    specs/3
PARTE II · EL HACER             contenido/  (hilado)
  MOTOR — 7 niveles             specs/2
  Wingmap                       specs/4
PARTE III · EL PORTAFOLIO       contenido/  (hilado)
  Casos de Uso                  specs/5
Epílogo                         contenido/  (hilado)
ANEXOS
  A. Inventario de Casos de Uso contenido/  (curado del inventario municipal v6.6)
```

**Regla:** para corregir un capítulo-spec se edita la spec en `specs/` (una sola
fuente); para corregir la introducción o el hilado se edita `contenido/`. Nada se copia.

Las **figuras propias** del libro se cocinan en `specs/figuras-fuente/` (HTML →
PNG vía `render.sh`, sistema visual compartido con AgencyDomains) y salen a
`specs/figuras/`, de donde el build las embebe (`--resource-path`).

**`para-agentes.md`** es el manifiesto canónico para agentes — espejo condensado
de la edición vigente (patrón AgencyDomains), artefacto aparte del ensamblado:
no entra al manifest del libro y se actualiza a mano con cada versión. Ante
contradicción, el libro humano gana.

## Edición inglesa (bilingüe)

Fuentes EN: `contenido-en/` (espejo de `contenido/`) + `specs-en/` (espejo de
`specs/`, mismos nombres de archivo y marcadores) + `para-agents.md`
(manifiesto EN). Ensambla `_build/build-en.sh` vía `manifest-en.txt`
(`concat.sh` acepta manifest y sufijo como parámetros). Vocabulario canónico EN
heredado de la edición inglesa de AgencyDomains (agentive · the Nadella Line ·
the Quantum Leap · online/real-time enterprise); expansión del acrónimo:
**Agentive Unified Reference Architecture** (preserva A-U-R-A). Ejes: the
KNOWING axis · the DOING axis; partes: Knowing · Doing · The Portfolio.
**Pendiente**: figuras en inglés (hoy embebidas en español, igual que en
AgencyDomains).

## Build y publicación

Builds locales (salen a `_dist/`, ignorado): `_build/build-pdf.sh` (ES PDF),
`_build/build-en.sh` (EN MD + PDF + web), `_build/build-web.sh` (ES web). El
generador web y el header LaTeX se comparten con AgencyDomains
(`../agencydomains/_build/`). Publicar = empujar un tag `aura-vX.Y` (el
workflow construye y despliega todo el sitio).

Rutas publicadas: **EN como default** en `/aura/` · ES en `/es/aura/` ·
manifiestos para agentes en la raíz de cada idioma.

## Pendientes

- Prólogo (prologuista invitado: Jesús, candidato) — el libro se publica sin
  prólogo, al estilo AgencyDomains; entrará en una versión posterior.
- Figuras en inglés (compartido con AgencyDomains) y figuras propias para
  Wingmap y Casos de Uso.
