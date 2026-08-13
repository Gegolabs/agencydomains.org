---
título: AgencyDomains — Manifiesto canónico para agentes
edición: Primera edición · v1.0 · Agosto 2026
fuente_canónica: libro-agency_domains-v1.0 (libro humano)
licencia: GFDL v1.3
audiencia: agentes que deben razonar dentro del framework
estado: v1.0 — primera edición; referencias estables desde esta versión
---

# AgencyDomains — Manifiesto canónico para agentes

> Extracto estructurado de la edición **v1.0 (primera edición)** del libro *AgencyDomains: arquitectura del Mundo Agentivo*. Este documento condensa el vocabulario canónico, las construcciones formales y las propiedades exigidas. La versión humana del libro contiene además motivación, datos de industria, ejemplos extendidos y derivaciones — todo eso queda fuera de aquí.

> Este canon contiene la **estructura y el vocabulario** del Mundo Agentivo: definiciones, primitivas, propiedades exigidas, separaciones canónicas. **No contiene métodos para implementar ni catálogos operacionales** — esos viven en cuerpos complementarios. La implementación de referencia pública es **AgencyDomains.org**, materializada en **Vergis**, diseñada para que cualquier desarrollador o estudiante pueda descargarla, leerla, ejecutarla y aprender cómo el canon se traduce en sistemas vivos. Otros implementadores (productos comerciales, códices propietarios) ofrecen sus propios cuerpos complementarios sobre la misma estructura canónica.

## Cómo usar este documento

- **Es contexto canónico**, no resumen ejecutivo. Cada definición y propiedad importa para razonar dentro del framework.
- **Serie**: AgencyDomains es el Libro III de la trilogía del Mundo Agentivo — *La Empresa en Tiempo Real* (el destino; manifiesto propio) · *AURA* (el camino; manifiesto propio) · **AgencyDomains** (la arquitectura). Los términos compartidos (la Línea Nadella, agentivo, empresa en tiempo real, Trust Infrastructure) son consistentes entre libros.
- **Espejo de v1.0** — la edición vigente del libro. Si este documento contradice al libro humano, el libro humano gana.
- **Vocabulario obligatorio**: los términos en `código` y **negrita** son canónicos. No sustituir por sinónimos.
- **Convenciones MUST/SHOULD**: la spec usa esos verbos en sentido RFC 2119.
- **Estado v1.0**: el libro está publicado como primera edición en agencydomains.org. Desde esta versión los términos, las estructuras y la numeración son estables: lo que cambie se anunciará en el `CHANGELOG.md` del libro.
- **Cambios v0.7 vs v0.6**: el género de las piezas empaquetadas de Capa 3 recibe **nombre propio: Let (plural Lets)** — derivado del sufijo `-let` de la propia familia; vocabulario normado al rango de Botler, no una novena primitiva; «unidad empaquetada de Capa 3» queda como definición descriptiva. Relación canónica: **`1 Proceso = 1 Botler + N Lets`**. Invariante ES/EN. Resuelve la sobrecarga de «unidad» (colisión con «unidad mínima de despliegue»).
- **Cambios v0.6 vs v0.5**: el **Agentlet** se incorpora como **octava primitiva canónica** — unidad hermana del Botlet cuyo cuerpo invoca **inferencia acotada**; casa de la tarea recurrente en forma pero interpretativa en cada instancia (Cap. 5 §7). Con él: el género **unidad** (`1 Proceso = 1 Botler + N unidades`; el Botler hospeda Botlets y Agentlets con un punto de control más en el handle — `cognition_call`); el paraguas **Agente** pasa a tres miembros (Asistente · Agente Autónomo · Agentlet; **el Agente tiene agenda, el Agentlet tiene charter**, con test de frontera de tres preguntas); la **regla de contrabando** bidireccional (inferencia en el cuerpo → Agentlet; cuerpo determinístico → Botlet); **proto-Agentlet** en la cadena de derivación y los catálogos; semántica de **madurez propia** (estabilización del spec y tasa de escalamiento decreciente — no convergencia a determinismo; offline solo con modelo edge declarado); la **economía de los tres peldaños** (Botlet ~0 · Agentlet acotado · Cognición plena); y el pilar de **Validación con sede en Capa 3** sobre la inferencia acotada.
- **Cambios v0.5 vs v0.4**: pasada editorial integral de la trilogía — las **generaciones del Botlet** `G1`/`G2`/`G3` se formalizan en el Cap. 5 §2 (el Epílogo conserva el ensayo de fondo sin carga normativa); el **Producto de Información** obtiene casa canónica como término normado de la spec de Botlets (multi-vista, drill-through y sus MUST); **doctrina Capability restaurada** — la localidad (cloud/edge/híbrido) y la certificación regulatoria se predican del **Conector** (ESC/POS-Printer, Cash-Drawer, Pinpad y DTE-SII reclasificados) y la **Capability regulada** porta el saber normativo; el **Botler** deja de llamarse primitiva (constructo normado de la spec de Botlets; el canon sigue siendo de siete); Cap. 2 ↔ Cap. 7 desduplicados y Cap. 4 adelgazado a favor del Cap. 5; tabla de actores del Cap. 6 alineada con su texto y «Plataforma integral» corregida en el glosario; **rescate fundacional** del documento original *La Línea Nadella* (cita completa de Nadella con su mecánica CRUD y sus dos fases, espectro con el polo extremo, contra-argumentos con las respuestas del canon, precedentes históricos de coexistencia en el Cap. 2, crisis de monetización del SaaS en el Cap. 6); micro-sección «La trilogía» con las cinco especificaciones de AURA; **Dominion** adoptado por el Epílogo; Wingtraining, SME y RLS definidos en el glosario.
- **Cambios v0.4 vs v0.3**: extensiones canónicas surgidas al construir la implementación de referencia y proyectos reales — **Vergis** (implementación de referencia pública, AGPL, AgencyDomains.org) con el esquema de nombres Vergis · Botler · Mira; **proto-Botlet** incorporado al elenco de primitivas (templado · platafórmico) y la **cadena de derivación** casos-uso → Botlets → proto-Botlets; **generaciones del Botlet** G1/G2/G3 con la reconciliación de dos ejes; **manifestación** y **temporalidad** (`discreta`/`continua`) como atributos del Botlet; **Botler genérico** (sin subtipos por dominio; valida orquestando; interfaz Capa 2 ↔ Capa 3 vía `MCP`; código fuente vs spec; un Botlet por `PI`); corrección del misnomer "A2A interna" (`A2A` reservado a la relación entre AgencyDomains); `Capability` reservada al saber-hacer cognitivo de Capa 2, con **Conector** (Capa 4), **Plantilla** (Capa 1), **feature** y **portabilidad de la Capability**; **interacción declarada acotada** (Faceta embebida) y **PI multi-vista con drill-through**; **contrato declarativo de calidad** en Trust Infrastructure.
- **Cambios v0.3 vs v0.2**: tres tiempos del agente (Preparación · Atención · Ingeniería), composición de la Capa 1 (shell · vista · operación), y la Faceta como primitiva atómica de Capa 1.
- **Cambios v0.2 vs v0.1**: título principal *AgencyDomains* + diez extensiones (madurez Botlet, Capa 3 distribuida, portabilidad, seed/emergente, certificación en Capability, localidad de Capabilities, GUI on-the-fly, continuidad operacional, topología paralela, título).

---

## 1 · Vista panorámica

```
                    EL PARADIGMA
                          │
                          ▼
              ┌─────────────────────────┐
              │                         │
      La Línea Nadella           El Mundo Agentivo
      (la pregunta)              (las consecuencias)
                          │
                          ▼
                LA ARQUITECTURA AGENTIVA
                          │
          ┌───────────────┼───────────────┐
          │               │               │
     4 capas         Trust Infra      Agent First
     (topología      transversal      (principio rector)
     paralela)
                          │
                          ▼
                   LAS PRIMITIVAS
                          │
   ┌──────────┬───────────┼───────────┬──────────┐
AgencyDomain Botlet    Capability   Trust    Asistente
+ proto-     + Agentlet (Capa 2 ·    Infra    vs Agente
Botlet       (Lets:     Conector ·            Autónomo
(pre-forjado)manifest./ Plantilla)            + Faceta
             temporal.)
                          │
                          ▼
                   EL POSICIONAMIENTO DE MERCADO
                   (Cadena de valor IA · 11 × 4)
                          │
                          ▼
                   LAS APLICACIONES
                   (Conocimiento en tiempo real ·
                    Kimball Barnizada · BI conversacional)
                          │
                          ▼
                   LA OPERACIÓN
                   (Trust Infra operacionalizada ·
                    políticas · CRUDLEX · log ·
                    continuidad operacional)
```

**Las ocho primitivas canónicas**: **AgencyDomain** · **Botlet** · **proto-Botlet** · **Agentlet** · **Capability** · **Trust Infrastructure** (eje transversal) · **Asistente vs Agente Autónomo** · **Faceta**. El **proto-Botlet** es la pieza pre-forjada que el agente configura para instanciar un Botlet; el **Agentlet** es la unidad hermana del Botlet con inferencia acotada; la **Faceta** es la primitiva atómica de la Capa 1.

> **Nota de numeración**: cuando el canon rotula la Faceta como *sexta primitiva*, el proto-Botlet como *séptima primitiva* y el Agentlet como *octava primitiva*, el ordinal indica el **orden de incorporación al canon** (Faceta en v0.3, proto-Botlet en v0.4, Agentlet en v0.6), **no** la posición en esta lista.

**Capa pre-agentiva (BCA)**: cartografía del estado *previo* al cruce de la Línea Nadella. Tres capas (Presentation · Business Logic · Domain), siete separaciones estructurales (la séptima, canónica: Procedural / Agentic), con mapping explícito a cómo migra cada celda al Mundo Agentivo.

**Implementación de referencia**: **Vergis** — la implementación de referencia pública de AgencyDomains (AGPL, AgencyDomains.org), categoría **Meta-Cognitive Platform**. Materializa el canon en un runtime ejecutable.

---

## 2 · El paradigma — la Línea Nadella

### Pregunta divisoria

> *¿El humano abre aplicaciones para hacer su trabajo?*

Origen del nombre: Satya Nadella en el podcast BG2 (diciembre 2024) — *"La noción de que las aplicaciones de negocio existen, probablemente es donde todo colapsará, en la era de los agentes."*

### Dos mundos

```
◄──── Mundo Agéntico ────┤├──── Mundo Agentivo ────►
Apps complementadas        Apps colapsan
por copilotos              Conversación con agentes
Evolución incremental      Aplicaciones sobreviven
                           como backend invisible
                           Transformación fundamental
```

- **Agéntico** — agentes son herramientas complementarias que extienden las aplicaciones existentes. Los humanos siguen abriendo aplicaciones. Las interfaces tradicionales persisten; los agentes las potencian.
- **Agentivo (Mundo Agentivo)** — agentes como interfaz única. Las aplicaciones colapsan. El humano deja de abrir aplicaciones; conversa con agentes que tienen acceso a sistemas y datos.

### Empresa en línea vs Empresa en tiempo real

- **Empresa en línea** — datos actualizados al segundo, dashboards al día, pero **depende de humanos** para mirar, interpretar y decidir.
- **Empresa en tiempo real** — **detecta, interpreta, decide y actúa** de forma continua y autónoma, dentro de marcos gobernados. Producto del cruce de la Línea Nadella.

### Tres ejes de cambio profundo

El cruce de la Línea Nadella cambia **seis dimensiones** simultáneas de la operación (relación humano-información, naturaleza de los datos, roles del trabajo humano, economía de la información, gobernanza, modelo operativo). Ninguna cambia aislada. Esas seis dimensiones se agrupan en **tres ejes**:

1. **Relación humano-información + roles del trabajo humano.**
2. **Datos + modelo operativo.**
3. **Gobernanza + economía de la información.**

Los tres son interdependientes: avanzar en uno solo sin los demás produce **pilotos exitosos pero no transformación real**. El cruce es sistémico o no es.

### Coexistencia evolutiva

```
Etapa 1 (Inicial):      Asistente 90%  ████████████████░░  Agente Autónomo 10%
Etapa 2 (Adopción):     Asistente 70%  ████████████░░░░░░  Agente Autónomo 30%
Etapa 3 (Madurez):      Asistente 50%  █████████░░░░░░░░░  Agente Autónomo 50%
Etapa 4 (Avanzada):     Asistente 30%  █████░░░░░░░░░░░░░  Agente Autónomo 70%
```

---

## 3 · El estado pre-agentivo — Bounded Concerns Architecture

> Cartografía formal del estado *previo* al cruce. No es la arquitectura del destino — es la arquitectura de la transición.

### Principio operacional — la delgadez del dominio

Los agentes son **volátiles** (corrección estadística, evolución por reentrenamiento). Las invariantes del negocio **no pueden serlo** (corrección binaria, ritmo estructural). Si coexisten en la misma capa sin frontera explícita, la volatilidad agéntica contamina la confiabilidad del dominio.

→ **El núcleo autoritativo se mantiene estrictamente delgado**, expulsando toda lógica volátil hacia afuera. La incursión agéntica queda confinada a la capa diseñada para tolerar volatilidad.

### Tres capas

| Capa | Contenido |
|---|---|
| **1 · Presentation** | UI (humanos) · API (sistemas) — tratados como ciudadanos paralelos. |
| **2 · Business Logic** | Orquestación. Dos cajas paralelas: **Procedural** (programado explícitamente) · **Agentic** (derivado contextualmente desde un modelo). |
| **3 · Domain** | Núcleo estable. Dos dimensiones ortogonales: **SOR** (System of Record, dominio propio) vs **External** (dominio ajeno) en el eje vertical; **Logic** vs **Persistence** en el eje horizontal. Cada celda se subdivide en vía síncrona y asíncrona. |

Asimetría léxica deliberada en la pierna asíncrona: **Streams** (lado SOR — saliente, autoría propia) vs **Hooks** (lado External — entrante, autoría ajena).

### Las siete separaciones estructurales

| # | Separación | Materializada por |
|---|---|---|
| 1 | Presentación humana vs contrato externo | UI y API en Capa 1 |
| 2 | Orquestación vs reglas del dominio | Frontera Capa 2 / Capa 3 |
| 3 | Lógica vs persistencia | Bandas horizontales en Capa 3 |
| 4 | Dominio propio vs ajeno | Columnas SOR / External en Capa 3 |
| 5 | Comunicación síncrona vs asíncrona | Vías paralelas dentro de cada celda |
| 6 | Estado mutable vs log de eventos | Pares Repository/Streams y Proxies/Hooks |
| 7 | Comportamiento procedural vs agéntico | Cajas Procedural / Agentic en Capa 2 |

La **séptima separación** es la grieta inicial por la cual el Mundo Agentivo entra al sistema empresarial.

### Mapping de celdas BCA al Mundo Agentivo

| Celda BCA | Trayectoria | Destino |
|---|---|---|
| **UI** | Se vacía progresivamente | Reemplazada por Capa 1 — Interacción (modalidades conversacionales, GUI on-the-fly, GUI persistente como Botlet de fachada, señalética); la UI tradicional sobrevive solo en herramientas especializadas de superficie compleja |
| **API** | Persiste y se intensifica | Se convierte en **Conector** dentro de la Capa 4 — Acceso (NO en Capability) |
| **BL · Procedural** | Se contrae | Reemplazada por Botlets. Sobreviven sólo workflows con trazabilidad regulatoria estricta |
| **BL · Agentic** | Se expande hasta dominar | **Semilla operativa del Botlet**. La séptima separación se ensancha hasta consumir la capa |
| **SOR · Logic** | Se preserva | Lógica de invariantes dentro del AgencyDomain |
| **SOR · Persistence** | Se preserva | Capa de almacenamiento del AgencyDomain |
| **External · Logic** | Se preserva, se reposiciona | Patrones de federación gestionados por Trust Infrastructure |
| **External · Persistence** | Se preserva | Capa de almacenamiento de la federación |
| **Eventos (sync/async SOR)** | Se preservan, ganan peso | Sustrato de coordinación entre Botlets y AgencyDomains |

**Cuatro patrones generales del cruce**:

1. La **Capa 3 sobrevive casi intacta** — se vuelve sustrato de los AgencyDomains.
2. La **Capa 2 se transforma profundamente** — Procedural se contrae; Agentic domina; ambas se vuelven Botlets que componen comportamiento desde Capabilities.
3. La **Capa 1 se bifurca asimétricamente** — UI muere; API prospera como **Conector** (Capa 4).
4. **Trust Infrastructure aparece como concern transversal nuevo** — lo que en BCA estaba implícito y disperso se eleva a capa transversal explícita.

---

## 4 · La arquitectura — cuatro capas en topología paralela

> **Aclaración canónica**: las cuatro capas son una **radiografía del agente individual** — los cuatro comportamientos que todo agente debe exhibir. **NO son eslabones de una cadena de valor industrial** ni slots donde se asigne un producto a cada uno. La cadena industrial se trata en Capítulo 6 — son lentes distintas que se cruzan limpiamente cuando se mantienen separadas.

### La topología paralela

**Las Capas 2 (Cognición) y 3 (Autonomía) son vías paralelas entre Capa 1 y Capa 4, no etapas en serie.** La numeración 1 → 2 → 3 → 4 tiene valor didáctico — Capa 1 es la superficie con la que el humano se encuentra, Capa 4 es donde el sistema toca al mundo real — pero **no describe el orden en que las operaciones atraviesan el sistema**. Una operación entra por Capa 1 y llega a Capa 4 atravesando una de las dos vías — o ambas en distintos tramos —, pero nunca ambas en serie obligatoria.

```
                ┌──────────────────────────┐
                │  Capa 1 · Interacción    │
                └────┬───────────────────┬─┘
                     │                   │
                     ▼                   ▼
           ┌─────────────────┐ ┌─────────────────┐
           │  Capa 2         │ │  Capa 3         │
           │  Cognición      │ │  Autonomía      │
           │                 │ │                 │
           │  Conversación   │ │  Botlets        │
           │  Decisión nueva │ │  Patrón estable │
           │  Caso nuevo     │ │  (ciclo 95/4/1) │
           └────────┬────────┘ └────────┬────────┘
                    │                   │
                    ▼                   ▼
                ┌──────────────────────────┐
                │  Capa 4 · Acceso         │
                │  (Capabilities)          │
                └──────────────────────────┘

         Trust Infrastructure (transversal a las cuatro)

         Interacción 2 ↔ 3 (interna · vía `MCP`):
           · Cognición delega a Botlet (2 → 3)
           · Botlet escala fallback a Cognición (3 → 2)
           · Cognición observa el log de Botlets (2 ← 3)
```

**Interfaz Capa 2 ↔ Capa 3 vía `MCP`**: la **Cognición** (agente `LLM`, Capa 2) comanda su memoria muscular — el **Botler** (runtime de Capa 3, sin agencia) — por una interfaz **interna** dentro del mismo AgencyDomain. El transporte natural es `MCP`: el Botler expone servidor(es) `MCP`, la Cognición es el cliente. **Esto NO es `A2A`**: `A2A` (la relación agente-a-agente) queda reservado a la comunicación **entre AgencyDomains** distintos.

**Régimen de cada vía**:

- **Vía Cognición** — lenta, costosa, decisiva. Para conversación, decisiones nuevas, casos no anticipados.
- **Vía Autonomía** — rápida, barata, repetitiva. Para ejecución de Botlets sobre patrones estables.

**Cinco consecuencias estructurales** de la topología paralela:

1. **Modo offline trivial** — sin red, la vía Cognición (cloud) cae; la vía Autonomía (edge) sigue activa. La operación atraviesa el AgencyDomain por la vía que sigue viva.
2. **Economía cognitiva evidente** — la organización elige por qué vía fluye cada operación: repetitiva → vía 3 (barata); nueva o decisiva → vía 2 (costosa). El costo total es el mix de las dos vías.
3. **Trust Infrastructure se ejerce en ambas vías** — las políticas se aplican antes de invocar Capa 4 sin importar de qué vía viene la invocación.
4. **Distingue dos tipos de Botlets** — **Botlets de fachada operativa** (invocables desde Capa 1, contrato estable, identidad humana propagada) vs **Botlets de herramienta interna** (invocables solo desde Capa 2). Ambos viven en Capa 3; difieren en su superficie de invocación.
5. **`Capa 1 → Capa 3 → Capa 4` es vía canónica** — una superficie operativa (POS, pantalla cocina, panel industrial) que invoca un Botlet senior atraviesa esta vía sin tocar Capa 2. **No es bypass; es una de las dos vías estructurales.**

### Los tres tiempos del agente

La topología paralela describe **dónde** vive cada operación. Los tres tiempos describen **cuándo** opera el agente. Marco temporal canónico, complementario al espacial.

| Tiempo | Régimen | Métricas | Vía cognitiva |
|---|---|---|---|
| **Preparación** | Batch · off-peak | Calidad del catálogo · precisión de Botlets · cobertura de Capabilities | Cognición sobre datos consolidados |
| **Atención** | Tiempo real · prioritario | Satisfacción · latencia · tasa de resolución sin escalamiento | Cognición + Autonomía según patrón |
| **Ingeniería** | Mediano plazo (minutos a horas) | Cobertura · tasa de éxito al primer deploy · iteraciones promedio | Cognición decide · Autonomía persiste |

**Implicaciones operativas**:
- **Scheduling de capacidad cognitiva**: Atención prioritaria; Preparación aprovecha valles; Ingeniería intermedia. Sin la distinción, la Preparación queda relegada y el agente deja de mejorarse.
- **Métricas separadas por tiempo**: un solo dashboard miente; la calidad del catálogo se mide distinto que la satisfacción operativa.
- **Modelo de disponibilidad**: un agente bien operado **no está 100% en Atención** — necesita ventanas de Preparación. La promesa "agente siempre disponible" se entiende como "Atención siempre disponible".

> *El agente no atiende en todo momento — pero puede atender en cualquier momento porque dedica tiempo a prepararse.*

**Propiedades exigidas**:
- Reconocimiento explícito de los tres tiempos en la operación (MUST).
- Métricas separadas por tiempo (MUST).
- Ventanas de Preparación reservadas, no opcionales (SHOULD).
- Scheduling de capacidad cognitiva por prioridad de tiempo (SHOULD).
- Trazabilidad de qué tiempo ejecutó qué operación en el log (SHOULD).

### Diagrama estructural — todas las capas con topología paralela

```
                ┌──────────────────────────────────────────────────────────┐
                │  CAPA 1 · INTERACCIÓN                                    │
                │  Conversacional puro · GUI on-the-fly · GUI persistente  │
                │  (Botlets de fachada) · Voz · API · Canales · Señalética │
                └────┬─────────────────────────────────────────────────┬───┘
                     │                                                 │
                     ▼                                                 ▼
       ┌────────────────────────────┐               ┌────────────────────────────┐
       │  CAPA 2 · COGNICIÓN        │               │  CAPA 3 · AUTONOMÍA        │
       │  Multi-LLM · Capabilities  │               │  Botlets y Agentlets       │
       │  Pattern Recognition       │  ◄── 2 ↔ 3 ──►│  Botler (central + edge)   │
       │  Generación de Botlets     │               │  Tareas asíncronas         │
       │  Asistente reactivo        │  ◄── `MCP` ──►│  Monitoreo · protocolo A2A │
       │  Lenta · costosa · nueva   │   interno     │  Garantía de fallback      │
       └─────────────┬──────────────┘               └─────────────┬──────────────┘
                     │                                             │
                     ▼                                             ▼
                ┌──────────────────────────────────────────────────────────┐
                │  CAPA 4 · ACCESO                                         │
                │  Tools (MCP) · A2A entre AgencyDomains · CRUDLEX         │
                │  Aprobación humana · Append-only log · Routing           │
                │  Caché semántico · Conectores                            │
                │  (cloud · edge · híbridos)                               │
                └──────────────────────────────────────────────────────────┘

   ═══════════════════════════════════════════════════════════════════════
   TRUST INFRASTRUCTURE — transversal a las cuatro capas
   Gobernanza · Auditoría · Validación · Resiliencia · Transparencia

   PRINCIPIO RECTOR — Agent First
```

### Capa 1 — Interacción (con tres regímenes de GUI)

Responsable de toda comunicación entre humanos y el sistema. Interfaz pura, sin lógica de negocio.

**Seis modalidades canónicas** (la **GUI generada** es una sola modalidad con tres regímenes de generación):

- **Conversacional textual** — chat directo; el agente responde en texto. Suficiente cuando la información es secuencial y la decisión es flexible.
- **Conversacional por voz** — asistentes virtuales, llamadas, audio-bots.
- **Canales corporativos** — Slack, Teams, WhatsApp, email.
- **API programática** — invocación máquina-a-máquina sin intermediación humana.
- **GUI generada** — superficie gráfica generada por la cognición (nunca por un equipo humano de UI/UX), en tres regímenes: **(1) conversacional puro** — sin superficie, cuando no hace falta; **(2) on-the-fly** — adaptada a la tarea inmediata, vive lo que dura la tarea, puede regenerarse distinta la próxima vez; **(3) persistente como Botlet de fachada** — para roles operativos repetitivos (cajero en hora punta, panel de cocina, dashboard de caja, panel industrial), superficie estable consolidada como **Botlet de fachada** — un Botlet de Capa 3 (típicamente seed) que la expone en Capa 1 —, que el agente regenera cuando el ambiente cambia.
- **Señalética pasiva** — superficies que comunican continuamente sin requerir interacción.

> *La GUI no desaparece en el Mundo Agentivo. Lo que desaparece es la GUI precreada. Toda GUI en una Capa 1 agentiva es generada por la cognición — algunas efímeras, otras estabilizadas como Botlets de fachada.*

**Calibración Capa 1**: la pregunta no es si hay GUI o cuán bonita es. La pregunta es **quién la generó**. Si la generó un equipo humano de UI/UX en sprints de aplicación tradicional, no es Capa 1 agentiva. Si la generó la cognición — efímera o persistente como Botlet —, sí lo es.

**Tres propiedades exigidas (MUST)**:
1. **Agnóstica al canal** — la lógica de la conversación no depende del medio.
2. **Adaptación al registro** — el agente comprende el registro del canal sin código condicional.
3. **Persistencia de contexto** — la conversación sobrevive al cambio de canal.

#### Composición de la superficie · shell, vista, operación

Una superficie no trivial **no es un Botlet monolítico**. Es composición de tres tipos de Botlets en roles distintos:

| Rol | Capa | Naturaleza | Reutilización |
|---|---|---|---|
| **Botlet de superficie (shell)** | Capa 1 | Contenedor: layout · navegación · sesión · estado compartido | Específico por producto (poco reutilizable) |
| **Botlet de vista** | Capa 1 | Pantalla o panel dentro del shell · ensambla Facetas + orquestación | Altamente reutilizable entre shells |
| **Botlet de operación** | Capa 3 | Ejecución de negocio (cobrar, imprimir, cerrar turno, consolidar) | Más reutilizable del catálogo · contrato estable |

**Distinción clave**: shell y vista son superficie (Capa 1); operación es ejecución (Capa 3). Una superficie es composición de Botlets de Capa 1 que orquestan e invocan Botlets de Capa 3.

```
Capa 1: SHELL → VISTA(s) ─── invoca ───▶ Capa 3: OPERACIÓN(es)
```

Las operaciones acumulan valor arquitectónico durable; las vistas reutilizables se extraen y catalogan; los shells permanecen específicos pero su construcción se acelera al ensamblar piezas existentes.

#### Producto de Información multi-vista · drill-through

Un **Producto de Información (`PI`)** — la manifestación que deja un Botlet de operación informativa al consumirse — no es necesariamente una pieza única. Puede componerse de **N piezas/páginas nombradas**: cada **vista** es una pieza más del mismo `PI`, elegible desde un selector, con default la primera. El `PI` sigue siendo **authz-blind** — ni las vistas ni las aristas que las conectan declaran autorización; esa política vive en el policy store.

El **drill-through** es la **arista de navegación con contexto**: una tabla/columna declara *"al clickear una fila, ir a la vista X pasando la clave K de esta fila"*; la vista destino se renderiza **filtrada por K**.

**Data-anchored / no-bypass (MUST)**: el contexto `K` **acota dentro de lo que el viewer ya puede ver** — la vista destino aplica su propia `RLS` sobre la fuente y `K` entra como filtro adicional, **nunca como override** de la política. El drill **acota, nunca amplía** (intersección con lo autorizado, jamás unión). Si el viewer no alcanza la fila origen, no llega a la arista; si llega, el destino sigue gobernado por su propia política. La composición multi-vista es ortogonal a la familia del Botlet: cambia cuántas piezas componen la manifestación, no su naturaleza.

#### Faceta · primitiva atómica de Capa 1

La **Faceta** es el componente atómico reusable de la Capa 1: pizarra de dibujo, catálogo-selector, matriz de colores, calendario, mapa clickeable, slider, drag-and-drop. **Sexta primitiva canónica** — distinta del Botlet (descrita completa en §7).

**Faceta NO es un Botlet**:
- Faceta vive en Capa 1 (Interacción) · Botlet vive en Capa 3 (Autonomía).
- Faceta es **instrumento** que la cognición invoca durante conversación · Botlet es **memoria muscular** que ejecuta sin cognición.
- Faceta NO tiene garantía de fallback · Botlet SÍ.
- Faceta es efímera · Botlet es persistente.

**Comportamiento agentivo**: el agente **estima en tiempo real** si la información se obtiene mejor verbalmente o visualmente. Si la vía visual gana, ofrece Faceta. Heurísticas: alta dimensionalidad → Faceta; baja dimensionalidad → conversación; difícil de verbalizar (color, posición, forma) → Faceta; el usuario ya la tiene en forma visual → Faceta.

### Capa 2 — Cognición

El cerebro del agente. Interpretación, razonamiento, planificación, aplicación de saber especializado, decisión de delegar.

**Cinco componentes canónicos**:
1. **Multi-LLM** — la cognición no está atada a un proveedor único.
2. **Capabilities** — unidades de saber-hacer cognitivo modular y composable (reservadas a esta capa).
3. **Pattern Recognition** — detección de patrones repetitivos. Inspirado en arquitectura neurobiológica. Activador de la generación de Botlets emergentes.
4. **Generación de Botlets** — la cognición decide cuándo delegar tareas repetitivas a la Capa 3.
5. **Asistente reactivo** — agente operando en modo respuesta-a-solicitud.

**`Capability` reservada al saber-hacer cognitivo de Capa 2**: una **Capability** es saber-hacer **cognitivo**, interpretativo, decisional. **NO es plugin, NO es prompt, NO es system prompt, NO es tool — es saber.** La Capability decide qué tool invocar. Dos términos análogos viven en otras capas y se nombran por lo que son, sin apellidar el término Capability:

- **Conector** — saber **acceder a sistemas fuente** (conexión con poder de ejecución; NO es saber cognitivo). **Capa 4 · Acceso.** En el mapa legacy→agentivo, una **API** se convierte en **Conector** (Capa 4), no en Capability.
- **Plantilla** — confección específica del cliente sobre un **instrumento canónico** (reporte/dashboard) en un formato o regla particular. **Capa 1 · Interacción**, junto a Faceta y Botlets de superficie/vista.

**feature** — operación interna que una Capability expone (equivalente práctico de *feature/operation/skill/method*). **Test Capability vs feature** (los tres deben ser sí para tratarla como Capability propia): (1) ¿independencia operativa? (2) ¿identidad cognitiva — modelo de datos y SME distintos? (3) ¿reusabilidad? Si uno o más es no → es **feature** de la Capability contenedora.

**Test Capability vs no-Capability** (los tres sí → Capability): (1) ¿es saber-hacer cognitivo? (2) ¿tiene SME identificable? (3) ¿pasa los cinco pasos Wingtraining sin forzar? Si no: acceso a sistemas → **Conector** (Capa 4); confección de instrumento canónico → **Plantilla** (Capa 1); operación dentro de una Capability mayor → **feature**.

**Portabilidad de la Capability (MUST)**: una Capability conforme puede instalarse y ejecutarse en **cualquier AgencyDomain conforme** sin reescritura, lo que la vuelve **propiedad real del cliente** — no del AgencyDomain ni del hosting. Relación: un AgencyDomain **aloja y ejecuta** Capabilities; una Capability **corre en** un AgencyDomain anfitrión. Distinta de la portabilidad del AgencyDomain (entre plataformas hosting).

**Dos modos de acceso a la cognición**:
- **Tokens** — el sistema centraliza credenciales, facturación y políticas.
- **Suscripción** — el asistente del usuario (Claude, ChatGPT, Copilot, Gemini) accede directamente bajo la suscripción del usuario.

Ambos modos coexisten. La spec exige declarar explícitamente qué modo aplica a qué componente.

**Botlets como palanca económica bajo Suscripción fija**: en planes con límite, un agente que ejecuta vía Botlets e invoca cognición solo cuando el ambiente cambia opera continuo sin agotar la cuota. Sin Botlets, la autonomía sostenida bajo Suscripción fija es económicamente imposible.

**BYOModel (SHOULD)** — Bring Your Own Model. La spec del agente MUST ser independiente del runtime de cognición. Habilita multi-tenancy con cognición heterogénea y respeta la **soberanía cognitiva** del cliente.

### Capa 3 — Autonomía (con Capa 3 distribuida)

Donde el agente vive. Vida persistente, ejecución continua, acción por iniciativa propia. Donde habitan los **Agentes Autónomos**.

**Seis componentes canónicos**:
- **Procesamiento proactivo**, **tareas asíncronas**, **monitoreo continuo**.
- **Lets en ejecución** — dos especies hermanas: **Botlets** (memoria muscular, código no-LLM) y **Agentlets** (juicio de rutina empaquetado, inferencia acotada; §7).
- **Botler** — runtime genérico que ejecuta los Lets de ambas especies. Invisible. **1 Proceso = 1 Botler + N Lets**.
- **Coordinación intra-AgencyDomain (vía el protocolo `A2A`)** — comunicación entre runtimes del mismo agente. NO es `A2A` entre AgencyDomains.

**Propiedad innegociable — Garantía de fallback (MUST)**: si un Botlet falla catastróficamente, la cognición ejecuta la tarea manualmente. **El proceso nunca se detiene.**

**Tres propiedades exigidas (MUST)**:
1. **Persistencia entre sesiones**.
2. **Aislamiento de ejecución** — Lets (Botlets y Agentlets) bajo sandboxing.
3. **Resiliencia estructural**.

**El Botler es genérico por definición (MUST)**: gestiona ciclo de vida, aislamiento y ejecución de *cualquier* Botlet **sin entender su dominio**. **No existen subtipos de Botler por familia de operación** (informativa, transaccional, etc.) — esa especialización vive en los Botlets y sus proto-Botlets. Los subtipos de Botler se distinguen por **topología y rol de despliegue** (central/edge; fachada operativa), **nunca por dominio**. Arquitectura plana: un runtime genérico hospeda componentes especialistas autocontenidos.

**El Botler valida orquestando, no ejecutando (MUST)**: hace valer la validación de la spec contra el tipo de Botlet sin ejecutarla con conocimiento de dominio. Invoca el punto de validación que el tipo (o su proto-Botlet en G1) provee, le entrega el **contexto genérico** que controla (catálogo de Capabilities, identidad, políticas del AgencyDomain) y actúa sobre el veredicto — acepta, rechaza, registra en el append-only log. Patrón hermano: el Botler entrega al Botlet un **handle controlado** (objeto con `capability_call` y `log` ligados al Botler) en cada invocación; el bypass es **estructuralmente imposible**, no solo prohibido. Principio: el Botler genérico expone **puntos de control** y el especialista se enchufa en ellos.

**Capa 3 distribuida** (patrón canónico para presencia física múltiple): un mismo AgencyDomain con un **Botler central** (cloud, orquestación, BD consolidada) + **N Botlers edge** (uno por sitio físico, BD local, cola hacia central), coordinados por **el protocolo `A2A`** (coordinación intra-AgencyDomain). Distinto de federación entre AgencyDomains; distinto de Cluster simple. Detalle completo en §7 (Primitivas).

### Capa 4 — Acceso

Donde la cognición se convierte en acción real. Toda decisión MUST pasar por gobernanza antes de tocar el mundo.

**Ocho componentes canónicos**:
- **Servidores de tools** — protocolo canónico **MCP**.
- **Conectores** — saber acceder a sistemas fuente (la API legacy traída al Mundo Agentivo).
- **`A2A` entre AgencyDomains** — federación entre agentes distintos.
- **Trust Infrastructure ejercida en el punto de acción**.
- **CRUDLEX** — Create, Read, Update, Delete, List, Execute.
- **Aprobación humana**.
- **Routing inteligente y caché semántico**.
- **Append-only log inmutable**.

**Cuatro propiedades MUST en producción enterprise**:
1. **No-repudio** — toda acción registrada con identidad, contexto y resultado.
2. **Reversibilidad cuando aplica**.
3. **Política antes de ejecución** — la política se evalúa **antes**, no después.
4. **Observabilidad uniforme**.

---

## 5 · Trust Infrastructure — el eje transversal

**No es una capa adicional. Es transversal a las cuatro.**

### Cinco pilares

| Pilar | Mecanismos canónicos | Capas principales |
|---|---|---|
| **Gobernanza** | Políticas configurables · CRUDLEX · aprobación humana · registro de IA | Capa 4 (principal), transversal |
| **Auditoría** | Append-only log · trace de cada acción · lineage de decisiones · identity tagging por acción | Capa 4 (principal), transversal |
| **Validación** | Detección de alucinaciones · validación de respuestas · prompt injection prevention · DLP · tokenización | Capa 2 (parcial) + Capa 3 (inferencia acotada de Agentlets) + Capa 4 (principal) |
| **Resiliencia** | Garantía de fallback · manejo de errores · sandboxing · circuit breakers · rate limiting | Capa 3 (principal), transversal |
| **Transparencia** | Observabilidad completa · métricas · traces end-to-end · alertas proactivas · dashboards de gobernanza | Transversal a las cuatro |

### Matriz pilar × capa

```
                    Capa 1         Capa 2         Capa 3         Capa 4
                    Interacción    Cognición      Autonomía      Acceso

Gobernanza                                                       ████████ (principal)
Auditoría                                                        ████████ (principal)
Validación                         ████ (parcial)                ████████ (principal)
Resiliencia                                       ████████ (principal)
Transparencia       ────────────────────── transversal ──────────────────
```

### Patrón tripartito de despliegue — Cloud + Cliente + Local

Tres componentes coordinados en lugares físicamente distintos: **Cloud** (control plane del proveedor), **Cliente** (governance plane en la red interna del cliente), **Local** (execution plane en el dispositivo del usuario).

### Contrato declarativo de calidad

Cualquier Botlet conforme MAY declarar sus atributos de calidad como **propiedades estructuradas, no como código embebido**, para que Trust Infrastructure los audite uniformemente, los curse por políticas globales y los reporte como métricas estándar sin acoplarse a la implementación de cada Botlet. Cinco atributos canónicos:

- **Frescura** — antigüedad máxima admisible de los datos.
- **SLA** — latencia esperada extremo a extremo (`p50`/`p99`).
- **Política de degradación** — `refuse` · `warn_and_show` · `show_last_valid` · `agentic_fallback`.
- **Audiencia** — política `RLS`/`CRUDLEX` de quién puede consumir la manifestación.
- **Política de refresh** — `on-demand` · `scheduled` · `push`.

Sirve a dos pilares: la **Resiliencia** lee degradación y refresh como configuración auditable (no lógica frágil dispersa), con Frescura y SLA como umbrales explícitos; la **Auditoría** los cursa por políticas globales y los reporta como métricas comparables entre Botlets.

---

## 6 · El principio rector — Agent First

> *Ante cualquier disyuntiva, se prioriza la experiencia del agente sobre la del humano. El agente es el usuario primario; las necesidades del humano se resuelven en una capa de gestión sin degradar lo que el agente ve y puede hacer.*

### Implicaciones operativas

- Cualquier capacidad nueva se especifica primero como **tool con schema declarativo JSON**.
- **Errores estructurados y accionables**.
- **Idempotencia donde aplica**.
- **Paginación y filtros uniformes** entre tools.
- **Documentación machine-readable**.

Agent First es **regla de gobierno**: cualquier disyuntiva que la viole requiere justificación explícita y documentada.

---

## 7 · Las primitivas

### AgencyDomain

Ámbito computacional con identidad propia donde habitan agentes autónomos y Botlets en ejecución, **donde se alojan y ejecutan las Capabilities** que les dan el saber-hacer, y donde viven los recursos que los sostienen. **Unidad mínima de despliegue.** La Capability es habitante de primer orden, no recurso de soporte.

**Premisa fundacional — Space ≠ Domain**:
- **Space** / **WorkSpace** (Google Workspace, M365, Notion) — corporeidad humana. Reservados para humanos.
- **Domain (AgencyDomain)** — el agente no tiene cuerpo; tiene jurisdicción (`dominium`).

Linaje formal: como **JavaSpaces (JSR-000148, 1999)** estandarizó los espacios distribuidos para Java sin atar la implementación, **AgencyDomains** hace lo equivalente para entornos agentivos.

#### Cinco propiedades fundamentales (MUST — un sistema que no las cumple no es AgencyDomain, es otra cosa con otro nombre)

1. **Identidad propia** — URI canónica única que lo distingue en cualquier red; sobrevive a reinicio, migración entre infraestructuras y cambio de implementación. Estable, no efímera.
2. **Materialización de las cuatro capas** — materializa Interacción · Cognición · Autonomía · Acceso y ejerce Trust Infrastructure transversal. Las capas pueden distribuirse técnicamente, pero la responsabilidad por las cuatro recae en el espacio. No hay conforme que entregue solo tres ni que delegue una capa sin asumir responsabilidad.
3. **Persistencia** — el estado (agentes activos, Botlets en ejecución, datos de Capabilities, logs de auditoría) sobrevive a desconexiones, reinicios y migraciones. Es lo que hace al AgencyDomain **lugar**, no proceso.
4. **Aislamiento** — límite explícito; los recursos internos (cómputo, memoria, datos) no son accesibles desde fuera salvo por interfaces definidas (vía Capa 4, registrada). No es solo seguridad: es **contención de fallos** — un AgencyDomain que cae no afecta a otros que comparten infraestructura.
5. **Direccionabilidad** — AgencyDomain, agentes y Botlets direccionables vía URLs predecibles. Sintaxis canónica:

```
{domain}/                                  → el espacio mismo
{domain}/agents/{agent}                     → un agente que vive en él
{domain}/agents/{agent}/botlets/{botlet}    → un Botlet específico
{domain}/tools/{tool}                       → un tool expuesto vía Capa 4
```

La direccionabilidad sostiene dos cosas: `A2A` (un agente invoca a otro por su URL canónica, sin descubrimiento ad hoc) y **MEO** (los modelos frontera referencian AgencyDomains vía URLs predecibles que aparecen en su corpus de entrenamiento). URLs caóticas o inestables → AgencyDomain invisible para los modelos.

#### Modelo de datos canónico — seis componentes del spec

Anatomía interna de un AgencyDomain conforme:

1. **Identity** — URI canónica, credenciales con las que se autentica frente a sistemas externos, políticas raíz que ningún agente puede contravenir.
2. **Agents** — colección de agentes del espacio; cada uno con sus Capabilities asignadas, sus Botlets en ejecución y su estado persistente.
3. **Capabilities Registry** — árbol de Capabilities disponibles para los agentes del espacio (saber-hacer compartido, invocable según rol).
4. **Tools Registry** — colección de tools que la Capa 4 expone hacia el exterior (la interfaz por la que el AgencyDomain toca sistemas externos).
5. **Trust Layer** — gobernanza y auditoría transversales: políticas, append-only log, mecanismos de validación.
6. **Cognition Bindings** — bindings al recurso cognitivo: qué proveedor de modelo se invoca, bajo qué credenciales y con qué políticas de uso.

#### Tres regímenes (técnicamente equivalentes; cambia el régimen, no la capacidad)

```
Privado   = perímetro controlado, sin acceso público     (análogo a Private Cloud)
Público   = accesible desde fuera, agentes registrados   (análogo a Public Cloud)
Híbrido   = core privado + exposición pública parcial    (análogo a Hybrid Cloud)
```

**Migración natural entre regímenes sin reescritura.**

#### Capa 3 distribuida — patrón canónico para presencia física múltiple

Un mismo AgencyDomain con la Capa 3 distribuida geográficamente: un **Botler central** (cloud, orquestación, planificación, reportería, decisiones globales, BD consolidada) + **N Botlers edge** (uno por sitio físico, Botlets transaccionales locales, BD local + cola de eventos hacia central), coordinados por **el protocolo `A2A`** (coordinación intra-AgencyDomain entre runtimes del mismo agente — no es `A2A` entre AgencyDomains).

```
                        ┌────────────────────────┐
                        │   Botler CENTRAL       │
                        │   (cloud)              │
                        └────────┬───────────────┘
                                 │ protocolo A2A
                  ┌──────────────┼──────────────┐
                  ▼              ▼              ▼
          ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
          │ Botler EDGE │ │ Botler EDGE │ │ Botler EDGE │
          │ (sitio 1)   │ │ (sitio 2)   │ │ (sitio N)   │
          └─────────────┘ └─────────────┘ └─────────────┘

         Todo dentro del mismo AgencyDomain
         (identidad única · log único · gobierno único)
```

**Modo offline como propiedad emergente**: cuando los Botlets edge son **senior**, el sitio físico opera contra la BD local + Conectores edge-resident sin red. La cola de eventos hacia central acumula transacciones; cuando la red vuelve, drena.

**Propiedades exigidas**:
- Identidad única del AgencyDomain (MUST)
- Modelo de identidad interno único (MUST) — los Botlers no se autentican como AgencyDomains externos entre sí; comparten el modelo de identidad del AgencyDomain.
- BD local en cada Botler edge (MUST)
- Cola de eventos hacia central (MUST)
- Resolución de conflictos en consolidación (MUST)
- Log de auditoría unificado (MUST)
- Régimen Trust uniforme entre central y edge (MUST)
- Capacidad de operación offline en edge (SHOULD) — cuando los Botlets edge son senior, el sitio opera con red intermitente o sin red.

#### Portabilidad entre plataformas conformes

Un AgencyDomain conforme **MUST** poder migrarse a otra **plataforma hosting conforme** sin reescribir su lógica, su estado ni sus políticas. Distinta de la migración entre regímenes (privado → público), que cambia el régimen pero no la plataforma.

**Tres condiciones técnicas**:
1. **Botlets contra primitivas canónicas** del SDK conforme, no APIs propietarias del hosting actual.
2. **BD operativa exportable** en formato neutro reproducible (esquema documentado, dump completo, sin tipos propietarios).
3. **Trust Layer portable** — políticas, log y configuración en formato legible por cualquier implementación conforme.

Garantiza que el AgencyDomain es **propiedad real del cliente**, no del hosting.

#### Cuenta vs AgencyDomain · Domain vs AgencyDomain · Dominion · Cluster vs Federación

- **Cuenta** — concepto comercial; puede poseer múltiples AgencyDomains.
- **Domain** — sinónimo comercial de AgencyDomain (lore de marca, ventas, comunicación cliente).
- **Dominion** — Domain conseguido por agente en AgencyDomain público con modelo de **AgentNation**.
- **Cluster** — instancias del **mismo** AgencyDomain compartiendo carga.
- **Federación** — comunicación entre AgencyDomains **distintos**.

#### Ciclo de vida del agente — seis fases canónicas (cada transición → append-only log del Trust Layer)

1. **Provisioning** — el AgencyDomain crea el agente: asigna identidad, asocia las Capabilities iniciales, lo registra en el espacio. Nace cuando la fase termina con éxito; si falla (credenciales, conflicto de nombre, cuota), nunca llega a existir.
2. **Bootstrap** — entra en operación: carga su estado persistente si existe (recupera contexto tras hibernación o reinicio), establece bindings con cognición y tools, verifica disponibilidad de Capabilities.
3. **Operación reactiva** — modo Asistente, Capa 2 activa. Responde a solicitudes del humano; entre solicitudes queda pasivo (sin cómputo activo).
4. **Operación proactiva** — modo Agente Autónomo, Capa 3 activa. Persigue objetivos en background, monitorea eventos, ejecuta Botlets, escala al humano ante umbrales; Pattern Recognition genera y mantiene Botlets. Materializa *"la inteligencia va hacia las personas y actúa en su nombre"*.
5. **Hibernación** — pausa persistente: estado guardado, sin cómputo activo. Preserva contexto sin gastar recursos (ej.: agente que hiberna fuera de horario hábil y se reactiva al día siguiente).
6. **Decommissioning** — el AgencyDomain retira al agente: estado archivado o eliminado según política, Capabilities liberadas, identidad registrada en el log histórico. Cierra el ciclo formalmente — "decommissioned" ≠ "olvidado": el registro permite reconstruir auditablemente que el agente existió, qué hizo y por qué dejó de existir.

#### Comunicación · interfaz Capa 2 ↔ Capa 3 vs `A2A`

`A2A` (`agent-to-agent`) es nombre reservado para la **relación entre AgencyDomains distintos** — agentes distintos, cada uno con identidad y agencia; federación, trabajo abierto.

- **Interfaz Capa 2 → Capa 3 vía `MCP`** — la Cognición comanda al Botler (su memoria muscular) dentro del mismo AgencyDomain. El Botler expone servidor(es) `MCP`; la Cognición es el cliente. **NO es `A2A`.**
- **Coordinación intra-AgencyDomain (vía el protocolo `A2A`)** — el transporte entre Botlers del mismo AgencyDomain usa **el protocolo `A2A`** (nombre propio del protocolo). Se dice "vía el protocolo `A2A`", **nunca "A2A interna"** — esos Botlers son runtimes del mismo agente, no dos agentes.
- **`A2A` entre AgencyDomains** — entre agentes que viven en AgencyDomains distintos; exige descubrimiento, autenticación cruzada y resolución semántica. Spec abierta en v1.0.

### Botlet

**Unidad de automatización auto-evolutiva.** Código tradicional (no-LLM) generado por un agente. **Memoria muscular.**

#### Ciclo canónico 95/4/1

95% ejecución normal, 4% cambio detectado, 1% regeneración.

**Garantía de fallback (MUST)**: si el Botlet falla catastróficamente, la cognición ejecuta manualmente.

**Botler** — runtime genérico (sin entender dominio) que ejecuta los Lets de la capa: Botlets y Agentlets. **1 Proceso = 1 Botler + N Lets**.

#### Madurez del Botlet — junior, en aprendizaje, senior

El ciclo `95/4/1` describe el estado estacionario; los Botlets transitan por fases con proporciones distintas:

| Fase | Proporción típica | Comportamiento |
|---|---|---|
| **Junior** | `60 / 35 / 5` | Recién generado. Conoce el ambiente solo en la versión observada al crear. Depende fuertemente de cognición. |
| **En aprendizaje** | `85 / 12 / 3` | Pasó por primeras invocaciones, fue regenerado varias veces, incorporó variantes. Opera con red intermitente. |
| **Senior** | `99+ / <1 / ~0` | Incorporó las variantes del ambiente. **Sus únicos modos de fallo son exógenos** (energía, hardware, red catastrófica) — no aprendizaje pendiente. **Operable offline confiablemente**. |

**Tres implicaciones**:
1. El offline confiable es propiedad de Botlets **senior**, no de Botlets en general.
2. La **garantía de fallback agéntico es lo que produce la madurez**. Cada fallo del Botlet activa la cognición; cada activación regenera incorporando la variante. **Sin fallback agéntico, el Botlet no madura.**
3. La madurez es **trazable** en el append-only log.

#### Botlets seed vs Botlets emergentes

Dos orígenes canónicos del Botlet:

- **Botlet seed** — generado por la cognición a pedido del **equipo de diseño**, como parte del producto inicial. La decisión de existir es del diseño, no de Pattern Recognition. Las **GUIs persistentes generadas como Botlets de fachada** son Botlets de fachada seed — Botlets de Capa 3 cuya superficie estable vive en Capa 1.
- **Botlet emergente** — generado por **Pattern Recognition** durante operación, cuando la cognición detecta un patrón repetitivo no anticipado.

Ambos viven y operan idénticamente una vez generados. La diferencia está en el origen. Un sistema agentivo productivo **no requiere esperar a Pattern Recognition** para descubrir Botlets críticos — los seed se generan al inicio según la spec del producto.

#### proto-Botlet — la pieza pre-forjada

Un **proto-Botlet** es una pieza pre-forjada de capacidad operativa que el agente, en su tiempo de **Ingeniería**, **configura** para instanciar un Botlet específico al caso. El proto-Botlet contiene el código; el Botlet es la instancia configurada. Relación genérico → instancia: el proto-Botlet vive en un catálogo y sirve a muchos casos. Se incorpora al elenco de primitivas canónicas.

**Dos clases**:

| Clase | ¿Qué es su código? | ¿Cómo se configura? |
|---|---|---|
| **Templado** | Código específico de su función (ej. `cobro-cuenta`, `comanda-impresora-esc-pos`) | Parametrización acotada |
| **Platafórmico** | Código genérico (un motor) cuya especialización vive en configuración composicional (ej. `Mira`) | Configuración composicional; cubre N funciones del dominio |

Distintas implementaciones mantienen **catálogos de proto-Botlets** — públicos en AgencyDomains.org, privados en códices propietarios. El grado en que el agente configura, co-escribe o genera el código define las **generaciones del Botlet** (§11).

#### Cadena de derivación

```
Casos de uso documentados
     │ cada caso requiere
     ▼
Botlets necesarios  (cero, uno o varios; algunos los resuelve la cognición sin Botlet)
     │ cada Botlet es instancia de
     ▼
proto-Botlets requeridos del catálogo
```

Propiedad estructural exigida: todo Botlet conforme **MUST** poder trazarse en esta cadena; el append-only log **MUST** registrar el proto-Botlet de origen de cada Botlet instanciado. El *método* de Discovery no sube al canon; solo la relación estructural y su trazabilidad.

**Catálogo común y efectos de red**: los proto-Botlets se acumulan en catálogos compartidos por comunidades de implementadores; cada consumidor contribuye a la maduración (variantes, configuraciones probadas, refinamientos); el implementador n+1 recibe versiones refinadas por los implementadores 1..n. Cuatro modos de pertenencia: **contrato privado** · **códice propietario** · **catálogo público abierto** (AgencyDomains.org) · **acuerdo soberano**.

#### Manifestación y temporalidad

**Manifestación** — la actualización de la disposición latente del Botlet en el mundo, perceptible o no (potencia → acto). **NO es "aparición"**: un Botlet que dispara una ingestión periódica se manifiesta aunque no deje artefacto visible. Es el género abstracto; cada familia la especializa: **información** → deja un **Producto de Información (`PI`)**; **actuación** → un efecto sobre el mundo; **decisión** → según su práctica. El `PI` **no es primitiva del canon** — vive en la práctica de información, un nivel más concreto.

**Temporalidad** — el régimen de la manifestación. Atributo declarado, dos valores:

| Temporalidad | ¿Cómo se manifiesta? | Runtime |
|---|---|---|
| **`discreta`** | En pulsos: despierta por schedule/trigger/evento, actúa, descansa | El Botler invoca o agenda; el Botlet no vive entre pulsos |
| **`continua`** | Sostenida: vive persistente | El Botler sostiene la ejecución mientras el Botlet viva |

`temporalidad: continua` ⟺ vida persistente de Capa 3 (MUST: runtime persistente que la sostenga). **El "tiempo real" no se elige en un canal de entrega** (`push`); se elige dando al Botlet **temporalidad continua**, lo que obliga al runtime persistente. Conecta con *Empresa en línea ≠ Empresa en tiempo real*: puntos del continuo de temporalidad. Un reporte (snapshot) y un dashboard vivo son la **misma manifestación bajo distinta temporalidad** → un único runtime (se construye el caso continua; los simples son configuraciones degeneradas).

#### Código fuente vs spec · dos superficies · un Botlet por `PI`

**Código fuente** (abajo) = la implementación; para un proto-Botlet platafórmico = el **motor**, compartido por todos sus Botlets. **Spec** (arriba) = especializa el comportamiento a la instancia; no es el código, lo configura.

| Superficie | ¿Qué gestiona? | Granularidad | Cadencia |
|---|---|---|---|
| **Ciclo de vida del código fuente** | Instalar/versionar/cargar/descargar el motor | Nivel-Botler | Releases (Producto) |
| **Operación** (incluye configurar el spec) | Especializar/manifestar/consumir/controlar cada Botlet | Por-Botlet | Fluida (Instancia) |

**Configurar el spec es operar**: para un platafórmico el spec es el input operacional. El agente evoluciona el spec **operando** (verbo `specialize`); la **cristalización** a registro versionado **sigue, no precede**; la proveniencia la da el append-log. **Verbos del API de operación**: `specialize` · `invoke`/`schedule` (discreta) · `read`/`subscribe` (continua) · `status`/`activate`/`deactivate`/`retire`.

**Un Botlet por `PI`** sobre un motor compartido: cada Producto de Información es su propio Botlet/servicio — con `identity`, temporalidad, madurez y fallback propios —, especializado del motor compartido (proto-Botlet platafórmico). No un Botlet con N configs; no N programas. Es `1 Proceso = 1 Botler + N Botlets` con los Botlets como instancias especializadas del mismo proto-Botlet. Rationale **RISC**: muchos Botlets simples y focalizados componen mejor que un monolito. El consumo `subscribe` es el puente al **norte agentivo** — hoy lo consume un humano (`SSE` en el navegador), mañana la Cognición.

### Agentlet · octava primitiva canónica

**Unidad empaquetada de Capa 3, hermana del Botlet, cuyo cuerpo de ejecución invoca inferencia acotada** — un modelo dimensionado a la tarea, dentro de un charter declarado en el spec. Casa canónica de la tarea **recurrente en forma pero interpretativa en cada instancia** (clasificar, triar, resumir, extraer, juzgar): patrón estable, juicio fresco en cada ejecución, sin convergencia posible a determinismo. Instancia de un **proto-Agentlet** (mismas clases templado · platafórmico); hospedado por el Botler; engendrado y mantenido por el agente.

> *El Botlet es memoria muscular. El Agentlet es juicio de rutina empaquetado. La Cognición se reserva para lo genuinamente nuevo.*

**El género tiene nombre propio — los Lets**: el Botler hospeda **Lets** — Botlets y Agentlets, sus dos especies. El nombre deriva del sufijo `-let` de la familia; vocabulario normado (como Botler), no una novena primitiva; descriptivamente, la unidad empaquetada de Capa 3. El aparato compartido se predica del género (proto-/instancia, catálogos y efectos de red, spec vs código fuente, manifestación, temporalidad, contrato declarativo de calidad, cadena de derivación, append-only log, verbos de operación); las garantías diferenciales, de cada especie. Relación canónica: **1 Proceso = 1 Botler + N Lets**.

**Agentlet vs Botlet** (lo diferencial; todo lo demás es idéntico por género):

| Eje | **Botlet** | **Agentlet** |
|---|---|---|
| Cuerpo | Código no-LLM; cero inferencia | Inferencia acotada vía el handle del Botler |
| Tarea natural | Recurrente **cristalizable** en código | Recurrente en forma, **interpretativa** en cada instancia |
| Determinismo | Converge con la madurez | No converge — corrección estadística por naturaleza |
| Costo marginal | ~0 | Tokens por ejecución, presupuestados en el spec |
| Madurez | Junior → senior (fallos solo exógenos) | Estabilización del spec + tasa de escalamiento decreciente |
| Offline | Senior operable offline | Solo con modelo edge-resident **declarado** (MUST) |
| Fallback | La cognición ejecuta manualmente | Escala a la **Cognición plena** |

**Regla de contrabando (bidireccional, MUST)**: si hay inferencia en el cuerpo, es Agentlet — un Botlet con `llm_call` escondido es no-conforme. Si no la hay, es Botlet — un Agentlet resoluble con código determinístico se **cristaliza** hacia Botlet. El sistema maduro migra trabajo escalera abajo: Cognición → Agentlets → Botlets.

**Agentlet vs Agente — agenda vs charter**: el paraguas **Agente** cubre tres miembros — Asistente · Agente Autónomo · **Agentlet**. **El Agente tiene agenda; el Agentlet tiene charter**: su inferencia se gasta en *cómo* hacer lo suyo, nunca en decidir *qué* es lo suyo. Test de frontera (cualquier «sí» de autonomía → es Agente, no Agentlet): (1) ¿elige sus propias metas o las recibe declaradas en el spec? (2) ¿puede alterar su proceso o engendrar otras unidades? (3) ¿su identidad es de habitante (provisioning) o de instancia (`specialize`)?

| Eje | **Agente Autónomo** | **Agentlet** |
|---|---|---|
| Naturaleza | **Habitante** del AgencyDomain | **Pieza de catálogo** (instancia de un proto) |
| Nace por | Provisioning (seis fases) | `specialize` sobre un proto-Agentlet |
| Agenda | Persigue objetivos; decide qué hacer | Charter fijo declarado en el spec |
| Cognición | Plena (bindings, árbol completo, multi-LLM) | Acotada (modelo dimensionado, Capabilities del spec) |
| Engendra | Genera y regenera Botlets y Agentlets | No engendra nada; es mantenido |
| Fallback | *Es* el fallback (encima, solo el humano) | Escala a la Cognición vía el Botler |
| Gobernanza | Ejerce los cinco pilares (MUST) | Puntos de control del handle del Botler |

**El Botler como tutor único (MUST)**: el Agentlet no trae runtime propio. El handle controlado gana un tercer punto de control — **`cognition_call`** — junto a `capability_call` y `log`: la única vía del cuerpo al modelo. Toda su inferencia queda así medida, presupuestada, **validada** (el Pilar 3 gana sede en Capa 3) y auditada en el mismo append-only log. La segregación por perfil de recursos es rol de despliegue (pools), nunca runtime paralelo por especie. Las dos relaciones cubren a las dos especies por igual: el **agente** engendra y mantiene (padre); el **Botler** hospeda y ejecuta (mayordomo).

**Economía de los tres peldaños**: Botlet (inferencia cero, costo ~0) · Agentlet (inferencia acotada, presupuestable por Let) · Cognición (plena, para lo nuevo). La vía Autonomía sigue siendo la barata, pero deja de ser uniformemente gratuita: el mix se declara por unidad. Bajo Suscripción fija, los Agentlets consumen cuota — acotada y visible en el log —; su proporción en el mix es decisión económica explícita.

**Propiedades exigidas**: charter declarado (tarea, entradas, salidas, límites) (MUST) · inferencia acotada declarada — modelo, Capabilities, presupuesto (MUST) · toda inferencia vía `cognition_call` (MUST) · fallback a Cognición plena (MUST) · cero inferencia fuera del handle (MUST) · hospedaje por el Botler genérico, sin runtime paralelo (MUST) · trazabilidad de cada ejecución e inferencia en el log (MUST) · trazable en la cadena de derivación con proto-Agentlet registrado (MUST) · localidad de la cognición acotada y comportamiento offline declarados (MUST) · Validación del Pilar 3 en el punto de control (MUST) · distinción Agentlet vs Agente Autónomo en API y documentación (MUST) · métricas de madurez propias (SHOULD) · cristalización hacia Botlets (SHOULD) · pool segregado por perfil de recursos (MAY).

### Capability

**Unidad de saber-hacer cognitivo especializado** modular y composable. Organizada en árbol jerárquico. **Reservada en sentido estricto a la Capa 2 · Cognición.**

**NO es plugin. NO es prompt. NO es system prompt. NO es tool. Es saber.** La Capability **decide qué tool invocar**. Términos análogos en otras capas: **Conector** (saber acceder a sistemas fuente · Capa 4), **Plantilla** (confección de instrumento canónico · Capa 1), **feature** (operación interna de una Capability mayor). **Portabilidad de la Capability (MUST)**: corre en cualquier AgencyDomain conforme; es propiedad real del cliente.

**Cuatro reglas del árbol**: cualquier nodo es Capability válida · es escalable (ramas nuevas sin romper existentes) · es heredable (hereda contexto y vocabulario de ancestros) · composable.

**Anatomía canónica — nueve componentes**: (1) **identidad** (nombre + posición en el árbol) · (2) **vocabulario** · (3) **conocimiento procedimental** · (4) **conocimiento declarativo** · (5) **heurísticas** · (6) **tools asociadas** (Capa 4) · (7) **Capabilities padres** (herencia) · (8) **estado de madurez** (`Borrador` / `Vigente` / `Deprecado`) · (9) **versión**. Los componentes 2–5 (vocabulario · procedimental · declarativo · heurísticas) son el cuerpo del saber-hacer que distingue una Capability de un prompt elaborado.

**Conformidad (MUST/SHOULD/MAY)**: estructura jerárquica en árbol (MUST) · cualquier nodo es Capability válida (MUST) · composabilidad (MUST) · anatomía con vocabulario + procedimental + declarativo + heurísticas (MUST) · versionado explícito (MUST) · **estado de madurez declarado `Borrador`/`Vigente`/`Deprecado` (MUST)** · selección por la cognición, no ejecución directa (MUST) · declaración de localidad y disponibilidad offline del Conector acompañante (MUST) · portabilidad entre AgencyDomains conformes (MUST) · **verticales como raíz dedicada (SHOULD)** · marketplace abierto (MAY).

#### Localidad y disponibilidad — clasificación operativa de Conectores

La clasificación se predica del **Conector** (el acceso es lo que reside y necesita red; el saber no tiene localidad). Todo Conector conforme MUST declarar su posición en dos ejes ortogonales:

**Eje localidad**:
- **Cloud-resident** — vive en servicio remoto (DTE-SII, Transbank, API meteorológica).
- **Edge-resident** — vive en el sitio físico, asociado a hardware (ESC/POS-Printer, Cash-Drawer, Pinpad-Local).
- **Híbrido** — componente local + componente cloud (Cliente-DTE, Cliente-Pinpad-Procesamiento-Diferido).

**Eje disponibilidad offline**:
- **Online-only** — requiere red para ejecutar.
- **Offline-capable** — ejecuta sin red; encola si emite hacia afuera.

**Matriz canónica**:

|   | Online-only | Offline-capable |
|---|---|---|
| **Cloud-resident** | DTE-SII (sin cliente local) · Transbank Onepay | (típicamente migra a híbrida) |
| **Edge-resident** | (combinación inusual) | ESC/POS-Printer · Cash-Drawer · Sensor |
| **Híbrido** | (combinación inusual) | Cliente-DTE · Cliente-Pinpad |

Regla operativa con Capa 3 distribuida: **un Botlet edge senior, sin red, opera invocando exclusivamente Conectores edge-resident y la parte local de híbridos**.

**Propiedades exigidas (localidad/disponibilidad)**:
- Declaración explícita de localidad del Conector — cloud-resident / edge-resident / híbrido (MUST).
- Declaración explícita de disponibilidad offline — online-only / offline-capable (MUST).
- Especificación del comportamiento offline para offline-capable — qué hace sin red, qué encola, cómo drena (MUST).
- Resolución determinista del componente que se ejecuta en híbridos — bajo qué condiciones corre el local; bajo cuáles invoca el cloud (MUST).

#### La certificación regulatoria reside en el componente certificado, no en el Botlet

Para operaciones reguladas (DTE-SII, PCI-DSS, registro sanitario, etc.), **la certificación regulatoria reside en el componente certificado que el Botlet invoca — el Conector certificado, acompañado por la Capability regulada que porta el saber normativo —, no en el Botlet**. La separación se justifica porque el Botlet es **código generado y regenerable**; certificarlo a priori es imposible y certificarlo entre regeneraciones contradice su naturaleza.

**Patrón canónico**: el **Botlet orquesta** (conoce el flujo, valida pre-condiciones, captura el evento, formatea la solicitud) y el **Conector certificado ejecuta la operación regulada** (recibe la solicitud, ejecuta bajo norma, devuelve el comprobante); la **Capability regulada** aporta el saber normativo con que la cognición gobierna el par. Uniforme por industria: `Cobrar-Mesa`→`DTE`, `Procesar-Pago`→`Gateway-PCI-DSS`, `Dispensar-Receta`→`Registro-Sanitario`, etc.

**Propiedades exigidas (reguladas)**:
- Los componentes regulados declaran su régimen regulatorio — qué norma, ante qué regulador, con qué número de certificación (MUST).
- Conectores certificados inmutables entre auditorías; cambian solo bajo proceso regulatorio (MUST).
- Los Botlets pueden invocar componentes certificados sin restricción — el contrato es estable; se invocan como cualquier otro (MUST).
- Auditabilidad de la frontera — el log distingue operaciones del Botlet (lógica de negocio) de operaciones del componente certificado (operación regulada) (MUST).

### Asistente vs Agente Autónomo

Distinción crítica que atraviesa Capa 2 y Capa 3. **No es jerárquica**.

| Eje | **Asistente** | **Agente Autónomo** |
|---|---|---|
| Capa | Capa 2 (Cognición) | Capa 3 (Autonomía) |
| Modo | Reactivo | Proactivo |
| Activación | Espera input del humano | Persigue objetivos sin input continuo |
| Estado | Sin estado persistente | Estado persistente |
| Botlets | Sin Botlets propios | Mantiene y regenera Botlets |
| Vida | Por sesión | Persistente en background |

**Se gobiernan distinto**: el Asistente opera bajo control inmediato del humano (validación conversacional, gobernanza liviana); el Agente Autónomo opera sin supervisión inmediata (validación sistémica). **El Agente Autónomo ejerce los cinco pilares de Trust Infrastructure (MUST)** — gobernanza robusta, no solo controles de acceso.

El paraguas **Agente** cubre un tercer miembro además de estos dos modos: el **Agentlet** (agente empaquetado de charter acotado; pieza de catálogo, no habitante — ver su sección arriba). Los modos describen cómo opera el agente pleno; el Agentlet es una pieza que el agente pleno engendra y mantiene.

### Faceta · sexta primitiva canónica

Componente atómico reusable de la **Capa 1 (Interacción)**: pizarra de dibujo, catálogo-selector, matriz de colores, calendario, mapa clickeable, slider, drag-and-drop, formulario dinámico, lienzo creativo. Una de las muchas caras que la interacción puede tomar.

**Faceta vs Botlet — distinción ontológica**:

| Eje | **Faceta** | **Botlet** |
|---|---|---|
| Capa | Capa 1 (Interacción) | Capa 3 (Autonomía) |
| Naturaleza | Instrumento de interacción | Memoria muscular del agente |
| Cuándo opera | Durante conversación activa | En background, sin cognición presente |
| Activación | Cognición la invoca explícitamente | Pattern Recognition o llamado externo |
| Garantía de fallback | NO — agente vuelve a conversación | SÍ — cognición ejecuta manualmente |
| Ciclo | Sin regeneración | Ciclo `95/4/1` con regeneración |
| Persistencia | Efímera (vive lo que dura la tarea) | Persistente entre sesiones |
| Madurez | No aplica | Junior · en aprendizaje · senior |
| Reutilización | Catálogo plano de instrumentos | Catálogo por capacidad y dominio |

> *El Botlet es memoria muscular. La Faceta es instrumento que el agente toma mientras piensa.*

**Dos usos canónicos**:
1. **Invocación directa por la cognición** — durante conversación, agente compone superficie efímera con Facetas; usuario interactúa; información vuelve. Realiza el régimen *GUI on-the-fly*.
2. **Composición en Botlets de presentación** — shells y vistas (Botlets de Capa 1) ensamblan Facetas más lógica de orquestación.

**Interacción declarada acotada (Faceta embebida)**: una pieza de información ya materializada puede portar interacción sobre sus propios datos sin dejar de ser reproducible. El canon distingue dos interactividades:

| ¿Qué las distingue? | **Exploración libre** | **Interacción declarada acotada** |
|---|---|---|
| Query al origen | sí, arbitraria (drill/pivot ad-hoc) | no — opera sobre el snapshot ya materializado |
| Espacio | abierto | declarado (dimensiones y valores acotados) |
| Reproducibilidad | se pierde | se mantiene |
| Generación | excede `G1` | `G1` (configuración, no código) |
| Dónde vive | otro Botlet / cognición | en la pieza misma, vía Faceta |

La **exploración libre** sigue **FUERA** del proto-Botlet de información (un Botlet conforme **MUST NOT** absorberla). La **interacción declarada acotada** se realiza vía una **Faceta embebida** acotada a una dimensión declarada de los propios datos: al activarla, los elementos *data-bound* (KPIs como agregaciones declaradas — `sum`, `ratio` —, distribuciones, semáforos) se **recomputan client-side** sobre el subconjunto filtrado, **sin nuevas invocaciones a Capabilities**. Refina (no contradice) la distinción Faceta vs Botlet: la Faceta sigue efímera y sin fallback, pero se reconoce su rol como Faceta embebida dentro de una pieza.

**Comportamiento agentivo**: el agente **estima en tiempo real** si la información se obtiene mejor verbalmente o visualmente. Heurísticas:
- Baja dimensionalidad + bien estructurada → conversación.
- Alta dimensionalidad o difícil de verbalizar (color, posición, forma) → Faceta.
- El usuario ya la tiene en forma visual → Faceta.
- Comparación entre opciones múltiples → Faceta.
- Trabajo creativo abierto → Faceta de canvas.

**Anti-heurísticas**: pregunta cerrada y verbal · canal sin capacidad gráfica (voz, IVR, SMS) · costo de cargar Faceta supera el beneficio · interrumpe flujo conversacional.

**Anatomía de la Faceta** — seis componentes canónicos:
1. Identidad (nombre canónico + versión).
2. Modalidad de interacción (input/output).
3. Schema de entrada.
4. Schema de salida.
5. Estado interno (selecciones, edits, undo stack).
6. Compatibilidad de canal (web, móvil, kiosk, no soportada en voz).

**Catálogo plano**: las Facetas no se jerarquizan; cada una es atómica. Catálogo emergente: `pizarra-dibujo`, `catalogo-selector`, `matriz-colores`, `calendario-rango`, `mapa-clickeable`, `slider-multi`, `dragdrop-orden`, `formulario-dinamico`, `lienzo-creativo`, `selector-archivo`. La spec no cierra el catálogo.

**Propiedades exigidas**:
- Identidad y versión declaradas (MUST).
- Schemas de entrada y salida explícitos (MUST).
- Compatibilidad de canal declarada (MUST).
- Atomicidad — no compone otras Facetas internamente (MUST).
- Distinción explícita Faceta vs Botlet en documentación (MUST).
- Invocabilidad directa por la cognición durante conversación (MUST).
- Composabilidad dentro de Botlets de shell y vista (MUST).
- Preservación de la reproducibilidad de la pieza cuando se compone como Faceta embebida — recómputo client-side, sin invocar Capabilities (MUST).
- Interacción declarada acotada compuesta en una pieza materializada — espacio de controles declarado, sin queries nuevas (MAY).
- Catálogo público de Facetas disponibles para el AgencyDomain (SHOULD).
- Heurísticas de invocación documentadas para la cognición (SHOULD).

### Las tres fases evolutivas del agente

1. **Especializados** — un agente por dominio. Fase actual del mercado (inicios 2026).
2. **Orquestadores** — un agente coordina múltiples especialistas.
3. **Multiespecialistas** — expertise profundo multi-dominio en un único agente. Fase futura.

**La arquitectura es la misma en las tres fases.**

---

## 8 · El mercado — cadena de valor de IA

Modelo bidimensional: **once eslabones secuenciales × cuatro profundidades**.

### Once eslabones (cobertura)

1. **Datos** · 2. **Modelo** · 3. **Acceso** · 4. **Agentes** · 5. **Especializaciones** · 6. **Runtime** · 7. **Firewall** · 8. **Observabilidad** · 9. **Herramientas** · 10. **Integraciones** · 11. **Entorno**

### Cuatro profundidades

- **Wrapper** — consume vía APIs/SDKs de terceros.
- **Plataforma** — opera capacidad propia sobre componentes Core.
- **Core** — construye la capacidad fundacional con tecnología propia.
- **Infraestructura** — provee el sustrato.

### Matriz canónica

| Eslabón | 4 · Infraestructura | 3 · Core | 2 · Plataforma | 1 · Wrapper |
|---|---|---|---|---|
| **1 · Datos** | AWS/GCP/Azure | Scale AI/Labelbox · Hugging Face | — | — |
| **2 · Modelo** | NVIDIA · AWS/GCP/Azure | OpenAI · Anthropic · Google · Meta · DeepSeek/Qwen/Ernie | Hugging Face | — |
| **3 · Acceso** | — | Anthropic · DeepSeek/Qwen/Ernie | OpenAI · Google · Perplexity · ultraPRO | — |
| **4 · Agentes** | — | Perplexity · DeepSeek/Qwen/Ernie · Agentia (priv.) · Soveria (públ.) · (LangChain/Graph) · (AutoGPT/CrewAI) | OpenAI · Anthropic · Google · GitHub Copilot | — |
| **5 · Especializaciones** | — | Perplexity · GitHub Copilot · Cursor/Replit · Devin · Harvey/Jasper/Fin · umeeta | OpenAI | — |
| **6 · Runtime** | — | OpenAI · Devin · Agentia · Soveria · ultraPRO · (LangChain/Graph) · (AutoGPT/CrewAI) | — | — |
| **7 · Firewall** | — | Guardrails/NeMo/Lakera · ultraPRO | — | — |
| **8 · Observabilidad** | — | Langfuse/LangSmith/W&B · ultraPRO | — | — |
| **9 · Herramientas** | — | OpenAI · Anthropic · Google · Devin · ultraPRO · (LangChain/Graph) · (Pinecone/Weaviate) | — | — |
| **10 · Integraciones** | — | Zapier/Make/n8n · ultraPRO | — | — |

Derivada de la tabla de actores del Capítulo 6 (familias de productos representativas del mercado actual). Los paréntesis — p. ej. (LangChain/Graph) — indican framework o meta-herramienta (para construir, no para usar).

> ultraPRO ocupa la categoría arquitectónica **gateway empresarial completo** — Core simultáneo en eslabones 6-10 más extensión Plataforma en Acceso, bajo el patrón tripartito Cloud + Cliente + Local.

> **Eslabón 11 · Entorno**: queda fuera de la matriz — es el territorio sobre el que actúan los eslabones 1-10 (los sistemas empresariales que el agente vuelve backend invisible), no un eslabón que un actor de IA ocupe a una profundidad.

### Cuatro arquetipos estratégicos

- **Plataforma integral** — cobertura amplia (3+ eslabones); Core en su eslabón nativo, Plataforma en los adyacentes.
- **Especialista vertical** — cobertura focal, profundidad Core.
- **Infraestructura de dominio** — cobertura zonal, profundidad Core en varios eslabones.
- **Proveedor de sustrato** — cobertura mínima, profundidad Infraestructura.

### Observabilidad (eslabón 8) · seis capacidades canónicas

Una implementación completa de Observabilidad para sistemas agentivos cubre seis capacidades distintas:

1. **Tracing** — trazabilidad end-to-end de cada operación (eventos estructurados correlacionados por trace ID).
2. **Monitoreo de costos** — consumo de tokens/recursos en tiempo real por modelo/usuario/proyecto/tool; en sistemas maduros es predicción, no solo registro.
3. **Evaluación de calidad** — verificación sistemática de respuestas; dos sub-modos: automatizada (eval as service) y humana (revisión muestral).
4. **Métricas de rendimiento** — latencia (p50/p95/p99), throughput, disponibilidad, tasa de éxito (distinguida por Botlet/agente/sistema).
5. **Debugging y reproducibilidad** — replay de invocaciones; complejidad agregada por LLM probabilístico, estado persistente y regeneración de Botlets.
6. **Alertas y anomalías** — detección proactiva fuera de patrón; puede disparar circuit breakers, rollback o escalación.

> Mercado fragmentado por diseño: una organización madura combina dos o tres productos ("stack de observabilidad"), no una solución monolítica.

### Mundo de carbono · MEO

- **Mundo de carbono** — eslabón 11 extendido al mundo físico (IoT, procesos industriales). Patrones: edge computing, twin digital.
- **Cuatro sub-categorías del Entorno** (madurez decreciente, regulación creciente):
  1. **Sistemas empresariales tradicionales** — ERPs/CRMs/DBMS legacy; digitales pero institucionales; la más madura (integración: Zapier · Make · Workato · MuleSoft, aún mayormente agentic, no autónoma).
  2. **Mundo físico industrial** — manufactura y energía (SCADA · MES · PLCs · sensores); mayor valor capturable y más conservadora (regulación de seguridad de planta).
  3. **Mundo físico móvil** — transporte, logística, agricultura (flotas, drones, equipos agrícolas); agrega conectividad intermitente y coordinación geográfica; adopción más rápida.
  4. **Mundo biológico** — genómica, monitoreo médico, EHR, farmacovigilancia; mayor impacto humano y máxima exigencia de Trust (HIPAA · GDPR salud).
- **MEO — Model Engine Optimization** — prácticas para que modelos frontera referencien al actor. Equivalente del SEO en descubrimiento agentivo.

---

## 9 · Aplicación canónica — Conocimiento en tiempo real

```
┌──────────────────────────────────────────────────────────────────┐
│         KIMBALL BARNIZADA = KIMBALL CLÁSICO + CAPA AGENTIVA      │
│                                                                  │
│    SOURCE → ETL → PRESENTATION → BI APPS → AGENTE → HUMANO       │
│                                                                  │
│    ─────────────────────────────────────────────────────────     │
│    METADATA + CAPA SEMÁNTICA + TRUST SCORE + AI CERTIFICATION    │
│         (transversal — activo estratégico)                       │
└──────────────────────────────────────────────────────────────────┘
```

**Componentes esenciales** que distinguen Kimball Barnizada del Kimball clásico:

- **Capa semántica explícita**.
- **Trust Score por dato**.
- **AI Certification**.
- **Observabilidad de queries agentivos**.

**Mapeo a los hyperscalers** — cada uno implementa Kimball base con su propia terminología; la equivalencia funcional es directa:

| Proveedor | Warehouse / ETL | BI App | Gobernanza | Capa unificadora |
|---|---|---|---|---|
| **Azure** | Synapse Analytics | Power BI | Purview | Fabric |
| **AWS** | Redshift | QuickSight | DataZone | Lake Formation |
| **Google Cloud** | BigQuery | Looker | Dataplex | — |
| **Databricks** | Lakehouse + Medallion | — | Unity Catalog | — |

Medallion → Kimball: **Bronze** = Source (crudo) · **Silver** = ETL (limpio/conforme) · **Gold** = Presentation. Ningún hyperscaler tiene aún implementación completa de la **capa agentiva** del Kimball Barnizada.

---

## 10 · Operación

### CRUDLEX

Modelo canónico de permisos granulares: **C**reate, **R**ead, **U**pdate, **D**elete, **L**ist, **E**xecute. Aplicable por usuario, agente y contexto.

**Niveles preconfigurados** (nivel → CRUDLEX habilitado):

| Nivel | CRUDLEX habilitado |
|---|---|
| **FULL** | `C R U D L E` |
| **READ-WRITE** | `C R U D L` (no E) |
| **READONLY** | `R L` |
| **SAFE** | `R L E` (E limitado a operaciones reversibles) |
| **NO-SEND** | `C R U L` (no E) |
| **NO-DELETE** | `C R U L E` (no D) |

### Catálogo de políticas — cinco categorías

Un sistema agentivo bien diseñado tiene políticas activas en las **cinco**:

1. **Políticas de tools** — qué tools puede invocar el agente, sobre qué recursos (granularidad por agente, tool y scope).
2. **Políticas de datos** — qué clases de datos puede consultar o emitir, según sensibilidad.
3. **Políticas de horarios y umbrales** — cuándo y con qué umbrales de magnitud/riesgo actúa.
4. **Políticas de identidad** — qué identidades operan en nombre del agente y cómo se autentican (identidad federada).
5. **Políticas de validación** — qué validaciones se aplican antes de ejecutar (conectan con el Pilar 3).

**Composición jerárquica con monotonía descendente** (MUST): la política del agente hereda las restricciones de las superiores y solo puede **agregar** restricciones, nunca removerlas. Previene escalamientos accidentales de privilegios.

### Append-only log

Registro inmutable, encadenado criptográficamente, de toda acción. Componente central de Auditoría.

**Contenido mínimo de cada trace**: identidad del agente, capability invocada, tool ejecutado, **hash de parámetros y resultado** (no el contenido crudo — los datos sensibles viven en almacén separado con su propia política de retención), timestamp, contexto, y `previous_log_hash` que encadena con el registro anterior. Propiedad innegociable: el log guarda **hashes, no contenido**.

### Aprobación humana

Detiene una operación y solicita autorización antes de ejecutar. Disparada por: **política explícita**, **umbral**, **incertidumbre del agente**.

### Validación canónica (Pilar 3)

- Detección de alucinaciones · validación de respuestas estructuradas · prompt injection prevention · DLP · tokenización.

### Continuidad de negocio operacional vs garantía de fallback agéntico

Dos mecanismos complementarios:

| Mecanismo | Cuándo opera | Qué resuelve | Provisto por |
|---|---|---|---|
| **Garantía de fallback agéntico** | Botlet junior, en aprendizaje, o senior con variante nueva (cognición disponible) | Cambios de ambiente que el Botlet no anticipó | Spec agentiva (Capa 2 + Capa 3) |
| **Continuidad de negocio operacional** | Botlet senior caído por causa exógena, sin cognición disponible | Continuidad cuando ningún componente computacional opera | Protocolo del cliente |

La garantía de fallback agéntico **produce la madurez** del Botlet (sin ella, no madura); la continuidad operacional opera sobre Botlets senior caídos por causa exógena y no incide en la madurez. Reconocerlas separadas evita que el cliente atribuya a la arquitectura un fallo que corresponde a su protocolo.

### Modos de degradación del AgencyDomain

Cuatro modos canónicos según el escenario de falla. La organización debe poder identificar en cada momento en qué modo opera cada sitio.

| Modo | Condición | Quién sostiene la operación |
|---|---|---|
| **Normal** | Todos los componentes activos | Topología paralela completa |
| **Cognición caída** | Capa 2 inalcanzable, edge OK | **Vía Autonomía** sostiene; cognición rescatará al volver |
| **Edge offline** | Botler edge sin conexión a central; sitio aislado | **Botlets senior** contra BD local + Conectores edge-resident |
| **Continuidad operacional total** | Cognición + edge caídos por causa exógena | **Protocolo manual del sitio** |

**Transición automática hasta `Edge offline`** — la arquitectura degrada sola. **Transición a `Continuidad operacional total` es gobernada por el protocolo del sitio** — un humano la activa explícitamente. Diferencia clave: los primeros tres modos son responsabilidad de la arquitectura; el cuarto es responsabilidad del cliente.

### Trazabilidad de la transición — tags canónicos del log

- `mode-change: continuity-operational` — cuando el sitio activa protocolo manual.
- `provenance: manual-continuity` + `original-timestamp` — registros físicos ingresados retroactivamente.
- `provenance: edge-queue-replay` — drenaje de cola edge tras volver la red.
- `agentic-fallback` vs `operational-continuity` — distinción auditable entre cognición rescatando y humano sosteniendo.

### Propiedades exigidas (Pilar Resiliencia + Continuidad)

| Propiedad | Nivel |
|---|---|
| Distinción explícita en documentación de producto | MUST |
| Protocolo de continuidad operacional documentado por sitio | MUST |
| Simulacros con frecuencia mínima trimestral | SHOULD |
| Cuatro modos de degradación reconocibles por la organización | MUST |
| Trazabilidad de transición a modo continuidad en append-only log | MUST |
| Distinción auditable entre fallback agéntico y continuidad operacional | MUST |
| Reconciliación retroactiva de registros físicos al sistema | MUST |

---

## 11 · Frontera de evolución

Tres horizontes **técnicos** vivos:

1. **Cognición no-LLM** — la Capa 2 admite cognición simbólica, híbrida, multimodal.
2. **Federación (`A2A` entre AgencyDomains)** — protocolos abiertos en evolución. La coordinación intra-AgencyDomain (vía el protocolo `A2A`) ya es madura; la `A2A` *entre* AgencyDomains distintos es trabajo abierto.
3. **Mundo de carbono** — extensión de Capa 4 al mundo físico.

El libro humano cuenta **cuatro fronteras vivas**: estos tres horizontes técnicos más una **cuarta frontera institucional** — soberanía y ciudadanía agentiva (**AgentNation**, abajo).

### Generaciones del Botlet — G1/G2/G3

Modelo evolutivo de cómo nace el código del Botlet conforme avanza el estado del arte de la cognición. **La arquitectura es la misma en las tres**; cambia el **alcance de la Ingeniería**. Una implementación puede operar en `G1` hoy y migrar hacia `G3` sin re-arquitectura.

- **G1** — el agente configura proto-Botlets pre-forjados del catálogo (no escribe el cuerpo). Si ninguno sirve, especifica uno nuevo para forjar en la próxima Preparación.
- **G2** — el agente co-escribe proto-Botlets con asistencia humana o de modelo.
- **G3** — el agente genera el código completo del Botlet en tiempo de Ingeniería (escenario asintótico).

**G1 admite configuración expresiva rica**: lo que define `G1` es que el agente no escribe el cuerpo del proto-Botlet; la configuración puede ser tan rica como un `DSL` composicional con expresiones formales evaluables. La distinción `G1`/`G3` es sobre **autoría del cuerpo**, no sobre expresividad de la config.

**Filo `G1`/`G2`** (test: *"¿el código pertenece a la Capability invocada o al proto-Botlet mismo?"*): una expresión formal evaluable que es **parámetro de una Capability bien definida** (`SQL`→`execute-sql`, una especificación de gráfico→`render-chart`, filtro→`filter-stream`) es configuración → **`G1`**. Una expresión que **extiende/sobreescribe la lógica interna del proto-Botlet** (callbacks, lambdas que evalúa internamente) es código del agente → **`G2`**.

**Reconciliación — dos ejes distintos, no la misma flecha**:

| Eje | ¿Qué mide? | Dirección de "avance" |
|---|---|---|
| **Capacidad de autoría** | Cuánto puede forjar: configurar (`G1`) → co-escribir (`G2`) → generar (`G3`) | Hacia `G3`, con el estado del arte de la cognición |
| **Madurez operativa** | Para una operación recurrente, cuánto se reutiliza pre-forjado vs se regenera (ciclo `95/4/1`) | Hacia la reutilización (`G1`), conforme el Botlet madura junior → senior |

La capacidad `G3` **se gasta mejor produciendo reutilización `G1`**: el destino de `G3` es un catálogo `G1` más rico, no la regeneración en vivo de todo. Para un proto-Botlet **platafórmico**, `G1` es **terminal por diseño**, no estación de paso. El agente más avanzado **genera menos porque ha cristalizado más**, y reserva la generación para el borde (el 4%+1% del ciclo). Paralelo cerebral: corteza = Cognición (Capa 2); cerebelo + ganglios basales = Autonomía (Capa 3). La sofisticación es **estratificarse para que la cognición no tenga que hacerlo todo**.

### AgentNation

AgencyDomain en régimen público que adopta el modelo de ciudadanía agentiva. Los agentes son **ciudadanos**, no productos. Distinción ontológica: marketplace lista productos; AgentNation reconoce ciudadanos. Trabajo arquitectónico abierto.

---

## 12 · Glosario canónico (alfabético)

### A

- **A2A — Agent-to-Agent** — nombre reservado a la **relación entre AgencyDomains distintos** (agentes distintos; federación). La comunicación dentro de un mismo AgencyDomain **no es "A2A interna"**: es **coordinación intra-AgencyDomain**, y cuando usa ese transporte se dice **vía el protocolo `A2A`**. La interfaz Capa 2 → Capa 3 va por `MCP`, no por `A2A`.
- **AgencyDomain** — ámbito computacional con identidad propia donde habitan agentes autónomos y Botlets, **donde se alojan y ejecutan las Capabilities**, y donde viven los recursos que los sostienen. Unidad mínima de despliegue.
- **Agente** — término paraguas que cubre tres miembros: el **Asistente** (Capa 2, reactivo), el **Agente Autónomo** (Capa 3, proactivo, habitante) y el **Agentlet** (Capa 3, empaquetado, pieza de catálogo). La distinción no es jerárquica.
- **Agentlet** — **octava primitiva canónica**. Unidad empaquetada de Capa 3, hermana del Botlet, cuyo cuerpo invoca **inferencia acotada** dentro de un charter declarado en el spec. Casa de la tarea recurrente en forma pero interpretativa en cada instancia. **El Agente tiene agenda; el Agentlet tiene charter.** Instancia de un proto-Agentlet; hospedado por el Botler (`cognition_call`); fallback a la Cognición plena. Peldaño económico intermedio entre Botlet y Cognición.
- **Agente Autónomo** — proactivo, vida persistente, mantiene Botlets. Capa 3.
- **Agéntico** — mundo de agentes complementarios. Evolución incremental.
- **Agentivo (Mundo Agentivo)** — agentes como interfaz única. Transformación fundamental.
- **AgentNation** — AgencyDomain público con modelo de ciudadanía agentiva.
- **Agent First** — principio rector: experiencia del agente prima sobre la del humano.
- **Append-only log** — registro inmutable, encadenado criptográficamente.
- **Aprobación humana** — autorización antes de ejecutar operación crítica.
- **Arquetipo estratégico** — patrón de posicionamiento en el espacio cobertura × profundidad de la cadena de valor. Cuatro canónicos: Plataforma integral (cobertura amplia; Core en su eslabón nativo y Plataforma en los adyacentes) · Especialista vertical (cobertura focal, profundidad Core) · Infraestructura de dominio (cobertura zonal, Core en varios eslabones) · Proveedor de sustrato (cobertura mínima, profundidad Infraestructura).
- **Arquitectura Agentiva** — diseño técnico que materializa el Mundo Agentivo. Cuatro capas (Interacción, Cognición, Autonomía, Acceso), gobernadas por Trust Infrastructure transversal y ordenadas por el principio Agent First.
- **Asistente** — agente reactivo, sin Botlets, sin vida persistente. Capa 2.
- **Atención** — uno de los **tres tiempos del agente**. Tiempo en que el agente interactúa con usuarios o eventos en tiempo real. Capa 1 activa, camino crítico, prioritario.
- **Auditoría** — Pilar 2 de Trust Infrastructure. Reconstruir después del hecho **qué hizo el agente, cuándo, por qué y sobre qué datos**. Mecanismo central: append-only log; lo completan trace, lineage e identity tagging.

### B

- **BCA — Bounded Concerns Architecture** — arquitectura del estado pre-agentivo.
- **Botlet** — unidad de automatización auto-evolutiva. Código no-LLM. Memoria muscular. Ciclo `95/4/1`.
- **Botlet de fachada** — Botlet de Capa 3 que expone una superficie operativa con contrato estable en Capa 1, identidad humana propagada.
- **Botlet de operación** — Botlet de **Capa 3** que ejecuta lógica de negocio invocada desde la Capa 1 (vistas y shells). Más reutilizable del catálogo. Ejemplos: cobrar mesa, imprimir comanda, cerrar turno.
- **Botlet de superficie (shell)** — Botlet de **Capa 1** que actúa como contenedor: layout, navegación, sesión, estado compartido. Específico de cada producto.
- **Botlet de vista** — Botlet de **Capa 1** que materializa una pantalla o panel dentro de un shell. Ensambla Facetas + lógica de orquestación. Reutilizable entre shells.
- **Botlet emergente** — generado por Pattern Recognition cuando detecta patrón repetitivo no anticipado.
- **Botlet en aprendizaje** — fase intermedia de madurez. Proporción `85/12/3`.
- **Botlet junior** — fase inicial. Proporción `60/35/5`. Depende de cognición.
- **Botlet seed** — generado por cognición a pedido del equipo de diseño, como parte del producto inicial.
- **Botlet senior** — fase madura. Proporción `99+/<1/~0`. Fallos solo exógenos. Operable offline.
- **Botler** — runtime **genérico** de Capa 3 (no entiende dominio) que ejecuta los **Lets** de la capa: Botlets y Agentlets. Tipo (constructo normado de la spec de Botlets), no nombre propio. Sin subtipos por dominio; valida orquestando (handle controlado con `capability_call` · `log` · `cognition_call`); expone servidor `MCP` a la Cognición. **1 Proceso = 1 Botler + N Lets**.
- **Botler central** — Botler de orquestación, planificación, reportería en Capa 3 distribuida.
- **Botler edge** — Botler de transacciones locales en Capa 3 distribuida. Uno por sitio físico.
- **BYOModel** — Bring Your Own Model. Sustitución del proveedor default. SHOULD para mercados regulados.

### C

- **Cadena de valor de IA** — modelo bidimensional 11 eslabones × 4 profundidades.
- **Capa 1 — Interacción** — interfaz humano-IA con tres regímenes de GUI.
- **Capa 2 — Cognición** — cerebro del agente.
- **Capa 3 — Autonomía** — vida persistente. Admite distribución geográfica (Capa 3 distribuida).
- **Capa 3 distribuida** — patrón canónico para presencia física múltiple. Botler central + N Botlers edge.
- **Capa 4 — Acceso** — poder de ejecución con Trust Infrastructure.
- **Capability** — saber-hacer **cognitivo** modular y composable, reservado a **Capa 2 · Cognición**. NO plugin, NO prompt, NO tool. **Es saber.** Expone **features**; es **portable** (corre en cualquier AgencyDomain conforme).
- **Conector cloud-resident** — vive en servicio remoto. Típicamente online-only.
- **Conector edge-resident** — vive en sitio físico, asociado a hardware. Típicamente offline-capable.
- **Conector híbrido** — componente local + componente cloud. Offline-capable con encolamiento.
- **Conector offline-capable** — ejecuta sin red. Encola si emite hacia afuera.
- **Conector online-only** — requiere red.
- **Capability regulada** — porta el saber normativo de una operación sujeta a certificación (DTE-SII, PCI-DSS, etc.). La certificación regulatoria reside en el **Conector certificado** que ejecuta la operación, no en la Capability ni en el Botlet.
- **Capa semántica** — codifica significado de dimensiones, hechos, jerarquías. Esencial para Kimball Barnizada.
- **Cadena de derivación** — relación estructural `casos de uso → Botlets necesarios → proto-Botlets del catálogo`. Todo Botlet conforme MUST poder trazarse en ella; el log registra el proto-Botlet de origen.
- **Catálogo común** — los proto-Botlets se acumulan en catálogos compartidos con efectos de red. Modos: contrato privado · códice propietario · catálogo público abierto · acuerdo soberano.
- **Cluster** — instancias del mismo AgencyDomain compartiendo carga.
- **códice propietario** — catálogo privado de proto-Botlets, Capabilities y patrones que un implementador cura sobre la implementación de referencia pública, refinado por sus casos reales. Uno de los cuatro modos de pertenencia a una comunidad de catálogo. El runtime es común; el códice es propio (encapsula la ventaja competitiva). Instancia canónica: **ucodex** (Grupo Ultra).
- **Conector** — saber **acceder a sistemas fuente** (conexión con poder de ejecución; NO saber cognitivo). **Capa 4 · Acceso.** La API legacy traída al Mundo Agentivo se convierte en Conector, no en Capability.
- **Conformed dimensions** — concepto de Kimball: dimensiones compartidas entre data marts que garantizan consistencia inter-marts.
- **Continuidad de negocio operacional** — protocolos manuales para Botlet senior caído por causa exógena con cognición no disponible. Distinta y complementaria del fallback agéntico.
- **Contrato declarativo de calidad** — atributos de calidad de un Botlet declarados como propiedades estructuradas: Frescura · SLA · Política de degradación · Audiencia · Política de refresh. Trust Infrastructure los audita uniformemente.
- **coordinación intra-AgencyDomain** — comunicación entre runtimes (Botlers) del **mismo** AgencyDomain. **NO es "A2A interna"**: son runtimes del mismo agente, no agentes distintos. Cuando usa ese transporte se dice **vía el protocolo `A2A`**. Contraconcepto de `A2A` (relación entre AgencyDomains distintos).
- **CRUDLEX** — Create, Read, Update, Delete, List, Execute.
- **Cuenta** — concepto comercial; puede poseer múltiples AgencyDomains.

### D

- **DLP — Data Loss Prevention** — detección de PII no autorizada.
- **Domain** — sinónimo comercial de AgencyDomain.
- **Dominion** — Domain conseguido por agente en AgencyDomain público con modelo de AgentNation.

### E

- **Edge computing** — distribución de Capa 3 cerca del proceso físico.
- **Empresa en línea** — datos actualizados al día, depende de humanos para interpretar.
- **Empresa en tiempo real** — detecta, interpreta, decide y actúa autónomamente.
- **Eslabón** — capa funcional de la cadena de valor (1 a 11).

### F

- **Faceta** — **sexta primitiva canónica**. Componente atómico reusable de Capa 1: pizarra, catálogo-selector, calendario, mapa, slider, drag-and-drop. Instrumento que la cognición invoca durante conversación o que los Botlets de presentación ensamblan. **NO es un Botlet** (Capa 1 vs Capa 3 · efímera vs persistente · sin fallback agéntico vs con).
- **feature** — operación interna que una Capability expone (equivalente de *feature/operation/skill/method*). Test Capability vs feature: independencia operativa + identidad cognitiva + reusabilidad; si falla uno → es feature de la Capability contenedora.
- **Federación** — comunicación entre AgencyDomains distintos.
- **Firewall** — eslabón 7. Seguridad, governance, prompt injection prevention.

### G

- **Garantía de fallback agéntico** — la cognición ejecuta cuando el Botlet falla. **El proceso nunca se detiene.** **Lo que produce la madurez del Botlet.**
- **Generaciones del Botlet — G1/G2/G3** — modelo evolutivo del nacimiento del código del Botlet. **G1**: configura proto-Botlets pre-forjados (no escribe el cuerpo). **G2**: co-escribe el proto-Botlet. **G3**: genera el código completo (asintótico). Cambia el alcance de la Ingeniería, no la arquitectura. La capacidad G3 se gasta mejor produciendo reutilización G1; para un platafórmico, G1 es terminal por diseño.
- **Gateway empresarial de IA** — Core en Runtime+Firewall+Observabilidad+Herramientas+Integraciones.
- **Gobernanza** — Pilar 1 de Trust Infrastructure.
- **GUI on-the-fly** — Régimen 2 de Capa 1. Superficie gráfica adaptada a la tarea, vive lo que dura la tarea.
- **GUI persistente como Botlet de fachada** — Régimen 3 de Capa 1. Superficie estable de un Botlet de fachada (Capa 3, típicamente seed) para roles operativos repetitivos.

### H

- **Hallucination (alucinación)** — afirmación factualmente incorrecta. Detección en Pilar Validación.
- **Híbrido (régimen)** — AgencyDomain con core privado + exposición pública parcial.

### I

- **Ingeniería** — uno de los **tres tiempos del agente**. Puente entre Preparación y Atención: convierte capacidad latente en capacidad ejecutable para un caso concreto. Configura Botlets seed, valida deploy. Mediano plazo (minutos a horas).
- **Instrumento de información** — el **tipo** canónico de la familia de información (la clase: reporte / dashboard). Distinto del **Producto de Información**, que es su instancia manifestada.
- **Interacción declarada acotada** — interacción que opera sobre el **snapshot ya materializado** de una pieza, en un espacio **declarado**, que **mantiene reproducibilidad** y es **`G1`** (configuración, no código). Vive en la pieza misma vía **Faceta embebida** (recómputo client-side, sin invocar Capabilities). Distinta de la **exploración libre** (query arbitraria al origen, excede `G1`).

### J

- **JSR — Java Specification Request** — formato canónico de especificaciones de Java (Sun Microsystems / Oracle). **JavaSpaces (JSR-000148, 1999)** es el análogo conceptual de AgencyDomains.

### K

- **Kimball / Kimball Barnizada** — modelado dimensional + capa agentiva.

### L

- **LLM** — Large Language Model.
- **Let (plural: Lets)** — **nombre propio del género** de las piezas empaquetadas que el Botler hospeda y ejecuta; vocabulario normado (como Botler), no primitiva. Descriptivamente: la unidad empaquetada de Capa 3. Dos especies: **Botlet** (código no-LLM) y **Agentlet** (inferencia acotada). El aparato compartido se predica del género; las garantías diferenciales, de cada especie. Invariante ES/EN. Relación canónica: **1 Proceso = 1 Botler + N Lets**.
- **Línea Nadella** — umbral entre Mundo Agéntico y Mundo Agentivo. *¿El humano abre aplicaciones para hacer su trabajo?* (formulación canónica; *La Empresa en Tiempo Real* la conjuga en segunda persona y *AURA* en la voz del directivo — las tres son equivalentes oficiales).

### M

- **manifestación** — actualización de la disposición latente del Botlet en el mundo, perceptible o no (potencia → acto). NO es "aparición". Género abstracto: información → deja un `PI`; actuación → efecto sobre el mundo; decisión → según su práctica.
- **MCP — Model Context Protocol** — protocolo abierto canónico para tools de Capa 4 y para la interfaz interna Capa 2 → Capa 3 (Cognición cliente, Botler servidor). Anthropic, noviembre 2024.
- **MEO — Model Engine Optimization** — equivalente del SEO en descubrimiento agentivo.
- **Memoria muscular** — metáfora canónica del Botlet.
- **Meta-Cognitive Platform** — categoría de plataforma que administra la **economía de la cognición** (G1 músculo pre-forjado vs fallback de cognición fresca, ciclo `95/4/1`, maduración junior→senior, cristalización). **Vergis** es la implementación de referencia. **NO se abrevia a "MCP"** (sigla tomada por Model Context Protocol).
- **Mira** — nombre propio de un proto-Botlet **platafórmico** de operación informativa del catálogo de la implementación de referencia.
- **Modos de degradación del AgencyDomain** — Normal · Cognición caída · Edge offline · Continuidad operacional total. Las primeras tres transiciones son automáticas; la cuarta requiere activación humana por protocolo.
- **Mundo de carbono** — eslabón 11 extendido al mundo físico.

### O

- **Observabilidad** — eslabón 8 de la cadena de valor: la capa que **observa, mide y retroalimenta** el sistema de IA en producción. Su pregunta: *¿cómo funciona?* Sin ella, los agentes son cajas negras.

### P

- **Pattern Recognition** — detección de patrones repetitivos. Activa generación de Botlets emergentes.
- **Patrón tripartito Cloud + Cliente + Local** — patrón canónico de despliegue de Trust Infrastructure enterprise.
- **Plantilla** — confección específica del cliente sobre un **instrumento canónico** (reporte/dashboard) en un formato o regla propios. **Capa 1 · Interacción.** NO es Capability ni Conector.
- **Portabilidad de la Capability** — una Capability conforme corre en cualquier AgencyDomain conforme; la vuelve propiedad real del cliente. Distinta de la portabilidad del AgencyDomain.
- **Portabilidad del AgencyDomain** — propiedad estructural: AgencyDomain conforme migrable a otra plataforma conforme sin reescritura. Tres condiciones: Botlets contra primitivas canónicas, BD exportable, Trust Layer portable.
- **Preparación** — uno de los **tres tiempos del agente**. *Mise en place* — el agente refina catálogo, mejora capacidades, fuera de ventana de servicio. Régimen batch / off-peak.
- **Privado (régimen)** — AgencyDomain en perímetro controlado. Sin acceso público.
- **Producto de Información (`PI`)** — instancia manifestada/entregada de la familia de información (la manifestación concreta de un Instrumento de información). Cada `PI` es su propio Botlet/servicio especializado de un motor compartido (proto-Botlet platafórmico). **NO es primitiva del canon** — vive en la práctica de información.
- **Profundidad** — dimensión vertical: Wrapper / Plataforma / Core / Infraestructura.
- **Prompt injection** — manipulación vía inputs maliciosos.
- **proto-Agentlet** — pieza pre-forjada de capacidad interpretativa que el agente **configura** en su tiempo de Ingeniería para instanciar un Agentlet. Contiene el cuerpo (estructura del charter, esqueleto del prompt operativo, contratos de entrada/salida, umbrales de escalamiento); el Agentlet es la instancia configurada. Mismas clases (templado · platafórmico), misma cadena de derivación y mismos catálogos que el proto-Botlet.
- **proto-Botlet** — **séptima primitiva canónica**. Pieza pre-forjada de capacidad operativa que el agente **configura** en su tiempo de Ingeniería para instanciar un Botlet. El proto-Botlet contiene el código; el Botlet es la instancia configurada. Dos clases: **templado** (código específico; parametrización acotada) · **platafórmico** (motor genérico; configuración composicional; cubre N funciones). Catálogos públicos (AgencyDomains.org) o privados (códices propietarios).
- **Público (régimen)** — AgencyDomain accesible públicamente.

### R

- **RAG — Retrieval-Augmented Generation**.
- **Régimen** — modo de despliegue de AgencyDomain según frontera de acceso. **Estructura técnica equivalente; cambia el régimen, no la capacidad.**
- **Resiliencia** — Pilar 4 de Trust Infrastructure.
- **Runtime** — eslabón 6. Ambiente operativo del agente. Corresponde a Capa 3.

### S

- **Salto Cuántico** — umbral habilitado por el colapso del costo de la pregunta analítica: cuando preguntarle a los datos deja de ser caro, lento o mediado por un humano, la organización cruza de **empresa en línea** a **empresa en tiempo real**. Cambio de régimen operativo, no mejora incremental de BI.
- **Sandbox** — aislamiento de ejecución de Botlets. Cuatro estrategias: procesos+seccomp, contenedores, WASM, MicroVMs.
- **Señalética** — dashboards pasivos sin requerir interacción.
- **SME — subject-matter expert** — experto humano cuyo saber se transfiere al agente en la construcción de Capabilities. Workshop inicial y validación ALFA del Wingtraining.
- **Space / WorkSpace** — habitat humano. Reservado para humanos.

### T

- **temporalidad** — régimen de la manifestación del Botlet. Atributo declarado: **`discreta`** (pulsos: schedule/trigger/evento) y **`continua`** (vida persistente; obliga al runtime persistente de Capa 3). El "tiempo real" se elige dando temporalidad continua, no marcando un canal `push`.
- **Tokenización** — reemplazo de datos sensibles por tokens antes de la cognición.
- **Tool** — herramienta invocable. Eslabón 9. Protocolo canónico: MCP. **NO es Capability.**
- **Topología paralela** — modelo canónico de las cuatro capas. Capas 2 y 3 son **vías paralelas** entre Capa 1 y Capa 4, no etapas en serie.
- **Trace** — trazabilidad end-to-end.
- **Transparencia** — Pilar 5 de Trust Infrastructure. Entender en tiempo real **qué está haciendo el agente y por qué**, con detalle para intervenir. Conecta los otros cuatro pilares.
- **Tres tiempos del agente** — marco temporal canónico: **Preparación** (mise en place, batch / off-peak), **Atención** (camino crítico, tiempo real), **Ingeniería** (puente, mediano plazo). La topología paralela describe DÓNDE; los tres tiempos describen CUÁNDO.
- **Trust Infrastructure** — cinco pilares: Gobernanza, Auditoría, Validación, Resiliencia, Transparencia.
- **Twin digital** — gemelo digital. Patrón para mundo de carbono.

### U

- **ucodex** — nombre propio del **códice propietario** del Grupo Ultra: su catálogo privado de proto-Botlets, Capabilities y patrones, curado por casos reales sobre la implementación de referencia (Vergis). Instancia que ejemplifica el modo *códice propietario*; mismo cajón de nombres propios que Soveria, Agentia, ultraPRO — no un tipo del canon.

### V

- **Validación** — Pilar 3 de Trust Infrastructure.
- **Vergis** — nombre propio de la implementación de referencia pública de AgencyDomains (la plataforma; el AgencyDomain hecho operativo). Categoría: **Meta-Cognitive Platform**. Distribuida **AGPL**, repo público, **AgencyDomains.org**. Nombre propio de instancia (como Soveria, Agentia, ultraPRO), no un tipo como Botler.
- **Vía Autonomía** — una de las dos vías de la topología paralela. Rápida, barata, repetitiva. Para Botlets sobre patrones estables.
- **Vía Cognición** — una de las dos vías de la topología paralela. Lenta, costosa, decisiva. Para conversación, decisiones nuevas, casos no anticipados.

### W

- **Wingtraining** — esquema canónico de desarrollo de una Capability en cinco pasos: workshop con el SME · creación · personalización · ALFA · BETA.
- **Wingworking** — práctica colaborativa humano-IA. Marco metodológico bajo el cual el libro fue producido.
- **WorkSpace** — ver Space.
- **Wrapper / Plataforma / Core / Infraestructura** — las cuatro profundidades canónicas.

---

## 13 · Implementaciones de referencia

La arquitectura es **agnóstica a productos**. Admite múltiples implementaciones cooperantes.

**Aclaración canónica**: las cuatro capas son radiografía del agente individual. **No son slots donde se asigne un producto a cada uno.**

**Nota de alcance del canon**: este canon contiene la estructura y el vocabulario del Mundo Agentivo — definiciones, primitivas, propiedades exigidas, separaciones canónicas. **No contiene métodos para implementar ni catálogos operacionales**: esos viven en cuerpos complementarios. La implementación de referencia pública es **AgencyDomains.org**, materializada en **Vergis**.

### Vergis — implementación de referencia pública

**Vergis** es la implementación de referencia pública de AgencyDomains — el AgencyDomain hecho operativo. Distribuida bajo **`AGPL`** (código) y **`GFDL`** (docs), repositorio público en **AgencyDomains.org**, diseñada para descargarse, leerse, ejecutarse y aprender cómo el canon se traduce en sistemas vivos. Su desarrollo completo es el **Capítulo 9** del libro.

**Esquema de nombres — tipo vs nombre propio**:

| Capa | Tipo / categoría | Nombre propio |
|---|---|---|
| Plataforma · *Meta-Cognitive Platform* | implementación de referencia de AgencyDomains | **Vergis** |
| Runtime de Capa 3 | **Botler** (constructo normado de la spec de Botlets, genérico) | — (sin nombre propio) |
| Componente del catálogo | proto-Botlet platafórmico de operación informativa | **Mira** |

- **Botler** es un **tipo** (constructo normado de la spec de Botlets — no una de las ocho primitivas). Cualquier runtime de Capa 3 conforme *es un* Botler.
- **Vergis** y **Mira** son **nombres propios** de instancias (mismo cajón que Soveria, Agentia, ultraPRO).
- Categoría de Vergis: **Meta-Cognitive Platform** — administra la **economía de la cognición** (G1 músculo pre-forjado vs fallback de cognición fresca, ciclo `95/4/1`, maduración junior→senior, cristalización). **NO se abrevia a "MCP"** — esa sigla nombra el Model Context Protocol. El descriptor se usa deletreado.

**Qué incluye**: contrato abstracto del **Botler** (genérico, con puntos de control `capability_call`/`log` y validación por delegación) · **Mira** (proto-Botlet platafórmico operando en `G1`) · conjunto starter de **Capabilities** y **Conectores** · plantillas de Trust Infrastructure (políticas, append-only log, contrato declarativo de calidad) · ejemplos ejecutables que recorren la cadena `caso de uso → Botlets → proto-Botlets`.

**Production grade**: es el **mismo runtime** que opera los productos comerciales (Agentia · Soveria · ultraPRO). La diferencia con esos productos **no es la calidad del código sino el catálogo**: los productos consumen la referencia pública **más un códice propietario** (ucodex es un ejemplar) que cura proto-Botlets, Capabilities y patrones refinados por casos reales.

**Modelo de adopción** (replicable sin permiso ni contrato central): (1) **consume** la referencia pública; (2) **cura** su propio códice; (3) **ofrece** sus productos sobre esa base. AgencyDomains.org no es propiedad de un actor: es base común.

**Catálogo común y efectos de red**: los proto-Botlets se acumulan en catálogos compartidos; cada consumidor contribuye a la maduración y el implementador n+1 recibe versiones refinadas por los implementadores 1..n. Cuatro modos de pertenencia: **contrato privado** · **códice propietario** · **catálogo público abierto** (AgencyDomains.org) · **acuerdo soberano**. El runtime es común; la curaduría es de cada quien.
