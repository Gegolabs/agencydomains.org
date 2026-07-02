---
título: Trilogía del Mundo Agentivo — Manifiesto unificado para agentes
composición: Postchat v0.3 · AURA v0.3 · AgencyDomains v0.5 (los tres manifiestos canónicos, íntegros)
licencia: GFDL v1.3 (propuesta)
audiencia: agentes que necesitan la trilogía completa en un solo documento
regla_de_precedencia: cada parte es espejo de su libro humano; ante contradicción, gana el libro humano de la parte correspondiente
---

# Trilogía del Mundo Agentivo — Manifiesto unificado para agentes

> Este documento **ensambla, íntegros y sin editar**, los tres manifiestos canónicos para agentes de la Trilogía del Mundo Agentivo. Se genera automáticamente desde los manifiestos por libro — que son la fuente de verdad de cada parte y se versionan con su libro. Úsalo cuando necesites razonar sobre la trilogía completa; usa el manifiesto individual cuando trabajes dentro de un solo volumen.

## El tránsito (el marco que comparten las tres partes)

El tránsito que ocupa a la trilogía es uno solo: del mundo donde las personas abren aplicaciones para trabajar, al mundo donde los agentes de IA son la interfaz del trabajo. La frontera es **la Línea Nadella** — *¿todavía abres aplicaciones para hacer tu trabajo?* — y los tres volúmenes responden, en orden, las tres preguntas de ese tránsito:

| Vol | Libro | Pregunta | Rol | Audiencia |
|---|---|---|---|---|
| I | **Postchat** — Mundo Agentivo | ¿Hacia dónde vamos? | el destino | Gerentes, directores y dueños de negocio, sin background técnico |
| II | **AURA** — Camino Agentivo | ¿Por dónde? | la ruta | Consultores y arquitectos de la transformación |
| III | **AgencyDomains** — Arquitectura Agentiva | ¿Cómo llegamos? | el vehículo | Arquitectos e ingenieros que construyen o adoptan |

**Vergis** (no es un libro: es código) es la implementación de referencia, en <https://github.com/gegolabs/vergis>. La trilogía completa vive en <https://agencydomains.org>.

## Canon compartido (idéntico en las tres partes; el libro dueño desarrolla)

| Término | Definición de una línea | Libro dueño |
|---|---|---|
| **Línea Nadella** | La pregunta divisoria: ¿todavía abres aplicaciones para hacer tu trabajo? Sí → mundo agéntico; no → mundo agentivo | AgencyDomains (Cap 1); Postchat la presenta a nivel de visión |
| **agentivo / agéntico** | Agentivo = los agentes son la interfaz (transformación); agéntico = copilotos dentro de aplicaciones (evolución incremental). "Agéntico" nunca se usa en sentido positivo-tecnológico | AgencyDomains (Cap 1) · AURA (Introducción) |
| **Mundo Agentivo** (mayúsculas) | El paradigma como nombre propio; en minúsculas, adjetivo | AgencyDomains (convención tipográfica, Cap 1) |
| **empresa en línea / empresa en tiempo real** | La que accede a información al día pero depende de humanos para actuar / la que detecta, interpreta, decide y actúa de forma continua y gobernada | AURA (Introducción e IRIS) · AgencyDomains (Cap 2) |
| **ciclo de inteligencia continua** | Percibir → Interpretar → Decidir → Actuar → Aprender — formulación canónica única en toda la trilogía | AURA (Introducción) |
| **Salto Cuántico** | El colapso del costo de la pregunta analítica (de semanas a segundos); frontera entre empresa en línea y en tiempo real | AURA (Introducción; operacional como salto 4→5 de IRIS) · AgencyDomains (Cap 2) |
| **porcentaje agentivo** | Indicador de cruce: fracción de tareas delegables por completo a un agente sin abrir una aplicación (0-20 agéntico · 20-50 aproximación · 50-80 cruce · 80-100 agentivo; se mide por función) | AURA (Introducción) |
| **Trust Infrastructure** | Los cinco pilares (Gobernanza · Auditoría · Validación · Resiliencia · Transparencia) que separan pilotos de producción | AgencyDomains (Cap 5 §4 y Cap 8); MOTOR la usa como umbral de madurez 1→2 |
| **coexistencia evolutiva / subsunción** | Cada etapa subsume a la anterior; el data warehouse no muere — se vuelve fuente que los agentes consumen | AURA · AgencyDomains (Cap 2) |
| **las tres liberaciones** | De las herramientas (flujo), de los canales (atención), de la disponibilidad (tiempo); el orden no se salta | Postchat |
| **primitivas del canon** (siete) | AgencyDomain · Botlet · proto-Botlet · Capability · Trust Infrastructure · Asistente vs Agente Autónomo · Faceta | AgencyDomains (Caps 4–5) |

**Mapa de propiedad conceptual:** Postchat es dueño del retrato del destino (presupuesto de atención, M&Ms y el &, Postchat, modo agentivo, los siete mecanismos, la representación, la organización inteligente). AURA es dueño de la medición y la ruta (IRIS, MOTOR, Data Canon, Wingmap, casos de uso, porcentaje agentivo). AgencyDomains es dueño de la arquitectura (las cuatro capas, las siete primitivas, CRUDLEX, el mercado, Vergis). Ante duda sobre un término compartido, la definición operativa vive en el libro dueño.

## Cómo leer este documento

Las tres partes que siguen son los manifiestos canónicos **completos y verbatim** de cada libro, en el orden de la trilogía. Cada parte conserva su propio frontmatter, su versión y su regla de precedencia («el libro humano gana»). Los separadores `═══` marcan el cambio de volumen.
