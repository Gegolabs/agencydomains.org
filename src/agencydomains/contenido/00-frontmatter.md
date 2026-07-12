# AgencyDomains

### Arquitectura del Mundo Agentivo

**Autor:** César Obach-Renner
**Editor:** GegoLabs
**Edición:** Borrador de desarrollo · Julio 2026 · v0.6
**Licencia:** GNU Free Documentation License v1.3 *(propuesta)*

> **Nota sobre la versión.** Este es un **borrador de desarrollo pre-1.0**: las referencias y las figuras pueden reorganizarse entre iteraciones hasta la versión **1.0**, que será la primera publicación pública estable. Comentarios y erratas son bienvenidos en el repositorio. El historial de versiones vive en `CHANGELOG.md`.

## Sobre este libro

La industria de la IA construye agentes con la misma actitud con que construyó aplicaciones web en 2005: cada proveedor con su propio stack, sin contratos comunes, sin separación clara de responsabilidades. Gartner proyecta que más del **cuarenta por ciento de los proyectos de IA agentiva serán cancelados antes de fines de 2027** por costos, valor de negocio poco claro o controles de riesgo inadecuados. **Solo el veintiuno por ciento de las organizaciones tiene gobernanza madura sobre sus agentes**. La causa raíz es estructural: la categoría carece de una arquitectura formal compartida — y no tiene un nombre concreto para la unidad mínima de despliegue.

Este libro propone ese nombre y esa arquitectura. La unidad mínima de despliegue es el **AgencyDomain** — el ámbito computacional donde los agentes habitan, los Botlets ejecutan y la Trust Infrastructure se ejerce. Alrededor del AgencyDomain, el libro define un paradigma (**el Mundo Agentivo** — *post-aplicaciones*), una arquitectura formal (**cuatro capas con responsabilidades distintas**, organizadas en topología paralela), un conjunto de primitivas técnicas canónicas (**Botlets**, **Capabilities**, **Trust Infrastructure**) y un modelo bidimensional para situar a cualquier actor en el mercado de IA (**la cadena de valor de IA** — once eslabones × cuatro profundidades).

El libro es **agnóstico a productos**. Las construcciones formales aquí descritas admiten múltiples implementaciones. La **implementación de referencia pública** —Vergis— se desarrolla en el Capítulo 9.

## Estructura

| Capítulo | Contenido |
|---|---|
| **Prólogo** | *(por completar)* |
| **Prefacio** | Origen del libro · quién debe leerlo · cómo está organizado · términos en inglés |
| **1 · La Línea Nadella** | La pregunta canónica · Agéntico vs Agentivo · los CEOs · por qué importa estratégicamente |
| **2 · El Mundo Agentivo** | Las consecuencias del cruce · transformación organizacional · la nueva economía de la información · datos del campo |
| **3 · Bounded Concerns Architecture** | El estado pre-agentivo · tres capas y siete separaciones · la séptima separación Procedural/Agentic · mapping al Mundo Agentivo |
| **4 · Arquitectura Agentiva** | Las cuatro capas en topología paralela · **tres tiempos del agente** (Preparación · Atención · Ingeniería) · interfaz Capa 2 ↔ Capa 3 vía `MCP` · Trust Infrastructure transversal · principio Agent First · GUI generada on-the-fly · **composición de la Capa 1** (shell · vista · operación · **PI multi-vista y drill-through**) · **Faceta vs Botlet** |
| **5 · Primitivas** | AgencyDomains (con Capa 3 distribuida + portabilidad) · Botlets (con madurez + seed/emergente + **proto-Botlet · manifestación · temporalidad** + Botler genérico) · Capabilities (**estricta a Capa 2** + localidad + certificación regulatoria + **portabilidad · feature · Conector · Plantilla**) · Trust Infrastructure (con continuidad operacional + **contrato declarativo de calidad**) · Asistente vs Agente Autónomo · **Facetas (sexta primitiva — Capa 1) · interacción declarada acotada** · **Agentlets (octava primitiva — juicio de rutina empaquetado)** |
| **6 · Mercado** | Cadena de valor de IA · profundidades y arquetipos · deep-dives por eslabón · mundo de carbono |
| **7 · Aplicaciones canónicas** | Conocimiento en tiempo real · Kimball Barnizada · BI conversacional |
| **8 · Operación** | Trust Infrastructure operacionalizada · CRUDLEX · políticas · continuidad de negocio operacional |
| **9 · Vergis** | La implementación de referencia · nota de alcance del canon · esquema Vergis · Botler · Mira · qué incluye · production grade · modelo de adopción · catálogo común y efectos de red |
| **Epílogo** | Frontera de evolución · cuatro fronteras (cognición no-LLM · federación · mundo de carbono · horizonte institucional) · ensayo de las generaciones del Botlet |
| **Apéndices** | Glosario · referencias · colofón |


<!-- FIG:g01-lamina-indice -->
![Lámina-índice · los cuatro pilares de la propuesta](figuras/g01-lamina-indice.png)


## ¿Quién debe leer este libro?

Este libro está dirigido a:

- **Arquitectos de sistemas** que diseñan o evalúan plataformas agentivas y necesitan un marco común para razonar sobre separación de responsabilidades, gobernanza y resiliencia.
- **CTOs y líderes técnicos** que deben tomar decisiones de stack agentivo en horizonte de tres a cinco años.
- **Estrategas y consultores** que asesoran a empresas en su tránsito hacia el Mundo Agentivo.
- **Investigadores y académicos** interesados en la formalización de la arquitectura agentiva como categoría de estudio.
- **Constructores de productos** que quieren situar su contribución en una cadena de valor más amplia que su producto particular.

El libro es introductorio en el sentido de que no asume conocimiento previo de implementaciones específicas, pero sí asume familiaridad básica con sistemas distribuidos, modelos de lenguaje y operación de sistemas en producción.

## Cómo citar

> Obach-Renner, César. *AgencyDomains: arquitectura del Mundo Agentivo*. Borrador de desarrollo v0.6. GegoLabs, 2026.

## La trilogía

Este libro es el volumen **III** de la **Trilogía del Mundo Agentivo**. El
tránsito que ocupa a la trilogía es uno solo: del mundo donde las personas
abren aplicaciones para trabajar, al mundo donde los agentes de IA son la
interfaz del trabajo. Los tres volúmenes responden, en orden, las tres
preguntas de ese tránsito — y cada uno se lee completo por sí solo:

**I · La Empresa en Tiempo Real — Mundo Agentivo**
¿Hacia dónde vamos? — **el destino.** Para quien quiere ver el mundo al otro
lado de la transición: cómo se trabaja, se decide y se compite cuando la
empresa opera en tiempo real — contado en sus cuatro caras.

**II · AURA — Camino Agentivo**
¿Por dónde? — **la ruta.** Para quien tiene que hacer el cruce: líderes y
asesores de la transformación. Sus cinco especificaciones son instrumentos
autónomos para la era agentiva — cada una se usa por separado, sin necesidad
del resto del libro:

| Spec | ¿Qué es? | Usada sola, ¿qué te da? |
|:---------|:----------------------------|:----------------------------|
| **IRIS** | Un modelo de madurez de inteligencia organizacional | Mide dónde está tu organización en el camino de los datos a la acción |
| **MOTOR** | Un modelo de madurez de automatización organizacional | Mide cuán avanzada está tu organización en automatización de procesos |
| **Data Canon** | La evolución del modelo de gestión descentralizada de datos (Data Mesh) | Define cómo se gobiernan los datos de la organización |
| **Wingmap** | La evolución de la gestión de procesos (BPM / *process mining*) | Reconstruye procesos y flujos de información sin entrevistas |
| **Casos de Uso** | Un marco de portafolio, ilustrado con 100 casos de uso y 30 soluciones de valor | Prioriza por dónde empezar, según tu madurez |

**III · AgencyDomains — Arquitectura Agentiva** *(este libro)*
¿Cómo llegamos? — **el vehículo.** Para arquitectos, CTOs y constructores de
plataformas agentivas: la especificación formal del Mundo Agentivo.

**Vergis — Tecnología Agentiva** *(no es un libro: es código)*
¿Con qué arranco hoy? — **las llaves.** Para quien quiera empezar a hacer todo
esto realidad: la implementación de referencia de la arquitectura, código
abierto, en <https://github.com/gegolabs/vergis>.

Empieza por **La Empresa en Tiempo Real** si necesitas convencerte — o convencer a alguien — de
que el tránsito va en serio; por **AURA** si te toca liderarlo; por
**AgencyDomains** si te toca construirlo; por **Vergis** si quieres verlo
funcionando. La trilogía completa vive en <https://agencydomains.org>.

## Licencia

Este libro se publica bajo **GNU Free Documentation License v1.3** (propuesta). El lector puede copiar, distribuir y modificar la obra bajo los términos de la licencia. La sección invariante es el Prefacio.

El motivo de la apertura de licenciamiento es deliberado: la Arquitectura Agentiva pretende establecer una categoría que sirva al ecosistema completo, no a un proveedor particular. Al adoptarla y desarrollarla, otras empresas, investigadores y constructores la enriquecen y consolidan como estándar de facto. Esto sirve al campo y refuerza simultáneamente la autoridad de quienes la acuñaron.

## Información de contacto

- **Sitio web:** <https://agencydomains.org>
- **Repositorio:** <https://github.com/gegolabs/agencydomains.org>
- **Errata y comentarios:** <https://github.com/gegolabs/agencydomains.org/issues>
