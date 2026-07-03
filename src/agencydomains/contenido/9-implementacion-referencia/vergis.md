# Capítulo 9 · Vergis — la implementación de referencia

Los capítulos anteriores entregaron una especificación: primitivas, propiedades exigidas, separaciones canónicas, contratos declarativos. Una especificación, por precisa que sea, no es un sistema vivo. Entre el contrato y la práctica hay un salto que cada lector externo intuye al cerrar el último capítulo de la spec: *"¿cómo se ve esto cuando funciona?"*. Esta es la sección que responde esa pregunta con un artefacto concreto, descargable y ejecutable.

## Nota de alcance del canon

Conviene fijar primero qué es y qué no es este canon, porque la respuesta delimita el rol de todo lo que sigue.

> Este canon contiene la **estructura y el vocabulario** del Mundo Agentivo: definiciones, primitivas, propiedades exigidas, separaciones canónicas. **No contiene métodos para implementar ni catálogos operacionales** — esos viven en cuerpos complementarios. La implementación de referencia pública es **AgencyDomains.org**, materializada en **Vergis**: diseñada para que cualquier desarrollador o estudiante pueda descargarla, leerla, ejecutarla y aprender cómo el canon se traduce en sistemas vivos. Otros implementadores —productos comerciales, códices propietarios— ofrecen sus propios cuerpos complementarios sobre la misma estructura canónica.

La separación es deliberada. El canon describe *qué* propiedades satisface un AgencyDomain conforme; no prescribe *cómo* se descubre un caso de uso, *cómo* se forja un proto-Botlet, ni *qué* proto-Botlets concretos debe contener un catálogo. Esos son método y catálogo — materia de los cuerpos complementarios. Sin esta nota, el lector se preguntaría por qué la spec no incluye un capítulo sobre Discovery o un repertorio de proto-Botlets listos. No los incluye porque no le corresponden: pertenecen al nivel de la implementación, y la implementación de referencia es donde se vuelven visibles.

Esta nota acota el eje *canon vs implementación de referencia* — qué pertenece a la spec y qué a quien la implementa. Es distinta de la declaración de **lo que el libro deliberadamente omite** (verticales detallados, código operativo, análisis de ROI por stack), que vive en el Epílogo, sección "Lo que NO está en este libro".

## ¿Qué es y por qué existe?

**Vergis** es la implementación de referencia pública de AgencyDomains — el AgencyDomain hecho operativo. Es el puente concreto entre el canon y la práctica: un sistema que cualquiera puede descargar, leer, ejecutar y contribuir, construido para demostrar que las primitivas de la spec no son teoría sino piezas que componen un runtime que funciona.

Una especificación sin implementación de referencia corre el riesgo de quedar como ejercicio formal sin tracción. La implementación de referencia cumple cuatro funciones que el texto del canon por sí solo no puede cumplir. Da al lector externo una **puerta de entrada concreta** después de leer la spec. Prueba que el canon es **implementable** —la implementación es la prueba viva—. Habilita un **modelo de adopción claro**: descargar, operar, extender, contribuir. Y ancla el vocabulario abstracto en componentes que se pueden inspeccionar línea a línea.

Vergis no es tutorial ni juguete pedagógico. Es el sustrato sobre el que corren sistemas productivos. Esa cualidad —que se desarrolla más abajo— es lo que distingue una implementación de referencia seria de una colección de ejemplos.

## ¿Dónde vive?

Vergis vive en un repositorio público enlazado desde **AgencyDomains.org**. El código se distribuye bajo **`AGPL`** (Affero General Public License); la documentación, bajo **`GFDL`** (GNU Free Documentation License).

La elección de licencias es estructural, no incidental. La `AGPL` garantiza que las mejoras al runtime —incluidas las que operan como servicio de red— permanezcan disponibles para la comunidad: quien despliega una versión modificada de Vergis y la ofrece por red MUST publicar su fuente. La `GFDL` mantiene la documentación libre y derivable. Juntas, sostienen la promesa de una base común que ningún actor puede cerrar: la plataforma de referencia permanece abierta aunque los catálogos que se construyan sobre ella sean privados.

## ¿Cómo se nombran las piezas? — Vergis · Botler · Mira

Tres etiquetas de **naturaleza distinta** intervienen en la implementación de referencia. Confundir su naturaleza —en particular, confundir un tipo con un nombre propio— oscurece la arquitectura. El esquema:

<!-- FIG:g49-vergis-botler-mira -->
![Vergis · Botler · Mira — tipo vs nombre propio](figuras/g49-vergis-botler-mira.png)

| Capa | Tipo · categoría / primitiva canónica | Nombre propio |
|------|----------------------------------------|---------------|
| Plataforma · *Meta-Cognitive Platform* | implementación de referencia de AgencyDomains (el AgencyDomain hecho operativo) | **Vergis** |
| Runtime de Capa 3 | **Botler** (constructo normado de la spec de Botlets) | — *(genérico; "el Botler". La build de Vergis no le pone nombre propio.)* |
| Componente del catálogo | proto-Botlet platafórmico de operación informativa | **Mira** |

La distinción tipo / nombre propio:

- **Botler** es un **tipo** — un constructo canónico de la spec de Botlets (no una de las siete primitivas, pero sí vocabulario normado del canon). Cualquier runtime de Capa 3 conforme *es un* Botler. No es nombre propio; el Botler que Vergis empaqueta es "el Botler" genérico, sin nombre de instancia.
- **Vergis** y **Mira** son **nombres propios** de instancias específicas — viven en el mismo cajón que Soveria, Agentia o ultraPRO. Vergis nombra *esta* plataforma; Mira nombra *este* proto-Botlet del catálogo.

Por categoría, Vergis es una **Meta-Cognitive Platform**: no realiza la cognición de objeto —eso es la Capa 2—, sino que **administra la economía de la cognición**. Decide cuándo el agente corre con músculo pre-forjado (G1) y cuándo invoca cognición fresca (fallback), gestiona el ciclo `95/4/1`, la maduración junior→senior y la cristalización de experiencia en estructura reutilizable. Eso es metacognición en sentido preciso: monitoreo y control de los procesos cognitivos.

> El descriptor **Meta-Cognitive Platform** **MUST NOT** abreviarse a `MCP`. En el espacio agentivo actual, `MCP` nombra el **Model Context Protocol**; la sigla está tomada. El descriptor se usa deletreado.

El nombre **Vergis** proviene de *Caprica* (universo *Battlestar Galactica*): Tomas Vergis fue el inventor legítimo del Meta-Cognitive Processor, la pieza que dio independencia cognitiva a las máquinas. El nombre reclama la metacognición para su fuente legítima. Y carga, de fábrica, el principio de diseño que gobierna la plataforma: en aquel relato, el sustrato metacognitivo **nunca funcionó hasta fusionarse con una consciencia viva**. El sustrato es **inerte hasta que algo lo anima** — el principio "aliento de vida": Vergis cobra vida solo cuando Mira y los agentes lo animan. La plataforma, por sí sola, es músculo en reposo; la cognición y los Botlets son lo que la actualizan.

## ¿Qué incluye?

Vergis empaqueta un conjunto inicial de componentes. Cada uno materializa una primitiva canónica, y se nombra aquí citándola:

- **Contrato abstracto del Botler** — la primitiva runtime de **Capa 3** (§5). El Botler de Vergis es genérico por definición: gestiona ciclo de vida, aislamiento y ejecución de *cualquier* Botlet sin entender su dominio. Expone los puntos de control —`capability_call`, `log`— en los que se enchufan los especialistas, y hace valer la validación de cada spec orquestando el punto de validación que el tipo de Botlet provee, sin ejecutarla con conocimiento de dominio.
- **Mira** — un **proto-Botlet platafórmico** (§5) de operación informativa. Su código es genérico —el motor compartido—; su especialización vive en una configuración composicional que el agente rellena en tiempo de Ingeniería. Cada Producto de Información es su propio Botlet, instancia especializada del motor común. Mira opera en **G1**: el agente configura, no escribe el cuerpo del motor.
- **Conjunto starter de Capabilities** — un repertorio mínimo de **Capabilities** canónicas (§5, sentido estricto: saber-hacer cognitivo de Capa 2) y los **Conectores** (Capa 4) que las alimentan, suficiente para componer los ejemplos.
- **Plantillas de Trust Infrastructure** — esqueletos del eje transversal (§5): políticas, append-only log, contrato declarativo de calidad (Frescura · SLA · Política de degradación · Audiencia · Política de refresh) que cualquier Botlet conforme puede declarar.
- **Ejemplos ejecutables** — casos completos y anonimizados que recorren la cadena de derivación `caso de uso → Botlets → proto-Botlets` y muestran las piezas operando juntas.

## ¿Por qué es production grade?

La implementación de referencia no es código didáctico ni prototipo. Es el **mismo runtime** que opera los productos comerciales del Grupo Ultra —**Agentia**, **Soveria**, **ultraPRO**— en operación productiva.

La diferencia entre Vergis público y esos productos **no es la calidad del código**, sino el **catálogo**. Los productos consumen la implementación de referencia pública **más un códice propietario** —en el caso del Grupo Ultra, **ucodex**— que cura proto-Botlets, Capabilities y patrones refinados por casos reales. El runtime es el mismo; lo que cambia es el repertorio pre-forjado que cada uno trae y el método con que lo forja y mantiene.

Esto importa para el lector que evalúa adoptar el canon. Descargar Vergis no es descargar una demo que habrá que reescribir para producción: es descargar la base sobre la que ya corren sistemas productivos. La ruta de un implementador no es "aprender con la referencia y luego comprar lo serio", sino "operar la referencia y curar el catálogo que el propio caso exige".

## ¿Cómo se adopta? — el modelo

El modelo de adopción es replicable por cualquier implementador, sin permiso ni contrato con un actor central:

1. **Consume** la implementación de referencia pública (Vergis, `AGPL`).
2. **Cura** su propio códice — su catálogo privado de proto-Botlets, Capabilities y patrones, refinado por sus casos.
3. **Ofrece** sus propios productos sobre esa base.

AgencyDomains.org **no es propiedad de un actor**: es base común. El Grupo Ultra es un adoptante más —con ucodex como su códice—, no el dueño de la plataforma de referencia. Cualquier otro implementador puede recorrer el mismo camino con un códice distinto. La spec pretende ser estándar de industria, no propiedad intelectual de un proveedor; la implementación de referencia hereda esa pretensión.

## ¿Cómo crece el catálogo? — catálogo común y efectos de red

Los proto-Botlets se acumulan en **catálogos compartidos** por comunidades de implementadores. Cada implementador que consume un proto-Botlet contribuye a su maduración: variantes nuevas, configuraciones probadas, refinamientos. Mientras más implementadores consumen un proto-Botlet, más rápido madura, más casos cubre y más confiable se vuelve. El implementador n+1 recibe versiones refinadas por los implementadores 1 a n — un efecto de red sobre la capacidad operativa.

Un catálogo no es necesariamente público. La pertenencia a una comunidad de catálogo admite cuatro **modos**:

| Modo | ¿Qué es? |
|------|----------|
| **Contrato privado** | Catálogo cerrado entre un cliente y su proveedor. |
| **Códice propietario** | Un implementador mantiene su catálogo privado curado (p. ej. ucodex). |
| **Catálogo público abierto** | AgencyDomains.org como ejemplar: cualquier implementador consume y contribuye. |
| **Acuerdo soberano** | AgencyDomains que adoptan estándares comunes sin contrato comercial directo. |

Los cuatro modos coexisten sobre la misma estructura canónica. Un proto-Botlet puede nacer en un códice propietario, madurar contra casos reales y promoverse al catálogo público cuando su naturaleza es estructural y no metodológica; o permanecer privado si encapsula ventaja competitiva. La estructura es común; la curaduría es de cada quien.

## ¿Cómo se contribuye?

La contribución a Vergis se gobierna por un proceso de propuestas público. A alto nivel:

- Una contribución **SHOULD** llegar como propuesta trazable —issue o request— antes que como código terminado, para que la discusión de diseño preceda a la implementación.
- Lo que se acepta es lo **estructural y reusable**: proto-Botlets de valor general, Capabilities canónicas, Conectores, refinamientos al contrato del Botler, mejoras al contrato declarativo de calidad.
- Lo que **no** sube a la referencia pública es el **método** y el **catálogo propietario**: cómo una organización particular hace Discovery, cura su códice o forja sus proto-Botlets de nicho. Eso vive en los cuerpos complementarios de cada implementador.
- El criterio de admisión es el mismo que separa canon de implementación: *¿es necesario para describir o ejecutar cualquier implementación conforme, o es una de N maneras posibles de hacerlo?* Lo primero pertenece a la referencia; lo segundo, a un códice.

Toda contribución aceptada queda bajo `AGPL` (código) y `GFDL` (docs), heredando la apertura de la base.

## ¿Conviven la referencia y los códices propietarios?

Sí, y sin tensión. La relación entre la implementación de referencia pública y los códices propietarios es **armónica por diseño**, no un equilibrio precario.

El runtime es común; el catálogo es propio. Un códice propietario no compite con Vergis: lo **consume** y lo **extiende**. Las mejoras al runtime fluyen hacia la base pública por la mecánica de la `AGPL`; las mejoras al catálogo permanecen donde su dueño decida, según el modo de pertenencia que elija. Un implementador no enfrenta la disyuntiva "abierto o cerrado": opera abierto en la base y elige, proto-Botlet a proto-Botlet, qué cura en público y qué retiene en su códice.

Esta coexistencia es la que hace sostenible el ecosistema. La base común evita que cada implementador reinvente el runtime; el catálogo propio preserva el espacio donde cada uno construye su ventaja. Sin la base común no habría interoperabilidad; sin catálogos propios no habría incentivo a invertir en curaduría profunda. La implementación de referencia sostiene ambos.

## Conformidad

Un sistema que pretenda presentarse como **implementación de referencia conforme** de AgencyDomains —no meramente como AgencyDomain conforme (§5)— satisface, además de los `MUST` de la spec, los siguientes requisitos. Convención IETF: `MUST` obligatorio, `SHOULD` fuertemente recomendado, `MAY` opcional.

| Requisito | Nivel |
|---|---|
| Disponible públicamente, descargable y ejecutable | **MUST** |
| Código bajo licencia libre con copyleft de red (`AGPL`) | **MUST** |
| Documentación bajo licencia libre (`GFDL`) | **MUST** |
| Botler genérico, sin especialización por dominio | **MUST** |
| Al menos un proto-Botlet platafórmico del catálogo, operando en G1 | **MUST** |
| Cadena de derivación trazable en sus ejemplos (`caso → Botlets → proto-Botlets`) | **MUST** |
| Contrato declarativo de calidad en los Botlets de ejemplo | **SHOULD** |
| Proceso de contribución público y gobernado | **SHOULD** |
| Conjunto starter de Capabilities y Conectores | **SHOULD** |
| Catálogo público abierto con efectos de red activos | **MAY** |

Una implementación de referencia que cumple todos los `MUST` es la prueba viva de que el canon es ejecutable. Vergis es tal implementación.

## Frontera de evolución

Tres áreas de la implementación de referencia están en evolución activa, en correspondencia con las fronteras de la spec misma.

La **generación operativa** es la primera. Vergis opera hoy en **G1**: el agente configura proto-Botlets pre-forjados del catálogo. La migración incremental hacia G2 y el horizonte asintótico G3 no exigen re-arquitectura; exigen que el estado del arte de la cognición avance. La referencia evolucionará su alcance de Ingeniería sin reescribir su estructura. La definición de las generaciones G1/G2/G3 vive en el Capítulo 5 §2 (y su ensayo de fondo, en el Epílogo); aquí solo se sitúa a Vergis dentro de ellas.

La **federación de catálogos** es la segunda. Los modos de pertenencia están descritos; el protocolo concreto por el cual catálogos soberanos descubren, versionan y reconcilian proto-Botlets entre sí es trabajo abierto, en correspondencia con la frontera de federación entre AgencyDomains.

La **amplitud del catálogo público** es la tercera. El conjunto starter cubre lo necesario para los ejemplos; el catálogo público crecerá por contribución de la comunidad, y su maduración seguirá la dinámica de efectos de red descrita arriba. La velocidad de ese crecimiento depende de la comunidad de implementadores, no de un plan central.
