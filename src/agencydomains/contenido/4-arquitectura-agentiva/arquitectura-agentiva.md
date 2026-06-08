# Capítulo 4 · Arquitectura Agentiva

Los Capítulos 1 y 2 establecieron el paradigma; el Capítulo 3 cartografió el estado pre-agentivo desde el cual la mayoría de las organizaciones cruzarán la línea, e identificó qué celdas de ese estado migran y cómo. Este capítulo entrega la respuesta arquitectónica del lado al que se cruza. Lo que sigue es la **Arquitectura Agentiva** — el diseño técnico canónico de un sistema construido para vivir del lado correcto de la línea.

La pregunta operativa que la arquitectura responde es concreta: ¿cómo se construye un sistema en el que un agente pueda razonar, persistir, actuar sobre el mundo real, y rendir cuentas de lo que hace — sin que esas cuatro funciones se mezclen en un magma indistinguible? La pregunta no es retórica. La mezcla — fundir cognición, autonomía, acción y gobernanza en una sola superficie indiferenciada — es exactamente lo que produce los pilotos que funcionan en demo y mueren al pasar a producción enterprise. Es el patrón recurrente detrás del cuarenta por ciento de proyectos cancelados que documentamos en el Capítulo 2. La causa raíz de ese fracaso no es técnica en el sentido de que falten algoritmos o capacidad de cómputo: es **arquitectónica**. Los sistemas no separan responsabilidades, y sin separación de responsabilidades no hay manera de razonar disciplinadamente sobre lo que hacen.

La respuesta que este libro propone es **separación de responsabilidades en cuatro capas, organizadas en topología paralela**, gobernadas por una infraestructura de confianza transversal y ordenadas por un principio rector que llamaremos *Agent First*. Las cuatro capas no son división arbitraria — cada una corresponde a una responsabilidad arquitectónica distinta que puede razonarse, especificarse e implementarse independientemente. La infraestructura transversal no es capa adicional, es propiedad que atraviesa las cuatro. Y el principio rector no es slogan: es regla operativa de diseño que ordena cómo se resuelve cualquier disyuntiva.

La precisión sobre **topología paralela** importa desde la primera lectura. La numeración de las capas (1 → 2 → 3 → 4) sugiere una secuencia, pero la operación real del sistema no es lineal. Las Capas 2 (Cognición) y 3 (Autonomía) son **vías paralelas** entre la Capa 1 (Interacción) y la Capa 4 (Acceso), no etapas en serie. Una operación que entra por Capa 1 puede llegar a Capa 4 atravesando la Cognición — costosa y decisiva — o atravesando la Autonomía — barata y repetitiva, vía Botlets. Las dos vías interactúan entre sí pero ninguna domina sobre la otra. La sección "La topología paralela" desarrolla las consecuencias.

La urgencia del trabajo no es teórica. Bain & Company identifica la ausencia de fundamentos arquitectónicos compartidos como la causa raíz del estancamiento entre proyectos piloto y operación productiva. Solo el veintiuno por ciento de las organizaciones tiene gobernanza madura sobre los agentes que opera. La industria carece — todavía — de una arquitectura formal compartida que permita razonar sobre estos sistemas con la disciplina con la que se razona sobre arquitecturas distribuidas, sistemas operativos o redes. Este capítulo propone esa arquitectura, no como verdad revelada sino como **punto de partida razonado** que cualquier organización o producto puede adoptar, criticar, extender o reemplazar.

> **Aclaración necesaria antes de entrar al detalle.** Las cuatro capas que este capítulo desarrolla son una **radiografía del agente individual** — los cuatro comportamientos que todo agente debe exhibir, sea que se materialicen en un solo bloque monolítico o se distribuyan entre componentes cooperantes. **No son eslabones de una cadena de valor industrial**, ni slots donde se asigne un producto del mercado a cada uno. La cadena de valor industrial — quiénes participan en la economía agentiva y dónde se posiciona cada actor — la desarrolla el Capítulo 6. Las dos lentes son verdaderas y se cruzan limpiamente cuando se mantienen separadas: la radiografía describe al agente; la cadena describe al ecosistema en el que el agente opera. Confundirlas produce errores de razonamiento típicos al hablar del portafolio de productos en mercado — por ejemplo, asumir que cada capa "le toca" a un producto en particular.

## Las cuatro capas, vistas en conjunto

<!-- FIG:g10-cuatro-capas -->
![Las cuatro capas + Trust Infrastructure transversal](figuras/g10-cuatro-capas.png)

Las cuatro capas de la Arquitectura Agentiva se nombran **Interacción, Cognición, Autonomía y Acceso**. La numeración tiene valor didáctico — Capa 1 es la superficie con la que el humano se encuentra, Capa 4 es el punto donde el sistema toca al mundo real — pero **no describe el orden en que las operaciones atraviesan el sistema**. La Capa 1 es donde el humano (o el agente externo) se comunica con el sistema; la Capa 2 es donde el sistema piensa; la Capa 3 es donde el sistema vive y persiste; la Capa 4 es donde el sistema actúa. Las Capas 2 y 3 son vías paralelas, no etapas en serie — la sección siguiente lo desarrolla.

La separación importa porque cada capa resuelve un problema distinto, exige propiedades distintas, falla por razones distintas, y se evoluciona en ritmos distintos. Un sistema bien arquitecturado puede mejorar su Capa 1 — agregar nuevos canales de interacción — sin tocar las otras tres. Puede cambiar su proveedor de Capa 2 — pasar de un modelo a otro — sin reescribir su Capa 4. Puede fortalecer su Capa 3 — agregar persistencia o monitoreo continuo — sin que el humano de la Capa 1 vea cambios. Esta independencia entre capas no es elegancia abstracta: es lo que permite que el sistema evolucione durante años sin reescritura completa, que es exactamente lo que un sistema en producción necesita para sobrevivir más allá del primer año.

> *La separación de responsabilidades es condición necesaria para poder operar agentes con confianza.*

Cada capa es una **responsabilidad arquitectónica**, no un atributo. La distinción importa: un sistema que mezcla cognición y acción en una sola superficie no tiene una "capa fundida" — tiene una violación arquitectónica que se paga al pasar a producción. La diferencia entre violación arquitectónica y "decisión simplificadora" es práctica: en piloto controlado, la fusión funciona porque el volumen de operación es bajo y el humano supervisa de cerca; en producción enterprise, la fusión hace imposible diagnosticar fallos, gobernar políticas, escalar volumen o cambiar componentes individuales. El sistema deja de ser explicable, y un sistema que el equipo no puede explicar es un sistema que la organización no puede operar.

A continuación, antes de desarrollar cada capa, formalizamos el modelo topológico que las relaciona. Después de eso presentamos cada capa con el detalle que su rol exige, la infraestructura transversal — Trust Infrastructure — y el principio rector que ordena el diseño. Al cerrar el capítulo describimos la frontera de evolución, esos vectores donde la arquitectura admite extensión que aún no ha cuajado como spec normativa.

## La topología paralela

El diagrama mental con el que la mayoría de los lectores entran al modelo de cuatro capas es el de pila lineal: el humano interactúa con Capa 1, Capa 1 invoca Capa 2, Capa 2 produce un plan, Capa 3 lo ejecuta persistentemente, Capa 4 toca el mundo. Esa lectura es errada y produce errores de diseño concretos. La topología real es **paralela**: las Capas 2 y 3 son **vías alternas** entre Capa 1 y Capa 4, no etapas secuenciales. Una operación atraviesa el AgencyDomain por una de las dos vías — o por ambas en distintos tramos — pero nunca por las dos en serie obligatoria.

Cada vía tiene un régimen propio. La **vía Cognición** es lenta, costosa y decisiva — funciona bien para conversación, decisiones nuevas, casos no anticipados, situaciones donde el humano necesita interlocución razonada y el sistema necesita combinar Capabilities en patrones nuevos. La **vía Autonomía** es rápida, barata y repetitiva — funciona bien para ejecución de Botlets sobre patrones estables, donde la cognición ya consolidó el saber operativo en código tradicional que se ejecuta sin invocar el modelo. La economía de operación del AgencyDomain depende de la mezcla: cuanta más operación fluye por la vía 3, más bajo el costo unitario; cuanta más fluye por la vía 2, mayor capacidad de adaptación a casos nuevos.

Las dos vías no operan en aislamiento. Tres patrones de interacción cruzan entre ellas y los desarrollamos en su capítulo correspondiente, pero conviene nombrarlos aquí para que el modelo topológico quede completo. Primero, la Cognición **delega a Botlet** (`2 → 3`): cuando Pattern Recognition detecta una operación repetitiva, la cognición genera un Botlet que ejecutará el patrón en adelante sin invocarla. Segundo, el Botlet **escala fallback a Cognición** (`3 → 2`): cuando el ambiente cambia y el Botlet falla, la cognición rescata la operación, regenera el Botlet con la variante incorporada, y devuelve la ejecución a la vía 3. Tercero, la Cognición **observa el log de Botlets** (`2 ← 3`): el Botlet emite eventos y métricas que la cognición consulta cuando el humano pregunta o cuando necesita razonar sobre el comportamiento del sistema en su conjunto.

La topología paralela tiene cinco consecuencias prácticas que conviene retener. La **primera** es que el modo offline de un nodo edge — un local físico sin red — es trivial de explicar bajo este modelo: la vía Cognición depende típicamente de cloud y queda inactiva sin red; la vía Autonomía local sigue activa porque sus Botlets corren en el edge contra una BD local y Capabilities locales. La operación atraviesa el AgencyDomain por la vía que sigue viva. Lo que sin topología paralela parecería exigir un sistema separado, bajo ella emerge como propiedad estructural.

La **segunda** es que la economía cognitiva queda evidente. La organización no paga por "el AgencyDomain" — paga por la mezcla de vías que su operación dispara. Las decisiones de qué patrones consolidar en Botlets son decisiones económicas explícitas, no detalle de implementación.

La **tercera** es que **Trust Infrastructure se ejerce en ambas vías**, no solo en la que pasa por la Cognición. El modelo lineal podía sugerir que la cognición filtra todo lo que llega a Capa 4. El modelo paralelo deja claro que la vía 3 también atraviesa Trust — las políticas se aplican antes de invocar Capa 4 sin importar de qué vía viene la invocación. Un Botlet que invoca DTE-SII pasa por las mismas validaciones de Trust que la cognición que lo haría.

La **cuarta** es que la topología paralela distingue dos tipos de Botlets que el modelo lineal confundía. Los **Botlets de fachada operativa** son invocables desde Capa 1 — un botón en un POS, una línea de comando, un endpoint — con contrato estable e identidad humana propagada hacia Capa 4. Los **Botlets de herramienta interna de la cognición** son invocables solo desde Capa 2 — la cognición los compone en planes que ella misma ejecuta. Ambos viven en Capa 3, pero su superficie de invocación es distinta y sus propiedades de gobierno también.

La **quinta** es que el camino `Capa 1 → Capa 3 → Capa 4` deja de ser excepción y pasa a ser **vía canónica**. Una superficie especializada — un POS de sala, una pantalla de cocina, un dashboard de caja, un panel de operación industrial — que invoca un Botlet senior y produce una acción en Capa 4 atraviesa esta vía sin tocar Capa 2. Bajo el modelo lineal, eso parecía bypass de la cognición, decisión local con caveat. Bajo la topología paralela, es **una de las dos vías estructurales del AgencyDomain**, perfectamente legítima, con sus propias propiedades de Trust y observabilidad.

## Los tres tiempos del agente

<!-- FIG:g11-tres-tiempos -->
![Los tres tiempos del agente · Preparación · Atención · Ingeniería](figuras/g11-tres-tiempos.png)

La topología paralela describe **dónde** vive cada operación dentro del AgencyDomain. Esta sección describe **cuándo** opera el agente — la dimensión temporal que la topología por sí sola no captura. Sin esta segunda lectura, los planes de capacidad confunden la actividad de fondo con la actividad en línea, y el agente queda mal dimensionado: o se le pide servicio continuo sin ventanas para mantenerse capaz, o se le reserva tanto tiempo de mantenimiento que la operación efectiva sufre.

La spec reconoce **tres tiempos canónicos** del agente. Los tres son actividades reales y simultáneas en un sistema productivo; difieren en su régimen, su urgencia y su economía cognitiva.

### Preparación

La Preparación es el tiempo en que el agente **crea y mejora sus capacidades fuera de la ventana de servicio**. Refina su catálogo, mejora sus capacidades cognitivas, estudia el ambiente, regenera Botlets que detectaron drift, incorpora variantes nuevas, entrena Pattern Recognition con tráfico observado, ajusta Capabilities a partir de retroalimentación del campo. Es el *mise en place* del agente — el trabajo que sostiene la calidad del servicio sin ser visible para el usuario.

La Preparación opera predominantemente en la vía Cognición (Capa 2) sobre datos consolidados, no sobre la ráfaga del momento. Es típicamente **batch / off-peak**: corre cuando la operación efectiva no exige toda la cognición disponible, o en infraestructura cognitiva separada. Sus métricas son de calidad — qué tan bueno es el catálogo, qué tan precisos son los Botlets recientes, qué tan completas son las Capabilities.

### Atención

La Atención es el tiempo en que el agente **interactúa con usuarios o eventos en tiempo real**. Capa 1 activa, conversación viva, ejecución de Botlets que sostienen operación, escalamientos cuando corresponde. Es el camino crítico — donde la organización siente al agente, donde el SLA importa, donde el costo del error se materializa.

La Atención opera por las dos vías (Cognición y Autonomía) según el patrón, prioritariamente, con latencia acotada y disponibilidad alta. Sus métricas son operativas — satisfacción del usuario, latencia de respuesta, tasa de resolución sin escalamiento, tiempo medio entre escalamientos.

### Ingeniería

La Ingeniería es el puente entre Preparación y Atención: el tiempo en que el agente **convierte capacidad latente en capacidad ejecutable para un caso concreto**. Recibe una solicitud, identifica qué Capabilities aplican, configura un Botlet seed para el contexto específico, valida su ejecución sobre datos reales, lo deploya al ambiente correspondiente, observa el resultado. Es trabajo de configuración y orquestación, no de razonamiento general ni de servicio puro.

La Ingeniería opera en una mezcla de vías: usa la cognición para decidir composición pero genera artefactos que persisten en Autonomía. Es típicamente **mediano plazo** — minutos a horas, no segundos — y tiene su propio ritmo distinto del ritmo de la Atención. Sus métricas son de cobertura — qué fracción de las solicitudes se logra atender con Botlets seed configurados, qué tasa de éxito tienen al primer deploy, cuántas iteraciones promedio requieren.

### Implicaciones para razonar sobre el sistema

La distinción entre los tres tiempos tiene tres consecuencias prácticas para la operación del AgencyDomain.

**Primera, scheduling de capacidad cognitiva.** La cognición es recurso costoso y finito. La organización elige consciente cuánto se asigna a cada tiempo: la Atención exige latencia acotada y prioridad alta; la Preparación tolera batch y aprovecha valles de demanda; la Ingeniería ocupa una franja intermedia. Sin esta distinción, la cognición se asigna por proximidad temporal a la solicitud y la Preparación queda relegada — el agente deja de mejorarse, su catálogo envejece.

**Segunda, métricas distintas por tiempo.** Un solo dashboard de "performance del agente" miente: la Preparación se mide por calidad agregada del catálogo y la Atención se mide por satisfacción operativa. Mezclarlas oculta dónde está el problema cuando algo va mal. La organización madura instrumenta los tres tiempos por separado.

**Tercera, modelo de disponibilidad.** Un agente bien operado **no está 100% en Atención**. Necesita ventanas de Preparación. La promesa "agente siempre disponible" se entiende mejor como "Atención siempre disponible" — la Preparación opera detrás. Esta distinción es la que permite ofrecer SLAs de servicio sin canibalizar el trabajo de fondo que sostiene la calidad.

> *El agente no atiende en todo momento — pero puede atender en cualquier momento porque dedica tiempo a prepararse.*

### Propiedades exigidas

| Propiedad | Nivel |
|---|---|
| Reconocimiento explícito de los tres tiempos en la operación | **MUST** |
| Métricas separadas por tiempo (Preparación, Atención, Ingeniería) | **MUST** |
| Ventanas de Preparación reservadas, no opcionales | **SHOULD** |
| Scheduling de capacidad cognitiva por prioridad de tiempo | **SHOULD** |
| Trazabilidad de qué tiempo ejecutó qué operación en el log | **SHOULD** |

## Capa 1 — Interacción

La Capa 1 es la responsable de toda comunicación entre humanos y el sistema. Es interfaz pura, sin lógica de negocio. El humano que interactúa con un sistema agentivo nunca toca directamente las otras tres capas — solo ve la Capa 1, y la Capa 1 traduce sus intenciones hacia las capas que ejecutan. Suena simple cuando se enuncia así, pero el diseño de la Capa 1 contiene casi todas las decisiones que determinan si el humano va a usar el sistema con frecuencia o lo va a abandonar después de la primera semana.

Las modalidades canónicas de la Capa 1 son seis, y un sistema agentivo serio típicamente soporta más de una. La modalidad **conversacional textual** — chat directo con el agente — es la más visible y la que la mayoría de los productos comerciales contemporáneos implementan primero. Es modalidad eficiente para tareas analíticas o de redacción, donde el humano formula bien sus solicitudes. La modalidad **conversacional por voz** — asistentes virtuales, llamadas, audio-bots — es crítica para casos de uso donde el humano tiene las manos ocupadas o necesita interactuar mientras se mueve. Los **canales corporativos** — Slack, Teams, WhatsApp, email — funcionan como superficies de conversación cuando el humano no quiere abrir una aplicación específica para hablar con el agente, sino que prefiere que el agente aparezca donde el humano ya está. La **API programática** habilita que sistemas externos invoquen al agente sin intermediación humana — patrón crítico para casos donde el agente es invocado por otro sistema, no por una persona.

Las dos modalidades menos discutidas, pero estructuralmente importantes, son la **GUI generada** y la **señalética pasiva**. La señalética pasiva son superficies que comunican información de manera continua sin requerir interacción del humano — paneles, dashboards de operación, displays ambientes. El humano no opera: lee. Esta modalidad es central para casos de uso operacionales donde el agente debe mantener informado al humano sin esperar que el humano consulte. La GUI generada merece tratamiento extendido porque es donde más fácilmente se confunde la lectura del paradigma agentivo. La sección que sigue lo desarrolla.

### Tres regímenes de GUI en la Capa 1 agentiva

Una lectura recurrente — y errada — del paradigma agentivo concluye que el Mundo Agentivo implica abandonar toda interfaz gráfica: si todo es conversación con el agente, las GUIs desaparecen. Esa lectura confunde dos cosas distintas. Lo que desaparece **no es la GUI** — es la GUI **precreada por equipos humanos en tiempos pre-agentivos**. La GUI sigue existiendo cuando la operación lo requiere; lo que cambia es **su modo de existencia**: pasa de ser plantilla fija codificada antes del uso a ser **superficie generada por la cognición** según las necesidades de cada interacción.

La Capa 1 productiva del Mundo Agentivo distingue **tres regímenes de generación**:

**1. Conversacional puro.** El agente responde en texto o voz; suficiente cuando la información es secuencial y la decisión es flexible. Un cliente que pregunta por su saldo, un usuario que pide redactar un email, un operador que consulta el estado de un proceso — todos casos donde la conversación es la modalidad correcta. No hay superficie gráfica generada porque no hace falta.

**2. GUI generada on-the-fly.** El agente compone una superficie gráfica adaptada a la tarea inmediata: una vista, un formulario, un panel, un dashboard. La GUI vive lo que dura la tarea; la próxima vez que el humano necesite algo similar, el agente puede regenerarla distinta según el contexto. Es la modalidad correcta cuando la información es densa o multidimensional, cuando la decisión exige comparación visual, o cuando el humano debe manipular varios elementos simultáneamente. Es lo que suele entenderse como "GUI dinámica".

**3. GUI persistente generada como Botlet.** Para roles operativos repetitivos — un cajero en hora punta, un panel de cocina, un dashboard de caja, una pantalla de monitoreo industrial — el agente genera una superficie estable y la consolida como **Botlet de Capa 1**. Es GUI generada que persiste porque el patrón de uso es estable, el rol operativo es claro, y la velocidad de respuesta es crítica. Sigue siendo agentiva: el agente puede regenerarla cuando el ambiente cambia (nuevos productos, nuevas reglas, nuevo flujo), exactamente como cualquier Botlet de Capa 3 se regenera cuando su ambiente cambia. La diferencia con la GUI tradicional es que **ningún equipo humano de UI/UX la diseñó**: la cognición la generó porque el patrón de uso lo justifica.

Las tres modalidades coexisten en un sistema agentivo maduro. La distinción entre ellas no es jerárquica — no es que la GUI persistente sea "mejor" que la conversacional. Es **adecuación al patrón de uso**: conversación cuando el caso es nuevo o flexible, GUI on-the-fly cuando la tarea es densa pero ocasional, GUI persistente cuando el rol es operativo y repetitivo.

> *La GUI no desaparece en el Mundo Agentivo. Lo que desaparece es la GUI precreada. Toda GUI en una Capa 1 agentiva es generada por la cognición — algunas efímeras, otras estabilizadas como Botlets de fachada.*

La consecuencia práctica de la distinción es operativa. Sin ella, "agentivo" se interpreta como "todo es chat" — operacionalmente impráctico para roles que necesitan velocidad. Un cajero en hora punta no conversa para cobrar; un cocinero no chatea con el sistema de comandas; un operador de planta no le pide al agente por voz que le muestre el estado del proceso. Con la distinción, esos roles operan sobre **GUIs persistentes generadas como Botlets de fachada** — superficies estables, rápidas, especializadas, que invocan Botlets de Capa 3 directamente (la vía `Capa 1 → Capa 3 → Capa 4` que la sección de topología paralela formaliza). El sistema sigue siendo enteramente agentivo; lo que cambia es que la cognición no participa en cada interacción operativa — sí en la generación inicial de la fachada, sí cuando la fachada necesita regenerarse, sí cuando el operador escala una situación nueva.

Los **Botlets de fachada** se conectan naturalmente con la distinción seed/emergente del Capítulo 5 §2: las GUIs persistentes son típicamente **Botlets seed de Capa 1** — generados por la cognición a pedido del equipo de diseño como parte del producto inicial, en línea con cómo se generan los Botlets transaccionales seed en Capa 3.

### Composición de la superficie · shell, vista, operación

<!-- FIG:g12-composicion-capa1 -->
![Composición de la Capa 1 · shell · vista · operación](figuras/g12-composicion-capa1.png)

Una superficie no trivial **no es un Botlet monolítico**. Es composición. Leerla así vuelve explícito qué se reutiliza, qué es específico y dónde vive cada pieza dentro de la arquitectura; tratarla como bloque único condena el diseño de la Capa 1 productiva a la intuición y desperdicia la reutilización entre superficies.

La spec reconoce **tres roles canónicos** que componen una superficie:

**Botlet de superficie (shell)** — Capa 1. Es el **contenedor**: layout, navegación entre vistas, ciclo de vida de la sesión, estado compartido. Lo específico de cada producto. Hay típicamente un shell por rol operativo principal — el shell del POS de sala, el shell del panel de caja, el shell del dashboard ejecutivo móvil. El shell es lo menos reutilizable: encapsula identidad de producto.

**Botlet de vista** — Capa 1. Una **pantalla o panel** dentro de la superficie. Una superficie tiene una o varias vistas; las que se usan en varios shells se extraen como Botlets propios. La vista de "carrito de compra", la vista de "detalle de pedido", la vista de "resumen de turno". Las vistas son **altamente reutilizables** — la misma vista de "detalle de pedido" puede aparecer dentro del shell de POS y dentro del shell de panel de caja.

**Botlet de operación** — Capa 3. La **ejecución de negocio** que la vista invoca. Vive en Autonomía, no en Interacción. *"Cobrar mesa", "imprimir comanda", "cerrar turno", "consolidar inventario"* — son operaciones en Capa 3, no superficies en Capa 1. Una operación puede ser invocada desde múltiples vistas dentro de múltiples shells. Las operaciones son **el activo más reutilizable** del catálogo.

La distinción clave: **shell y vista son superficie (Capa 1); operación es ejecución (Capa 3)**. Una superficie es composición de Botlets de Capa 1 que orquestan e invocan Botlets de Capa 3.

**Catálogo emergente.** Esta descomposición es **prerequisito para razonar sobre el catálogo de piezas reusables**: las operaciones se acumulan en el catálogo a lo largo del tiempo y forman el activo arquitectónico más durable; las vistas reutilizables se extraen y catalogan; los shells permanecen específicos pero su construcción se acelera porque ensamblan piezas existentes. Sin la descomposición explícita, todo se trata como "feature de aplicación" y no se aprovecha la reutilización.

**Producto de Información multi-vista · drill-through.** Un **Producto de Información (`PI`)** — la manifestación que deja un Botlet de operación informativa al consumirse — no es necesariamente una pieza única. Puede componerse de **N piezas nombradas**: cada **vista** es una pieza más del mismo `PI`, elegible desde un selector, con una vista por defecto (la primera). El `PI` sigue siendo **authz-blind** — ni las vistas ni las aristas que las conectan declaran autorización; esa política vive en el policy store, no en la composición.

La conexión entre vistas es el **drill-through**: una **arista de navegación con contexto**. Una tabla declara *"al clickear una fila, ir a la vista destino pasando la clave de esa fila"*; la vista destino se renderiza **filtrada por esa clave**. La propiedad crítica es **data-anchored / no-bypass**: el contexto que viaja con la arista **acota dentro de lo que el viewer ya puede ver** — la vista destino aplica su propia política de filas (`RLS`) sobre la fuente, y el contexto entra como filtro adicional, nunca como override de la política (**MUST**). El drill **acota, nunca amplía** — intersección con lo autorizado, jamás unión. Si el viewer no alcanza la fila origen, no llega a la arista; si llega, el destino sigue gobernado por su propia política.

Un reporte de cartera / aging de saldos ilustra el patrón: vistas nombradas (Clientes, Proveedores, Relacionados, Detalle) sobre el mismo `PI`, una tabla jerárquica Empresa→Socio, y una arista de drill-through Socio→Detalle que abre los documentos de ese socio — filtrados por la clave del socio y acotados a lo que el viewer ya tenía derecho a ver. La composición multi-vista es ortogonal a la familia del Botlet de operación: lo que cambia es cuántas piezas componen la manifestación, no su naturaleza. La descripción canónica del `PI` como manifestación de la familia de información vive en el Capítulo 7.

<!-- FIG:g13-pi-multivista-drillthrough -->
![PI multi-vista y drill-through — navegación con contexto, data-anchored](figuras/g13-pi-multivista-drillthrough.png)

### Faceta · primitiva atómica de la Capa 1

<!-- FIG:g14-faceta-vs-botlet -->
![Faceta vs Botlet · dos primitivas, dos capas, dos naturalezas](figuras/g14-faceta-vs-botlet.png)

Hasta aquí la Capa 1 se ha descrito en términos de regímenes de generación (conversacional puro, on-the-fly, persistente como Botlet) y composición (shell, vista, operación). Falta nombrar la **unidad atómica** con la que estas superficies se construyen — la pieza que la vista pone en la pantalla, el componente que la cognición invoca durante una conversación, el instrumento que el agente toma cuando decide que la información se obtiene mejor visualmente que verbalmente.

Esa unidad es la **Faceta**.

**Definición canónica.** Una **Faceta** es un componente atómico reusable de la Capa 1 — una pizarra de dibujo a mano alzada, un catálogo-selector, una matriz de colores, un calendario, un mapa clickeable, un slider, un ordenamiento drag-and-drop. Una de las muchas caras que la interacción con el usuario puede tomar en un momento dado. Es **instrumento**, no proceso. Vive y opera en la Capa 1.

**La Faceta no es un Botlet.** Esta es la distinción más importante de la sección. Las dos primitivas se confunden fácil porque ambas son "pieza de software canónica con identidad propia", pero su naturaleza es radicalmente distinta:

| Eje | **Faceta** | **Botlet** |
|---|---|---|
| Capa | Capa 1 (Interacción) | Capa 3 (Autonomía) |
| Naturaleza | Instrumento de interacción | Memoria muscular del agente |
| Activación | La cognición la invoca durante conversación activa | Ejecuta sin cognición presente |
| Garantía de fallback | NO — si falla, agente vuelve a conversación textual | SÍ — la cognición ejecuta manualmente |
| Ciclo | No tiene ciclo de regeneración | Ciclo `95/4/1` con regeneración |
| Persistencia | Efímera por defecto (vive lo que dura la tarea) | Persistente entre sesiones |
| Estado de fase | No aplica | Junior · en aprendizaje · senior |

El **Botlet es memoria muscular**: el agente consolidó saber repetitivo en código tradicional que ejecuta sin pensar. La **Faceta es instrumento**: el agente la toma mientras piensa, la usa para obtener información del usuario, la suelta cuando termina. El Botlet automatiza; la Faceta interactúa.

**Dos usos canónicos** de la Faceta:

1. **El agente la invoca directamente en conversación** — compone una superficie efímera con una o varias Facetas, el usuario interactúa, la información vuelve, la conversación continúa. La superficie efímera **no es un Botlet** y no persiste. Esto realiza el régimen *GUI generada on-the-fly* descrito antes.

2. **Las superficies estables se componen de Facetas** — los Botlets de presentación (shells y vistas) ensamblan Facetas más lógica de orquestación. La vista de "detalle de pedido" usa internamente la Faceta de "matriz de productos", la Faceta de "calendario", la Faceta de "selector". El Botlet de vista define la orquestación; las Facetas son los instrumentos que el Botlet pone en la pantalla.

**Comportamiento agentivo asociado.** El agente, durante una conversación, **decide** ofrecer una Faceta cuando estima que la información se obtiene más rápido visualmente que verbalmente. Estima el tiempo de verbalización versus el tiempo de uso del instrumento; si el segundo gana, ofrece la Faceta. Heurísticas canónicas:

- Información de **baja dimensionalidad** y bien estructurada → conversación.
- Información de **alta dimensionalidad** o difícil de verbalizar → Faceta.
- Información que el usuario ya tiene en **forma espacial o visual** → Faceta.

El agente hace este cálculo en tiempo real. Es decisión cognitiva del agente, no feature pre-programada del producto. Una Capa 1 productiva sin este comportamiento agentivo activo se queda en chat; con él, abre la totalidad del rango interactivo.

**¿Por qué importa la primitiva?** Nombrar la Faceta convierte el "GUI on-the-fly" —que sin ella queda como capacidad sin estructura— en algo razonable: deja claro cuál es la **unidad mínima** de la Capa 1, cómo se relaciona con los Botlets de presentación (composición), y por qué ofrecer un GUI ad-hoc es agentivo (un acto cognitivo, no una feature). La descripción completa de la Faceta como primitiva canónica vive en el Capítulo 5 §6.

> *Si el humano abre aplicaciones para hacer su trabajo, no estamos en la Capa 1 del Mundo Agentivo.*

La declaración recoge la tesis de Satya Nadella en el podcast BG2 de diciembre 2024, que ya citamos en el Capítulo 1. Es ejercicio operativo de calibración con un matiz adicional bajo los tres regímenes que acabamos de definir: la pregunta no es si hay GUI o no, ni cuán bonita es. La pregunta es **quién la generó**. Si la GUI fue precreada por un equipo de UI/UX en sprints de aplicación tradicional, no es Capa 1 agentiva. Si la GUI fue generada por la cognición — efímera o persistente como Botlet —, sí lo es.

Tres propiedades exigidas distinguen una Capa 1 bien diseñada de una colección de adaptadores ad hoc. Ser **agnóstica al canal** significa que la lógica de la conversación no depende del medio: el mismo agente debe manifestarse coherentemente en chat, voz, GUI on-the-fly, sin que el desarrollador reescriba la lógica para cada canal. Si el agente conoce los datos del cliente y sus preferencias, esa información es la misma sin importar si el cliente está hablando por voz desde su auto o por chat desde su laptop. La **adaptación al registro** exige que el agente comprenda el registro del canal — formal en email corporativo, conciso en chat, verbal en voz — sin que esa adaptación viva en código condicional. Es propiedad de la cognición que se manifiesta a través de la Capa 1, no de la Capa 1 misma. Y la **persistencia de contexto** garantiza que la conversación sobreviva al cambio de canal: un humano que empieza por chat y continúa por voz mantiene el hilo. Sin esta propiedad, el sistema fragmenta la experiencia humana en silos de canal, y el humano percibe al "agente" como múltiples agentes desconectados — exactamente la fricción que el paradigma agentivo promete eliminar.

## Capa 2 — Cognición

La Capa 2 es donde el sistema piensa. Es el cerebro del agente — interpretación, razonamiento, planificación, aplicación de saber especializado, decisión de delegar. Si la Capa 1 es la cara del agente, la Capa 2 es lo que hay detrás de la cara.

Los componentes canónicos de la Capa 2 son cinco. El primero es **multi-LLM**: la cognición no está atada a un proveedor de modelo único. Diferentes proveedores, modelos, modalidades — texto, multimodal — y arquitecturas — LLM, simbólico, híbrido — coexisten bajo un contrato común. La razón es operativa antes que filosófica: el panorama de proveedores de cognición evoluciona en escalas de meses, y un sistema atado a un proveedor único acumula deuda cada vez que ese proveedor pierde competitividad respecto a un nuevo entrante. Un sistema multi-LLM bien diseñado permite migrar entre proveedores sin reescribir la lógica del agente.

El segundo componente son las **Capabilities** — unidades de saber-hacer modular y composable, organizadas en árbol jerárquico. La cognición selecciona y aplica Capabilities según la tarea. Las Capabilities son el saber profesional codificado — saber contable para un agente financiero, saber regulatorio para un agente legal, saber operativo para un agente de soporte. Las desarrollamos con detalle en el Capítulo 5. Por ahora basta retener que la Capa 2 no opera con conocimiento monolítico — opera seleccionando módulos de saber especializado y combinándolos según el caso.

El tercer componente es **Pattern Recognition** — detección de patrones repetitivos en la actividad del agente. La capacidad está inspirada en arquitectura neurobiológica: corteza perirrinal para familiaridad rápida, hipocampo para recollection detallada, corteza prefrontal para decisión consciente. El mismo patrón funcional descrito por Squire y Wixted en su trabajo sobre el sistema de memoria humano. Cuando el agente reconoce un patrón repetitivo en la actividad — la misma tarea ejecutándose con frecuencia variable pero estructura estable —, dispara la generación de un Botlet que automatiza esa tarea sin requerir cognición adicional cada vez. Pattern Recognition es la entrada al ciclo del Botlet, que desarrollamos en el Capítulo 5.

El cuarto componente es la **generación de Botlets** misma. La cognición decide cuándo delegar tareas repetitivas a la Capa 3 — donde los Botlets se ejecutan sin invocar cognición. Esta decisión no es trivial: una cognición que delega demasiado pierde flexibilidad cuando el ambiente cambia; una cognición que delega muy poco satura sus recursos en tareas que el código tradicional ejecuta mejor. La calibración de cuándo generar Botlet es propiedad emergente de la cognición madura.

El quinto componente es el **Asistente reactivo** — el agente operando en modo respuesta-a-solicitud. Espera input del humano, responde, pasa al siguiente turno. Este modo es Capa 2 pura — cognición sin autonomía, a diferencia del modo proactivo que vive en Capa 3. La distinción Asistente vs Agente Autónomo la desarrolla el Capítulo 5 §5.

La especificación reconoce además **dos modos de acceso a la cognición** que importa nombrar con precisión. El primer modo es **Tokens**: el sistema centraliza credenciales, facturación y políticas para acceder a la cognición. Provee acceso cognitivo a todos sus componentes activos. Este modo aplica cuando los agentes deben operar en background sin intervención del usuario, cuando la organización desea control central sobre consumo y costos, o cuando múltiples agentes comparten un mismo proveedor de cognición. El segundo modo es **Suscripción**: el asistente con el cual el usuario interactúa — Claude, ChatGPT, Copilot, Gemini — accede directamente al recurso cognitivo bajo la suscripción del propio usuario. El sistema agentivo no consume tokens del recurso. Este modo aplica cuando el usuario ya tiene una suscripción activa al proveedor, cuando el sistema expone tools y datos al asistente del usuario sin centralizar la cognición, o cuando la economía operativa privilegia minimizar costos de inferencia.

Los dos modos coexisten. Un mismo sistema agentivo puede operar Asistentes del usuario en modo Suscripción y Agentes Autónomos en background en modo Tokens, simultáneamente. La especificación exige que el sistema declare explícitamente qué modo aplica a qué componente. Confundir los modos en la implementación es fuente recurrente de errores económicos: un Agente Autónomo accidentalmente operando en modo Suscripción puede agotar la cuota del usuario en horas; un Asistente accidentalmente operando en modo Tokens puede facturar al sistema operaciones que deberían ir contra la suscripción del usuario.

Bajo planes de Suscripción fija, los **Botlets son el mecanismo arquitectónico para extender autonomía sin saturar el plan**: un agente que ejecuta su trabajo cotidiano vía Botlets, reservando la cognición para cuando el ambiente cambia, puede operar en background continuo sin agotar la cuota. Esto hace al Botlet palanca económica, no solo optimización técnica. El Capítulo 5 §2 desarrolla esta economía de la suscripción.

Una propiedad complementaria de la Capa 2 es la **configurabilidad del proveedor de cognición**. Una arquitectura agentiva conforme debe permitir que el sistema use un proveedor default — el que el operador del AgencyDomain haya elegido como economía base — pero admita su sustitución por un proveedor traído por el cliente final. La industria usa el término **BYOModel** (*bring your own model*), análogo al patrón BYOK (*bring your own key*) o BYOIP (*bring your own IP*) del campo cloud. La consecuencia arquitectónica es que la spec del agente — sus Capabilities, sus tools, sus políticas de Trust Infrastructure — debe ser **independiente del runtime de cognición**. Esto habilita multi-tenancy con cognición heterogénea (distintos clientes operando en el mismo sustrato con distintos proveedores de modelo) y respeta la **soberanía cognitiva** del cliente: la organización decide quién procesa sus prompts. La spec exige BYOModel como propiedad **SHOULD**: no toda implementación lo soporta hoy, pero las arquitecturas que aspiren a operar en mercados regulados deberán incorporarlo en plazo previsible.

Una nota final sobre la frontera de evolución de la Capa 2: la especificación admite **cognición agnóstica** — simbólica, híbrida, multimodal. La implementación contemporánea es predominantemente LLM-céntrica, pero la arquitectura no lo exige. La extensión formal de la Capa 2 a otros sustratos cognitivos — sistemas simbólicos para problemas formales, modelos multimodales que integran datos de sensores, arquitecturas híbridas que combinan ambos — es horizonte estratégico, no de corto plazo. La importancia para el arquitecto es no atar el diseño de las otras capas a la suposición de que la Capa 2 será siempre LLM. La arquitectura debe sobrevivir el cambio.

Una segunda nota sobre el rol de la **capa semántica** — concepto que el Capítulo 2 ya introdujo con sus cifras. La calidad de la cognición depende críticamente de la calidad de la información que la alimenta. Una arquitectura agentiva seria contempla la capa semántica como integración necesaria entre Capa 2 y los datos del Entorno (Capa 4): sin ella, la cognición opera sobre representaciones inconsistentes de la realidad y produce respuestas que se ven coherentes pero fallan en lo que importa.

## Capa 3 — Autonomía

La Capa 3 es donde el agente vive. Es vida persistente, ejecución continua, acción por iniciativa propia. Donde habitan los **Agentes Autónomos** — proactivos, no reactivos. Distintos del Asistente que vive en Capa 2 y espera ser invocado.

El Agente Autónomo se distingue del Asistente de la Capa 2 en una diferencia operativa: el Asistente responde cuando se le solicita, sin estado persistente ni Botlets propios; el Agente Autónomo persigue objetivos sin input continuo del humano, mantiene estado, regenera Botlets y vive en background. El Capítulo 5 §5 desarrolla la distinción.

Los componentes canónicos de la Capa 3 son seis. El **procesamiento proactivo** es el corazón de la capa: el agente no espera órdenes; persigue objetivos. Las **tareas asíncronas** son operaciones que se ejecutan en background sin bloquear ningún hilo conversacional. El **monitoreo continuo** detecta anomalías, eventos, umbrales que disparan acción. Los **Botlets en ejecución** son la memoria muscular del agente operando — ciclo canónico `95/4/1`: 95% de ejecución normal, 4% de cambio detectado en el ambiente que hace fallar el Botlet, 1% de regeneración del Botlet por la cognición. El **Botler** es el framework runner que ejecuta los Botlets — pieza invisible al usuario y al agente mismo, responsabilidad de la implementación. La **coordinación intra-AgencyDomain** —vía el protocolo `A2A`— es comunicación entre componentes especialistas que viven en el mismo espacio computacional: coordinación entre agentes especialistas, delegación dinámica, intercambio de resultados.

Y la propiedad innegociable que define la capa: **garantía de fallback**. Si un Botlet falla catastróficamente, la cognición ejecuta la tarea manualmente. El proceso nunca se detiene. Esta garantía distingue al sistema agentivo conforme a esta especificación de cualquier "automatización con IA" frágil. Una organización que delega operación a agentes debe poder confiar en que un fallo aislado no detiene su negocio. La resiliencia es lo que hace esa confianza razonable. Sin garantía de fallback, los Botlets son scripts frágiles disfrazados de innovación; con garantía de fallback, son piezas operacionales en las que la organización puede apoyarse.

> *Sin Capa 3, el agente solo reacciona. Con Capa 3, el agente puede anticipar.*

La Capa 3 exige tres propiedades fuertes que cualquier implementación debe satisfacer. La **persistencia entre sesiones** asegura que el estado del agente sobrevive a desconexiones, reinicios y migraciones. Un agente que pierde su estado cuando el servidor se reinicia no es Agente Autónomo — es Asistente con un proceso largo. El **aislamiento de ejecución** asegura que los Botlets corren bajo sandboxing apropiado al ambiente — contenedores, WASM, MicroVMs según trade-off de seguridad y overhead. Un Botlet generado por la cognición es código nuevo; debe operar bajo confinamiento estricto antes de tocar recursos sensibles. La **resiliencia estructural** asegura que ningún fallo de un Botlet individual detiene la operación del agente. Un Botlet falla, otro lo reemplaza, la cognición regenera, y el sistema sigue.

Hay una tentación recurrente, especialmente en equipos provenientes del mundo del software tradicional, de tratar a la Capa 3 como "donde corren los workflows" — análogo agentivo de un orquestador clásico tipo Airflow o Temporal. La analogía es engañosa porque los workflows tradicionales son estáticos: están definidos por código que el humano escribió, ejecutan los pasos en el orden previsto, fallan cuando algo se sale del flujo. La Capa 3 agentiva es **dinámica**: los Botlets que ejecuta los generó la cognición, se regeneran cuando el ambiente cambia, y la organización confía en que el conjunto opera coherentemente sin que ningún humano haya escrito explícitamente el flujo. Un orquestador clásico es ejecutor de instrucciones humanas; la Capa 3 es ejecutor de instrucciones que la cognición misma generó — y eso cambia todo el modelo de gobierno del sistema.

La interfaz por la que la Cognición comanda esta capa es **interna** y vive **dentro del mismo AgencyDomain**: la Capa 2 comanda a la Capa 3 — la Cognición operando su propia memoria muscular. El transporte natural es `MCP` (la Cognición es un agente LLM y `MCP` es el protocolo LLM↔herramienta): el **Botler expone servidor(es) `MCP`** y la **Cognición es el cliente**. Esto **no es `A2A`** — `A2A` es la relación entre AgencyDomains (agentes), federación o externo, no la operación interna de un agente sobre su propio runtime. El desarrollo de esta interfaz y de su API de operación vive en la especificación de AgencyDomains (Capítulo 5 §1) y en el capítulo de Botlets.

Una propiedad estructural adicional de la Capa 3 — central para sistemas con presencia física múltiple — es que admite **distribución geográfica dentro de un mismo AgencyDomain**. Un sistema que opera 7 locales gastronómicos, 50 sucursales bancarias o 200 puntos de atención de salud no necesita 7, 50 o 200 AgencyDomains independientes — necesita un solo AgencyDomain con la **Capa 3 distribuida** entre un Botler central (Botlets de orquestación, planificación, reportería, decisiones globales) y N Botlers edge (Botlets transaccionales locales con BD local y cola de eventos hacia central), coordinados por la coordinación intra-AgencyDomain —vía el protocolo `A2A`— entre Botlers del mismo AgencyDomain. Esto no es federación `A2A` entre AgencyDomains distintos; es **distribución interna de la Capa 3** dentro de un solo AgencyDomain. La spec completa del patrón vive en el Capítulo 5 §1.

## Capa 4 — Acceso

La Capa 4 es donde la cognición se convierte en acción real sobre el mundo. Es el poder de ejecución del agente sobre sistemas, datos y agentes externos. Punto donde toda decisión del agente debe pasar por gobernanza antes de tocar el mundo. Si la Capa 3 es donde el agente vive, la Capa 4 es donde el agente actúa.

Los componentes canónicos de la Capa 4 son ocho y los desplegamos con cuidado. Los **servidores de tools** son herramientas que el agente puede invocar para tocar sistemas externos — correo, calendarios, repositorios, bases de datos, ERPs, CRMs, APIs públicas, archivos. El protocolo canónico contemporáneo es el **Model Context Protocol** (MCP), introducido por Anthropic en noviembre de 2024 y adoptado progresivamente como estándar abierto de la industria. La adopción rápida de MCP — más rápida de lo que casi cualquier protocolo abierto reciente había logrado — refleja una necesidad real: el campo carecía de un estándar para conectar agentes con tools, y todos los actores serios entendieron que la fragmentación era problema antes que ventaja. Los **Conectores** son el saber acceder a sistemas fuente — la API legacy del mundo pre-agentivo traída a la Capa 4 como capacidad de acceso con poder de ejecución, no como saber cognitivo (ese vive en la Capa 2 como Capability). Es la materialización en la arquitectura del destino que la Bounded Concerns Architecture asigna a la celda API: persiste, se intensifica y se reposiciona como Conector.

La **`A2A` entre AgencyDomains** habilita interacción entre agentes que viven en espacios computacionales distintos — federación entre AgencyDomains de organizaciones diferentes, integración con agentes de proveedores externos. La **Trust Infrastructure ejercida en el punto de acción** es probablemente el componente más crítico de la Capa 4: gobernanza, auditoría, validación, resiliencia y transparencia se ejercen aquí, donde el agente está a punto de actuar. La descripción detallada de Trust Infrastructure viene más adelante en este capítulo y se desarrolla con detalle en el Capítulo 5. Los **permisos CRUDLEX** son el modelo canónico de control granular: Create, Read, Update, Delete, List, Execute, aplicables por usuario, agente o contexto. La descripción operacional completa de CRUDLEX vive en el Capítulo 8. La **aprobación humana** es opcional, configurable por política, para operaciones críticas — envío de email externo, transferencia financiera, modificación irreversible. El **routing inteligente y caché semántico** optimizan costos y latencia de invocaciones. El **append-only log inmutable** es el registro auditable de cada acción del agente, con linaje completo para reconstrucción posterior.

> *La Capa 4 convierte la cognición en acción real con gobernanza.*

Las propiedades exigidas de la Capa 4 son cuatro y todas son obligatorias para un sistema en producción enterprise. La primera es **no-repudio**: toda acción queda registrada con identidad del agente, contexto y resultado. Cuando el sistema ejecuta una operación, debe poder reconstruirse después qué agente la ejecutó, en nombre de qué humano u organización, con qué autorización, y con qué resultado. Sin no-repudio, no hay auditoría posible y no hay defensa regulatoria. La segunda es **reversibilidad cuando aplica**: operaciones críticas tienen mecanismo de rollback o compensación. No todas las operaciones son reversibles — un email enviado o una transferencia ejecutada típicamente no lo son —, pero cuando la reversibilidad es técnicamente posible, debe diseñarse desde el inicio. La tercera es **política antes de ejecución**: ninguna acción se ejecuta sin haber pasado por el plano de gobernanza. La política se evalúa antes, no después. Un sistema que registra decisiones después de tomarlas y luego espera al humano a corregirlas tiene un modelo de gobernanza que llega tarde. La cuarta es **observabilidad uniforme**: toda invocación produce traces, métricas y eventos en el mismo formato. Sin uniformidad, los datos de observabilidad son inconsumibles operativamente.

La Capa 4 es donde la mayoría de los proyectos agentivos fracasan, según los datos de campo del Capítulo 2. La razón estructural: equipos que vienen del mundo del software tradicional tratan la Capa 4 como "API gateway con permisos", y no es eso. Un API gateway tradicional opera sobre solicitudes humanas — el humano hace la solicitud, el gateway valida permisos, el sistema ejecuta. La Capa 4 agentiva opera sobre solicitudes generadas por agentes que actúan autónomamente. La validación no puede asumir que un humano supervisó la solicitud antes; debe asumir que el agente decidió por sí mismo, y que el humano no la verá hasta el log de auditoría. Esto exige niveles de validación, registro y aprobación que los sistemas tradicionales no necesitaban.

## Trust Infrastructure — el eje transversal

Trust Infrastructure no es una capa adicional. Es **transversal a las cuatro**. Sin Trust Infrastructure, los pilotos con agentes mueren al pasar a producción enterprise — y "morir" no es metáfora; es lo que produce el cuarenta por ciento de proyectos cancelados que Gartner pronostica. Trust Infrastructure es la diferencia entre experimentar y operar.

Cinco pilares constituyen Trust Infrastructure. La **Gobernanza** define políticas configurables, permisos CRUDLEX, aprobación humana para operaciones críticas, registro de IA. Se ejerce principalmente en la Capa 4, transversalmente en el resto. La **Auditoría** mantiene append-only log inmutable, trace de cada acción, lineage de decisiones, identity tagging por acción. Se ejerce en Capa 4 y transversalmente. La **Validación** detecta alucinaciones, valida respuestas, previene prompt injection, ejecuta DLP y tokenización. Se ejerce en Capa 2 y Capa 4. La **Resiliencia** garantiza fallback, maneja errores, sandboxing de Botlets. Se ejerce en Capa 3 y transversalmente. La **Transparencia** entrega observabilidad completa, métricas, traces end-to-end, alertas proactivas, dashboards de gobernanza. Es transversal a las cuatro capas.

La descripción detallada de cada pilar — sus mecanismos canónicos, sus propiedades exigidas, su operacionalización en políticas concretas — vive en el Capítulo 5 §4 y en el Capítulo 8 (que operacionaliza los cinco pilares en políticas, modelo CRUDLEX completo, formato del append-only log, protocolos de aprobación humana). En este capítulo basta retener la propiedad arquitectónica fundamental: Trust Infrastructure no se agrega después de que el agente funciona — se diseña desde el inicio, en la arquitectura misma.

La urgencia de Trust Infrastructure ya no es solo arquitectónica — es regulatoria. Singapore IMDA publicó en enero de 2026 el primer framework estatal de gobernanza para IA agentiva — el Model AI Governance Framework for Generative AI (MGF) —, que establece que aunque los agentes actúan autónomamente, *"la responsabilidad humana continúa aplicando"*. La Unión Europea hace lo propio con el EU AI Act, NIST con su AI Risk Management Framework, ISO/IEC con 42001. La pregunta ya no es si los reguladores exigirán infraestructura de confianza — es si la organización puede demostrarla auditablemente cuando se la pidan.

El estado del campo respecto a gobernanza está documentado con cifras en el Capítulo 2: la mayoría de las organizaciones que operan agentes hoy no están preparadas para defender lo que sus agentes hacen. Lo que aquí importa es la consecuencia arquitectónica de ese diagnóstico: si la gobernanza no se diseña desde el inicio, no se construye después.

> *La gobernanza no es lo que se agrega después de que el agente funciona. Es lo que separa pilotos de producción.*

## El principio rector — Agent First

> *Ante cualquier disyuntiva, se prioriza la experiencia del agente sobre la del humano. El agente es el usuario primario; las necesidades del humano se resuelven en una capa de gestión sin degradar lo que el agente ve y puede hacer.*

El principio Agent First es regla de gobierno de diseño que ordena cualquier disyuntiva de arquitectura. Invierte la lógica del diseño tradicional de software, donde el humano es siempre el usuario primario y todo se diseña para que él pueda operar. En la Arquitectura Agentiva, las APIs, los schemas, los errores y los flujos de control se diseñan **primero** para el consumo del agente. La superficie humana — settings, dashboards, interfaces administrativas — es secundaria y no condiciona las decisiones arquitectónicas.

La inversión no es retórica — tiene implicaciones operativas concretas. Cualquier capacidad nueva del sistema se especifica primero como **tool con schema declarativo JSON**, después como GUI si aplica. Los **errores son estructurados y accionables**: códigos y mensajes diseñados para que el agente decida el siguiente paso, no para que el humano "lea el log". La **idempotencia donde aplica**: los reintentos del agente deben ser seguros sin requerir lógica defensiva en el llamador. La **paginación y filtros uniformes** entre tools: formato consistente, predecible para el agente. La **documentación machine-readable**: la documentación pública es consumible por el agente como contexto, no solo legible por humanos.

Agent First es **regla de gobierno**. Cualquier disyuntiva de diseño que la viole requiere justificación explícita y documentada. Cuando el equipo se enfrenta a una decisión donde "esto sería más fácil para el humano operador, pero hace más difícil para el agente", la respuesta default es priorizar al agente. La excepción debe argumentarse y registrarse. Sin regla de gobierno explícita, la inercia del software tradicional empuja todas las decisiones hacia el lado humano, y el sistema termina siendo otra aplicación con maquillaje agentivo.

La razón estructural detrás del principio: en el Mundo Agentivo, la frecuencia con la que el sistema interactúa con agentes es **órdenes de magnitud mayor** que la frecuencia con la que interactúa con humanos. Un sistema agentivo en producción típicamente tiene millones de invocaciones de agentes contra cientos de operaciones humanas. Optimizar para el caso minoritario — el humano — degrada exponencialmente el caso mayoritario — el agente. Agent First es reconocimiento de esa asimetría.

## La evolución de los agentes

<!-- FIG:g15-tres-fases -->
![Las tres fases evolutivas de los agentes](figuras/g15-tres-fases.png)

La arquitectura admite tres fases evolutivas en la sofisticación del agente. Distintas organizaciones se encuentran en distintas fases, y la conversación sobre arquitectura cambia significativamente según la fase actual.

La **fase uno** son los **agentes especializados**: un agente por dominio. Cada uno con sus Capabilities específicas, su rol claro, su superficie limitada. El agente financiero opera sobre cashflow; el agente de atención al cliente opera sobre tickets; el agente de operaciones opera sobre inventario. Esta es la fase actual del mercado. La mayoría de los agentes en producción a inicios de 2026 son agentes especializados de fase uno. La razón es práctica: es la fase más fácil de gobernar — el alcance es estrecho, el riesgo es contenido, el caso de uso está claro.

La **fase dos** son los **agentes orquestadores**: un agente coordina múltiples especialistas. Delegación dinámica según la tarea. El agente orquestador no resuelve el problema directamente — descompone el problema, identifica qué especialistas pueden resolver cada parte, delega, integra los resultados. Esta es fase de transición que algunos actores líderes ya están explorando, especialmente en casos donde las tareas atraviesan dominios — un caso de servicio al cliente que requiere consulta a finanzas, validación con operaciones y respuesta al cliente final, por ejemplo. La fase dos exige Capa 3 robusta para que los agentes especializados puedan coordinarse intra-AgencyDomain, vía el protocolo `A2A`.

La **fase tres** son los **agentes multiespecialistas**: expertise profundo multi-dominio en un único agente. La fase futura — requiere madurez de Capabilities y Pattern Recognition que la industria todavía no ha alcanzado. Un agente multiespecialista no descompone el problema delegando — lo resuelve directamente integrando saber de múltiples dominios. La diferencia con el orquestador es ontológica: el orquestador es coordinador de especialistas; el multiespecialista es especialista profundo en muchas cosas a la vez. Las Capabilities en el caso multiespecialista forman un árbol mucho más amplio y profundo, y la cognición debe poder navegarlo eficientemente.

La arquitectura es **la misma en las tres fases**. Lo que cambia es la complejidad de la cognición y la profundidad del árbol de Capabilities. Un sistema bien diseñado en fase uno puede evolucionar a fase dos sin reescritura — agregando más agentes especializados al espacio computacional y habilitando la coordinación intra-AgencyDomain. Un sistema bien diseñado en fase dos puede evolucionar a fase tres cuando las Capabilities maduren — fusionando árboles de saber especializados en árboles más amplios. Esta capacidad de evolución sin reescritura es propiedad emergente del diseño en cuatro capas. Un sistema mal diseñado — con capas fundidas — necesita reescritura completa para pasar de fase uno a fase dos, y eso es típicamente cuando los proyectos colapsan.

## El ámbito computacional — AgencyDomains

<!-- FIG:g16-space-domain -->
![Space ≠ Domain · la diferencia ontológica](figuras/g16-space-domain.png)

### Premisa fundacional — Space ≠ Domain

Donde el humano tiene un **Space** —corporeidad heredada del escritorio físico, extendida por la industria a **WorkSpace**—, el agente no tiene cuerpo: ejerce agencia sobre un **Domain**, un ámbito de jurisdicción computacional donde su identidad rige, sus Capabilities aplican y sus Botlets corren. El Capítulo 5 §1 desarrolla la derivación completa de esta premisa.

> *Donde el humano tiene Space (WorkSpace), el agente tiene Domain (AgencyDomain).*

### El AgencyDomain como construcción formal

La arquitectura se materializa en una construcción formal: el **AgencyDomain** — ámbito computacional donde habitan agentes autónomos. Análoga conceptual a JavaSpaces — la especificación JSR-000148 de Sun Microsystems que en 1999 estandarizó los espacios distribuidos para sistemas Java sin atar la implementación a un proveedor particular —, AgencyDomains hace lo equivalente para los entornos agentivos. Define cómo deben construirse — capas, ciclos, primitivas, interfaces — sin prescribir una implementación específica. La diferencia de nombre con su predecesor no es ruptura sino precisión: un Java *Space* era espacio computacional para procesos sin cuerpo; un Agency *Domain* es ámbito de jurisdicción para agentes con agencia.

La especificación formal de AgencyDomains vive en su documento dedicado, que es la primera sección del Capítulo 5. En este capítulo basta retener que la Arquitectura Agentiva, vista como construcción técnica concreta, se instancia en AgencyDomains. Cuando hablamos de "el sistema agentivo", nos referimos a una instancia de AgencyDomain que materializa las cuatro capas, ejerce Trust Infrastructure y respeta el principio Agent First.

La especificación cubre aspectos como el modelo de identidad y direccionamiento de agentes y Botlets, el ciclo de vida del agente dentro del ámbito, la coordinación intra-AgencyDomain y la `A2A` entre AgencyDomains (ambas vía el protocolo `A2A`), la federación entre AgencyDomains (cómo dos ámbitos distintos colaboran), y el modelo de tenancy y aislamiento. Todos estos detalles los desarrolla el Capítulo 5 §1.

## La distinción Asistente vs Agente Autónomo

Una distinción crítica atraviesa las capas 2 y 3 y determina cómo se diseña, opera y cobra cualquier sistema agentivo: la distinción entre **Asistente** y **Agente Autónomo**.

El Asistente vive en Capa 2 (Cognición). Es reactivo: responde cuando se le solicita, espera input del humano, no mantiene Botlets propios, no tiene vida persistente entre sesiones. El Agente Autónomo vive en Capa 3 (Autonomía). Es proactivo: actúa por iniciativa propia, persigue objetivos sin input continuo del humano, mantiene y regenera sus Botlets, vive con vida persistente en background.

La operacionalización de la distinción — cuándo conviene cada rol, qué anti-patrones evitar al confundirlos, cómo se cobran y se gobiernan distinto — la desarrolla el Capítulo 5 §5. En este capítulo basta haber introducido la distinción para que el lector pueda interpretar correctamente las referencias a uno o al otro modo en el resto de la arquitectura.

## Implementaciones de referencia

Esta arquitectura admite múltiples implementaciones. La primera implementación coordinada es el portafolio de ultraBASE, donde la responsabilidad por las cuatro capas se materializa a través de productos cooperantes — sin que cada capa quede asignada exclusivamente a un producto. Cada producto contribuye con uno o más de los comportamientos del agente; la pila integrada los compone para que el agente exhiba los cuatro.

Otros actores que adopten esta arquitectura tendrán sus propias implementaciones — cada una válida en la medida en que respete las cuatro capas, ejerza Trust Infrastructure y honre el principio Agent First.

El libro evita deliberadamente describir la implementación específica de ultraBASE dentro de sus capítulos, para no confundir la arquitectura formal con su implementación particular. El Epílogo, en "Lo que NO está en este libro", desarrolla por qué esa separación preserva la pretensión de estándar de industria.

## Frontera de evolución

La arquitectura admite extensión legítima en el tiempo a lo largo de tres horizontes técnicos: la **cognición no-LLM** —simbólica, híbrida, multimodal— que la frontera de la Capa 2 ya anticipó arriba; la **federación entre AgencyDomains** —la `A2A` entre ámbitos no-relacionados, hoy capacidad emergente y no spec consolidada—; y el **mundo de carbono** —conectar la Capa 4 al mundo físico (IoT, sistemas industriales, manufactura), eslabón once de la cadena de valor que el Capítulo 6 §3 desarrolla—. El Epílogo desarrolla las cuatro fronteras vivas de la arquitectura, estas tres técnicas más la institucional.

Los tres vectores definen la frontera de innovación de la plataforma. Los tres están sostenidos por las proyecciones de mercado documentadas en el Capítulo 2: penetración masiva de agentes en aplicaciones empresariales hacia 2026, decisión autónoma significativa hacia 2028, capital colectivo apostando una década completa a la dirección agentiva. La pregunta que esta arquitectura responde — *cómo se construyen estos sistemas con disciplina* — solo se vuelve más urgente con cada trimestre que pasa.

---

Las cuatro capas son la respuesta arquitectónica al paradigma. Pero las capas no se sostienen solas — necesitan piezas reusables que las pueblen para que un implementador pueda construir contra ellas con disciplina. El Capítulo 5 entrega esas piezas — siete primitivas técnicas canónicas que constituyen el vocabulario constructivo de un sistema agentivo conforme: **AgencyDomain** como espacio computacional, **Botlet** como memoria muscular del agente, **proto-Botlet** como su pieza pre-forjada, **Capability** como árbol del saber cognitivo, **Trust Infrastructure** como infraestructura de confianza, la distinción **Asistente vs Agente Autónomo** como eje operativo, y la **Faceta** como unidad atómica de la Capa 1. Quien complete los dos capítulos tiene en mano el conjunto de construcciones formales con las que la categoría agentiva puede ser razonada y construida.

Una nota sobre la numeración de las primitivas: a lo largo del libro la Faceta se rotula como *sexta primitiva canónica* y el proto-Botlet como *séptima primitiva canónica*. Esos ordinales indican el **orden en que cada primitiva se incorporó al canon** —la Faceta se formalizó en v0.3, el proto-Botlet en v0.4— y no su posición en la enumeración de arriba, donde el proto-Botlet aparece junto al Botlet por ser su pieza pre-forjada.

## Resumen visual

Las cuatro capas en topología paralela, con sus componentes principales, la infraestructura transversal y el principio rector:

| Capa | Rol | Componentes principales |
|---|---|---|
| **1 · Interacción** | donde el humano se comunica con el sistema | conversacional textual · conversacional por voz · canales · API directa · GUI generada (on-the-fly · persistente como Botlet de fachada) · señalética |
| **2 · Cognición** (vía lenta · costosa · decisiva) | donde el sistema piensa | multi-LLM · Capabilities · Pattern Recognition · generación de Botlets · Asistente reactivo |
| **3 · Autonomía** (vía rápida · barata · repetitiva) | donde el sistema vive con persistencia | Botlets en ejecución · Botler central + edge · tareas asíncronas · monitoreo · garantía de fallback |
| **4 · Acceso** | donde el sistema actúa sobre el mundo real | tools (MCP) · Conectores · A2A entre AgencyDomains · CRUDLEX · aprobación humana · append-only log · Capabilities cloud/edge/híbridas |

**Trust Infrastructure** es transversal a las cuatro capas (Gobernanza · Auditoría · Validación · Resiliencia · Transparencia). Las Capas 2 y 3 son **vías paralelas** entre Capa 1 y Capa 4 — no etapas en serie —, y el principio rector es **Agent First**.

