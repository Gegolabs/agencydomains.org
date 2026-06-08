# Capítulo 5 · Primitivas

Las cuatro capas del Capítulo 4 son la respuesta arquitectónica al paradigma, pero no se sostienen solas: necesitan piezas reusables que las pueblen. Este capítulo entrega esas piezas — las **primitivas técnicas canónicas** del Mundo Agentivo. Cada sección formaliza una: el **AgencyDomain** (§1), el **Botlet** con su **proto-Botlet** (§2), la **Capability** (§3), la **Trust Infrastructure** (§4), la distinción **Asistente vs Agente Autónomo** (§5) y la **Faceta** (§6).

## AgencyDomains

El Capítulo 4 introdujo la noción del AgencyDomain como construcción formal donde se materializa la Arquitectura Agentiva. Esta sección desarrolla esa noción con el detalle de una especificación. Lo que sigue es lo más cercano a una *spec normativa* que este libro entrega — un documento que un implementador puede tomar y construir, sabiendo qué es obligatorio y qué es opcional, qué propiedades debe satisfacer y qué decisiones puede tomar libremente.

### Premisa fundacional — Space ≠ Domain

Las palabras cargan corporeidad. **Space** (*espacio*, en inglés) nace describiendo extensión física: oficina, escritorio, hogar, ciudad. Cuando un humano dice *"mi espacio"*, invoca lugar — coordenadas, paredes, presencia. La industria del software empresarial extendió la palabra a **WorkSpace** (*espacio de trabajo*) — Google Workspace, Microsoft 365, Notion — para nombrar la colección de soluciones que digitalizan lo que la persona hace en su escritorio físico: leer email, agendar reuniones, escribir documentos, archivar. WorkSpace es la prótesis digital del Space humano; ambos términos cargan la misma corporeidad de origen.

El agente no tiene cuerpo. No abre aplicaciones. No trabaja sobre un escritorio. No habita en un espacio físico ni en metáfora de él: ejerce agencia sobre un **ámbito de jurisdicción computacional** — territorio digital donde su identidad rige, sus Capabilities aplican y sus Botlets corren. La palabra latina que nombra exactamente eso es **Domain** (`dominium`: ámbito de pertenencia y soberanía).

> **Donde el humano tiene Space (WorkSpace), el agente tiene Domain (AgencyDomain).**

### El paralelo histórico — JSR-000148

El paralelo histórico se conserva: como **JavaSpaces** (JSR-000148, 1999) formalizó los espacios distribuidos para sistemas Java sin atar la implementación a un proveedor, esta especificación formaliza los **AgencyDomains** para sistemas agentivos con la misma agnosticidad. Múltiples implementaciones surgieron sobre JavaSpaces — GigaSpaces, Blitz, otras —, todas compatibles entre sí porque respetaban el contrato común. La spec sobrevivió a las implementaciones; las implementaciones evolucionaron sin que la spec necesitara reescritura constante. Ese es el patrón que **AgencyDomains** busca replicar para el campo agentivo. Este libro propone la spec; las implementaciones que cumplan con ella podrán llamarse **AgencyDomain conforme**.

La diferencia de nombre con su predecesor no es ruptura — es precisión. Un Java *Space* (*espacio*) era espacio computacional para procesos sin cuerpo; un Agency *Domain* (*dominio, ámbito*) es ámbito de jurisdicción para agentes con agencia. Lo que en 1999 se nombraba como "espacio" se nombra mejor en 2026 como "domain". El término **AgencyDomain** carga sentido en cada palabra. *Agency* — agencia, en su sentido filosófico de capacidad de actuar — denota que el ámbito es habitado por entidades con iniciativa propia, no por procesos pasivos. *Domain* — `dominium`: ámbito de pertenencia y soberanía — denota territorio donde la identidad del agente rige, no proceso efímero. La unión de las dos palabras nombra exactamente lo que la spec define: un ámbito donde el agente ejerce agencia.

> Nota terminológica: en lore comercial (marca, ventas, comunicación cliente) la forma corta `Domain` reemplaza a `AgencyDomain`. Es el patrón Apple iCloud / CloudKit, Stripe Connect / Account: marca corta + nombre técnico largo. Las dos formas son intercambiables; cada registro elige la suya.

### Definición

Un **AgencyDomain** es un espacio computacional con identidad propia donde habitan agentes autónomos y Botlets en ejecución, donde se alojan y ejecutan las **Capabilities** que les dan el saber-hacer, y donde viven los recursos que los sostienen — cognición, tools, almacenamiento persistente. Constituye la **unidad mínima de despliegue** de un sistema agentivo productivo.

La Capability no es recurso de soporte: es saber-hacer cognitivo, habitante de primer orden del espacio junto al agente y al Botlet. La relación entre las dos primitivas es directa — un AgencyDomain **aloja y ejecuta** Capabilities; una Capability **corre en** un AgencyDomain anfitrión.

La spec define cómo deben construirse esos espacios — capas, identidad, ciclos de vida, protocolos de comunicación — sin prescribir una implementación específica. Múltiples implementaciones son admisibles siempre que respeten el contrato. Una implementación puede usar Kubernetes para contenerización; otra puede usar microVMs aisladas; otra puede usar procesos nativos en una sola máquina. Las tres son válidas si satisfacen las propiedades fundamentales que la spec exige.

> *Donde un agente vive, ese lugar es un AgencyDomain. Donde no hay AgencyDomain, no hay vida del agente — hay invocación de modelo.*

La cita anterior distingue al AgencyDomain conforme a esta especificación de cualquier "endpoint que invoca un LLM". Un endpoint que invoca un LLM responde a peticiones; un AgencyDomain **hospeda agentes que viven**. La diferencia es estructural, no de grado. Un sistema sin estado persistente, sin Botlets propios, sin capacidad de operación proactiva, no es AgencyDomain — es servicio. Puede ser servicio útil, pero no satisface lo que el campo agentivo requiere.

La unidad mínima importa. Un AgencyDomain no es subcomponente de algo más grande — es la unidad atómica del despliegue. Un sistema agentivo más grande es una colección de AgencyDomains que cooperan, posiblemente bajo un mismo gobierno o federados entre dueños distintos, pero cada uno conserva su identidad propia y sus propiedades fundamentales.

### Propiedades fundamentales

Toda implementación que pretenda llamarse AgencyDomain conforme a esta spec debe satisfacer cinco propiedades fundamentales. La satisfacción no es opcional — un sistema que no las cumple no es AgencyDomain, sino otra cosa con otro nombre.

La primera propiedad es **identidad propia**. Cada AgencyDomain tiene una identidad única — una URI canónica — que lo distingue en cualquier red. La identidad sobrevive al reinicio del espacio, a la migración entre infraestructuras y al cambio de implementación. Si un AgencyDomain migra de un cloud provider a otro, su identidad no cambia: los agentes que lo habitan, los humanos que interactúan con él, los otros AgencyDomains que lo invocan, todos siguen reconociéndolo como el mismo espacio. La identidad es estable, no efímera.

La segunda propiedad es **materialización de las cuatro capas**. Un AgencyDomain materializa las cuatro capas de la Arquitectura Agentiva — Interacción, Cognición, Autonomía, Acceso — y ejerce Trust Infrastructure transversal. La materialización puede distribuirse técnicamente — las capas pueden vivir en infraestructuras distintas, en servidores físicos distintos, hasta en proveedores cloud distintos —, pero la responsabilidad por las cuatro recae en el espacio. No hay AgencyDomain conforme que entregue solo tres capas, o que delegue alguna capa a un sistema externo sin asumir responsabilidad sobre ella. La completitud es no-negociable.

La tercera propiedad es **persistencia**. El estado del AgencyDomain — agentes activos, Botlets en ejecución, datos de capabilities, logs de auditoría — sobrevive a desconexiones, reinicios y migraciones. Un AgencyDomain no es proceso efímero; es entidad persistente. Si el sistema se reinicia por mantenimiento, los agentes que estaban activos continúan donde estaban. Si la conexión a un servicio externo se cae temporalmente, el agente espera y reanuda. La persistencia es lo que hace al AgencyDomain **lugar** y no proceso.

La cuarta propiedad es **aislamiento**. Cada AgencyDomain tiene un límite explícito. Recursos internos — cómputo, memoria, datos — no son accesibles desde fuera salvo por interfaces definidas. La comunicación con el exterior pasa por la Capa 4 (Acceso) y queda registrada. El aislamiento no es solo seguridad — es **contención de fallos**: un AgencyDomain que se cae no afecta a otros AgencyDomains que comparten infraestructura, porque el límite contiene la falla. Los modelos de implementación que ofrecen aislamiento varían — desde sandboxing fuerte vía MicroVMs hasta aislamiento más liviano vía namespaces de Kubernetes —, pero el límite explícito existe siempre.

La quinta propiedad es **direccionabilidad**. Tanto el AgencyDomain como los agentes y Botlets que lo habitan son direccionables vía URLs predecibles. La sintaxis canónica que la spec adopta es:

```
{domain}/                          → el espacio mismo
{domain}/agents/{agent}            → un agente que vive en él
{domain}/agents/{agent}/botlets/{botlet}   → un Botlet específico
{domain}/tools/{tool}              → un tool expuesto vía Capa 4
```

La direccionabilidad importa por dos razones operativas. Primera, es la base de la comunicación A2A — un agente que necesita invocar a otro agente lo hace a través de su URL canónica, sin necesidad de descubrimiento ad hoc. Segunda, es la base del MEO (Model Engine Optimization) — los modelos frontera que aprenden a referenciar AgencyDomains los hacen a través de URLs predecibles que aparecen en su corpus de entrenamiento. URLs caóticas o inestables hacen al AgencyDomain invisible para los modelos que no fueron entrenados con su mapa específico.

### Modelo de datos canónico

<!-- FIG:g17-anatomia-agencydomain -->
![Anatomía del AgencyDomain](figuras/g17-anatomia-agencydomain.png)

La estructura interna de un AgencyDomain conforme sigue un modelo canónico que la spec define con precisión (figura arriba).

Cada componente del modelo tiene su rol específico. **Identity** mantiene la información que identifica el espacio frente al mundo: su URI canónica, las credenciales con las que se autentica frente a sistemas externos, las políticas raíz que ningún agente puede contravenir. **Agents** es la colección de agentes que viven en el espacio, cada uno con sus Capabilities asignadas, sus Botlets en ejecución y su estado persistente. **Capabilities Registry** es el árbol de capabilities disponibles para los agentes del espacio — saber-hacer compartido que los agentes pueden invocar según su rol. **Tools Registry** es la colección de tools que la Capa 4 expone hacia el exterior — la interfaz por la cual el AgencyDomain toca sistemas externos. **Trust Layer** ejerce gobernanza y auditoría transversales — políticas, log append-only, mecanismos de validación. **Cognition Bindings** son los bindings al recurso cognitivo — qué proveedor de modelo invoca el AgencyDomain, bajo qué credenciales, con qué políticas de uso.

La noción de **Cuenta** es concepto comercial superpuesto al modelo técnico. Una Cuenta puede poseer múltiples AgencyDomains. La spec trata la Cuenta como entidad opaca; cada implementación define su semántica específica — una empresa cliente, una organización federada, un usuario individual. La distinción entre AgencyDomain (técnico) y Cuenta (comercial) es importante porque permite que el modelo técnico evolucione sin que el modelo comercial necesite reescritura cada vez.

### El modelo de regímenes

<!-- FIG:g18-tres-regimenes -->
![Los tres regímenes · privado · público · híbrido](figuras/g18-tres-regimenes.png)

Un aspecto que distingue significativamente a la spec de AgencyDomains respecto a soluciones agentivas más limitadas es el reconocimiento de tres **regímenes** posibles de un AgencyDomain, análogos a los regímenes del cómputo en la nube. Los tres regímenes son técnicamente equivalentes en su estructura interna; lo que cambia entre ellos es la **frontera de acceso**, no la arquitectura.

El **régimen privado** corresponde a un AgencyDomain donde el espacio y todos sus componentes viven dentro de un perímetro controlado por una organización. No hay acceso público. Los agentes del espacio son invocables solo desde dentro de la organización. Los datos del espacio no salen del perímetro. Es análogo conceptual al Private Cloud — la organización tiene el control total de sus recursos, paga por ese control en términos de operación pero gana en términos de soberanía. El régimen privado es típico para casos donde la organización opera datos sensibles o cumple regulación que exige residencia local.

El **régimen público** corresponde a un AgencyDomain accesible públicamente. Agentes, Botlets y tools son invocables desde fuera del perímetro. El AgencyDomain tiene una URL pública y los agentes que lo habitan están registrados en un directorio que cualquier sistema externo puede consultar. Es análogo conceptual al Public Cloud — máxima accesibilidad, máxima exposición, modelo de operación distinto. El régimen público es donde la red de agentes coopera abiertamente con el resto de internet.

El **régimen híbrido** es combinación de los dos anteriores. Un AgencyDomain híbrido tiene componentes en perímetro privado y componentes accesibles públicamente vía proxy. Los datos sensibles permanecen privados, pero la interfaz que expone capacidades al exterior está disponible públicamente. Es análogo conceptual al Hybrid Cloud — la organización elige qué exponer y qué retener, balanceando soberanía y accesibilidad. El régimen híbrido es típico para organizaciones que necesitan ofrecer agentes públicos a sus clientes pero quieren mantener los datos del cliente dentro del perímetro corporativo.

Lo crítico de esta arquitectura de regímenes — y es propiedad fuerte de la spec — es que **la estructura técnica del AgencyDomain es la misma en los tres regímenes**. Un agente que opera en un AgencyDomain privado es técnicamente equivalente a uno que opera en uno público; lo que cambia es el régimen, no la capacidad. Un Botlet que ejecuta en privado puede mover ese mismo código a un régimen público sin reescritura. Esta uniformidad estructural habilita la **migración natural** entre regímenes — un agente puede graduarse de privado a público o viceversa sin cambiar su lógica interna. La organización gobierna el régimen; la lógica del agente no se entera.

Esta propiedad de migración natural es estructuralmente importante porque desacopla la decisión arquitectónica (cómo se construye el agente) de la decisión comercial (en qué régimen se opera). Una organización puede empezar construyendo agentes en régimen privado mientras valida su utilidad, y migrarlos a régimen público o híbrido cuando la madurez lo justifique. La inversión arquitectónica inicial no se pierde en la transición.

Para fijar la idea con instancias concretas a mayo de 2026: Agentia opera AgencyDomains en régimen privado para firmas que mantienen sus agentes dentro del perímetro corporativo; Soveria opera AgencyDomains en régimen público donde agentes habilitados se hospedan con identidad pública y URL canónica; un mismo agente puede graduarse del primero al segundo sin reescritura técnica, manteniendo intacta la spec del agente y mudando sólo el régimen.

### Modelos de acceso a la cognición

La spec reconoce dos modos coexistentes mediante los cuales los componentes del AgencyDomain acceden al recurso cognitivo (Capa 2). Los dos modos coexisten porque resuelven problemas distintos, y un AgencyDomain serio típicamente opera ambos simultáneamente para distintos componentes.

El primer modo es **Tokens**. El flujo es: AgencyDomain → recurso cognitivo, centralizado y facturado al espacio. El AgencyDomain centraliza credenciales, facturación y políticas. Provee acceso cognitivo a todos sus componentes activos. Este modo aplica cuando los agentes deben operar en background sin intervención del usuario, cuando la organización desea control central sobre consumo y costos, o cuando múltiples agentes comparten un mismo proveedor de cognición. La organización que opera Agentes Autónomos en background — agentes que monitorean continuamente, responden a eventos, ejecutan tareas asíncronas — necesita Tokens, porque no hay un humano disponible cuya suscripción individual subsidie las invocaciones.

El segundo modo es **Suscripción**. El flujo es: Asistente del usuario → recurso cognitivo, vía la suscripción del propio usuario. El asistente con el cual el usuario interactúa — Claude, ChatGPT, Copilot, Gemini — accede directamente al recurso cognitivo bajo la suscripción del usuario. El AgencyDomain no consume tokens del recurso. Este modo aplica cuando el usuario ya tiene una suscripción activa al proveedor de cognición, cuando el AgencyDomain expone tools y datos al asistente del usuario sin centralizar la cognición, o cuando la economía operativa del AgencyDomain privilegia minimizar costos de inferencia. La organización que adopta ultraPRO — el integrador seguro entre el agente del usuario y los sistemas corporativos — opera típicamente en modo Suscripción, porque los usuarios traen sus propias suscripciones a los proveedores de cognición.

Ambos modos coexisten en sistemas maduros. Un mismo AgencyDomain puede operar Asistentes del usuario (modo Suscripción) y Agentes Autónomos en background (modo Tokens), simultáneamente. La spec exige que el AgencyDomain **declare explícitamente** qué modo aplica a qué componente. La declaración explícita previene la fuente más recurrente de errores económicos en sistemas agentivos: confusión accidental entre modos, donde un Agente Autónomo que debería operar en Tokens termina facturando contra la suscripción del usuario y la agota en horas, o donde un Asistente que debería operar en Suscripción termina facturando contra el AgencyDomain y consume tokens que no debería.

El rol de los Botlets en la economía cognitiva merece énfasis particular. En planes de Suscripción fija, los Botlets son el mecanismo para lograr autonomía sin costo adicional: el ciclo `95/4/1` de los Botlets es la base económica de la autonomía bajo suscripción. El desarrollo completo de esta economía vive en §2 (ver §2).

### Ciclo de vida del agente

Un AgencyDomain conforme a la spec gestiona el ciclo de vida completo de cada agente que habita en él. El ciclo tiene seis fases canónicas, y cada transición entre fases queda registrada en el append-only log del Trust Layer.

La fase de **provisioning** es donde el AgencyDomain crea el agente. Asigna identidad, asocia las Capabilities iniciales que el agente puede invocar, registra al agente en el espacio. El agente nace, en términos del sistema, cuando esta fase termina exitosamente. Si la fase falla — por error de credenciales, por conflicto de nombre, por restricciones de cuota —, el agente nunca llega a existir.

La fase de **bootstrap** es donde el agente entra en operación. Carga su estado persistente si existe — si el agente había sido hibernado o reiniciado, recupera su contexto previo. Establece bindings con la cognición y los tools que va a usar. Verifica que sus Capabilities estén disponibles. Después de bootstrap, el agente está listo para responder o para operar proactivamente, según su modo.

La fase de **operación reactiva** corresponde al agente operando en modo Asistente. Capa 2 activa. El agente responde a solicitudes del humano: cada solicitud llega, el agente la procesa invocando cognición y posiblemente Capabilities, devuelve respuesta. Entre solicitudes, el agente está pasivo — no consume cómputo activo, no ejecuta nada. Esta fase es la más frecuente en sistemas que operan principalmente con Asistentes.

La fase de **operación proactiva** corresponde al agente operando en modo Agente Autónomo. Capa 3 activa. El agente persigue objetivos en background, monitorea eventos, ejecuta Botlets cuando corresponde, escala al humano cuando los umbrales lo exigen. Pattern Recognition genera y mantiene Botlets a medida que el agente identifica patrones repetitivos. Esta fase es donde se materializa el modelo *"la inteligencia va hacia las personas y actúa en su nombre"* — el agente está activo continuamente, el humano interviene solo cuando es necesario.

La fase de **hibernación** es donde el agente queda en pausa pero persistente. Estado guardado. No consume cómputo activo. Esta fase es útil cuando un agente no necesita operar durante períodos extendidos — un agente de soporte que solo opera durante horario hábil, por ejemplo, hiberna durante la noche y se reactiva con el inicio del día siguiente. La hibernación preserva el contexto sin gastar recursos.

La fase de **decommissioning** es donde el AgencyDomain retira al agente. El estado del agente se archiva o se elimina según política. Las Capabilities que tenía asignadas se liberan. La identidad del agente queda registrada en el log histórico, pero el agente deja de existir como entidad operativa. La fase de decommissioning es importante porque cierra el ciclo formalmente — un agente "decommissioned" no es lo mismo que un agente "olvidado". El registro del decommissioning es lo que permite, semanas o meses después, reconstruir auditablemente que el agente existió, qué hizo, y por qué dejó de existir.

### Comunicación entre agentes

La spec reserva el término **A2A** (`agent-to-agent`) para la *relación* entre agentes, y un agente es un AgencyDomain. La relación A2A es, por tanto, **entre AgencyDomains** — entre agentes distintos, cada uno con su propia identidad y agencia. La comunicación dentro de un mismo AgencyDomain no es A2A en este sentido relacional: los componentes que la sostienen son runtimes del mismo agente, no agentes distintos. La spec distingue así dos planos: el plano **intra-AgencyDomain** (un agente comandando sus propios runtimes y memoria muscular) y el plano **A2A** (un agente invocando a otro agente). Cuando dentro de un AgencyDomain se usa el **protocolo `A2A`** como transporte entre runtimes, se dice **vía el protocolo `A2A`** — el nombre propio del protocolo —, nunca "A2A interna", para no atribuir agencia a runtimes que no la tienen.

#### ¿Cómo comanda la Cognición a su memoria muscular? — interfaz Capa 2 ↔ Capa 3

La **Cognición** (el agente `LLM`, Capa 2) comanda su propia memoria muscular — el **Botler**, runtime de Capa 3 sin agencia — por una interfaz **interna** dentro del mismo AgencyDomain. Es la relación Capa 2 → Capa 3: la Cognición especializa, manifiesta, consume y controla los Botlets que el Botler hospeda. El transporte natural de esta interfaz es **`MCP`** (`LLM`↔herramienta): el Botler expone uno o más servidores `MCP` y la Cognición es el cliente. Esta interfaz **no es `A2A`** — no cruza la frontera del AgencyDomain ni media entre agentes distintos; es un agente operando su propio sustrato de ejecución. `A2A` queda reservado para AgencyDomain↔AgencyDomain.

<!-- FIG:g19-interfaz-capa2-capa3-mcp -->
![Interfaz Capa 2 → Capa 3 vía MCP — interna, no A2A](figuras/g19-interfaz-capa2-capa3-mcp.png)

#### ¿Qué propiedades exige la comunicación intra-AgencyDomain?

Toda comunicación entre componentes que viven **en el mismo AgencyDomain** — sea la interfaz Capa 2 → Capa 3 vía `MCP`, sea el transporte entre Botlers vía el protocolo `A2A` — satisface tres propiedades que la spec exige. La primera es **direccionabilidad uniforme** — cualquier componente del espacio puede ser invocado por su URI canónica, sin necesidad de descubrimiento ad hoc. La segunda es **tipado de mensajes** — los mensajes tienen schema declarativo verificable; quien emite declara el schema y quien recibe verifica que el mensaje lo cumple antes de procesarlo. La tercera es **trazabilidad** — toda invocación queda registrada en el append-only log con identidad de emisor y receptor. Si un componente invocó a otro, el sistema sabe quién, cuándo y con qué contenido.

#### ¿Cómo se comunican agentes distintos? — A2A entre AgencyDomains

La **comunicación `A2A` entre AgencyDomains** es entre agentes que viven **en AgencyDomains distintos**. Esta modalidad requiere protocolos adicionales que la spec reconoce como necesarios pero no completamente normaliza en su versión 1.0. Los protocolos abiertos para `A2A` están en evolución — la industria está convergiendo hacia ciertas direcciones, pero el consenso completo no ha llegado. Lo que la spec sí define es que el `A2A` entre AgencyDomains requiere tres mecanismos: **descubrimiento** — cómo un AgencyDomain publica los agentes que ofrece para ser invocados externamente; **autenticación cruzada** — cómo dos AgencyDomains verifican identidad mutuamente; **resolución semántica** — cómo dos AgencyDomains que pueden tener glosarios distintos negocian el significado de tools y capabilities cuando interoperan.

La especificación normativa completa del `A2A` entre AgencyDomains — protocolo de descubrimiento, formato de mensajes federados, resolución de identidad — es **trabajo abierto**. Implementaciones de referencia pueden adoptar protocolos emergentes, por ejemplo `MCP` federado, o el protocolo `A2A` propuesto por **Google**. Cuando exista consenso de industria sobre un protocolo específico, una versión futura de esta spec lo incorporará como normativo. Por ahora, las implementaciones serias tratan el `A2A` entre AgencyDomains como capacidad emergente, no como spec consolidada.

### Federación entre AgencyDomains

<!-- FIG:g20-federacion-vs-cluster -->
![Federación vs. Cluster · distinción crítica](figuras/g20-federacion-vs-cluster.png)

La **federación** es el mecanismo formal mediante el cual múltiples AgencyDomains colaboran como red. Hay que distinguirla del concepto cercano pero distinto del **Cluster** — múltiples instancias del mismo AgencyDomain operando como conjunto coordinado. Cluster es operacional; Federación es arquitectónica.

| Concepto | Granularidad | Ejemplo |
|---|---|---|
| **Cluster** | Múltiples instancias del **mismo** AgencyDomain | Tres instancias de un AgencyDomain de la misma firma compartiendo carga |
| **Federación** | Múltiples AgencyDomains **distintos** colaborando | El AgencyDomain de la firma A invoca un agente del AgencyDomain de la firma B |

La federación habilita ecosistemas de agentes que cruzan límites organizacionales. Un AgencyDomain puede invocar agentes de otro AgencyDomain, intercambiar datos, coordinar operaciones — todo bajo modelos de confianza explícitos que cada participante establece. Esto extiende el modelo agentivo más allá de los límites de una organización individual y permite redes de cooperación que se asemejan más a internet abierta que a sistemas corporativos cerrados.

La especificación normativa de federación es trabajo abierto. La versión 1.0 de la spec reconoce los mecanismos necesarios sin prescribir su implementación específica:

Un **protocolo de descubrimiento abierto** debe existir, posiblemente sobre DNS y bien-conocidos. Cuando un AgencyDomain quiere descubrir qué agentes ofrece otro AgencyDomain, debe poder consultar un endpoint estándar y obtener la lista. La spec no prescribe el formato exacto del endpoint — esa decisión depende del consenso de industria que aún no ha llegado.

**Estándares de identidad criptográfica** para AgencyDomains y agentes son necesarios. Cada AgencyDomain federado debe poder autenticarse criptográficamente — no por API key compartida, sino por mecanismo verificable que no requiere autoridad central. Las tecnologías candidatas incluyen DIDs (Decentralized Identifiers) del W3C, certificados X.509, mecanismos basados en blockchain. La spec admite cualquiera que satisfaga la propiedad fundamental: identidad verificable sin autoridad central.

**Modelos de confianza explícitos** son requisito. Cuando dos AgencyDomains interactúan, cada uno debe declarar el nivel de confianza que extiende al otro: qué operaciones permite, qué datos comparte, qué auditoría ejerce. La confianza no es binaria — un AgencyDomain puede confiar en otro para invocaciones de bajo impacto pero no para alto, o puede confiar para lectura pero no para escritura. La spec exige que estos modelos sean explícitos y configurables, no implícitos en código.

**Resolución de conflictos** cuando dos AgencyDomains aplican políticas contradictorias. Si el AgencyDomain A invoca a un agente del AgencyDomain B, y las políticas de A y B tienen conflictos — A permite la operación pero B la prohíbe, por ejemplo —, debe haber mecanismo claro para resolver el conflicto. La spec define que la prioridad es siempre del AgencyDomain receptor — es decir, B en este caso. El emisor puede pedir; el receptor decide.

### Capa 3 distribuida — patrón canónico para presencia física múltiple

<!-- FIG:g21-capa3-distribuida -->
![Capa 3 distribuida · Botler central + N Botlers edge](figuras/g21-capa3-distribuida.png)

La Capa 4 del Capítulo 4 anticipó que las cuatro capas pueden distribuirse técnicamente en infraestructuras distintas. Esta sección formaliza el caso particular más frecuente y operacionalmente importante: la **distribución geográfica de la Capa 3** dentro de un mismo AgencyDomain. El patrón resuelve un escenario que cualquier organización con sucursales físicas múltiples encuentra invariablemente — gastronomía multilocal, retail con cadena de tiendas, logística distribuida, salud con red de centros, banca con sucursales, plantas industriales con líneas de producción simultáneas. Sin formalización, cada implementador reinventa el patrón con vocabulario propio y lo trata como excepción al modelo. Con formalización, queda como **patrón canónico** que cualquier implementación seria debe contemplar.

La distinción esencial es entre **distribución interna** y **federación externa**. La distribución interna ocurre cuando un mismo AgencyDomain divide su Capa 3 entre múltiples nodos físicos coordinados — un Botler central y N Botlers edge —, manteniendo identidad única, gobierno único, log único y modelo de datos único. La federación externa ocurre entre AgencyDomains distintos, cada uno con su identidad y gobierno propios. Cluster es un caso intermedio (mismo AgencyDomain, mismas instancias compartiendo carga). La distribución de Capa 3 es Cluster en términos de identidad — todos los Botlers pertenecen al mismo AgencyDomain — con la complicación adicional de que los Botlers no son intercambiables: cada Botler edge es responsable de un sitio físico específico.

#### Tres piezas del patrón

El patrón canónico distingue tres piezas con responsabilidades distintas:

**1. Botler central.** Hospeda los Botlets de orquestación, planificación, reportería, decisiones globales. Vive típicamente en cloud. Tiene visión consolidada del estado de todos los nodos edge. Ejecuta operaciones que requieren atravesar varios sitios — consolidar inventario, conciliar caja del día, planificar la operación del día siguiente, enviar reportes regulatorios consolidados. Mantiene la BD consolidada y el log de auditoría unificado. Comunica con la cognición (Capa 2) para escalamientos y decisiones nuevas.

**2. Botlers edge.** Uno por cada sitio físico. Hospedan los Botlets transaccionales locales — los que ejecutan la operación cotidiana del sitio: tomar pedidos, cobrar, emitir comprobantes, gestionar inventario local, controlar dispositivos físicos (pinpads, impresoras, sensores). Cada Botler edge mantiene una BD local con el estado del sitio y una **cola de eventos hacia central** que sincroniza cuando hay red. Operan con autonomía total cuando la red está disponible y con autonomía local cuando la red se cae — el sitio sigue operando contra su BD local; los eventos se acumulan en cola; cuando la red vuelve, la cola drena y la consolidación con el central se reanuda.

**3. Coordinación entre Botlers vía el protocolo `A2A`.** Los Botlers central y edge se comunican **vía el protocolo `A2A`** — el nombre propio del protocolo de coordinación. No es `A2A` en sentido relacional: estos Botlers son runtimes del mismo agente — el mismo AgencyDomain —, no agentes distintos, de modo que la coordinación entre ellos es comunicación **intra-AgencyDomain**, no `A2A` entre AgencyDomains. La conversación atraviesa la red corporativa pero **no atraviesa la federación** — está enteramente dentro de un solo AgencyDomain. La distinción no es retórica: el régimen de Trust Infrastructure es el del AgencyDomain único, no el de federación entre AgencyDomains; el log es unificado; el modelo de identidad es interno; las políticas se aplican uniformemente.


#### Modo offline como propiedad emergente

Bajo la topología paralela del Capítulo 4 + el patrón de Capa 3 distribuida, el **modo offline** de un sitio físico emerge como **propiedad estructural del sistema**, no como capacidad especial que requiere construcción separada. Cuando la red se cae en un sitio, dos cosas ocurren simultáneamente: la vía Cognición queda inactiva (la Capa 2 vive en cloud y no es accesible), y el Botler central tampoco es accesible. Pero el Botler edge sigue activo: sus Botlets corren contra la BD local, las Capabilities edge-resident (impresora ESC/POS, gaveta, pinpad) siguen disponibles, la operación cotidiana del sitio continúa. La cola de eventos hacia central acumula transacciones pendientes; cuando la red vuelve, drena y consolida.

La condición para que el modo offline opere correctamente es que los Botlets edge sean **senior** en términos de la propuesta de madurez (sección §2): Botlets que ya incorporaron las variantes del ambiente y operan con ratio cercano a `99+ / <1 / ~0`. Un Botlet edge en fase junior — todavía descubriendo variantes — no puede operar sin la posibilidad de fallback a cognición. Un Botlet edge senior sí puede, porque sus únicos modos de fallo son exógenos (energía, hardware, red catastrófica), no aprendizaje pendiente.

#### Propiedades exigidas del patrón

Una implementación de AgencyDomain con Capa 3 distribuida debe satisfacer:

| Propiedad | Nivel | Descripción |
|---|---|---|
| Identidad única del AgencyDomain | **MUST** | Todos los Botlers (central + edge) pertenecen al mismo AgencyDomain con una sola URI canónica. |
| BD local en cada Botler edge | **MUST** | Estado operativo del sitio físico, accesible sin red. |
| Cola de eventos hacia central | **MUST** | Mecanismo de sincronización eventual; transacciones pendientes drenan cuando hay red. |
| Resolución de conflictos en consolidación | **MUST** | Cuando un evento desde edge llega a central y entra en conflicto con el estado consolidado, política explícita decide. |
| Log de auditoría unificado | **MUST** | Un solo append-only log para todo el AgencyDomain, alimentado por todos los Botlers. |
| Modelo de identidad interno único | **MUST** | Los Botlers no se autentican como AgencyDomains externos entre sí; comparten el modelo de identidad del AgencyDomain. |
| Régimen Trust uniforme | **MUST** | Las políticas se aplican igual en central y edge; no hay régimen especial para edge. |
| Capacidad de operación offline en edge | **SHOULD** | Cuando los Botlets edge son senior, el sitio opera con red intermitente o sin red. |

### Portabilidad del AgencyDomain entre plataformas conformes

La sección de regímenes formalizó la **migración natural** entre regímenes (privado, público, híbrido) sin reescritura. Esta sección formaliza una propiedad complementaria pero distinta: la **portabilidad entre plataformas hosting conformes a la spec**. Un AgencyDomain conforme puede migrarse a otra plataforma conforme sin reescribir su lógica, su estado, ni sus políticas. Esto es propiedad estructural de la spec — no compromiso comercial de un proveedor particular.

La motivación es operativa antes que filosófica. Sin compromiso explícito de portabilidad, el AgencyDomain repite el lock-in de la era de las aplicaciones — el cliente queda atado a su proveedor agéntico exactamente como antes quedaba atado a su proveedor SaaS. La promesa estructural de la spec — que el AgencyDomain es **propiedad real del cliente**, no del hosting — depende de que la portabilidad sea propiedad de la spec, no concesión negociada caso por caso.

#### Tres condiciones técnicas

La portabilidad exige tres condiciones técnicas que cualquier implementación conforme debe satisfacer:

**1. Botlets contra primitivas canónicas.** Los Botlets del AgencyDomain deben invocar Capabilities y el SDK de AgencyDomain conforme, **no APIs propietarias del hosting actual**. Si un Botlet invoca una API específica del proveedor — `cloudprovider.lambda.exec`, `vendor.workflow.run` —, esa invocación es deuda de portabilidad. Cuando llega el momento de migrar, ese Botlet debe regenerarse para invocar la primitiva canónica equivalente. Una implementación conforme provee SDKs y registries que abstraen del hosting; el Botlet ve la primitiva, no la implementación.

**2. BD operativa exportable.** El estado persistente del AgencyDomain — agentes, Botlets, capabilities, log de auditoría, datos operativos — debe ser exportable en formato neutro, sin dependencias del motor de almacenamiento del hosting. Esquema documentado (DDL portable o representación equivalente). Dump completo (toda la información necesaria para reconstruir el espacio en otra plataforma). Sin tipos de datos propietarios. Sin extensiones específicas del motor que no tengan equivalente en motores estándar. La portabilidad de la BD es lo que permite que la migración no sea reescritura.

**3. Trust Layer portable.** Las políticas, el log append-only, la configuración de Capabilities y los bindings de identidad deben mantenerse en formato neutro reproducible — típicamente Markdown estructurado o YAML/JSON con schema explícito. La spec no prescribe el formato exacto, pero exige que el formato sea **legible por cualquier implementación conforme**, no solo por la implementación actual. Una política que solo el motor de políticas de un proveedor sabe interpretar no es política del AgencyDomain — es configuración del proveedor.

#### Migración natural vs portabilidad

Las dos propiedades — migración natural entre regímenes y portabilidad entre plataformas — son complementarias pero distintas:

| Eje | Migración natural entre regímenes | Portabilidad entre plataformas |
|---|---|---|
| **¿Qué cambia?** | El régimen del AgencyDomain (privado → público) | La plataforma de hosting |
| **¿Qué permanece?** | Plataforma de hosting | Régimen del AgencyDomain |
| **¿Quién decide?** | La organización dueña, según madurez de uso | La organización dueña, según economía o estrategia |
| **Frecuencia esperada** | Una o dos veces en la vida del AgencyDomain | Cero o pocas veces, pero la posibilidad debe existir |

La portabilidad no es promesa de que la migración será trivial — siempre habrá costo de orquestación, validación, ventana de corte. Es promesa de que la migración será **posible sin reescribir la lógica del agente**. Esa diferencia — entre posible-con-trabajo y imposible-sin-reescritura — es lo que separa un AgencyDomain conforme de un sistema agentivo proprietary disfrazado.

### Conformidad

Una implementación que pretenda llamarse **AgencyDomain conforme** a esta especificación debe satisfacer la siguiente lista de requisitos. Los marcamos con la convención de IETF: **MUST** para obligatorio, **SHOULD** para fuertemente recomendado, **MAY** para opcional.

| Requisito | Nivel |
|---|---|
| Identidad propia | **MUST** |
| Materialización de las cuatro capas | **MUST** |
| Persistencia del estado | **MUST** |
| Aislamiento entre espacios | **MUST** |
| Direccionabilidad URL | **MUST** |
| Modelo de datos canónico | **MUST** |
| Soporte de los tres regímenes | **SHOULD** (al menos uno; idealmente los tres con migración) |
| Soporte de modos Tokens y Suscripción | **MUST** ambos |
| Ciclo de vida completo del agente | **MUST** |
| Comunicación intra-AgencyDomain (interfaz Capa 2 → Capa 3 vía `MCP`; coordinación entre runtimes vía el protocolo `A2A`) | **MUST** |
| `A2A` entre AgencyDomains | **SHOULD** |
| Federación | **MAY** (cuando la spec normativa esté disponible) |
| Trust Infrastructure transversal | **MUST** |
| Principio Agent First | **MUST** |
| Capa 3 distribuida (Botler central + edge) | **SHOULD** (cuando hay presencia física múltiple) |
| Portabilidad entre plataformas conformes | **MUST** (Botlets contra primitivas canónicas, BD exportable, Trust Layer portable) |

Una implementación que cumple todos los **MUST** es AgencyDomain conforme a la versión 1.0 de la spec. Una implementación que cumple los **MUST** y los **SHOULD** es lo que llamaríamos AgencyDomain de referencia — implementación ejemplar que la industria puede tomar como base. Las implementaciones que cumplen también los **MAY** son implementaciones de frontera, que típicamente lideran la evolución del campo.

### Implementaciones de referencia

Como mencionamos en el Capítulo 4, esta especificación es agnóstica a implementación. La **implementación de referencia pública** es **Vergis**: distribuida bajo `AGPL`, con repositorio público en AgencyDomains.org, diseñada para que cualquier desarrollador o estudiante pueda descargarla, leerla, ejecutarla y aprender cómo la spec se traduce en un sistema vivo. El **Capítulo 9** la desarrolla en detalle; aquí basta con dejar el puntero y afirmar que es conforme.

Sobre la misma estructura canónica operan también implementaciones de productos en regímenes complementarios: **Agentia** materializa AgencyDomains en **régimen privado** dentro de la infraestructura de la firma cliente, y **Soveria** los materializa en **régimen público** como red de agentes con identidad pública. Otras implementaciones son admisibles y bienvenidas. La especificación pretende ser estándar de industria, no propiedad intelectual de un actor.

### Frontera de evolución

Tres áreas de la especificación están en evolución activa y una versión futura del libro probablemente las normalizará con mayor detalle.

La **federación** es la primera. Como mencionamos, el protocolo normativo aún no está consensuado por la industria. La versión 1.0 reconoce los mecanismos necesarios sin prescribirlos en detalle. Cuando el consenso llegue — probablemente en los próximos dos a tres años —, la spec lo incorporará.

La **cognición agnóstica** es la segunda. La spec admite cognición no-LLM — simbólica, multimodal, híbrida. La implementación contemporánea es predominantemente LLM-céntrica. La extensión a otros sustratos cognitivos exige refinamiento de las interfaces entre Capa 2 y los demás componentes del AgencyDomain.

La **identidad criptográfica de agentes** es la tercera. El modelo de identidad verificable on-chain o por DID está en exploración. La adopción depende de que el ecosistema más amplio de identidad descentralizada madure suficientemente para soportar el caso de uso agentivo.

Estas tres fronteras coinciden con las del Capítulo 4 — son fronteras de la arquitectura misma, no solo de su materialización en AgencyDomains.
