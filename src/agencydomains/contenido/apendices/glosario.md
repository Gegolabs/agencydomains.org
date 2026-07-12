# Apéndice A · Glosario canónico

> Términos canónicos del libro con definición precisa y referencia al capítulo donde se desarrollan.

## A

### A2A — Agent-to-Agent

Nombre reservado para la **relación** entre AgencyDomains distintos (agentes distintos) — federación, trabajo abierto. La comunicación **dentro de** un mismo AgencyDomain no es "A2A interna": es **coordinación intra-AgencyDomain** entre Botlers del mismo agente, y cuando usa este transporte se dice **vía el protocolo `A2A`** (`A2A` como nombre propio del protocolo). La interfaz Capa 2 → Capa 3 (Cognición → Botler) no va por `A2A` sino por `MCP`.

*Ver: Capítulo 4, sección "Capa 3 — Autonomía", Capítulo 5 §1; entradas **coordinación intra-AgencyDomain**, **MCP**.*

### AgencyDomain

Ámbito computacional con identidad propia donde habitan agentes autónomos y Botlets en ejecución, donde se alojan y ejecutan las Capabilities que les dan el saber-hacer, y donde viven los recursos que los sostienen. Constituye la unidad mínima de despliegue de un sistema agentivo productivo.

Las palabras cargan corporeidad. **Space** (*espacio*) y **WorkSpace** (*espacio de trabajo*: Google Workspace, Microsoft 365, Notion) cargan corporeidad humana. El agente no tiene cuerpo: tiene jurisdicción. Donde el humano tiene Space (WorkSpace), el agente tiene **Domain (AgencyDomain)** — el ámbito computacional donde ejerce agencia. La palabra latina que nombra exactamente eso es Domain (`dominium`: ámbito de pertenencia y soberanía).

Linaje: como **JavaSpaces** (JSR-000148, 1999) formalizó los espacios distribuidos para sistemas Java, esta especificación formaliza los **AgencyDomains** para sistemas agentivos. Lo que en 1999 se nombraba como "espacio" se nombra mejor en 2026 como "domain": un Java *Space* era espacio computacional para procesos sin cuerpo; un Agency *Domain* es ámbito de jurisdicción para agentes con agencia.

Tres regímenes posibles: **privado**, **público**, **híbrido**.

*Ver: Capítulo 5 §1.*

### Agente

Sistema computacional que actúa con cierto grado de iniciativa para producir resultados en nombre de un usuario u organización. El término paraguas cubre tres miembros:

- **Asistente** — agente reactivo (Capa 2).
- **Agente Autónomo** — agente proactivo con vida persistente (Capa 3); habitante del AgencyDomain.
- **Agentlet** — agente empaquetado de charter acotado (Capa 3); pieza de catálogo, no habitante.

*Ver: Capítulo 5 §5 (los dos modos) y §7 (el Agentlet).*

### Agent First

Principio rector de diseño de la Arquitectura Agentiva: ante cualquier disyuntiva, se prioriza la experiencia del agente sobre la del humano. El agente es el usuario primario; las necesidades del humano se resuelven en una capa de gestión sin degradar lo que el agente ve y puede hacer.

*Ver: Capítulo 4, sección "El principio rector — Agent First".*

### Agentlet

**Octava primitiva canónica**. Unidad empaquetada de Capa 3 (Autonomía), hermana del Botlet, cuyo cuerpo de ejecución **invoca inferencia acotada** — un modelo dimensionado a la tarea, dentro de un charter declarado en el spec. Casa canónica de la tarea **recurrente en forma pero interpretativa en cada instancia** (clasificar, triar, resumir, extraer, juzgar). Su juicio opera *dentro* del charter, nunca sobre el charter: **el Agente tiene agenda; el Agentlet tiene charter**. Instancia de un **proto-Agentlet**; hospedado por el Botler (toda su inferencia cursa por el punto de control `cognition_call` del handle); su fallback escala a la Cognición plena. Miembro del paraguas **Agente**, pieza de catálogo y no habitante. Peldaño económico intermedio entre el Botlet (inferencia cero) y la Cognición (inferencia plena).

*Ver: Capítulo 5 §7; entradas **Botlet**, **Botler**, **proto-Agentlet**.*

### AgentNation

AgencyDomain en régimen público que adopta explícitamente el modelo de ciudadanía agentiva — los agentes que lo habitan no son listados como productos sino reconocidos como ciudadanos del espacio, con identidad pública sostenida, soberanía sobre su territorio (Domain) y economía propia. La distinción frente a un marketplace es ontológica: marketplace lista productos; AgentNation reconoce ciudadanos. Categoría institucional emergente; trabajo arquitectónico abierto.

*Ver: Epílogo, sección "Frontera 4 — el horizonte institucional".*

### Agéntico

Mundo donde los agentes son herramientas complementarias que extienden las aplicaciones existentes. Los humanos siguen abriendo aplicaciones para hacer su trabajo. Las interfaces tradicionales persisten; los agentes las potencian. Es **evolución incremental**.

*Ver: Capítulo 1, sección "Lo que separa la línea — Agéntico y Agentivo en detalle".*

### Agentivo (Mundo Agentivo)

Mundo donde los agentes son la interfaz única. Las aplicaciones colapsan. El humano deja de abrir aplicaciones; conversa con agentes que tienen acceso a sistemas y datos. Es **transformación fundamental**.

La distinción definitoria entre Agéntico y Agentivo: *¿el humano abre aplicaciones para hacer su trabajo?*

*Ver: Capítulo 1, sección "Lo que separa la línea — Agéntico y Agentivo en detalle", Capítulo 2.*

### Append-only log

Registro inmutable, encadenado criptográficamente, de toda acción del agente. Componente central del pilar de Auditoría de Trust Infrastructure. Formato y propiedades canónicas en Capítulo 8, sección "Formato del append-only log".

### Aprobación humana

Mecanismo de Gobernanza por el cual una operación del agente se detiene y solicita autorización de un humano antes de ejecutarse. Disparada por política explícita, por umbral o por incertidumbre del agente. Protocolo canónico en Capítulo 8, sección "Protocolo de aprobación humana".

### Arquetipo estratégico

Patrón de posicionamiento en el espacio cobertura × profundidad de la cadena de valor de IA. Cuatro arquetipos canónicos:

- **Plataforma integral** — cobertura amplia; profundidad Core en su eslabón nativo y Plataforma en los adyacentes.
- **Especialista vertical** — cobertura focal, profundidad Core.
- **Infraestructura de dominio** — cobertura zonal, profundidad Core en varios eslabones.
- **Proveedor de sustrato** — cobertura mínima, profundidad Infraestructura.

*Ver: Capítulo 6 §1.*

### Arquitectura Agentiva

Diseño técnico que materializa el Mundo Agentivo. Especificación de cuatro capas con responsabilidades distintas (Interacción, Cognición, Autonomía, Acceso), gobernadas por Trust Infrastructure transversal y ordenadas por el principio Agent First.

*Ver: Capítulo 4 — la especificación completa.*

### Asistente

Modo del agente: reactivo, responde cuando se le solicita, sin Botlets propios, sin vida persistente. Vive en Capa 2 (Cognición). Distinto del Agente Autónomo.

*Ver: Capítulo 5 §5.*

### Atención

Uno de los **tres tiempos del agente** (Cap 4). Tiempo en que el agente interactúa con usuarios o eventos en tiempo real. Capa 1 activa, conversación viva, ejecución de Botlets que sostienen operación, escalamientos cuando corresponde. Camino crítico — donde la organización siente al agente, donde el SLA importa, donde el costo del error se materializa. Régimen prioritario; métricas: satisfacción, latencia, tasa de resolución sin escalamiento.

*Ver: Capítulo 4, sección "Los tres tiempos del agente".*

### Auditoría

Pilar 2 de Trust Infrastructure. Capacidad de reconstruir, después del hecho, **qué hizo el agente, cuándo, por qué y sobre qué datos** — con fidelidad suficiente para análisis forense, cumplimiento regulatorio o disputa contractual.

Mecanismos canónicos: el **append-only log** inmutable (componente central), el trace de cada acción, el lineage de decisiones y el identity tagging por acción. Exige diseño explícito desde el inicio — no emerge naturalmente de una arquitectura agentiva.

*Ver: Capítulo 5 §4; Capítulo 8; entradas **Append-only log**, **Trace**.*

## B

### BCA — Bounded Concerns Architecture

Arquitectura del estado pre-agentivo: el patrón de separación de incumbencias (presentación humana, orquestación, lógica de dominio, persistencia, dominio propio vs ajeno) sobre el que se levanta el Mundo Agentivo. Sus siete separaciones canónicas se mapean celda a celda a las cuatro capas de la Arquitectura Agentiva; la séptima (comportamiento procedural vs agéntico) es la grieta de entrada.

*Ver: Capítulo 3 — la especificación completa.*

### Botlet

Unidad de automatización auto-evolutiva. Código tradicional (no-LLM) generado por un agente para ejecutar tareas repetitivas sin invocar cognición costosa. Es la **memoria muscular** del agente.

Ciclo canónico **95/4/1**: 95% ejecución normal, 4% cambio detectado, 1% regeneración. Garantía de fallback: si falla, la cognición ejecuta manualmente.

*Ver: Capítulo 5 §2.*

### Botlet de fachada

Botlet de **Capa 3** que expone una superficie con contrato estable en **Capa 1** (POS, pantalla de cocina, dashboard, panel industrial), con identidad humana propagada hacia Capa 4. Tipo de Botlet que la **topología paralela** (Cap 4) distingue del Botlet de herramienta interna de la cognición. Atraviesa la vía `Capa 1 → Capa 3 → Capa 4` sin invocar Capa 2.

*Ver: Capítulo 4, sección "La topología paralela".*

### Botlet de operación

Botlet de **Capa 3 (Autonomía)** que ejecuta lógica de negocio invocada desde la Capa 1 (vistas y shells). Ejemplos canónicos: `Cobrar mesa`, `Imprimir comanda`, `Cerrar turno`, `Consolidar inventario`. Es el activo más reutilizable del catálogo: una operación puede ser invocada desde múltiples vistas dentro de múltiples shells. Vive en Capa 3 (no en Capa 1). Distinto del Botlet de superficie y del Botlet de vista, que son superficie.

*Ver: Capítulo 4 §1, sección "Composición de la superficie · shell, vista, operación".*

### Botlet de superficie (shell)

Botlet de **Capa 1 (Interacción)** que actúa como contenedor de una superficie: layout, navegación entre vistas, ciclo de vida de la sesión, estado compartido. Específico de cada producto — encapsula identidad. Hay típicamente un shell por rol operativo principal (POS de sala, panel de caja, dashboard ejecutivo móvil). Es el menos reutilizable de los tres tipos de Botlets de presentación. Distinto del Botlet de vista (que vive dentro del shell) y del Botlet de operación (que vive en Capa 3).

*Ver: Capítulo 4 §1, sección "Composición de la superficie · shell, vista, operación".*

### Botlet de vista

Botlet de **Capa 1 (Interacción)** que materializa una pantalla o panel dentro de una superficie. Ensambla Facetas más lógica de orquestación. Las vistas que se usan en varios shells se extraen como Botlets propios (vistas reutilizables). Distinto del Botlet de superficie (contenedor) y del Botlet de operación (ejecución en Capa 3).

*Ver: Capítulo 4 §1, sección "Composición de la superficie · shell, vista, operación".*

### Botlet emergente

Botlet generado por **Pattern Recognition** cuando la cognición detecta un patrón repetitivo no anticipado por el diseño. Distinto del Botlet seed por su origen, no por sus propiedades operativas.

*Ver: Capítulo 5 §2.*

### Botlet en aprendizaje

Fase intermedia de la trayectoria de madurez del Botlet. Ya pasó por las primeras invocaciones reales y fue regenerado varias veces para incorporar variantes del ambiente. Proporción típica: `85/12/3`. Puede operar con red intermitente; no aún con red ausente prolongada.

*Ver: Capítulo 5 §2, sección "Madurez del Botlet".*

### Botlet junior

Fase inicial de la trayectoria de madurez del Botlet. Recién generado, conoce el ambiente solo en la versión observada al crearlo. Proporción típica: `60/35/5`. Depende fuertemente de la disponibilidad de la cognición para fallback y aprendizaje.

*Ver: Capítulo 5 §2, sección "Madurez del Botlet".*

### Botlet seed

Botlet generado por la cognición a pedido del equipo de diseño, como parte del producto inicial. La cognición ejecuta la implementación; la decisión de existir es del diseño, no de Pattern Recognition. Distinto del Botlet emergente. Las **GUIs persistentes generadas como Botlets de fachada** (Cap 4 §1) son Botlets de fachada seed — Botlets de Capa 3 cuya superficie estable vive en Capa 1.

*Ver: Capítulo 5 §2, sección "Botlets seed vs Botlets emergentes".*

### Botlet senior

Fase madura de la trayectoria del Botlet. Ya incorporó las variantes del ambiente. Proporción típica: `99+/<1/~0`. **Sus únicos modos de fallo son exógenos** (energía, hardware, red catastrófica) — no aprendizaje pendiente. **Operable offline confiablemente** cuando la cognición no está disponible. Base estructural del modo offline en Capa 3 distribuida.

*Ver: Capítulo 5 §2, sección "Madurez del Botlet".*

### Botler

Runtime genérico de Capa 3 (Autonomía) que ejecuta las **unidades** de la capa — Botlets y Agentlets — sin entender su dominio. Invisible al usuario. La Cognición (Capa 2) lo comanda por una interfaz interna cuyo transporte natural es `MCP` — el Botler expone servidor(es) `MCP` y la Cognición es el cliente; esto **no es `A2A`**.

Relación: 1 Proceso = 1 Botler + N unidades (instanciada por especie: N Botlets, N Agentlets, o mezcla).

**Handle controlado** — punto de acceso ligado que el Botler entrega a la unidad en cada invocación (objeto con `capability_call`, `log` y — para Agentlets — `cognition_call`, enlazados al Botler). Hace el bypass estructuralmente imposible, no solo prohibido.

### Botler central

Componente de la **Capa 3 distribuida** (Cap 5 §1) que vive típicamente en cloud y hospeda los Botlets de orquestación, planificación, reportería y decisiones globales. Mantiene la BD consolidada y coordina con N Botlers edge mediante coordinación intra-AgencyDomain (vía el protocolo `A2A`). Distinto del Botler edge.

*Ver: Capítulo 5 §1, sección "Capa 3 distribuida".*

### Botler edge

Componente de la **Capa 3 distribuida** (Cap 5 §1) que vive en un sitio físico específico y hospeda los Botlets transaccionales locales. Mantiene BD local del sitio y cola de eventos hacia el Botler central. Opera offline cuando la red se cae. Uno por cada sitio físico del AgencyDomain.

*Ver: Capítulo 5 §1, sección "Capa 3 distribuida".*

### BYOModel — Bring Your Own Model

Patrón configurable de la Capa 2 mediante el cual el cliente sustituye el proveedor de cognición default del AgencyDomain por uno propio. Análogo al patrón BYOK/BYOIP del campo cloud. Habilita multi-tenancy con cognición heterogénea y respeta la soberanía cognitiva — el cliente decide quién procesa sus prompts. La spec lo exige como propiedad SHOULD para arquitecturas que aspiren a operar en mercados regulados.

*Ver: Capítulo 4, sección "Capa 2 — Cognición"; Capítulo 5 §2.*

## C

### Cadena de derivación

Relación estructural `casos de uso documentados → Botlets necesarios → proto-Botlets requeridos del catálogo`. Cada caso requiere cero, uno o varios Botlets (algunos los resuelve la cognición sin Botlet); cada Botlet es instancia de un proto-Botlet. Propiedad exigida: todo Botlet conforme MUST poder trazarse en esta cadena, y el append-only log registra el proto-Botlet de origen de cada Botlet instanciado.

*Ver: Capítulo 5; entradas **Botlet**, **proto-Botlet**.*

### Cadena de valor de IA

Modelo bidimensional para clasificar a cualquier actor en la industria de IA: **once eslabones secuenciales** (cobertura) × **cuatro profundidades** (cómo participa en cada eslabón).

*Ver: Capítulo 6 §1.*

### Capa 1 — Interacción

Capa de la Arquitectura Agentiva. Interfaz humano-IA. Multi-canal: chat, voz, **GUI on-the-fly**, **GUI persistente como Botlet de fachada**, señalética, API directa. Tres regímenes canónicos de generación de GUI distinguen el modo agentivo del precreado tradicional.

*Ver: Capítulo 4, sección "Tres regímenes de GUI en la Capa 1 agentiva".*

### Capa 2 — Cognición

Capa de la Arquitectura Agentiva. El cerebro del agente. Razonamiento, planificación, aplicación de Capabilities, generación de Botlets.

*Ver: Capítulo 4, sección "Capa 2 — Cognición".*

### Capa 3 — Autonomía

Capa de la Arquitectura Agentiva. Vida persistente del agente. Ejecución de unidades — Botlets y Agentlets —, monitoreo continuo, coordinación intra-AgencyDomain (vía el protocolo `A2A`).

*Ver: Capítulo 4, sección "Capa 3 — Autonomía".*

### Capa 3 distribuida

Patrón canónico de la Capa 3 para AgencyDomains con presencia física múltiple (gastronomía multilocal, retail en cadena, logística, salud con red de centros, banca con sucursales). Compone **un Botler central** (cloud, orquestación, BD consolidada) con **N Botlers edge** (uno por sitio, BD local, Botlets transaccionales), coordinados por coordinación intra-AgencyDomain (vía el protocolo `A2A`) entre Botlers del mismo AgencyDomain. Distinto de federación entre AgencyDomains; distinto de Cluster simple. Habilita modo offline como propiedad estructural cuando los Botlets edge son senior.

*Ver: Capítulo 5 §1, sección "Capa 3 distribuida".*

### Capa 4 — Acceso

Capa de la Arquitectura Agentiva. Poder de ejecución real sobre sistemas, datos y agentes externos. Trust Infrastructure ejercida en el punto de acción.

*Ver: Capítulo 4, sección "Capa 4 — Acceso".*

### Capability

Saber-hacer **cognitivo**, interpretativo, decisional (sentido estricto: **Capa 2 · Cognición**) que un agente comprende y aplica. Modular y composable. Organizada en árbol jerárquico (Finance, Sales, Manufacturing, Telecom, etc.). Expone operaciones internas (**features**) y es **portable**: una Capability conforme corre en cualquier AgencyDomain conforme. El saber acceder a sistemas fuente no es Capability sino **Conector** (Capa 4); la confección de un instrumento canónico es **Plantilla** (Capa 1).

NO es plugin. NO es prompt. NO es tool. Es **saber**.

La localidad y la disponibilidad offline se declaran sobre el **Conector** que acompaña a la Capability — el acceso es lo que reside y necesita red, nunca el saber (Cap 5 §3). Los componentes regulados declaran además su régimen regulatorio; el Conector certificado es inmutable entre auditorías.

*Ver: Capítulo 5 §3.*

### Capability regulada

Capability que porta el **saber normativo** de un dominio regulado — qué exige la norma, cómo se interpreta, qué hacer ante rechazo del regulador. Acompaña a un **Conector certificado**, que es donde reside la certificación regulatoria: el Botlet orquesta y formatea; el Conector certificado ejecuta la operación regulada (emisión DTE bajo norma SII, cobro con tarjeta bajo PCI-DSS, dispensación farmacéutica) y devuelve el comprobante; la Capability regulada aporta el criterio con que la cognición gobierna el conjunto. Los Conectores certificados son inmutables entre auditorías; cambian solo bajo proceso regulatorio.

*Ver: Capítulo 5 §3, sección "La certificación regulatoria reside en el componente certificado".*

### Catálogo común / efectos de red

Principio por el cual los proto-Botlets se acumulan en catálogos compartidos por comunidades de implementadores: cada implementador que consume contribuye a la maduración (variantes, configuraciones probadas, refinamientos), y el implementador n+1 recibe versiones refinadas por los implementadores 1..n. Modos de pertenencia: **contrato privado** · **códice propietario** · **catálogo público abierto** (AgencyDomains.org) · **acuerdo soberano** (entre AgencyDomains que adoptan estándares comunes sin contrato comercial directo).

*Ver: entrada **proto-Botlet**.*

### Cluster

Grupo de instancias del **mismo** AgencyDomain que comparten carga operativa. Distinto de federación (que es entre AgencyDomains **distintos**).

*Ver: Capítulo 5 §1.*

### códice propietario

Catálogo privado de proto-Botlets, Capabilities y patrones que un implementador cura sobre la implementación de referencia pública, refinado por sus casos reales. Es uno de los cuatro modos de pertenencia a una comunidad de catálogo. El runtime es común (la implementación de referencia); el códice es propio — encapsula la ventaja competitiva de cada implementador. Instancia canónica: **ucodex**, el códice del Grupo Ultra.

*Ver: Capítulo 9; entradas **Catálogo común / efectos de red**, **proto-Botlet**, **ucodex**.*

### Conector

Saber acceder a sistemas fuente: conexión con poder de ejecución, **no saber cognitivo**. **Capa 4 · Acceso.** En el mapa legacy→agentivo, una **API** se convierte en **Conector**, no en Capability. Esquema de integración: relevar · configurar · probar · certificar.

*Ver: Capítulo 4, sección "Capa 4 — Acceso"; entradas **Capability**, **Tool**.*

### Conector cloud-resident

Conector cuyos componentes viven en un servicio remoto. Ejemplos canónicos: DTE-SII (sin cliente local), Transbank Onepay, API meteorológica. Típicamente online-only — sin red no hay invocación posible. Distinto de edge-resident e híbrido.

*Ver: Capítulo 5 §3, sección "Localidad y disponibilidad".*

### Conector edge-resident

Conector cuyos componentes viven en el sitio físico, asociados a hardware o sistemas locales. Ejemplos canónicos: ESC/POS-Printer, Cash-Drawer, Pinpad-Local, Sensor-Temperatura. Típicamente offline-capable — operan contra el hardware del sitio sin necesitar red.

*Ver: Capítulo 5 §3, sección "Localidad y disponibilidad".*

### Conector híbrido

Conector con componente local y componente cloud. La parte local opera offline; la parte cloud sincroniza cuando hay red. Típicamente offline-capable con encolamiento. Ejemplos canónicos: Cliente-DTE (firma localmente, encola, envía al SII cuando vuelve la red), Cliente-Pinpad-Procesamiento-Diferido.

*Ver: Capítulo 5 §3, sección "Localidad y disponibilidad".*

### Conector offline-capable

Conector que ejecuta sin red. Si su contrato externo exige eventualmente comunicación cloud, **encola** y emite hacia afuera cuando la red vuelve. Típicos: edge-resident e híbridos.

*Ver: Capítulo 5 §3, sección "Localidad y disponibilidad".*

### Conector online-only

Conector que requiere red para ejecutar. Sin red, la invocación falla. Típicos: cloud-resident sin componente local.

*Ver: Capítulo 5 §3, sección "Localidad y disponibilidad".*

### Conformed dimensions

Concepto de Kimball: dimensiones compartidas entre data marts que garantizan consistencia inter-marts.

*Ver: Capítulo 7, sección "La arquitectura subyacente — Kimball Barnizada".*

### Continuidad de negocio operacional

Protocolos manuales documentados para cuando el Botlet senior cae por causas exógenas (corte de energía, hardware, red catastrófica) y la cognición tampoco está disponible. **Propiedad operacional**, equivalente a la que cualquier negocio tradicional tiene cuando se le cae el sistema. Distinta y complementaria de la **garantía de fallback agéntico** (que cubre cambios de ambiente con cognición disponible). Reduce ansiedad sobre offline al separar lo que resuelve la arquitectura de lo que resuelve el protocolo del cliente.

*Ver: Capítulo 5 §4, sección "Continuidad de negocio operacional vs garantía de fallback agéntico".*

### Contrato declarativo de calidad

Atributos de calidad de un Botlet declarados como propiedades estructuradas (no como código embebido): **frescura** (antigüedad máxima de los datos) · **SLA** (latencia p50/p99) · **política de degradación** (`refuse` · `warn_and_show` · `show_last_valid` · `agentic_fallback`) · **audiencia** (política RLS/CRUDLEX) · **política de refresh** (`on-demand` · `scheduled` · `push`). Permite que Trust Infrastructure los audite uniformemente, los curse por políticas globales y los reporte como métricas estándar, sin acoplarse a la implementación de cada Botlet.

*Ver: Capítulo 8; entrada **Trust Infrastructure**.*

### coordinación intra-AgencyDomain

Comunicación entre Botlers del **mismo** AgencyDomain — runtimes del mismo agente, no agentes distintos. Cuando usa este transporte se dice **vía el protocolo `A2A`**. No debe llamarse "A2A interna": `A2A` (la relación) se reserva para AgencyDomain ↔ AgencyDomain. La interfaz Cognición → Botler (Capa 2 → Capa 3) va por `MCP`.

*Ver: Capítulo 5 §1; entradas **A2A**, **MCP**, **Capa 3 distribuida**.*

### CRUDLEX

Modelo canónico de permisos granulares para sistemas agentivos: **C**reate, **R**ead, **U**pdate, **D**elete, **L**ist, **E**xecute. Aplicable por usuario, agente y contexto.

Niveles preconfigurados: FULL, READ-WRITE, READONLY, SAFE, NO-SEND, NO-DELETE.

*Ver: Capítulo 8, sección "Modelo CRUDLEX completo".*

### Cuenta

Concepto comercial superpuesto al modelo técnico de AgencyDomains. Una Cuenta puede poseer múltiples AgencyDomains. La especificación trata la Cuenta como entidad opaca; cada implementación define su semántica.

## D

### DLP — Data Loss Prevention

Detección automatizada de datos personales (PII) en lugares donde no deberían aparecer. Control ejercido en la Capa 4 — Acceso de la arquitectura; en la lente de mercado, es capacidad típica del eslabón Firewall de IA. Componente del pilar Validación de Trust Infrastructure.

*Ver: Capítulo 5 §4.*

### Domain

Término del ámbito computacional donde un agente ejerce agencia. Sinónimo comercial del término técnico **AgencyDomain**. La forma corta `Domain` es la que aparece en lore comercial, marketing, ventas y comunicación cliente; la forma larga `AgencyDomain` se reserva para documentación técnica formal y especificaciones.

Patrón análogo al que usan productos serios: Apple iCloud (marca) / CloudKit (técnico); Stripe Connect (marca) / Account (técnico). La existencia de dos formas no es ambigüedad — es separación de registros.

*Ver: Capítulo 5 §1; entrada **AgencyDomain**.*

### Dominion

Concepto institucional emergente: Domain conseguido por un agente en un AgencyDomain público que adopta el modelo de AgentNation. La distinción frente a un Domain asignado es ontológica — Domain asignado = residencia (la organización lo puso ahí); Domain conseguido = ciudadanía (el agente cumplió requisitos para ser admitido). Vocabulario de la frontera institucional, no obligatorio para implementaciones que no adoptan el modelo de ciudadanía.

*Ver: Epílogo, sección "Frontera 4 — el horizonte institucional".*

## E

### Edge computing

Distribución de la Capa 3 (Autonomía) a dispositivos cerca del proceso físico, para evitar latencia de cognición remota e independizarse de conectividad intermitente. Patrón canónico para mundo de carbono.

*Ver: Capítulo 6 §3.*

### Empresa en línea

Organización con sus datos actualizados en tiempo real, dashboards al día, información accesible — pero que **depende de humanos** para mirar, interpretar y decidir. Ciclo clásico, optimizado.

*Ver: Capítulo 2, sección "Del ciclo clásico al ciclo de inteligencia continua".*

### Empresa en tiempo real

Organización que **detecta, interpreta, decide y actúa** de forma continua y autónoma, dentro de marcos gobernados. Ciclo agentivo. Producto del cruce de la Línea Nadella.

*Ver: Capítulo 2, sección "Del ciclo clásico al ciclo de inteligencia continua".*

### Eslabón

Capa funcional secuencial de la cadena de valor de IA. La especificación canónica define **once eslabones**:

1. Datos · 2. Modelo · 3. Acceso · 4. Agentes · 5. Especializaciones · 6. Runtime · 7. Firewall · 8. Observabilidad · 9. Herramientas · 10. Integraciones · 11. Entorno

*Ver: Capítulo 6 §1.*

## F

### Faceta

**Sexta primitiva canónica** del libro. Componente atómico reusable de la **Capa 1 (Interacción)**: pizarra de dibujo a mano alzada, catálogo-selector, matriz de colores, calendario, mapa clickeable, slider, ordenamiento drag-and-drop. Una de las muchas caras que la interacción con el usuario puede tomar en un momento dado. Es **instrumento**, no proceso.

**No es un Botlet.** La Faceta vive en Capa 1; el Botlet vive en Capa 3. La Faceta es invocada por la cognición durante conversación activa, no tiene garantía de fallback, no tiene ciclo de regeneración, es efímera por defecto. El Botlet automatiza; la Faceta interactúa.

Dos usos canónicos: (1) la cognición la invoca directamente durante conversación para componer una superficie efímera (realiza el régimen *GUI on-the-fly*); (2) los Botlets de presentación (shells y vistas) la ensamblan como pieza de su composición.

*Ver: Capítulo 4 §1 · Capítulo 5 §6 (la primitiva completa).*

### feature

Operación interna que una Capability expone — sub-unidad funcional (equivalente práctico de *feature/operation/skill/method*). **Test Capability vs feature** (los tres deben ser sí para tratarla como Capability propia): (1) independencia operativa — ¿puede instalarse y operar sin la otra?; (2) identidad cognitiva — ¿tiene modelo de datos y SME distintos?; (3) reusabilidad — ¿tiene valor para más de un consumidor/contexto? Si uno o más es **no** → es feature de la Capability contenedora.

*Ver: Capítulo 5 §3; entrada **Capability**.*

### Federación

Comunicación entre AgencyDomains distintos. Trabajo abierto en evolución. Distinta de Cluster (que es entre instancias del mismo AgencyDomain).

*Ver: Capítulo 5 §1.*

### Firewall

Eslabón 7 de la cadena de valor: seguridad, control, governance. Protección contra prompt injection, alucinaciones, filtrado de contenido, auditoría de uso. Productos representativos: Lakera, Lasso, Guardrails.

*Ver: Capítulo 6 §1.*

## G

### Garantía de fallback

Propiedad innegociable de las unidades de Capa 3 conformes a esta especificación: si un Botlet falla catastróficamente, **la cognición ejecuta la tarea manualmente**; si un Agentlet no resuelve dentro de su charter, **escala a la Cognición plena**. El proceso nunca se detiene.

*Ver: Capítulo 5 §2 y §7.*

### Gateway empresarial de IA

Categoría arquitectónica que combina Core en Runtime + Firewall + Observabilidad + Herramientas + Integraciones, con extensión Plataforma en Acceso. Función única: **conectar y controlar simultáneamente** la operación de agentes empresariales. Materialización de la Capa 4 (Acceso) sobre los eslabones de mercado.

*Ver: Capítulo 6 §1.*

### Generaciones del Botlet — G1/G2/G3

Modelo evolutivo de cómo nace el código del Botlet conforme avanza el estado del arte de la cognición. **G1** — el agente configura proto-Botlets pre-forjados (no escribe el cuerpo). **G2** — el agente co-escribe el proto-Botlet. **G3** — el agente genera el código completo (escenario asintótico). La arquitectura es la misma en las tres; lo que cambia es el **alcance de la Ingeniería**.

*Ver: Capítulo 5 §2 (definición); Epílogo (ensayo de fondo); entrada **proto-Botlet**.*

### Gobernanza

Pilar 1 de Trust Infrastructure. Mecanismos mediante los cuales la organización define **qué** puede hacer el agente, **bajo qué condiciones** y **con qué nivel de supervisión**.

*Ver: Capítulo 5 §4.*

### GUI on-the-fly

Régimen 2 de generación de Capa 1 (Cap 4 §1). Superficie gráfica que el agente compone adaptada a la tarea inmediata — una vista, un formulario, un panel, un dashboard. Vive lo que dura la tarea; puede regenerarse distinta la próxima vez según contexto. Distinta de GUI persistente (régimen 3) y de conversacional puro (régimen 1).

*Ver: Capítulo 4 §1, sección "Tres regímenes de GUI en la Capa 1 agentiva".*

### GUI persistente como Botlet de fachada

Régimen 3 de generación de Capa 1 (Cap 4 §1). Superficie estable que el agente genera y consolida como **Botlet de fachada** — un Botlet de Capa 3 que la expone en Capa 1 — porque el rol operativo es estable y la velocidad crítica (cajero en hora punta, panel de cocina, dashboard de caja, panel industrial). Sigue siendo agentiva: el agente puede regenerarla cuando el ambiente cambia. **Ningún equipo humano de UI/UX la diseñó** — la cognición la generó. Típicamente Botlet seed.

*Ver: Capítulo 4 §1, sección "Tres regímenes de GUI en la Capa 1 agentiva".*

## H

### Hallucination (alucinación)

Afirmación factualmente incorrecta producida por un modelo de cognición con apariencia de confianza. Detección de alucinaciones es parte del pilar Validación de Trust Infrastructure.

*Ver: Capítulo 8, sección "Reglas de detección de alucinaciones".*

### Híbrido (régimen)

Régimen de AgencyDomain que combina core privado con exposición pública parcial vía proxy, o datos privados con interfaz pública mediada por una capa de trust. Análogo a Hybrid Cloud.

*Ver: Capítulo 5 §1.*

## I

### Ingeniería

Uno de los **tres tiempos del agente** (Cap 4). Tiempo en que el agente convierte capacidad latente en capacidad ejecutable para un caso concreto: identifica qué Capabilities aplican, configura un Botlet seed para el contexto específico, valida su ejecución sobre datos reales, lo deploya. Puente entre Preparación y Atención. Régimen de mediano plazo (minutos a horas); métricas: cobertura, tasa de éxito al primer deploy, iteraciones promedio.

*Ver: Capítulo 4, sección "Los tres tiempos del agente".*

### Instrumento de información

El **tipo** canónico de la familia de información (la clase: reporte / dashboard). Distinto del **Producto de Información (PI)**, que es su **instancia** manifestada/entregada. Lectura preferida; no son sinónimos.

*Ver: entradas **Producto de Información (PI)**, **manifestación**.*

### Interacción declarada acotada

Interacción que opera sobre el **snapshot ya materializado** de una pieza, en un espacio **declarado** (dimensiones y valores acotados), que **mantiene reproducibilidad** y es **G1** (configuración, no código). Vive **en la pieza misma vía Faceta embebida**: los elementos *data-bound* (KPIs como agregaciones declaradas, distribuciones, semáforos) se recomputan client-side sobre el subconjunto filtrado, sin nuevas invocaciones a Capabilities. Distinta de la **exploración libre** (query nueva arbitraria al origen, espacio abierto, pierde reproducibilidad, excede G1).

*Ver: Capítulo 4 §1, Capítulo 5 §6; entrada **Faceta**.*

## J

### JSR — Java Specification Request

Formato canónico de especificaciones de Java publicado por Sun Microsystems / Oracle. JavaSpaces (JSR-000148) es el análogo conceptual de la especificación AgencyDomains.

*Ver: Capítulo 5 §1.*

## K

### Kimball / Kimball Barnizada

**Kimball** — metodología canónica de modelado dimensional para data warehousing, formulada por Ralph Kimball en *The Data Warehouse Toolkit* (1996).

**Kimball Barnizada** — evolución contemporánea que preserva la estructura conceptual de Kimball y agrega la capa agentiva: capa semántica explícita, Trust Score por dato, AI Certification, observabilidad de queries agentivos.

*Ver: Capítulo 7, sección "La arquitectura subyacente — Kimball Barnizada".*

## L

### LLM — Large Language Model

Modelo de lenguaje grande (Claude, GPT, Gemini, Llama, etc.). La cognición contemporánea (Capa 2) es predominantemente LLM-céntrica, pero la arquitectura admite cognición no-LLM (frontera de evolución).

### Línea Nadella

Umbral conceptual que separa el Mundo Agéntico del Mundo Agentivo. Pregunta divisoria: *¿el humano abre aplicaciones para hacer su trabajo?*

Origen del nombre: Satya Nadella en BG2 podcast (diciembre 2024) — *"La noción de que las aplicaciones de negocio existen, probablemente es donde todo colapsará, en la era de los agentes."*

La formulación canónica es la de este libro; cada volumen de la trilogía la conjuga a su audiencia: en segunda persona en *La Empresa en Tiempo Real* («¿todavía abres aplicaciones para hacer tu trabajo?») y en la voz del directivo en *AURA* («¿sus empleados todavía abren aplicaciones para hacer su trabajo?»). Las tres son equivalentes oficiales.

*Ver: Capítulo 1.*

## M

### manifestación

Actualización de la disposición latente del Botlet en el mundo, perceptible o no. Un Botlet es memoria muscular (disposición latente); al ejecutarse, ese latente se actualiza — se manifiesta (potencia → acto). **No es "aparición"**: un Botlet que dispara una ingestión periódica se manifiesta aunque no deje artefacto visible. Es el género abstracto; cada familia lo especializa — **información** → deja un **Producto de Información (PI)**; **actuación** → un efecto sobre el mundo; **decisión** → según su práctica.

*Ver: entradas **temporalidad**, **Producto de Información (PI)**.*

### MCP — Model Context Protocol

Protocolo abierto introducido por Anthropic en noviembre de 2024 para conectar modelos de IA con herramientas externas. Estándar canónico contemporáneo para tools de Capa 4 y para la interfaz interna Capa 2 → Capa 3 (la Cognición es el cliente; el Botler expone el servidor `MCP`).

*Ver: Capítulo 4, sección "Capa 4 — Acceso". Sitio: [modelcontextprotocol.io](https://modelcontextprotocol.io).*

### Memoria muscular

Metáfora canónica del Botlet. Análoga al aprendizaje motor humano: la primera vez se piensa cada paso (cognición); con práctica suficiente, los movimientos se ejecutan sin pensamiento consciente (Botlet); cuando el ambiente cambia, la cognición vuelve.

*Ver: Capítulo 5 §2.*

### MEO — Model Engine Optimization

Conjunto de prácticas que aseguran que los modelos frontera (Claude, GPT, Gemini, Llama) tengan al actor en su conocimiento entrenado y operativo, para que lo referencien al ser preguntados. Equivalente conceptual del SEO en la capa de descubrimiento agentiva. Se construye con presencia pública estructurada — repositorios open source, documentación citable, integración nativa con MCP, papers, mentions de alta autoridad. Dinámica persistente y asimétrica con tendencia a ganador-toma-todo.

*Ver: Capítulo 6 §1 (discoverability agentiva).*

### Meta-Cognitive Platform

Categoría de plataforma que administra la **economía de la cognición**: G1 músculo pre-forjado vs fallback de cognición fresca, ciclo 95/4/1, maduración junior→senior, cristalización. **Vergis** es la implementación de referencia de esta categoría. No se abrevia a "MCP" — esa sigla está tomada por Model Context Protocol.

*Ver: entradas **Vergis**, **Botlet**.*

### Mira

**Nombre propio** de un proto-Botlet **platafórmico** de operación informativa, parte del catálogo de la implementación de referencia. Especializa N Productos de Información sobre un motor compartido.

*Ver: entradas **proto-Botlet**, **Vergis**.*

### Modos de degradación del AgencyDomain

Cuatro modos canónicos de operación según el escenario de falla, formalizados en Cap 8: **Normal** (todos los componentes activos · topología paralela completa) · **Cognición caída** (vía Autonomía sostiene; Botlets senior ejecutan) · **Edge offline** (Botlets senior contra BD local + Conectores edge-resident) · **Continuidad operacional total** (protocolo manual del sitio; registro físico como fuente de verdad temporal). Las primeras tres transiciones son automáticas y responsabilidad de la arquitectura; la cuarta es gobernada por el protocolo del cliente y activada explícitamente por un humano.

*Ver: Capítulo 8, sección "Continuidad operacional".*

### Mundo de carbono

El mundo físico (IoT, procesos industriales, máquinas, sistemas biológicos) en oposición al mundo digital (sistemas, APIs). Eslabón 11 (Entorno) de la cadena de valor extendido al mundo físico. Frontera de evolución de la Arquitectura Agentiva.

*Ver: Capítulo 6 §3.*

## O

### Observabilidad

Eslabón 8 de la cadena de valor de IA: la capa que **observa, mide y retroalimenta** sobre el comportamiento de un sistema de IA en producción. Provee el **ciclo de feedback operacional** que permite mantener confiabilidad, costo y calidad bajo control. Su pregunta: *¿cómo funciona?* — distinta de la del Firewall (*¿es seguro?*) y de la de Herramientas (*¿qué puede hacer?*). Sin Observabilidad, los agentes son cajas negras; con ella, sistemas operables. Seis capacidades canónicas: tracing, monitoreo de costos, evaluación de calidad, métricas de rendimiento, debugging y reproducibilidad, alertas y anomalías.

*Ver: Capítulo 6 §2 (deep-dive del eslabón).*

## P

### Patrón tripartito — Cloud + Cliente + Local

Patrón canónico de despliegue de Trust Infrastructure en sistemas agentivos enterprise. Tres componentes coordinados que viven en lugares físicamente distintos: **Cloud** (control plane operado por el proveedor de la plataforma); **Cliente** (governance plane desplegado en la red interna de la organización cliente); **Local** (execution plane en el dispositivo de cada usuario). Cada plano resuelve un problema que los otros dos no pueden resolver bien.

*Ver: Capítulo 8, sección "El patrón tripartito de despliegue".*

### Pattern Recognition

Detección de patrones repetitivos en la actividad del agente. Inspirada en arquitectura neurobiológica: corteza perirrinal → hipocampo → corteza prefrontal. Activador de la generación de Botlets.

*Ver: Capítulo 4, sección "Capa 2 — Cognición", Capítulo 5 §2.*

### Plantilla

Confección específica del cliente sobre un instrumento canónico (reporte / dashboard) en un formato o regla propios del cliente (por ejemplo, una plantilla regulatoria de un instrumento normado). **Capa 1 · Interacción**, junto a Faceta / Botlet de superficie / Botlet de vista. Esquema de confección: relevar expectativa · confeccionar sobre instrumento canónico · validar. No es Capability (saber cognitivo) ni Conector (acceso).

*Ver: Capítulo 5 §3, sección "Capability, Conector y Plantilla"; entradas **Capability**, **Faceta**.*

### Portabilidad de la Capability

Propiedad por la cual una Capability conforme puede instalarse y ejecutarse en cualquier AgencyDomain conforme, lo que la vuelve **propiedad real del cliente** — no del AgencyDomain ni del hosting. Relación: un AgencyDomain **aloja y ejecuta** Capabilities; una Capability **corre en** un AgencyDomain anfitrión. Distinta de la **portabilidad del AgencyDomain** (entre plataformas hosting conformes).

*Ver: Capítulo 5 §3; entradas **Capability**, **Portabilidad del AgencyDomain**.*

### Portabilidad del AgencyDomain

Propiedad estructural de la spec: un AgencyDomain conforme puede migrarse a otra **plataforma hosting conforme** sin reescribir su lógica, su estado ni sus políticas. Distinta de la migración natural entre regímenes (privado → público), que cambia el régimen pero no la plataforma. Tres condiciones técnicas: (1) **Botlets contra primitivas canónicas** del SDK conforme, no APIs propietarias del hosting; (2) **BD operativa exportable** en formato neutro reproducible; (3) **Trust Layer portable** — políticas, log y configuración en formato legible por cualquier implementación conforme. Garantiza que el AgencyDomain es **propiedad real del cliente**, no del hosting.

*Ver: Capítulo 5 §1, sección "Portabilidad del AgencyDomain entre plataformas conformes".*

### Preparación

Uno de los **tres tiempos del agente** (Cap 4). Tiempo en que el agente crea y mejora sus capacidades fuera de la ventana de servicio: refina su catálogo, mejora capacidades cognitivas, estudia el ambiente, regenera Botlets que detectaron drift, incorpora variantes nuevas. *Mise en place* del agente — el trabajo que sostiene la calidad del servicio sin ser visible para el usuario. Régimen batch / off-peak; métricas: calidad del catálogo, precisión de Botlets, cobertura de Capabilities.

*Ver: Capítulo 4, sección "Los tres tiempos del agente".*

### Privado (régimen)

Régimen de AgencyDomain donde el espacio y todos sus componentes viven dentro de un perímetro controlado. No hay acceso público. Análogo a Private Cloud.

*Ver: Capítulo 5 §1.*

### Producto de Información (PI)

Instancia manifestada/entregada de la familia de información de Botlets — la manifestación concreta de un **Instrumento de información** (su tipo). Cada PI es su propio Botlet/servicio (con `identity`, temporalidad, madurez y fallback propios), especializado de un motor compartido (proto-Botlet platafórmico). **No es primitiva del canon**: vive en la práctica de información, un nivel más concreto.

*Ver: entradas **Instrumento de información**, **manifestación**, **proto-Botlet**.*

### Profundidad

Dimensión vertical del modelo de cadena de valor de IA. Cuatro niveles canónicos: **Wrapper** (consume), **Plataforma** (opera), **Core** (construye), **Infraestructura** (sustenta).

*Ver: Capítulo 6 §1.*

### Prompt injection

Manipulación de un sistema de IA mediante inputs maliciosos disfrazados como datos legítimos. Detección y prevención son parte del pilar Validación de Trust Infrastructure.

### proto-Agentlet

Pieza pre-forjada de capacidad interpretativa que el agente, en su tiempo de **Ingeniería**, **configura** para instanciar un Agentlet específico al caso. El proto-Agentlet contiene el cuerpo — el andamiaje de la tarea interpretativa: estructura del charter, esqueleto del prompt operativo, contratos de entrada/salida, umbrales de escalamiento —; el Agentlet es la instancia configurada. Las dos clases del proto-Botlet aplican sin cambio (templado · platafórmico), igual que la cadena de derivación y los catálogos comunes con sus efectos de red.

*Ver: Capítulo 5 §7; entradas **Agentlet**, **proto-Botlet**, **Cadena de derivación**.*

### proto-Botlet

**Séptima primitiva canónica** del libro. Pieza pre-forjada de capacidad operativa que el agente, en su tiempo de **Ingeniería**, **configura** para instanciar un Botlet específico al caso. El proto-Botlet contiene el código; el Botlet es la instancia configurada. En **G1**, la totalidad del código de un Botlet vive en su proto-Botlet (el agente solo configura); en **G3** el agente puede generar el código sin proto-Botlet de por medio. Distintas implementaciones mantienen catálogos de proto-Botlets (públicos en AgencyDomains.org, privados en códices propietarios). Dos clases:

- **proto-Botlet templado** — código específico de su función (ej. `cobro-cuenta`, `comanda-impresora-esc-pos`); su configuración es parametrización acotada.
- **proto-Botlet platafórmico** — código genérico cuya especialización vive en una configuración composicional (ej. `mira`); cubre N funciones de su dominio. Para él, G1 es terminal por diseño.

*Ver: Capítulo 5; entradas **Botlet**, **Generaciones del Botlet — G1/G2/G3**, **Cadena de derivación**.*

### Público (régimen)

Régimen de AgencyDomain donde el espacio es accesible públicamente. Agentes, Botlets y tools son invocables desde fuera del perímetro. Análogo a Public Cloud.

*Ver: Capítulo 5 §1.*

## R

### RAG — Retrieval-Augmented Generation

Técnica donde un modelo de cognición consulta una base de documentos antes de responder, para citar fuentes y reducir alucinaciones.

### Régimen

Modo de despliegue de un AgencyDomain según la frontera de acceso. La spec reconoce tres regímenes técnicamente equivalentes en estructura interna: **privado** (perímetro controlado por una organización, sin acceso público); **público** (accesible desde fuera, agentes registrados en directorio); **híbrido** (combinación con datos privados y exposición pública vía proxy). La estructura técnica del AgencyDomain es la misma en los tres; lo que cambia es el régimen, no la capacidad. Habilita migración natural entre regímenes sin reescritura.

*Ver: Capítulo 5 §1.*

### Resiliencia

Pilar 4 de Trust Infrastructure. Garantía de que el sistema sigue operando — y la organización conserva control — cuando algo sale mal.

Mecanismos canónicos: garantía de fallback, manejo de errores, sandboxing, circuit breakers, rate limiting.

*Ver: Capítulo 5 §4.*

### RLS — Row-Level Security

Seguridad a nivel de fila: la política que decide qué filas de una fuente puede ver cada identidad. En el drill-through de un Producto de Información, la vista destino aplica su propia `RLS` sobre la fuente y el contexto de navegación entra como filtro adicional — nunca como override (propiedad data-anchored / no-bypass).

*Ver: Capítulo 5 §2, descripción del Producto de Información.*

### Runtime

Eslabón 6 de la cadena de valor: ambiente operativo donde los agentes viven y operan de manera autónoma. Ciclo de vida, persistencia de estado, identidad, scheduling. Corresponde a la Capa 3 (Autonomía) de la Arquitectura Agentiva.

*Ver: Capítulo 6 §1.*

## S

### Salto Cuántico

Umbral habilitado por el colapso del costo de la pregunta analítica: cuando preguntarle a los datos deja de ser caro, lento o mediado por un humano, la organización cruza de **empresa en línea** (datos al día pero dependiente de humanos para mirar, interpretar y decidir) a **empresa en tiempo real** (detecta, interpreta, decide y actúa de forma continua y autónoma). No es una mejora incremental de BI sino un cambio de régimen operativo — la frontera empresa-en-línea → empresa-en-tiempo-real.

*Ver: Capítulo 2, sección "Del ciclo clásico al ciclo de inteligencia continua"; entradas **Empresa en línea**, **Empresa en tiempo real**.*

### Sandbox

Aislamiento de ejecución de las unidades de Capa 3 (Botlets y Agentlets) y código generado dinámicamente. Cuatro estrategias canónicas con sus trade-offs: procesos+seccomp, contenedores, WASM, MicroVMs.

*Ver: Capítulo 5 §2.*

### Semantic layer / Capa semántica

Capa que codifica el significado de las dimensiones, hechos, jerarquías y reglas de negocio sobre un data warehouse. Sin ella, los agentes que consultan datos alucinan o producen consultas incorrectas. Componente esencial de la Kimball Barnizada.

*Ver: Capítulo 7, sección "La arquitectura subyacente — Kimball Barnizada".*

### Señalética

Dashboards pasivos que comunican información continuamente sin requerir interacción del humano (como paneles en aeropuertos). Modalidad de Capa 1 (Interacción).

*Ver: Capítulo 4, sección "Capa 1 — Interacción".*

### SME — subject-matter expert

Experto humano cuyo saber se transfiere al agente en el esquema de construcción de Capabilities. El Wingtraining abre con un workshop con el SME y valida con él la fase ALFA; tener un **SME identificable** es criterio del test de clasificación de la Capability, y compartir SME y modelo de datos con la capacidad contenedora es señal de que una operación es feature, no Capability propia.

*Ver: Capítulo 5 §3; entradas **Capability**, **Wingtraining**, **feature**.*

### Space

Habitat humano físico. La palabra carga corporeidad: oficina, escritorio, hogar, ciudad. En esta especificación, **Space se reserva para humanos**. El ámbito computacional del agente nunca se nombra como Space — se nombra como Domain (AgencyDomain).

*Ver: Capítulo 5 §1, entrada AgencyDomain.*

## T

### temporalidad

Régimen de la manifestación del Botlet. Atributo declarado, dos valores: **discreta** (el Botlet se manifiesta en pulsos: despierta por schedule/trigger/evento, actúa, descansa) y **continua** (se manifiesta sostenido: vive persistente). `temporalidad: continua` ⟺ vida persistente de Capa 3 (el Botler sostiene la ejecución mientras viva). El "tiempo real" no se elige en un canal de entrega (`push`) sino dando al Botlet temporalidad continua, lo que obliga al runtime persistente. Un reporte (snapshot) y un dashboard vivo son la misma manifestación bajo distinta temporalidad → un único runtime.

*Ver: entradas **manifestación**, **Empresa en tiempo real**.*

### Tokenización

Reemplazo de datos sensibles por tokens antes de que lleguen al modelo de cognición. Permite que el agente razone sobre los datos sin exponerlos al proveedor de cognición externo. Componente del pilar Validación de Trust Infrastructure.

*Ver: Capítulo 8, sección "Política de tokenización".*

### Tool

Herramienta que un agente puede invocar para tocar sistemas externos. Eslabón 9 de la cadena de valor. El protocolo canónico contemporáneo es MCP.

NO es Capability. La Capability es saber; el tool es acción. La Capability **decide** qué tool invocar.

*Ver: Capítulo 6 §1, Capítulo 5 §3.*

### Topología paralela

Modelo canónico de relación entre las cuatro capas de la Arquitectura Agentiva (Cap 4). Las **Capas 2 (Cognición) y 3 (Autonomía) son vías paralelas** entre Capa 1 (Interacción) y Capa 4 (Acceso), no etapas en serie. Una operación que entra por Capa 1 puede llegar a Capa 4 atravesando la **vía Cognición** (lenta, costosa, decisiva) o la **vía Autonomía** (rápida, barata, repetitiva). Las dos vías interactúan (`2 ↔ 3`: cognición delega a Botlet, Botlet escala fallback a cognición, cognición observa el log) pero ninguna domina sobre la otra. Modelo refundacional respecto a la lectura lineal `1 → 2 → 3 → 4`.

*Ver: Capítulo 4, sección "La topología paralela".*

### Trace

Trazabilidad end-to-end de una operación del agente. Contiene identidad, capability invocada, tool ejecutado, parámetros, resultado, timestamp, contexto. Componente del pilar Auditoría de Trust Infrastructure.

*Ver: Capítulo 5 §4 (pilar Auditoría); el tracing como capacidad de producto, en el Capítulo 6 §2.*

### Transparencia

Pilar 5 de Trust Infrastructure. Capacidad del humano de entender, en tiempo real, **qué está haciendo el agente y por qué** — con detalle suficiente para intervenir si es necesario. Es el pilar que conecta los otros cuatro: la Gobernanza define qué puede hacer, la Auditoría registra qué hizo, la Validación verifica qué está por hacer, la Resiliencia asegura que sigue operando; la Transparencia asegura que un humano puede entender todo lo anterior.

Mecanismos canónicos: observabilidad completa, métricas operativas, traces consultables por humanos, alertas proactivas, dashboards de gobernanza.

*Ver: Capítulo 5 §4.*

### Tres tiempos del agente

Marco temporal canónico del agente: **Preparación** (mise en place — refina catálogo, mejora capacidades, fuera de ventana de servicio), **Atención** (interactúa con usuarios en tiempo real, camino crítico), **Ingeniería** (puente: convierte capacidad latente en capacidad ejecutable para un caso concreto). Los tres son simultáneos pero diferenciados en régimen, urgencia y economía cognitiva. La topología paralela describe DÓNDE vive cada operación; los tres tiempos describen CUÁNDO opera el agente.

*Ver: Capítulo 4, sección "Los tres tiempos del agente".*

### Trust Infrastructure

Conjunto de propiedades transversales que permiten a una organización confiar en que sus agentes operen con autonomía sin perder control. Cinco pilares: Gobernanza, Auditoría, Validación, Resiliencia, Transparencia.

*Ver: Capítulo 5 §4.*

### Twin digital (Digital twin)

Gemelo digital que refleja en tiempo real el estado de un sistema físico. Patrón canónico para que agentes operen sobre el mundo de carbono — el agente actúa sobre el twin; el twin propaga al mundo físico cuando es seguro.

*Ver: Capítulo 6 §3.*

## U

### ucodex

**Nombre propio** del códice propietario del Grupo Ultra: su catálogo privado de proto-Botlets, Capabilities y patrones, curado por casos reales sobre la implementación de referencia pública (Vergis). Es la instancia que ejemplifica el modo *códice propietario*; vive en el mismo cajón de nombres propios de instancia que Soveria, Agentia o ultraPRO, no es un tipo del canon.

*Ver: Capítulo 9; entradas **códice propietario**, **Catálogo común / efectos de red**.*

### unidad (de Capa 3)

Género de las piezas empaquetadas que el Botler hospeda y ejecuta. Dos especies: el **Botlet** (código no-LLM, memoria muscular) y el **Agentlet** (inferencia acotada, juicio de rutina empaquetado). El aparato compartido — patrón proto-/instancia, catálogos, spec, manifestación, temporalidad, contrato declarativo de calidad, cadena de derivación, append-only log, verbos de operación — se predica del género; las garantías diferenciales (costo, determinismo, offline, fallback), de cada especie. Relación canónica del runtime: **1 Proceso = 1 Botler + N unidades**.

*Ver: Capítulo 5 §2 y §7; entradas **Botlet**, **Agentlet**, **Botler**.*

## V

### Validación

Pilar 3 de Trust Infrastructure. Capacidad de verificar que la respuesta o acción del agente sea correcta antes de que afecte al mundo.

Mecanismos canónicos: detección de alucinaciones, validación de respuestas estructuradas, prompt injection prevention, DLP, tokenización.

*Ver: Capítulo 5 §4.*

### Vergis

**Nombre propio** de la implementación de referencia pública de AgencyDomains (la plataforma; el AgencyDomain hecho operativo). Categoría: **Meta-Cognitive Platform**. Distribuida bajo **AGPL**, repositorio público, **AgencyDomains.org**. Es nombre propio de una instancia (mismo cajón que Soveria, Agentia, ultraPRO), no un tipo como Botler o Botlet.

*Ver: Capítulo 9; entradas **Meta-Cognitive Platform**, **Mira**, **Botler**.*

### Vía Autonomía

Una de las dos vías de la **topología paralela** (Cap 4). Camino que una operación atraviesa entre Capa 1 y Capa 4 pasando por Capa 3 (Autonomía) sin invocar Capa 2 (Cognición). Régimen propio: rápido, barato, repetitivo. Para ejecución de unidades — Botlets sobre patrones estables y Agentlets sobre juicio de rutina —. Es la vía que sostiene la operación cotidiana de un AgencyDomain en producción y la base estructural del modo offline cuando los Botlets son senior.

*Ver: Capítulo 4, sección "La topología paralela".*

### Vía Cognición

Una de las dos vías de la **topología paralela** (Cap 4). Camino que una operación atraviesa entre Capa 1 y Capa 4 pasando por Capa 2 (Cognición) sin pasar obligatoriamente por Capa 3. Régimen propio: lento, costoso, decisivo. Para conversación, decisiones nuevas, casos no anticipados, casos donde el humano necesita interlocución razonada. Económicamente cara — la organización la usa con mesura y reserva su capacidad para casos donde el valor lo justifica.

*Ver: Capítulo 4, sección "La topología paralela".*

## W

### Wingtraining

Esquema canónico de desarrollo de una Capability en cinco pasos: **workshop con el SME** · **creación** · **personalización** · **ALFA** (validación con el SME) · **BETA** (validación en operación real). Su desarrollo pertenece a la práctica de entrega, no al canon; el test de clasificación de la Capability lo usa como criterio porque es la prueba operativa de que un alcance es transferencia de saber — no integración ni formato.

*Ver: Capítulo 5 §3; entradas **Capability**, **SME**.*

### Wingworking

Práctica colaborativa entre humano e IA, generalización de *wingcoding* (programar con copiloto IA) a cualquier disciplina del trabajo profesional. Es el marco metodológico bajo el cual este libro fue producido — autor humano y agente IA trabajando en paralelo, con división explícita de roles y contrato común de calidad. La metodología vive fuera del alcance arquitectónico del libro; aparece declarada en el Colofón como atribución del proceso de producción.

### WorkSpace

Espacio de trabajo digital del humano. La industria del software empresarial extendió la palabra Space a WorkSpace (Google Workspace, Microsoft 365, Notion) para nombrar la colección de soluciones que digitalizan lo que la persona hace en su escritorio físico: leer email, agendar reuniones, escribir documentos, archivar. WorkSpace es la prótesis digital del Space humano; ambos cargan la misma corporeidad de origen y se reservan para humanos. El equivalente agentivo es **Domain (AgencyDomain)**.

*Ver: Capítulo 5 §1, entrada AgencyDomain.*

### Wrapper / Plataforma / Core / Infraestructura

Las cuatro profundidades canónicas del modelo de cadena de valor de IA. Definen, dentro de un eslabón dado, **cómo** participa un actor:

- **Wrapper** — consume el eslabón vía APIs/SDKs de terceros.
- **Plataforma** — opera capacidad propia sobre componentes Core de terceros.
- **Core** — construye la capacidad fundacional con tecnología propia.
- **Infraestructura** — provee el sustrato sobre el cual operan los niveles superiores.

*Ver: Capítulo 6 §1.*

