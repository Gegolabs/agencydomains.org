# AgencyDomains — fuente del libro

Fuente en **Markdown** del libro *AgencyDomains · Arquitectura del Mundo Agentivo*.
Publicado en <https://agencydomains.org>. Licencia: **GNU FDL v1.3**.

## Estructura

- `contenido/` — el libro, un archivo por capítulo/sección (orden en `_build/manifest.txt`).
- `figuras/` — las 51 figuras (PNG).
- `para-agentes.md` — manifiesto canónico para agentes.
- `_build/` — scripts de construcción (Markdown único + PDF).

## Construir

Requiere `pandoc` y `xelatex` (MacTeX o equivalente) + fuentes STIX Two Text y Menlo.

```sh
bash _build/build-pdf.sh   # PDF + Markdown único + manifiesto de agentes (en _dist/)
bash _build/build-web.sh   # libro-web multipágina (una página por capítulo)
```

## Contribuir

Erratas y mejoras vía *pull request* sobre los archivos de `contenido/`.
Los artefactos de `_dist/` son **generados** — edita siempre la fuente.

---
Editado por **GegoLabs** · GNU FDL v1.3.
