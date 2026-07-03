# Prefacio

*Por César Obach-Renner · Julio 2026*

---

Después de dieciocho meses observando cómo la industria construía agentes de IA — algunos como capricho de demo, otros como pilotos enterprise que morían al pasar a producción —, sinteticé una arquitectura formal para el problema. La llamo **Arquitectura Agentiva**. Este libro es su especificación.

Llegué al problema por la vía menos elegante: lo necesitaba. En 2025 empecé a construir, dentro de mi empresa, un portafolio de productos donde humanos y agentes debían coexistir como ciudadanos digitales de primera clase. Pronto descubrí que la categoría no existía con la madurez necesaria para sostener ese diseño. Había mucho lenguaje suelto — *"agentic AI"*, *"AI copilots"*, *"AI agents"*, *"autonomous workflows"* —, mucho marketing y poca arquitectura. La industria nombraba el horizonte; pero no había una especificación común del sustrato técnico, ni un vocabulario compartido para discutirlo.

Frente a eso me ofrecía dos caminos: improvisar sobre lo disperso o construir el marco que mi empresa necesitaba. Opté por el segundo. Lo construí primero como notas internas; después como documentos canónicos del proyecto; después como la columna vertebral del portafolio entero. En algún momento se hizo evidente que el resultado tenía valor más allá de mi empresa — que cualquier organización que esté construyendo en este horizonte enfrenta el mismo problema y necesita el mismo marco.

Este libro es la formalización de ese marco. Define el paradigma (**el Mundo Agentivo**), una arquitectura formal de cuatro capas, las primitivas técnicas que las habitan (**Botlets**, **Capabilities**, **AgencyDomains**), una infraestructura de confianza transversal (**Trust Infrastructure**) y un modelo de mercado bidimensional (**la cadena de valor de IA**). El propósito no es convencer al lector de adoptar mi implementación particular. El propósito es ofrecer al ecosistema completo un lenguaje común para razonar sobre sistemas agentivos productivos.

Tengo claro de dónde vengo. Hace casi veinte años escribí un libro similar para otra categoría que entonces empezaba a tomar forma — *SOAr: El concepto* (2008), una formalización de Arquitectura Orientada a Servicios para integración empresarial. Aquel trabajo nació también de un proyecto real donde la metodología no existía, así que la creé y la documenté. Lo que aprendí entonces, y aplico aquí, es que las categorías técnicas se establecen no cuando alguien las inventa, sino cuando alguien las **escribe con disciplina suficiente como para que otros las adopten**. Este libro es ese intento.

## ¿Quién debe leer este libro?

Este libro está dirigido a quienes están construyendo, evaluando o gobernando sistemas agentivos productivos.

Si es **arquitecto de sistemas** o **CTO**, encontrará un marco común para razonar sobre separación de responsabilidades, gobernanza, primitivas técnicas y posicionamiento de stack en horizonte de tres a cinco años. Si es **estratega de producto** o **consultor**, encontrará un mapa de mercado bidimensional para situar a cualquier actor — propio o ajeno — en la cadena de valor de IA. Si es **investigador** o **académico**, encontrará una formalización razonablemente rigurosa de una categoría aún en consolidación.

El libro es introductorio en el sentido de que no asume conocimiento previo de implementaciones específicas. Pero asume familiaridad básica con sistemas distribuidos, modelos de lenguaje y operación de sistemas en producción. No es un manual de implementación — es la especificación que un manual debería respetar.

## ¿Cómo está organizado este libro?

El libro avanza del paradigma a la implementación, en una secuencia donde cada parte se apoya en la anterior:

- **El paradigma** — La Línea Nadella (la pregunta) · El Mundo Agentivo (las consecuencias).
- **La Arquitectura Agentiva** — cuatro capas distintas · Trust Infrastructure transversal · Agent First (principio rector).
- **Las primitivas (siete)** — AgencyDomain · Botlet · proto-Botlet (+ manifestación + temporalidad) · Capability (cognitiva, Capa 2) · Trust Infrastructure · Asistente vs Agente Autónomo (primitiva-eje) · Faceta (Capa 1).
- **El posicionamiento de mercado** — Cadena de valor de IA (11 × 4) · Observabilidad · Mundo de carbono.
- **Las aplicaciones** — Conocimiento en tiempo real (caso canónico: Kimball Barnizada · BI conversacional).
- **La operación** — Trust Infrastructure operacionalizada (políticas · CRUDLEX · log).
- **La implementación de referencia** — Vergis (Capítulo 9).
- **El epílogo** — frontera de evolución (cognición no-LLM · federación · mundo de carbono · AgentNation).

El recorrido encadena los capítulos así: **La Línea Nadella** (la pregunta) → **El Mundo Agentivo** (las consecuencias) → **la Arquitectura Agentiva** (las cuatro capas) → **las primitivas** que las pueblan → **el posicionamiento de mercado** → **la aplicación canónica** → **la operación** → **Vergis**, la implementación de referencia → **el epílogo**. El glosario al final fija el vocabulario canónico.

## Sobre los términos en inglés

Buena parte del vocabulario técnico de esta categoría nace en inglés y carece de traducciones al español que sean a la vez precisas y reconocidas: *agent*, *agentic*, *agentive*, *runtime*, *guardrails*, *tool*, *prompt injection*, entre otros. Este libro adopta el original en inglés cuando la traducción sería forzada o cuando el término ya circula con autoridad en el campo. Cuando una traducción al español sí captura el concepto sin pérdida — *capa*, *modelo*, *gobernanza*, *cognición* —, se utiliza esa.

Los conceptos canónicos acuñados en este libro — **Arquitectura Agentiva**, **Línea Nadella**, **AgencyDomains**, **Botlet**, **Capability**, **Trust Infrastructure**, **Mundo Agentivo** — se mantienen en su forma original a través de toda la obra, capitalizados, como nombres propios. Su definición precisa vive en el glosario al final del libro.

A medida que la categoría madura en regiones de habla hispana, traducciones consensuadas pueden emerger. Si así ocurre, futuras ediciones las recogerán. Por ahora, la prioridad es no romper la trazabilidad del concepto entre comunidades.

