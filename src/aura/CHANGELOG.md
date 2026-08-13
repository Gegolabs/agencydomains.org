# Changelog — AURA

Historial de versiones del libro *AURA · El Camino Agentivo*.

## v1.0 — Agosto 2026

**Primera edición.** El libro se sanciona como obra publicada: el corpus queda
estable y citable, y las ediciones ES/EN quedan a la par. Respecto de la v0.3 no
hay cambios de contenido — lo que cambia es el estatuto: deja de presentarse como
borrador de desarrollo.

## v0.3 — Julio 2026
> **Revisiones dentro de v0.3** (auditoría integral + decisiones editoriales,
> 2026-07-03): oración final de IRIS rescatada del ensamblado; «Agentivo» en
> Wingmap + puente de apertura; CU-052/058 reclasificados a Área D (conteos
> 17/37/24/22); tesis duplicadas variadas en la edición-libro; manifiestos con
> estado real de publicación. Detalle en
> `editorial/auditorias/_correcciones-aplicadas-v0.3.md`.

**La pasada editorial.** Revisión integral de la trilogía (inventario en la
cocina del proyecto):

- **Sistema agentivo/agéntico unificado.** "Agéntico" queda reservado al mundo
  incremental (copilotos dentro de aplicaciones); Wingmap pasa a "levantamiento
  **agentivo**" y a "era agentiva" en todas sus formas, con nota de terminología
  alineada a la Introducción. Data Canon ya era conforme.
- **Duplicaciones de ensamblaje resueltas con guards.** "Inteligencia
  organizacional", "La convergencia" (ahora 4 conceptos también en IRIS
  standalone), el "par diagnóstico" con su figura y la "naturaleza diagnóstica"
  viven completos solo en las specs autónomas; el libro los remite a la
  Introducción con una línea.
- **Ciclo de inteligencia continua canónico**: Percibir → Interpretar → Decidir
  → Actuar → **Aprender**, idéntico en Introducción e IRIS (Etapa 8); la fórmula
  "detecta, interpreta, decide y actúa" deja de ser muletilla.
- **El Salto Cuántico se acuña bajo su definición** (La nueva economía de la
  información); la sección que describía la inversión del flujo se renombra.
- **Data Canon estrena puente de libro** (enlace desde IRIS y el eje SABER) y
  glosas de audiencia (agency-crítico, MDM, SLO, data marts); la cita de SLAs de
  Informatica en la Introducción ahora anticipa la política de un solo nivel.
- **Trust Infrastructure con puente de trilogía** en el glosario de MOTOR (misma
  primitiva que especifica *AgencyDomains*; aquí, umbral de madurez).
- **Residuos standalone limpiados**: tercera persona del autor (Wingworking),
  "versiones futuras de este capítulo", "La tercera fase" bajo Fase 2, typos;
  *El Futuro Agentivo* deja de citarse (la definición vive en la Introducción y
  el mapa de la serie).
- **Micro-sección «La trilogía»**: ancla el tránsito, glosa Data Mesh y BPM, y
  registra las **cinco** especificaciones (entra Casos de Uso).
- **El prólogo placeholder sale del build** hasta que llegue el texto del
  prologuista.
- **Rescate fundacional**: el **porcentaje agentivo** — el indicador de cruce
  del documento original de la Línea Nadella (dic-2024) — entra a la
  Introducción como complemento de posición al par diagnóstico.

## v0.2 — Junio 2026

Homogeneización de voz, figuras propias y **primera publicación** en
agencydomains.org (EN default en `/aura/`, ES en `/es/aura/`), sin prólogo —
estilo AgencyDomains; la fuente se gradúa a `src/aura/` en el repo del sitio.

- **Voz única de libro.** La autorreferencia "paper" desaparece — Data Canon y
  Wingmap hablan como capítulos; reescrituras donde la sustitución empobrecía la
  prosa. *Governance* → *gobernanza* en MOTOR. Trato al lector unificado en tuteo.
  El aparato de paper de Data Canon (palabras clave, agradecimientos) queda
  confinado a la spec autónoma vía marcadores standalone.
- **Cinco figuras propias** (sistema visual de la casa; fuentes en
  `specs/figuras-fuente/`): el mapa del camino (a01) y la Pirámide del Valor (a02)
  en la Introducción; el cuadrante IRIS×MOTOR (a03) en ambos capítulos del par;
  el mapa IRIS (a04); el mapa MOTOR (a05), que releva a la lámina legada AOMM v2.0.
- **Referencia rápida saneada.** El mapeo etapas↔niveles↔pirámide de IRIS —
  rendido tres veces en v0.1 — colapsa en la figura a04; la tabla ASCII inicial
  de MOTOR colapsa en a05. Las Vistas Rápidas de ambos modelos quedan declaradas
  como tablas de consulta.
- **Primer manifiesto canónico para agentes** (`para-agentes.md`), espejo de
  v0.2 con el patrón de AgencyDomains: modelos, transiciones, preguntas
  diagnósticas, marcos e instrumentos condensados + glosario canónico. El libro
  humano gana ante contradicción.
- **Edición inglesa completa**: `contenido-en/` + `../specs-en/` (espejos 1:1
  con los mismos marcadores standalone/libro) y `para-agents.md` (manifiesto EN
  con glosario re-alfabetizado). Vocabulario heredado de la edición EN de
  AgencyDomains; acrónimo expandido como *Agentive Unified Reference
  Architecture*. Build propio (`build-en.sh` + `manifest-en.txt`; `concat.sh`
  parametrizado). Figuras aún en español.

## v0.1 — Junio 2026

Primer ensamblaje. La **Visión de AURA** (v3) — la spec semilla del libro — se absorbe
como Introducción (voz propia del libro). Las 5 specs componentes entran como capítulos
por referencia desde la biblioteca `../specs/`:

1. **IRIS** (v3) — madurez de inteligencia organizacional, 10 etapas (eje SABER).
2. **MOTOR** (v3) — madurez de automatización organizacional, 7 niveles (eje HACER).
3. **Data Canon** (v1.0) — gobernanza de datos recentralizada bajo canon.
4. **Wingmap** (v1.0) — levantamiento agéntico de procesos sin entrevistas.
5. **Casos de Uso** (v1.0, nueva) — CU/SV, tres dimensiones, marco Citizen/City/DUAL,
   disciplina de ROI, portafolio real de gobierno local como caso ilustrativo.

Hilado original de esta versión: prefacio, intros de parte (El Saber · El Hacer ·
El Portafolio) y epílogo. Prólogo pendiente (prologuista invitado).
