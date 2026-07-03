# Capítulo 1 · La Línea Nadella

Todo este libro gira alrededor de una sola pregunta — y de la respuesta arquitectónica que esa pregunta exige. La pregunta la dejó caer, casi al pasar, el CEO de Microsoft; este capítulo la convierte en la frontera que hoy parte a la industria en dos: la **Línea Nadella**. La respuesta — la construcción formal que da título al libro — llegará a su tiempo, cuando el lector tenga el paradigma completo en la mano.

En diciembre de 2024, Satya Nadella se sentó frente a Brad Gerstner y Bill Gurley en el podcast BG2 y dejó caer una frase que sus entrevistadores no esperaban. La conversación venía hablando del futuro de la productividad, del rol de los copilotos, de cómo Microsoft estaba pensando la siguiente década del software empresarial. Nadella, sin tono de profecía, casi como si estuviera diciendo lo obvio, soltó la frase que daría nombre a este libro:

> *La noción de que las aplicaciones de negocio existen, probablemente es donde todo colapsará, en la era de los agentes.*

La declaración pasó casi desapercibida. Se publicaron docenas de cortes del podcast, se discutió mucho más sobre OpenAI y los modelos de razonamiento, sobre la economía de cómputo, sobre el rol de NVIDIA. Pero esa frase contenía una predicción que, si resulta correcta, cambia el orden completo del software empresarial moderno. La predicción no era sobre IA — era sobre **aplicaciones**: específicamente, sobre la afirmación de que dejarán de existir como categoría.

Nadella no estaba hablando de evolución. No dijo "las aplicaciones serán más inteligentes". No dijo "las aplicaciones tendrán copilotos embebidos". Dijo *colapsará*. Y dijo *donde todo colapsará* — singular, definitorio. Si Microsoft, dueño de la suite ofimática más extendida del planeta, predice que las aplicaciones de negocio dejan de existir, hay que entender por qué.

La cita completa merece leerse, porque contiene más que el pronóstico — contiene la **mecánica** del colapso:

> *"…son esencialmente bases de datos CRUD con un montón de lógica de negocio. La lógica de negocio se irá toda a estos agentes, y estos agentes van a ser CRUD multi-repositorio: no van a discriminar cuál es el backend. Van a actualizar múltiples bases de datos, y toda la lógica estará en la capa de IA, por así decirlo. Y una vez que la capa de IA se convierta en el lugar donde está toda la lógica, entonces la gente empezará a reemplazar los backends."*

Léase con calma: Nadella describe **dos fases**. Primero colapsa la interfaz — la lógica migra a la capa de agentes, que operan sobre los repositorios sin discriminar el backend. Después, con la lógica ya en la capa de IA, empiezan a reemplazarse los backends mismos. Este libro formaliza exactamente esa mecánica: la capa de agentes que concentra la lógica es la arquitectura del Capítulo 4; el "CRUD multi-repositorio" gobernado es lo que el Capítulo 8 operacionaliza como CRUDLEX; y los backends que persisten invisibles, consumidos vía Conectores, son la Capa 4. La frase corta da el titular; la cita completa da el plano.

Este capítulo es la respuesta. Lo que vamos a llamar **La Línea Nadella** es la frontera conceptual entre dos futuros del software irreconciliables — uno donde las aplicaciones persisten, otro donde colapsan. Toda la industria de IA, conscientemente o no, está apostando hoy por uno u otro lado. Cada decisión de stack que una organización toma hoy es, implícitamente, una respuesta a una sola pregunta.

## La pregunta que divide a la industria

<!-- FIG:g02-linea-nadella -->
![La Línea Nadella · pregunta divisoria que parte la industria](figuras/g02-linea-nadella.png)

La pregunta es engañosamente simple:

> *¿El humano abre aplicaciones para hacer su trabajo?*

Si la respuesta es **sí**, la organización vive en lo que llamamos el lado **Agentic** de la línea. La interfaz tradicional — Excel, Salesforce, Power BI, Outlook, ServiceNow, Confluence — persiste. La IA llega como **copiloto embebido** en cada una de esas aplicaciones: el botón "Sugerir fórmula" en Excel, el "Componer email" en Outlook, la "Pregunta a tu data" en Power BI. La aplicación es el sustrato; la IA es ornamento sofisticado encima.

Si la respuesta es **no**, la organización ha cruzado al lado **Agentivo** de la línea. Las aplicaciones, **como interfaz**, han desaparecido. El humano no abre Salesforce para preguntar por su pipeline — le pregunta a un agente. El humano no abre Power BI para revisar márgenes trimestrales — le pregunta a un agente. Las aplicaciones pueden seguir existiendo *por debajo*, como infraestructura backend invisible que el agente consulta, pero el humano ya no las ve. Su interfaz primaria con el mundo digital es la **conversación con un agente que tiene acceso a todo**.

La diferencia entre ambos lados no es de grado — es **categórica**. Un Mundo Agéntico muy avanzado, con copilotos perfectos en cada aplicación, sigue siendo Agentic mientras el humano mantenga el hábito de abrir aplicaciones. Un Mundo Agentivo incipiente, donde la conversación con un agente todavía es torpe, ya cruzó la línea si el humano dejó de abrir aplicaciones para hacer su trabajo. La frontera la marca el comportamiento del humano, no la sofisticación técnica del sistema.

La pregunta es importante porque no admite término medio honesto. Un humano que abre veinte aplicaciones al día y un humano que conversa con un agente todo el día son dos modelos operativos distintos del trabajo profesional, y las arquitecturas técnicas que los soportan son **incompatibles**. Una organización que apuesta a que las aplicaciones persisten construye una cosa; una organización que apuesta a que colapsan construye otra. No se puede construir las dos simultáneamente con coherencia.

## Lo que separa la línea — Agéntico y Agentivo en detalle

El paradigma **Agéntico** describe el horizonte donde los agentes de IA son herramientas complementarias dentro de un universo de aplicaciones que sobrevive. La interfaz tradicional persiste. El empleado sigue siendo el operador del software — abre las aplicaciones, navega sus menús, pulsa sus botones —, solo que ahora cada aplicación tiene **copilotos** que aceleran lo que el humano hacía a mano. Microsoft 365 Copilot dentro de Word, Gemini for Workspace dentro de Google Docs, Salesforce Einstein dentro de Salesforce, GitHub Copilot dentro del IDE.

El paradigma agéntico es **evolución incremental**. La forma de trabajar no cambia: cambia la velocidad. El analista financiero sigue construyendo su modelo en Excel — solo que ahora le pide al copiloto que sugiera la fórmula correcta en lugar de buscarla en la documentación. El consultor sigue redactando su propuesta en Word — solo que ahora el copiloto le ayuda a estructurar el primer borrador. El ejecutivo sigue revisando dashboards en Power BI — solo que ahora puede preguntarle al copiloto que le explique una anomalía. La habilidad requerida es una extensión natural de la habilidad actual: el empleado que sabía operar Excel ahora aprende a *operar Excel con copiloto*. Misma aplicación, misma estructura mental del trabajo, mejor velocidad.

El paradigma **Agentivo** describe un horizonte cualitativamente distinto. En el Mundo Agentivo, los agentes **son** la interfaz. Las aplicaciones, como categoría perceptible para el humano, **colapsan**. El analista financiero deja de abrir Excel: le pregunta directamente a un agente por qué cayeron los márgenes en Q3. El agente, por debajo, consulta sistemas que pueden o no incluir bases de datos de Excel — pero el humano nunca ve la celda. El consultor deja de abrir Word: le dicta a un agente la estructura de la propuesta y revisa el resultado. El ejecutivo deja de abrir Power BI: el agente le envía proactivamente las anomalías que detectó, en formato conversacional, sin dashboards de por medio.

El paradigma agentivo es **transformación fundamental**. La forma de trabajar cambia. La habilidad requerida se redefine: ya no se trata de saber operar aplicaciones sino de **dirigir agentes** — formular bien las solicitudes, validar respuestas, gobernar lo que los agentes deciden y ejecutan. El analista que en el Mundo Agéntico se preciaba de saber Excel a fondo, en el Mundo Agentivo se precia de saber **plantear preguntas analíticas** que el agente puede responder. La aplicación específica — Excel, Power BI, Salesforce — pasa a ser detalle de implementación que el humano no toca.

El Mundo Agentivo **no implica que las aplicaciones desaparezcan del todo**. Implica que dejan de ser la **interfaz** del humano. Salesforce, como sistema que almacena información de clientes, puede seguir operando perfectamente en el Mundo Agentivo — solo que el agente lo consulta vía API, no el humano vía UI. La aplicación se vuelve **infraestructura backend invisible**. Sobrevive como repositorio de datos y lógica de negocio, pero pierde su rol de superficie de trabajo. Esto distingue el escenario agentivo de uno apocalíptico donde "todo el software muere" — el software sobrevive, lo que muere es la **GUI** como interfaz primaria del trabajo cognitivo.

## Mundo Agentivo y mundo agéntico — una distinción tipográfica deliberada

La industria de habla inglesa tomó *agentic AI* como término general para cualquier IA que actúa con grado de iniciativa. El término circuló rápido y se llenó de contenidos heterogéneos: copilotos embebidos, asistentes virtuales, sistemas autónomos. Hoy *agentic AI* significa cualquier cosa que un proveedor quiera vender bajo ese paraguas. La distinción que Nadella hizo en BG2 — la distinción entre los dos lados de la línea — quedó sepultada bajo el ruido del marketing.

Este libro mantiene la distinción que la industria consolidada perdió. La distinción es cualitativa, no de grado. **Agéntico** describe el modo evolutivo: agentes que complementan aplicaciones. **Agentivo** describe el modo transformacional: agentes que reemplazan aplicaciones como interfaz. Agéntico dice: *las herramientas siguen, pero ahora son más inteligentes*. Agentivo dice: *las herramientas que conocemos desaparecen como interfaz; lo que queda es conversación con agentes*.

Si tomáramos *agentivo* y *agéntico* solamente como adjetivos en español, la diferencia entre ambas categorías quedaría reducida a un cambio de tilde — diferencia que ningún lector retiene. Por eso este libro adopta una **convención tipográfica deliberada**: cuando los términos refieren al **paradigma** como sustantivo nombrado — la visión, la categoría, el lado de la línea —, se escriben capitalizados: el **Mundo Agentivo**, el **Mundo Agéntico**. Cuando los mismos términos se usan como **adjetivo descriptivo** — calificando un sistema, una organización, una era —, se escriben en minúscula: *un sistema agentivo*, *una era agéntica*, *productos agentivos*.

La distinción mayúscula / minúscula es la que carga la diferencia categórica. Cuando el lector encuentra *"el Mundo Agentivo es el destino"*, lee el sustantivo del paradigma — la entidad referenciable que el libro defiende. Cuando encuentra *"construir un sistema agentivo serio"*, lee el adjetivo descriptivo — calidad de un objeto particular. Es la misma convención que usan tratados técnicos serios: *Bounded Context* en Eric Evans, *Aggregate* en Domain-Driven Design, *Replication* en Kleppmann. El concepto canónico va capitalizado; el uso descriptivo va en minúscula.

El costo de esta convención es un microsegundo de atención del lector cuando ve las dos formas. El beneficio es preservar la categoría sin recurrir a un calco del inglés que el lector hispanohablante no acepta naturalmente. Cuando alguien lee *"el Mundo Agentivo"* y le suena distinto de *"un mundo agentivo"* sin más, está captando exactamente la diferencia que el libro pretende defender.

## ¿Quién apuesta a cada lado, y por qué?

<!-- FIG:g03-pregunta-divisoria -->
![La pregunta divisoria · flujo de consecuencias arquitectónicas](figuras/g03-pregunta-divisoria.png)

A inicios de 2026, los principales actores de la industria han tomado posiciones identificables en la pregunta de la Línea Nadella. La división no es ideológica — es **de modelo de negocio**. Cada actor predice el mundo que protege su posición competitiva, y aunque las predicciones se publican como visión técnica, son en última instancia predicciones sobre dónde va a sobrevivir el flujo de caja de su empresa.

**Microsoft (Satya Nadella)** apuesta abiertamente por el Mundo Agentivo. La apuesta es coherente con un reposicionamiento estratégico que Microsoft viene haciendo durante años. La empresa que construyó su fortuna sobre Office se está reconvirtiendo en plataforma de agentes: Copilot Studio para construir agentes empresariales, AutoGen como framework de orquestación multi-agente, Microsoft 365 Copilot integrando agentes especializados que reemplazan, no extienden, las interfaces tradicionales. Microsoft puede permitirse predecir el colapso de las aplicaciones porque su parque instalado se convierte en sustrato — los datos que viven en SharePoint, Outlook, Teams, OneDrive ya están en su infraestructura. Si las GUIs colapsan, los datos siguen siendo suyos. Para Microsoft, el lado Agentivo es donde su flujo de caja sobrevive.

**xAI (Elon Musk)** apuesta también por el Mundo Agentivo, aunque desde una posición distinta. Musk no tiene una suite ofimática que defender; lo que tiene es Grok integrado a X y la integración planeada con vehículos Tesla. Su apuesta es construir un agente que opere autónomamente sobre tareas extensas — no como asistente de aplicación, sino como operador de procesos. Para xAI, el Mundo Agentivo es donde su producto tiene relevancia: en un Mundo Agéntico con copilotos embebidos en aplicaciones existentes, Grok compite con productos consolidados (Office Copilot, Google Gemini); en un Mundo Agentivo, compite por una nueva categoría sin incumbents establecidos. Y conviene registrar que la posición de Musk es más radical que la de este libro: en su formulación no solo colapsa la interfaz — tampoco sobreviven las aplicaciones como backend (*"las apps desaparecerán, como las cintas VHS de Blockbuster"*; los teléfonos, "nodos de borde para inferencia de IA"). El espectro real tiene tres posiciones — Agéntico, Agentivo (la interfaz colapsa; el backend persiste, invisible y gobernado) y Agentivo extremo (tampoco hay backends) — y la tesis de este libro es deliberadamente la del medio: la que se puede sostener con arquitectura.

**OpenAI (Sam Altman)** ocupa una posición más ambigua. Públicamente Altman ha favorecido la narrativa agéntica — "GPT como herramienta complementaria de las aplicaciones existentes" — coherente con el modelo de negocio API-céntrico de OpenAI: cuanto más se invoque GPT desde aplicaciones existentes, más tokens se cobran. Pero internamente, OpenAI ha desarrollado capacidades agentivas crecientes (GPTs como agentes-en-aplicación, Operator como agente de ejecución, una visión declarada de "AGI"). La ambigüedad refleja la realidad operativa: OpenAI gana dinero hoy en el Mundo Agéntico, pero su valuación supone que ganará exponencialmente más en el Mundo Agentivo.

**Google (Sundar Pichai)** apuesta por el Mundo Agéntico dominante. La razón es estructural: el modelo de negocio de Google se sostiene sobre la búsqueda y la publicidad atada a interfaces — una página de Google Search con anuncios, un dashboard de Google Workspace con suscripción mensual. Si las GUIs colapsan, Google pierde la superficie donde monetiza. Pichai habla de Gemini como "capa que potencia" Search, Workspace y Android — verbo deliberado: *potencia*, no *reemplaza*. La predicción es coherente con su modelo: las aplicaciones de Google sobreviven, mejoradas con IA, pero no colapsan.

**NVIDIA (Jensen Huang)** ocupa una posición técnica sin necesidad de tomar partido. NVIDIA vende cómputo. Cualquiera de los dos mundos consume GPUs masivamente: el Mundo Agéntico requiere copilotos que invocan modelos por cada acción del usuario; el Mundo Agentivo requiere agentes que operan continuamente en background. Huang habla de los agentes como "una nueva clase de cargas de trabajo" — neutralidad estratégica, porque NVIDIA gana en los dos escenarios.

**Anthropic (Dario y Daniela Amodei)** apuesta predominantemente por el Mundo Agentivo, con énfasis en autonomía prolongada y herramientas. La introducción del Model Context Protocol (MCP) en noviembre de 2024 es señal clara: MCP es un estándar abierto para que los agentes se conecten a tools externos — exactamente la pieza arquitectónica que la categoría agentiva necesita. Claude está diseñado, desde su entrenamiento, para uso autónomo prolongado en lugar de respuestas turn-by-turn cortas. La apuesta agentiva de Anthropic es coherente con su tesis sobre AGI: el camino al modelo más capaz pasa por modelos que actúan, no por modelos que responden.

**Meta (Mark Zuckerberg)** apuesta por el Mundo Agéntico. Llama, su modelo de fundación, se distribuye open-source para ser usado dentro de aplicaciones de terceros. Los agentes en WhatsApp e Instagram son features dentro de aplicaciones que existen. Meta se beneficia de un mundo donde las plataformas sociales sobreviven y los agentes son ornamento dentro de ellas.

La división resultante es reveladora. Los actores que predicen el Mundo Agentivo son aquellos cuyo modelo de negocio sobrevive — o mejora — en ese escenario. Los actores que predicen el Mundo Agéntico son aquellos cuyo modelo de negocio depende de que las aplicaciones persistan. La predicción técnica de cada uno es, debajo del lenguaje neutro, una predicción de supervivencia económica.

## ¿Por qué la pregunta importa hoy y no después?

La objeción razonable de un ejecutivo prudente leyendo este capítulo es: *aun si la Línea Nadella es real, su cruce parece lejano. ¿Por qué tomar decisiones hoy basándose en una transición que tomará una década?*. Tres razones operativas hacen que la pregunta sea **inevitable** en el horizonte de decisión actual, no postergable.

**La primera razón es la velocidad de la transición.** Los datos de campo no permiten ya tratar el Mundo Agentivo como horizonte lejano: el mercado global de IA agentiva multiplica su tamaño por veinte en una década, a una tasa compuesta superior al cuarenta por ciento anual. La transición no es lineal: se acelera. El **Capítulo 2 desarrolla** las cifras y las fuentes que sustentan esta velocidad. Quien planifica para el horizonte 2027-2028 está planificando para un mundo donde una fracción material de las decisiones operativas las toman agentes.

**La segunda razón es el horizonte de las decisiones de stack que se toman ahora.** Una empresa que adopta hoy una suite empresarial — Microsoft 365, Google Workspace, Salesforce Sales Cloud, ServiceNow — está comprometiendo capital y tiempo de implementación que se amortiza típicamente en tres a cinco años. Esa misma ventana es exactamente la frontera donde la Línea Nadella se vuelve verificable o falsable. La pregunta no se pospone: cada decisión de stack que la organización toma hoy es implícitamente una respuesta. Renovar Office 365 con un horizonte de cinco años es implícitamente apostar a que el Mundo Agéntico durará cinco años. Migrar a una arquitectura agentiva nativa es implícitamente apostar a que el cruce ocurrirá dentro de ese horizonte. No tomar la decisión es también una decisión: es default a la inercia, que casi siempre coincide con apostar al lado agéntico por mero hábito institucional.

**La tercera razón es la asimetría del costo de equivocarse.** Una organización que apuesta por el lado agéntico e invierte en arquitecturas dependientes de aplicaciones — workflows atados a UIs, integraciones por scraping de pantallas, lógica de negocio embebida en cómo se ve el sistema — construye **deuda arquitectónica creciente** si la línea se cruza. Migrar al Mundo Agentivo desde una base agéntica no es extender lo construido: es desensamblarlo. Inversamente, una organización que apuesta por el lado Agentivo temprano y construye con la arquitectura correcta puede sostener su sistema bajo ambos paradigmas durante el período de transición, sin reescritura. Las cuatro capas que este libro desarrolla en el Capítulo 4 — Interacción, Cognición, Autonomía, Acceso — son válidas tanto si la Capa 1 sigue siendo una GUI tradicional como si es una conversación con un agente. La asimetría es estructural: construir Agentivo desde el inicio sirve a los dos mundos. Construir agéntico puro y migrar después no.

Esta asimetría es lo que hace impostergable la pregunta. Una empresa puede equivocarse al apostar por el Mundo Agentivo demasiado temprano — perder algunos años de eficiencia mientras la transición no termina de ocurrir — pero no se queda sin opciones. Una empresa que apuesta por el Mundo Agéntico asumiendo que el cruce no ocurrirá, y luego descubre que sí ocurrió, enfrenta una migración estructural costosa o, peor, queda con sistemas inviables operando en un mercado que evolucionó. El error en una dirección es inconveniencia; el error en la otra es deuda arquitectónica difícil de revertir.

## ¿Cómo se cruza la línea? — la transición no es un evento

Hay un riesgo de leer la Línea Nadella como si fuera un acontecimiento puntual: el día que las aplicaciones desaparecen, el momento de la transición. Esa lectura es errada. **El cruce de la línea es una transición progresiva que se acumula** capa por capa, función por función, equipo por equipo. Una organización no se vuelve agentiva un lunes. Se vuelve **progresivamente** agentiva: primero un proceso, después un equipo, después una función, después la mayor parte de su operación cotidiana.

La transición tiene tres dinámicas características — **coexistencia evolutiva** (el paradigma actual y el emergente conviven durante años), **asimetría entre funciones** (no todas cruzan al mismo ritmo) y **asimetría temporal** (el ritmo del cruce tampoco es uniforme en el tiempo) — y una consecuencia de fondo: la **reorganización del trabajo humano**, que se desplaza de ejecutar tareas a gobernar agentes que las ejecutan. El **Capítulo 2 lo desarrolla** en detalle, con los datos de campo que lo sustentan.

Las tres dinámicas tomadas juntas explican por qué la transición no es traumática para la organización que la planifica. Una organización que reconoce la coexistencia evolutiva no se ve obligada a un big bang; una que acepta la asimetría entre funciones no fuerza ritmos uniformes; una que rediseña los roles humanos hacia gobernanza no descarta su capital humano sino que lo recoloca. La transición es progresiva, asimétrica y reorganizativa — y eso es lo que la hace operable. El cruce admite además un indicador operativo — el **porcentaje agentivo**: qué fracción de sus tareas puede un empleado delegar por completo sin abrir una aplicación. *AURA*, el volumen II, lo desarrolla como instrumento de diagnóstico junto a sus modelos de madurez.

## ¿Por qué la línea podría no cruzarse — y qué cambia si no se cruza?

Una tesis que no enfrenta su objeción más fuerte no está validada — está sin probar. Este capítulo ha argumentado que la pregunta es inevitable y que el costo de equivocarse es asimétrico; corresponde ahora dejar que el otro lado hable. Cinco argumentos serios sostienen que la línea podría no cruzarse — o cruzarse solo parcialmente.

**El argumento del control.** Los humanos tienen sesgo de control: preferimos ver y validar antes de ejecutar, incluso cuando delegar sería más eficiente. Un CFO puede no querer preguntar "¿están bien nuestras finanzas?" y confiar en la respuesta — querrá **ver** los números, las fórmulas, las fuentes. La interfaz gráfica provee una sensación de control que la conversación no replica, y podría conservar por eso los casos de uso de alto riesgo y alta responsabilidad.

**El argumento de la complejidad irreducible.** Los sistemas empresariales no son solo "bases de datos CRUD con lógica de negocio": acumulan décadas de reglas que ningún agente puede inferir sin documentación que frecuentemente no existe, integraciones con comportamientos emergentes de años de uso, y casos borde codificados a raíz de incidentes reales. Un agente que los orqueste sin entenderlos genera errores catastróficos; entrenarlo sistema por sistema replica la complejidad que promete eliminar.

**El argumento regulatorio.** Sectores enteros — finanzas, salud, gobierno — operan bajo marcos que exigen trazabilidad determinística y responsabilidad asignable, y los agentes son fundamentalmente probabilísticos: ante inputs idénticos pueden producir resultados distintos. Hasta que eso cambie, hay industrias que permanecerán del lado agéntico por mandato legal, no por atraso técnico.

**El argumento económico.** La transición exige reentrenar fuerzas laborales completas, reescribir o abandonar billones en software existente, y montar una infraestructura de gobernanza que en buena parte aún no existe. Una empresa racional puede quedarse del lado agéntico simplemente porque cruzar cuesta más de lo que rinde — durante años.

**El argumento histórico.** Cada generación tecnológica produjo la misma profecía de extinción total — "el PC matará al mainframe", "la web matará al software instalado", "la nube matará al on-premise" — y cada vez la realidad fue coexistencia estratificada, con plazos tres a cinco veces más largos que los predichos.

Estos argumentos no derriban la Línea Nadella. La **refinan**, y conviene incorporar el refinamiento a la tesis en vez de esquivarlo: la línea puede ser **asintótica** — aproximación indefinida sin cruce completo —; cada industria tiene **su propia línea**, y algunas quizá nunca crucen; el cruce puede **revertirse** ante incidentes; y la **coexistencia es el estado estable** — agéntico para el alto riesgo, agentivo para el resto, con la proporción moviéndose en una sola dirección.

Y hay una segunda razón para enfrentarlos en vez de esquivarlos: **este libro existe, en buena parte, porque esas objeciones son válidas.** El argumento del control se responde con la Transparencia y el registro auditable de Trust Infrastructure (Capítulo 5 §4): el CFO que quiere ver los números los ve — con linaje. El regulatorio se responde con la certificación que reside en el componente certificado y no en el código generado (Capítulo 5 §3), y con el append-only log del Capítulo 8. El de la complejidad se responde con una Capa 3 que consolida saber operativo en Botlets maduros en lugar de improvisar cada vez (Capítulo 5 §2). Y el económico es exactamente la asimetría que ya argumentamos: construir agentivo desde el inicio sirve a los dos mundos. Las objeciones no son enemigas de la arquitectura — son su lista de requisitos.

---

La pregunta no es retórica. Es la pregunta de la cual dependen las decisiones de stack, de talento, de arquitectura, de inversión, de toda organización seria sobre el horizonte de los próximos cinco años. Es la pregunta sobre la cual descansa el resto del libro: comprender hacia dónde va el cruce permite operar con confianza en el período de transición; ignorarla expone a la organización a decisiones que envejecen mal. La pregunta es: *¿de qué lado de la Línea Nadella está construyendo su organización?*

## Resumen visual

Para apoyo de lectura posterior, los dos lados de la línea sintetizados en una tabla comparativa.

| | **Mundo Agéntico** (pre-línea) | **Mundo Agentivo** (post-línea) |
|---|---|---|
| **Estado de las aplicaciones** | Persisten como interfaz primaria | Colapsan como interfaz; sobreviven como backend |
| **Pregunta operativa** | El humano abre aplicaciones para trabajar | El humano conversa con agentes que tienen acceso a sistemas |
| **Rol de la IA** | Copilotos embebidos en cada aplicación | Agentes que reemplazan la interfaz tradicional |
| **Habilidad humana valiosa** | Saber operar aplicaciones | Saber dirigir agentes |
| **Transformación** | Evolución incremental, misma forma de trabajar | Transformación fundamental, nueva forma de trabajar |
| **Predicen** | Altman (OpenAI)\*, Pichai (Google), Zuckerberg (Meta) | Nadella (Microsoft), Musk (xAI), Amodei (Anthropic) |
| **Apuesta económica** | El modelo de negocio actual sobrevive | El modelo de negocio se reinventa |

\* posición con matices; ver el cuerpo del capítulo.

---

Lo que sigue — el Mundo Agentivo (Capítulo 2), la cartografía pre-agentiva (Capítulo 3), la arquitectura formal en cuatro capas (Capítulo 4) y las primitivas (Capítulo 5) — cobra coherencia bajo una única construcción central que el libro propone como unidad mínima de despliegue: el **AgencyDomain**. El libro lo nombra explícitamente en el título no por elección retórica, sino porque toda la spec gira alrededor suyo. La Línea Nadella es la pregunta del paradigma; el AgencyDomain es la respuesta arquitectónica.
