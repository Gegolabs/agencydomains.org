## Agentlets

En la entrada de una sala de urgencias hay una enfermera de triaje. Su tarea es la misma todo el día: recibir al paciente, evaluarlo, clasificarlo — rojo, amarillo, verde — y derivarlo. La tarea es repetitiva en su forma; ninguna repetición es igual a la anterior. Cada paciente llega con síntomas distintos, historias distintas, señales que no están en ningún manual exactamente como se presentan. La enfermera no puede resolver su trabajo con memoria muscular — cada clasificación exige juicio fresco —, pero tampoco necesita al jefe de medicina interna para cada paciente: su juicio opera dentro de un protocolo acotado, y cuando el caso excede el protocolo, escala. La enfermera de triaje no es un reflejo ni es la deliberación plena del hospital. Es una tercera cosa: **juicio de rutina, empaquetado en un rol**.

Los sistemas agentivos están llenos de trabajo con esa forma. Clasificar los correos que llegan a una casilla operativa. Hacer triaje de las alertas de monitoreo. Resumir cada documento nuevo que entra a un expediente. Extraer las entidades de una factura que nunca se había visto. Juzgar si un mensaje amerita interrupción inmediata o espera al reporte de la mañana. Son tareas **recurrentes en su forma pero frescas en cada instancia**: el patrón es estable, la ejecución exige interpretación. No maduran hacia el determinismo — no por falta de regeneraciones, sino por naturaleza.

El canon, hasta aquí, les daba dos casas y ninguna era la correcta. La primera casa es el **Botlet**: pero el Botlet es código no-LLM por definición, y forzar una tarea interpretativa a código determinístico produce exactamente la fragilidad que la arquitectura existe para evitar. La segunda casa es la **Cognición plena** de la Capa 2: funciona, pero al costo de la vía más cara del sistema — deliberativa, conversacional, dimensionada para lo genuinamente nuevo — aplicada a un patrón que se repite cien veces al día. Entre la memoria muscular y la deliberación plena faltaba el peldaño del medio.

Esta sección formaliza el **Agentlet** como **octava primitiva canónica** — la unidad hermana del Botlet cuyo cuerpo de ejecución invoca inferencia acotada. El Agentlet es la casa del juicio de rutina: patrón empaquetado por fuera, juicio acotado por dentro.

> *El Botlet es memoria muscular. El Agentlet es juicio de rutina empaquetado. La Cognición se reserva para lo genuinamente nuevo.*

### Definición

Un **Agentlet** es una unidad empaquetada de la Capa 3 (Autonomía), hermana del Botlet, cuyo cuerpo de ejecución **invoca inferencia acotada**: un modelo dimensionado a la tarea, aplicado dentro de un charter que el spec declara. Como el Botlet, es instancia configurada de una pieza pre-forjada — el **proto-Agentlet** —, es hospedado por el Botler y es engendrado y mantenido por el agente. A diferencia del Botlet, cada una de sus ejecuciones ejerce juicio: interpreta la instancia concreta que tiene delante en lugar de ejecutar código determinístico.

La frase que fija la doctrina de hermandad: **un Agentlet es un Botlet con juicio adentro — ni más ni menos**. Vive exactamente como su hermano. Hereda por estructura, no por excepción, todo el aparato de las unidades de Capa 3: el patrón proto-/instancia, los catálogos y sus efectos de red, la separación código fuente vs spec, la **manifestación** y la **temporalidad** (`discreta`/`continua`), el contrato declarativo de calidad, la cadena de derivación, el append-only log y los verbos del API de operación (`specialize` · `invoke`/`schedule` · `read`/`subscribe` · `status`/`activate`/`deactivate`/`retire`). Lo que cambia es un solo atributo — el cuerpo invoca inferencia — y de ese atributo se siguen, en cascada, las diferencias que el resto de la sección desarrolla.

Cuatro propiedades definen al Agentlet conforme. La primera es que su **charter está declarado en el spec**: qué tarea resuelve, sobre qué entradas, con qué salidas, dentro de qué límites. El Agentlet no elige qué hacer — su inferencia se gasta en *cómo* hacer lo suyo, nunca en decidir *qué* es lo suyo. La segunda es que su **inferencia es acotada**: el spec declara el modelo (dimensionado a la tarea, no el modelo frontera de la Cognición), las Capabilities que puede consultar y el presupuesto por ejecución. La tercera es que **toda su inferencia pasa por el Botler**: el handle controlado que el Botler le entrega incluye el punto de control de cognición, de modo que cada llamada al modelo queda medida, presupuestada, validada y auditada — el bypass es estructuralmente imposible, no solo prohibido. La cuarta es que tiene **garantía de fallback hacia la Cognición plena**: cuando su inferencia acotada no resuelve el caso — el charter no alcanza, la confianza del veredicto queda bajo umbral, la entrada no se parece a nada previsto —, el Agentlet escala y la Cognición de Capa 2 rescata. El proceso nunca se detiene.

### La regla de contrabando

La frontera entre el Botlet y el Agentlet es un atributo binario, y la spec la protege en ambas direcciones:

- **Si hay inferencia en el cuerpo, es Agentlet.** Un Botlet con una llamada a modelo escondida en su código es no-conforme — contrabandea costo y no-determinismo hacia una unidad cuyas garantías (costo marginal cero, madurez que converge, offline senior) dependen de no tenerlos.
- **Si no hay inferencia en el cuerpo, es Botlet.** Un Agentlet cuyo charter resultó resoluble con código determinístico es un Botlet mal clasificado — y mal presupuestado: paga tokens por un trabajo que la memoria muscular haría gratis. La cognición, al detectarlo, lo cristaliza: genera el Botlet que lo reemplaza.

La segunda dirección de la regla describe además una **trayectoria natural**: hay tareas que ingresan al sistema como Agentlets — porque al inicio cada instancia parecía exigir juicio — y que, con la operación acumulada, revelan un núcleo cristalizable. La cognición extrae ese núcleo a un Botlet y deja al Agentlet solo el residuo genuinamente interpretativo, o lo retira por completo. El sistema maduro migra trabajo hacia abajo en la escalera del costo: de la Cognición a los Agentlets, de los Agentlets a los Botlets.

### Agentlet vs Botlet — la distinción canónica

| Eje | **Botlet** | **Agentlet** |
|---|---|---|
| **Cuerpo de ejecución** | Código no-LLM; cero inferencia | Invoca inferencia acotada, vía el handle del Botler |
| **Metáfora** | Memoria muscular | Juicio de rutina empaquetado |
| **Tarea natural** | Recurrente y **cristalizable** en código | Recurrente en forma, **interpretativa** en cada instancia |
| **Determinismo** | Converge con la madurez | No converge — la corrección es estadística por naturaleza |
| **Costo marginal** | ~0 (cómputo tradicional) | Tokens por ejecución, presupuestados en el spec |
| **Madurez** | Junior → senior; senior = fallos solo exógenos | Semántica propia: spec estabilizado, tasa de escalamiento decreciente |
| **Offline** | Senior operable offline confiablemente | Solo con modelo edge-resident, declarado en el spec |
| **Fallback** | La cognición ejecuta manualmente | Escala a la Cognición plena |

Lo que la tabla **no** contiene es tan importante como lo que contiene: proto-/instancia, catálogos, spec, manifestación, temporalidad, contrato de calidad, cadena de derivación, log, verbos de operación, hospedaje por el Botler, génesis por el agente — todo eso es idéntico, porque se predica del género y no de la especie. La spec llama **unidades** al género: el Botler hospeda unidades; el Botlet y el Agentlet son sus dos especies. La relación canónica del runtime se enuncia en su forma general — **1 Proceso = 1 Botler + N unidades** — y cada contexto la instancia a la especie que corresponda.

### Agentlet vs Agente — agenda vs charter

El nombre de la primitiva reclama membresía en la familia del **Agente**, y la spec se la concede: el término paraguas *Agente* cubre, desde esta versión del canon, **tres miembros** — el **Asistente** (Capa 2, reactivo), el **Agente Autónomo** (Capa 3, proactivo, habitante) y el **Agentlet** (Capa 3, empaquetado). La concesión es honesta — la criatura razona de verdad, con un modelo de verdad — pero exige trazar la frontera con el Agente Autónomo con el mismo rigor con que el canon trazó Faceta vs Botlet, porque los dos viven en la misma capa y los dos usan inferencia.

La frontera cabe en una línea: **el Agente tiene agenda; el Agentlet tiene charter.** El Agente Autónomo persigue objetivos — decide qué hacer, cuándo, con qué medios, y engendra las unidades que necesita. El Agentlet ejecuta la tarea que su spec declara — su juicio opera dentro del charter, jamás sobre el charter.

| Eje | **Agente Autónomo** | **Agentlet** |
|---|---|---|
| **Naturaleza** | **Habitante** del AgencyDomain | **Pieza de catálogo** — instancia de un proto |
| **Nace por** | Provisioning (ciclo de vida de seis fases, identidad de primer orden) | `specialize` sobre un proto-Agentlet |
| **Agenda** | Persigue objetivos; decide qué hacer y cuándo | Charter fijo declarado en el spec |
| **Cognición** | Plena: bindings propios, árbol completo de Capabilities, multi-LLM | Acotada: modelo dimensionado, Capabilities que el spec declara |
| **Engendra** | Genera y regenera Botlets y Agentlets | No engendra nada; es mantenido |
| **Fallback** | *Es* el fallback — encima de él solo está el humano | Escala a la Cognición vía el Botler |
| **Gobernanza** | Ejerce los cinco pilares de Trust Infrastructure (MUST) | Gobernado por los puntos de control del handle del Botler |

El **test de frontera** protege la categoría de desangrarse hacia arriba. Tres preguntas; cualquier respuesta del lado de la autonomía significa que la pieza es un Agente, no un Agentlet:

1. ¿Elige sus propias metas, o las recibe declaradas en el spec?
2. ¿Puede alterar su propio proceso o engendrar otras unidades?
3. ¿Su identidad es de habitante (provisioning) o de instancia (`specialize`)?

Un Agentlet con charter gordo, un loop interno y criterio propio sobre qué perseguir no es un Agentlet avanzado: es un Agente Autónomo disfrazado, operando sin la gobernanza que su naturaleza exige — la versión agentiva del anti-patrón C del §5.

### El Botler como tutor — mismo runtime, un punto de control más

El Agentlet no trae runtime propio. Lo hospeda **el mismo Botler** que hospeda a los Botlets, y esta decisión es de principio, no de conveniencia. El Botler es genérico por definición: gestiona ciclo de vida, aislamiento y ejecución de cualquier unidad sin entender su dominio — y llamar a un modelo no es dominio; es un servicio de runtime. La extensión sigue el patrón que el Botler ya practica: junto a `capability_call` y `log`, el handle controlado que el Botler entrega en cada invocación expone un tercer punto de control — **`cognition_call`** —, la única vía por la cual el cuerpo del Agentlet alcanza un modelo.

La consecuencia de gobierno es el argumento entero: **como toda la inferencia del Agentlet pasa por el handle, Trust Infrastructure la ve completa**. Cada llamada al modelo queda medida (tokens, latencia), presupuestada (contra el límite que el spec declara), validada (los mecanismos del Pilar 3 — detección de alucinaciones, DLP, tokenización — aplican en el punto de control) y auditada (en el mismo append-only log, con la misma identidad, bajo el mismo gobierno que el resto del AgencyDomain). Un runtime paralelo para Agentlets tendría que duplicar toda esa maquinaria — segundo sandbox, segundo esquema de handle, segunda cadena de escalamiento, segunda presencia en la Capa 3 distribuida — para terminar entregando las mismas garantías. La arquitectura plana del Botler ya las entrega.

La preocupación legítima que podría empujar hacia un runtime separado — el perfil de recursos: latencia de modelo, costo por token, eventual aceleración por hardware — es asunto de despliegue, y el canon ya tiene la puerta abierta: los subtipos de Botler se distinguen **por topología y rol de despliegue, nunca por dominio**. Un pool de ejecución segregado para unidades de inferencia pesada es exactamente una distinción de rol de despliegue: un Botler conceptual, N procesos si la operación lo pide.

Conviene dejar explícitas las **dos relaciones** que sostienen a las unidades, porque operan en pisos distintos y las dos cubren a las dos especies por igual:

| Relación | ¿Quién la ejerce? | Sobre Botlets | Sobre Agentlets |
|---|---|---|---|
| **Hospedaje / ejecución** — runtime sin agencia: ciclo de vida, aislamiento, handle controlado, log | El **Botler** | Sí | Sí (mismo handle, más `cognition_call`) |
| **Génesis / mantenimiento** — decidir que exista, especializarlo, regenerarlo, responder por él | El **agente** (la cognición) | Sí | Sí |

El agente es el padre de ambas especies; el Botler es el mayordomo de ambas. Ninguna unidad tiene casa aparte.

### Madurez del Agentlet — estabilización, no convergencia

La trayectoria junior → senior del Botlet converge porque cada regeneración **cristaliza** variantes en código: el senior es determinístico y por eso sus únicos fallos son exógenos. El Agentlet no recorre esa trayectoria — su corrección es estadística por naturaleza y ninguna cantidad de operación la vuelve determinística. Pretender que un Agentlet "madura a senior" en el sentido del Botlet es un error de categoría con consecuencias operativas: nunca se le puede prometer la confiabilidad offline del Botlet senior sobre la misma base.

La spec define para el Agentlet una **semántica de madurez propia**, observable en el mismo append-only log que ya rastrea a los Botlets:

- **Estabilización del spec** — el charter, el prompt operativo y la configuración dejan de cambiar entre revisiones; las ediciones del `specialize` se espacian.
- **Tasa de escalamiento decreciente** — la fracción de ejecuciones que el Agentlet resuelve dentro de su charter sin escalar a la Cognición plena crece y se estabiliza. Es el análogo funcional del `95/4/1`: la proporción entre juicio acotado que basta y juicio pleno que rescata.
- **Calidad sostenida bajo el contrato declarativo** — sus atributos de calidad declarados (frescura, SLA, degradación) se cumplen dentro de umbral por período sostenido.

El **offline** del Agentlet exige declaración explícita, no herencia del hermano. Un Botlet senior opera offline porque no necesita ningún modelo; un Agentlet solo opera offline si su modelo reside en el edge. El spec de todo Agentlet conforme **MUST** declarar la localidad de su cognición acotada — cloud-resident, edge-resident o híbrida, con el mismo vocabulario que la spec ya usa para los Conectores — y su comportamiento sin red. Sin esa declaración, la consecuencia «modo offline trivial» de la topología paralela se rompe en silencio: el sitio que contaba con su vía Autonomía descubre, con la red caída, que la mitad de sus unidades necesitaba un modelo al otro lado del cable.

### proto-Agentlet — la pieza pre-forjada del juicio

Como su hermano, el Agentlet rara vez nace de la nada: nace de un **proto-Agentlet** — la pieza pre-forjada que el agente configura en su tiempo de Ingeniería para instanciar un Agentlet específico al caso. El proto-Agentlet contiene el cuerpo (el andamiaje de la tarea interpretativa: la estructura del charter, el esqueleto del prompt operativo, los contratos de entrada y salida, los umbrales de escalamiento); el Agentlet es la instancia configurada. Las dos clases del proto-Botlet aplican sin cambio: un proto-Agentlet **templado** resuelve una función interpretativa y se configura por parametrización acotada (un clasificador de correo operativo, un extractor de campos de factura); un proto-Agentlet **platafórmico** es un motor de juicio genérico cuya especialización vive en configuración composicional y cubre N funciones de su dominio.

La **cadena de derivación** se extiende sin fricción: los casos de uso documentados requieren unidades — cero, una o varias, de cualquiera de las dos especies —, y cada unidad es instancia de algún proto del catálogo. Todo Agentlet conforme **MUST** poder trazarse en esa cadena, y el append-only log **MUST** registrar el proto-Agentlet de origen de cada instancia. Los catálogos comunes — público abierto en AgencyDomains.org, códices propietarios, contratos privados, acuerdos soberanos — acumulan proto-Agentlets con los mismos efectos de red que acumulan proto-Botlets: el implementador n+1 recibe charters, prompts operativos y umbrales refinados por los implementadores 1 a n.

Las **generaciones** (`G1`/`G2`/`G3`) aplican con una lectura natural: en `G1` el agente configura el proto-Agentlet — rellena el charter, ajusta el prompt operativo dentro del andamiaje, fija umbrales — sin escribir su cuerpo. El filo `G1`/`G2` es el mismo del Botlet: configuración que una Capability bien definida evalúa es `G1`; extensión de la lógica interna del proto es `G2`.

### La economía de los tres peldaños

Con el Agentlet, la escalera económica del sistema agentivo queda completa. El Capítulo 4 presentó dos vías — Cognición costosa, Autonomía barata —; la vista fina distingue **tres peldaños de costo por ejecución**:

| Peldaño | Unidad | Inferencia | Costo marginal |
|---|---|---|---|
| 1 | **Botlet** | Cero | ~0 — cómputo tradicional |
| 2 | **Agentlet** | Acotada: modelo dimensionado, presupuesto declarado | Bajo y **presupuestable por unidad** |
| 3 | **Cognición** | Plena: deliberativa, modelo frontera, árbol completo | Alto — se reserva para lo nuevo |

El peldaño intermedio es el que faltaba. Sin él, toda tarea interpretativa recurrente pagaba precio de peldaño 3 — o se forzaba, frágil, al peldaño 1. Con él, la organización asigna cada patrón a su costo natural, y el sistema maduro migra trabajo escalera abajo: la Cognición cede rutinas interpretativas a Agentlets; los Agentlets ceden núcleos cristalizables a Botlets.

La entrada del Agentlet **matiza, no rompe**, la promesa económica de la vía Autonomía. La vía sigue siendo la barata — pero deja de ser uniformemente gratuita: contiene unidades de costo marginal ~0 y unidades de costo acotado, y el mix se declara por unidad, no se promedia. Bajo planes de **Suscripción fija**, el argumento del Capítulo 5 §2 se refina en el mismo sentido: los Botlets siguen siendo el mecanismo que hace posible la autonomía sostenida sin agotar la cuota, y los Agentlets consumen cuota — acotada, presupuestada, visible en el log — por lo que su proporción en el mix es una decisión económica explícita de la organización, exactamente como lo es la decisión de qué patrones consolidar en Botlets.

Hay una segunda consecuencia transversal: **el pilar de Validación gana presencia en la Capa 3.** Hasta esta versión del canon, la Validación se ejercía en la Capa 2 (parcial) y en la Capa 4 (principal), porque la Capa 3 solo contenía código determinístico. Con los Agentlets entra corrección estadística a la zona de la memoria muscular — exactamente la volatilidad que la Bounded Concerns Architecture (Capítulo 3) enseña a confinar —, y los mecanismos del Pilar 3 (detección de alucinaciones, validación de salidas estructuradas, DLP, tokenización) aplican en el punto de control `cognition_call` del Botler, sobre cada ejecución de cada Agentlet. La delgadez del dominio se preserva: el juicio estadístico queda confinado a unidades declaradas, gobernadas y auditables, nunca disperso por el runtime.

### ¿Cuándo usar Agentlet — y cuándo no?

La decisión entre las tres casas — Botlet, Agentlet, Cognición — se resuelve con dos preguntas en cascada:

**Primera: ¿la tarea es recurrente?** Si no — si es única, exploratoria, o su patrón todavía no se estabiliza —, pertenece a la Cognición. La regla práctica de las diez invocaciones del §2 aplica a las dos especies de unidad por igual.

**Segunda: ¿cada instancia exige juicio?** Si no — si la lógica es cristalizable en código determinístico —, **Botlet**, siempre: es el peldaño más barato y el único que madura hacia el offline confiable. Si sí — si el patrón es estable pero cada ejecución interpreta una instancia nueva —, **Agentlet**.

Tres señales confirman que una tarea es territorio de Agentlet: la entrada es **lenguaje natural o contenido no estructurado** (correos, documentos, transcripciones, descripciones libres); la salida exige **clasificar, resumir, extraer o juzgar** más que calcular o transportar; y los intentos de resolverla con reglas producen **listas de excepciones que crecen sin converger**. Y dos anti-señales devuelven la tarea a sus vecinos: si el "juicio" resultó ser una tabla de decisión estable, es un Botlet que todavía no se cristaliza; si el charter no logra declararse — la tarea exige decidir qué hacer, no solo cómo —, es trabajo de Agente, con la gobernanza de Agente.

### Conformidad

Una implementación de Agentlet conforme a esta especificación debe satisfacer:

| Requisito | Nivel |
|---|---|
| Charter declarado en el spec: tarea, entradas, salidas, límites | **MUST** |
| Inferencia acotada declarada: modelo, Capabilities accesibles, presupuesto por ejecución | **MUST** |
| Toda inferencia cursada por el punto de control `cognition_call` del handle del Botler | **MUST** |
| Garantía de fallback: escalamiento a la Cognición plena ante caso fuera de charter o confianza bajo umbral | **MUST** |
| Cero inferencia fuera del handle (la regla de contrabando, dirección Botlet→Agentlet) | **MUST** |
| Hospedaje por el Botler genérico — sin runtime paralelo por especie | **MUST** |
| Trazabilidad: cada ejecución y cada llamada de inferencia en el append-only log | **MUST** |
| Trazable en la cadena casos-de-uso → unidades → protos; proto-Agentlet de origen registrado | **MUST** |
| Declaración de localidad de la cognición acotada (cloud / edge / híbrida) y comportamiento offline | **MUST** |
| Validación del Pilar 3 aplicada en el punto de control de cognición | **MUST** |
| Distinción explícita Agentlet vs Agente Autónomo en API y documentación (el test de frontera) | **MUST** |
| Métricas de madurez propias: estabilización del spec y tasa de escalamiento | **SHOULD** |
| Cristalización: detección de núcleos deterministas y extracción hacia Botlets | **SHOULD** |
| Pool de ejecución segregado por perfil de recursos (rol de despliegue) | **MAY** |

### Frontera de evolución

Tres áreas activas de evolución del Agentlet merecen mención al cierre.

Los **modelos edge para juicio acotado** son la primera. La viabilidad del Agentlet offline depende de modelos pequeños ejecutando en el sitio físico con calidad suficiente para charters acotados. El estado del arte avanza rápido; la spec ya provee el vocabulario de declaración (localidad de la cognición acotada) para que las implementaciones adopten modelos edge sin cambio de contrato.

La **calibración de confianza** es la segunda. El escalamiento del Agentlet a la Cognición plena depende de que el propio Agentlet estime cuándo su veredicto no alcanza el umbral — un problema de calibración estadística abierto. Mientras madura, las implementaciones conservadoras compensan con umbrales bajos: escalar de más cuesta tokens; escalar de menos cuesta confianza.

La **cristalización asistida** es la tercera. La detección automática de núcleos deterministas dentro de charters de Agentlet — la trayectoria Agentlet → Botlet de la regla de contrabando — es hoy juicio de la cognición en su tiempo de Preparación. Su formalización como mecanismo de Pattern Recognition inverso (detectar lo que *dejó* de necesitar juicio) es trabajo abierto.

---

Con el Agentlet cierra el elenco de construcciones formales de este capítulo — **ocho primitivas canónicas**: AgencyDomain, Botlet, proto-Botlet, Agentlet, Capability, Trust Infrastructure, la distinción Asistente vs Agente Autónomo y la Faceta. Quien haya seguido los Capítulos 4 y 5 tiene en mano el vocabulario constructivo completo con el que la categoría agentiva puede ser razonada y construida — desde el espacio computacional que lo contiene todo hasta la escalera de tres peldaños por la que el trabajo encuentra su costo natural.

El Capítulo 6 desplaza la mirada del sistema individual al mercado. Permite a quien construye o invierte responder con disciplina la pregunta de dónde compite cada actor — propio o ajeno — y por qué un mismo eslabón de la cadena puede ser zona muy disputada o territorio aún abierto.
