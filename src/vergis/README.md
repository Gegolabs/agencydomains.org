# Vergis en el sitio

**Vergis · Tecnología Agentiva (A)**: la implementación de referencia de AgencyDomains. Su código vive en
[gegolabs/vergis](https://github.com/gegolabs/vergis) (AGPL-3.0); aquí vive lo que el sitio publica de Vergis,
bajo GNU FDL v1.3: la página que explica qué es, la colección de sus documentos y la biblioteca de referencias.

| Ruta | Qué es | Se publica en |
|---|---|---|
| `sitio/vergis.{es,en}.html` | Qué es Vergis, en simple (el cuerpo de la página) | `/es/vergis/` · `/vergis/` |
| `sitio/documentos.json` | La colección: los documentos, en su orden, con su resumen | `/es/vergis/documentos/` · `/vergis/documents/` |
| `sitio/biblioteca.json` | La biblioteca: las fuentes por tema, con su línea de «por qué importa» y dónde las cita cada documento | `/es/vergis/biblioteca/` · `/vergis/library/` |
| `yava/` | El primer documento: *Yava · Arquitectura de lo determinista del AgencyDomain* (ver su README) | `/es/vergis/yava/` · `/vergis/yava/` |
| `_build/build-web.sh` | Construye cada documento (PDF y web) y las tres páginas → `_dist/web-{es,en}` | el workflow las copia a `/es/vergis/` y `/vergis/` |
| `_build/build-sitio.py` | Las tres páginas, desde `sitio/` y desde la edición web ya construida de cada documento | — |

**Sumar un documento:** su carpeta `src/vergis/<id>/` con un `_build/build-pdf.sh` y un `_build/build-web.sh` que dejen
`_dist/<Título>-v<versión>-<es|en>.{pdf,md}` y `_dist/web-<es|en>/`, y su entrada en `sitio/documentos.json`.
**Sumar una fuente:** una entrada en `sitio/biblioteca.json`, con las secciones que la citan por su título; el build
falla si una cita no nombra una sección que exista, o si un capítulo de la colección no tiene su página.

Las páginas usan la plantilla del sitio (`site/assets/agencydomains.css` y `page.css`, sección «Vergis»), con el color de Vergis como acento.
