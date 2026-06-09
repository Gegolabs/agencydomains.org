# agencydomains.org

Sitio y **fuente abierta** de la trilogía del **Mundo Agentivo** y su implementación de referencia.

Publicado en **https://agencydomains.org** vía GitHub Pages.

## Contenido

| Ruta | Qué es |
|---|---|
| `src/agencydomains/` | **Fuente canónica** del libro AgencyDomains (Markdown ES + EN, figuras, builds) — aquí llegan los *pull requests* |
| `src/_fonts/` | Tipografías del PDF (STIX Two · Source Code Pro), vendorizadas bajo SIL OFL |
| `site/` | Shell estático del sitio: landings EN/ES, `llms.txt`, assets, y las landings de `aura/` y `postchat/` (próximamente) |
| `.github/workflows/publish.yml` | El **publicador**: un tag `agencydomains-vX.Y` construye todo (web ES/EN, PDFs, manifiestos para agentes) y despliega a Pages |

Lo publicado (el libro navegable, los PDFs, los manifiestos `AgencyDomains-vX.Y-agents-{en,es}.{md,txt}`)
**no vive en el repo**: lo construye y despliega el workflow en cada tag.

## Contribuir

Los libros se publican bajo **GNU Free Documentation License v1.3**. Su fuente Markdown vive en
`src/`. Para corregir una errata o proponer una mejora, abre un *pull request* sobre el archivo
correspondiente en `src/agencydomains/contenido/` (español, fuente primaria) o `src/agencydomains/contenido-en/` (inglés).

La **implementación de referencia (Vergis)** vive en su propio repositorio, bajo **AGPL-3.0**:
[github.com/gegolabs/vergis](https://github.com/gegolabs/vergis).

## Licencias

- **Libros / documentación:** GNU FDL v1.3 — ver `LICENSE`.
- **Vergis (código):** AGPL-3.0 — en su repositorio.

---
Editado por **GegoLabs**.
