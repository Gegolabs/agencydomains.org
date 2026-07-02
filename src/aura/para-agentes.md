---
título: AURA — Manifiesto canónico para agentes
edición: Borrador de desarrollo · v0.3 · Julio 2026
fuente_canónica: libro-aura-v0.3 (libro humano)
licencia: GFDL v1.3 (propuesta)
audiencia: agentes que deben diagnosticar madurez organizacional y razonar dentro del marco AURA
estado: pre-1.0 — sin compromiso de estabilidad de referencias hasta v1.0
---

# AURA — Manifiesto canónico para agentes

> Extracto estructurado de la edición **v0.3 (borrador de desarrollo)** del libro *AURA: el Camino Agentivo*. Este documento condensa el vocabulario canónico, los dos modelos diagnósticos (IRIS y MOTOR), los dos instrumentos (Data Canon y Wingmap) y el marco de decisión (Casos de Uso). La versión humana del libro contiene además motivación, datos de industria, los argumentos completos de los capítulos-paper, ejemplos extendidos y el portafolio ilustrativo de cien casos — todo eso queda fuera de aquí.

> AURA es **diagnóstica, no prescriptiva**. Este manifiesto permite *ubicar* a una organización en sus trayectorias de madurez y razonar sobre su siguiente paso; no recomienda productos, inversiones ni plazos — eso pertenece a la consultoría que estos modelos informan.

## Cómo usar este documento

- **Es contexto canónico**, no resumen ejecutivo. Cada definición, etapa, nivel y pregunta diagnóstica importa para razonar dentro del marco.
- **Espejo de v0.3** — la versión vigente del libro en desarrollo. Si este documento contradice al libro humano, el libro humano gana.
- **Vocabulario obligatorio**: los términos en `código` y **negrita** son canónicos. No sustituir por sinónimos. En particular: **agentivo** ≠ **agéntico** (ver §2) — la distinción es de tesis, no de estilo.
- **Convenciones MUST/SHOULD** en sentido RFC 2119, usadas con moderación: AURA diagnostica; sus pocos imperativos son estructurales (secuencialidad de niveles, pre-condiciones bloqueantes, honestidad del ROI).
- **Estado pre-1.0**: el libro está en desarrollo activo, sin publicación pública aún. Términos, estructuras y numeración pueden cambiar entre v0.x. La estabilidad de referencias se compromete a partir de v1.0 (primera publicación).
- **Serie**: AURA es el Libro II de la trilogía del Mundo Agentivo — *AgencyDomains* (la arquitectura del destino; tiene su propio manifiesto canónico) · **AURA** (el camino) · *Postchat* (el destino habitado). Los términos compartidos con la trilogía (La Línea Nadella, agentivo, Trust Infrastructure, empresa en tiempo real) son consistentes entre libros.

---

## 1 · Vista panorámica

```
                          AURA
        Arquitectura Unificada de Referencia Agentiva
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   PARTE I · EL SABER  PARTE II · EL HACER  PARTE III · EL PORTAFOLIO
        │                   │                   │
   IRIS (modelo,       MOTOR (modelo,      Casos de Uso (marco:
   10 etapas)          7 niveles)          CU/SV · 3 dimensiones ·
        │                   │              Citizen/City/DUAL)
   Data Canon          Wingmap                  │
   (gobernanza         (levantamiento           │
   del dato)           de procesos)             │
        │                   │                   │
   ¿dónde estoy?      ¿sobre qué terreno?  ¿qué hago primero?
```

**La convergencia** — cuatro conceptos se unifican en AURA:

- **Inteligencia Organizacional** es la capacidad que se mide — el *qué*. (IRIS mide este eje: el SABER.)
- **Automatización Organizacional** es la capacidad de ejecutar — el *quién*. (MOTOR mide este eje: el HACER.)
- **Empresa en Tiempo Real** es el resultado organizacional de ambas capacidades maduras — el *para qué*.
- **IA Agentiva** es el mecanismo habilitador — el *cómo*.

**Declaración de visión:** las organizaciones transitan desde la **empresa en línea** — donde personas usan herramientas para acceder y entender datos — hacia la **empresa en tiempo real** — donde personas diseñan y gobiernan sistemas inteligentes que autónomamente detectan, analizan, deciden y actúan sobre la información del negocio. AURA organiza esta transformación en dos ejes diagnósticos; juntos diagnostican la transformación completa.

---

## 2 · El paradigma — conceptos fundantes

### Agéntico vs agentivo

- **Agéntico** (*agentic*): los agentes complementan las aplicaciones existentes. Los empleados siguen abriendo Excel, Salesforce, Power BI — con copilotos. Las interfaces persisten. **Evolución incremental.**
- **Agentivo**: los agentes reemplazan las interfaces tradicionales. Los empleados dejan de abrir aplicaciones e interactúan con agentes que ejecutan en su nombre. Las aplicaciones sobreviven como backend invisible; la interfaz colapsó. **Transformación fundamental.**

**La Línea Nadella** — la frontera entre ambos mundos, formulada como pregunta divisoria: *¿sus empleados todavía abren aplicaciones para hacer su trabajo?* Sí → mundo agéntico. No → mundo agentivo.

### La Pirámide del Valor de los Datos

Cuatro capas ascendentes: **DATOS** (registros crudos en sistemas) → **INFORMACIÓN** (datos con contexto y estructura) → **CONOCIMIENTO** (análisis, patrones, comprensión) → **ACCIÓN** (ejecución autónoma gobernada). La industria invirtió décadas en las dos capas inferiores; el salto información→conocimiento es dolorosamente lento y el salto conocimiento→acción prácticamente inexistente — no por la tecnología sino porque **hay humanos en el medio**.

### Empresa en línea vs empresa en tiempo real

- **Empresa en línea**: *accede* — datos actualizados, dashboards al día — pero depende de que un humano mire, interprete y decida.
- **Empresa en tiempo real**: *reacciona* — detecta, interpreta, decide y actúa de forma continua y autónoma.

### El Salto Cuántico

El colapso del costo de una pregunta analítica **de semanas a segundos**. Disuelve el racionamiento de preguntas: la capacidad analítica se vuelve elástica, la iteración reemplaza a la especificación, las preguntas que nunca se hacían se hacen. Es condición habilitante de todo lo demás y la frontera entre fundamentos y empresa en tiempo real (en IRIS: salto 4→5).

### El ciclo de inteligencia continua

El ciclo clásico (Descriptive → Diagnostic → Predictive → Prescriptive → humano decide) es lineal y humano-dependiente. El ciclo nuevo es continuo, agente-ejecutado y humano-gobernado:

```
Percibir → Interpretar → Decidir → Actuar → Aprender ─┐
   ▲                                                  │
   └──────────────────────────────────────────────────┘
```

El cambio crítico: el paso de recomendación a acción ya no espera a un humano — un agente ejecuta, monitorea el resultado y ajusta, dentro de límites gobernados.

### Tres ejes de cambio profundo

1. **De consumir información a gobernar agentes** — las personas pasan de consumir dashboards a diseñar reglas y supervisar sistemas autónomos.
2. **De arquitectura para humanos a arquitectura para agentes** — capas semánticas donde agentes razonan, knowledge graphs, flujos en tiempo real; calidad de dato = accionabilidad, no solo limpieza.
3. **De gobernanza de acceso a gobernanza de autonomía** — la pregunta deja de ser "quién puede ver qué datos" y pasa a ser "qué puede hacer un agente, bajo qué condiciones, con qué trazabilidad".

### Coexistencia evolutiva

Principio fundamental de AURA: **cada etapa/nivel no invalida al anterior — lo subsume.** El data warehouse no muere: se integra como fuente que los agentes consumen. La empresa en línea no desaparece: se convierte en el cimiento de la empresa en tiempo real. La transformación es un modelo híbrido donde cambia la proporción, no una demolición.

---

## 3 · IRIS — el eje SABER

**IRIS (Modelo de Madurez de Inteligencia Organizacional)** mide la trayectoria de una organización desde datos fragmentados hasta un ecosistema de inteligencia auto-gestionado, en **10 etapas** agrupadas en **5 niveles**. Es un modelo **diagnóstico**: evalúa en qué etapa está la organización y qué significa; no prescribe qué implementar.

### Las 10 etapas

| # | Etapa | Una frase | Pregunta diagnóstica |
|---|---|---|---|
| 1 | **Fragmentada** | Datos dispersos sin conexión | *¿Si le pido a dos personas de áreas diferentes el mismo indicador, obtendré el mismo número?* |
| 2 | **Sistematizada** | Captura ordenada en sistemas definidos | *¿Hay un sistema definido para capturar las transacciones clave del negocio, con reglas de registro consistentes?* |
| 3 | **Centralizada** | Repositorio central con BI clásico | *¿Existe un data warehouse centralizado con dashboards que los usuarios de negocio consultan regularmente?* |
| 4 | **Modelada** | Capa semántica y definiciones gobernadas | *¿Las métricas clave del negocio tienen una definición única y gobernada que toda la organización comparte?* |
| 5 | **Accesible** | Acceso libre bajo demanda · inicio de empresa en tiempo real | *¿Un gerente puede obtener una respuesta analítica que no estaba pre-construida en un dashboard, en minutos en lugar de semanas?* |
| 6 | **Contextual** | Información contextual y adaptativa | *¿El sistema es capaz de cruzar fuentes y enriquecer una respuesta con contexto relevante que el usuario no pidió explícitamente?* |
| 7 | **Proactiva** | La información busca al usuario | *¿Los responsables de negocio reciben información relevante antes de pedirla, con contexto suficiente para actuar?* |
| 8 | **Bidireccional** | Acción autónoma gobernada | *¿Existen agentes que ejecutan acciones operativas autónomamente con trazabilidad, dentro de reglas que los humanos definen y supervisan?* |
| 9 | **Coordinada** | Coordinación cross-domain | *¿Los agentes de diferentes áreas del negocio se comunican entre sí para coordinar acciones con información consistente?* |
| 10 | **Orquestada** | Ecosistema auto-gestionado · empresa en tiempo real plena | *¿El ecosistema de información evoluciona autónomamente — identificando gaps, mejorando modelos, y optimizando flujos — con supervisión humana solo a nivel estratégico?* |

### Los 5 niveles y el mapeo a la Pirámide

| Nivel | Etapas | Capa de la Pirámide | Trayectoria |
|---|---|---|---|
| **I · Fundacional** | 1–2 | DATOS | Fundamentos (empresa en línea) |
| **II · Estructurada** | 3–4 | INFORMACIÓN | Fundamentos (empresa en línea) |
| **III · Dinámica** | 5–6 | CONOCIMIENTO | Empresa en tiempo real |
| **IV · Activa** | 7–8 | ACCIÓN | Empresa en tiempo real |
| **V · Inteligente** | 9–10 | ACCIÓN | Empresa en tiempo real |

**El Salto Cuántico es el salto 4→5** — la frontera entre fundamentos y empresa en tiempo real. Las fronteras de nivel son los saltos 2→3, 4→5, 6→7 y 8→9. Los tres saltos de mayor magnitud (Medio-Alto) son 4→5 (democratización del acceso), 7→8 (acción autónoma) y 9→10 (auto-gestión del ecosistema).

### Las 6 dimensiones de evaluación

Datos & Arquitectura · Capacidades Analíticas · Personas & Cultura · Gobernanza · Modelo Operativo · Valor de Negocio. Una organización puede estar en etapas distintas según la dimensión.

### Reglas de uso (MUST)

- **La etapa general la fija la dimensión más baja** — es el cuello de botella real.
- **No saltar etapas**: la coexistencia evolutiva exige construir sobre la etapa anterior. Llegar a la Etapa 7 sin la capa semántica de la Etapa 4 produce agentes poco confiables.
- Para comunicación ejecutiva usar los 5 niveles; para diagnóstico táctico, las 10 etapas. El primer diagnóstico estratégico es: ¿de qué lado de El Salto Cuántico está la organización?

---

## 4 · MOTOR — el eje HACER

**MOTOR (Modelo de Madurez de Automatización Organizacional)** mide el grado de automatización de los procesos en **7 niveles**. Su pregunta fundamental: **¿quién ejecuta el trabajo en tu organización — humanos, humanos asistidos, o agentes autónomos?** Es diagnóstico, no prescriptivo; la prescripción vive en el cuerpo complementario *MOTOR in Practice*.

### Los 7 niveles

| # | Nivel (ES · EN) | Quién ejecuta | Pregunta diagnóstica |
|---|---|---|---|
| 1 | **Invisible** · Shadow AI | Humanos (la IA es riesgo oculto) | *¿Saben cuántas herramientas de IA se usan en la organización, quién las usa, y qué datos se comparten con ellas?* |
| 2 | **Confiable** · Trusted | Humanos con copiloto gobernado | *¿Tienen herramientas de IA oficiales con gobernanza, audit trails y protección de datos sensibles implementadas?* |
| 3 | **Colaborador** · Collaborator | Humanos delegan tareas completas; agentes ejecutan bajo aprobación | *¿Los empleados delegan tareas completas a agentes de IA — definiendo el objetivo y recibiendo el resultado — en lugar de solo pedir asistencia puntual?* |
| 4 | **Analista** · Analyst | Agentes 24/7; humano solo en excepciones (>95% autonomía) | *¿Tienen agentes operando 24/7 coordinados entre sí, consultando un modelo digital del sistema, con intervención humana solo en excepciones?* |
| 5 | **Especialista** · Specialist | Agentes con predicción propietaria (moat) | *¿Tienen agentes especialistas con capacidad de predecir eventos y simular escenarios usando datos propietarios que la competencia no puede replicar?* |
| 6 | **Gerente** · Manager | Agentes gestionan equipos, presupuestos y recursos | *¿Tienen agentes con autoridad para asignar trabajo, gestionar presupuestos o tomar decisiones de gestión respaldadas por un modelo digital de toda la organización?* |
| 7 | **Autoridad** · Authority | Agentes en el liderazgo estratégico, redes inter-organizacionales | *¿Tienen agentes que participan en decisiones estratégicas con un modelo digital del ecosistema completo — competencia, mercado, regulación — y simulación de futuros a largo plazo?* |

### Mapa de transiciones (señales diagnósticas, no prescripciones)

| Transición | Nombre | Naturaleza del cambio |
|---|---|---|
| 1→2 | **Trust Infrastructure** | De riesgo a gobernanza |
| 2→3 | **Wingworking** | De asistencia a delegación |
| 3→4 | **Agentic Infrastructure** + DT Descriptivo | De delegación a autonomía |
| 4→5 | **Marketplace de Agentes** + DT Predictivo | De genérico a especializado |
| 5→6 | **Organización Autónoma** + DT Organizacional | De capacidades a autoridad |
| 6→7 | **Social Agentic** + DT del Ecosistema | De intra-org a ecosistema |

### Digital Twins como dimensión diagnóstica

| Nivel | Tipo de Digital Twin | Responde |
|---|---|---|
| 1–3 | No existe | — |
| 4 | **Descriptivo** (infraestructura/operaciones, tiempo real) | ¿qué tengo? ¿qué está pasando? — sin predicción ni simulación |
| 5 | **Predictivo/Prescriptivo** (dominio técnico; requiere 5–10 años de datos propietarios) | ¿qué va a pasar? ¿qué pasa si hago X? |
| 6 | **Organizacional** (personas + finanzas + operaciones + interdependencias) | ¿qué impacto tiene esta decisión en toda la organización? |
| 7 | **del Ecosistema** (org + competencia + mercado + regulación) | ¿qué oportunidades estratégicas existen? |

### Diferenciadores críticos entre niveles adyacentes

- **2 vs 3**: en Nivel 2 la IA asiste *dentro* de la tarea del humano; en Nivel 3 ejecuta *la tarea completa* end-to-end (el humano define y valida).
- **3 vs 4**: Nivel 3 es workflow pre-definido con aprobación humana de cada plan, sin modelo digital; Nivel 4 es decisión autónoma dinámica sobre DT Descriptivo, 24/7.
- **4 vs 5**: Nivel 4 *reacciona* al estado actual (reglas + análisis, sin simulación); Nivel 5 *predice y prepara* antes del evento (simulación de escenarios). Señal Build vs Rent: importa tener la capacidad predictiva operando, no cómo se obtuvo.
- **5 vs 6**: Nivel 5 es DT de dominio técnico con capacidades propietarias; Nivel 6 es DT de TODA la organización y **autoridad organizacional** (agentes gestionan personas y presupuestos).
- **6 vs 7**: Nivel 6 optimiza la organización existente (intra-org, horizonte 6–24 meses); Nivel 7 propone cambiar el juego (inter-org, horizonte 5–10 años, M&A, nuevos mercados).

### Assessment rápido (8 preguntas)

1. ¿Inventario completo de herramientas de IA? No → N1 · Sí con gobernanza → N2+
2. ¿Políticas formales de uso de IA con enforcement? No → N1 · Sí → N2+
3. ¿Trust Infrastructure (tokenización, audit trails)? No → N1 · Sí → N2+
4. ¿Delegan tareas completas end-to-end? No → N2 · Sí con workflow fijo → N3 · Sí con autonomía → N4+
5. ¿Digital Twin Descriptivo en tiempo real? No → N3 o inferior · Sí → N4+
6. ¿Agentes 24/7 con coordinación multi-agente? No → N3 o inferior · Sí → N4+
7. ¿Agentes especialistas con predicción/simulación? No → N4 o inferior · Sí con DT Predictivo → N5+
8. ¿DT Organizacional o del Ecosistema? No → N5 o inferior · Organizacional → N6 · Ecosistema → N7

### Reglas de uso (MUST)

- **Secuencialidad**: no se pueden saltar niveles. Operar en Nivel 4 sin la gobernanza del Nivel 2 genera riesgo, no valor.
- **El nivel general lo fija la dimensión más baja** (mismas reglas de cuello de botella que IRIS; dimensiones: Infraestructura & Agentes · Autonomía Operacional · Personas & Cultura · Gobernanza · Digital Twins · Valor de Negocio).
- **Sweet Spot**: el Nivel 4 (Analista) maximiza el balance retorno/riesgo/inversión y será el baseline competitivo hacia 2030. Las estimaciones de distribución de mercado del libro son referenciales.

---

## 5 · El par diagnóstico

IRIS y MOTOR son **ortogonales**: una organización puede estar alta en uno y baja en el otro. Los cuatro cuadrantes:

- **Sabe todo, hace manual** (IRIS alto, MOTOR bajo): dashboards impecables, decisiones embotelladas.
- **No sabe, pero automatiza a ciegas** (MOTOR alto, IRIS bajo): velocidad sin dirección — el cuadrante de riesgo.
- **No sabe, no hace**: el punto de partida.
- **Sabe todo y ejecuta solo**: el destino — la empresa en tiempo real gobernada por personas.

**Un diagnóstico AURA completo tiene tres componentes:** posición IRIS + posición MOTOR + mix de prioridad Citizen/City/DUAL para el roadmap (§8).

---

## 6 · Data Canon — la gobernanza del dato (instrumento del SABER)

**Tesis.** Data Mesh prescribió descentralizar el ownership del dato por dominio. Tres fuerzas erosionan esa prescripción: (1) los tres modos de falla que Dehghani atribuía a las arquitecturas centralizadas son **límites de escala cognitiva humana**, y la era agentiva los eleva en un orden de magnitud; (2) **la semántica no se inventa: se adopta** — las industrias maduras la externalizaron en estándares (SID/TM Forum, BIAN, ACORD, IFRS/IAS 41, GS1); donde hay estándar, no hay nada local que distribuir; (3) el ownership distribuido pone al definidor de cada cifra a cargo de cómo se reporta esa cifra — un **riesgo de agencia** (Jensen & Meckling) que un marco de control interno (espíritu SOX/COSO) no toleraría. Conclusión sobre-determinada: la recentralización del núcleo agency-crítico es *posible* (era agentiva) y *exigida* (control interno).

**Data Canon** = Data Fabric con principios de *gobernanza* de Mesh, **anclados a un canon central**, operado por agentes, responsable ante el directorio.

### Las tres funciones

| Función | Data Mesh | Data Canon |
|---|---|---|
| **Especificación** (semántica, calidad) | El dominio | El **estándar de industria** (donde existe) + la **autoridad del canon** (lo agency-crítico) + **grupos federados** (core propio no sensible) |
| **Ejecución** (mover, transformar, conformar) | El dominio o la plataforma | La **plataforma agentiva** |
| **Responsabilidad** | El dominio | El **directorio** (adopta estándares) + la **autoridad del canon** + los **grupos federados** (brechas, ensamblaje) |

Regla estructural: **el área medida por una cifra no controla cómo se define esa cifra** (segregación de funciones; control preventivo, no detectivo).

### Las dos capas de gobernanza

- **La autoridad del canon** — central, *delgada*. Custodia la semántica canónica de reporte, las reglas de supervivencia, la política de calidad y la calibración del sistema agentivo. Ratifica; no opera.
- **Los grupos federados de conformidad** — uno por dominio/capa, *ligeros*, cada uno ligado a su foro de estándares. Hacen triaje de brechas, enlace con el foro y modelado del dato propietario no agency-crítico. Lo que toca cifras de reporte sube a ratificación.

La federación está **anclada**: el anclaje impide el problema de agencia; la federación impide que el centro se vuelva una "diva" (punto único de dependencia).

### El estándar-mosaico

El ancla semántica externa varía por industria: telco/banca/seguros tienen modelo único maduro; un conglomerado diversificado **ensambla** su estándar corporativo por capas (contable: IFRS/IAS 41/XBRL — fuerte; trazabilidad: GS1 — fuerte; I+D: BrAPI/MIAPPE — bueno en su nicho; operaciones de campo: parcial; core comercial propio: sin estándar → lo define el canon + grupo federado).

### Arquitectura: el medallion se queda en tres pisos

**Bronze** (crudos fieles por fuente — replicación exhaustiva legítima, "vertedero por diseño") · **Silver** (conformado al modelo canónico/estándar-mosaico) · **Gold** (productos de datos **materializados, selectivos**). Con capa semántica agentiva sobre Silver, **el consumo por defecto es virtual**: el agente compone cualquier vista conforme al canon al vuelo; un mart Gold es la forma cacheada de un patrón que se *ganó* materializarse (volumen, SLA externo, snapshot regulatorio, feature store). El tiempo real lo da Silver + agente, no la cantidad de marts.

### La política de calidad (un solo nivel, estructural, de directorio)

| # | Garantía | Cubre |
|---|---|---|
| 1 | **Tiempo real** | Frescura (piso objetivo; materialización por fases) |
| 2 | **Fiel al origen** | Exactitud/completitud no introducida por la plataforma (acotada por el origen) |
| 3 | **Linaje completo** | Procedencia/trazabilidad — el audit trail |
| 4 | **Conforme al estándar (mosaico)** | Validez — binaria, verificable por máquina |
| 5 | **Reconciliado por reglas de supervivencia** | Consistencia cross-sistema; el golden record sin juicio ad hoc del interesado |

### Falsadores (la tesis se debilita si…)

El dato propietario resulta el grueso del valor, no el margen · las brechas con el estándar no convergen · las capacidades agentivas tienen techo más bajo del asumido · "tiempo real" es infactible para fuentes críticas · el argumento de control no mueve al directorio. Diseño para degradar con gracia: si una capacidad agentiva no rinde, el fallback es trabajo humano en los grupos federados, no el colapso del modelo.

---

## 7 · Wingmap — el levantamiento agentivo (instrumento del HACER)

**Definición.** Técnica de levantamiento agentivo de la inteligencia operacional: un agente de IA con acceso de **lectura** a los canales digitales corporativos (correo, mensajería, repositorios, calendarios, sistemas transaccionales) reconstruye, **sin entrevistas ni talleres**, **dos mapas vivos y conectados**: el mapa del proceso (cómo se ejecuta el trabajo) y el grafo del flujo de información (qué dato se origina dónde, quién lo transforma, hacia dónde viaja). Opera primero en modo pasivo (observación) y, con condiciones, en modo activo (**Wingworking**: el usuario opera vía el agente).

**Hipótesis (tres componentes encadenados):** (1) la inteligencia organizacional accionable no se obtiene preguntando — los ejecutores no pueden articular en abstracto lo que ejecutan en concreto (conocimiento tácito, BAU saturado, descripción políticamente situada); (2) sí se puede reconstruir observando los rastros digitales que la organización ya genera; (3) la reconstrucción debe ser **dual** — proceso *y* flujo de información.

### Los seis principios rectores

1. **Observación primero, intervención después** — (observar → inferir → validar), no (preguntar → escribir → validar).
2. **Doble plano, no uno solo** — omitir cualquiera de los dos mapas rompe la propuesta de valor.
3. **Trazabilidad común a evidencia** — toda afirmación cita el documento crudo del que se infirió; sin trazabilidad, el output es indistinguible de una alucinación plausible.
4. **Validación distribuida en roles operativos** — embajador del proceso valida procesos; dueño operativo del dato valida flujos. No un comité central.
5. **Modo pasivo antes que activo** — el modo activo solo en dominios donde el pasivo ya demostró valor. Invertir el orden produce abandono.
6. **Producir sustrato, no consumir requerimiento** — el output es un modelo persistente y validado que múltiples destinos consumen (specs de datos, BPM, prompts de agentes operacionales, briefings).

### Las fases (MUST: secuenciales; las pre-condiciones son bloqueantes)

- **Fase 0 — Pre-condiciones** (bloqueantes): sponsor ejecutivo con autoridad · scope acotado y consentido · embajador del proceso designado · dueños del dato identificados · marco legal/compliance validado para la jurisdicción.
- **Fase 1 — Observación**: mínimo 3 iteraciones del ciclo del proceso más lento Y nunca menos de 2 semanas. Entregable: reporte de cobertura.
- **Fase 2 — Inferencia**: 3–5 mapas de proceso candidatos + 5–10 flujos cross-rol candidatos, con evidencia trazable y confianza por elemento.
- **Fase 3 — Validación dual**: sesiones de 60–90 min; umbrales del primer despliegue: **70%** de mapas de proceso y **60%** de flujos validados sin corrección mayor; si no se alcanzan en dos iteraciones, diagnóstico y decisión del sponsor.
- **Fase 4 — Mantenimiento**: los grafos viven. Métrica clave: **latencia del grafo** (último evento relevante ↔ versión vigente) bajo el umbral acordado (típico: 24–72 h).
- **Fase 5 (opcional) — Modo activo selectivo**: produce una biblioteca de bots determinísticos, gobernada con disciplina DevOps.

### Zonas de no aplicabilidad (declarar antes de desplegar)

- **Procesos fuera del rastro digital** (papel, presencial, WhatsApp informal): la cobertura cae — administrativo 70–90%, comercial 40–60%, campo <40%. Elegir pilotos de alta cobertura.
- **Bajo apetito de discovery**: la autorización de observación es decisión política; sin ella la técnica no aplica.
- **Privacidad y compliance**: AI Act, GDPR y análogos, derecho laboral sobre monitoreo — asesoría legal específica, consentimiento informado, tokenización/redacción de PII. No es opcional ni post-hoc.
- **La dependencia humana se desplaza, no se elimina**: el cuello de botella pasa de describir a validar (factor de reducción 4–10×, no cero).
- **Madurez tecnológica**: tasas de inferencia actuales adecuadas para hipótesis validables, no para producción autónoma sin supervisión.

### Distinciones de categoría

- **vs process mining clásico**: lo extiende a los canales no estructurados donde el proceso real vive; añade el segundo grafo (flujo de información) que los logs de ERP no pueden capturar.
- **vs consultoría tradicional**: reemplaza el levantamiento artesanal (velocidad, costo, cobertura, continuidad — un orden de magnitud); no reemplaza la interpretación estratégica ni la negociación del cambio.
- **vs copilotos individuales**: el copiloto opera la sesión de un usuario; Wingmap opera el flujo agregado cross-rol.
- **vs AI-builders**: ellos son agentivos para construir, pre-agentivos para correr; Wingmap es agentivo para levantar y produce el sustrato que los agentes de runtime necesitan.

---

## 8 · Casos de Uso — el portafolio (marco de decisión)

Responde la tercera pregunta del camino: **¿qué hacemos primero?** — con un portafolio estructurado, no una lista de ocurrencias.

### CU y SV

- **Caso de Uso (CU)**: bloque atómico — capacidad específica, acotada, *reutilizable*. Se describe por qué hace, por qué la IA lo hace mejor, y qué madurez exige.
- **Solución de Valor (SV)**: configuración estratégica — conjunto de CU integrados que resuelven un problema de negocio completo ante un decisor (problema, solución, métricas, retorno).
- Relación de **composición**: un CU puede venderse solo (modular) o dentro de una SV (integral). Ambos catálogos vivos y enlazados (MUST: referencias cruzadas completas).

### Las tres dimensiones de clasificación

1. **Nivel de madurez requerido** — el nivel MOTOR (y, según el caso, la etapa IRIS) que el caso presupone. Ancla el portafolio al diagnóstico: casos del nivel actual = *quick wins*; un nivel arriba = *sweet spot* (la frontera alcanzable); varios niveles arriba = visión declarada, no compromiso.
2. **Beneficiario del impacto** — Citizen / City / DUAL (abajo).
3. **Dominio de negocio** — segmentación temática para filtrar la oferta en segundos ante el foco del decisor.

### El marco Citizen / City / DUAL

| Clasificación | Quién percibe el beneficio | Función estratégica |
|---|---|---|
| **CITIZEN** | La audiencia externa (ciudadano, cliente, usuario) | Apoyo visible, legitimidad |
| **CITY** | La audiencia interna (la organización) | Eficiencia, compliance, sostenibilidad |
| **DUAL** | Ambas | Consenso: cada actor tiene su victoria visible |

Nació en gobierno local pero es genérico (banca: cliente/compliance; salud: paciente/equipos clínicos; telco: suscriptor/operación de red). Es transversal a IRIS y MOTOR: clasifica por beneficiario, no por eje.

**Dos estrategias canónicas:** **Citizen-First** (visibilidad y legitimidad primero; pool = CITIZEN + DUAL; riesgo: ROI difuso) y **City-First** (eficiencia y alivio interno primero; pool = CITY + DUAL; riesgo: el beneficio no se percibe afuera). Los casos **DUAL son el núcleo común** — la moneda más cara del portafolio: escasean y *se diseñan*. La estrategia se elige por contexto, no por ideología; el marco prioriza *dentro* de cada nivel de madurez, no sustituye la trayectoria.

### La disciplina del ROI (MUST)

1. Todo ROI estimado se declara **referencial** — visible, sin asterisco escondido — hasta que exista línea base validada.
2. El **valor social** se separa del retorno financiero y se defiende en sus propios términos.
3. La **línea base se valida** antes de declarar retorno (protocolo de validación independiente).

### Cómo usar este marco

1. Diagnosticar primero (posición IRIS + posición MOTOR) — sin esto el portafolio no tiene ancla.
2. Inventariar con las tres dimensiones — lo que no se puede clasificar no está suficientemente definido.
3. Separar CU de SV, con referencias cruzadas completas.
4. Elegir estrategia por contexto (decisión explícita del liderazgo, revisable, DUAL al frente).
5. Atacar el nivel actual + 1 (quick wins para momentum; sweet spot para tracción).
6. Declarar el ROI con honestidad.

---

## 9 · Glosario canónico (alfabético)

- **Agéntico** — mundo de agentes complementarios; interfaces persisten. Evolución incremental. Es el único sentido de "agéntico" en el libro; el sentido tecnológico-positivo se dice siempre *agentivo* (Wingmap: levantamiento agentivo, era agentiva, pre-agentivo).
- **Agentivo** — mundo donde los agentes reemplazan las interfaces; transformación fundamental. La tesis central del libro vive en este horizonte.
- **Agentic Infrastructure** — protocolos y servicios que permiten a múltiples agentes comunicarse, coordinarse y ejecutar autónomamente. Señal de la transición MOTOR 3→4.
- **AURA** — Arquitectura Unificada de Referencia Agentiva: dos ejes diagnósticos (IRIS · MOTOR) + instrumentos (Data Canon · Wingmap) + marco de decisión (Casos de Uso).
- **Autopilot** — operación autónoma 24/7 con intervención humana solo en excepciones. Característica definitoria del Nivel 4 de MOTOR.
- **Autoridad del canon** — órgano central *delgado* que custodia el canon (semántica de reporte, reglas de supervivencia, política de calidad, calibración agentiva). Ratifica; no opera.
- **BYOA (Bring Your Own Agent)** — patrón del Nivel 1 de MOTOR: cada empleado elige su herramienta de IA sin coordinación.
- **Canon (el)** — cuerpo central no discrecional al que todo se conforma: estándares adoptados + reglas de supervivencia + política de calidad. Ningún dominio puede redefinirlo.
- **Caso de Uso (CU)** — bloque atómico del portafolio: capacidad específica, acotada, reutilizable.
- **Citizen / City / DUAL** — clasificación por beneficiario del impacto: audiencia externa / audiencia interna / ambas.
- **Coexistencia evolutiva** — cada etapa/nivel subsume al anterior; la infraestructura previa se vuelve cimiento, no legado.
- **Data Canon** — patrón de gobernanza de datos: Data Fabric + principios de gobernanza de Mesh anclados a un canon central; semántica adoptada de estándares; política de calidad de directorio; federación de conformidad por dominio.
- **Data Fabric** — capa de integración con metadatos activos, transformación inferida y capa semántica; el sostén técnico que la era agentiva potencia.
- **Data Mesh** — patrón de Dehghani (2019–2022): ownership por dominio, datos como producto, plataforma self-serve, gobierno federado. Data Canon no lo refuta: lo datea.
- **Digital Twin (DT)** — modelo digital sincronizado de un sistema, organización o ecosistema. Indicador transversal de madurez MOTOR: **Descriptivo** (N4) → **Predictivo/Prescriptivo** (N5) → **Organizacional** (N6) → **del Ecosistema** (N7).
- **El Salto Cuántico** — colapso del costo de la pregunta analítica de semanas a segundos. En IRIS, el salto 4→5: frontera entre fundamentos y empresa en tiempo real.
- **Empresa en línea** — accede a información actualizada pero depende de humanos para interpretar y actuar.
- **Empresa en tiempo real** — detecta, interpreta, decide y actúa de forma continua y autónoma, con gobernanza humana.
- **Era agentiva** — estado del arte en que sistemas de IA ejecutan autónomamente mapeo de esquemas, resolución de entidades, transformación y mantenimiento de pipelines a escala impracticable para equipos humanos.
- **Estándar-mosaico** — el estándar corporativo ensamblado: estándares externos por capa + modelo propio para el core que ningún cuerpo cubre.
- **Grupos federados de conformidad** — red de grupos ligeros, uno por dominio/capa, ligados a su foro de estándares: triaje de brechas, enlace río arriba, modelado del dato propietario no agency-crítico.
- **Inteligencia organizacional** — capacidad de transformar datos en conocimiento y acción de forma continua y autónoma (las cuatro capas de la Pirámide, no solo las dos primeras).
- **IRIS** — Modelo de Madurez de Inteligencia Organizacional: 10 etapas, 5 niveles, eje SABER.
- **La Línea Nadella** — pregunta divisoria entre los mundos agéntico y agentivo: *¿sus empleados todavía abren aplicaciones para hacer su trabajo?*
- **Latencia del grafo** — métrica de mantenimiento de Wingmap: distancia temporal entre el último evento observado relevante y la versión vigente del grafo.
- **Marketplace de Agentes** — ecosistema donde capacidades de agentes se adquieren o comercializan entre organizaciones. Señal de la transición MOTOR 4→5.
- **Medallion (Bronze/Silver/Gold)** — las tres zonas del lakehouse: crudos fieles · conformado al canon · productos materializados selectivos.
- **Moat** — ventaja competitiva sostenible; en MOTOR emerge en Nivel 5 con datos propietarios alimentando predicción.
- **MOTOR** — Modelo de Madurez de Automatización Organizacional: 7 niveles, eje HACER.
- **Organización Autónoma** — agentes gestionan procesos y personas con métricas objetivas y simulación sobre el DT Organizacional. Señal de la transición MOTOR 5→6.
- **Pirámide del Valor (de los Datos)** — DATOS → INFORMACIÓN → CONOCIMIENTO → ACCIÓN.
- **Problema de agencia** — (Jensen & Meckling, 1976) conflicto estructural: quien gestiona recursos ajenos tiende a presentar su gestión de la forma que más lo favorece. La crítica de gobierno a Data Mesh deriva de aquí.
- **Quick Win** — caso de uso con alta visibilidad, baja complejidad y ROI rápido (típicamente <6 meses); genera momentum en transiciones tempranas.
- **Reglas de supervivencia** — reglas pre-especificadas (parte del canon) que deciden qué valor prevalece en el registro dorado cuando varias fuentes discrepan.
- **Shadow AI** — uso no gestionado de IA sin gobernanza, compliance ni visibilidad. Estado definitorio del Nivel 1 de MOTOR.
- **Social Agentic** — ecosistema donde agentes de distintas organizaciones colaboran con identidades verificables. Señal de la transición MOTOR 6→7.
- **Solución de Valor (SV)** — configuración estratégica: CU integrados que resuelven un problema de negocio completo ante un decisor.
- **Sweet Spot** — nivel donde se maximiza el balance retorno/riesgo/inversión. En MOTOR: Nivel 4. En el portafolio: el nivel actual + 1.
- **Trust Infrastructure** — tecnologías de confianza (tokenización, anti-prompt injection, audit trails, compliance automático) que permiten usar IA gobernada y auditable. Señal de la transición MOTOR 1→2. (Término compartido con *AgencyDomains*, donde es el eje transversal de la arquitectura.)
- **Wingmap** — técnica de levantamiento agentivo: dos mapas vivos y conectados (proceso + flujo de información) reconstruidos desde rastros digitales, sin entrevistas.
- **Wingworking** — metodología de colaboración humano-IA (César Obach): el humano como piloto (decisiones estratégicas, validación), el agente como wingman (ejecución táctica delegada). Señal de la transición MOTOR 2→3 y modo activo de Wingmap.

---

## 10 · Relación con la trilogía

- ***AgencyDomains* — la arquitectura** (Libro III del mapa, publicado en agencydomains.org): las primitivas, las capas, la Trust Infrastructure del destino. Tiene su propio manifiesto canónico para agentes; ante términos arquitectónicos (AgencyDomain, Botlet, Capability, Faceta), ese manifiesto manda.
- ***Postchat* — el destino** (Libro I, en gestación): cómo se ve el mundo cuando la transición quedó atrás.
- ***AURA* — el camino** (este libro): dónde está parada la organización, qué trayectoria tiene por delante, en qué orden recorrerla y con qué instrumentos.

Regla de lectura cruzada: AURA diagnostica y prepara; AgencyDomains especifica el destino. Una organización madura en ambos ejes de AURA termina operando la arquitectura que AgencyDomains describe.
