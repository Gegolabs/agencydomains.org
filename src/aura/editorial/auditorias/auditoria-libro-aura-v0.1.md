# Inventario de Hallazgos — Libro AURA v0.1

|  |  |
|--|--|
| Documento auditado | *AURA · El Camino Agentivo*, borrador de desarrollo v0.1 (ensamblado de 2026-06-09, 40.140 palabras) |
| Tipo | Libro (borrador de revisión) |
| Fecha de auditoría | 2026-06-09 |
| Auditor | Claude (8 subagentes por capítulo + consolidación cross-chapter) |
| Fuentes consultadas | Specs originales de trabajo (`spec-aura/008-v3`, `informacion/iris/009-v3`, `procesos/motor/010-v3`, papers v1.0), `INVENTARIO-COMPLETO-V6-6.md`, `CITIZEN-CITY-DUAL.md`, manifest y ensamblado del libro, canon AgencyDomains (`twin/src/agencydomains/para-agentes.md`) |
| Fuentes no disponibles | DICCIONARIO del proyecto (no existe), validación externa de benchmarks citados |

## Resumen Ejecutivo

La base del libro es sólida: la curación de las specs resultó **verbatim e íntegra** (verificada por diff en IRIS, MOTOR e Introducción), los conteos estructurales cuadran en todas partes (10 etapas, 7 niveles, 100 CU, totales del anexo exactos contra fuente) y el marco Citizen/City/DUAL es fiel a su original. Los hallazgos se concentran en cuatro frentes: **(a) residuos mecánicos de la des-numeración §** en Data Canon y Wingmap (construcciones agramaticales "del «La…»", una referencia corrupta, dos con destino equivocado); **(b) costuras spec→libro** — referencias a documentos que ahora son capítulos del propio libro, aparato de spec sobreviviente (pies, notas de versión, fuentes con anclas "Link"), la numeración de capítulos fantasma del prefacio, y la duplicación de la tesis de IRIS contra la Introducción; **(c) anonimización**: Wingmap expone a Grupo Hijuelas y al proyecto A.R.B.O.L. con un dato negativo — bloqueante absoluto para publicación; **(d) un error factual propio** en Casos de Uso (composición de la SV #1). Recomendación: **revisión puntual extensa** (una sesión de correcciones quirúrgicas) — ningún hallazgo exige re-redacción mayor. Bloqueantes para publicar: H-C03/C04 (anonimización), H-C05 (figura rota), H-C07 (prólogo vacío).

## Estadísticas

### Por Severidad

| Severidad | Cantidad |
|-----------|:--------:|
| CRITICO | 7 |
| IMPORTANTE | 19 |
| MENOR | 32 (varios agrupados por patrón) |
| **Total** | **58** |

### Por Capítulo

| Capítulo | C | I | M |
|----------|:-:|:-:|:-:|
| Hilado (prefacio · partes · epílogo) | 1 | 3 | 6 |
| Introducción | — | 3 (+2 compartidos) | 3 |
| IRIS | — | 1 (+2 compartidos) | 3 |
| Data Canon | 1 | 2 | 7 |
| MOTOR | 1 | 2 | 8 |
| Wingmap | 3 | 5 (+1 compartido) | 3 |
| Casos de Uso | 1 | 2 (compartido c/Anexo) | 4 |
| Anexo A | — | 3 (1 compartido) | 6 |

Dimensiones dominantes: ARTIFACTS (costuras y residuos de transformación), CROSS-DUP (spec↔libro), TERMINOLOGY (agentivo/agéntico, Wingworking), NUMERIC (4 hallazgos reales sobre ~60 verificaciones — tasa baja).

---

## Hallazgos CRITICOS

### H-C01 · Data Canon — patrón agramatical "del «La/El…»" (×7)

| Campo | Valor |
|-------|-------|
| Dimensión | ARTIFACTS |
| Ubicación | `specs/3-data-canon.md` L97, 253, 271, 272, 273, 282, 297 |
| Texto | "se canaliza por la gobernanza federada del «La gobernanza recentralizada es federada…»" |
| Problema | Residuo de la transformación §N→«título»: la contracción "del" quedó pegada a títulos que abren con artículo. Siete instancias, detectables por cualquier lector. |
| Corrección | Reescribir cada una: "de la sección «…»" / "el argumento de «…»". |

### H-C02 · Wingmap — referencia corrupta con ".5" colgante

| Campo | Valor |
|-------|-------|
| Dimensión | ARTIFACTS |
| Ubicación | `specs/4-wingmap.md` L338 |
| Texto | "…con sub-sección «Definición y principios de la técnica».5 sobre métricas…" |
| Problema | El original decía "sub-sección §3.5" de un archivo EXTERNO; el reemplazo automático insertó un heading de este documento y dejó un ".5" huérfano. Sinsentido visible. |
| Corrección | "— KPIs de aplicación de la técnica, incluidas las métricas del grafo informacional." (o eliminar la entrada — ver H-C03). |

### H-C03 · Wingmap — 9 referencias a archivos del cluster + sección "Documentos del cluster"

| Campo | Valor |
|-------|-------|
| Dimensión | ARTIFACTS |
| Ubicación | L27, 49, 63, 80, 116, 142, 192, 238, 357 + sección L326-342 |
| Texto | "→ ver \`15-comparativa-pit.md\` §3.6 para…" |
| Problema | Referencias a archivos locales de trabajo, rotas para el lector del libro. La sección "Documentos del cluster" lista 15 archivos internos con metadata de sprint **y nombra al cliente A.R.B.O.L.** |
| Corrección | Eliminar las flechas "→ ver…" (las frases sobreviven sin ellas); reemplazar la sección por nota única ("este capítulo deriva de un cluster de investigación interno"); conservar solo Literatura externa y Referencias de mercado. |

### H-C04 · Wingmap — exposición de cliente (anonimización)

| Campo | Valor |
|-------|-------|
| Dimensión | FACTUAL / FRAMING |
| Ubicación | L57, L300, L332 |
| Texto | "el proyecto A.R.B.O.L. de Grupo Hijuelas — once iniciativas Quick Win… produjeron información del negocio en sólo dos o tres casos"; "holding agroindustrial chileno con 50 empresas, 7 países y aproximadamente 133 personas" |
| Problema | Nombra al cliente con (a) un dato negativo del engagement y (b) datos internos de estructura. El libro AgencyDomains anonimizó exactamente estos nombres (lista de anonimización del proyecto). "Aproximadamente 133" es además falsa precisión. |
| Corrección | Anonimizar ("un holding agroindustrial multinacional"); fijar el conteo exacto de Quick Wins o declararlo como orden de magnitud; "~130 personas". **Bloqueante para publicación.** |

### H-C05 · MOTOR — figura rota en el build del libro

| Campo | Valor |
|-------|-------|
| Dimensión | ARTIFACTS |
| Ubicación | `specs/2-motor.md` L54 |
| Texto | `![Modelo de Madurez MOTOR…](motor-maturity-v1.png)` |
| Problema | La ruta relativa no resuelve desde `specs/` ni desde el ensamblado: el PNG vive en `procesos/motor/`. Imagen rota garantizada en el PDF/web del libro. |
| Corrección | Crear `figuras/` del libro (o de la biblioteca specs/), copiar el PNG y ajustar la ruta; o enseñar a `concat.sh` a resolver figuras. |

### H-C06 · Casos de Uso — composición de la SV #1 falseada

| Campo | Valor |
|-------|-------|
| Dimensión | FACTUAL / NUMERIC |
| Ubicación | `specs/5-casos-de-uso.md` L108 (y L23) |
| Texto | "La SV mejor rankeada…, *Gestión Financiera Autónoma*, integra cuatro CU de nivel 6" |
| Problema | SV-GOB-012 es de nivel 6, pero sus componentes son CU-082 (n6), CU-083 (n6), CU-017 (**n2**) y CU-051 (**n4**). El capítulo confunde nivel de la SV con nivel de sus CU. En L23, además, lista componentes que no corresponden (incluye "detección de anomalías" = CU-010, que no es parte; omite el CU central CU-082). |
| Corrección | L108: "una SV de nivel 6 que integra cuatro CU — entre ellos el agente que gestiona el presupuesto completo y el que reasigna partidas". L23: alinear componentes con el inventario. |

### H-C07 · Prólogo — placeholder (mitigado: pendiente declarado)

| Campo | Valor |
|-------|-------|
| Dimensión | GAPS |
| Ubicación | `contenido/prologo.md` |
| Texto | "*(Pendiente — prologuista invitado.)*" |
| Problema | Sección vacía. Aceptable en v0.1 (pendiente declarado en README, candidato: Jesús); **bloqueante para cualquier publicación**. |
| Corrección | Completar antes de publicar, o excluir del manifest hasta que exista. |

---

## Hallazgos IMPORTANTES

| # | Cap | Dim | Hallazgo | Corrección |
|---|-----|-----|----------|------------|
| H-I01 | Prefacio | FACTUAL | Referencia capítulos numerados ("capítulo 1… capítulos 2 y 3…") que el libro no numera, y llama "La Visión" al capítulo cuyo H1 real es "Introducción". | Numerar capítulos vía manifest `\|titulo=` o reescribir el prefacio sin números; alinear el nombre. |
| H-I02 | Epílogo | FRAMING | "las proyecciones de cancelación masiva… tienen ahí su causa raíz" — Gartner da 3 causas (costos, valor poco claro, controles); el epílogo monocausaliza y dramatiza. | "…tienen ahí buena parte de su explicación". |
| H-I03 | Parte Hacer | FRAMING | "veinte años de BPM demostraron… batalla perdida" — el propio capítulo Wingmap matiza (industrias dinámicas vs estáticas). | "…es, en las industrias dinámicas, una batalla perdida". |
| H-I04 | Introducción | NUMERIC | "$7.3B → $139.2B (CAGR >40%)": el CAGR real es ≈38.7%, y es el único dato sin fuente. | "CAGR ≈39%" + fuente, o eliminar. |
| H-I05 | Introducción | NUMERIC | Bullets de "Datos de contexto" desalineados con la prosa: "antes de 2027" (vs "fines de 2027"), causa única de cancelación (vs triple), "48%… barrera principal" (vs "entre las barreras"). | Alinear los 3 bullets con la prosa (que es fiel a las fuentes). |
| H-I06 | Intro+IRIS | CROSS-DUP | "Empresa en línea vs tiempo real" definida 3 veces en la Introducción (la sección movida quedó presentando como nuevo lo ya leído) y la Tesis de IRIS duplica ~8 párrafos de la Introducción (agentiva/agéntica, tres ejes, Línea Nadella). | Decisión editorial: condensar la Tesis de IRIS a recap con remisión, o declarar capítulos autocontenidos (nota del frontmatter ya apunta ahí); reescribir la apertura de la sección movida como recapitulación. |
| H-I07 | Intro/IRIS | TERMINOLOGY | "etapas" y "niveles" alternados para IRIS sin regla; "una organización en Nivel 4" (L269) choca con "etapas 1–4". | Unificar: etapas = 10 de IRIS; niveles = vista simplificada (5) — y corregir L269. |
| H-I08 | Introducción | GAPS/ARTIFACTS | "Fuentes Principales": 32 filas con ancla "[Link]" (mueren en PDF impreso), 7 fuentes nunca citadas, 2 citadas ausentes. | Migrar a bibliografía del libro con cita formal; reconciliar con lo citado. |
| H-I09 | IRIS | ARTIFACTS | Cita la "Visión de AURA (ultraBASE, Febrero 2026)" como documento complementario externo (×2) — dentro del libro, ESA visión es la Introducción. | "ver la Introducción de este libro". |
| H-I10 | DataCanon+Wingmap | TERMINOLOGY | Costura agentivo/agéntico: keywords "IA agéntica" y "capa (semántica) agéntica" ×6 en Data Canon contradicen la distinción que el libro define; Wingmap usa "agéntico" con rigor propio pero sin puente al vocabulario del libro. | Data Canon → "agentiva" (keywords y capa; conservar "agentic semantic layer" una vez en inglés citado); Wingmap → una frase-puente en «La distinción pre-agéntico/agéntico». |
| H-I11 | Data Canon | STRUCTURAL | "Apéndice A — Glosario" y "Apéndice B — Notas de versión" del capítulo colisionan con el "Anexo A" del libro; el Apéndice B es metadata de proceso (1 fila). | Renombrar "Glosario del capítulo"; eliminar Apéndice B (su contenido va al CHANGELOG). |
| H-I12 | MOTOR | TERMINOLOGY | "Wing Working" (×8, incluye heading y glosario) — la práctica se llama **Wingworking**; el capítulo Wingmap lo escribe bien (×7). | Unificar a "Wingworking". |
| H-I13 | MOTOR | ARTIFACTS/FACTUAL | Nota de versión v2→v3 con linaje AOMM = rastro evolutivo impropio de libro (M1 transversal "sin rastros evolutivos"); además afirma que AOMM "se conserva archivado en el corpus AURA" — hoy vive en `lost+found/`, no en el corpus. | Mover la nota al historial del doc fuente; eliminar la afirmación de ubicación. Pie "*ultraBASE · v3 · Mayo 2026*" ídem. |
| H-I14 | Wingmap | ARTIFACTS | Dos referencias «…» defectuosas: L148 apunta a la sección equivocada (debía ser «Riesgos de privacidad y compliance»); L186 quedó agramatical ("del «La interfaz de validación»"). | Corregir destino y redacción. |
| H-I15 | Wingmap | NUMERIC | "Cinco fases" enunciadas pero seis desarrolladas (Fase 0–5), con ordinales en prosa desalineados ("la tercera fase" = Fase 2…). | "Cinco fases más una fase previa (Fase 0)" o renumerar; eliminar ordinales en prosa ("esta fase"). |
| H-I16 | Wingmap | NUMERIC | Regla "tres iteraciones del ciclo más corto" contradice sus propios ejemplos (3 iteraciones diarias = 3 días, no 2-4 semanas). | Reformular la regla (piso absoluto en semanas + mínimo de iteraciones). |
| H-I17 | Wingmap | FRAMING | "el cliente" ~25 veces — lenguaje de consultoría en un libro para practitioners. | Barrido → "la organización (observada)"; conservar "sponsor" donde el binomio sea el tema. |
| H-I18 | Wingmap | FACTUAL | "ProcessBench… F1 entre 0.4 y 0.7": ProcessBench es un benchmark de razonamiento matemático, no de inferencia de procesos; cifras sin fuente. Posible fabricación plausible. | Verificar fuente real o reformular como estimación del autor sin nombre de benchmark. |
| H-I19 | Casos de Uso | FACTUAL | SV #2: "cinco CU de nivel 3" no verificable (3 de sus componentes son CU-NEW sin nivel listado); "Organización sin Papeles" renombra a "Municipio sin Papeles" en la sección del caso *real* y lo describe como "trámite interno" siendo CITIZEN. | "una SV de nivel 3 que integra cinco CU"; usar el nombre real y beneficio ciudadano. |
| H-I20 | Casos+Anexo | TERMINOLOGY | Equivalencia AOMM↔MOTOR afirmada sin puente: el capítulo dice "nivel MOTOR", el anexo dice "corresponden al modelo MOTOR" pero conserva 2 headers "Nivel AOMM". | Renombrar headers del anexo a "Nivel MOTOR" (coherente con M1-transversal); opcional nota de trazabilidad al inventario original. |
| H-I21 | Anexo A | ARTIFACTS | 13 IDs `CU-NEW-###` como componentes de 5 SV sin existir en el listado de 100 ni explicarse. | Nota al pie ("casos adicionales del inventario fuente, fuera del catálogo de 100") o depurar las listas. |
| H-I22 | Anexo A | NUMERIC | "ROI Total: USD $117.95M/año" sin un solo sumando visible (las 30 SV dicen "ROI: N/A"); "Campos Especiales v6.3+" referencia un changelog eliminado. | Eliminar el campo ROI de las fichas y mantener el total calificado como referencial; retitular "Campos Especiales". |

---

## Hallazgos MENORES

### Patrones (multi-capítulo)

**P1 · Subtítulo como H3 bajo el H1** — Instancias: Introducción, Data Canon, Wingmap (y convención heredada en IRIS/MOTOR). Salto de jerarquía H1→H3; en la Introducción además el subtítulo es el nombre de AURA, no del capítulo. *Corrección:* convención única (línea en cursiva o H2 estilizado) aplicada al ensamblar.

**P2 · Pies de capítulo con metadata de spec** — IRIS "*ultraBASE · Febrero 2026*", MOTOR "*ultraBASE · v3 · Mayo 2026*". Rastro de producción por-documento, inconsistente entre capítulos. *Corrección:* eliminar pies; el frontmatter acredita.

**P3 · Tercer-resumen del mismo contenido** — IRIS: el mapeo etapas↔niveles↔pirámide se rinde 3 veces; MOTOR: "Vista Rápida" replica la tabla ASCII inicial + mapa de transiciones. *Corrección:* eliminar un render en cada caso o declararlos anexo de referencia rápida.

**P4 · Formato heredado del inventario (Anexo A)** — "ROI: N/A" ×30, campos camelCase (`valorSocial`), escala de Prioridad sin definir, leyenda A–D recién al final, "Area" sin tilde en headers de sección, headers dobles (## + ### redundante). *Corrección:* pasada única de formato sobre el anexo.

### Individuales

| # | Cap | Hallazgo · Corrección |
|---|-----|----------------------|
| M-01 | Epílogo | "matriz diagnóstica de AURA" — término acuñado en la última página; usar "par diagnóstico" o introducirlo antes. |
| M-02 | Prefacio/Epílogo | "infraestructura de confianza" al apuntar a AgencyDomains — la primitiva-marca es *Trust Infrastructure*; usar el término canónico (×2). |
| M-03 | Prefacio | "revierte la descentralización" sobresimplifica (el patrón recentraliza el núcleo y federa la periferia). |
| M-04 | Prefacio | El mapa del libro omite Epílogo y Anexo A. |
| M-05 | Prefacio vs intros de parte | Re-dicen las mismas descripciones con ~10 pp de distancia; diferenciar ángulo. |
| M-06 | Epílogo | "a donde siempre debieron estar" — absolutismo retórico de cierre (decisión de estilo consciente o suavizar). |
| M-07 | Introducción | "esta visión" ×4 — autorreferencia del doc fuente; sustituir por "este libro"/"AURA". |
| M-08 | Introducción | Emoji ⚠️ dentro de code block — verificar render XeLaTeX. |
| M-09 | Introducción | "#### La convergencia" anidada bajo empresa en línea/tiempo real cuando trata los 4 conceptos; promover. |
| M-10 | IRIS | Doble línea en blanco residual de la curación (L115-117). |
| M-11 | Data Canon | Referencias «El argumento, parte I/II» truncan los títulos reales — fijar convención (corta o completa). |
| M-12 | Data Canon | "Open Digital Architecture (Frameworx)" equipara dos marcos distintos de TM Forum; precisar (SID ∈ Frameworx, sucedido por ODA). |
| M-13 | Data Canon | "a prueba de balas" — absolutismo impropio de un paper con sección de falsadores. |
| M-14 | Data Canon | "la disputa semántica interna es no-disponible" — calco; "queda sin materia". |
| M-15 | Data Canon | Oración verbatim repetida entre Resumen y Conclusión (riesgo de agencia); parafrasear. |
| M-16 | Data Canon | "anclada a un canon central" como coletilla (~22 "anclado/a"); variar fuera de definiciones. |
| M-17 | Data Canon | Se autodenomina "paper" ×15 — decisión editorial pendiente (¿capítulos se presentan como papers?). |
| M-18 | MOTOR | Doble separador `---` huérfano (L95-99) — residuo de curación. |
| M-19 | MOTOR | Distribución de mercado suma ~101% (2025) y ~100.1% (2030); ajustar tramos. |
| M-20 | MOTOR | Nombres de nivel en 3 convenciones (EN / ES / bilingüe) según sección; fijar regla. |
| M-21 | MOTOR | "Prescriptivo Organizacional" — variante única del "DT Organizacional". |
| M-22 | MOTOR | Glosario sin entrada "Marketplace de Agentes" (única transición sin definir). |
| M-23 | MOTOR | Assessment pregunta 3 con lógica incoherente ("No → Nivel 1-2"); corregir o eliminar. |
| M-24 | MOTOR | "15 minutos vs 3 días" sin marco de ejemplo; marcar como ilustrativo. |
| M-25 | Wingmap | 5 entradas de literatura no citadas en el cuerpo (Pentland, Helmer, Hammer & Champy, Rother & Shook, MCP); *Learning to See* es 1999, no 2003. |
| M-26 | Wingmap | "se incompleta" (verbo no estándar); "…de un orden de magnitud… del orden de un orden de magnitud" (repetición torpe). |
| M-27 | Casos de Uso | "casi perfectamente balanceada" para 31/38/31 — desproporcionado; "razonablemente balanceada". |
| M-28 | Casos de Uso | "seis versiones mayores" — son 7 iteraciones menores dentro de v6 (v6.0–v6.6); ajustar. |
| M-29 | Casos de Uso | "45 obras simultáneas" — el CU dice "45 Proyectos". |
| M-30 | Casos de Uso | Nombres de área truncados (B omite Presupuesto, C omite Emergencias, D omite Deporte) ×3. |

---

## Verificaciones limpias (lo que NO falló)

- **Integridad de curación**: diff verbatim limpio en IRIS, MOTOR e Introducción — la curación solo tocó estructura, ni una palabra de contenido.
- **NUMERIC global**: ~60 verificaciones aritméticas pasadas (conteos de etapas/niveles/principios/fases-parcial, totales del anexo 100/30 exactos, distribuciones 31/38/31 y 19/37/24/20, estadísticas de la Introducción internamente consistentes, factor 4-10 de Wingmap, saltos de IRIS).
- **Fidelidad del Anexo A**: 0 desviaciones en 260+ líneas de datos contra el inventario fuente.
- **Marco Citizen/City/DUAL**: fiel al original, con genericización que mejora el framing.
- **Vocabulario de la trilogía**: expansión de AURA consistente; "Postchat"/"AgencyDomains"/"GegoLabs" correctos.
- **Referencias «…» de Data Canon**: 26 verificadas una a una — 23 exactas, todas semánticamente correctas (los defectos son los 7 "del «…»" gramaticales y 2 títulos truncados).

---

• *Generado con [Wingworking](https://wingworking.org)*
