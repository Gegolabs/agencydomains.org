## Trust Infrastructure

Hay una asimetría operativa que cualquier organización que ha intentado llevar IA agentiva a producción reconoce con incomodidad: lo que funciona en piloto rara vez funciona en producción enterprise. Un piloto controlado, con un puñado de usuarios sofisticados, supervisado de cerca por el equipo que lo construyó, puede ejecutarse exitosamente sin gobernanza explícita. Los pilotos demuestran capacidad técnica, no aptitud operativa. La distancia entre los dos es exactamente lo que esta sección desarrolla.

La cifra que más preocupa al campo en 2026 es la proyección de Gartner: más del cuarenta por ciento de los proyectos de IA agentiva serán cancelados antes de fines de 2027. Las razones que Gartner identifica son tres: costos imprevistos, valor de negocio poco claro, y controles de riesgo inadecuados. La tercera razón — controles de riesgo inadecuados — es la que conecta directamente con el contenido de esta sección. Las organizaciones cancelan proyectos no porque la tecnología no funcione, sino porque la organización no puede defender lo que la tecnología hace cuando algo sale mal. La diferencia entre un piloto exitoso y un proyecto cancelado es típicamente la madurez de la **infraestructura de confianza**.

Trust Infrastructure es el conjunto de propiedades transversales que permiten a una organización **confiar en que sus agentes operen con autonomía sin perder control**. No es una capa adicional de la Arquitectura Agentiva — es una propiedad que atraviesa las cuatro capas existentes (Interacción, Cognición, Autonomía, Acceso) y se ejerce en distintos puntos según el pilar específico. Esta sección desarrolla los cinco pilares con el detalle que el lector arquitecto necesita para diseñar y el lector ejecutivo necesita para evaluar.

> *La Trust Infrastructure no es lo que se agrega después de que el agente funciona. Es lo que separa pilotos de producción.*

La urgencia de Trust Infrastructure ya no es solo arquitectónica. Es regulatoria. Singapore IMDA publicó en enero de 2026 el primer framework estatal de gobernanza específicamente para IA agentiva. La Unión Europea hace lo propio con el EU AI Act. NIST con su AI Risk Management Framework. ISO/IEC con la norma 42001. La pregunta ya no es si los reguladores exigirán infraestructura de confianza — es si la organización puede demostrarla auditablemente cuando se la pidan. Las organizaciones que no la tengan operativa enfrentarán, en el horizonte de los próximos veinticuatro meses, una decisión binaria: invertir aceleradamente para alcanzar conformidad, o suspender operaciones agentivas en mercados regulados.

### Los cinco pilares

<!-- FIG:g30-cinco-pilares -->
![Los cinco pilares de Trust Infrastructure](figuras/g30-cinco-pilares.png)

Cinco pilares constituyen Trust Infrastructure. Cada uno responde una pregunta operativa específica que la organización necesita poder responder cuando alguien — un auditor, un regulador, un cliente — la cuestione.

| Pilar | Pregunta que responde |
|---|---|
| **Gobernanza** | ¿Quién decide qué puede hacer el agente, bajo qué condiciones? |
| **Auditoría** | ¿Qué hizo el agente, cuándo, por qué, sobre qué datos? |
| **Validación** | ¿Es correcto lo que el agente está a punto de hacer (o decir)? |
| **Resiliencia** | ¿Qué pasa cuando algo sale mal — el sistema se detiene o sigue? |
| **Transparencia** | ¿Cómo lo entiende un humano si necesita intervenir? |

Cada pilar se ejerce en una o más capas y se materializa con mecanismos concretos. Las próximas cinco subsecciones desarrollan cada pilar con detalle. Después mostramos el mapa transversal — qué pilar opera principalmente en qué capa — y cerramos con la lectura regulatoria del campo.

### Pilar 1 — Gobernanza

El pilar de Gobernanza define el conjunto de mecanismos mediante los cuales la organización establece **qué** puede hacer el agente, **bajo qué condiciones** y **con qué nivel de supervisión**. Es el pilar más visible para quien viene del mundo del IT tradicional, porque tiene el equivalente más directo en mecanismos conocidos — IAM, SSO, RBAC. Pero la Gobernanza agentiva es estructuralmente distinta de la gobernanza tradicional, y confundir las dos es fuente recurrente de proyectos fallidos.

La Gobernanza tradicional pregunta *"¿quién puede ver qué datos?"*. El sujeto del control es un humano con identidad estable; el objeto es un recurso discreto. La pregunta es estática: los permisos rara vez cambian, y cuando cambian es por evento humano explícito (alguien fue contratado, alguien fue promovido, alguien dejó la empresa). La Gobernanza agentiva pregunta *"¿qué puede hacer un agente, bajo qué condiciones?"*. El sujeto es un agente que actúa autónomamente; el objeto es una secuencia de acciones que el agente puede ejecutar con grados variables de impacto. La pregunta es dinámica: las condiciones cambian con el contexto, el momento, el estado del sistema. Las herramientas de Gobernanza tradicional — IAM, SSO, RBAC — son insuficientes para este modelo. Funcionan bien para sujetos humanos con identidad estable; no funcionan para agentes que actúan continuamente con grados variables de autonomía.

Los mecanismos canónicos de la Gobernanza agentiva son cuatro. Las **políticas configurables** son reglas declarativas — no código embebido — que definen qué tools puede invocar el agente, sobre qué datos, en qué horarios, con qué umbrales de impacto. La separación entre política (declarativa) y código (imperativo) es importante: las políticas deben poder cambiarse sin redeploy del sistema, deben poder versionarse independientemente del código, deben poder ser auditadas sin requerir review del código. Los **permisos CRUDLEX** — Create, Read, Update, Delete, List, Execute — son modelo granular de permisos sobre tools y datos, aplicable por usuario, agente o contexto. La operacionalización completa de CRUDLEX vive en el Capítulo 8. La **aprobación humana para operaciones críticas** establece que el agente puede ejecutar operaciones de bajo impacto autónomamente, pero las de alto impacto se detienen y solicitan aprobación. La definición de "alto impacto" es política, no técnica — la organización decide qué umbrales activan aprobación. El **registro de IA** es inventario formal de qué agentes están activos, qué Capabilities aplican, qué tools tienen autorizados, quién los aprobó. Es lo que un regulador verá cuando audite, y lo que la organización debe mantener actualizado y accesible.

Los datos del campo respecto a Gobernanza son crudos — el Capítulo 2 los documenta. La historia que cuentan es consistente: la mayoría de las organizaciones sabe que el problema existe pero no ha invertido lo suficiente para resolverlo, y los reguladores están en camino de forzar la inversión.

### Pilar 2 — Auditoría

El pilar de Auditoría define la capacidad de reconstruir, después del hecho, **qué hizo el agente, cuándo, por qué y sobre qué datos** — con suficiente fidelidad para análisis forense, cumplimiento regulatorio o disputa contractual. Es el pilar que la organización necesita cuando algo sale mal: si un agente tomó una decisión que produjo un mal resultado, o ejecutó una acción que un cliente cuestiona, o realizó operación que el regulador quiere examinar, la organización necesita poder reconstruir auditablemente lo que pasó.

Los mecanismos canónicos de la Auditoría son cuatro. El **append-only log inmutable** es el componente central: toda acción del agente queda registrada en un log que no admite modificación retroactiva. Solo se agrega — nunca se edita ni se elimina. El log típicamente está encadenado criptográficamente: cada registro contiene el hash del anterior, formando una cadena verificable donde una alteración retroactiva sería inmediatamente detectable. El **trace de cada acción** registra identidad del agente, capability invocada, tool ejecutado, parámetros, resultado, timestamp, contexto. Cada acción genera un registro completo que reconstruye el estado del sistema en el momento de la decisión. El **lineage de decisiones** es la cadena causal de razonamiento que llevó a una acción particular: qué información consultó el agente, qué Capabilities aplicó, qué heurísticas usó, qué cognición evaluó. Sin lineage, una acción aparece como evento aislado; con lineage, aparece como resultado de un proceso de razonamiento reconstruible. El **identity tagging por acción** asegura que cada acción es atribuible inequívocamente a un agente identificable, no a "el sistema" o a "la IA". La distinción importa para responsabilidad: cuando algo sale mal, debe poder identificarse qué agente específico fue responsable, y por extensión, quién lo configuró, quién aprobó sus capacidades, qué política cubría su operación.

ISACA — la asociación profesional de auditoría — destaca que la IA agentiva presenta un desafío creciente para funciones de auditoría porque sus procesos de decisión carecen de trazabilidad clara cuando el sistema no fue diseñado con auditoría en mente. La observación es importante porque captura una propiedad estructural: un agente que combina cognición probabilística (LLM) con tools determinísticos toma decisiones cuyo camino es difícil de reconstruir si el log no está diseñado para hacerlo. Un log que solo registra "el agente ejecutó X tool con Y parámetros" no es suficiente — necesita registrar también "porque la cognición evaluó Z razonamiento basándose en W contexto". La Auditoría agentiva exige diseño explícito desde el inicio. No emerge naturalmente de una arquitectura agentiva — se construye con disciplina desde el inicio.

> *La auditoría agentiva exige diseño explícito. No emerge naturalmente de una arquitectura agentiva — se construye con disciplina desde el inicio.*

### Pilar 3 — Validación

El pilar de Validación define la capacidad de verificar que la respuesta o acción del agente sea **correcta** antes de que afecte al mundo. Es el pilar más reciente en madurar como categoría — la industria de validación de IA es de los últimos tres años — y, simultáneamente, el más crítico para casos de uso donde el costo del error es alto.

La diferencia con la validación tradicional es importante. La validación tradicional verifica formatos: ¿el JSON es válido? ¿la fecha tiene el formato correcto? ¿el monto es número? La validación agentiva verifica **semántica**: ¿el agente está diciendo la verdad? ¿está actuando dentro de los límites razonables del dominio? ¿está exponiendo datos que no debería? La validación tradicional opera sobre estructura; la validación agentiva opera sobre significado.

Los mecanismos canónicos de Validación son cinco. La **detección de alucinaciones** verifica que las afirmaciones factuales del agente sean consistentes con las fuentes consultadas. Es área activa de investigación; mecanismos contemporáneos incluyen self-consistency (preguntar lo mismo de varias maneras y comparar respuestas), retrieval-augmented verification (consultar fuentes autoritativas antes de afirmar), y model-as-judge (un segundo modelo evalúa la respuesta del primero). La **validación de respuestas estructuradas** verifica que las salidas con schema — JSON, XML, tablas — cumplan el contrato esperado antes de emitirlas. Es la validación más directa, equivalente a la validación tradicional pero aplicada sobre salidas que el modelo generó. La **prompt injection prevention** detecta intentos de manipulación a través de inputs maliciosos disfrazados como datos legítimos. Un usuario que intenta inyectar instrucciones en un campo de comentarios para que el agente las ejecute como si fueran instrucciones legítimas es ataque común que la validación debe detectar. Productos como Lakera y Lasso Security productizan precisamente este mecanismo. La **DLP** — Data Loss Prevention — detecta automáticamente datos personales (PII), información financiera sensible o material clasificado en lugares donde no deberían aparecer. Si un agente está a punto de incluir un número de seguridad social en una respuesta a un usuario externo, la DLP lo detecta y bloquea. La **tokenización** reemplaza datos sensibles por tokens antes de que lleguen al modelo. Permite que el agente razone sobre los datos sin exponerlos al proveedor de cognición externo. La organización mantiene el mapeo token-a-dato en almacén con seguridad reforzada — típicamente HSM (Hardware Security Module) o servicio dedicado.

Informatica formula con precisión la transición que la Validación representa: *"Because agents act without human approval loops, the data they use must be fully trusted, verified, and monitored."* La frase captura algo importante. En sistemas tradicionales, un humano supervisa cada operación importante antes de ejecutarla — es el último loop de validación, hecho de carne. En sistemas agentivos, ese loop humano no existe en cada operación — solo en operaciones críticas que escalan. La Validación tiene que **suplir el loop humano** para todas las demás operaciones, asegurando que lo que el agente está a punto de hacer es correcto antes de hacerlo. Sin esa suplencia, el sistema se queda corto: o ejecuta acciones incorrectas, o requiere supervisión humana en cada operación, anulando la productividad del agente.

La validación de la spec de un componente especialista admite un patrón estructural que merece nota: la **validación por delegación**. El runtime genérico de Capa 3 (el Botler) **hace valer** la validación de la spec de un Botlet sin entender su dominio — orquesta el punto de validación que el Botlet o su proto-Botlet provee, le entrega el contexto genérico que controla (catálogo de Capabilities, identidad, políticas del AgencyDomain) y audita el veredicto en el append-only log. El juicio de qué hace válida a la spec vive en el especialista; el runtime exige y registra la validación sin ejecutarla con conocimiento de dominio. El desarrollo de este patrón vive en el capítulo de Botlets; aquí solo se enlaza el principio con el pilar de Validación.

### Pilar 4 — Resiliencia

El pilar de Resiliencia define la garantía de que el sistema sigue operando — y la organización conserva control — cuando algo sale mal. Es el pilar más cercano a las prácticas de ingeniería de software tradicional — el campo de DevOps y SRE ha desarrollado patrones de resiliencia durante quince años — pero adaptado a las particularidades del sistema agentivo.

Los mecanismos canónicos son cinco. La **garantía de fallback** es la propiedad fundamental que ya describimos en Capítulo 5 §2 (Botlets §4): si un Botlet falla catastróficamente, la cognición ejecuta la tarea manualmente; si la cognición falla, la operación escala al humano. Esta garantía es lo que distingue al sistema agentivo conforme a esta spec de cualquier "automatización con IA" frágil. El **manejo de errores estructurado** asegura que los errores son tipificados, accionables, propagados con contexto suficiente para que el siguiente nivel decida. Un error que dice "algo falló" no es manejo estructurado; un error que dice "API X devolvió código Y, parámetro Z, en operación W del agente V" es manejo estructurado. El **sandboxing** asegura aislamiento de ejecución de Botlets y código generado, con límites estrictos sobre qué pueden tocar. Detalle en la sección de Botlets. Los **circuit breakers** detienen y notifican cuando un agente o Botlet falla repetidamente, antes de seguir consumiendo recursos. Es patrón clásico de resiliencia adaptado al contexto agentivo: si un Botlet ha fallado N veces consecutivas, se detiene su ejecución automática y se escala al humano para revisión. El **rate limiting** establece límites configurables sobre frecuencia de invocaciones, tanto a la cognición (controlar costo) como a tools externos (proteger sistemas downstream). Sin rate limiting, un agente con un loop mal diseñado puede agotar los recursos del sistema en horas.

El principio de no-detención que la spec garantiza — declarado en Capítulo 5 §2 — es lo que permite a la organización delegar operación a agentes con la confianza de que un fallo aislado no detiene el negocio. La resiliencia es lo que hace esa confianza razonable.

#### Continuidad de negocio operacional vs garantía de fallback agéntico

La garantía de fallback que el Pilar 4 describe supone **cognición disponible**: cuando el Botlet falla por cambio de ambiente, la cognición rescata. Esta supuesto se cumple en la mayoría de los escenarios — la cognición vive en cloud altamente disponible y los Botlets fallan ocasionalmente por cambios menores que la cognición resuelve sin esfuerzo. Pero en sistemas productivos físicos — locales sin red, hardware caído, energía cortada — **la cognición tampoco está disponible**, y la continuidad operacional necesita un protocolo adicional que la garantía de fallback agéntico no cubre.

La spec distingue por tanto **dos mecanismos complementarios** que resuelven escenarios distintos:

**Garantía de fallback agéntico** — la cognición ejecuta cuando el Botlet falla por cambios de ambiente. Es propiedad de la Arquitectura Agentiva, codificada en la spec del Botlet (§2). Cubre la inmensa mayoría de los fallos: el ambiente cambia, el Botlet detecta el cambio, la cognición rescata. Esta es la propiedad que produce la trayectoria de madurez del Botlet desde junior hasta senior.

**Continuidad de negocio operacional** — protocolos manuales documentados para cuando el Botlet senior cae por causas exógenas y la cognición tampoco está disponible. Es propiedad operacional, equivalente a la que cualquier negocio tradicional ya tiene cuando se le cae el sistema (corte de energía, hardware caído, red catastrófica, proveedor crítico abajo). No depende de la spec agentiva — depende del protocolo del cliente.

Las dos no se excluyen: se complementan. La primera resuelve el aprendizaje del Botlet y la mayoría de los fallos operativos. La segunda cubre el residuo exógeno catastrófico que ningún sistema previene completamente.

#### Conexión con la madurez del Botlet

La conexión entre los dos mecanismos y la trayectoria de madurez del Botlet (§2) merece tratamiento explícito porque revela una propiedad estructural del sistema agentivo:

**La garantía de fallback agéntico es lo que produce la madurez.** Cada vez que el Botlet falla por un cambio de ambiente, la cognición rescata, regenera y devuelve operación — y esa regeneración es justamente lo que produce la incorporación progresiva de variantes hasta alcanzar madurez senior. Sin fallback agéntico, el Botlet quedaría atrapado en su versión inicial, sin manera de aprender. **Sin fallback agéntico, el Botlet no madura.**

**La continuidad operacional, en cambio, no incide en la madurez.** Opera sobre Botlets ya maduros que caen por causas exógenas, no por aprendizaje pendiente. Cuando un Botlet senior cae porque el local sufrió corte de energía, no es problema de aprendizaje — es problema operacional que el protocolo de continuidad debe resolver (caja manual, registro en papel, conciliación posterior).

| Mecanismo | ¿Cuándo opera? | ¿Qué resuelve? | ¿Quién lo provee? |
|---|---|---|---|
| **Garantía de fallback agéntico** | Botlet junior, en aprendizaje, o senior con variante nueva | Cambios de ambiente que el Botlet no anticipó | La spec agentiva (Capa 2 + Capa 3) |
| **Continuidad de negocio operacional** | Botlet senior caído por causa exógena, sin cognición disponible | Continuidad operativa cuando ningún componente computacional opera | Protocolo del cliente (procedimiento manual documentado) |

#### ¿Por qué importa la distinción?

Sin la distinción, los planes de continuidad operacional se confunden con la promesa agéntica. Un cliente lee "garantía de fallback" en la documentación del producto y asume que cubre cualquier fallo, incluyendo cortes de energía. Cuando ocurre el corte y descubre que el sistema no opera, atribuye el fallo a la arquitectura agentiva — y concluye que "el sistema falla".

Reconocer las dos propiedades como mecanismos separados pero complementarios reduce ansiedad sobre offline y deja claro qué resuelve la arquitectura y qué resuelve el protocolo operacional del cliente. La conversación con el cliente cambia: ya no se promete que "nunca pasa nada"; se promete que "los fallos por aprendizaje los maneja la arquitectura, los fallos exógenos los maneja el protocolo de continuidad — y ambos están documentados".

La distinción conceptual entre fallback agéntico y continuidad operacional es la sede de esta sección. Su operacionalización —el protocolo de campo por sitio, los modos de degradación y las marcas de log con que se registra la transición a continuidad— vive en el Capítulo 8, donde se desarrollan las exigencias operativas (todas **MUST**, incluida la trazabilidad de la transición a modo continuidad).

### Pilar 5 — Transparencia

El pilar de Transparencia define la capacidad del humano de entender, en tiempo real, **qué está haciendo el agente y por qué** — con detalle suficiente para intervenir si es necesario. Es el pilar que conecta los otros cuatro: la Gobernanza define qué puede hacer, la Auditoría registra qué hizo, la Validación verifica qué está por hacer, la Resiliencia asegura que sigue operando — la Transparencia asegura que un humano puede entender todo lo anterior.

Los mecanismos canónicos son cinco. La **observabilidad completa** entrega tracing end-to-end de cada operación, métricas de latencia, costo, calidad, y eventos estructurados. Es el equivalente agentivo de los sistemas de observabilidad tradicionales (Datadog, New Relic, Splunk) adaptados a las particularidades del sistema agentivo. Las **métricas operativas** miden tasa de éxito de Botlets, frecuencia de regeneración, latencia de cognición, consumo de tokens, errores por capa. Estas métricas son lo que un equipo de operaciones consulta diariamente para entender la salud del sistema. Los **traces consultables por humanos** aseguran que la traza de una decisión es legible por un humano técnico, no solo por otra máquina. Esto importa para auditoría reactiva: cuando algo salió mal y un humano necesita reconstruir qué pasó, debe poder leer los traces directamente, no depender de un sistema de análisis automatizado intermedio. Las **alertas proactivas** notifican cuando el agente detecta que está cerca de un límite, fallando con frecuencia inusual, o tomando decisiones de alto impacto. La proactividad importa: el sistema no espera a que el humano consulte para informar problemas; informa antes de que se vuelvan críticos. Los **dashboards de gobernanza** dan vista al responsable humano: qué agentes están operativos, qué hacen, con qué éxito, sobre qué recursos. Es interfaz de control para la persona que gobierna el sistema.

La observabilidad de IA es categoría madura del mercado. Productos como Langfuse, LangSmith, Helicone, Arize AI, Braintrust, Weights & Biases cubren distintas capas. La transparencia agentiva no exige construir estos productos desde cero — exige integrarlos coherentemente con los demás pilares de Trust Infrastructure. La organización adopta los productos que mejor se ajusten a su stack y los integra con el resto de la infraestructura.

### Contrato declarativo de calidad

Los pilares de **Resiliencia** y **Auditoría** se ejercen mejor cuando lo que la organización debe auditar y sostener está **declarado**, no enterrado en código. El **contrato declarativo de calidad** es el mecanismo que lo habilita: cualquier Botlet conforme MAY declarar sus atributos de calidad como propiedades estructuradas, no como código embebido. Trust Infrastructure los lee de manera uniforme — sin acoplarse a la implementación de cada Botlet.

Los atributos canónicos del contrato son cinco. La **Frescura** declara la antigüedad máxima admisible de los datos que el Botlet consume. El **SLA** declara la latencia esperada extremo a extremo, expresada como percentiles (`p50`, `p99`). La **Política de degradación** declara el comportamiento ante fallo — `refuse` (rechaza y no entrega), `warn_and_show` (advierte y muestra de todas formas), `show_last_valid` (entrega el último resultado válido conocido), `agentic_fallback` (escala a la cognición). La **Audiencia** declara la política `RLS`/`CRUDLEX` aplicable a quién puede consumir la manifestación. La **Política de refresh** declara cómo se renueva — `on-demand`, `scheduled` o `push`.

Declarados así, estos atributos se vuelven mecanismos transversales que sirven a dos pilares a la vez. Para la **Resiliencia**, la Política de degradación y la Política de refresh son configuración auditable y no lógica frágil dispersa por la implementación: el runtime sabe qué hacer ante fallo y cuándo renovar sin leer el cuerpo del Botlet, y la Frescura y el SLA dan umbrales explícitos contra los cuales medir si un resultado sigue siendo confiable. Para la **Auditoría**, los cinco atributos permiten que Trust Infrastructure los audite uniformemente, los curse por **políticas globales** del AgencyDomain (una política puede endurecer la Frescura mínima o vetar `warn_and_show` para una clase de operación) y los reporte como **métricas estándar** comparables entre Botlets. La organización no inventa un formato por Botlet; declara contra un vocabulario común que el append-only log y los dashboards de gobernanza ya entienden.

### Mapa transversal — ¿qué pilar opera en qué capa?

<!-- FIG:g31-pilares-x-capas -->
![Mapa transversal · qué pilar opera en qué capa](figuras/g31-pilares-x-capas.png)

Los cinco pilares se ejercen en distintas capas de la Arquitectura Agentiva, como sintetiza la figura anterior.

Tres lecturas del mapa son útiles. La primera: **la Capa 4 concentra la mayor carga**. Gobernanza, Auditoría y Validación final operan principalmente en Capa 4. Es coherente con su naturaleza: la Capa 4 es donde la cognición se convierte en acción real, y por tanto donde se ejerce el control. Las decisiones de qué se puede hacer, qué se está por hacer, y qué se hizo, todas pasan por Capa 4. La segunda: **la Resiliencia vive en la Capa 3**. La continuidad operativa se sostiene en la autonomía persistente del agente, su Botler, sus Botlets con fallback. Cuando el sistema agentivo "sigue funcionando" a pesar de que algún componente falló, esa continuidad la asegura la Capa 3. La tercera: **la Transparencia es propiedad transversal**. No vive en una capa específica — atraviesa todas. Esto exige diseño explícito de instrumentación en cada capa, no agregada al final como capa adicional. Cada capa emite eventos, cada capa tiene métricas, cada capa contribuye al log de auditoría.

### Trust Infrastructure y los reguladores

La infraestructura de confianza no es decisión solo arquitectónica. Es decisión de **conformidad regulatoria** ante un marco creciente de regulación específica para IA agentiva. Los principales frameworks que el campo enfrenta a inicios de 2026 son:

El **EU AI Act** de la Unión Europea, vigente con aplicación gradual entre 2024 y 2026. El **NIST AI Risk Management Framework** de Estados Unidos, vigente como framework voluntario pero adoptado por industrias reguladas. La **ISO/IEC 42001**, publicada en 2023 con certificación voluntaria pero creciente adopción enterprise. El **MGF — Model AI Governance Framework for Generative AI** de Singapore IMDA, publicado en enero de 2026 y notable por ser el primer framework estatal específicamente para IA agentiva (el nombre conserva la IA generativa; el cuerpo gobierna agentes). Los **lineamientos del World Economic Forum** sobre onboarding y gobernanza de agentes. Las **guías de la NACD** — National Association of Corporate Directors — para boards corporativos.

Patrón común: todos estos frameworks exigen — en términos formalmente distintos pero funcionalmente equivalentes — los cinco pilares descritos en esta sección. No es coincidencia. La lista de pilares emerge del análisis funcional del problema, no de imitación a un regulador particular. Cualquier regulador serio que analice los riesgos del sistema agentivo llega a una lista similar: gobernanza, auditoría, validación, resiliencia, transparencia. La ecuación es estructural.

La consecuencia operativa para la organización es que invertir en Trust Infrastructure no es solo decisión arquitectónica — es **inversión regulatoria**. Una organización que adopta los cinco pilares correctamente se posiciona para satisfacer los cuatro frameworks principales simultáneamente — EU AI Act, NIST AI RMF, ISO/IEC 42001, IMDA MGF —, porque convergen en exigencias funcionales similares. Una organización que los descuida queda expuesta a los cuatro a la vez, sin defensa estructural.

### Conformidad

Una implementación de Trust Infrastructure conforme a esta especificación debe satisfacer:

| Requisito | Nivel |
|---|---|
| Los cinco pilares ejercidos en alguna capa | **MUST** |
| Append-only log inmutable de toda acción | **MUST** |
| Permisos CRUDLEX granulares por usuario / agente / contexto | **MUST** |
| Garantía de fallback ante fallo | **MUST** |
| Trazabilidad consultable por humanos | **MUST** |
| Detección de alucinaciones | **SHOULD** |
| Prompt injection prevention | **SHOULD** |
| DLP / tokenización de datos sensibles | **SHOULD** |
| Aprobación humana configurable para operaciones críticas | **MUST** |
| Conformidad con al menos un framework regulatorio reconocido | **SHOULD** |
| Distinción explícita entre fallback agéntico y continuidad operacional | **MUST** |
| Protocolo de continuidad operacional documentado para sistemas con presencia física | **MUST** |

### Frontera de evolución

Tres áreas activas de evolución de Trust Infrastructure merecen mención al cierre.

La **auditoría auditable** es la primera. Protocolos verificables criptográficamente que permitan a un auditor externo verificar el log sin acceso al sistema. Está en intersección con tecnologías de cómputo confidencial y zero-knowledge proofs. Cuando madure, permitirá auditoría externa sin exponer datos operativos al auditor.

El **trust scoring de agentes** es la segunda. Métricas compuestas de confiabilidad que evolucionan con el comportamiento del agente, similar al puntaje de crédito. Permitiría a la organización adoptar agentes con confianza modulada según su trust score: agentes con alto score reciben más autonomía; agentes con bajo score requieren más supervisión.

La **federación de Trust Infrastructure** es la tercera. Cuando dos AgencyDomains colaboran (federación, ver sección 1 de este capítulo), cómo sus respectivas Trust Infrastructures se reconocen y se componen. ¿La política del AgencyDomain A se aplica también a las invocaciones del AgencyDomain B? ¿Cómo se reconcilian políticas contradictorias? Es problema sin solución general en la versión 1.0 de la spec.
