# La muerte del software como lo conocemos

### Libro I de la trilogía del Mundo Agentivo

**Autor:** César Obach-Renner · **Editor:** GegoLabs
**Edición:** Primera edición · v1.0 · Octubre 2026
**DOI:** [10.5281/zenodo.23674805](https://doi.org/10.5281/zenodo.23674805) (concepto: apunta siempre a la última versión)
*(Slug técnico del libro: `muerte`.)*

¿Por qué ahora? El punto de partida de la trilogía: por qué deja de ser la forma
de automatizar un negocio describirlo una vez y congelarlo en un software, qué se
pierde cuando cada organización construye el suyo, y qué pieza sobrevive al
cambio: el sistema de verdad.

## Fuentes

| Ruta | Qué es |
|---|---|
| `contenido/` | El libro en español (canónico) |
| `contenido-en/` | *The Death of Software as We Know It*, la edición en inglés (mismos archivos) |
| `para-agentes.md` · `para-agents.md` | Manifiestos canónicos para agentes (ES · EN) |
| `portada.html` · `portada-en.html` | La portada: el tomo I de la pila |
| `libro.css` · `notas-al-pie.lua` | Diseño del PDF (WeasyPrint) y notas al pie de página |
| `figuras/` | Las dos láminas ODA del TM Forum (© TM Forum, fuera de la GFDL) |
| `_build/` | `build-pdf.sh` (ES) · `build-en.sh` (EN: PDF + web) · `build-web.sh` (ES web) |

## Publicación

- EN: <https://agencydomains.org/death-of-software/> · ES: <https://agencydomains.org/es/muerte-del-software/>
- Distribuibles: `DeathOfSoftware-vX.Y-en.pdf` · `MuerteDelSoftware-vX.Y-es.pdf` y
  sus manifiestos `-agents-{en,es}.{md,txt}` en la raíz de cada idioma.
- Tag de publicación: `muerte-vX.Y`, que debe coincidir con el primer `## vX.Y` de `CHANGELOG.md`.

A diferencia de los otros tres libros, el PDF no se arma con XeLaTeX sino con
WeasyPrint (`_build/libro.sh`), el mismo armado con que se depositó la v1.0 en
Zenodo: el PDF del sitio es el del registro.

## Licencia

GNU Free Documentation License v1.3. Las figuras 1 y 2 son © TM Forum y quedan fuera de esta licencia.
