# Casos de Uso

*Del diagnóstico al portafolio: cómo se prioriza la transformación*

---

## Introducción · La Tesis

Los modelos diagnósticos responden *dónde está* la organización; los instrumentos de levantamiento responden *cómo es* su terreno real. Falta la tercera pregunta, la que convierte el diagnóstico en movimiento: **¿qué hacemos primero?**

Esa pregunta tiene una mala respuesta tradicional — la lista de iniciativas armada por intuición, donde conviven el proyecto favorito del gerente, la demo que impresionó en una feria y el pendiente histórico de TI. Y tiene una respuesta disciplinada: un **portafolio de casos de uso** — un catálogo estructurado donde cada caso está clasificado por nivel de madurez requerido, por beneficiario del impacto y por dominio de negocio, de modo que la priorización sea una decisión estratégica explícita y no una acumulación de ocurrencias.

Este capítulo define las piezas de ese portafolio: la distinción entre **casos de uso** y **soluciones de valor**, las **tres dimensiones de clasificación**, el marco de priorización **Citizen / City / DUAL** con sus dos estrategias canónicas, y la disciplina de honestidad sobre el ROI. Cierra con un portafolio real — cien casos para gobierno local — que ilustra el sistema completo en operación.

---

## Casos de Uso y Soluciones de Valor

La primera distinción del portafolio es de granularidad, y separar las dos piezas evita un error que arruina catálogos enteros: mezclar el ladrillo con el edificio.

Un **Caso de Uso (CU)** es el bloque atómico: una capacidad específica, acotada y *reutilizable*. "Detección de anomalías en gastos", "chatbot de atención 24/7", "clasificación automática de reclamos". Un CU se describe por lo que hace, por qué la IA lo hace mejor que la alternativa tradicional, y qué madurez exige de la organización. Su valor está en la reutilización: el mismo CU puede participar en varias soluciones distintas.

Una **Solución de Valor (SV)** es la configuración estratégica: un conjunto de CU integrados que, juntos, resuelven un problema de negocio completo y se presentan ante un decisor como una unidad con propuesta de valor propia — problema, solución, métricas, retorno. "Gestión financiera autónoma" no es un CU: es una SV que integra la gestión integral del presupuesto, el análisis financiero, la proyección continua y la reasignación automática de partidas.

La relación es de composición, no de jerarquía exclusiva: un CU puede venderse solo (venta modular, cuando el cliente busca una capacidad específica) o como componente de una SV (venta integral, cuando busca la solución llave en mano). El portafolio sano mantiene los dos catálogos vivos y enlazados — cada CU declara en qué SV participa; cada SV lista los CU que integra.

---

## Las Tres Dimensiones de Clasificación

Cada caso del portafolio se clasifica en tres dimensiones ortogonales. Las tres juntas convierten un listado plano en un instrumento de decisión.

### Dimensión 1 · Nivel de madurez requerido

Cada CU exige un nivel mínimo de madurez organizacional para operar — el nivel MOTOR de la organización que puede ejecutarlo (y, según el caso, la etapa IRIS que su componente de información presupone). Un chatbot con datos enmascarados es ejecutable en los niveles tempranos; un agente que gestiona presupuesto con autoridad organizacional exige los niveles altos; una red inter-organizacional de agentes, el nivel máximo.

Esta dimensión es la que ancla el portafolio al diagnóstico: **el nivel del caso se cruza con el nivel de la organización.** Los casos del nivel actual son ejecutables hoy — ahí viven los *quick wins*. Los casos un nivel por encima son la frontera alcanzable — el *sweet spot* donde la ambición tracciona la madurez sin romperla. (Este *sweet spot* es local al portafolio — tu nivel actual más uno —, distinto del Sweet Spot de mercado que MOTOR sitúa en el Nivel 4.) Los casos varios niveles por encima son visión de largo plazo: valiosos para mostrar el destino, peligrosos como compromiso inmediato.

### Dimensión 2 · Beneficiario del impacto (Citizen / City / DUAL)

La segunda dimensión clasifica por *quién percibe el beneficio* — y se desarrolla en la sección siguiente, porque es el corazón político del portafolio.

### Dimensión 3 · Dominio de negocio

La tercera dimensión segmenta por área temática del negocio — atención al cliente externo, gestión interna y finanzas, operaciones e infraestructura, servicios especializados. Su función es práctica: cuando el decisor tiene un foco ("mi problema es seguridad", "mi crisis es financiera"), el portafolio debe poder filtrarse por dominio en segundos y presentar la oferta relevante completa — los CU del dominio, las SV que los integran, y el camino de escala.

---

## El Marco Citizen / City / DUAL

Cualquier organización que sirve simultáneamente a una audiencia externa (beneficiaria del servicio) y una audiencia interna (operadora) vive bajo **doble presión**: la audiencia externa pide mejor servicio; la interna pide eficiencia operacional. Un caso de uso puede beneficiar a una, a la otra, o a las dos.

El marco clasifica cada caso según quién percibe el beneficio directo:

| Clasificación | Quién se beneficia | Función política/estratégica |
|---|---|---|
| **CITIZEN** | La audiencia externa (ciudadano, cliente final, usuario del servicio) | Genera apoyo visible y legitimidad pública |
| **CITY** | La audiencia interna (la organización, su equipo, su estructura financiera) | Genera eficiencia, compliance, sostenibilidad |
| **DUAL** | Ambas simultáneamente | Genera consenso: cada actor relevante tiene su victoria visible |

El marco nació en gobierno local — de ahí sus nombres — pero la estructura es genérica: en banca retail, CITIZEN es el cliente y CITY es compliance y operaciones; en salud, el paciente y los equipos clínicos; en telecomunicaciones, el suscriptor y la operación de red. En todos los casos la lógica es la misma: la organización tiene dos relaciones simultáneas que pueden alinearse o tensionarse, y la transformación puede priorizar el lado externo, el interno, o el cruce.

**Por qué es transversal a IRIS y MOTOR:** el marco no clasifica por eje de transformación (saber/hacer) sino por beneficiario del impacto. Un caso CITIZEN puede ser del eje SABER (el cliente consulta su trámite en lenguaje natural) o del HACER (un agente lo atiende 24/7). Por eso el marco vive a nivel AURA: un diagnóstico completo evalúa posición IRIS, posición MOTOR, y mix de prioridad Citizen/City/DUAL para el roadmap.

### Las dos estrategias canónicas

Al armar el roadmap, el marco se traduce en dos estrategias arquetípicas con perfiles de inversión y retorno distintos.

**Estrategia A · Citizen-First.** Priorizar casos visibles a la audiencia externa para ganar apoyo, legitimidad y momentum. Aplica cuando el liderazgo está bajo presión de stakeholders externos, cuando la confianza pública está baja y hay que reconstruirla, o cuando el costo político de no actuar excede el costo financiero de actuar. Su pool son los casos CITIZEN más los DUAL. Su riesgo: ROI financiero más bajo o difuso — se gana legitimidad sin necesariamente reducir costo operacional.

**Estrategia B · City-First.** Priorizar eficiencia interna, ahorro y compliance antes de exponer nada a la audiencia externa. Aplica en crisis fiscal, con equipos sobrecargados que necesitan alivio antes de cualquier expansión de servicio, o cuando la urgencia es regulatoria. Su pool son los casos CITY más los DUAL. Su riesgo: la audiencia externa no percibe beneficio — la organización mejora pero no lo capitaliza.

**El núcleo común — los casos DUAL.** Aparecen en ambas estrategias y son la intersección óptima: la audiencia externa los percibe, la organización los cuantifica, y frente a cualquier crítico son defendibles. Construir el roadmap con priorización máxima de casos DUAL es la jugada de menor fricción — y diseñar casos para que *sean* DUAL desde su concepción es disciplina, no suerte.

Tres notas de uso cierran el marco. Primera: **no forzar una estrategia** — una organización grande con presupuesto puede combinar ambas; una en crisis fiscal probablemente necesita City-First puro el primer año; la estrategia se elige por contexto, no por ideología. Segunda: los casos DUAL son la moneda más cara del portafolio — escasean y se diseñan. Tercera: **el marco no reemplaza al diagnóstico** — aplicar Citizen-First sin haber resuelto la gobernanza de IA (el paso del Nivel 1 al 2 de MOTOR) es construir visibilidad sobre arena; el marco prioriza qué atacar primero *dentro* de cada nivel, no sustituye la trayectoria de madurez.

---

## La Disciplina del ROI

Un portafolio pierde su utilidad el día que el decisor deja de creerle. Y la forma más rápida de perder credibilidad es presentar retornos estimados como si fueran medidos.

La disciplina tiene tres reglas. **Primera: todo ROI estimado se declara referencial** — visible, sin vergüenza y sin asterisco escondido — hasta que exista una línea base validada. **Segunda: el valor social se separa del retorno financiero.** Hay casos cuyo beneficio dominante es intangible — deserción escolar detectada a tiempo, patrimonio preservado, salud pública vigilada — y forzarlos a una cifra de ahorro los desnaturaliza; el portafolio los marca como casos de valor social y los defiende en esos términos. **Tercera: la línea base se valida antes de declarar retorno** — un protocolo de validación independiente del baseline es parte del portafolio, no un lujo posterior.

A esto se suma la calidad formal del catálogo: terminología consistente, descripciones que distinguen *qué hace* el caso de *por qué la IA* lo hace mejor, y referencias cruzadas completas entre CU y SV. Un portafolio de cien casos es un producto editorial — y se gobierna como tal, con su propio framework de calidad y revisiones sistemáticas.

---

## Un Portafolio Real: Cien Casos para Gobierno Local

El sistema completo — CU/SV, tres dimensiones, marco de priorización — se ilustra mejor con el portafolio donde nació: el inventario de transformación agentiva para gobierno municipal, desarrollado por ultraBASE durante 2025.

**La escala:** 100 casos de uso atómicos y 30 soluciones de valor, con un retorno agregado estimado (referencial) del orden de USD 118M/año para el conjunto, distribuidos en cuatro dominios de negocio: atención ciudadana y comunicación (17%), gestión interna —legal, RRHH, finanzas, compras y presupuesto— (37%), infraestructura, vialidad, seguridad y emergencias (24%), y servicios —salud, educación, cultura, deporte y medioambiente— (22%).

**La distribución por madurez** cuenta la historia de la transformación completa:

| Nivel de madurez | CU | Carácter de los casos |
|---|---|---|
| 1–2 (IA gobernada, asistiva) | 34 | Análisis de documentos, chatbots con datos protegidos, auditoría automática — los *quick wins* |
| 3 (delegación de tareas) | 21 | Trámites de punta a punta, planificación multi-proyecto, casos complejos multi-sistema |
| 4 (operación autónoma 24/7) | 19 | Detección de fraude en tiempo real, patrullaje predictivo, respuesta automática a emergencias |
| 5 (capacidades predictivas propias) | 9 | Deterioro de pavimento, evaluación sísmica post-terremoto, optimización de tráfico |
| 6 (agentes con autoridad de gestión) | 6 | Agentes que gerencian equipos de 25 funcionarios, coordinan 45 proyectos simultáneos, gestionan USD 45M de presupuesto |
| 7 (ecosistema inter-organizacional) | 11 | Redes regionales de seguridad y residuos, marketplace de agentes públicos, agentes que proponen políticas |

La pirámide es elocuente: un tercio del portafolio es ejecutable en los niveles tempranos de madurez — ahí se construye el momentum — mientras la punta describe un horizonte donde agentes de distintas organizaciones cooperan en red. Y la distribución por beneficiario quedó razonablemente balanceada — 31 CITIZEN, 38 CITY, 31 DUAL — lo que permite servir ambas estrategias canónicas desde el mismo catálogo.

**Las soluciones estrella** muestran el patrón de composición. La SV mejor rankeada del portafolio, *Gestión Financiera Municipal Autónoma* — una solución de nivel 6 —, integra cuatro CU, entre ellos el agente que gestiona el presupuesto completo (nivel 6) y el que reasigna partidas automáticamente (nivel 6), apoyados en capacidades de análisis financiero y proyección de niveles previos. La segunda, *Municipio sin Papeles* — una solución de nivel 3 —, integra cinco CU para la digitalización total de los trámites que el ciudadano percibe. Que el #1 sea nivel 6 y el #2 sea nivel 3 no es contradicción: es el portafolio haciendo su trabajo — mostrar simultáneamente la ambición del destino y el paso ejecutable de mañana.

**Lo que el caso enseña** trasciende al sector público. Primero, que el portafolio se *cura*: este pasó por siete iteraciones de versión y casi quinientas mejoras de calidad antes de considerarse presentable. Segundo, que las dimensiones de clasificación se ganan iterando con el decisor real — el área temática nació de una necesidad concreta de segmentación comercial, no de un ejercicio de gabinete. Tercero, que la honestidad del ROI referencial no debilitó el portafolio: lo hizo defendible.

---

## ¿Cómo usar este marco?

1. **Diagnosticar primero.** Posición IRIS, posición MOTOR. Sin esto, el portafolio no tiene ancla.
2. **Inventariar con las tres dimensiones.** Cada caso candidato se clasifica por nivel requerido, beneficiario y dominio. Lo que no se puede clasificar no está suficientemente definido.
3. **Separar CU de SV.** Los bloques atómicos en un catálogo; las configuraciones estratégicas en otro; las referencias cruzadas, completas.
4. **Elegir estrategia por contexto.** Citizen-First, City-First o mixta — decisión explícita del liderazgo, revisable, con los casos DUAL siempre al frente.
5. **Atacar el nivel actual + 1.** Quick wins del nivel vigente para el momentum; el sweet spot un nivel arriba para la tracción; el resto del portafolio como horizonte declarado.
6. **Declarar el ROI con honestidad.** Referencial hasta validar línea base; valor social en sus propios términos.

El portafolio es el instrumento que cierra el camino AURA: la visión define el destino, IRIS y MOTOR ubican a la organización, Data Canon y Wingmap preparan el terreno — y el portafolio decide, con disciplina, el siguiente paso.
