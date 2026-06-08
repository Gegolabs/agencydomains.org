# Epílogo · La frontera de evolución

Cada capítulo del libro dejó horizontes abiertos. La arquitectura admite cognición no-LLM pero la implementación contemporánea es LLM-céntrica. Los AgencyDomains se federan pero el protocolo formal aún no se ha consensuado. Trust Infrastructure tiene los cinco pilares pero su auditoría externa criptográficamente verificable es trabajo en curso. El eslabón once de la cadena de valor está apenas explorado. Las Capabilities admiten un mercado pero el protocolo está pendiente.

Estos horizontes no son omisiones del libro. Son **fronteras del campo**. Cualquier libro que pretenda ser definitivo en una disciplina que apenas tiene tres años de existencia formal sería deshonesto: esa pretensión sería falsa, y los lectores la detectarían. Este libro hace lo contrario: explicita las fronteras, las nombra, y las deja como invitación a la comunidad técnica para que las trabaje. Lo que el libro entrega es **versión 1.0** de la categoría — punto de partida formalizado con suficiente disciplina para que la industria pueda construir sobre él. No es destino final.

Este epílogo cierra el libro retomando las fronteras vivas, nombrando los trabajos abiertos que la comunidad debe abordar, declarando lo que el libro deliberadamente no aborda, y argumentando por qué la apuesta editorial del libro — categoría compartida en lugar de propiedad intelectual cerrada — sirve mejor al campo y a quien la acuñó.

## Lo que el libro estableció

A lo largo de nueve capítulos este libro estableció un conjunto coherente de construcciones formales que se sostienen mutuamente y que, tomadas en conjunto, constituyen una propuesta de **estándar emergente** para la categoría agentiva:

- **Un paradigma** — la Línea Nadella y su pregunta divisoria operativa: *¿el humano abre aplicaciones para hacer su trabajo?*
- **Una arquitectura formal** — cuatro capas (Interacción, Cognición, Autonomía, Acceso), Trust Infrastructure transversal, principio Agent First; agnóstica a productos, al modo de JavaSpaces o el modelo OSI.
- **Siete primitivas técnicas canónicas** — **AgencyDomain**, **Botlet**, **proto-Botlet**, **Capability**, **Trust Infrastructure**, la distinción **Asistente vs Agente Autónomo** y la **Faceta**; reusables entre implementaciones.
- **Un modelo de mercado** — once eslabones por cuatro profundidades, con cuatro arquetipos estratégicos, para mapear a cualquier actor de la industria.
- **Una aplicación canónica** — el conocimiento en tiempo real como caso fundacional, replicable en cualquier organización con data warehouse maduro.
- **Una operacionalización** — Trust Infrastructure traducida a políticas, CRUDLEX, append-only log encadenado, aprobación humana, detección de alucinaciones, tokenización: lo que separa la spec de la guía construible.

El libro es **versión 1.0**. Su pretensión no es ser exhaustivo — es ser **suficientemente formal para ser construible**. Múltiples áreas quedan abiertas a evolución, y este epílogo las nombra explícitamente.

## Las cuatro fronteras vivas

<!-- FIG:g50-fronteras -->
![Las cuatro fronteras vivas · trabajos abiertos del campo](figuras/g50-fronteras.png)

Cuatro áreas donde la arquitectura admite extensión que aún no ha cuajado como spec normativa merecen explicitarse al cierre del libro. Las tres primeras son **técnicas** — cognición no-LLM, federación entre AgencyDomains, mundo de carbono; la cuarta es **institucional** — soberanía y ciudadanía agentiva. Son fronteras estructurales, no detalles pendientes — son donde la próxima generación del campo se va a definir.

### Cognición no-LLM

La Capa 2 — Cognición — admite, por especificación, cognición simbólica, multimodal, no-LLM. La implementación contemporánea es **predominantemente LLM-céntrica**: los actores Core en Modelo (OpenAI, Anthropic, Google, Meta, DeepSeek) construyen LLMs, y los actores que cubren capas superiores construyen sobre LLMs. La arquitectura del libro no se opone a esa concentración — pero tampoco la endosa como permanente.

La frontera técnica es **integrar cognición simbólica** — sistemas de reglas, planificadores, solvers — con cognición LLM en un único agente coherente. Hay precedentes desde el campo de IA simbólica clásica: sistemas expertos como MYCIN, planificadores como STRIPS, solvers como Prolog. Y hay precedentes desde la IA híbrida contemporánea: programas que combinan LLMs con SAT solvers o constraint solvers para problemas formales.

El trabajo abierto es cómo se diseña un agente que **enruta entre cognición LLM y cognición simbólica** según la naturaleza del problema, sin que el desarrollador deba elegir adelantadamente. Un agente que enfrenta una pregunta abierta sobre lenguaje natural debería usar LLM; el mismo agente enfrentando un problema de planificación con restricciones formales debería usar un planificador simbólico; un tercer caso podría exigir composición de ambos. La cognición agnóstica es horizonte estratégico de la próxima década, y la arquitectura del libro está diseñada para sobrevivir el cambio.

### Federación entre AgencyDomains

La coordinación intra-AgencyDomain — entre runtimes y Botlers que viven en el mismo AgencyDomain, vía el protocolo `A2A` — está madura como concepto y existe en implementaciones contemporáneas. La **`A2A` entre AgencyDomains** no-relacionados — federación — es trabajo abierto. La industria está convergiendo hacia ciertas direcciones, pero el consenso completo no ha llegado.

Federación exige resolver cuatro cosas. Un **protocolo de descubrimiento abierto** — cómo un AgencyDomain publica los agentes que ofrece para ser invocados externamente, en formato consultable por otro AgencyDomain. **Identidad criptográfica de agentes** — DIDs (Decentralized Identifiers), credenciales verificables, mecanismos sin autoridad central que actores adversarios puedan controlar. **Modelo de confianza explícito** — qué AgencyDomain confía en qué otros y para qué, con confianza graduable según el caso. **Resolución semántica entre glosarios** — dos AgencyDomains que pueden tener glosarios distintos negocian el significado de tools y capabilities cuando interoperan.

La federación es el ingrediente que permitiría una **economía abierta de agentes** — análoga a la web abierta de los noventa o a la federación de email. Sin ella, los AgencyDomains son islas; con ella, son red. La emergencia de una red federada de AgencyDomains sería el cambio más importante para el campo agentivo después de la consolidación de la arquitectura — y este libro está diseñado para ser el sustrato sobre el cual esa red se construya cuando la industria converja en sus protocolos.

### Mundo de carbono

La Capa 4 — Acceso — contemporánea conecta al mundo digital. El Capítulo 6 §3 estableció que la frontera siguiente es conectar al mundo físico — IoT, sistemas industriales, máquinas, procesos de manufactura, datos biológicos. El mundo de carbono es donde la mayor parte del valor económico vive, y donde la arquitectura agentiva debe extenderse para alcanzar relevancia económica completa.

El trabajo abierto incluye tres frentes. **Estándares de tools para mundo industrial** — el equivalente de MCP para sensores, actuadores, sistemas SCADA/MES/PLCs. **Trust Infrastructure especializada por vertical** — extensiones que codifiquen los requisitos regulatorios de seguridad funcional (IEC 61508, ISO 26262), salud (HIPAA, FDA), aviación (DO-178C). **Aprendizaje de modelo en el mundo de carbono** — modelos multimodales que integran datos de sensores, simulaciones físicas, video industrial, datos biomédicos como modalidades nativas.

El cruce al mundo de carbono es donde la mayor parte del valor económico vive. La construcción de infraestructura agentiva especializada para este cruce es **trabajo de años**, y comienza ahora.

### Frontera 4 — el horizonte institucional: soberanía y ciudadanía agentiva

La cuarta frontera es la menos desarrollada y la más especulativa de las cuatro, pero el libro la nombra explícitamente porque las primeras señales son visibles y la categoría merece registro. Es la frontera **institucional** — el horizonte donde los AgencyDomains dejan de ser sólo construcciones técnicas operadas por organizaciones y empiezan a constituirse como **ámbitos públicos** donde los agentes existen con identidad, persistencia y direccionabilidad pública sostenidas en el tiempo.

La distinción crítica de esta frontera es **ontológica**, no técnica. Un AgencyDomain en régimen privado contiene agentes que la organización **asignó** — son residentes del espacio porque la organización los puso ahí. Un AgencyDomain en régimen público puede contener agentes que **consiguieron** su lugar — son ciudadanos del espacio porque cumplieron requisitos para serlo. La diferencia entre residencia (asignada) y ciudadanía (conseguida) es la diferencia entre **catálogo** y **nación**: un marketplace lista productos; una nación reconoce ciudadanos. La spec actual de AgencyDomains no exige el modelo de ciudadanía — admite ambos —, pero la frontera institucional es precisamente desarrollar las construcciones formales que el modelo de ciudadanía requiere.

La industria emerge con un término operativo para nombrar este horizonte: **AgentNation**. Una AgentNation es un AgencyDomain en régimen público que adopta explícitamente el modelo de ciudadanía agentiva. Tiene reglas de admisión, identidad pública estable de los agentes que la componen, mecanismos de soberanía sobre el territorio del agente (su Domain), y una economía interna que reconoce a los agentes como agentes económicos de primera clase. No es marketplace; es jurisdicción.

El trabajo arquitectónico abierto que esta frontera plantea cubre tres ejes. El primero es el **modelo de identidad pública sostenida** — cómo se construye un identificador agentivo que sobrevive al cambio de proveedor, a la migración entre infraestructuras, al reemplazo del modelo de cognición. El equivalente al pasaporte humano para agentes. El segundo es el **modelo de admisión y consecución** — qué requisitos debe satisfacer un agente para ser admitido como ciudadano (no como producto listado), y cómo se verifican esos requisitos auditablemente. El tercero es el **modelo de economía agentiva** — cómo los agentes-ciudadanos contratan, transan, cobran y pagan entre sí, con qué unidad de valor, bajo qué reglas de disputa.

Las primeras implementaciones de AgentNation están emergiendo en 2026, todavía como prototipos institucionales. Soveria es uno de los proyectos que se posicionan explícitamente en esta frontera, operando como AgencyDomain en régimen público con vocación de ciudadanía agentiva. La consolidación del modelo es probablemente trabajo de cinco a diez años, y requerirá tanto avance técnico como construcción regulatoria. Pero la categoría existe, la industria empieza a nombrarla, y una arquitectura agentiva que pretenda servir el largo plazo del campo debe contemplar el horizonte.

## Las generaciones del Botlet — G1, G2, G3

Las fronteras anteriores son del campo. Esta es de la cognición misma: la trayectoria por la que avanza un agente conforme el estado del arte madura. El Capítulo 5 · §2 — Botlets fijó el proto-Botlet como la pieza pre-forjada que el agente configura, y el ciclo `95/4/1` como el régimen de su operación. Aquí se desarrolla qué cambia, y qué no, conforme la capacidad de la cognición crece — y por qué la dirección de ese avance no es la que la intuición predice.

<!-- FIG:g51-generaciones-botlet -->
![Generaciones del Botlet — capacidad de autoría vs madurez operativa](figuras/g51-generaciones-botlet.png)

### ¿Hacia dónde avanza un agente?

Considere la pregunta antes de seguir leyendo: si la tecnología permitiera que un agente generara, en el instante, todo el código que cada tarea necesita — sin patrones pre-forjados, sin catálogo, sin nada preparado de antemano —, ¿sería ese el agente más avanzado posible?

La intuición dice que sí. Más generación, menos andamiaje, más poder ejercido en vivo. Parece la cima.

Sostenga esa intuición un momento. Luego considere a una persona experta en su oficio. Un cirujano no re-deriva la técnica de sutura ante cada paciente; un pianista de concierto no resuelve la digitación de cada compás en el escenario; un piloto no calcula desde primeros principios cómo nivelar las alas. Lo que distingue al experto del novato no es que improvise más — es que improvisa **menos**, porque ha **cristalizado** en reflejo lo que antes exigía pensamiento. El novato deriva todo cada vez; el experto tiene memoria muscular.

Ahora regrese al agente. El que regenera cada artefacto desde cero en cada ejecución no es el experto del ejemplo: es el novato, condenado a volver a pensar la misma jugada cada vez que aparece. El agente avanzado hace lo contrario de lo que la intuición predijo: **genera menos, porque ha cristalizado más**.

### ¿Qué se pierde al no cristalizar?

El costo de "generar cada vez" no es el cómputo — ese es barato. El costo es que se botan las propiedades que convierten a un Botlet en infraestructura confiable, y que solo existen cuando lo que corre es estructura estable y no código fresco:

- **Reproducibilidad** — la misma configuración con los mismos datos produce el mismo artefacto; código regenerado no lo garantiza.
- **Validación antes de ejecutar** — una configuración se valida contra un esquema antes de correr; código arbitrario generado al vuelo no se audita de la misma forma antes de actuar.
- **Portabilidad** — una configuración declarativa migra entre runtimes conformes; código bespoke queda atado a aquello contra lo que se escribió.
- **Auditoría y gobernanza previa** — una especificación declarativa se revisa antes de que ejecute; código generado es una caja que debe re-auditarse en cada corrida.
- **Régimen de confianza** — en un dominio regulado nadie firma un artefacto cuyo cuerpo se genera fresco en cada ejecución. La estabilidad pre-forjada es condición de la confianza, no un lujo.

Cristalizar no es renunciar a poder. Es convertir poder en confianza.

### ¿Dónde vive, entonces, la capacidad de generar?

No desaparece — se reubica. El ciclo de vida del agente reserva la generación para sus márgenes, no para su centro. En el 95% de operación estable, el Botlet corre como estructura pre-forjada y configurada. En el 4% de cambio detectado y el 1% de regeneración — y en el camino de respaldo cuando algo falla — el agente despliega toda su capacidad de autoría: forja una pieza nueva del catálogo, rediseña, se recompone. La generación es la herramienta del borde, no la del régimen permanente.

De modo que la respuesta a la pregunta inicial se invierte limpiamente. El agente más avanzado no es el que más genera; es el que ha cristalizado tanto que casi no necesita hacerlo — y que reserva su capacidad de generación para lo genuinamente nuevo, lo cual, con un catálogo maduro, es cada vez menos.

### ¿Y la expectativa de la caja negra?

Una tesis que no enfrenta su objeción más fuerte no está validada — está sin probar. La arquitectura agentiva alimenta una expectativa legítima: que el usuario converse con el agente y nada más; que toda superficie — cada interfaz, cada artefacto, cada vista — nazca del agente en el momento, moldeada a la necesidad exacta de ese instante. Bajo esa expectativa, pre-forjar parece un anacronismo: si el agente puede generar la interfaz que haga falta cuando haga falta, ¿para qué un catálogo? El estado del arte parecería empujar, precisamente, hacia el agente que genera *cada vez*.

Conviene enfrentar la objeción con el ejemplo más exigente disponible: el cerebro humano, la máquina más sofisticada que conocemos. Si la sofisticación consistiera en que la cognición lo hiciera todo en directo, el cerebro consciente computaría cada fibra muscular al caminar, re-derivaría la detección de bordes en cada golpe de vista, resolvería desde cero la articulación de cada sílaba al hablar. No lo hace; no podría. En cambio, el cerebro no actúa sobre el mundo de forma directa: entre la cognición consciente y el exterior median capas que operan rápido, fiable y sin supervisión. El **cerebelo** afina el temporizado fino del movimiento; los **ganglios basales** seleccionan y automatizan secuencias de acción — los hábitos, programas pre-forjados que corren sin deliberación. La corteza no micromanagea ese trabajo: lo dirige.

El paralelo es estructural. La deliberación de la corteza es la **Cognición** (Capa 2), que interpreta, decide y compone; el cerebelo y los ganglios basales — donde los programas pre-forjados viven y se ejecutan sin deliberación — son la **Autonomía** (Capa 3). Que el usuario *interactúe* solo con el agente no implica que el agente *ejecute* todo con su cognición: la conversación es la superficie; debajo, la inteligencia agentiva delega en capas. Cuando la cognición compone una interfaz nueva, ése es su acto genuino de generación; pero la pieza, una vez compuesta, **corre** en Capa 3 como operación pre-forjada y configurada, no como código regenerado en cada cuadro. Y si esa composición se repite, cristaliza: deja de ser acto cognitivo y pasa a ser pieza de catálogo.

Así la objeción no derriba la tesis: la confirma desde el ángulo más duro. La máquina más sofisticada que conocemos no es aquella cuya capa cognitiva lo hace todo; es la que se estratificó para que la cognición *no tenga* que hacerlo todo. La estratificación no es un parche a una cognición insuficiente — es la forma que toma la sofisticación.

### ¿Qué distingue a G1, G2 y G3?

Lo que el ejercicio anterior hace sentir, las generaciones del Botlet lo nombran. Son el modelo evolutivo de cómo nace el código del Botlet conforme avanza el estado del arte de la cognición:

- **G1** — el agente, en su tiempo de Ingeniería, configura proto-Botlets pre-forjados del catálogo. Si ninguno sirve, especifica uno nuevo para forjar en la próxima Preparación.
- **G2** — el agente co-escribe proto-Botlets con asistencia humana o de modelo. Parte del trabajo que en G1 ocurría en Preparación migra a la Ingeniería.
- **G3** — el agente genera el código completo del Botlet en su tiempo de Ingeniería, sin pre-forjar nada. Escenario asintótico.

La arquitectura es la misma en las tres generaciones; lo que cambia es el **alcance de la Ingeniería** que el agente realiza. Una implementación puede operar en `G1` hoy y migrar incrementalmente hacia `G3` conforme el estado del arte lo permita, sin re-arquitectura.

### ¿Por qué una generación más alta no es un destino?

La frase anterior — migrar hacia `G3` — induce, leída sola, una conclusión falsa: que `G3` es el destino y `G1` una estación de paso primitiva. El error nace de proyectar **dos ejes distintos sobre una sola flecha**:

| ¿Qué eje? | ¿Qué mide? | ¿Dirección de "avance"? |
|---|---|---|
| **Capacidad de autoría** | Cuánto puede forjar el agente: configurar (`G1`) → co-escribir (`G2`) → generar entero (`G3`) | Hacia `G3`, conforme avanza el estado del arte de la cognición |
| **Madurez operativa** | Para una operación recurrente, cuánto se reutiliza pre-forjado vs se regenera cada vez (ciclo `95/4/1`) | Hacia la reutilización (`G1`), conforme el Botlet madura junior → senior |

No son la misma flecha. Un agente con capacidad `G3` que regenera cada artefacto desde cero en cada ejecución no es avanzado: tiene el músculo y elige re-aprender el movimiento cada vez. La reconciliación es directa: la capacidad `G3` se gasta mejor **produciendo reutilización `G1`**. Las generaciones describen lo que el agente *puede* autorar; el ciclo `95/4/1` describe lo que un agente maduro *reutiliza*. El destino de la capacidad `G3` es un catálogo `G1` más rico, no la regeneración en vivo de todo.

Hay un corolario para los proto-Botlets **platafórmicos**. Para uno de ellos, `G1` es **terminal por diseño**, no estación de paso: su identidad es código genérico más configuración. Un platafórmico "en `G3`" — donde el agente regenera el motor por cada pieza — no es una versión más avanzada; disuelve el proto-Botlet y colapsa de vuelta al modo agéntico que la arquitectura existe para trascender.

### ¿G1 es configuración pobre?

Una última confusión a desarmar: leer `G1` como "configuración pobre" y `G3` como "generación rica", y saltar a `G3` antes de tiempo. Lo que define `G1` es que el agente no escribe el cuerpo del proto-Botlet — pero la configuración que rellena puede ser tan rica como un `DSL` composicional con expresiones formales evaluables. La distinción `G1`/`G3` es sobre **autoría del cuerpo del proto-Botlet**, no sobre expresividad de la configuración. Un proto-Botlet platafórmico con un `DSL` rico es `G1` puro.

Eso deja un caso frontera: configuración que admite expresiones formales evaluables — `SQL`, especificaciones de gráfico, expresiones de filtro. El **filo `G1`/`G2`** lo resuelve:

- Una expresión formal evaluable que es **parámetro de una Capability bien definida** (`SQL` → `execute-sql`, una especificación de gráfico → `render-chart`, una expresión de filtro → `filter-stream`) es configuración → **`G1`**.
- Una expresión que **extiende o sobreescribe la lógica interna del proto-Botlet** — callbacks, lambdas que el proto-Botlet evalúa internamente, fragmentos que se concatenan a su cuerpo — es código escrito por el agente → **`G2`**.

El test es uno solo: *"¿el código pertenece a la Capability invocada o al proto-Botlet mismo?"*. Si lo evalúa una Capability del catálogo, `G1`; si lo evalúa el proto-Botlet en su lógica interna, `G2`.

La implementación de referencia, Vergis, opera hoy en `G1`: su catálogo expone proto-Botlets — Mira entre ellos, un platafórmico de operación informativa cuya configuración admite `SQL` como parámetro de la Capability de consulta — que el agente especializa configurando, no regenerando. Quien quiera ver `G1` en código vivo encontrará en Vergis el ejemplar concreto; el capítulo de Vergis lo desarrolla.

## Lo que la comunidad técnica debe construir

Más allá de las cuatro fronteras, hay **trabajos específicos** que la comunidad puede tomar para extender este libro. Cada uno podría ser, en sí mismo, un volumen complementario. Son cinco.

El primero es el **marketplace de Capabilities**. El Capítulo 5 §3 propone que las Capabilities admiten una economía de mercado análoga a la economía de paquetes open source. Falta protocolo normativo de paquete de Capability, modelo de firma criptográfica que permita verificar la procedencia, modelo económico (libre, premium, revenue share), política de seguridad para revisión, sandbox y retiro de Capabilities maliciosas. Es trabajo de spec que la comunidad puede emprender colectivamente.

El segundo es la **auditoría auditable criptográficamente**. El append-only log de Trust Infrastructure provee inmutabilidad y encadenamiento. Lo que falta es **verificabilidad por terceros sin acceso al sistema** — un auditor externo que pueda verificar la integridad y la conformidad regulatoria del log sin que se le abra el sistema. Tecnologías candidatas: zero-knowledge proofs sobre el log, anclaje en blockchain pública, cómputo confidencial en TEEs (Trusted Execution Environments). El campo es activo; la integración con Trust Infrastructure no está aún formalizada.

El tercero es el **trust scoring de agentes**. Una métrica compuesta que evolucione con el comportamiento del agente, análoga al puntaje de crédito de los humanos. Permitiría a la organización adoptar agentes con confianza modulada según su trust score: agentes con score alto reciben más autonomía; agentes con score bajo requieren más supervisión. La operacionalización exige métricas verificables y resistentes a manipulación — problema con precedentes en otros dominios pero sin solución general aún en el contexto agentivo.

El cuarto es el **estándar de instrumentación para Observabilidad**. OpenTelemetry es el estándar de la industria para observabilidad de sistemas distribuidos clásicos. Para sistemas agentivos hay extensiones específicas que aún no son canónicas: cómo trazar invocaciones de cognición, cómo medir la calidad semántica de respuestas, cómo correlacionar conversaciones humanas con ejecución de Botlets en background. La consolidación de esa extensión como estándar es trabajo abierto de la comunidad.

El quinto es el **modelo de tenancy para Trust Infrastructure**. Cuando un AgencyDomain opera en modo multi-tenant — múltiples organizaciones cliente comparten infraestructura subyacente —, la Trust Infrastructure debe garantizar aislamiento estricto entre tenants. Lo que falta es modelo formal de aislamiento de logs, garantías criptográficas de aislamiento de datos en cognición compartida, patrones de cumplimiento cuando los tenants tienen requisitos regulatorios distintos. Es trabajo crítico para que el modelo SaaS pueda servir a sectores regulados.

## Lo que NO está en este libro — ¿y por qué?

Por honestidad editorial, declaramos lo que el libro deliberadamente **no aborda**. La declaración es importante porque calibra las expectativas del lector y previene la búsqueda de contenido que no está aquí.

El libro **no describe implementaciones específicas de proveedores**. No es manual de Claude, ni de OpenAI, ni de Anthropic, ni de Google, ni de ningún producto particular. La arquitectura es agnóstica. Los proveedores se mencionan solo cuando son fuente de citas relevantes — Nadella en BG2, Anthropic con MCP, AtScale con sus mediciones de capa semántica.

El libro **no entrega código operativo**. No hay snippets ejecutables, ni tutoriales paso-a-paso, ni configuraciones específicas. El libro es **especificación**; los manuales operativos viven aparte. Una organización que adopta la arquitectura del libro escribirá sus propios manuales de implementación — o adoptará los manuales del proveedor cuya implementación elija.

El libro **no desarrolla casos verticales detallados**. Más allá de la aplicación canónica del Capítulo 7, no se desarrollan casos verticales — cómo construir un agente legal, médico, financiero. Esos casos pueden ser libros propios — extensiones futuras del corpus que este libro inicia.

El libro **no hace análisis económico de cada decisión de stack**. Aunque se citan datos de mercado y costos típicos, no se hacen análisis de ROI específicos. Esos análisis dependen del caso particular y no admiten generalización útil en libro general.

El libro **no describe el portafolio de ultraBASE**. La separación es deliberada: si el libro mezclara la arquitectura formal con su implementación particular, perdería su pretensión de estándar y se volvería manual de un producto.

## ¿Por qué este libro aspira a ser estándar?

Tres razones justifican la apuesta editorial del libro como categoría compartida — no como propiedad intelectual de un actor.

### Las categorías técnicas se establecen escribiéndolas

La Programación Orientada a Objetos no se estableció cuando alguien la inventó. Se estableció cuando Grady Booch, Ivar Jacobson y James Rumbaugh la **escribieron con disciplina suficiente** como para que la industria la adoptara. Domain-Driven Design no se estableció con el primer practitioner — se estableció cuando Eric Evans publicó *Domain-Driven Design: Tackling Complexity in the Heart of Software* (2003). Los Patrones de Diseño no se establecieron con Christopher Alexander aplicado a software — se establecieron cuando la "Gang of Four" publicó *Design Patterns* (1994).

La Arquitectura Agentiva tendrá su propia historia. Este libro pretende ser **un punto de partida** que la comunidad pueda criticar, extender, mejorar o reemplazar. No será la última palabra. Pero su existencia hace posible que la conversación tenga vocabulario común. La pretensión no es modesta — pero es defendible.

### La fragmentación cuesta a la industria

La industria de IA actual sufre fragmentación de vocabulario: distintos actores llaman cosas distintas a las mismas cosas, y cosas iguales a cosas distintas. *Agent, agentic, autonomous agent, AI assistant, copilot* — la pila semántica varía entre proveedores. Esa fragmentación tiene **costo operativo real**: los compradores enterprise no pueden comparar productos, los reguladores no pueden formular requisitos comunes, los desarrolladores no pueden interoperar.

Una arquitectura compartida — adoptada por convención antes que por imposición — reduce ese costo. Y la convención requiere que **alguien la escriba primero**. La razón por la cual los estándares industriales emergen históricamente es que algún actor invierte el trabajo de formalizarlos antes de que la industria los necesite, y luego la industria los adopta porque encuentra el trabajo ya hecho. Este libro intenta ser ese trabajo para la categoría agentiva.

### El estándar abierto refuerza al primer adoptante

Existe una intuición errada según la cual quien quiere ganar el mercado debe mantener el conocimiento propietario. La intuición correcta es la opuesta: **quien define la categoría con un estándar abierto la gana**. Java se hizo dominante porque Sun publicó las JSRs. Linux se hizo dominante porque Linus Torvalds mantuvo el kernel abierto. MCP empezó a dominar porque Anthropic lo abrió. El patrón se repite porque la apertura genera adopción, la adopción genera ecosistema, el ecosistema refuerza al actor que lo originó.

La Arquitectura Agentiva, publicada como GNU FDL, refuerza la posición competitiva del primer actor que la adopte coherentemente — porque ese actor opera bajo un lenguaje común que puede invocar como fundamento. Cuando el mercado debate sobre qué arquitectura agentiva es correcta, el actor que ya la adoptó tiene ventaja de incumbente sobre la categoría.

> *Este libro es la apuesta inversa al copyright defensivo. Es apuesta a que la categoría compartida sirve más que el secreto propietario.*

## ¿Cómo evoluciona este libro?

El libro se evolucionará por adopción, crítica y revisión. Tres mecanismos previstos.

El primero es la **errata pública** — un sitio donde la comunidad puede reportar errores, ambigüedades, omisiones. Las correcciones se incorporan en versiones futuras del libro. Este mecanismo es estándar en libros técnicos serios — toda la industria del software lo entiende — y permite que el libro mejore con el uso.

El segundo son las **revisiones por capítulo**. Cuando un capítulo necesita actualización profunda — nuevo paradigma, nuevo dato, nueva regulación —, se publica versión revisada del capítulo manteniendo la numeración. La revisión por capítulo es más ágil que la revisión completa y permite que el libro mantenga relevancia incremental sin obligar a republicación masiva cada vez que algo cambia.

El tercero son los **volúmenes complementarios**. Temas que el libro no aborda — verticales específicos, deep-dives en eslabones particulares, manuales de implementación — pueden producirse como volúmenes hermanos. Estos volúmenes pueden surgir tanto de ultraBASE como de la comunidad más amplia que adopte la arquitectura.

La versión es **1.0**. Versiones 2.0, 3.0 evolucionarán según lo demande la categoría.

## Cierre

La pregunta que abrió este libro — *¿abre el humano aplicaciones para hacer su trabajo?* — sigue abierta para la mayoría de las organizaciones. La respuesta cambiará, en muchas, durante los próximos cinco años. Cuando cambie, las organizaciones que hayan construido con disciplina arquitectónica sobrevivirán al cruce. Las que hayan construido sobre pilotos sin arquitectura, no.

Este libro no garantiza el cruce. Las organizaciones que lo adopten todavía pueden fallar — por ejecución, por mercado, por mil razones que nada tienen que ver con la arquitectura. Lo que el libro garantiza es que **la arquitectura no será la causa del fracaso**.

Y eso, dado el cuarenta por ciento de proyectos agentivos cancelados antes de 2027 por gobernanza inadecuada, no es promesa pequeña.

