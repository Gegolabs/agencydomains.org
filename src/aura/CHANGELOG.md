# Changelog — AURA

Historial de versiones del libro *AURA · El Camino Agentivo*.

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
