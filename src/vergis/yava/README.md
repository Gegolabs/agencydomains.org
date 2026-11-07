# Yava — el libro

*Yava · Arquitectura de lo determinista del AgencyDomain* (*Yet Another Vergis Architecture*), de César Obach-Renner y Simón Alero: la arquitectura que da vida a todo lo determinista de un AgencyDomain, base determinista de Vergis. Tomo de **Vergis · Tecnología Agentiva (A)**, en español y en inglés.

| Ruta | Qué es |
|---|---|
| `es/yava.md` · `en/yava.md` | El texto: el cuerpo, el Anexo A y las fuentes |
| `es/figuras/` · `en/figuras/` | Las nueve figuras (PNG a 2×); la 2 y la 5, al cuádruple (`-2x`), van como láminas apaisadas a página completa |
| `portada/` | La portada: la maqueta de la trilogía (`src/trilogia/portada/portada.css`) en el color de Vergis |
| `_build/build-pdf.sh` | El libro en PDF: `./build-pdf.sh [es\|en]` → `_dist/Yava-v<versión>-<es\|en>.{pdf,md}` |

El build usa la plantilla de los libros del sitio: la cabecera `src/agencydomains/_build/header-libro-extra.tex`, STIX Two, pandoc y xelatex, más `_build/header-yava.tex` (secciones numeradas sin capítulos, láminas, tablas). Requisitos: pandoc, xelatex, WeasyPrint (o `uvx`) y pdfinfo.

Licencia: documentación bajo GNU FDL v1.3; el código de Vergis, bajo AGPL-3.0.
