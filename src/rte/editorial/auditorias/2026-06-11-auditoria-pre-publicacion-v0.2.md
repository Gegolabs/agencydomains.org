# Inventario de Hallazgos — Postchat v0.2 (pre-publicación)

|  |  |
|--|--|
| Documento auditado | *Postchat: Mundo Agentivo* · borrador de desarrollo v0.2 (ES + EN) |
| Tipo | Libro (docuficción + comentario) |
| Fecha de auditoría | 2026-06-11 |
| Auditor | Claude (Wingworking con César Obach) |
| Fuentes consultadas | Fuente ES (`contenido/`), fuente EN (`contenido-en/`), manifiestos para agentes, CHANGELOG, shell del sitio (consistencia de trilogía) |
| Fuentes no aplicables | DICCIONARIO / organigrama / memorias (la obra es ficción compuesta; la verificación factual se ejecutó como **continuidad interna de la película** y consistencia ES↔EN) |

## Resumen Ejecutivo

El libro está estructuralmente sano: sin placeholders, sin referencias rotas, teasers correctamente apuntados a sus capítulos, terminología canónica consistente con la trilogía, edición EN con paridad 1:1. Los hallazgos relevantes son **tres errores de continuidad cronológica/narrativa en la película** — el tipo de error más dañino en una docuficción cuya fuerza es "se siente real" — y una nota de frontmatter desactualizada. Recomendación: **corrección puntual e inmediata; apto para publicar tras aplicarla.**

## Estadísticas

| Severidad | Cantidad |
|-----------|:--------:|
| CRITICO | 3 |
| IMPORTANTE | 1 |
| MENOR | 1 |
| **Total** | **5** |

## Hallazgos CRITICOS

### H-C01: La ratificación de Andrés llega después de haber sido anunciada

| Campo | Valor |
|-------|-------|
| Dimensión | NUMERIC (continuidad cronológica) |
| Capítulo | 15:00 · El agente de otro ↔ 17:00 · El cierre |
| Texto | 15:00: "A las 17:10, una línea en la pantalla… Andrés ratificó" · 17:00: "Andrés ratificó **hace veinte minutos**" (= 16:40) |
| Problema | El cierre de las 17:00 reporta como pasado un evento que la escena anterior fecha a las 17:10. La predicción del agente era "a eso de las cinco". |
| Corrección | 15:00: "A las 17:10" → **"A las 16:40"** (ES y EN). Coherente con la predicción y con el cierre. |

### H-C02: El plazo de la consulta ERP se contradice entre escenas

| Campo | Valor |
|-------|-------|
| Dimensión | NUMERIC (continuidad cronológica) |
| Capítulo | 11:00 · La reunión que no fue ↔ 17:00 ↔ Nocturno |
| Texto | 11:00: "Dales **cuarenta y ocho horas**" / "dentro de **dos días**" · 17:00: "plazo hasta **mañana a las once**" + "Tu briefing de **mañana** incluirá la síntesis" · Nocturno: "con plazo a las once" |
| Problema | 48 h desde el martes 11:00 = jueves 11:00; el cierre y el nocturno operan con miércoles 11:00. |
| Corrección | Mínima (1 archivo × 2 idiomas): 11:00 → **"Dales veinticuatro horas"** / **"mañana a esta hora tendrá sobre la mesa…"**. El cierre y el nocturno quedan consistentes sin tocarse. |

### H-C03: Elena defiende mañana el presupuesto — pero lo que defiende es el plan de mantenimiento

| Campo | Valor |
|-------|-------|
| Dimensión | FACTUAL (continuidad narrativa) |
| Capítulo | 15:40 · Los zapatos ↔ 7:00 ↔ 17:00 |
| Texto | Zapatos: "mañana defiende **el presupuesto** ante el comité" · 7:00: "el plan de mantenimiento **que defenderá mañana**" · 17:00: "mañana a las diez, la revisión del **plan de mantenimiento mayor**"; el presupuesto solo tiene "comentarios antes del viernes" (Finanzas, 7:00) |
| Problema | La escena de los zapatos confunde los dos artefactos: lo que se defiende mañana (con los zapatos) es el plan de mantenimiento; el presupuesto es un plazo de comentarios del viernes. |
| Corrección | Zapatos: "mañana defiende **el plan de mantenimiento** ante el comité" (ES y EN). |

## Hallazgos IMPORTANTES

### H-I01: Nota de versión del frontmatter desactualizada

| Campo | Valor |
|-------|-------|
| Dimensión | GAPS (staleness) |
| Capítulo | Frontmatter (ES y EN) |
| Texto | "Quedan pendientes el prólogo del invitado y **las figuras propias**." / "…and **the original figures** remain pending." |
| Problema | Las cinco figuras propias existen desde hoy (f01–f05, embebidas en los caps. 2, 3, 5 y la Conclusión). |
| Corrección | Dejar solo el prólogo como pendiente, y declarar que las figuras de la edición EN están en español (consistente con los otros dos libros). |

## Hallazgos MENORES

### H-M01: CHANGELOG v0.2 no registra las adiciones de la pasada final

El asiento `## v0.2` no menciona: figuras propias f01–f05, edición EN completa, sección "La trilogía", cajas de teaser, internacionalización de léxico. Al publicarse con tag `postchat-v0.2`, conviene que el asiento refleje el contenido real de la versión. **Corrección:** ampliar el asiento v0.2 antes del tag.

## Verificaciones que pasaron limpias

- ARTIFACTS: sin placeholders, TODO, IDs internos ni referencias rotas (el único "(Pendiente)" es el prólogo, declarado deliberadamente).
- Teasers: los 8 punteros "El comentario de esta escena" apuntan a los capítulos correctos.
- TERMINOLOGY: vocabulario canónico consistente con la trilogía (ES y EN); departamentos unificados (Distribución); léxico internacionalizado (sin chilenismos).
- Mandamiento 1: todos los headings-pregunta llevan `¿…?` en ES.
- NUMERIC global: 500×, 3–4 horas, 15–25 min, 41 mensajes, cuarenta mil empleados — consistentes en todas sus apariciones y entre idiomas.
- ES↔EN: paridad estructural 1:1 (23 archivos, mismos headings); cadenas canónicas exactas en los 8 teasers y 7 "essentials".

---

• *Generado con Wingworking*
