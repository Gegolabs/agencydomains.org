## Capabilities

Cuando un consultor experimentado de finanzas se enfrenta a un problema nuevo en un cliente, no parte de cero. Trae consigo un cuerpo de saber-hacer organizado que aplica al caso particular: principios contables, marcos regulatorios, frameworks de análisis, prácticas profesionales que la industria ha consolidado durante décadas. Cuando un consultor de operaciones aborda un problema de cadena de suministro, hace lo mismo con su propio cuerpo de saber: SCOR, Six Sigma, lean manufacturing, planificación de demanda. Cada disciplina profesional tiene su árbol de saber-hacer, y la calidad del consultor depende en buena parte de cuán profundo y bien organizado está ese árbol en su cabeza.

Los agentes de IA enfrentan el mismo problema. Un agente que opera en finanzas necesita saber finanzas; un agente que opera en legal necesita saber legal; un agente que opera en marketing necesita saber marketing. Pero "saber" en este contexto no significa simplemente que el modelo subyacente haya leído documentación de finanzas durante el entrenamiento. Significa que el agente tiene acceso, modular y composable, a un cuerpo organizado de saber-hacer profesional que puede aplicar selectivamente según la tarea. Esta organización es lo que la Arquitectura Agentiva llama **Capabilities**.

Esta sección desarrolla el concepto de Capability como primitiva canónica de la Capa 2 (Cognición). Lo que hace especial a la Capability respecto a otros conceptos cercanos del campo es su **estructura jerárquica**, su **composabilidad**, y su distinción explícita de plugins y prompts. Un agente sin Capabilities tiene cognición monolítica que confunde dominios; un agente con Capabilities bien organizadas opera con la disciplina de un profesional que conoce las distinciones de su campo.

### Definición

Una **Capability** es una unidad de saber-hacer especializado que un agente comprende y aplica. Encapsula el conocimiento procedimental y declarativo de un dominio: qué se sabe, cómo se aplica, qué se decide, qué se pregunta cuando faltan datos. Las Capabilities residen en la **Capa 2 (Cognición)** de la Arquitectura Agentiva. La cognición selecciona y aplica Capabilities según la tarea — del mismo modo en que un consultor experto selecciona y aplica frameworks profesionales según el problema que tiene enfrente.

> *El agente no sabe lo que el modelo sabe. Sabe lo que sus Capabilities le permiten saber.*

La cita anterior distingue lo que la Capa 2 sabe de lo que el modelo subyacente conoce. El modelo subyacente — Claude, GPT, Gemini — fue entrenado con una cantidad masiva de información que incluye, entre muchas otras cosas, conocimiento profesional. Pero el agente que vive en la Capa 2 **no opera directamente con el conocimiento del modelo**. Opera con las Capabilities que le fueron asignadas, que son curaciones específicas de saber-hacer aplicado a contextos particulares. Un agente que tiene la Capability de *General Ledger* pero no la Capability de *Tax* responde con autoridad sobre contabilidad general pero sabe que no es la fuente correcta para preguntas de impuestos. Un agente sin Capabilities específicas opera con el conocimiento difuso del modelo, que puede ser correcto en general pero rara vez es preciso en lo profesional.

### ¿Qué NO es una Capability?

Para fijar la definición con la precisión que la spec exige, contrastamos la Capability con conceptos vecinos que la industria usa con descuido. Cada uno de estos conceptos vecinos tiene su rol legítimo en sistemas de IA, pero ninguno es Capability, y confundirlos lleva a arquitecturas que terminan siendo collages mal integrados.

El término **Capability** queda reservado, en sentido estricto, al **saber-hacer cognitivo** de la **Capa 2 (Cognición)**: saber que interpreta, decide y razona sobre un dominio. Esta reserva importa porque otros entregables agentivos —conexiones a sistemas fuente, confecciones de presentación— viven en otras capas, tienen naturaleza distinta y se construyen con esquemas de desarrollo propios. Tratarlos a todos como Capabilities obligaría a apellidar el término en cada uso y diluiría su valor. La sección *Capability, Conector y Plantilla — tres entregables por capa* fija los términos propios de cada capa.

Un **plugin** vive en el contexto de una aplicación host. Extiende esa aplicación con una función nueva. Está atado al host: el plugin de Excel solo opera dentro de Excel, el plugin de Notion solo opera dentro de Notion. Una Capability no está atada a un host — vive en el árbol de Capabilities del agente y es invocable desde cualquier contexto donde el agente opere.

Un **prompt** es una formulación lingüística específica que se inyecta al modelo en una invocación particular. Los prompts son útiles, pero son artefacto transitorio: cambian de invocación a invocación, no codifican saber persistente. La Capability puede usar prompts internamente como uno de sus mecanismos de implementación, pero no se reduce a un prompt. Una Capability bien diseñada incluye vocabulario, conocimiento procedimental, conocimiento declarativo, heurísticas y referencias a tools — el prompt es solo uno de los componentes.

Un **system prompt** establece tono y comportamiento general del modelo. Es configuración del modo de operación, no saber-hacer modular. Las Capabilities **no son system prompts** — pueden coexistir con uno, pero capturan otra cosa: conocimiento del dominio aplicable según la tarea, no configuración global del agente.

Un **tool** vive en la Capa 4 (Acceso). Es acción ejecutable sobre el mundo externo: invocar una API, leer un archivo, enviar un email. La Capability **decide qué tool invocar y cómo interpretar su resultado**, pero no es el tool mismo. La Capability es saber; el tool es acción. Un agente financiero con la Capability de *Treasury* sabe cuándo y cómo invocar el tool que consulta los saldos bancarios — pero el tool en sí es componente separado que vive en otra capa.

Un **skill**, en la terminología popular del campo, es término que la industria usa con tanto descuido que prácticamente ha perdido sentido. Diversos proveedores llaman "skills" a plugins, a prompts, a tools, a configuraciones — sin distinción precisa. La Capability no es skill en el sentido genérico, pero la coincidencia parcial de uso popular puede confundir al lector. Para evitar la confusión, este libro reserva el término Capability con definición precisa y evita usar "skill" salvo en cita textual de fuentes que lo usan.

Tres rasgos distinguen a una Capability genuina. **Modular**: puede activarse o desactivarse independientemente de las demás. Si un agente tiene Capabilities de *Finance* y *Legal* y se le retira *Legal*, el agente sigue operando coherentemente con *Finance* solamente. **Composable**: múltiples Capabilities pueden coexistir en un mismo agente y combinarse cuando la tarea cruza dominios. Un agente que tiene *Finance* y *Operations* puede manejar un caso de logística que tiene componentes financieros sin tropezarse en la transición. **Saber, no acción**: la Capability sabe; los tools (Capa 4) actúan. La Capability decide qué tool invocar y cómo interpretar su resultado.

### Capability, Conector y Plantilla — tres entregables por capa

Un proyecto agentivo de entrega rara vez entrega solo una Capability. La Capability cognitiva es la protagonista, pero suele venir acompañada de entregables que viven en otras capas y se construyen con esquemas distintos. La spec canoniza tres términos, uno por capa, para que cada entregable se nombre por lo que es sin apellidar el término Capability.

<!-- FIG:g28-tres-entregables -->
![Tres entregables por capa — Capability (Capa 2) · Conector (Capa 4) · Plantilla (Capa 1)](figuras/g28-tres-entregables.png)

Una **Capability** (sentido estricto) es saber-hacer **cognitivo**, interpretativo, decisional. Vive en la **Capa 2 · Cognición**. Es la protagonista del proyecto.

Un **Conector** es saber **acceder a sistemas fuente** — conexión con poder de ejecución. **No es saber cognitivo**. Vive en la **Capa 4 · Acceso**. El Conector es lo que el campo pre-agentivo conoce como la integración técnica que toca el mundo externo. Una API legacy, al traerse al Mundo Agentivo, se convierte en **Conector** (Capa 4), no en Capability.

Una **Plantilla** es la **confección específica del cliente** sobre un instrumento canónico — un reporte o dashboard que la Capability produce — en un formato o regla particular exigido por el cliente. Vive en la **Capa 1 · Interacción**, junto a la Faceta, el Botlet de superficie y el Botlet de vista. Ejemplos anonimizados: una plantilla regulatoria de oferta básica de interconexión sobre el reporte canónico de costos; un formato de cierre financiero mensual gerencial sobre el dashboard canónico de rentabilidad. La Plantilla no es Capability, no es Faceta y no es Botlet: el comprador ya conoce el término "plantilla" del vocabulario pre-agéntico y no necesita aprender uno nuevo.

#### ¿Cómo se desarrolla cada entregable?

Cada término tiene su capa, su naturaleza y su esquema de desarrollo propio:

| Entregable | Capa | Naturaleza | Esquema de desarrollo |
|---|---|---|---|
| **Capability** (protagonista) | Capa 2 · Cognición | Saber-hacer cognitivo, interpretativo, decisional | Wingtraining 5 pasos (workshop SME · creación · personalización · ALFA · BETA) |
| **Conector** (compañero, si requiere acceso a sistemas fuente) | Capa 4 · Acceso | Saber acceder a sistemas; no es saber cognitivo | Esquema de integración (relevar · configurar · probar · certificar) |
| **Plantilla** (compañero, si la entrega debe conformar a una expectativa de presentación) | Capa 1 · Interacción | Confección de un instrumento canónico en un formato o regla del cliente | Esquema de confección (relevar expectativa · confeccionar sobre instrumento canónico · validar) |

El **Wingtraining**, citado en la tabla, es el esquema canónico de desarrollo de una Capability en cinco pasos: **workshop con el SME** (*subject-matter expert* — el experto humano cuyo saber se transfiere al agente), **creación**, **personalización**, **ALFA** (validación con el SME) y **BETA** (validación en operación real). Su desarrollo pertenece a la práctica de entrega, no a este canon; el test de clasificación de más abajo lo usa como criterio porque es la prueba operativa de que un alcance es transferencia de saber — y no integración ni formato.

#### ¿Cuál es la estructura conceptual de un proyecto agentivo de entrega?

Un proyecto agentivo de entrega se estructura como una **Capability protagonista** (Capa 2) acompañada típicamente de uno o más **Conectores** (Capa 4) y una o más **Plantillas** (Capa 1). Además, la propia Capability produce sin esfuerzo adicional sus **instrumentos de información** — reportes y dashboards canónicos —, que quedan implícitos en la entrega: no requieren esquema de desarrollo propio porque emergen de la Capability y su capa de interacción. La Plantilla aparece solo cuando uno de esos instrumentos debe conformar a una forma específica del cliente.

#### ¿Capability o entregable de otra capa? — el test

Para decidir si un alcance es Capability en sentido estricto, los tres tests siguientes deben ser **sí**:

1. **¿Es saber-hacer cognitivo?** ¿Interpreta, decide o razona sobre un dominio — más allá de solo conectar o solo formatear?
2. **¿Tiene un SME identificable?** ¿Hay un humano experto cuyo saber se transfiere al agente?
3. **¿Pasa por los cinco pasos de Wingtraining sin forzar?** ¿Tiene sentido aplicarle workshop SME · creación · personalización · ALFA · BETA?

Si uno o más son **no**, el alcance no es Capability: pertenece a otra capa — Conector o Plantilla, según el mapeo de la sección *Capability, Conector y Plantilla* — o, si es saber cognitivo pero subordinado a una Capability mayor, es **feature** de esa Capability (ver la sección siguiente).

### La estructura jerárquica — el árbol del saber

<!-- FIG:g29-arbol-capabilities -->
![El árbol del saber + ortogonalidad funcional × vertical](figuras/g29-arbol-capabilities.png)

Las Capabilities se organizan en un **árbol jerárquico**. La estructura no es decoración — es la forma natural en que el conocimiento profesional está organizado en cualquier disciplina seria. Los analistas financieros piensan jerárquicamente: las finanzas tienen sub-disciplinas (contabilidad, corporate finance, treasury, tax), cada sub-disciplina tiene áreas (general ledger, cuentas por pagar, reconciliación), cada área tiene prácticas específicas. La organización jerárquica refleja cómo el profesional domina el campo.

A continuación un ejemplo del árbol canónico que la spec propone como punto de partida. El árbol no es exhaustivo — se extiende según las necesidades de cada implementación —, pero ilustra la estructura (figura arriba).

Cuatro reglas estructurales gobiernan el árbol. La primera: **cualquier nodo es una Capability válida**. Tanto los nodos hoja — *Reconciliación*, *Demand generation*, *Calidad* — como los nodos intermedios — *Contabilidad*, *Sales & Marketing*, *Manufacturing* — son Capabilities válidas. La granularidad la decide el contexto. Un agente especializado en operación contable diaria adopta nodos hoja con alta especificidad; un agente orquestador que coordina varios especialistas adopta nodos intermedios con visión panorámica; un agente multiespecialista combina varias raíces.

La segunda regla: **es composable**. Capabilities pueden compartirse entre agentes. Una Capability *Customer success* puede vivir en el agente de un equipo comercial y simultáneamente en el agente de un equipo de soporte, sin duplicación. Esto es crítico operativamente — la organización no necesita re-construir el saber para cada agente nuevo, sino que asigna Capabilities ya construidas según el rol del agente.

La tercera regla: **es escalable**. Se agregan ramas nuevas sin romper las existentes. La Capability *Telecom* puede subir en sofisticación — agregar sub-ramas *Network APIs*, *5G core*, *Customer experience* — sin que las otras ramas del árbol cambien. Esta propiedad es lo que permite que el árbol crezca con la organización: cada vez que la organización entra en un dominio nuevo, agrega ramas; cada vez que profundiza en un dominio existente, extiende ramas. El árbol nunca necesita reescritura completa.

La cuarta regla: **es heredable**. Una Capability hereda contexto y vocabulario de sus ancestros. Una Capability *General Ledger* no necesita re-explicar lo que es Contabilidad ni Finanzas — esa contextualización viene del árbol. Esto importa en la implementación porque permite que las Capabilities hojas sean más concisas: solo necesitan describir lo que es específico de su nodo, no lo que ya está implícito en el camino del árbol.

### Anatomía de una Capability

La especificación canónica de una Capability incluye nueve componentes que desplegamos uno por uno. Los componentes uno y nueve son metadata; los componentes dos a siete son el cuerpo del saber-hacer; el componente ocho es el binding con la capa de acción.

El primer componente es **identidad**: nombre canónico más posición en el árbol. La identidad es lo que hace que la Capability sea referenciable — los agentes la invocan por nombre, las políticas se aplican a Capabilities específicas, los logs registran qué Capability se invocó.

El segundo componente es **vocabulario**: términos técnicos del dominio que el agente debe reconocer y usar correctamente. Un agente con Capability *General Ledger* debe distinguir débito de crédito sin titubeos, debe conocer la diferencia entre asientos manuales y automáticos, debe usar correctamente el concepto de período fiscal. El vocabulario es lo que permite al agente conversar con profesionales del dominio sin sonar amateur.

El tercer componente es el **conocimiento procedimental**: cómo se hacen las tareas típicas del dominio. Cómo se reconcilia una cuenta. Cómo se valida una factura. Cómo se prepara un cierre mensual. El conocimiento procedimental es secuencial y operativo — describe pasos, no solo conceptos.

El cuarto componente es el **conocimiento declarativo**: hechos y reglas verificables del dominio. Que las cuentas por pagar tienen vencimientos. Que los ingresos se reconocen cuando se cumplen ciertos criterios. Que la conciliación bancaria debe ocurrir mensualmente. El conocimiento declarativo es factual y permanente — describe qué es verdadero del dominio.

El quinto componente son las **heurísticas**: reglas de decisión profesionales del dominio. Cuando una factura se desvía más del cinco por ciento del monto típico, escalar. Cuando una conciliación tiene más de diez transacciones sin hacer match, suspender el proceso y escalar. Cuando un proveedor tiene tres reclamos en seis meses, marcar para revisión. Las heurísticas son juicio profesional codificado — capturan no qué es verdadero del dominio, sino qué decisión tomaría un profesional en cada situación.

El sexto componente son las **tools asociadas**: tools de Capa 4 que la Capability invoca típicamente. La Capability *General Ledger* invoca tools que consultan la base de datos contable, que ejecutan asientos, que generan reportes. La Capability declara qué tools usa para que el agente sepa qué necesita disponible cuando ejerce esa Capability.

El séptimo componente son las **Capabilities padres**: posición jerárquica de la cual la Capability hereda contexto. Una Capability *General Ledger* declara que es hija de *Contabilidad*, que a su vez es hija de *Finance*. La declaración de los padres es lo que permite la herencia descrita en la sección anterior.

El octavo componente es el **estado de madurez**: Borrador / Vigente / Deprecado. El estado de madurez es metadata operacional — permite que la organización gestione el ciclo de vida de sus Capabilities. Una Capability en Borrador todavía se está validando; una Vigente está aprobada para uso productivo; una Deprecada es legacy que se mantiene por compatibilidad pero no debe usarse en agentes nuevos.

El noveno componente es **versión**: trazabilidad de evolución. Las Capabilities cambian con el tiempo — las prácticas profesionales evolucionan, las regulaciones cambian, el saber acumulado se refina. Las versiones permiten que la organización rastree la evolución del saber y que distintos agentes puedan operar con versiones distintas según sus requisitos.

Los componentes dos a cinco — vocabulario, procedimental, declarativo, heurísticas — son lo que **diferencia profundamente** una Capability bien construida de un prompt elaborado. Un prompt da contexto al modelo de manera transitoria, una sola conversación. Una Capability codifica saber profesional con persistencia y modularidad. La diferencia es estructural: el agente puede consultar la Capability *General Ledger* sin que el saber contable inunde todas sus otras conversaciones — puede tener al mismo tiempo la Capability *Marketing* sin que los frameworks de marketing contaminen el rigor contable. Esta separación es lo que permite a los agentes operar con la disciplina del profesional que cambia de marcos según la tarea.

### Features de una Capability

Una Capability expone operaciones internas. La spec canoniza el término **feature** para nombrarlas — equivalente práctico de lo que otros vocabularios llaman *feature*, *operation*, *skill* o *method*. Una feature es una operación interna que la Capability expone; comparte con la Capability contenedora su modelo de datos, su SME, su instalación y su runtime. Una Capability única de costeo, por ejemplo, expone como features la asignación de costos, la rentabilidad y el *pricing*: tres dimensiones de un mismo saber-hacer, no tres Capabilities.

#### ¿Capability o feature interna? — el test

Un alcance se trata como Capability propia si y solo si los tres tests siguientes son **sí**:

1. **¿Independencia operativa?** ¿Puede instalarse y operar sin la otra capacidad?
2. **¿Identidad cognitiva?** ¿Tiene modelo de datos y SME distintos de la otra capacidad?
3. **¿Reusabilidad?** ¿Tiene valor para más de un consumidor o contexto fuera de este caso?

Si uno o más son **no**, el alcance es **feature** de la Capability contenedora, no Capability propia.

#### Convención de IDs

Una implementación MAY adoptar una convención de identificadores para trazar el árbol de entregables: la Capability (o entregable) lleva ID `E<n>` —`E1`, `E2`—; la feature lleva ID compuesto `F<n>.<m>` —`F1.1`, `F1.2`— donde `<n>` es el ID de la Capability contenedora. La convención es opcional; lo canónico es que el constructo feature tenga nombre.

#### ¿Qué patologías previene el test?

Distinguir feature de Capability previene dos patologías observadas en proyectos reales:

- **Inflación del codominio de entregables** — dimensiones de una misma Capability se documentan como Capabilities separadas, multiplicando el inventario y diluyendo la portabilidad. El ejemplo de costeo ya citado —asignación, rentabilidad y *pricing* tratadas como tres Capabilities cuando son features de una sola— es el caso típico.
- **Esconder lock-in** — alcances que sí son Capabilities propias, con lifecycle, modelo de datos y reusabilidad independientes, terminan empotrados como "sub-capacidades" de otra, escondiendo que podrían instalarse y portarse por separado.

Los dos tests se aplican en orden: el primero decide si el alcance es siquiera cognitivo; recién entonces el segundo decide su granularidad dentro de la Capa 2. Si el alcance no es cognitivo, se clasifica directamente como Conector o Plantilla por su capa, sin correr el test de feature.

### ¿Cómo opera la cognición sobre Capabilities?

Dado un agente con un conjunto de Capabilities activas, cuando el agente recibe una solicitud, el procesamiento sigue un flujo canónico de siete pasos.

**Paso uno**: la solicitud del usuario llega al agente. El agente la recibe en lenguaje natural — *"reconcilía la cuenta de ingresos del mes pasado"*, por ejemplo.

**Paso dos**: la cognición clasifica el dominio de la solicitud. Esta operación es de routing semántico — el agente identifica que la solicitud es sobre contabilidad, específicamente reconciliación. Esta identificación se basa en el vocabulario que las Capabilities activas le proveen al agente.

**Paso tres**: la cognición selecciona las Capabilities relevantes. En el caso del ejemplo, *Finance/Contabilidad/Reconciliación* es la Capability más específica aplicable. La cognición la selecciona junto con sus ancestros — Contabilidad, Finance — para tener todo el contexto heredado.

**Paso cuatro**: la cognición aplica el conocimiento procedimental y declarativo de las Capabilities seleccionadas. Sabe qué pasos componen una reconciliación, qué reglas debe seguir, qué errores típicos puede encontrar.

**Paso cinco**: la cognición invoca los tools que la Capability indica. Consulta la base de datos contable para los asientos del mes pasado, consulta el extracto bancario, ejecuta el proceso de match.

**Paso seis**: la cognición compone la respuesta usando el vocabulario del dominio y las heurísticas de la Capability. Reporta los matches encontrados, los items sin match, las recomendaciones de cómo proceder con las discrepancias. Usa terminología que un profesional contable reconocería como correcta.

**Paso siete**: si la solicitud es repetitiva — el agente ya hizo reconciliaciones similares en el pasado —, Pattern Recognition sugiere generar un Botlet que automatice el ciclo uno a seis para futuras solicitudes similares. La cognición evalúa la sugerencia y, si las condiciones son apropiadas (frecuencia alta, patrón estable), genera el Botlet.

Una observación importante: la Capability **no se ejecuta** — es ejecutada por la cognición. Esto importa estructuralmente: la misma Capability puede ser aplicada con distinta profundidad — rápida y superficial, o lenta y exhaustiva — según el modelo cognitivo y el modo de operación del agente. Un agente con cognición sofisticada puede aplicar la Capability *General Ledger* con todo el rigor de un controller experimentado; un agente con cognición más limitada puede aplicar la misma Capability con la profundidad de un junior. La Capability define el saber-hacer; la cognición define cuán profundamente lo aplica.

### Las industrias verticales como Capabilities raíz

El árbol incluye una raíz dedicada a **industrias verticales** — Telecom, Healthcare, Retail, Banking, Public sector. Esto es deliberado: cada vertical tiene su propio vocabulario, sus propias regulaciones, sus propios procesos canónicos. La existencia de una raíz vertical separada de las raíces funcionales (Finance, Sales, Operations) refleja una propiedad estructural del saber profesional: las verticales y las funciones son **ortogonales**.

Un consultor financiero generalista tiene saber funcional — Finance — pero no saber vertical específico. Un consultor de finanzas para telecom tiene los dos: Finance (la función) y Telecom (la vertical). El consultor de telecom puede aplicar frameworks financieros generalistas, pero también conoce las particularidades del sector — los modelos de revenue assurance específicos de telecom, las regulaciones del regulador sectorial, los sistemas operacionales típicos de un operador. El conocimiento vertical es **adicional**, no sustituto, del conocimiento funcional.

El árbol de Capabilities refleja esta ortogonalidad. Un agente puede tener simultáneamente Capabilities de *Finance/Treasury* y de *Industrias verticales/Telecom* — y la combinación produce un agente que opera con saber funcional y vertical al mismo tiempo, exactamente como el consultor experto del sector.

Esta arquitectura tiene dos consecuencias importantes. La primera: **la especialización vertical no es prompt — es Capability**. Un "agente legal" o "agente médico" o "agente de telco" no es un prompt sofisticado del modelo general. Es un agente que carga la Capability vertical correspondiente, con su vocabulario, heurísticas y conocimiento normativo propio. Esto distingue Capabilities de System Prompts genéricos: el saber vertical es modular, persistente, y se compone con otras Capabilities no verticales sin contaminación.

La segunda consecuencia es comercial. Esta arquitectura explica el éxito comercial de los **especialistas verticales** del mercado actual: Cursor (coding), Harvey (legal), Jasper (marketing), Fin (customer support). Lo que estos productos venden no es "un GPT especializado" en su vertical — es una Capability vertical robusta que la cognición aplica con confianza. La diferencia con un GPT genérico no es marketing; es estructural. El usuario que prueba Cursor para programar no nota que la diferencia es la Capability *Coding* que la herramienta carga; nota que las respuestas son correctas más frecuentemente que con GPT genérico, y eso es exactamente lo que la Capability bien construida produce.

> *La Capability vertical es la diferencia entre un agente útil y un agente serio para el dominio.*

### Marketplace de Capabilities

Una propiedad emergente de la arquitectura es que las Capabilities admiten un **mercado**. Una Capability bien construida puede distribuirse entre AgencyDomains, versionarse y mantenerse por un proveedor especializado distinto del operador del AgencyDomain, cobrarse por suscripción o licencia, y auditarse por terceros respecto a su corrección y completitud.

Esto da forma a una **economía de Capabilities** análoga a la economía de paquetes de software open source. Quien construye y mantiene Capabilities expertas — por ejemplo *General Ledger* IFRS-compliant, o *Telecom 5G core* — puede operar como proveedor especializado sin construir agentes ni AgencyDomains propios. Su producto es la Capability misma. Su modelo de negocio es licencia o suscripción de la Capability. Sus clientes son organizaciones que operan AgencyDomains y necesitan saber-hacer profesional verificado.

La economía emergente tiene precedentes claros. La industria del software cuenta con economías similares de componentes especializados desde hace décadas: librerías compiladas que se venden o licencian, módulos certificados para frameworks específicos, configuraciones de mejores prácticas que las consultoras venden como activos. La economía de Capabilities sería evolución natural de esos modelos al campo agentivo.

La especificación normativa del **protocolo de Marketplace de Capabilities** — formato de paquete, modelo de versionado, sistema de firmas, modelo de cobro — es **trabajo abierto** en la versión 1.0 de este libro. Las implementaciones contemporáneas pueden adoptar paquetes ad-hoc; la consolidación como estándar de industria está pendiente. Cuando el consenso llegue, una versión futura del libro lo incorporará como spec normativa.

### Localidad y disponibilidad — clasificación operativa de Conectores

La descripción canónica anterior trata el saber-hacer como aplicable en cualquier contexto. La realidad operativa de sistemas con presencia física múltiple — restaurantes con locales, sucursales bancarias, tiendas de retail, plantas industriales — exige una clasificación adicional que la spec formaliza explícitamente: **localidad** y **disponibilidad offline**. La clasificación pertenece a los **Conectores** — la cara de Capa 4 del par que acompaña a la Capability —, porque lo que reside en un lugar y necesita (o no) red es el *acceso*, nunca el saber: la Capability que decide cuándo y cómo invocar no tiene localidad. Se documenta en este capítulo porque el par Capability–Conector se entrega y se razona junto. Sin esta clasificación, las decisiones de qué puede invocarse desde un Botlet edge en modo offline se hacen en la oscuridad.

La clasificación opera sobre **dos ejes ortogonales**:

#### Eje de localidad

Dónde residen físicamente los componentes del Conector:

- **Cloud-resident** — el Conector vive en un servicio remoto. Ejemplos canónicos: Conector `DTE-SII` (servicio del SII de Chile para emisión de boleta y factura electrónica), `Transbank-Onepay` (gateway bancario), `Stripe-Connect` (procesamiento de pagos). El agente los invoca por red; sin red no hay acceso.

- **Edge-resident** — el Conector vive en el sitio físico, asociado a hardware o sistemas locales. Ejemplos canónicos: Conector `ESC/POS-Printer` (impresora térmica de comandas y boletas con protocolo ESC/POS conectada por USB o serial), `Cash-Drawer` (gaveta de dinero del cajón), `Pinpad-Local` (pinpad de tarjetas conectado al POS), `Sensor-Temperatura` (sensor de cámara de frío conectado por GPIO). El agente los invoca contra el hardware del sitio; no necesitan red para operar.

- **Híbrido** — el Conector tiene un componente local y un componente cloud. Ejemplos canónicos: Conector `Cliente-DTE` (firma localmente el documento, lo encola si no hay red, lo envía al SII cuando vuelve la red), `Cliente-Pinpad-Procesamiento-Diferido` (autoriza localmente con clave PIN y batch, envía al adquirente cuando vuelve la red). La parte local opera offline; la parte cloud sincroniza cuando hay red.

#### Eje de disponibilidad offline

Si el Conector puede ejecutarse sin red:

- **Online-only** — requiere red para ejecutar. Sin red, la invocación falla. Los Conectores cloud-resident son típicamente online-only en el sentido estricto, aunque algunos tienen variantes con cliente local que los convierten en híbridos.

- **Offline-capable** — ejecuta sin red. Si su contrato externo exige eventualmente comunicación cloud (un comprobante que debe llegar al SII, una transacción que debe consolidarse en central), **encola** y emite hacia afuera cuando la red vuelve. Los Conectores edge-resident son típicamente offline-capable; los híbridos también lo son por diseño.

#### Matriz canónica de clasificación

Cada Conector conforme declara explícitamente su posición en la matriz:

|   | Online-only | Offline-capable |
|---|---|---|
| **Cloud-resident** | DTE-SII (sin cliente local) · Transbank Onepay · API meteorológica | (combinación inusual; típicamente migra a híbrido) |
| **Edge-resident** | (combinación inusual) | ESC/POS-Printer · Cash-Drawer · Sensor-Temperatura · Pinpad-Local |
| **Híbrido** | (combinación inusual) | Cliente-DTE · Cliente-Pinpad-Procesamiento-Diferido · Sync-Inventario |

#### Conexión con Capa 3 distribuida

La clasificación es necesaria estructuralmente cuando la Capa 3 está distribuida (Capítulo 5 §1). Un Botler edge debe **saber** qué Conectores puede invocar offline. Si no lo sabe, sus Botlets edge intentarán invocar Conectores cloud-resident sin red y fallarán catastróficamente — sin red, ni siquiera el fallback agéntico aplica, porque la cognición vive en cloud.

La regla operativa que la clasificación habilita es directa: **un Botlet edge senior, en un sitio físico sin red, opera invocando exclusivamente Conectores edge-resident y la parte local de Conectores híbridos**. Los cloud-resident y la parte cloud de los híbridos quedan inaccesibles temporalmente; los efectos diferidos (envío a SII, consolidación con central) se encolan; cuando la red vuelve, las colas drenan.

#### Propiedades exigidas

| Propiedad | Nivel | Descripción |
|---|---|---|
| Declaración explícita de localidad del Conector | **MUST** | Cloud-resident, edge-resident o híbrido. |
| Declaración explícita de disponibilidad offline | **MUST** | Online-only u offline-capable. |
| Especificación del comportamiento offline para offline-capable | **MUST** | Qué hace cuando no hay red, qué encola, cómo drena. |
| Resolución determinista del componente que se ejecuta en híbridos | **MUST** | Bajo qué condiciones corre el componente local; bajo cuáles invoca el cloud. |

### Portabilidad de la Capability

La sección anterior clasifica *dónde* reside físicamente el Conector que acompaña a la Capability — cloud, edge o híbrido. Una propiedad distinta, que la spec formaliza explícitamente, es la **portabilidad de la Capability**: una Capability conforme puede instalarse y ejecutarse en **cualquier AgencyDomain conforme**, sin reescritura. Esta portabilidad es lo que vuelve a la Capability **propiedad real del cliente** — no del AgencyDomain que la aloja, ni del hosting que sostiene a ese AgencyDomain.

El argumento es el mismo de no-lock-in que el canon hace para el AgencyDomain, aplicado un nivel más abajo. Así como un AgencyDomain conforme migra a otra plataforma hosting conforme sin quedar cautivo de ella, una Capability conforme migra a otro AgencyDomain conforme sin quedar cautiva de él. El cliente que adquiere una Capability adquiere un activo portable, no un alquiler atado a una plataforma.

#### ¿Las dos portabilidades?

Conviene no confundir dos portabilidades que operan en niveles distintos:

| Portabilidad | ¿Qué migra? | ¿Hacia dónde? |
|---|---|---|
| **Portabilidad del AgencyDomain** | El AgencyDomain completo | A otra plataforma hosting conforme |
| **Portabilidad de la Capability** | Una Capability | A otro AgencyDomain conforme |

#### ¿Cuál es la relación Capability ↔ AgencyDomain?

La relación es asimétrica y explícita: un **AgencyDomain aloja y ejecuta** Capabilities; una **Capability corre en** un AgencyDomain anfitrión. La Capability es habitante de primer orden de la Capa 2 del AgencyDomain — el saber-hacer que da cognición a sus agentes —, no un recurso de soporte. Esta es la razón por la que la definición canónica de AgencyDomain nombra a las Capabilities entre lo que el AgencyDomain aloja y ejecuta, a la par de los agentes autónomos y los Botlets.

### La certificación regulatoria reside en el componente certificado, no en el Botlet

Una propiedad estructural que aparece con fuerza en sistemas agentivos productivos en industrias reguladas — gastronomía, salud, finanzas, retail con DTE, farmacia, telecomunicaciones — y que la spec necesita formalizar explícitamente: **la certificación regulatoria de operaciones reside en el componente certificado que el Botlet invoca — el Conector certificado, con la Capability regulada que porta su saber normativo —, nunca en el Botlet que orquesta**. La separación es necesaria porque la naturaleza generada del Botlet hace imposible certificarlo a priori, y certificarlo a posteriori contradice su naturaleza regenerable.

#### El problema

El libro define que la cognición genera el código del Botlet (Capítulo 5 §2). Pero algunas operaciones que un Botlet ejecuta están **reguladas**: emisión de DTE bajo norma del SII, cobro con tarjeta bajo PCI-DSS, dispensación farmacéutica bajo registro sanitario, comunicación financiera bajo norma del regulador correspondiente. Para estas operaciones, **la regulación exige certificación del componente que ejecuta la operación**. Un sistema que emite boleta electrónica sin certificación SII no es legal; un sistema que cobra con tarjeta sin certificación PCI no puede operar.

Si la certificación residiera en el Botlet, cada Botlet que ejecuta una operación regulada tendría que ser certificado individualmente. Pero un Botlet es **código generado por la cognición** que se regenera cuando el ambiente cambia. Cada regeneración produciría un Botlet técnicamente distinto que requeriría re-certificación. La certificación regulatoria sobre Botlets convierte el ciclo `95/4/1` en imposibilidad operacional: cada cambio del 1% requeriría un proceso regulatorio.

#### La solución canónica

La spec resuelve la tensión separando responsabilidades con disciplina, y el reparto respeta la doctrina de capas del capítulo:

- **El Botlet orquesta.** Conoce el flujo del proceso, valida pre-condiciones operativas (¿hay productos?, ¿la mesa está abierta?, ¿el cliente tiene su RUT registrado?), captura el evento, formatea la solicitud según el contrato del componente certificado.
- **El Conector certificado ejecuta la operación regulada.** Recibe la solicitud del Botlet, ejecuta bajo todas las normas que aplican, devuelve el comprobante. El Conector `DTE-SII` recibe el detalle de la venta, firma con el certificado tributario, transmite al SII, recibe folio y timbre electrónico, devuelve el comprobante al Botlet. Es certificable precisamente porque es acceso estable, no saber generado.
- **La Capability regulada porta el saber normativo.** Qué exige la norma, cómo se interpreta, cuándo corresponde boleta y cuándo factura, qué hacer ante rechazo del regulador — el saber cognitivo con que la cognición decide y valida. Vive en Capa 2, se desarrolla con SME del dominio regulatorio, y acompaña al Conector como su par.

La separación tiene tres consecuencias estructurales:

**Primera, la certificación es del componente certificable.** El Conector `DTE-SII` puede certificarse formalmente — su código es estable, su contrato con el SII es explícito, su comportamiento es auditable. La certificación es trabajo único; vale para todos los Botlets que lo invoquen.

**Segunda, los Botlets generados conviven naturalmente con cumplimiento regulatorio.** Un Botlet `Cobrar-Mesa-9` que se regenera cuando la cocina cambia su menú no rompe la certificación tributaria — sigue invocando el mismo Conector `DTE-SII` certificado. La regeneración del Botlet afecta lógica de orquestación, no la operación regulada.

**Tercera, la frontera de auditoría queda nítida.** Cuando el regulador audita, el AgencyDomain expone: el Botlet (lógica de negocio, mutable, regenerable) y el componente certificado (operación regulada, congelada, auditable). La inspección regulatoria se concentra en el Conector certificado — donde la certificación reside —, mientras la lógica de negocio se gobierna con los mecanismos de Trust del Capítulo 5 §4 sin contradecirse con la regulación.

#### Patrón canónico

El patrón se aplica a cualquier industria regulada:

| Industria | Botlet (orquesta) | Componente certificado (ejecuta la operación regulada) |
|---|---|---|
| **Gastronomía** | `Cobrar-Mesa` | Conector `DTE-SII` (boleta o factura electrónica) |
| **Banca** | `Procesar-Pago` | Conector `Gateway-PCI-DSS` (tokenización + autorización) |
| **Farmacia** | `Dispensar-Receta` | Conector `Registro-Sanitario` (validación y registro de dispensación) |
| **Telecom** | `Activar-Servicio` | Conector `Registro-Subtel` (registro regulatorio de activación) |
| **Salud** | `Emitir-Prescripción` | Conector `MINSAL-Receta-Electrónica` (firma médica certificada) |

El patrón es uniforme: el Botlet contiene la lógica de negocio mutable; el componente certificado contiene la operación regulada congelada; la Capability regulada aporta el saber normativo con que la cognición gobierna el conjunto. La frontera entre ellos es la frontera entre lo que la organización puede regenerar libremente y lo que debe mantener bajo certificación.

#### Propiedades exigidas

| Propiedad | Nivel | Descripción |
|---|---|---|
| Componentes regulados declaran su régimen regulatorio | **MUST** | Qué norma cumple, ante qué regulador, con qué número de certificación. |
| Componentes certificados son inmutables entre auditorías | **MUST** | El código del Conector certificado no se regenera; cambia solo bajo proceso regulatorio. |
| Botlets pueden invocar componentes certificados sin restricción | **MUST** | El contrato del componente es estable; el Botlet lo invoca como cualquier otro. |
| Auditabilidad de la frontera | **MUST** | El log distingue claramente operaciones del Botlet (lógica de negocio) de operaciones del componente certificado (operación regulada). |

### Capabilities y Botlets — la relación

Capabilities y Botlets viven en capas distintas y resuelven problemas distintos, pero interactúan de manera estructurada. Capability vive en Capa 2 (Cognición). Es saber-hacer. Botlet vive en Capa 3 (Autonomía). Es hacer aprendido. Capability tiene forma de vocabulario más procedimientos más heurísticas más tools. Botlet tiene forma de código tradicional ejecutable. Capability es persistente y versionada. Botlet es auto-regenerable y efímero. Capability se aplica cuando el agente reconoce su dominio. Botlet se invoca cuando el agente reconoce el patrón. Capability es creada por humanos expertos o por proveedores especializados. Botlet es creado por la cognición del agente, automáticamente.

La interacción canónica es la siguiente: una Capability puede dar lugar a múltiples Botlets. El agente que aplica *General Ledger* repetidamente para una empresa específica empieza a generar Botlets que automatizan los pasos rutinarios del proceso — clasificar transacciones, conciliar cuentas, generar reportes mensuales — sin invocar la cognición. La Capability sigue siendo la misma; los Botlets son el residuo eficiente de su aplicación reiterada en un contexto particular.

Esta relación es lo que permite que el sistema agentivo escale económicamente. Las Capabilities son el saber estable que la organización adquiere, mantiene, evoluciona. Los Botlets son el residuo eficiente que la cognición genera al aplicar Capabilities reiteradamente en contextos específicos. La organización invierte en Capabilities; los Botlets emergen del uso. La inversión en saber genera ahorro en operación.

### Conformidad

Una implementación de Capabilities conforme a esta especificación debe satisfacer los siguientes requisitos:

| Requisito | Nivel |
|---|---|
| Estructura jerárquica en árbol | **MUST** |
| Cualquier nodo es Capability válida | **MUST** |
| Composabilidad entre Capabilities | **MUST** |
| Anatomía con vocabulario + procedimental + declarativo + heurísticas | **MUST** |
| Versionado explícito | **MUST** |
| Estado de madurez declarado (Borrador / Vigente / Deprecado) | **MUST** |
| Selección por la cognición, no ejecución directa | **MUST** |
| Verticales como raíz dedicada | **SHOULD** |
| Marketplace abierto | **MAY** (cuando la spec normativa exista) |
| Declaración explícita de localidad del Conector acompañante (cloud / edge / híbrido) | **MUST** |
| Declaración explícita de disponibilidad offline | **MUST** |
| Portabilidad entre AgencyDomains conformes | **MUST** |
| Componentes regulados (Capability normativa + Conector certificado): régimen declarado | **MUST** |
| Conectores certificados: inmutabilidad entre auditorías | **MUST** |

### Frontera de evolución

Tres áreas activas de evolución de la primitiva Capability merecen mención.

El **marketplace de Capabilities** es la primera. El protocolo normativo aún no está consolidado; cuando lo esté, la versión 2.0 de este libro lo incorporará.

Las **Capabilities cross-vertical** son la segunda. Cómo una Capability puede combinarse con verticales múltiples sin contradicciones — un agente que opera en finanzas para banca y para telecom simultáneamente, por ejemplo — exige refinamiento de los mecanismos de herencia que la versión 1.0 de la spec describe.

La **auditoría de Capabilities** es la tercera. Cómo certificar que una Capability hace lo que dice hacer — que una Capability *IFRS Compliance* efectivamente refleja IFRS y no su aproximación informal — es problema de gobernanza que el campo aún no resuelve. Las soluciones probables vendrán del lado de la auditoría profesional tradicional adaptada al contexto agentivo.
