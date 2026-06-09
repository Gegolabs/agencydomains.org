# Inventario de Hallazgos — AgencyDomains v0.4 (edición -humanos)

|  |  |
|--|--|
| Documento auditado | *AgencyDomains — arquitectura del Mundo Agentivo*, Borrador v0.4 (edición -humanos) |
| Tipo | Libro canónico / especificación |
| Fecha de auditoría | 2026-06-05 |
| Auditor | Claude (Wingworking) |
| Alcance | Todo `contenido/` (24 archivos). Foco solicitado: redundancia, repetitividad, inconsistencia |
| Fuentes de verificación | El propio canon · Mandamientos (`~/.claude/CLAUDE.md`) · PROTOCOLO-libro-para-agentes · grafía oficial de protocolos públicos (A2A, MCP) |
| Estado | **Informe para revisión — sin correcciones aplicadas** |

## Resumen Ejecutivo

El libro está sólido en estructura y vocabulario; los hallazgos se concentran en **tres patrones** coherentes con la prioridad pedida:

1. **Repetición de mensajes clave (claim repetition) y duplicación cross-chapter** — el patrón dominante. Varias tesis se desarrollan completas en 3+ lugares (economía del Botlet bajo suscripción, "tiempo real = temporalidad continua", la triada de fronteras, interfaz MCP "no es A2A", distinción Asistente/Agente). Hay además **3 duplicaciones casi literales de párrafo** (Space≠Domain; costos de BI; bloque de citas de industria). La cifra **Gartner 40%** y la cita **"separa pilotos de producción"** son los elementos más sobre-repetidos.
2. **Inconsistencias de conteo** — dos visibles y dañinas: el **conteo de primitivas** ("siete" declarado pero seis enumeradas; glosario llama Faceta "sexta"; mapa trata Asistente/Agente como "eje") y el **conteo de fronteras del Epílogo** (heading "tres" vs cuatro reales vs figura "cuatro"). Más una inconsistencia normativa MUST/SHOULD entre Cap 5 §4 y Cap 8.
3. **Errores factuales y artefactos puntuales** — atribución "A2A propuesto por Anthropic" (es de Google); referencia rota "(Botlets §10)"; dos rastros evolutivos (Mandamiento #2); placeholders pendientes de v1.0 (Prólogo, contactos, licencia); erratas léxicas; fechas/atribuciones a verificar (episodio BG2; Stafford vs Fowler).

**Recomendación:** revisión **puntual dirigida** — no hay defecto estructural de fondo. Atacar primero las 3 inconsistencias de conteo (visibles al lector) y las 3 duplicaciones literales; luego consolidar los claims repetidos fijando un "dueño" por mensaje; cerrar con erratas y verificaciones factuales.

## Estadísticas

### Por Severidad

| Severidad | Cantidad |
|-----------|:--------:|
| CRÍTICO | 10 |
| IMPORTANTE | 24 |
| MENOR (patrones) | 9 |
| **Total** | **43** |

### Por Dimensión

| Dimensión | C | I | M | Total |
|-----------|:-:|:-:|:-:|:-----:|
| FACTUAL | 3 | 0 | 0 | 3 |
| NUMERIC (incl. conteos/normativa) | 2 | 1 | 1 | 4 |
| TERMINOLOGY | 0 | 1 | 2 | 3 |
| LEXICAL | 0 | 2 | 2 | 4 |
| CROSS-DUP (incl. claim repetition) | 3 | 11 | 1 | 15 |
| GAPS | 0 | 2 | 1 | 3 |
| STRUCTURAL | 1 | 3 | 0 | 4 |
| FRAMING | 0 | 2 | 0 | 2 |
| ARTIFACTS | 1 | 0 | 2 | 3 |
| NARRATIVE | 0 | 0 | 0 | 0 |
| Mandamiento #1 | 0 | 1 | 0 | 1 |
| Mandamiento #2 | 1 | 1 | 0 | 2 |

### Por Capítulo (focos principales)

| Capítulo | Hallazgos destacados |
|----------|----------------------|
| Frontmatter / Prólogo / Prefacio | placeholders v1.0; "Salto Cuántico" sin glosario |
| 1 · Línea Nadella | erratas; fecha BG2; CROSS-DUP transición con Cap 2; Mand.#1 heading |
| 2 · Mundo Agentivo | duplicación con Cap 7 (costos, citas); FRAMING AtScale; cifras repetidas |
| 3 · BCA | "Stafford" vs "Fowler"; "Mundo Agentic" |
| 4 · Arquitectura | Space≠Domain dup; cognición no-LLM dup interna; Asistente/Agente ×3; Mand.#2; Mand.#1; FRAMING; LEXICAL tics |
| 5 · Primitivas | economía suscripción ×3; MCP "no es A2A" dup; A2A→Anthropic; ref §10 rota; tripleta Cap/Conector/Plantilla ×3; interacción acotada ×4; conteo primitivas |
| 6 · Mercado | "siete actores Core"; ASCII desalineado; fecha mercado; typos |
| 7 · Aplicaciones | temporalidad continua dup con Cap 5; drill-through dup con Cap 4; cita AtScale no idéntica |
| 8 · Operación | MUST/SHOULD vs Cap 5; distinción fallback/continuidad dup |
| 9 · Vergis | nota de alcance solapa con Epílogo; capitalización agentia/soveria |
| Epílogo | conteo de fronteras roto; G1/G2/G3 triplicado; "Lo que estableció" vs frontmatter |
| Apéndices (glosario/mapa/referencias) | orden alfabético; entradas faltantes; mapa §1 omite Vergis; conteo primitivas |

---

## Hallazgos CRÍTICOS

### H-C01: Conteo de primitivas inconsistente ("siete" pero seis enumeradas)
| Campo | Valor |
|-------|-------|
| Dimensión | NUMERIC / consistency |
| Ubicación | Cap 4 (cierre), Epílogo "Lo que el libro estableció", glosario (Faceta, proto-Botlet), mapa-conceptual §1/§4/§10 |
| Texto | Epílogo: "Estableció **siete primitivas**: AgencyDomains, Botlets —con su pieza pre-forjada, el proto-Botlet—, Capabilities, Trust Infrastructure, la distinción Asistente/Agente Autónomo, y la Faceta" (se cuentan **seis** ítems); glosario: "Faceta — **Sexta primitiva**"; mapa §4: Asistente/Agente como "eje operativo", no primitiva |
| Problema | Tres artefactos discrepan: ¿son siete (proto-Botlet y Asistente/Agente contados) o seis (Faceta=sexta, proto-Botlet sub-pieza, Asistente/Agente=eje)? El lector que cuenta encuentra seis donde dice siete. |
| Corrección sugerida | Fijar el elenco canónico exacto en UN lugar y alinear: si son siete, enumerar proto-Botlet como ítem propio y revisar el rótulo "sexta" de Faceta; si Faceta es sexta, "siete" es incorrecto. |

### H-C02: Conteo de fronteras del Epílogo roto (tres vs cuatro)
| Campo | Valor |
|-------|-------|
| Dimensión | STRUCTURAL / NUMERIC |
| Ubicación | Epílogo (heading "Las tres fronteras vivas", figura, §"Frontera 4", "más allá de las tres fronteras"); mapa-conceptual §1 (lista cuatro con AgentNation) |
| Texto | Heading: "Las tres fronteras vivas" + "Tres áreas…"; figura alt: "Las cuatro fronteras vivas"; luego "## Frontera 4 — el horizonte institucional"; cierre "Más allá de las tres fronteras" |
| Problema | El rótulo dice tres; el contenido y la figura entregan cuatro. Se propaga en ≥4 puntos + el mapa. |
| Corrección sugerida | Unificar a "cuatro" (heading+texto+figura+cierre) o segregar explícito "tres fronteras técnicas + una institucional". |

### H-C03: Duplicación literal — premisa "Space ≠ Domain"
| Campo | Valor |
|-------|-------|
| Dimensión | CROSS-DUP |
| Ubicación | Cap 4 "Premisa fundacional — Space ≠ Domain" ↔ Cap 5 §1 (mismo título) |
| Texto | Dos párrafos ("Las palabras cargan corporeidad… Space nace describiendo extensión física…" / "El agente no tiene cuerpo…") **idénticos** + la misma cita destacada |
| Problema | ~2 párrafos clonados a ~90 líneas de distancia; Cap 4 ya remite a Cap 5 §1 para la spec. |
| Corrección sugerida | Conservar completo en Cap 5 §1; en Cap 4 reducir a una frase + referencia (dejando la cita destacada). |

### H-C04: Duplicación literal — costos de BI tradicional + "cuello de botella humano"
| Campo | Valor |
|-------|-------|
| Dimensión | CROSS-DUP |
| Ubicación | Cap 2 "La nueva economía de la información" ↔ Cap 7 "El problema histórico" |
| Texto | "…entre cien mil y quinientos mil dólares de setup… **todo esa** inversión entrega capacidad de responder solo aquellas preguntas que alguien previó…" — palabra por palabra en ambos (incluida la errata "todo esa") |
| Problema | Párrafo entero clonado + frase "el cuello de botella real… es la transferencia de conocimiento entre personas". |
| Corrección sugerida | Conservar las cifras en Cap 7 (corazón del caso); en Cap 2 versión resumida + referencia. Corregir "todo esa"→"toda esa" (en ambos). |

### H-C05: Duplicación — bloque de citas de industria BI
| Campo | Valor |
|-------|-------|
| Dimensión | CROSS-DUP |
| Ubicación | Cap 2 ↔ Cap 7 |
| Texto | Citas Tellius / Superwise / Cube + bloque AtScale (80%/100%, "el semantic layer no es nice-to-have") + ThoughtSpot/Salesforce/Databricks — casi textuales en ambos; Cap 7 incluso dice "Las citas que recogimos en el Capítulo 2 son representativas" y aun así las reproduce |
| Problema | El set completo de citas de vendors aparece dos veces. |
| Corrección sugerida | Desarrollo completo en Cap 7 ("consenso de la industria"); en Cap 2 dejar 1–2 citas + referencia. |

### H-C06: Atribución factual errónea — "A2A protocol propuesto por Anthropic"
| Campo | Valor |
|-------|-------|
| Dimensión | FACTUAL |
| Ubicación | Cap 5 §1 (domains-spec) |
| Texto | "…por ejemplo `MCP` federado, o el A2A protocol **propuesto por Anthropic**." |
| Problema | El protocolo **A2A (Agent2Agent) fue anunciado por Google** (2025); Anthropic es autor de MCP. Dato verificable y de alta visibilidad. Además "A2A protocol" sin formato `código`. |
| Corrección sugerida | "el protocolo `A2A` propuesto por **Google**". |

### H-C07: Referencia interna rota — "(Botlets §10)"
| Campo | Valor |
|-------|-------|
| Dimensión | ARTIFACTS |
| Ubicación | Cap 5 §5 (asistente-vs-agente-autonomo), Anti-patrón B |
| Texto | "…se desarrolla en Capítulo 5 §2 (Botlets §10)." |
| Problema | "§10" no existe en Botlets; resto de generación. |
| Corrección sugerida | Dejar "Capítulo 5 §2 (Botlets)". |

### H-C08: Rastro evolutivo en el cuerpo (Mandamiento #2)
| Campo | Valor |
|-------|-------|
| Dimensión | Mandamiento #2 |
| Ubicación | Cap 4 §1 |
| Texto | "Es lo que el lector probablemente entendió como 'GUI dinámica' **en versiones anteriores de este libro**." |
| Problema | Referencia explícita a versiones previas del propio libro en el cuerpo (no en el changelog, que sí es legítimo). |
| Corrección sugerida | "lo que suele entenderse como 'GUI dinámica'." |

### H-C09: Placeholders pendientes visibles (bloqueante v1.0)
| Campo | Valor |
|-------|-------|
| Dimensión | ARTIFACTS |
| Ubicación | Frontmatter (Prólogo "Por escribir"; web/repo/errata "por definir"; licencia "propuesta"), Prólogo (archivo placeholder), Prefacio (Watermark/Dedicatoria/Agradecimientos con instrucciones internas al autor visibles) |
| Problema | Marcadores de pendiente e instrucciones internas presentes en el documento. Legítimos como estado pre-1.0, pero quedan visibles. |
| Corrección sugerida | Completar antes de v1.0, o suprimir/ocultar en build hasta tenerlos. (No es error de contenido; es estado inacabado declarado.) |

### H-C10: Verificaciones factuales pendientes (fecha BG2 · autoría PoEAA)
| Campo | Valor |
|-------|-------|
| Dimensión | FACTUAL |
| Ubicación | Cap 1 (apertura) y Cap 3 (BCA) |
| Texto | Cap 1: "En **diciembre de 2024**, Satya Nadella… en el podcast BG2…" · Cap 3: "En *Patterns of Enterprise Application Architecture*, **Stafford** articula la distinción entre *domain logic*…" (el resto del párrafo atribuye a Fowler) |
| Problema | Ambos son datos verificables y de alta visibilidad (la fecha BG2 da nombre a la "Línea Nadella"; la distinción domain/application logic de PoEAA suele atribuirse a Fowler). Requieren verificación externa antes de v1.0. |
| Corrección sugerida | Confirmar fecha exacta del episodio BG2; confirmar autoría del capítulo PoEAA (probablemente "Fowler"). |

---

## Hallazgos IMPORTANTES

> Agrupados. Cada uno con dimensión · ubicación · problema · corrección.

**Claim repetition / duplicación cross-chapter:**

- **H-I01 · CROSS-DUP — Cifra Gartner 40% sobre-repetida (8+ veces)** + cita "Trust Infrastructure… separa pilotos de producción" como blockquote en Cap 4 y Cap 5 §4. *Corrección:* una aparición por capítulo clave; blockquote único en Cap 5 §4.
- **H-I02 · CROSS-DUP — Economía del Botlet bajo suscripción** ("…económicamente imposible") desarrollada completa en Cap 4, Cap 5 §1 y Cap 5 §2 (misma terna Claude Pro/ChatGPT Plus/Copilot). *Corrección:* sede única Cap 5 §2; los otros, frase + referencia. Corregir el puntero "sección siguiente" (domains-spec) → "§2".
- **H-I03 · CROSS-DUP — "Tiempo real = temporalidad continua"** triple (Cap 2, Cap 5 §2, Cap 7), con la analogía reporte=dashboard repetida. *Corrección:* sede Cap 5 §2; Cap 7 referencia.
- **H-I04 · CROSS-DUP — Interfaz Capa 2↔3 vía MCP "no es A2A"** casi literal en domains-spec ↔ botlets (botlets reconoce que la corrección vive en domains-spec pero la reproduce). *Corrección:* definición única en §1; §2 recorta a puntero.
- **H-I05 · CROSS-DUP/STRUCTURAL — Triada de fronteras** (cognición no-LLM · federación · mundo de carbono) desarrollada en Cap 4, Cap 5 §1 y Epílogo. *Corrección:* sede Epílogo; Cap 4 y §1 a frase + "ver Epílogo". (Las "Frontera de evolución" locales por primitiva sí se quedan.)
- **H-I06 · CROSS-DUP — Cognición no-LLM** párrafo casi idéntico DENTRO de Cap 4 (Capa 2 ↔ Frontera de evolución del capítulo). *Corrección:* dejar el desarrollo en una; la otra, nota mínima.
- **H-I07 · CROSS-DUP — Distinción Asistente vs Agente Autónomo** ("no es jerárquica / no es Asistente mejorado / roles distintos / el sistema maduro los compone") en Cap 4 (×2) y Cap 5 §5. *Corrección:* desarrollo en §5; menciones de Cap 4 a diferencia puntual + referencia.
- **H-I08 · CROSS-DUP — "Cuatro capas = radiografía, no slots / agnóstico a productos"** casi literal Cap 4 "Implementaciones de referencia" ↔ Epílogo "Lo que NO está en este libro". *Corrección:* declaración en Epílogo; Cap 4 a una frase.
- **H-I09 · CROSS-DUP — Distinción fallback agéntico vs continuidad operacional** desarrollada en Cap 5 §4 y re-narrada en Cap 8 (que debería solo operacionalizar). *Corrección:* Cap 8 asume la distinción (referencia a §4) y entrega solo lo nuevo (protocolo de campo, 4 modos, marcas de log).
- **H-I10 · CROSS-DUP — Generaciones G1/G2/G3** definición triplicada textualmente (Epílogo, glosario, vergis). *Corrección:* locus canónico único (Cap 5 §2 / glosario); Epílogo y Vergis referencian.
- **H-I11 · CROSS-DUP — Tripleta Capability/Conector/Plantilla** enunciada 3× en ~50 líneas (capabilities.md: párrafo de reserva + sección + lista del test). *Corrección:* anunciar una vez y remitir; condensar la lista del test.
- **H-I12 · CROSS-DUP — "Interacción declarada acotada"** núcleo ("sobre el snapshot, sin queries nuevas, reproducible, G1") reenunciado 4+ veces (párrafo + tabla + cierre de bullet + Faceta-en-pieza). Es la **concentración de redundancia más alta del libro**. *Corrección:* declararlo una vez con fuerza; la tabla y el cierre no deben repetir el párrafo.
- **H-I13 · CROSS-DUP — "Tres dinámicas de la transición"** (coexistencia evolutiva, asimetría entre funciones, reorganización del trabajo) solapadas entre cierre de Cap 1 y Cap 2, con la misma enumeración de funciones casi literal. *Corrección:* Cap 1 anticipa y delega a Cap 2.
- **H-I14 · CROSS-DUP — Cifras de mercado repetidas en Cap 1/Cap 2** (Gartner 40%, 21% gobernanza, mercado 7.3→139.2 mil M) 3–5× con bloque Cap 2 L145-149 reiterando L83. *Corrección:* lugar canónico por estadística; las demás referencian.
- **H-I15 · STRUCTURAL — "Lo que el libro estableció" (Epílogo) ↔ "Sobre este libro" (frontmatter)** recapitulan la misma lista. *Corrección:* diferenciar ángulo (frontmatter = mapa; Epílogo = qué queda establecido + qué queda abierto; comprimir el recuento).
- **H-I16 · STRUCTURAL — "Frontera de evolución" en ~7 secciones** con la triada repetida. *Corrección:* consolidar la triada en el Epílogo; conservar solo las fronteras locales específicas de cada primitiva.

**Inconsistencias:**

- **H-I17 · NUMERIC/normativa — MUST vs SHOULD** del mismo requisito: "Trazabilidad de transición a continuidad" es **SHOULD** en Cap 5 §4 y **MUST** en Cap 8. *Corrección:* unificar (probablemente MUST, por ser Cap 8 la operacionalización).
- **H-I18 · TERMINOLOGY — Capitalización de nombres propios de instancia** inconsistente: `agentia/Agentia`, `soveria/Soveria`, `ultrapro/ultraPRO` (domains-spec L101 vs L303; mapa; epílogo). *Corrección:* fijar grafía única y aplicarla.

**Mandamientos / Framing / Narrative:**

- **H-I19 · Mandamiento #1 — etiqueta-pregunta en negrita sin `¿…?`**: "**Por qué importa la primitiva.**" (Cap 4 §1). El libro usa la convención correcta en hermanos ("### ¿Por qué importa la distinción?"). *Corrección:* "**¿Por qué importa la primitiva?**". (Secundario: heading "## La pregunta que divide a la industria", Cap 1 — declarativo, pero desalineado con sus hermanos interrogativos; evaluar.)
- **H-I20 · Mandamiento #2 — rastros evolutivos menores**: "reemplaza la noción de 'API convertida en Capability'" (capabilities L44); "refina, no contradice la distinción Faceta vs Botlet" (facetas L75). *Corrección:* reformular en positivo/definitivo.
- **H-I21 · FRAMING — absolutismos**: "números que terminan los debates" + "precisión cercana al cien por cien" (AtScale, vendor con interés, Cap 2); "la separación de responsabilidades es **la causa, no la consecuencia**" (Cap 4). *Corrección:* atenuar ("según AtScale…"; "condición necesaria").
- **H-I22 · NARRATIVE — falsa precisión "siete actores Core"** (observabilidad-deepdive) — cifra dura que coincide con las filas de la propia tabla ilustrativa. *Corrección:* "los principales actores Core incluyen…".
- **H-I23 · GAPS — "Salto Cuántico"** acuñado y capitalizado (Cap 2) sin entrada en glosario ni en la lista de conceptos canónicos del prefacio. *Corrección:* si es canónico, agregarlo al glosario; si no, bajar capitalización.
- **H-I24 · ARTIFACTS/STRUCTURAL — observabilidad-deepdive sin figura** (único deep-dive sin `<!-- FIG -->`, rompe el patrón visual). *Corrección:* agregar una figura (las 6 capacidades / stack de observabilidad) o confirmar omisión deliberada.

---

## Hallazgos MENORES (por patrón)

### Patrón M1 · Erratas y anglicismos
**Instancias:** "revela**a**dora" (Cap 1); "**su** entrevistadores"→sus (Cap 1); "**Cualquier** de los dos"→Cualquiera (Cap 1); "**todo esa** inversión"→toda esa (Cap 2 y Cap 7, duplicada); "Compos**ada**"→Compuesta y "rol compuest**a**"→compuesto (facetas); "verifi**able**"→verificable (domains-spec ×2); "pro**pr**ietaria"→propietaria (cadena-valor); "las tres planos"→los tres planos (trust-policies); "Mundo **Agentic**"→Agéntico (BCA); "dressed up" sin cursiva/traducción (Cap 4). *Corrección:* barrido de corrección léxica.

### Patrón M2 · Tics léxicos (repetitividad de estructura)
**Instancias:** fórmula "Sin X…; con X…" ≥7× (Cap 4); enumeración ordinal "La primera/segunda/…" en 4 secciones seguidas (Cap 4); "código tradicional ejecuta mejor / sin invocar la cognición" 4× (Cap 4); "la especialización de dominio vive en los Botlets" 3× en ~15 líneas (botlets). *Corrección:* variar formulación; conservar la antítesis solo donde aporta.

### Patrón M3 · Grafía inconsistente del ciclo y de números
**Instancias:** `95 / 4 / 1` (con espacios) vs `95/4/1` (sin) en el mismo archivo (botlets); ciclo deletreado "noventa y cinco / cuatro / uno" en Cap 4 vs cifras en el resto; cifras vs palabras mezcladas (Cap 4 L293). *Corrección:* fijar convención y aplicarla.

### Patrón M4 · "son varios/varias" con el número a la vista
**Instancias:** "Las modalidades de la Capa 1 son **varias**…" (enumera 6); "Los componentes de la Capa 3 son **varios**…" (5); idem Capa 4 (Cap 4). Contrasta con "son cinco" (Capa 2). *Corrección:* usar el cardinal.

### Patrón M5 · Citas no idénticas / atribuciones vagas
**Instancias:** cita AtScale "no es nice-to-have" vs "no es **un** nice-to-have" (Cap 2 vs Cap 7); "algunos actores líderes", "la mayoría… a inicios de 2026" sin fuente (Cap 4); "en los próximos cinco años no se espera entrante…" como hecho (cadena-valor). *Corrección:* unificar la cita textual; marcar predicciones como tales.

### Patrón M6 · Fechas-ancla inconsistentes
**Instancias:** estado del mercado "mayo de 2026" (nota) vs "inicios de 2026" (cuerpo) vs "2026" (cadena-valor); prefacio "Mayo 2026" vs frontmatter "Junio 2026". *Corrección:* fijar una fecha-ancla por contexto.

### Patrón M7 · Glosario — orden y cobertura
**Instancias:** orden alfabético roto (AgencyDomain tras Agente; Atención antes de Asistente; subtipos de Botlet intercalados); faltan entradas para términos del Cap 9 nuevo (**códice propietario**, eval. **ucodex**, AGPL/GFDL, production grade); rótulo de primitiva solo en Faceta ("Sexta") y no en las demás. *Corrección:* reordenar; agregar entradas faltantes; criterio uniforme de rótulo.

### Patrón M8 · Mapa-conceptual — desajustes con v0.4
**Instancias:** el árbol §1 **omite el Capítulo 9 (Vergis)** que §10 sí incluye; "protocolo A2A" en Capa 3 podría leerse como la relación A2A (alinear con la terminología del glosario); capitalización Agentia/Soveria; término "umeeta" no presente en otros archivos (verificar). *Corrección:* insertar nodo Vergis en §1; precisar rótulos.

### Patrón M9 · ASCII art desalineado y tablas
**Instancias:** diagramas de 4 profundidades y del gateway con bordes `│` desfasados (cadena-valor); tabla de actores con 10 columnas omite eslabón 11 (Entorno) sin nota; referencias.md con encabezados de columna inconsistentes (`Link` vs `URL`, con/sin `Tema`) y faltan fuentes citadas en el Epílogo (DDD, GoF, Booch/UML). *Corrección:* re-cuadrar ASCII (o pasar a figura); unificar tablas; completar referencias.

---

## Verificaciones que resultaron CONSISTENTES (sin hallazgo)

- **Figuras = 51**: aritmética 44+7 correcta; `g01`–`g51` secuenciales; `g14` referenciada 2× (legítimo). Refs ↔ archivos sin huérfanos.
- **Ciclo 95/4/1, cadena 11×4, cinco pilares, cuatro capas, CRUDLEX (6 operaciones)**: valores consistentes en todo el libro.
- **"A2A interna"**: aparece solo en contexto **correctivo** (entrecomillado, explicando que no debe usarse). Correcto.
- **Referencias a capítulos**: Vergis = Capítulo 9 en todo el libro; ninguna a "Capítulo 10+".
- **Anonimización**: sin clientes/proyectos prohibidos (lista interna — redactada en la edición pública). (umeeta/agentia/soveria/ultrapro/ucodex son activos propios.)
- **Tríada manifestación / Instrumento de información / Producto de Información**: bien diferenciada (género→tipo→instancia, con cross-refs). proto-Botlet templado/platafórmico bien distinguidos, sin duplicación.
- **Mandamiento #1**: cumplimiento alto (≈44 headings con `¿…?`); única excepción real H-I19.

---

• *Generado con Wingworking · auditoría no destructiva — sin correcciones aplicadas*
