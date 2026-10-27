# Cambios de «La muerte del software como lo conocemos»

Las ediciones del libro, de la más nueva a la más vieja. Términos, estructuras y numeración son estables desde la v1.0; lo que cambie se anuncia aquí.

## v1.1 — El determinismo, dicho explícitamente

Tres cambios, en español y en inglés, a partir de comentarios de lectores de la v1.0.

- **El determinismo.** El capítulo 3 gana la sección «¿No salva el determinismo al software?», que expone como el argumento más fuerte en contra que, con las mismas entradas y el mismo proceso, las salidas deben ser las mismas, y que el no determinismo del agente impide la confianza que la autonomía requiere. El libro lo concede: en lo inmediato, el determinismo salva el sistema de verdad, el núcleo que tasa y factura y se sigue comprando (capítulo 7, que lo recoge en «¿Qué no se construye con agentes?»); lo que no salva es el negocio congelado a su alrededor. En el trabajo que el agente atiende, la capa determinista son los Botlets, que el agente cristaliza cuando una tarea deja de necesitar juicio (no software que alguien escribe para el agente); el Agentlet es el peldaño probabilístico y confina la imprevisibilidad; y la confianza la dan las capas de control del capítulo 6 y el contrato del capítulo 5. Dos notas nuevas citan la madurez del Botlet y la regla de contrabando de *AgencyDomains*. El glosario gana «determinismo» y «capa determinista»; los manifiestos para agentes, la regla correspondiente.
- **El epílogo**, retitulado «Qué muere, qué nace y qué sobrevive», se abre para el lector que llega por primera vez: cuenta la historia entera de corrido («¿Qué cuenta este libro?») antes de las tres decisiones del lunes («¿Qué puede decidir un directorio el lunes?»).
- **Segundo pase narrativo.** El prefacio cuenta el libro como una historia en tres movimientos; cada capítulo abre diciendo qué recorre y cierra con el puente al siguiente (cap. 1 a 7), el capítulo 2 gana «¿Qué queda de las dos muertes?», el 5 una lectura conjunta de las seis propiedades y «¿Cómo trabajan los agentes con él?» desarrollada en tres párrafos; en el 2, «¿Es legítimo copiar?» pasa antes de «¿Y qué no se copia?». No cambian cifras, citas, fuentes, términos ni figuras.

Desde esta edición el libro lo publica **Soveria Press**: firma como editorial en la portada, en la ficha del libro, en «Cómo citar», en el registro de Zenodo y en el colofón, que termina con «Publicado por Soveria Press» (en inglés, «Published by Soveria Press»). Gegolabs deja de ser el editor, y en las referencias a los otros libros de la trilogía el nombre se escribe Gegolabs.

Además, la página de dedicatoria del libro, después de la portada y antes del prefacio, y «Cómo citar» con el DOI de esta versión, 10.5281/zenodo.23693160, y el de todas las versiones, 10.5281/zenodo.23674805. Los PDF depositados en Zenodo no llevan el DOI de su propia versión, porque el registro no puede contenerlo antes de existir; lo llevan los PDF del repositorio y del sitio. Los PDF: `la-muerte-del-software-v1.1.pdf` y `la-muerte-del-software-v1.1-en.pdf`; con `REVISION=1 build.sh [es|en]` salen los de revisión (`-v1.1-revision`), con una marca visible de borrador en la dedicatoria y en «Cómo citar».

## v1.0 — Primera edición

La primera edición, en español.

### Edición en inglés

*The Death of Software as We Know It*, la traducción de la v1.0 (`contenido-en/`, `para-agents.md`, `portada-en.html`, `la-muerte-del-software-v1.0-en.pdf`, con `build.sh en`). Mismo texto, mismas figuras del TM Forum, que ya estaban en inglés; «Cómo citar» lleva el DOI de concepto 10.5281/zenodo.23674805. `para-agents.md` agrega, como los manifiestos de AURA y RTE, la oración que declara que el libro canónico es el español y que el manifiesto refleja la edición en inglés; y en la tabla de las capas, la pregunta de la quinta va en primera persona («Are we building it well?»), como en el cap. 6, donde `para-agentes.md` dice «¿Lo están construyendo bien?».
