# Correcciones v0.4 · nota de trabajo (NO se publica — se borra al cerrar)

Fuente única de verdad para aplicar los hallazgos de la auditoría. Edición **no destructiva**: corregir lo indicado, sin reescribir secciones enteras. Mantener Mandamientos (#1 ¿...?, #2 sin rastros evolutivos), anonimización y grafías canónicas.

---

## §A · DECISIONES CANÓNICAS (aplican a varios archivos)

### A1 · Conteo de primitivas = SIETE
Elenco canónico (7): **AgencyDomain · Botlet · proto-Botlet · Capability · Trust Infrastructure · Asistente vs Agente Autónomo · Faceta**.
- **Faceta conserva su ordinal "sexta primitiva"** (NO cambiar). **proto-Botlet es la "séptima primitiva"** (la más reciente). Los demás no llevan ordinal en el texto.
- **Asistente vs Agente Autónomo SÍ cuenta** como primitiva (distinción canónica), coherente con v0.3.
- **Recap canónico** (usar esta enumeración en epílogo y arquitectura, exactamente siete ítems distintos): *"siete primitivas técnicas canónicas: **AgencyDomain** como espacio computacional, **Botlet** como memoria muscular del agente, **proto-Botlet** como su pieza pre-forjada, **Capability** como árbol del saber cognitivo, **Trust Infrastructure** como infraestructura de confianza, la distinción **Asistente vs Agente Autónomo** como eje operativo, y la **Faceta** como unidad atómica de la Capa 1."*
- **glosario**: entrada proto-Botlet → "**Séptima primitiva canónica**"; Faceta → conservar "Sexta primitiva". (Rótulo de ordinal solo en Faceta y proto-Botlet; las otras sin ordinal — es deliberado: son las dos añadidas por versión.)
- **mapa-conceptual §1 (nodo LAS PRIMITIVAS)** y **§4** y **§10**: deben mostrar/contar las siete; en §4 etiquetar Asistente vs Agente como **primitiva-eje** (no solo "eje"), para no contradecir el conteo.

### A2 · Conteo de fronteras (Epílogo) = CUATRO
Hay cuatro fronteras vivas: tres **técnicas** (cognición no-LLM · federación entre AgencyDomains · mundo de carbono) + una **institucional** (soberanía / ciudadanía agentiva / AgentNation).
- Heading "## Las tres fronteras vivas" → "## Las cuatro fronteras vivas".
- Intro "Tres áreas… merecen explicitarse" → "Cuatro áreas…", aclarando "las tres primeras técnicas; la cuarta, institucional".
- Cierre "Más allá de las tres fronteras" → "Más allá de las cuatro fronteras".
- La figura (alt "Las cuatro fronteras vivas") y el mapa-conceptual §1 (que ya listan cuatro) quedan como están.

### A3 · Resoluciones factuales (verificadas)
- **Fecha BG2** "diciembre de 2024" → **correcta** (episodio 13-dic-2024). No tocar.
- **"Stafford"** (Cap 3, distinción domain/application logic) → **correcto** (patrón Service Layer de PoEAA, de Randy Stafford). Opcional: aclarar "en el patrón Service Layer de *PoEAA*". No es error.
- **A2A** → **es de Google**, no de Anthropic. CORREGIR (ver C·domains-spec).

### A4 · Política para placeholders pendientes de autor (H-C09)
NO fabricar contenido. Lo que requiere decisión/redacción del autor (Prólogo "Por escribir", Sitio web/Repositorio/Errata "por definir", Licencia "propuesta") **se deja**, pero se LIMPIAN las instrucciones internas visibles (notas tipo "placeholder para que César complete") dejando un marcador sobrio "(por completar)". Reportar estos como pendientes-de-autor, no como corregidos.

### A5 · Claim repetition — regla general
Para cada mensaje repetido: **una sede canónica** con el desarrollo completo; las demás apariciones se reducen a **una frase + referencia cruzada** ("ver Capítulo X §Y"). No borrar el concepto donde es localmente necesario; sí evitar re-derivarlo completo. NO introducir rastros evolutivos al recortar.

---

## §B · CORRECCIONES POR ARCHIVO

### contenido/00-frontmatter.md + 0-prologo/
- **M6**: en `0-prologo/prefacio.md`, fecha "Mayo 2026" → "Junio 2026" (alinear con v0.4).
- **H-C09 / A4**: en `prefacio.md`, secciones Watermark/Dedicatoria/Agradecimientos: quitar las instrucciones internas al autor; dejar "(por completar)". En frontmatter, dejar Prólogo/web/repo/licencia como pendientes sobrios (no inventar). `0-prologo/prologo.md` queda como pendiente de autor.
- **H-I23 / Salto Cuántico**: no es de frontmatter; ver glosario (agregar entrada).

### contenido/1-la-linea-nadella/la-linea-nadella.md
- **M1 erratas**: "revelaadora"→"reveladora"; "su entrevistadores"→"sus entrevistadores"; "Cualquier de los dos"→"Cualquiera de los dos".
- **H-I13 (CROSS-DUP con Cap 2)**: en el cierre "¿Cómo se cruza la línea?", REDUCIR las tres dinámicas (coexistencia evolutiva / asimetría entre funciones / reorganización del trabajo) a una mención breve + "el Capítulo 2 lo desarrolla". NO repetir la enumeración de funciones (finanzas, operaciones, atención al cliente, inventario) que vive en Cap 2.
- **H-I14 (cifras repetidas)**: dejar la cifra Gartner/mercado UNA vez aquí con referencia; el desarrollo de estadísticas vive en Cap 2.
- **H-I21 (framing)**: "el error en la otra es insolvencia técnica" — suavizar levemente (p. ej. "deuda arquitectónica difícil de revertir") manteniendo la fuerza.
- (heading "La pregunta que divide a la industria": se acepta como rótulo declarativo; NO cambiar.)

### contenido/2-mundo-agentivo/mundo-agentivo.md  ← SEDE de estadísticas de campo y citas de industria
- **H-C04 (KEEP resumida) / H-C05 (KEEP citas)**: Cap 2 conserva la versión **resumida** de costos de BI y 1–2 citas testimoniales; el desarrollo completo (cifras detalladas + bloque completo de citas) vive en Cap 7. (Coordinar: aquí resumir, Cap 7 mantiene completo… **decisión: el desarrollo completo de citas y costos queda en Cap 7**; Cap 2 deja versión corta + "ver Capítulo 7".) Corregir errata "todo esa"→"toda esa".
- **H-I14**: fijar las estadísticas (Gartner 40%, 21% gobernanza, mercado 7.3→139.2) como SEDE aquí, una vez; eliminar la reiteración interna (el bloque que repite lo ya dicho en el mismo capítulo).
- **H-I03 (tiempo real)**: la mención de "temporalidad continua" puede anticiparse brevemente (aquí nace "empresa en línea ≠ tiempo real") pero NO desarrollar la analogía completa (vive en Cap 5 §2).
- **H-I21 (framing AtScale)**: "números que terminan los debates"→atenuar ("según AtScale…"); "precisión cercana al cien por cien"→atribuir explícitamente al estudio de AtScale.
- **M5**: unificar la cita AtScale a su forma exacta (coordinar con Cap 7: usar idéntico texto). "no es un nice-to-have" (elegir una forma y usarla en ambos).
- **M8/Salto Cuántico**: "Salto Cuántico" se mantiene capitalizado (se agrega al glosario); aquí sin cambio salvo coherencia.
- **STRUCTURAL seis dimensiones vs tres ejes (M)**: añadir una frase que reconcilie ("los tres ejes agrupan las seis dimensiones").
- **M1**: "Mundo Agentic" no está aquí (está en BCA) — ver BCA.

### contenido/3-bounded-concerns-architecture/bounded-concerns-architecture.md
- **M1**: "Mundo Agentic" → "Mundo Agéntico" (convención canónica del Cap 1).
- **A3**: "Stafford" es correcto; opcional aclarar "(patrón Service Layer de *PoEAA*)". No forzar.

### contenido/4-arquitectura-agentiva/arquitectura-agentiva.md
- **H-C03 (Space≠Domain)**: REDUCIR el bloque duplicado a una frase + "el Capítulo 5 §1 lo desarrolla" (conservar la cita destacada si aporta). La versión completa vive en Cap 5 §1.
- **H-C08 (radiografía/agnóstico)**: la declaración "no mezclar arquitectura con producto para preservar la pretensión de estándar" se conserva en el **Epílogo**; aquí reducir a una frase. (La aclaración "radiografía del agente, no slots" SÍ se queda — es local y útil.)
- **H-C10 → A3**: sin cambios de fecha.
- **H-C08/H-C02 fronteras**: la triada de fronteras se desarrolla en el **Epílogo**; aquí reducir a frase + "ver Epílogo".
- **H-I06 (cognición no-LLM duplicada DENTRO de Cap 4)**: dejar el desarrollo en UNA de las dos ubicaciones (preferible la sección "Frontera de evolución" del capítulo o Capa 2, no ambas); la otra a nota mínima.
- **H-I02 (economía suscripción)**: reducir a frase + "ver Capítulo 5 §2".
- **H-I07 (Asistente vs Agente)**: en Capa 2 y Capa 3, reducir a la diferencia puntual + "ver Capítulo 5 §5"; no re-enunciar "no es jerárquica / roles distintos / los compone".
- **H-C08 (Mandamiento #2)**: "en versiones anteriores de este libro" → "lo que suele entenderse como 'GUI dinámica'." (eliminar la alusión a versiones).
- **H-I19 (Mandamiento #1)**: "**Por qué importa la primitiva.**" → "**¿Por qué importa la primitiva?**".
- **H-I21 (framing)**: "la separación de responsabilidades es **la causa, no la consecuencia**" → "es **condición necesaria**…" (atenuar el absolutismo de causa única).
- **Recap "siete primitivas" (final del cap)**: aplicar el recap canónico de §A1 (siete ítems distintos).
- **M2 (tics léxicos)**: variar la fórmula "Sin X…; con X…" donde se acumula (≥7 veces); variar las enumeraciones ordinales repetidas; "código tradicional ejecuta mejor" (2 ocurrencias a 8 líneas) variar una.
- **M3/M4**: "son varias/varios" → cardinal exacto ("son seis", "son cinco", "son siete") como en Capa 2; unificar grafía de números si fácil.
- **M1**: "dressed up" → "disfrazados" (o cursiva).

### contenido/5-primitivas/domains-spec.md
- **H-C06 (A2A→Google)**: "el A2A protocol propuesto por Anthropic" → "el protocolo `A2A` propuesto por **Google**".
- **H-I04 (MCP no es A2A)**: ESTA es la sede canónica de la interfaz Capa2↔3 y de la corrección A2A. Conservar completo aquí.
- **H-I02 (economía suscripción)**: reducir a puntero + "ver §2"; corregir "la sección siguiente" → "§2".
- **H-I18 (capitalización)**: unificar Agentia/Soveria/Vergis (elegir: **agentia, soveria** en minúscula como nombres de producto del Grupo Ultra — coherente con vergis.md; Vergis con mayúscula inicial por ser nombre de plataforma). Aplicar consistente.
- **M1**: "verifiable" → "verificable" (2 ocurrencias).
- **A1**: la def de AgencyDomain ya nombra Capabilities — sin cambio.

### contenido/5-primitivas/botlets.md  ← SEDE de economía-suscripción, manifestación/temporalidad, proto-Botlet, Botler
- **H-I04 (MCP)**: reconoce que la corrección A2A vive en domains-spec; RECORTAR la re-derivación a 1–2 frases + referencia a §1.
- **H-I02 (economía suscripción)**: SEDE canónica — conservar el desarrollo y la cita destacada aquí.
- **H-I03 (temporalidad)**: SEDE canónica de manifestación/temporalidad — conservar.
- **M2**: "la especialización de dominio vive en los Botlets" 3× en ~15 líneas → dejar 2 (cuerpo + cita).
- **M3**: unificar grafía del ciclo a `95/4/1` (sin espacios) en todo el archivo.
- **CROSS-DUP modo offline/senior con §1**: dueño de "Botlet senior" es §2; mantener aquí; §1 referencia.

### contenido/5-primitivas/capabilities.md
- **H-I11 (tripleta Cap/Conector/Plantilla 3×)**: el párrafo de reserva (sección "¿Qué NO es…?") anuncia y remite; la sección "tres entregables" es la sede; la lista del test (Capability vs no-Capability) condensar para no re-enunciar el mapeo capa por capa.
- **H-I20 (Mandamiento #2)**: "reemplaza la noción de 'API convertida en Capability'" → "Una API legacy, al traerse al Mundo Agentivo, se convierte en **Conector** (Capa 4), no en Capability." (sin "reemplaza la noción").
- **dos tests con título casi idéntico** ("¿Cuándo es Capability y cuándo no?" vs "¿Cuándo es Capability y cuándo feature?"): diferenciar encabezados (p. ej. "¿Capability o entregable de otra capa?" vs "¿Capability o feature interna?") y eliminar la re-narración intermedia.
- **STRUCTURAL tabla Conformidad**: alinear orden de filas con orden de secciones (menor).
- **M Narrative**: ejemplo de costeo usado 2× en la misma sección → segunda vez referir "el ejemplo ya citado".
- **TERMINOLOGY**: "capabilities" en minúscula en prosa → "Capabilities".

### contenido/5-primitivas/trust-infrastructure.md
- **H-I09 (fallback vs continuidad)**: SEDE de la distinción conceptual; conservar. La tabla de propiedades operacionales que pisa Cap 8 → dejar la operacional a Cap 8 (mover/recortar).
- **H-I17 (MUST/SHOULD)**: "Trazabilidad de transición a continuidad" — unificar a **MUST** (coincidir con Cap 8).
- **H-I12 no aplica aquí**.

### contenido/5-primitivas/facetas.md  ← mayor concentración de redundancia
- **H-I12 (interacción declarada acotada 4×)**: declarar el núcleo UNA vez (párrafo introductorio + tabla). Eliminar el bullet de cierre que resume la tabla (L67) y fundir el párrafo suelto de KPIs (L77) dentro de L71. Faceta-en-pieza conserva solo lo nuevo (el mecanismo), sin re-enunciar "sin queries / reproducible / G1".
- **H-I20 (Mandamiento #2)**: "**refina, no contradice** la distinción Faceta vs Botlet" → reformular en positivo ("la distinción admite un tercer uso: …").
- **M1**: "Composada"→"Compuesta"; "su rol compuesta"→"compuesto".
- **GAPS**: aclarar en Faceta-en-pieza que es la **pieza** (no la Faceta) la que compone, preservando el MUST de atomicidad.

### contenido/5-primitivas/asistente-vs-agente-autonomo.md
- **H-C07 (ref rota)**: "(Botlets §10)" → "(Botlets)".
- **M·CROSS-DUP**: "el humano… último loop de validación" — dejar en trust-infrastructure (Validación); aquí reducir a frase + referencia. "los cinco pilares… operacionalizados con disciplina" 3× → variar/consolidar.
- **M·cifra**: "cuarenta por ciento" → "más del cuarenta por ciento… (Capítulo 2)".

### contenido/6-mercado/cadena-valor-ia.md
- **M1**: "proprietaria" → "propietaria".
- **M·CROSS-DUP gateway**: el claim "conectar + controlar = gateway, ningún incumbente cubre ambos" 3× → enunciar una vez; las otras secciones añaden evidencia sin repetir la tesis.
- **M·fecha**: unificar "mayo de 2026" / "inicios de 2026" → una sola (usar la de la nota: "mayo de 2026").
- **M·NARRATIVE**: "en los próximos cinco años no se espera entrante…" → matizar ("es razonable esperar…").
- **M9 ASCII**: re-cuadrar los diagramas ASCII desalineados (4 profundidades; gateway) o dejar nota; **tabla actores**: nota al pie "Entorno (eslabón 11) omitido por ser externo a la cadena".
- **M·LEXICAL**: marcar cuáles actores son ilustrativos vs reales si fácil (menor).

### contenido/6-mercado/observabilidad-deepdive.md
- **H-I22 (falsa precisión)**: "siete actores Core" → "los principales actores Core incluyen…" (sin número derivado de la tabla).
- **H-I24 (sin figura)**: dejar nota/decisión — agregar figura es trabajo de la pasada de figuras; por ahora marcar como pendiente (NO bloquea). (No crear figura aquí.)

### contenido/7-aplicaciones-canonicas/conocimiento-tiempo-real.md
- **H-C04/H-C05**: SEDE del desarrollo completo de costos de BI y bloque de citas — conservar aquí; quitar la frase "Las citas que recogimos en el Capítulo 2 son representativas" si suena a repetición. Corregir "todo esa"→"toda esa".
- **H-I03 (temporalidad continua)**: reducir a frase aplicada al caso BI + "la spec de temporalidad vive en Capítulo 5 §2"; NO re-derivar el principio ni la analogía.
- **H-I0X drill-through**: este capítulo es dueño del PI (manifestación de información); el mecanismo drill-through se referencia a Cap 4 §1, sin repetir el ejemplo de cartera completo.
- **M5 cita AtScale**: forma idéntica a Cap 2.

### contenido/8-operacion/trust-policies-y-crudlex.md
- **H-I09 (distinción fallback/continuidad)**: asumir la distinción como dada (referencia a Cap 5 §4); entregar solo lo operacional (protocolo de campo, 4 modos, marcas de log), sin re-narrar la distinción.
- **H-I17 (MUST/SHOULD)**: alinear "Trazabilidad de transición a continuidad" a **MUST** (coincide con la corrección en trust-infrastructure).
- **M1**: "las tres planos" → "los tres planos".
- **H-I22/narrative**: "dos órdenes de magnitud" (L368) → reemplazar por las dos cifras concretas o "dos hallazgos de campo"; "el cuarenta por ciento… cancelados" → añadir "antes de fines de 2027".
- **M·GAP**: incluir constraint validation en el "mínimo viable" o explicar su omisión.

### contenido/9-implementacion-referencia/vergis.md
- **H-I05/nota de alcance**: diferenciar de "Lo que NO está en este libro" (Epílogo) — agregar que la nota de Vergis es sobre *canon vs implementación de referencia*; remitir a Epílogo para *lo que el libro omite*.
- **H-I10 (G1/G2/G3)**: "Frontera de evolución" de Vergis — referenciar la definición de generaciones (Epílogo/Cap 5), no redefinir.
- **H-I18**: capitalización agentia/soveria/ultrapro consistente (minúscula).

### contenido/10-epilogo/epilogo.md  ← SEDE de fronteras y "lo que el libro estableció"
- **H-C02 / A2 (fronteras = cuatro)**: aplicar A2 (heading, intro, cierre).
- **H-I05/H-I16 (triada fronteras)**: SEDE — conservar el desarrollo completo de las cuatro fronteras aquí.
- **H-C08 (radiografía/agnóstico)**: SEDE de "Lo que NO está en este libro" — conservar.
- **H-I10 (G1/G2/G3)**: SEDE del desarrollo de generaciones; el glosario y vergis referencian. (Aquí conservar; revisar que no repita verbatim el glosario.)
- **H-I15 (Lo que el libro estableció vs frontmatter)**: comprimir el recuento (puede ser lista de 1 línea por construcción) y dar el peso a las fronteras/abierto.
- **Recap "siete primitivas" (L17)**: aplicar recap canónico §A1 (siete ítems).

### contenido/apendices/glosario.md
- **A1**: proto-Botlet → "Séptima primitiva canónica"; Faceta conserva "Sexta".
- **H-I23**: agregar entrada **Salto Cuántico** (umbral habilitado por el colapso del costo de la pregunta analítica; frontera empresa-en-línea → empresa-en-tiempo-real).
- **H-I·glosario**: agregar entrada **códice propietario** (catálogo privado curado por un implementador; p. ej. ucodex). Evaluar entrada **ucodex** (nombre propio de instancia).
- **M7 orden alfabético**: reordenar las entradas fuera de orden (AgencyDomain antes de Agente; Asistente antes de Atención; subtipos de Botlet con criterio uniforme).
- **H-I10**: la definición de Generaciones G1/G2/G3 puede quedar (es glosario), pero condensada; el desarrollo vive en Epílogo.

### contenido/apendices/mapa-conceptual.md
- **M8**: insertar nodo **Capítulo 9 · Vergis** en el árbol §1 (entre Operación y Epílogo).
- **A1**: §4 etiquetar Asistente vs Agente como primitiva-eje; §1 nodo de primitivas refleja siete.
- **M·terminología**: §3 "protocolo A2A" en Capa 3 → "coordinación intra-AgencyDomain (vía protocolo `A2A`)"; capitalización agentia/soveria; verificar "umeeta".

### contenido/apendices/referencias.md
- **M9**: unificar encabezados de columna (`Tema`/`Link`); agregar fuentes citadas en el Epílogo que falten (DDD/Evans, GoF, Booch/UML) a "Investigación académica y especificaciones".
