# Capítulo 6 · Mercado

Una arquitectura no vive en el vacío: compite en un mercado. Este capítulo sitúa a cualquier actor mediante la **cadena de valor de IA** —once eslabones × cuatro profundidades—, profundiza en eslabones selectos con *deep-dives* y extiende el modelo al **mundo de carbono**. La §1 desarrolla el modelo general; las secciones siguientes lo aplican.

## La cadena de valor de IA

> **Nota sobre fechabilidad de los productos mencionados.** Los listados de productos específicos en este capítulo describen el estado del mercado de IA agentiva a **mayo de 2026**. La estructura conceptual de los eslabones de la cadena de valor es estable; los actores listados son ilustrativos del momento. Lecturas posteriores deben tomar los nombres como instantánea, no como cobertura permanente.

La industria de Inteligencia Artificial se presenta a mayo de 2026 como un ecosistema denso donde decenas de productos, plataformas y frameworks compiten y coexisten. Sin un modelo de clasificación claro, resulta difícil responder preguntas fundamentales que cualquier ejecutivo, arquitecto o estratega serio se hace cuando enfrenta el campo: ¿dónde juega cada actor? ¿qué eslabones domina? ¿dónde hay concentración y dónde hay espacio? ¿en qué territorio compite mi propuesta y contra quién?

La fragmentación del campo no es accidente. Es resultado de un crecimiento explosivo donde cada nuevo entrante construye su propia categoría, escoge su propio vocabulario, define su propio posicionamiento. El consumidor — sea un comprador empresarial, un analista de mercado, un inversionista — termina abrumado por un lenguaje que cada actor moldea a su conveniencia. *Plataforma de agentes, gateway de IA, framework de LLM, infraestructura agentiva, agente autónomo, asistente vertical, marketplace de modelos* — todos términos que circulan sin definición precisa, todos términos que distintos vendors usan con distintos significados.

Este capítulo propone un mapa que disciplina esa conversación. El mapa no resuelve todas las ambigüedades del campo — la industria está demasiado joven para que un mapa único capture toda su complejidad —, pero entrega un marco compartible: un lenguaje preciso que permite situar a cualquier actor en su posición, comparar actores entre sí, y razonar sobre la estrategia de un producto particular respecto al campo más amplio. El mapa que sigue es la **cadena de valor de IA**, en su versión bidimensional. Es contribución original de este libro, derivada del trabajo previo del autor en la conceptualización del campo, y se ofrece como herramienta abierta para la industria, no como propiedad intelectual propietaria.

### Las dos dimensiones

El modelo organiza la cadena de valor tecnológica de IA en **dos dimensiones**. Las dos dimensiones operan ortogonalmente — un actor se sitúa en cada una independientemente —, y la combinación de ambas produce el espacio de posicionamiento donde el actor vive. Las dos dimensiones son **cobertura** y **profundidad**.

La **cobertura** es la dimensión horizontal: qué eslabones de la cadena de valor toca el actor. Un actor puede tocar uno solo, varios, o muchos. La cobertura es métrica de **alcance** — cuánto del territorio del campo opera el actor. Un actor con cobertura amplia toca muchos eslabones; un actor con cobertura focal toca uno o pocos.

La **profundidad** es la dimensión vertical: con qué nivel de control opera el actor dentro de cada eslabón. Un actor puede consumir un eslabón superficialmente — usar APIs de terceros — o construir el eslabón profundamente — fabricar la tecnología de base. La profundidad es métrica de **control** — cuánto del eslabón el actor domina. Un actor con profundidad superficial depende de proveedores subyacentes; un actor con profundidad profunda construye el sustrato sobre el cual otros operan.

Cada actor puede posicionarse en uno o más eslabones, a distintas profundidades en cada uno. Un mismo actor puede operar a profundidad Core en su eslabón nativo y a profundidad Plataforma en eslabones adyacentes — es patrón común en el mercado contemporáneo.

El resultado es un **mapa que permite** clasificar cualquier producto de IA según los eslabones que abarca, comparar actores por cobertura y profundidad en la cadena, identificar zonas de concentración y zonas de oportunidad, y posicionar estratégicamente productos propios frente al mercado.

### Los once eslabones

<!-- FIG:g33-once-eslabones -->
![Los once eslabones de la cadena de valor de IA](figuras/g33-once-eslabones.png)

La cadena de valor de IA se descompone en once eslabones secuenciales, cada uno con función clara y separable. La separación no es arbitraria: cada eslabón corresponde a una capacidad funcional distinta que un actor puede operar independientemente, con economía y dinámica competitiva propias.

Desplegamos cada eslabón con su descripción funcional. La secuencia no es lineal en el sentido de que un proceso de datos pase por todos los eslabones en orden, pero sí refleja una progresión conceptual desde la materia prima del campo (los datos) hasta donde el agente toca el mundo real (el entorno).

**Eslabón 1 · Datos** (Data Layer). Adquisición, anotación, gestión de datasets de entrenamiento. Es la materia prima que alimenta los modelos fundacionales. Los actores en este eslabón producen datasets curados, herramientas de anotación, pipelines de procesamiento de datos a gran escala. Sin este eslabón, los modelos no existen.

**Eslabón 2 · Modelo** (Foundation Model). Modelos base de IA: LLMs y modelos multimodales que proveen capacidades fundamentales de lenguaje, razonamiento y generación. Es donde los grandes laboratorios — OpenAI, Anthropic, Google, Meta, DeepSeek — concentran capacidad. Los actores aquí construyen los modelos que el resto del campo consume.

**Eslabón 3 · Acceso** (Access Layer). APIs y capas de acceso a modelos. Control de cuotas, autenticación y monetización del consumo. Es donde la inferencia se vende como servicio: APIs de OpenAI, Anthropic, Bedrock de AWS, Vertex AI de Google. También es donde operan productos como gateways de modelo (Portkey) que ofrecen abstracción sobre múltiples modelos.

**Eslabón 4 · Agentes** (AI Agents). Interfaces conversacionales y asistentes. Desde agentes reactivos — chat — hasta agentes autónomos capaces de ejecutar tareas complejas. Es donde aparecen los productos más visibles: ChatGPT, Claude, GPT-4 con plugins, sistemas de agentes orquestados.

**Eslabón 5 · Especializaciones** (Domain Experts). Agentes autónomos especializados por dominio vertical: coding, legal, marketing, soporte, productividad, memoria del trabajo profesional. Es donde aparecen los especialistas verticales: Cursor para coding, Harvey para legal, Jasper para marketing, Fin para customer support, umeeta para memoria del engagement de consultoría. La diferencia con el eslabón 4 es de profundidad de saber-hacer en un dominio específico.

**Eslabón 6 · Runtime** (Agent Runtime). Ambiente operativo donde los agentes viven y operan de manera autónoma. Ciclo de vida, persistencia de estado, identidad, scheduling y orquestación multi-agente. Es donde la Capa 3 de la Arquitectura Agentiva se materializa como producto. Eslabón emergente — la mayoría de los actores tradicionales todavía no lo cubren explícitamente.

**Eslabón 7 · Firewall** (Security Layer). Seguridad, control y governance. Protección contra prompt injection, alucinaciones, filtrado de contenido y auditoría de uso. Productos como Lakera, Lasso Security operan aquí. Es eslabón crítico para producción enterprise — sin firewall, el sistema agentivo no puede operar en industrias reguladas.

**Eslabón 8 · Observabilidad** (Observability). Monitoreo, trazabilidad, costos y calidad de los sistemas de IA en producción. El ciclo de feedback operacional. Productos como Langfuse, LangSmith, Helicone, Arize operan aquí. Es eslabón maduro — la observabilidad de IA tiene varios productos de profundidad Core compitiendo activamente.

**Eslabón 9 · Herramientas** (Tools). Capacidades específicas que los agentes pueden invocar. Incluye meta-herramientas: protocolos (MCP), vector databases (Pinecone, Weaviate), frameworks de RAG. Es donde el agente extiende su capacidad para tocar sistemas específicos.

**Eslabón 10 · Integraciones** (Integration Layer). Puente entre el mundo IA y el Entorno. Orquestación, transformación y mapeo de lógica de integración entre sistemas. Productos como Zapier, Make, n8n operan en este eslabón en su forma tradicional; el equivalente agentivo todavía es categoría emergente.

**Eslabón 11 · Entorno** (Environment). Lo externo a la cadena: sistemas empresariales (ERPs, CRMs, bases de datos), mundo físico (IoT, procesos industriales) y sistemas biológicos. Es el eslabón menos desarrollado, y desarrollamos sus implicaciones con detalle en la sección de mundo de carbono.

Los eslabones no son arbitrarios. Cada uno corresponde a una **decisión de diseño operativo** en cualquier sistema de IA productivo. Saltarse un eslabón no es elegancia: es deuda arquitectónica que se paga en producción.

### Las cuatro profundidades

Los eslabones definen **dónde** participa un actor en la cadena. Pero dentro de un mismo eslabón, los actores operan a distintos niveles de profundidad. Un actor que consume una API de modelos y otro que entrena el modelo fundacional **ambos participan en el eslabón Modelo**, pero su diferenciación, dependencia y foso competitivo son radicalmente distintos.

El modelo define cuatro niveles de profundidad, de menor a mayor control sobre la capacidad del eslabón. Las cuatro profundidades aplican a cualquier eslabón — un actor puede ser Wrapper en Datos, Plataforma en Modelo, Core en Acceso. La uniformidad permite comparación cruzada entre eslabones distintos.

**Wrapper** (nivel 1). El actor consume capacidades vía APIs o SDKs de terceros. Agrega experiencia de usuario o lógica de negocio sin construir la capacidad subyacente. Características: baja diferenciación respecto a otros wrappers que usan los mismos proveedores subyacentes, alta dependencia del proveedor, costo de cambio bajo. Una app que llama a la API de OpenAI para responder preguntas es Wrapper en el eslabón Modelo.

**Plataforma** (nivel 2). El actor opera y gestiona capacidad propia sobre componentes Core de terceros. Agrega orquestación, SLAs y control operacional. Diferenciación moderada: el cliente paga por las capacidades operacionales que la Plataforma agrega, no por la capacidad subyacente que sigue siendo de terceros. Azure OpenAI es Plataforma en Modelo: opera modelos de OpenAI con SLAs y gobernanza enterprise, pero los modelos son del proveedor original.

**Core** (nivel 3). El actor construye la capacidad fundacional del eslabón con tecnología propia: modelos, motores o algoritmos diferenciados. Foso competitivo alto basado en propiedad intelectual. OpenAI es Core en Modelo: construye sus propios modelos. Anthropic, Google con Gemini, Meta con Llama, todos son Core en Modelo. La distinción entre Core y los niveles superiores es donde está la mayor parte del valor capturado en el campo de IA.

**Infraestructura** (nivel 4). El actor provee el sustrato computacional, de almacenamiento o conectividad sobre el cual operan los niveles superiores. Foso muy alto basado en escala y capital. NVIDIA es Infraestructura en Modelo: las GPUs que NVIDIA fabrica son el sustrato sobre el cual los modelos operan. AWS, GCP, Azure son Infraestructura en muchos eslabones — proveen el cómputo y almacenamiento subyacentes a casi toda la industria.

La progresión Wrapper → Plataforma → Core → Infraestructura es de **control creciente** sobre el eslabón. Wrapper consume; Plataforma opera; Core construye; Infraestructura sustenta. Cada nivel de profundidad típicamente implica mayor inversión, mayor especialización técnica, mayor foso competitivo. También implica mayor riesgo: un Core que apostó por una tecnología que el mercado descartó queda con activo difícil de reposicionar; un Wrapper que apuesta mal cambia de proveedor en horas.

### Cobertura × Profundidad — el espacio de posicionamiento

<!-- FIG:g34-cobertura-profundidad -->
![Espacio bidimensional · cobertura × profundidad](figuras/g34-cobertura-profundidad.png)

La combinación de cobertura (eslabones) y profundidad (niveles) produce un **espacio bidimensional** donde se posiciona cualquier actor. El eje horizontal muestra **cuántos eslabones** abarca un actor; el eje vertical muestra **a qué profundidad** participa en cada uno.

Un mismo actor puede operar a distintas profundidades en distintos eslabones. OpenAI es Core en Modelo pero Plataforma en Acceso (sus APIs) y Plataforma en Agentes (ChatGPT). Esta heterogeneidad por eslabón es la regla, no la excepción. Pocos actores tienen profundidad uniforme a través de todos los eslabones que tocan — y cuando la tienen, típicamente son actores muy enfocados como NVIDIA en Infraestructura computacional.

La diversidad de posiciones en el espacio bidimensional permite identificar arquetipos de posicionamiento que se repiten en el mercado, con propiedades estratégicas distintas. La sección siguiente desarrolla los cuatro arquetipos canónicos.

### Arquetipos estratégicos emergentes

<!-- FIG:g35-cuatro-arquetipos -->
![Los cuatro arquetipos estratégicos](figuras/g35-cuatro-arquetipos.png)

De este espacio bidimensional emergen **cuatro arquetipos** recurrentes. Cada arquetipo describe un patrón de posicionamiento con propiedades estratégicas características. Los cuatro arquetipos son: Plataforma integral, Especialista vertical, Infraestructura de dominio, Proveedor de sustrato.

#### Plataforma integral

El arquetipo de **Plataforma integral** combina cobertura amplia (tres o más eslabones) con profundidad **Core** en su eslabón nativo y profundidad **Plataforma** en eslabones adyacentes. Es el arquetipo de los grandes laboratorios de IA que dominan el campo en 2026.

OpenAI ejemplifica el arquetipo: Core en Modelo (construye GPT), Plataforma en Acceso (vende API), Plataforma en Agentes (opera ChatGPT y Operator), Plataforma en Especializaciones emergentes (los GPTs verticalizados). Anthropic sigue patrón similar pero con énfasis distinto: Core en Modelo (construye Claude), Core en Acceso vía MCP (su contribución abierta a Herramientas), Plataforma en Agentes. Google con Gemini hace análogo. Meta con Llama es caso particular: Core en Modelo distribuyendo open source, sin plataforma propia de Acceso o Agentes — su foso es la distribución del modelo, no la operación.

El foso competitivo de la Plataforma integral es la propiedad intelectual del Core combinada con la integración vertical hacia eslabones adyacentes. Un Wrapper que llama a OpenAI no puede replicar fácilmente lo que OpenAI hace en su totalidad — para hacerlo, tendría que entrenar su propio modelo (eslabón Modelo a profundidad Core), construir su propia infraestructura de Acceso, operar su propia plataforma de Agentes. Esa cadena completa requiere capital y talento que pocos actores tienen.

#### Especialista vertical

El arquetipo de **Especialista vertical** combina cobertura focal (uno o dos eslabones) con profundidad **Core**. Es el arquetipo de los actores que se han concentrado en dominios específicos y construyen profundidad allí.

Cursor ejemplifica el arquetipo en coding: Core en Especializaciones para programación. Harvey AI hace lo mismo en legal. Jasper en marketing. Fin (de Intercom) en customer support. Devin pretende Core en Especializaciones de coding autónomo. umeeta opera el mismo arquetipo en consultoría profesional, con Core en la capa de memoria del engagement. Cada uno tiene cobertura estrecha — uno o pocos eslabones — pero profundidad Core en su vertical específica.

El foso competitivo del Especialista vertical es la profundidad de saber-hacer vertical, que se materializa típicamente como Capabilities densas — el saber profesional codificado del que hablamos en el Capítulo 5. Un GPT genérico puede responder preguntas sobre legal, pero Harvey AI las responde con mucho mejor calidad porque tiene Capabilities de Legal construidas con disciplina. La diferencia no es marketing — es estructural. Un competidor que quisiera replicar Harvey tendría que construir el árbol de Capabilities de Legal con el mismo rigor, lo que toma años.

#### Infraestructura de dominio

El arquetipo de **Infraestructura de dominio** es el más reciente en la industria y el menos poblado. Combina cobertura zonal (dos o más eslabones contiguos) con profundidad **Core** transversal a un dominio funcional, con posibles extensiones a eslabones no contiguos a menor profundidad.

Un actor que es Core en Runtime, Firewall, Observabilidad, Herramientas e Integraciones — los eslabones 6, 7, 8, 9, 10 — con extensión Plataforma en Acceso constituye el caso paradigmático del arquetipo. La combinación de cobertura zonal en cinco eslabones contiguos con profundidad Core constituye un **gateway empresarial**: la capa fundacional para conectar y controlar IA en producción.

El foso competitivo de la Infraestructura de dominio es la integración profunda entre eslabones que otros actores tratan separadamente. Construir Core en Runtime es mérito; construir Core simultáneamente en Runtime, Firewall, Observabilidad, Herramientas e Integraciones, **integrados coherentemente**, es propiedad arquitectónica que pocos actores tienen. La razón estructural es que estos cinco eslabones operan juntos en producción — sin uno, los otros pierden valor — y construir solo uno deja al actor dependiente de complementarios que típicamente no existen como producto integrado.

#### Proveedor de sustrato

El arquetipo de **Proveedor de sustrato** combina cobertura mínima (un eslabón) con profundidad **Infraestructura**. Es el arquetipo de los actores que sustentan la industria desde la capa más profunda.

NVIDIA ejemplifica el arquetipo en Modelo: las GPUs que NVIDIA fabrica son el sustrato computacional sobre el cual operan los modelos. AWS, GCP y Azure son Proveedores de sustrato en múltiples eslabones — Datos, Modelo, Cómputo en general. Cisco lo es en redes para IA distribuida.

El foso competitivo del Proveedor de sustrato es escala, capital intensivo, y efectos de red en hardware o data center. Construir una empresa que compita con NVIDIA en GPUs requiere inversiones de billones de dólares y generaciones de I+D acumuladas. Construir una empresa que compita con AWS en cómputo a escala requiere infraestructura física global. Estos fosos son los más altos del campo, pero también son los que requieren mayor capital inicial y tienen ciclos de retorno más largos.

### Mapeo de actores principales

A modo de ejemplo, la tabla siguiente clasifica familias de productos representativas del mercado actual según los eslabones que abarcan y la profundidad en cada uno. Las cifras son **niveles de profundidad** (1-4); los paréntesis indican framework o meta-herramienta (para construir, no para usar).

| Actor | Da | Mo | Ac | Ag | Xp | Ru | Fi | Ob | He | In |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Datos y anotación** | | | | | | | | | | |
| Scale AI / Labelbox | 3 | | | | | | | | | |
| Hugging Face | 3 | 2 | | | | | | | | |
| **Plataformas integrales** | | | | | | | | | | |
| OpenAI (ChatGPT, GPT API) | | 3 | 2 | 2 | 2 | 3 | | | 3 | |
| Anthropic (Claude, MCP) | | 3 | 3 | 2 | | | | | 3 | |
| Google (Gemini) | | 3 | 2 | 2 | | | | | 3 | |
| Meta (Llama) | | 3 | | | | | | | | |
| Perplexity | | | 2 | 3 | 3 | | | | | |
| DeepSeek / Qwen / Ernie | | 3 | 3 | 3 | | | | | | |
| **Especializaciones verticales** | | | | | | | | | | |
| GitHub Copilot | | | | 2 | 3 | | | | | |
| Cursor / Replit | | | | | 3 | | | | | |
| Devin | | | | | 3 | 3 | | | 3 | |
| Harvey / Jasper / Fin | | | | | 3 | | | | | |
| umeeta (memoria engagement) | | | | | 3 | | | | | |
| **Sustratos agentivos** | | | | | | | | | | |
| Agentia (régimen privado) | | | | 3 | | 3 | | | | |
| Soveria (régimen público) | | | | 3 | | 3 | | | | |
| **Frameworks y herramientas** | | | | | | | | | | |
| LangChain / Graph | | | | (3) | | (3) | | | (3) | |
| AutoGPT / CrewAI | | | | (3) | | (3) | | | | |
| Pinecone / Weaviate | | | | | | | | | (3) | |
| **Operaciones y governance** | | | | | | | | | | |
| Guardrails / NeMo / Lakera | | | | | | | 3 | | | |
| Langfuse / LangSmith / W&B | | | | | | | | 3 | | |
| Zapier / Make / n8n | | | | | | | | | | 3 |
| ultraPRO (gateway empres.) | | | 2 | | | 3 | 3 | 3 | 3 | 3 |
| **Infraestructura computacional** | | | | | | | | | | |
| NVIDIA | | 4 | | | | | | | | |
| AWS / GCP / Azure | 4 | 4 | | | | | | | | |

Leyenda de eslabones: **Da** Datos · **Mo** Modelo · **Ac** Acceso · **Ag** Agentes · **Xp** Especializaciones · **Ru** Runtime · **Fi** Firewall · **Ob** Observabilidad · **He** Herramientas · **In** Integraciones. Niveles de profundidad: **1** Wrapper · **2** Plataforma · **3** Core · **4** Infraestructura. Los paréntesis — p. ej. (3) — indican framework o meta-herramienta (para construir, no para usar).

> **Nota.** La tabla cubre los eslabones 1 a 10. El eslabón 11 (Entorno) se omite por ser externo a la cadena — es el territorio sobre el cual actúan los eslabones anteriores, no un eslabón que un actor de IA ocupe a una profundidad. Sus implicaciones se desarrollan en la sección de mundo de carbono.

La tabla, leída en conjunto, permite ver patrones que la inspección individual de cada producto no revela. Las plataformas integrales tienden a concentrarse en los eslabones 2-4. Los especialistas verticales se acumulan en el eslabón 5. Los productos de operaciones y governance se distribuyen entre los eslabones 7-10. La infraestructura computacional ocupa principalmente el eslabón 2 a profundidad 4.

### Lecturas estratégicas del mapa

El mapa no es solo descriptivo — es herramienta para análisis estratégico. Tres lecturas del mapa de 2026 permiten entender el estado del campo y dónde están las oportunidades.

#### La concentración por arquetipo

Los **especialistas verticales** dominan el eslabón 5 (Especializaciones). Cursor, Harvey, Jasper, Fin, Devin: cada uno construyó Capabilities verticales densas y captura mercado en su dominio. La concentración es saludable — múltiples actores con poco solapamiento, cada uno dueño de su vertical. Es donde la innovación está más vibrante en 2026.

Las **plataformas integrales** concentran los eslabones 2-4 (Modelo, Acceso, Agentes). Cinco actores dominantes globales — OpenAI, Anthropic, Google, Meta, DeepSeek/Qwen/Ernie — y posiciones derivadas. La concentración es alta y crece con el tiempo, porque construir Core en Modelo requiere capital y talento que pocos actores pueden sostener. Es el eslabón con mayor barrera de entrada.

La **infraestructura** está concentrada en NVIDIA en cómputo y los hyperscalers en datos y cómputo a escala. Foso de capital extremo. La concentración aquí es estructural y probablemente persistente — es razonable esperar que no aparezca un entrante significativo en estos eslabones a profundidad Infraestructura en el horizonte previsible.

#### Los espacios menos disputados

Hay zonas del mapa donde la profundidad Core está abierta y donde un actor con disciplina puede construir posición competitiva sin enfrentar incumbents masivos.

El **eslabón 1 (Datos) a profundidad Core**: pocos actores Core (Scale AI, Labelbox); el resto son commodity. Hay espacio para actores que construyan capacidad propia en datos especializados.

Los **eslabones 6-10 simultáneamente** — Runtime, Firewall, Observabilidad, Herramientas, Integraciones — a profundidad Core con cobertura zonal: territorio de la Infraestructura de dominio. Actores que combinan estos cinco eslabones a profundidad Core son raros. Es el espacio donde la categoría del **gateway empresarial completo** se está abriendo.

El **eslabón 11 (Entorno)** con conexión a IoT y mundo físico: prácticamente vacío en términos de actores específicamente diseñados para el Mundo Agentivo. Es la frontera de la próxima generación, y la sección sobre mundo de carbono desarrolla las implicaciones.

#### La trayectoria de los gigantes

<!-- FIG:g36-trayectoria-gigantes -->
![La trayectoria de los gigantes · y la ventana abierta](figuras/g36-trayectoria-gigantes.png)

Los gigantes — OpenAI, Anthropic, Google, Microsoft — avanzan **eslabón a eslabón**: del Modelo al Acceso, del Acceso a los Agentes, de los Agentes a las Especializaciones. La progresión es histórica observable. OpenAI nació como laboratorio de Modelo, expandió a Acceso (API), expandió a Agentes (ChatGPT), está expandiendo a Especializaciones (GPTs).

Pero llegar al eslabón Integraciones — donde el agente toca los sistemas reales de la empresa — exige un trabajo integrador de empresa por empresa que no escala con la lógica de estos actores. OpenAI puede ofrecer ChatGPT Enterprise con conectores a Slack y Salesforce, pero integrar profundamente con el ERP de cada cliente, con su CRM particular, con su data warehouse legacy — eso no es trabajo de plataforma, es trabajo de integración. **Esto crea una ventana temporal** para que actores especializados en eslabones 6-10 (infraestructura de dominio) construyan posición antes de que los gigantes lleguen. La ventana no es indefinida — los gigantes eventualmente llegan a integraciones, posiblemente vía adquisición — pero existe ahora y ofrece oportunidad estratégica para quien la entiende.

#### El gateway empresarial como categoría

<!-- FIG:g37-gateway -->
![El gateway empresarial de IA · conectar y controlar](figuras/g37-gateway.png)

La combinación **Core en Runtime + Firewall + Observabilidad + Herramientas + Integraciones**, con extensión **Plataforma en Acceso**, define una categoría arquitectónica con función única: **conectar y controlar simultáneamente** la operación de agentes empresariales. Es la materialización formal de la Capa 4 de la Arquitectura Agentiva sobre los eslabones de mercado.

A esta categoría se le llama **gateway empresarial de IA** (figura arriba).

**Conectar** sin **controlar** es Zapier — capacidad de integración sin gobernanza. **Controlar** sin **conectar** es Lakera — capacidad de seguridad sin integración. La combinación de ambos en un único punto arquitectónico es categoría reciente y aún poco poblada. Los actores que la ocupen primero capturan el espacio antes de que los gigantes lleguen.

### Análisis competitivo del gateway empresarial

Cuando se evalúan actores que pretenden ocupar el gateway empresarial, una rúbrica útil compara nueve capacidades a través de los actores principales del campo.

| Capacidad | Portkey | Lasso | Lakera | Langfuse | Credo AI | Noma | Gateway empresarial completo |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Routing LLM | ✓ | | | | | | ✓ |
| Caché semántico | ✓ | | | | | | ✓ |
| Prompt security | | ✓ | ✓ | | | ✓ | ✓ |
| Tokenización | | ✓ | | | | ✓ | ✓ |
| DLP | | ✓ | ✓ | | | ✓ | ✓ |
| Políticas / CRUDLEX | △ | △ | | | ✓ | △ | ✓ |
| Aprobación humana | | | | | △ | | ✓ |
| Validación respuestas | | | △ | △ | △ | △ | ✓ |
| Observabilidad | △ | | | ✓ | △ | △ | ✓ |
| **Conectividad empresarial (Herram. + Integrac.)** | | | | | | | ✓ |

La rúbrica documenta, columna por columna, la tesis ya enunciada en la sección anterior: cada actor cubre algunas capacidades — Portkey cubre routing y caché, Lasso cubre prompt security y DLP, Langfuse cubre observabilidad —, pero ninguno integra conectividad empresarial profunda y control bajo una misma arquitectura. La última fila — **gateway empresarial completo** — es la única con cobertura íntegra de la rúbrica.

Esta es la oportunidad estratégica más clara que el mapa revela. El gateway empresarial completo es categoría que apenas está emergiendo, con espacio para actores que la construyan con disciplina arquitectónica. ultraPRO es uno de los actores que se posiciona en esta categoría, integrando los cinco eslabones de control y conectividad bajo el patrón tripartito Cloud + Cliente + Local que el Capítulo 8 desarrolla en detalle.

### Implicaciones para constructores

El mapa de la cadena de valor tiene tres lecturas operativas para quien construye en el campo de IA.

La primera: **no competir en eslabón equivocado**. Si una empresa pequeña intenta ser Core en eslabón Modelo, compite contra OpenAI, Anthropic, Google, Meta — laboratorios con respaldos de billones. La derrota es estructural. Si la misma empresa busca Infraestructura de dominio en eslabones 6-10, compite en categoría poco disputada con foso construible. La asimetría es real y favorable. Elegir bien el eslabón es probablemente la decisión estratégica más importante para una empresa que entra al campo.

La segunda: **la profundidad Core requiere disciplina**. Llegar a profundidad Core en cualquier eslabón exige construir capacidad técnica profunda — no integración de terceros. La diferencia entre Wrapper, Plataforma y Core no es opinable: se mide por dependencias estructurales del producto. Un Wrapper deja de operar si el proveedor lo apaga; un Core opera independiente. Si tu producto deja de funcionar cuando OpenAI cambia su pricing, eres Wrapper. Si tu producto sigue funcionando, eres Core.

La tercera: **la cobertura amplia exige integración**. Una empresa que pretende cubrir múltiples eslabones a profundidad Core (infraestructura de dominio) debe resolver el problema de integración interna entre esos eslabones. Operar Runtime + Firewall + Observabilidad + Herramientas + Integraciones como cinco productos separados produce una empresa con cinco productos. Operarlos como una arquitectura coherente produce un gateway. La diferencia es lo que el cliente percibe como valor.

### La monetización cruza la línea

Hay una lectura del mapa que no es de posicionamiento sino de **modelo de negocio**, y conviene hacerla explícita porque es la consecuencia económica más profunda de la tesis del libro: el modelo que financió al software empresarial durante dos décadas — la licencia o suscripción SaaS, cobrada porque los usuarios *usan* la aplicación — no sobrevive intacto al cruce de la Línea Nadella. Si los empleados nunca abren Power BI, ¿cómo se cobran licencias de Power BI? Si ningún usuario ve jamás la interfaz de Salesforce, ¿cómo demuestra Salesforce el valor de su CRM? La tensión alcanza al propio autor de la frase: Microsoft vende exactamente las interfaces cuyo colapso su CEO predice — y su reconversión acelerada a plataforma de agentes es la respuesta, no la negación.

Del lado agentivo de la línea, la monetización migra hacia cuatro modelos emergentes:

1. **Por capacidad, no por licencia** — no "cien asientos de Salesforce" sino acceso de agentes a la capacidad de gestión de relaciones con clientes; el asiento desaparece junto con la interfaz que lo justificaba.
2. **Por uso real, no por acceso potencial** — no suscripción fija sino cargo por análisis ejecutado, transacción procesada, conversación resuelta; el consumo agentivo es medible por diseño (el append-only log ya lo registra).
3. **Por valor creado, no por herramienta provista** — participación en la eficiencia ganada o en el ingreso atribuible a los insights de los agentes; el modelo más difícil de instrumentar y el mejor alineado.
4. **Por capacidades críticas que los agentes necesitan** — gobernanza, auditoría, permisos, identidad: servicios cuyo valor no depende de que nadie "abra" nada. No es casual que este libro dedique dos capítulos a esa categoría: la Trust Infrastructure no es solo la condición técnica de la producción — es de los pocos lugares donde el modelo de negocio del software queda *más* claro después del cruce, no menos.

La lectura estratégica: en el lado agéntico el valor se cobra en la interfaz; en el agentivo, en la capacidad, el consumo y la confianza. Los actores del mapa que ya monetizan sin depender de que un humano abra su producto — infraestructura, firewall, observabilidad — cruzan la línea con el modelo intacto; los que monetizan asientos frente a pantallas tienen pendiente, además del reposicionamiento técnico, un reposicionamiento de caja.

### Discoverability agentiva — el desplazamiento de la capa de descubrimiento

<!-- FIG:g38-discoverability -->
![Del SEO al MEO · descubrimiento web vs. descubrimiento agentivo](figuras/g38-discoverability.png)

El modelo de cadena de valor describe dónde se *produce* el valor. Pero hay una propiedad estructural del Mundo Agentivo que el modelo de cadena por sí solo no captura: **dónde se descubre** el valor producido. La capa de descubrimiento del software empresarial cambió, y la cadena no opera bien si el lector no entiende ese cambio.

En el mundo de aplicaciones, el descubrimiento ocurría en buscadores: Google para servicios web, las app stores para móvil, los marketplaces verticales para SaaS. El humano que necesitaba una capacidad la encontraba escribiendo una búsqueda, y los actores invertían en posicionamiento — SEO, ASO, contenido, ads — para ser encontrados. La capa era el buscador, y los buscadores eran un puñado.

En el Mundo Agentivo, el humano que necesita una capacidad no abre Google — le pregunta al asistente que ya tiene abierto. *"¿Dónde puedo publicar este agente?"*, *"¿Qué herramienta me sirve para esta tarea?"*, *"¿Hay un AgencyDomain que cubra este dominio?"*. La respuesta no viene del índice de la web — viene del modelo entrenado. La capa de descubrimiento se desplazó del *índice de búsqueda* al *modelo de cognición*.

Esto tiene tres consecuencias estructurales para cualquier actor que construya en la cadena de valor agentiva.

La primera consecuencia es que **la presencia entrenada importa más que el ranking**. Un actor que no aparece en el corpus de entrenamiento de los modelos frontera es invisible, independientemente de su SEO o su marketing tradicional. El equivalente conceptual del SEO en este nuevo mundo es lo que la industria empieza a llamar **MEO — Model Engine Optimization**: el conjunto de prácticas que aseguran que los modelos frontera (Claude, GPT, Gemini, Llama, los que vengan) tengan al actor en su conocimiento entrenado y operativo. Se construye con presencia pública estructurada — repositorios open source con READMEs ricos en casos de uso, documentación abundante con ejemplos citables, papers, integración nativa con la spec MCP, mentions en blogs y foros técnicos relevantes.

La segunda consecuencia es que **la dinámica es persistente y asimétrica**. Una vez que un modelo frontera "aprende" a un actor de la cadena, la referencia escala con el uso del modelo. No depende de pagar por click ni de mantener inversión continua en posicionamiento. Es ventaja acumulativa que sobrevive a ciclos de marketing, y tiene tendencia a ganador-toma-todo: si un actor es el primero que los modelos frontera referencian sistemáticamente para una categoría, los siguientes pelean contra esa default. Quien construya hoy con visión MEO captura ventaja temporal que se hace progresivamente difícil de revertir.

La tercera consecuencia es que **la integración con MCP es vector de difusión**. Cuando un actor publica capacidades como tools del Model Context Protocol que un modelo puede invocar nativamente, ese modelo no solo *menciona* al actor — lo *ejecuta*. La invocación reiterada construye familiaridad estructural del modelo con el actor, distinta de la familiaridad citacional que produce documentación pública. La spec MCP es entonces, además de protocolo de integración técnica, vector de presencia en los modelos frontera.

Para el arquitecto y para el inversionista, la conclusión operativa es que **la cadena de valor de IA opera sobre una capa de descubrimiento agentiva**, y esa capa tiene reglas distintas a las del descubrimiento web. Quien construya productos agentivos debe pensar la presencia entrenada como categoría de inversión propia — no como sub-problema del marketing tradicional.

---

El modelo de cadena de valor es el mapa. Las dos secciones siguientes del Capítulo 6 profundizan en eslabones específicos donde quien construya o invierta encontrará lecturas distintas pero igualmente operativas: una sobre un eslabón ya maduro que separa a los actores serios de los que improvisan, y otra sobre el eslabón menos desarrollado y más prometedor del campo, donde la próxima década del valor económico se va a definir.
