# Data Canon

*Gobernanza de datos recentralizada en la era agentiva*

<!-- libro
IRIS acaba de trazar la trayectoria del SABER, y sus etapas medias dejaron pendiente una pregunta de gobierno: cuando los agentes — y no las personas — son quienes consumen el dato, ¿quién manda sobre él? Este capítulo la responde con un patrón nombrado: Data Canon. Nació como paper autónomo y conserva ese registro — resumen, argumento en dos partes, falsadores.
/libro -->

---

## Resumen

Data Mesh — formalizado por Zhamak Dehghani entre 2019 y 2022 — prescribe descentralizar la gestión de datos por dominio: ownership distribuido, datos como producto, plataforma de autoservicio, gobierno federado. Este capítulo sostiene que dos fuerzas contemporáneas erosionan la premisa sobre la que descansa la parte descentralizadora de esa prescripción, y que a ellas se suma un argumento de gobierno corporativo que Data Mesh no consideró. Primero: los tres modos de falla que Dehghani atribuye a las arquitecturas centralizadas son, en el fondo, límites de escala cognitiva humana — y la era agentiva (mapeo de esquemas y resolución de entidades por modelos de lenguaje, metadatos activos, transformación inferida, mantenimiento autónomo de pipelines, capa semántica sobre fuentes heterogéneas) eleva ese límite en un orden de magnitud. Segundo: Data Mesh asume que la semántica de dominio es local y se inventa, cuando las industrias maduras han producido modelos de información compartidos — el SID de TM Forum en telecomunicaciones, BIAN en banca, ACORD en seguros, IFRS/IAS 41 en lo contable — que la externalizan; donde existe un estándar, no hay nada local que distribuir. Tercero: el ownership distribuido pone al definidor de cada cifra a cargo de cómo se reporta esa cifra — un riesgo de agencia que un marco de control interno (en el espíritu de Sarbanes-Oxley / COSO) no toleraría. Lo que queda en pie es la gobernanza de responsabilidad, pero **recentralizada — y federada bajo un canon central**: la autoridad de decisión sobre lo **agency-crítico** — lo que toca las cifras con que se reporta la gestión — vive en el directorio (que adopta los estándares y fija la política de calidad) y en una *autoridad del canon* delgada; la conformidad operativa, la gestión de brechas y el modelado del dato propietario no sensible se reparten en *grupos federados por dominio*, cada uno ligado a su foro de estándares. A este patrón lo llamamos **Data Canon**. El capítulo define el patrón, lo posiciona frente al trabajo previo (Data Mesh, Data Fabric, lakehouse/medallion, MDM, modelos de información de industria, teoría de la agencia, marcos de control interno), y enuncia los falsadores que lo probarían equivocado.

<!-- standalone -->
**Palabras clave:** Data Mesh · Data Fabric · gobierno de datos · IA agentiva · arquitectura de datos · control interno · problema de agencia · estándares de información de industria.
<!-- /standalone -->

---

## Introducción

Los roadmaps de plataforma de datos contemporáneos persiguen, cada vez con más frecuencia, una "empresa en tiempo real": integrar todas las aplicaciones de la organización y traer todos sus datos a una plataforma común para analítica, reporting e IA. Esa dirección — centralizar la ingesta de todas las fuentes — parece, a primera vista, contradecir la descentralización que Data Mesh prescribe. Una formulación intuitiva de la tensión: *Data Mesh era la solución pragmática a cómo ingestar datos en la era pre-agentiva; la tecnología agentiva permite hacerlo de forma centralizada y automática, lo que vuelve prescindible la metodología.*

Este capítulo desarrolla esa intuición — la corrige donde está mal formulada, la fortalece donde tiene razón, y la lleva hasta un patrón arquitectónico nombrado y acotado: **Data Canon**.

### Contribución

La contribución es triple:

1. **Reencuadre del argumento de Data Mesh.** Las críticas habituales a Data Mesh sostienen que es complejo o que las organizaciones no están preparadas. Este capítulo ofrece una distinta: los tres modos de falla de Dehghani son límites de escala cognitiva humana disfrazados de problema organizacional — y por tanto la prescripción descentralizadora estaba amarrada a una restricción que la era agentiva está soltando. No es que Data Mesh esté equivocado: su premisa expira.
2. **El argumento "la semántica se adopta, no se inventa".** El argumento de Dehghani para el domain ownership descansa en un supuesto no enunciado: que la semántica de dominio es local e idiosincrática. Pero las industrias maduras la externalizaron en modelos de información compartidos. La inferencia lógica — si el estándar existe, no hay nada local que distribuir, y el ownership distribuido pierde su razón de ser para esos dominios — no parece haber sido formulada en estos términos.
3. **La crítica desde el control interno.** Las críticas a Data Mesh son técnicas u organizacionales. Esta es de gobierno corporativo: poner al dominio a definir *y reportar* sus propias cifras hace que el definidor del número sea el reportado por él — un riesgo de agencia clásico. De ahí el giro: la centralización (de lo agency-crítico) deja de ser "la opción burocrática" y pasa a ser la estructura que un marco de control interno *mandaría*.

El patrón que resulta de estas tres líneas — y que sobre-determina la recentralización (la era agentiva la *permite*; el control la *exige*) — es Data Canon. Su gobierno no es un monolito central: es federado, pero **anclado** a un canon central («La gobernanza recentralizada es federada — anclada a un canon central»).

### ¿Qué afirma este capítulo, y qué no?

**Afirma:** que el argumento de Data Mesh por la descentralización del ownership descansa en una premisa que dos fuerzas contemporáneas erosionan; que lo que persiste — la responsabilidad — se recentraliza en su núcleo agency-crítico y se federa en su periferia, no se elimina; que esa centralización del núcleo es preferible por razones de control interno; que la arquitectura objetivo resultante es Data Fabric con principios de gobernanza de Mesh, sostenidos centralizadamente en el canon y federadamente en la conformidad.

**No afirma:** que Data Mesh estuviera equivocado (resolvía un problema real con las herramientas de su época); que la era agentiva resuelva todos los problemas de gestión de datos (resuelve uno — la escala cognitiva — con consecuencias arquitectónicas grandes); que la recentralización sea gratis (la autoridad del canon y los grupos federados son una organización con costo, riesgo y permanencia); que la plataforma sea, por su arquitectura, conforme a un régimen de control específico (provee la precondición arquitectónica; los controles efectivos hay que diseñarlos y probarlos); que todas las capacidades agentivas asumidas estén disponibles, maduras y confiables hoy (algunas lo están; otras son trayectoria — «Límites, riesgos y falsabilidad»).

---

## Antecedentes: Data Mesh y su racional

Data Mesh fue formalizado por **Zhamak Dehghani** (ThoughtWorks) en tres textos canónicos: *How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh* (martinfowler.com, 2019), *Data Mesh Principles and Logical Architecture* (martinfowler.com, 2020) y *Data Mesh: Delivering Data-Driven Value at Scale* (O'Reilly, 2022).

### Los tres modos de falla

Dehghani diagnostica tres formas en que las arquitecturas centralizadas (data warehouse + data lake monolítico) fracasan al escalar:

1. **Arquitectura centralizada y monolítica que no escala.** Al proliferar las fuentes, "la capacidad de consumirlo todo y armonizarlo en un solo lugar bajo el control de una sola plataforma disminuye".
2. **Descomposición acoplada de pipelines.** Los data platforms se descomponen por funciones técnicas (ingestión, limpieza, agregación) en vez de por dominios; "todo el pipeline es la unidad mínima que debe cambiar para una nueva funcionalidad" — cuello de botella sistémico.
3. **Ownership siloado e hiper-especializado.** Un equipo central de datos, desconectado de las fuentes y de los consumidores, carece de domain knowledge.

### Los cuatro principios

(i) Domain-oriented decentralized data ownership and architecture; (ii) data as a product; (iii) self-serve data infrastructure as a platform; (iv) federated computational governance.

### El racional declarado, y dos silencios

Dehghani articula su motivación así: "our aspiration to augment and improve every aspect of business with data demands a paradigm shift in how we manage data **at scale**". La palabra operativa es *scale*. Y hay dos cosas que Dehghani no dice. Primero: **no** dice que el problema sea tecnológico — falta de cómputo, herramientas insuficientes; lo formula como problema organizacional. Pero un problema organizacional puede ser, a su vez, una respuesta a un límite cognitivo humano que se vuelve removible («El argumento, parte I»). Segundo: **no** pesa el riesgo de agencia que su propio diseño introduce al fusionar al definidor de la cifra con el reportado por ella («El argumento, parte II»).

### Posiciones intermedias y sus límites

El argumento de este capítulo se decanta tras descartar tres posiciones intermedias:

| | Tesis | ¿Por qué no basta? |
|---|---|---|
| **A** | La era agentiva vuelve prescindible a Data Mesh porque era respuesta a una limitación tecnológica pre-agentiva | Núcleo correcto (los problemas que Mesh resuelve son, en el fondo, humanos) pero formulación que no resiste el contraste con la fuente: Dehghani no plantea un problema tecnológico |
| **B** | El racional de Data Mesh es organizacional, no tecnológico; la era agentiva no lo vuelve prescindible | Lectura literal correcta de Dehghani, pero subdimensiona que esos problemas organizacionales son, a su vez, respuesta a límites cognitivos humanos |
| **C** | Dos planos: escala cognitiva (la era agentiva la atenúa) y gobernanza (persiste, **distribuida** por dominio) | Avance real — separa lo absorbible de lo no absorbible — pero asume que la gobernanza tiene que estar distribuida por dominio del modo en que Data Mesh la distribuye; no considera la semántica externa, ni que el núcleo agency-crítico se recentraliza mientras la periferia se federa de otro modo |
| **D** | El núcleo agency-crítico de la gobernanza se recentraliza (semántica adoptada de estándares + política estructural de directorio + un canon central); su periferia se federa en grupos por dominio ligados a sus foros de estándares. Y la recentralización del núcleo es la estructura que un marco de control mandaría | — *(esta es la tesis del capítulo; el patrón se llama Data Canon)* |

---

## El argumento, parte I: distribuir ya no es necesario

### Los tres modos de falla son límites de escala cognitiva humana

| Falla identificada por Dehghani | ¿Por qué es, en el fondo, un límite humano? |
|---|---|
| La centralización no escala al proliferar fuentes | Límite de cuántas fuentes puede normalizar, mantener y armonizar un equipo humano |
| Pipelines acoplados por funciones técnicas, no por dominios | Límite cognitivo humano para descomponer y orquestar dinámicamente |
| Equipo central sin domain knowledge | Ningún humano puede ser experto en todos los dominios simultáneamente |

Los tres son límites de escala cognitiva humana. Data Mesh es la respuesta organizacional inteligente a ese límite: si una unidad de procesamiento no puede con todo, repartir el trabajo entre muchas unidades cercanas al conocimiento — una aplicación de la ley de Conway al problema de datos. Pero la inteligencia de esa respuesta es *contingente* al límite. Si el límite se mueve, la respuesta deja de ser obligatoria.

### La era agentiva absorbe la escala cognitiva

"Era agentiva" no es una invocación mágica. Son capacidades concretas, con distinto grado de madurez:

| Capacidad | ¿Qué reemplaza? | Madurez actual |
|---|---|---|
| Mapeo de esquemas y resolución de entidades por modelos de lenguaje | El ETL hand-coded de mapeo fuente→canónico y las reglas de matching de MDM (*master data management*, la disciplina del registro maestro) | Alta para casos acotados; degrada en ambigüedad genuina |
| Metadatos activos / pipelines que se auto-ajustan al *schema drift* | El mantenimiento manual cuando una fuente cambia de forma | Media-alta |
| Transformación inferida (deducir la transformación desde ejemplos / desde el contrato de datos) | El desarrollo de transformaciones tabla por tabla | Media; en ascenso |
| Mantenimiento autónomo de pipelines (monitoreo, detección de anomalías, auto-reparación) | El equipo de plataforma que vigila y arregla pipelines rotos | Media |
| Capa semántica sobre fuentes heterogéneas, incluyendo no estructuradas | El "SQL como interfaz" y el curador humano que sabe dónde está todo | Media; es la apuesta de los roadmaps actuales |
| Generación de código de transformación a partir de requerimientos | El rol del desarrollador; deja al equipo como "modeladores de requerimiento" que orquestan agentes de desarrollo | Media-alta |

El efecto agregado: la unidad de procesamiento que mantiene N pipelines, descubre relaciones, normaliza y "sabe" sobre M dominios deja de tener N y M acotados por la cabeza de un equipo humano. Los tres modos de falla de Dehghani se atenúan en la misma medida en que esas capacidades funcionan. La atenuación no es infinita: los agentes son confiables en mapeo, matching y mantenimiento *bien acotados*, y degradan en ambigüedad semántica genuina (cuando dos mapeos son igualmente defendibles y hay que *elegir*) y en juicios que requieren contexto de estrategia de negocio. Ese residuo no se evapora; se canaliza por la gobernanza federada de la sección «La gobernanza recentralizada es federada — anclada a un canon central».

### La semántica de dominio no se inventa: se adopta

Cuando Dehghani argumenta que el dominio debe ser dueño de la semántica de sus datos — qué es "cliente", qué es "pedido" —, asume implícitamente que esa semántica es *local*: que la organización la construye, que es idiosincrática, que por eso conviene tenerla cerca de quien la conoce. Para la mayoría de las organizaciones en 2019–2022, era un supuesto razonable.

Pero las industrias maduras han producido **modelos de información compartidos** que externalizan la semántica: el **SID (Shared Information/Data Model)** de TM Forum en telecomunicaciones (25 años de desarrollo; cubre producto, cliente, servicio, recurso, parte); **BIAN** en banca; **ACORD** en seguros; y, transversal a toda industria, **IFRS** define la semántica contable, **XBRL** la estructura del reporting, con norma específica para agricultura — **IAS 41 *Agriculture*** (activos biológicos, producto agrícola).

Donde existe un estándar así, **no hay nada local que distribuir**. El significado de "cliente" no es lo que prefiere el área comercial ni lo que prefiere finanzas: es lo que el estándar define. Y los accionistas no quieren que se les reporte según la preferencia de un área; quieren que se les reporte *según el estándar*. La supuesta contienda semántica entre dominios que Data Mesh resuelve dándole la palabra al dominio se disuelve por otra vía: hay un árbitro externo, autoritativo, y la organización decide subordinarse a él. Esa decisión — "reportamos según el estándar de industria, punto" — es un acto de gobierno, de nivel directorio, que se toma una vez.

Corolario: si la semántica viene de afuera (estándar) y la ejecución la absorbe la era agentiva («La era agentiva absorbe la escala cognitiva»), las dos funciones que Data Mesh fusionaba en el dominio — especificar y ejecutar — salen del dominio. Lo que queda es la tercera: responder (ver «El argumento, parte II» y «El patrón Data Canon»).

---

## El argumento, parte II: distribuir es peor en términos de gobierno

### Data Mesh estructura el problema de agencia hacia adentro

El conflicto en juego tiene nombre en teoría de la firma: el **problema de agencia** (Jensen & Meckling, 1976) — los administradores (agentes) gestionan recursos de los accionistas (principales) y tienen incentivo a presentar su gestión de la forma que más los favorece. Buena parte del andamiaje de integridad del reporting financiero existe para contenerlo.

Data Mesh, sin proponérselo, estructura el problema hacia adentro. Sus principios 1 y 2 (ownership por dominio, datos como producto) ponen al dominio a cargo de definir la semántica, la calidad y los contratos de sus datos. Es decir: la persona cuyo desempeño se mide con una cifra pasa a controlar cómo se define, se calcula y se presenta esa cifra. Las palancas son concretas: elegir, entre dos definiciones igualmente defendibles, la de "cliente activo" o "margen de la unidad" que mejor luce; fijar el SLO (*service level objective* — el nivel de servicio comprometido) de calidad del producto de datos lo bastante bajo como para no tener que arreglar el dato vergonzoso; diseñar el contrato del producto para exponer lo que ayuda y enterrar lo que no. Aun acotada por las políticas globales de interoperabilidad del cuarto principio, esa discrecionalidad **es** la palanca de agencia — porque *el definidor de la cifra y el reportado por ella son la misma parte*. En lenguaje de control interno, eso es una violación de la segregación de funciones.

No es exactamente un error de Dehghani — es un punto ciego: optimizó la efectividad (más cerca del conocimiento = mejor dato) e ignoró el control (independencia de la función de reporte respecto de los reportados). Para una empresa con accionistas, ese segundo eje no es opcional.

### ¿Por qué "federated computational governance" no lo cierra?

El cuarto principio de Data Mesh — gobierno computacional federado — podría parecer la respuesta. No lo es *como Dehghani lo plantea*: gobierna la *interoperabilidad* entre productos de datos (políticas globales para que encajen, se descubran, sean direccionables), no la *independencia* de la función de reporte; la federación que fija esas políticas incluye a los propios dominios (la zorra ayuda a escribir las reglas del gallinero); y un comité que revisa *a posteriori* las definiciones de los dominios sería un control detectivo, no preventivo — el más débil de los dos. El control preventivo requiere independencia estructural, no supervisión: no se le pone independencia *encima* a una estructura que fusionó al productor con el reportado; hay que diseñarla *adentro*. Data Canon conserva el principio de federación — pero **anclado** a un canon central que sí es independiente del dominio reportado («La gobernanza recentralizada es federada — anclada a un canon central»): la federación conforma y gestiona brechas; el canon, no.

### El patrón con canon central como ambiente de control interno

La recentralización del núcleo agency-crítico neutraliza el problema de agencia no por agregar supervisión, sino por su estructura:

| Propiedad del patrón | ¿Qué neutraliza? | ¿A qué exigencia de control equivale? |
|---|---|---|
| Semántica de reporte en estándar externo (IFRS / IAS 41 para lo financiero) | Ningún jefe de unidad puede redefinir "ingreso", "activo biológico" o "margen" — la definición no es suya | La base consistente y no discrecional de las cifras que exigen SOX §404 / el componente *Control Environment* de COSO |
| Ejecución por la plataforma, fiel al origen, con linaje completo | Lo que sube al directorio es trazable al sistema transaccional, no curado por el dominio | El *audit trail* que §404 requiere — y la condición para que la gerencia pueda certificar honestamente bajo SOX §302 |
| El **canon** (semántica de reporte, reglas de supervivencia, política de calidad) es central y no discrecional, custodiado por la *autoridad del canon*; la conformidad operativa y la gestión de brechas se federan por dominio | El que define cómo se reporta es independiente del que opera | La segregación de funciones: el dominio *opera* (corre los sistemas transaccionales — la verdad de lo que pasó) y, vía su grupo federado, *conforma y gestiona brechas* — pero no *define* la semántica de reporte; eso lo fija el canon central. Toda propuesta del grupo federado que toque cifras de reporte sube a la autoridad del canon para ratificación (control preventivo) |
| Reglas de supervivencia pre-especificadas y auditables | Las decisiones de reconciliación son reglas verificables, no juicios ad hoc del interesado | Control preventivo en vez de detectivo |

En conjunto: el patrón con su canon central es la estructura que un marco de control interno *mandaría* aunque la era agentiva no existiera. La dirección de la implicación importa — no es que un ambiente de control "tolere" esta arquitectura; es que la prescribiría. (Salvedad de alcance: Sarbanes-Oxley aplica literalmente a registrantes ante la SEC; a una empresa privada no le aplica como tal, pero el principio es universal, casi toda jurisdicción tiene análogos — regímenes de responsabilidad de la persona jurídica, normas de los reguladores de valores y seguros, las exigencias de control interno que un auditor externo evalúa al opinar sobre estados financieros bajo IFRS — y es lo primero que se mira en una eventual apertura, levantamiento de capital o *due diligence* de M&A. La formulación correcta: el patrón provee la *precondición arquitectónica* de un ambiente de control en el espíritu de SOX / COSO, no "compliance".)

### La recentralización sobre-determinada

Juntando las dos líneas: «El argumento, parte I» muestra que distribuir ya no es **necesario** (la era agentiva removió la restricción de escala cognitiva; la semántica se adopta de estándares externos). «El argumento, parte II» muestra que distribuir el núcleo agency-crítico es, además, **peor** en el eje de control que Data Mesh no pesó. Por lo tanto la recentralización de ese núcleo está sobre-determinada: la era agentiva la *permite*; el control de la información para los accionistas la *exige*. Esto también invierte la objeción estándar contra la centralización («La objeción Dehghani-fuerte»): es cierto que un monolito recentralizado arriesga reintroducir el cuello de botella organizacional que Dehghani señalaba — pero en Data Canon lo que se centraliza es el *canon* (un núcleo delgado y agency-crítico), no toda la operación de gobierno; ésta se federa («La gobernanza recentralizada es federada — anclada a un canon central»). Así se evitan a la vez el cuello de botella del monolito y la dependencia de un único centro "estrella"; y la alternativa puramente distribuida carga con un riesgo *peor*, el de agencia, que el canon central no tiene.

---

## El patrón Data Canon

**Data Canon** es el patrón de arquitectura y gobernanza que resulta de las dos partes del argumento: distribuir ya no es necesario, y distribuir es peor en términos de gobierno. El nombre viene del *ancla semántica externa y autoritativa a la que todo se conforma*: un *canon* es algo que se adopta y se acata, no que se inventa — y, por definición, lo que nadie puede redefinir a su conveniencia.

### Las tres funciones — especificación, ejecución, responsabilidad

| Función | DWH tradicional | Data Mesh canónico | Data Canon |
|---|---|---|---|
| **Especificación** — definir los datos, la semántica, la calidad | Equipo central con input del dominio | El dominio | El **estándar de industria** (donde existe); la **autoridad del canon** (para la semántica de reporte y la política, agency-crítico); los **grupos federados por dominio** (para el modelado del core propio no sensible y la conformidad) |
| **Ejecución** — mover, transformar, conformar | Equipo central | El dominio o la plataforma self-serve | La **plataforma agentiva** |
| **Responsabilidad** — responder cuando algo falla | Difusa (equipo central por defecto) | El dominio (explícito) | El **directorio** (vía "se reporta según el estándar"); la **autoridad del canon** (por la semántica de reporte y la política); los **grupos federados** (por el ensamblaje, las brechas y el core de dominio) |

Data Mesh diseña que las tres caigan en el dominio, y por eso la responsabilidad cae naturalmente ahí. Data Canon rompe la coincidencia: especificación → afuera (estándar) y arriba (canon), con la fracción no sensible federada; ejecución → la máquina; responsabilidad → arriba (canon) y federada (grupos). Ninguna queda repartida por área *del modo agency-problemático*: el área medida por una cifra no controla cómo se define esa cifra. (La responsabilidad de cada dueño de sistema transaccional por la calidad de los datos *en su sistema* subsiste — pero eso no es un "data domain owner": es el dueño de una aplicación operativa, que existe con o sin Data Mesh; la plataforma sólo le da visibilidad de qué calidad aporta, vía linaje.)

La responsabilidad es la sombra de la **autoridad de decisión**: quien decide qué semántica aplica y qué calidad se exige, responde. En Data Mesh esa autoridad vive en el dominio porque la semántica es local; en Data Canon la semántica de reporte es adoptada de un estándar y custodiada por el canon central, así que la autoridad agency-crítica vive en el directorio y la autoridad del canon. La autoridad sobre el residuo (mapeos ambiguos, brechas, modelado del core propio no sensible) se federa por dominio, con la fracción que toca cifras de reporte reservada al canon central («La gobernanza recentralizada es federada — anclada a un canon central»).

### La gobernanza recentralizada es federada — anclada a un canon central

La versión ingenua de Data Canon pondría todo en un único centro de excelencia. Es un error — y no por motivos de escala cognitiva (de eso se ocupan los agentes), sino por una razón de gobierno de otra clase: un único centro todopoderoso se vuelve un punto único de dependencia. Lo expresó, con crudeza memorable, un CEO de una gran operadora de telecomunicaciones: los centros de excelencia *"tienden a crear divas de las que la empresa empieza a depender demasiado"*. Riesgo de persona clave, cuello de botella, riesgo de captura.

Por eso Data Canon distribuye la gobernanza *operativa* — pero anclada. Dos capas:

- **La autoridad del canon** (delgada, central). Custodia el núcleo agency-crítico: la semántica canónica de reporte (lo que el directorio reporta — IFRS/IAS 41 y lo que de ello se derive), las reglas de supervivencia, la política de calidad (autorizada por el directorio) y la calibración del sistema agentivo (qué decide el agente solo, qué propone para ratificación, qué queda fuera). No *opera* nada; ratifica y mantiene el canon. Es pequeña precisamente porque casi no hace trabajo de campo — el trabajo de campo es de los agentes y de los grupos federados.
- **Los grupos federados de conformidad** (uno por dominio / por capa). Cada uno ligado a su foro de estándares especializado: el grupo de finanzas con el cuerpo de normas contables; el de trazabilidad con GS1; el de I+D con la comunidad científica del dominio; etc. Hacen: triaje de brechas (un registro no encaja en el estándar — ¿qué hacemos, provisionalmente?), enlace con el foro (empujar la brecha río arriba para que el estándar la cierre), y el modelado del dato propietario *no agency-crítico* de su dominio. Lo agency-crítico — cualquier cosa que toque cifras de reporte — lo *proponen* hacia arriba, a la autoridad del canon, que *ratifica*. Es exactamente el patrón de control preventivo.

Por qué esto no rompe el argumento:

- **No reintroduce la carga de escala cognitiva.** Los grupos federados son *ligeros* — son grupos de enlace, triaje y propuesta, no equipos que operan pipelines; los agentes cargan el grueso. La federación es pequeña *por grupo* porque la máquina hace el trabajo de campo.
- **No reintroduce el problema de agencia.** Las decisiones agency-críticas quedan en la autoridad del canon; la federación gestiona la periferia (conformidad, brechas, foros) y el dato propietario no sensible; toda propuesta que toque la semántica de reporte sube para ratificación — no baja al área medida por la cifra.

Y esto **honra de verdad el cuarto principio de Data Mesh** — *gobernanza computacional federada* —, no sólo de nombre. Donde la federación de Dehghani era federada *hasta el fondo* (cada dominio define lo suyo; un consejo coordina la interoperabilidad), la de Data Canon es federada *alrededor de un canon central*: el canon — la semántica de reporte más la política — es innegociable y central; la federación conforma, gestiona brechas y enlaza con los foros. La federación no flota libre; está **anclada**. Ese anclaje es lo que impide que la federación derive hacia el territorio del problema de agencia (ningún dominio puede redefinir "ingreso"); y la federación es lo que impide que el centro se vuelva una diva.

Una nota sobre robustez: para el dato propietario que da ventaja competitiva — que por definición ningún estándar de industria cubre porque no es compartido — el grupo federado del dominio correspondiente carga con su modelado, de forma permanente. Esa parte no es un trámite ligero. Pero sigue siendo *federada* (no concentrada en un centro único) y *anclada* (lo que de ese dato afecta cifras de reporte pasa por el canon).

### El estándar-mosaico

La viabilidad de Data Canon depende de que exista un ancla semántica externa — y dónde existe varía por industria.

En **telco, banca y seguros** hay un modelo único maduro (SID/TM Forum; BIAN; ACORD), mantenido por un cuerpo, con cobertura del negocio completo: el patrón opera en su caso más favorable; los grupos federados sólo *adoptan y mapean*; la disputa semántica interna queda sin materia.

En un **conglomerado diversificado multi-vertical** — consideremos, por ejemplo, un grupo agroindustrial con producción agronómica, I+D genética y comercialización en varios países — el ancla es un mosaico, desigual:

| Capa del negocio | ¿Estándar externo autoritativo? | Madurez |
|---|---|---|
| Contable / financiero / consolidación | **Sí, fuerte** — IFRS; IAS 41 *Agriculture*; XBRL | Décadas. Autoritativo. Es lo que el directorio reporta |
| Trazabilidad / cadena de suministro / identificación de producto | **Sí, fuerte** — GS1 (GTIN, GLN, EPCIS) | Décadas. De facto global |
| I+D / mejoramiento genético / fenotipado | **Sí, bueno en su nicho** — BrAPI v2, MIAPPE 1.1, Crop Ontology, AGROVOC (FAO) | Maduro en la comunidad científica; APIs y ontologías |
| Operaciones de campo / agricultura de precisión | **Parcial** — AgGateway ADAPT Standard (Modus para lab de suelos) | Joven; foco angosto |
| Core comercial / operativo del grupo como entidad de negocio | **No existe** un modelo de información compartido | — |

Telco produjo un SID porque es una industria homogénea — todos venden conectividad y servicios sobre redes. Un grupo diversificado abarca, dentro de sí mismo, varias verticales; el mismo motivo por el que no existe un "SID" para él es el motivo por el que es difícil de consolidar. Consecuencia: el estándar corporativo se **ensambla** — los grupos federados adoptan los estándares externos de su capa y, donde no hay estándar (el core comercial/operativo), la autoridad del canon define la semántica de reporte y el grupo federado correspondiente el resto del modelo. La tesis estructural sobrevive intacta (lo que reemplaza al ownership distribuido es "estándares externos + canon central + grupos federados ligeros", y nada de eso devuelve al área medida por una cifra el control de cómo se define esa cifra); lo que no sobrevive es la versión ingenua que asumiría que basta un trámite o que la semántica viene íntegra de afuera. Para una parte importante — el core — no.

### El medallion se queda en tres pisos — y el agente vuelve virtual la mayor parte del consumo

Data Canon **no agrega una cuarta capa de almacenamiento**. El medallion clásico se mantiene:

| Capa | ¿Qué es? | Criterio para entrar |
|---|---|---|
| **Bronze** | Aterrizaje de crudos por fuente — copia fiel del sistema origen | "Lo necesito accesible". Replicar es legítimo aunque no haya caso de uso. Regla: si el dato vive en un sistema transaccional, va a Bronze — no lo decide nadie |
| **Silver** | Datos conformados al modelo canónico unificado (el estándar-mosaico) | "Tiene forma estable y semántica acordada". Conformidad binaria y verificable por máquina |
| **Gold** | Productos de datos **materializados** — data marts (subconjuntos analíticos pre-construidos) | "Es un producto que se ganó materializarse" — ver abajo |

Lo que cambia con la era agentiva no es la *estructura* del medallion sino *cómo se consume*. En el mundo pre-agentivo se materializaban productos en Gold porque consultar Silver directamente era lento o difícil; el mart era una *optimización de performance*. Con una **capa semántica agentiva** sobre Silver, el agente compone cualquier vista conforme al canon **al vuelo** — la mayor parte del consumo deja de necesitar un mart pre-construido. Dos consecuencias:

- **El consumo por defecto es virtual** — el agente compone la vista que el consumidor pide, en términos del canon, sobre Silver, en tiempo real. No es una "cuarta capa": es el agente operando. Las definiciones canónicas que el agente aplica — "margen por segmento, por país, por trimestre" y demás — son **parte del canon**, no un artefacto aparte: el agente las *aplica*, no las improvisa, y por eso dos vistas pedidas por dos consumidores distintos son automáticamente coherentes entre sí.
- **Gold se vuelve selectivo por una razón, no por dogma** — se materializa un mart cuando el patrón *se gana congelarse*: alto volumen, SLA de un sistema externo que depende de una interfaz física estable, snapshot regulatorio que hay que congelar, feature store de ML. Un **mart Gold es la forma materializada/cacheada de un patrón de consulta que la capa agentiva compondría en vivo** — el equivalente de datos a una vista materializada respecto de su vista lógica, con la propiedad de que si el mart queda stale o se rompe, el sistema **recomputa desde Silver** (la definición viva sigue ahí). El agente puede materializar; la decisión de *qué vale la pena* materializar la gobierna el negocio (caso de uso, dueño de cada capa, contrato — «Los productos de datos: ¿quién los identifica y quién los realiza?»).

Esto resuelve dos fricciones de una vez:

- **"Centralizar todos los datos es un despropósito contrario a Data Mesh"** — verdad para **Gold** (subir 500 tablas de un ERP a Gold viola los cuatro atributos de un producto — caso de uso, dueño, contrato, mantenimiento sostenible: la mayoría son auxiliares sin consumidor real; ningún área responde por 500 tablas; garantizar calidad de producto a 500 tablas es desproporcionado; mantener 500 productos sin consumo es overhead puro — *cuando todo es producto, nada es producto*); falsa para **Bronze**, vertedero *por diseño* — copia fiel del crudo, ingesta de fuente, no productización, y Mesh aplica a la capa de productos, no a la de aterrizaje. Las dos partes de la discusión suelen estar hablando de capas distintas sin nombrarlas; la trayectoria replicación → federación que un roadmap moderno declara afecta principalmente a **Bronze** — Gold no se federa.
- **"¿Y entonces cómo es una empresa en tiempo real con un Gold selectivo?"** — el tiempo real lo da **Silver (conformado, en tiempo real) + el agente componiendo sobre él**, no la cantidad de marts pre-construidos. Gold materializado es la excepción de optimización; el sustrato vivo es Silver-más-agente. (Y "empresa en tiempo real" en sentido fuerte — detectar, interpretar, decidir y actuar — es lo que el agente *hace* sobre ese sustrato, no una propiedad del almacenamiento.)

### La política de calidad como artefacto estructural

En Data Mesh, cada producto declara su calidad y SLA, y el consumidor decide si le sirve — un juicio recurrente ("¿este dato es suficientemente bueno para *este* uso?") que alguien cercano al dominio tiene que hacer; es uno de los anclajes del ownership distribuido. Data Canon lo disuelve invirtiendo el planteo: en vez de niveles por caso de uso, **un solo nivel — el más estricto — para todo**, porque eso es lo que significa ser una empresa en tiempo real; la decisión se toma una vez, a nivel directorio, y vive en el canon. La plataforma garantiza, para todo dato, sin decisión por caso de uso:

| # | Garantía | Dimensión que cubre | ¿Por qué no requiere juicio humano? |
|---|---|---|---|
| 1 | **Tiempo real** | Frescura | El ajuste más estricto posible; ningún caso de uso puede pedir más. Un solo nivel |
| 2 | **Fiel al origen** | Exactitud y completitud (la parte no introducida por la plataforma) | El valor en la plataforma = el valor en el origen al momento de captura. Binario, verificable por agente |
| 3 | **Linaje completo** | Procedencia / trazabilidad | Cada dato carga de dónde vino y cuándo. Hace honesto al punto 2; es capacidad de plataforma, no decisión |
| 4 | **Conforme al estándar (mosaico)** | Validez / conformidad | Cada dato mapeado al esquema canónico. Conformidad binaria, chequeable por máquina |
| 5 | **Reconciliado por reglas de supervivencia** | Consistencia cross-sistema; unicidad | Cuando varias fuentes describen la misma entidad canónica, una regla pre-especificada (parte del canon) produce el registro dorado; el agente la aplica. La ambigüedad residual → el grupo federado del dominio, que propone a la autoridad del canon si toca cifras de reporte |

Los puntos 3 y 5 son piezas que el enunciado intuitivo ("tiempo real + fiel al origen + conforme al estándar") no nombra pero el modelo necesita: el 5 es el problema clásico de *master data / golden record*, que se disuelve porque el estándar da el esquema canónico único (no hay tres definiciones de "cliente", hay una), el paso de conformidad mapea cada fuente a ese esquema, y la regla de supervivencia decide el ganador cuando los valores discrepan — nada de eso pide que el área medida por la cifra defina la cifra; pide un artefacto más en el canon.

Dos límites honestos: **(A)** exactitud y completitud están acotadas por el origen, no garantizadas por la plataforma — si el sistema origen tiene un dato mal, la plataforma lo replica mal, fielmente; mejorarlo es un proyecto de mejora del sistema origen, propiedad del dueño de ese sistema, que ya existe, no un domain owner nuevo. **(B)** "tiempo real" es el piso *objetivo*, realizado progresivamente conforme la conectividad de cada fuente lo permite (legados batch, terceros con bajada diaria); la política es estructural, su materialización es por fases. Ninguno de los dos reintroduce ownership distribuido agency-problemático.

### Los productos de datos: ¿quién los identifica y quién los realiza?

En Data Mesh, cada dominio es responsable de *identificar y realizar* los productos de datos que comparte con el resto de la empresa — el productor del dato es también su productizador, y eso es lo que justifica el ownership distribuido. En Data Canon esa responsabilidad se descompone, porque ya no hay un único acto de "productizar" sino una cadena con piezas en lugares distintos:

| Paso | En Data Mesh | En Data Canon |
|---|---|---|
| **Identificar la necesidad** | El dominio dueño del dato decide qué productizar para los demás | La **demanda** nace en el consumidor — la unidad que necesita la vista la formula vía su interlocutor — o la levanta el **reconocimiento de patrones del agente** (push: "este patrón se repite; conviene ofrecerlo, o materializarlo"). El consumidor y el dato fuente pueden estar en dominios distintos; el agente los puentea |
| **Realizar el producto** | El equipo del dominio opera un pipeline y construye un mart | El **agente** lo compone — *en vivo, virtual, por defecto* (en términos del canon, sobre Silver). Sólo se *materializa a Gold* si el patrón se gana congelarse («El medallion se queda en tres pisos — y el agente vuelve virtual la mayor parte del consumo»). El dominio no opera un pipeline |
| **La semántica del producto** | La fija el dominio | La fija el **canon** — la vista se compone de definiciones canónicas, no inventadas. Lo que toque cifras de reporte lo ratifica la **autoridad del canon**; los **grupos federados** mantienen el catálogo de definiciones de su sub-árbol |
| **El contrato / la calidad** | Lo negocia el dominio con sus consumidores | El piso de calidad ya está fijado por el canon («La política de calidad como artefacto estructural» — tiempo real, fiel al origen, linaje, conforme, reconciliado): la vista lo hereda. Lo único específico del producto es el encuadre del caso de uso; el contrato es, en gran parte, *derivado*, no negociado |
| **Responder si está mal** | El dominio productor | Se descompone por capa, con linaje completo que hace la atribución mecánica: si el *origen* está mal → el dueño del sistema origen (que ya existe); si la *semántica* está mal → la autoridad del canon; si el *encuadre del caso de uso* está mal → el consumidor que lo pidió o el grupo federado que lo modeló |
| **Descubrirlo** | Catálogo federado (cada dominio publica el suyo) | Un único catálogo autoritativo — de definiciones canónicas (las vistas virtuales) y de los marts Gold (las materializadas), bajo la autoridad del canon |

Así Data Canon conserva el espíritu de "datos como producto" de Data Mesh — los productos existen, son direccionables, descubribles, con contrato y con un responsable de cada capa — pero sin su acoplamiento: el productor del dato no tiene que ser su productizador; *realizar* un producto no carga al dominio (lo hace el agente); la interoperabilidad entre productos no se negocia caso a caso, sale del canon compartido. La "responsabilidad del dominio de identificar y realizar los productos compartidos" sobrevive sólo en su mitad de **identificación** — la demanda sigue naciendo cerca de quien la necesita, o la anticipa el agente — mientras que la **realización** la absorbe el agente y la **gobernanza** (semántica, calidad) la fija el canon.

---

## Implicaciones de implementación

**Arquitectura.** La combinación correcta es **Data Fabric con principios de gobernanza de Data Mesh, anclados a un canon central** — y eso *es* Data Canon. El Fabric (potenciado por la era agentiva: metadatos activos, transformación inferida, capa semántica) absorbe la escala cognitiva; los principios de Mesh que persisten son los de gobernanza (datos como producto en Gold, selectivo; gobernanza federada), pero la federación está anclada a un canon central que custodia lo agency-crítico. Donde un programa haya declarado en una fase temprana "Data Mesh" a secas y en una fase posterior "Data Fabric con principios de Mesh", la diferencia no es una inconsistencia a esconder sino una precisión.

**Modelo organizacional.** La organización no necesita montar domain owners de datos por área en el sentido de Data Mesh. Necesita: una **autoridad del canon** delgada (la pieza de control interno de «El patrón con canon central como ambiente de control interno» — custodia la semántica de reporte, las reglas de supervivencia, la política de calidad, la calibración de los agentes); **grupos federados de conformidad** por dominio, ligeros, cada uno ligado a su foro de estándares (triaje de brechas, enlace con el foro, modelado del core propio no sensible); y, a nivel directorio, decidir el piso de calidad y el compromiso de tiempo real, y la adopción del mosaico de estándares de industria capa por capa, empezando por la capa contable/financiera. Lo que el negocio no puede delegar a la tecnología es exactamente esto — y es *menos*, y mejor repartido, de lo que la disciplina distribuida de Data Mesh haría temer o de lo que un CoE monolítico arriesgaría.

**Gestión del cambio.** Si la organización sólo sostiene gobernanza federada anclada, los embajadores de áreas no son "dueños de dominio en formación" sino **interlocutores en su unidad** — los que traducen qué le importa al negocio local a requisitos que los grupos federados y los agentes ejecutan, y, donde corresponda, integran su unidad al grupo federado de su capa. Eso aligera la formación y la enfoca hacia la traducción negocio↔dato, no hacia la administración técnica de un dominio.

**Lenguaje de directorio.** La distinción "escala cognitiva vs. gobernanza" es nítida internamente pero no es lenguaje de directorio. Hacia afuera: *"La tecnología de hoy nos deja traer y ordenar todos los datos del grupo sin repartir el trabajo de plomería por todas las áreas. Y conviene hacerlo así por una razón de control: cuando cada área define cómo se reportan sus propios números, los números terminan favoreciendo a quien los reporta; con la semántica de reporte fijada por los estándares de la industria (la contabilidad ya los tiene, IFRS) y un registro completo de dónde viene cada dato, eso no pasa. No ponemos un único equipo central todopoderoso — eso crea dependencias peligrosas; ponemos un guardián delgado del estándar y una red de grupos por dominio que conectan con los foros especializados. Del negocio necesitamos una decisión de directorio: adoptar esos estándares, dotar esa estructura, y comprometernos a operar en tiempo real."*

---

## Límites, riesgos y falsabilidad

Un argumento que se respeta dice qué lo probaría equivocado.

### Falsadores

| Si resulta que… | …entonces la tesis se debilita así |
|---|---|
| El dato propietario / de ventaja competitiva es el **grueso** del valor, no el margen | Los grupos federados que lo modelan se vuelven pesados, y "gobernanza federada anclada" es, en la práctica, casi indistinguible de Data Mesh distribuido — salvo que el canon central sigue acotando la semántica de reporte. La tesis sobrevive en forma pero pierde gracia |
| El volumen de brechas (lo que no encaja en el estándar) **no converge** — estándar inmaduro, foro lento, organización sin influencia río arriba | Los grupos federados se vuelven un aparato grande y permanente; o, peor, la autoridad del canon engorda para absorberlos — el monolito pre-Mesh otra vez. Viable sólo en la medida en que los agentes absorban la escala |
| Las capacidades agentivas tienen un **techo de complejidad más bajo** del asumido | El argumento de «La era agentiva absorbe la escala cognitiva» se debilita; vuelve a justificarse repartir el trabajo cognitivo (y la federación deja de poder ser ligera) |
| "Tiempo real" es **infactible** para fuentes críticas | La política definida en «La política de calidad como artefacto estructural» se vuelve aspiracional para una parte del negocio; reaparecen los niveles por caso de uso para esa parte |
| El argumento de control resulta **insuficiente para mover al directorio** | El eje de «El argumento, parte II» pierde tracción práctica, aunque siga siendo válido |
| El **core comercial/operativo** sí tiene un estándar de industria emergente que este análisis no detectó | La tesis se *fortalece* (más semántica externa, autoridad del canon y grupos federados más delgados) |

### La objeción Dehghani-fuerte

Aun concediendo que la era agentiva remueve el límite *cognitivo*, una estructura recentralizada puede reintroducir el límite *organizacional* que Dehghani también señalaba: cola única de cambios, lejanía respecto del consumidor, el dominio esperando que el centro atienda su requerimiento. Data Canon lo mitiga por diseño: (a) el autoservicio agentivo reduce la cola — el consumidor describe lo que necesita y el sistema lo produce sin pasar por una persona; (b) el estándar como contrato reduce la coordinación — no hay que negociar la semántica, ya está fijada; (c) la gobernanza es federada, no monolítica — el "centro" es un canon delgado, no un equipo todopoderoso, y la conformidad la lleva un grupo cercano a cada dominio; (d) los interlocutores de unidad acortan la distancia. Es una mitigación, no una garantía: el riesgo es real y conviene monitorearlo. Pero el balance no es simétrico — la alternativa puramente distribuida no evita este riesgo gratis; lo cambia por el riesgo de agencia («El argumento, parte II»), que es peor y más difícil de auditar.

### Riesgo de hype

No confundir "los agentes *pueden*" con "los agentes *hacen bien hoy*". Varias capacidades de «La era agentiva absorbe la escala cognitiva» están en madurez media y suben rápido — pero "suben rápido" es una apuesta, no un hecho consumado. La arquitectura debe diseñarse para degradar con gracia: si una capacidad agentiva no rinde, el fallback es trabajo humano en los grupos federados (y, para lo agency-crítico, en la autoridad del canon), no el colapso del modelo.

### Lo que sigue abierto

¿El "domain knowledge emergente" de un agente es equivalente al de un experto humano de dominio, o hay una clase de juicio tácito que no se transfiere? ¿Hay un tercer plano humano además de escala cognitiva y gobernanza — la "alineación con qué le importa al negocio" — que ni la era agentiva resuelve ni cae limpiamente bajo "gobernanza" (hipótesis de trabajo: existe, y es el rol del interlocutor de unidad)? ¿La trayectoria replicación → federación está bien fundada técnicamente para las fuentes concretas de cada organización? ¿Cuál es el reparto óptimo entre la autoridad del canon y los grupos federados — cuánto del modelado del core propio puede federarse sin reabrir, por la ventana, el problema de agencia?

---

## Trabajo relacionado

- **Data Mesh** (Dehghani, 2019–2022) — la fuente que este capítulo revisita. Data Canon no la refuta: la datea, y rescata sus principios *de gobernanza* — datos como producto, y la *gobernanza computacional federada*, que Data Canon conserva pero **anclada a un canon central** (la federación conforma y gestiona brechas; el canon — agency-crítico — no se federa).
- **Data Fabric** — la corriente, asociada a Gartner y a varios proveedores, que enfatiza metadatos activos, transformación inferida y capa semántica unificada. Data Canon adopta el Fabric como sostén técnico (el lado que la era agentiva potencia) y lo complementa con los principios de gobernanza de Mesh anclados. El debate "Mesh vs. Fabric" es previo a este capítulo; lo que el capítulo aporta es el *motivo* — la escala cognitiva absorbida por la IA — y la conexión con el argumento de control.
- **Lakehouse y arquitectura medallion** (linaje Inmon/Kimball → data warehouse → data lake → lakehouse; Bronze/Silver/Gold popularizado por la práctica de la industria) — Data Canon usa el medallion **sin agregar capas**, y precisa: Bronze absorbe la centralización exhaustiva; Gold permanece selectivo porque, con una capa semántica agentiva, la mayor parte del consumo se vuelve virtual (el agente compone sobre Silver al vuelo) — un mart Gold es la forma materializada/cacheada de un patrón que la capa agentiva compondría en vivo (vista materializada vs. vista lógica), no un piso que crece.
- **Master Data Management** — la disciplina clásica de golden record / survivorship. Data Canon la subsume: el esquema canónico viene del estándar; las reglas de supervivencia son parte del canon central; la resolución de entidades la hace el agente, con el residuo ambiguo en el grupo federado del dominio.
- **Modelos de información de industria** — TM Forum SID / Open Digital Architecture (Frameworx) en telecomunicaciones; BIAN en banca; ACORD en seguros; IFRS / IAS 41 / XBRL en contabilidad; GS1 en trazabilidad; BrAPI / MIAPPE / Crop Ontology / AGROVOC en ciencia vegetal. Data Canon eleva la observación "usa estándares de industria" de consejo de implementación a *premisa que socava el argumento del ownership distribuido*.
- **Teoría de la firma** (Jensen & Meckling, 1976) — el problema de agencia, del que se deriva la crítica de gobierno de «El argumento, parte II».
- **Marcos de control interno** — Sarbanes-Oxley (§302 certificación de la gerencia; §404 evaluación del control interno sobre el reporting financiero); COSO *Internal Control – Integrated Framework* (1992, actualización 2013). Data Canon no implementa estos marcos; muestra que su estructura — canon central agency-crítico + conformidad federada — es la precondición arquitectónica de un ambiente de control conforme a ellos.

---

## Conclusión

Data Mesh no estaba equivocado. Resolvía un problema real — la complejidad de datos a escala desbordaba a cualquier equipo central — con la herramienta de su época: repartir el trabajo cognitivo entre muchas unidades cercanas al conocimiento, alinear la arquitectura con la organización. Inteligente y contingente.

Dos cosas cambiaron la premisa: la era agentiva removió — en la medida en que sus capacidades rinden — el límite cognitivo que hacía obligatorio repartir; y la madurez de los estándares de información de industria mostró que la semántica de dominio, que Data Mesh asumía local, en buena parte se adopta de afuera. A eso se suma un dato que Data Mesh no pesó: distribuir el ownership deja al definidor de cada cifra a cargo de la forma en que esa cifra se reporta — exactamente el conflicto que los marcos de control interno no tolerarían. La recentralización del núcleo agency-crítico no es solo posible: es la estructura correcta.

Lo que persiste — la responsabilidad — no se evapora: se recentraliza en su núcleo y se federa en su periferia. La autoridad sobre la semántica de reporte y la política de calidad vive arriba (el directorio y una autoridad del canon delgada); la conformidad, la gestión de brechas y el modelado del core propio no sensible se reparten en grupos federados por dominio, cada uno ligado a su foro de estándares. Eso es gobernanza — centralizada donde el control lo exige, federada donde la cercanía al dominio ayuda, anclada en todo caso a un canon que ningún dominio puede redefinir. A ese patrón lo llamamos **Data Canon**: Data Fabric con principios de gobernanza de Mesh, anclados a un canon central, operado por agentes, responsable ante el directorio. No hay que asumir la disciplina distribuida de Data Mesh ni montar un centro de excelencia monolítico; hay que montar la autoridad del canon, los grupos federados, adoptar el mosaico de estándares, y decidir — a nivel directorio — ser una empresa en tiempo real. Y de paso, esa estructura *es* el cimiento del control interno sobre la información del negocio — y honra, esta vez de verdad, la gobernanza computacional federada que Dehghani propuso.

<!-- standalone -->
---

## Agradecimientos

Este capítulo se desarrolló en el contexto de la práctica de consultoría en plataformas de datos, con asistencia de IA bajo la metodología colaborativa Wingworking. Las versiones preliminares fueron sometidas a discusión crítica; los errores que queden son del autor.
<!-- /standalone -->

---

## Referencias

**Data Mesh:**
- Dehghani, Z. *How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh.* martinfowler.com, 20-may-2019.
- Dehghani, Z. *Data Mesh Principles and Logical Architecture.* martinfowler.com, 3-dic-2020.
- Dehghani, Z. *Data Mesh: Delivering Data-Driven Value at Scale.* O'Reilly Media, 2022.

**Teoría de la firma y control interno:**
- Jensen, M. C. & Meckling, W. H. *Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure.* Journal of Financial Economics, 3(4), 1976.
- Sarbanes-Oxley Act of 2002 (EE.UU.) — §302, §404.
- COSO. *Internal Control – Integrated Framework.* 1992 (actualización 2013).

**Estándares de información de industria:**
- TM Forum — *Information Framework (SID)* / *Open Digital Architecture (Frameworx).* https://www.tmforum.org/open-digital-architecture/information-framework-sid/
- BIAN — *Banking Industry Architecture Network.*
- ACORD — *Data and messaging standards for the insurance industry.*
- IFRS Foundation — *IAS 41 Agriculture*; marco general IFRS; XBRL.
- GS1 — *Identification and traceability standards (GTIN, GLN, EPCIS).*
- AgGateway — *ADAPT Standard.* https://adaptstandard.org/
- *BrAPI (Breeding API) v2.* https://brapi.org/
- *MIAPPE 1.1 (Minimum Information About a Plant Phenotyping Experiment).* https://www.miappe.org/
- *Crop Ontology.* https://cropontology.org/
- *AGROVOC* (FAO) — multilingual agricultural vocabulary.

---

## Glosario del capítulo

| Término | Definición operativa |
|---|---|
| **Data Mesh** | Patrón de arquitectura de datos (Dehghani, 2019–2022): ownership descentralizado por dominio, datos como producto, plataforma de autoservicio, gobierno federado |
| **Data Fabric** | Capa de integración basada en metadatos activos, transformación inferida y capa semántica unificada; el sostén técnico de la arquitectura, potenciado por la era agentiva |
| **Data Canon** | El patrón propuesto en este capítulo: Data Fabric con principios de *gobernanza* de Mesh, anclados a un canon central; semántica de reporte adoptada de estándares de industria; política de calidad estructural de directorio; gobernanza federada por dominio (anclada al canon) para la conformidad, las brechas y el core propio. El nombre viene del *ancla semántica externa y autoritativa a la que todo se conforma* |
| **Era agentiva** | El estado del arte en el que sistemas de IA (modelos de lenguaje + orquestación de agentes) ejecutan autónomamente mapeo de esquemas, resolución de entidades, transformación, mantenimiento de pipelines y descubrimiento de datos a una escala impracticable para equipos humanos centralizados |
| **Medallion (Bronze/Silver/Gold)** | Las tres zonas del lakehouse: Bronze = crudos fieles por fuente; Silver = conformado al modelo canónico; Gold = productos de datos selectivos |
| **El canon** | El cuerpo central, no discrecional, al que todo se conforma: la semántica canónica de reporte (estándares de industria adoptados + lo que de ello se derive), las reglas de supervivencia, la política de calidad. Lo custodia la autoridad del canon; ningún dominio puede redefinirlo |
| **Autoridad del canon** | El órgano central, *delgado*, que custodia el canon: ratifica y mantiene la semántica de reporte, las reglas de supervivencia y la política de calidad, y calibra el sistema agentivo. No opera pipelines; no hace trabajo de campo. Es la pieza de control interno independiente de las operaciones |
| **Grupos federados de conformidad** | Una red de grupos, uno por dominio / capa, *ligeros*, cada uno ligado a su foro de estándares especializado: hacen triaje de brechas, enlace con el foro (empujar la brecha río arriba), y el modelado del dato propietario no agency-crítico de su dominio. Las propuestas que tocan cifras de reporte las elevan a la autoridad del canon para ratificación |
| **Reglas de supervivencia** | Las reglas pre-especificadas (parte del canon) que deciden, cuando varias fuentes describen la misma entidad canónica con valores discrepantes, cuál valor prevalece en el registro dorado |
| **Problema de agencia** | (Jensen & Meckling, 1976.) El conflicto de interés estructural entre administradores (agentes) y accionistas (principales): los primeros tienden a presentar su gestión de la forma que más los favorece |
| **Estándar-mosaico** | El estándar corporativo de una organización: ensamblado de estándares externos por capa más un modelo propio para el core que ningún cuerpo cubre |

---

