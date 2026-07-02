## Botlets

Cuando un pianista aprende una pieza nueva, los primeros minutos son una experiencia consciente y costosa. El pianista mira la partitura, identifica cada nota, decide la digitación, ejecuta cada movimiento de los dedos prestando atención plena. La pieza, en esa primera lectura, es trabajo cognitivo intenso. Una hora más tarde, después de práctica deliberada, los dedos empiezan a tocar solos. El pianista todavía sigue la partitura, pero ya no tiene que decidir conscientemente cada nota — los dedos saben dónde van. Una semana después, la pieza está incorporada en la **memoria muscular**: el pianista la ejecuta sin pensar. Si en algún momento se equivoca o algo sale del esperado — un sonido raro, una digitación incómoda — la conciencia vuelve a aparecer brevemente, evalúa el problema, ajusta, y luego se retira de nuevo. La memoria muscular vuelve a tomar control.

Esta dinámica del aprendizaje motor humano no es metáfora arbitraria. Es la base neurobiológica documentada por Squire y Wixted en su trabajo de 2011 sobre los sistemas de memoria humana, ampliando trabajo previo de Larry Squire sobre las modalidades de memoria. La corteza prefrontal aprende patrones nuevos invirtiendo recursos cognitivos costosos. Los traspasa a estructuras subcorticales — el cerebelo, los ganglios basales — que los ejecutan sin intervención consciente. La corteza prefrontal se reactiva solo cuando detecta una desviación significativa que la rutina codificada no maneja. Esta arquitectura es lo que permite que el cerebro humano opere eficientemente: lo costoso se minimiza, lo barato se maximiza, y la atención consciente se reserva para cuando es realmente necesaria.

La Arquitectura Agentiva replica esta arquitectura biológica con disciplina. Lo que el cerebro hace con corteza prefrontal y memoria procedimental, el sistema agentivo lo hace con cognición LLM y Botlets. Cuando un agente enfrenta una tarea por primera vez, la cognición — Capa 2 — la procesa con los recursos costosos del LLM: razona, decide, ejecuta. Cuando la tarea se repite con frecuencia, la cognición delega la ejecución a un **Botlet** — código tradicional, no-LLM, que la cognición misma generó — que vive en Capa 3 y ejecuta sin invocar al modelo. Si el ambiente cambia y el Botlet falla, la cognición vuelve a tomar control: regenera el Botlet adaptado al ambiente nuevo o, en el peor caso, ejecuta la tarea manualmente. Lo costoso se minimiza, lo barato se maximiza, la cognición se reserva para casos genuinamente nuevos.

> *La cognición piensa una vez. El Botlet ejecuta diez mil veces.*

Esta sección desarrolla la primitiva del Botlet con el detalle que merece. La spec del Botlet es probablemente la primitiva más importante para la economía operativa de un sistema agentivo — sin Botlets, los costos de inferencia hacen inviable la autonomía continua; con Botlets bien diseñados, la organización puede operar agentes en producción a costos predecibles y estables.

### Definición

Un **Botlet** es una unidad de automatización auto-evolutiva: código tradicional, no basado en LLM, generado por un agente para ejecutar una tarea repetitiva sin invocar cognición costosa. Los Botlets son la **memoria muscular** del agente — el equivalente computacional de los gestos automatizados que un humano ejecuta sin pensar conscientemente.

Cuatro propiedades distinguen al Botlet de cualquier "macro" o "script automatizado" tradicional. La primera es que **el código del Botlet no lo escribió un humano**: lo generó la cognición del agente cuando reconoció un patrón repetitivo en su actividad. Esto importa porque la generación dinámica del código permite que el sistema adapte la automatización a cada contexto particular, sin depender de que un programador anticipe cada caso. La segunda es que el Botlet **ejecuta sin invocar cognición** durante operación normal. Una vez generado, el Botlet corre como código tradicional — Python, JavaScript, Bash, lo que sea —, independiente del modelo que lo creó. La tercera es que **se regenera automáticamente** cuando detecta que el ambiente cambió. Si el Botlet falla porque una API cambió, una estructura de datos varió, o una pantalla se renombró, la cognición regenera el Botlet adaptado al ambiente nuevo. La cuarta — y crítica — es que tiene **garantía de fallback**: si el Botlet falla catastróficamente y no puede ejecutarse, la cognición ejecuta la tarea manualmente. El proceso nunca se detiene.

La diferencia con un script tradicional es estructural. Un script tradicional que falla deja a la operación detenida hasta que un humano intervenga: alguien debe identificar el problema, modificar el script, redeployarlo, validar. Un Botlet que falla activa la cognición, que ejecuta la tarea — en ese caso particular, sin Botlet — y registra el evento para regenerar después. La organización puede **depender** del Botlet sin riesgo operativo, porque la falla del Botlet no es falla del sistema.

### El ciclo `95/4/1`

<!-- FIG:g22-ciclo-95-4-1 -->
![El ciclo `95/4/1` · memoria muscular del agente](figuras/g22-ciclo-95-4-1.png)

El ciclo de vida operativo de un Botlet en producción se distribuye típicamente con la proporción que da nombre a este modelo: **`95/4/1`**. Las proporciones son aproximadas pero estructuralmente correctas: la mayor parte del tiempo el Botlet ejecuta sin invocar cognición; ocasionalmente el ambiente cambia y el Botlet falla; raramente la cognición debe regenerar el código.

El **noventa y cinco por ciento del tiempo**, el Botlet está en **ejecución normal**. La cognición no se invoca. El Botlet corre, completa su tarea en segundos o minutos según el caso, devuelve resultado. Esta es la fase eficiente — donde toda la economía del sistema agentivo se sostiene. Una organización que opera mil agentes con Botlets bien diseñados ejecuta noventa y cinco por ciento de las tareas a costo de cómputo tradicional, no a costo de inferencia LLM. La diferencia económica es de uno o dos órdenes de magnitud.

El **cuatro por ciento del tiempo**, el Botlet detecta un **cambio en el ambiente**. Falla o devuelve un resultado anómalo. El ambiente cambió: un campo de la API se movió, una estructura de datos varió, la respuesta de un sistema externo tiene un formato distinto. El Botlet, escrito para el ambiente de hace dos semanas, ya no funciona. La cognición se activa. Evalúa el cambio: ¿es algo que se puede manejar regenerando el Botlet? ¿es algo que requiere ejecución manual única en este caso? ¿es algo que requiere escalación al humano?

El **uno por ciento del tiempo**, la cognición decide **regenerar el Botlet**. Genera una nueva versión adaptada al ambiente cambiado. La nueva versión queda como Botlet activo, reemplazando la versión anterior. Las próximas invocaciones — la nueva fase del noventa y cinco por ciento — usan la versión regenerada. El ciclo se cierra y vuelve a empezar.

La proporción exacta varía según el caso. Un Botlet operando contra un sistema externo muy estable puede mantener noventa y nueve por ciento de ejecución normal y solo uno por ciento de cambio detectado. Un Botlet operando contra un sistema externo volátil puede caer a ochenta por ciento de ejecución normal con quince por ciento de cambios y cinco por ciento de regeneración. Lo importante no son las proporciones específicas: es la **estructura** del ciclo. El Botlet ejecuta la mayoría del tiempo sin cognición; la cognición se reserva para los casos donde el ambiente cambia.

### Madurez del Botlet — junior, en aprendizaje, senior

<!-- FIG:g23-madurez-botlet -->
![Madurez del Botlet · trayectoria junior → en aprendizaje → senior](figuras/g23-madurez-botlet.png)

El ciclo `95/4/1` es presentación didáctica útil, pero es **estática**: describe el estado estacionario de un Botlet ya conformado, no la trayectoria por la cual el Botlet llega a ese estado. La realidad operativa exige una distinción adicional: un Botlet recién generado **no opera con la proporción `95/4/1`**. Opera con una proporción peor. Solo después de incorporar las variantes del ambiente alcanza la madurez que el ciclo canónico describe. Esta sección formaliza la trayectoria.

La spec reconoce **tres fases canónicas** en la madurez de un Botlet: junior, en aprendizaje, senior. Las fases no son etiquetas administrativas; son estados con propiedades distintas que el sistema rastrea para decidir cuánto delegar al Botlet y cuándo escalarlo.

#### Fase junior

Un Botlet **junior** es un Botlet recién generado. Acaba de salir de la cognición. Conoce el ambiente solo en la versión que la cognición observó cuando lo creó. Las variantes del ambiente — fechas en formato distinto, mensajes de error con redacción nueva, campos opcionales que aparecen solo a veces, casos límite — todavía no han pasado por él, así que su código no las contempla.

La proporción típica de un Botlet junior es algo como `60 / 35 / 5`: solo el 60% de las invocaciones son ejecución normal exitosa; el 35% son fallos por variantes del ambiente que el Botlet no anticipa; el 5% son regeneraciones cuando la cognición decide que la variante observada es estructural y debe incorporarse. La proporción es desfavorable, pero no es problema — es la fase normal de cualquier Botlet recién generado, y la cognición está ahí precisamente para rescatarlo.

Operativamente, un Botlet junior depende fuertemente de la disponibilidad de la cognición (Capa 2). No puede operar offline porque demasiadas de sus invocaciones requieren rescate. Tampoco puede asumir responsabilidades críticas sin red de seguridad explícita.

#### Fase en aprendizaje

Un Botlet **en aprendizaje** es un Botlet que ya pasó por las primeras invocaciones reales. Ha enfrentado variantes del ambiente y ha sido regenerado varias veces para incorporarlas. Su proporción se mueve hacia algo como `85 / 12 / 3`: la mayoría de las invocaciones son exitosas, los fallos por variantes nuevas son menos frecuentes, las regeneraciones son ocasionales.

La fase en aprendizaje es la fase más larga de la vida útil del Botlet — puede durar semanas o meses según la frecuencia de invocación y la volatilidad del ambiente. Cada regeneración consolida saber operativo: cada variante incorporada es una variante menos que puede sorprender al Botlet en el futuro.

Operativamente, un Botlet en aprendizaje puede operar con red intermitente — los fallos siguen siendo lo suficientemente frecuentes como para necesitar la cognición disponible regularmente, pero no en cada invocación. Puede asumir responsabilidades operativas con observación humana cercana.

#### Fase senior

Un Botlet **senior** es un Botlet que ya incorporó las variantes del ambiente. Su proporción tiende a `99+ / <1 / ~0`: prácticamente todas las invocaciones son ejecución normal exitosa; los fallos por cambios de ambiente son raros porque el ambiente ya rara vez le presenta algo que no conozca; las regeneraciones son excepcionales.

Una propiedad fundamental del Botlet senior cambia respecto a las fases anteriores: **sus fallos en estado senior no son cambios de ambiente; son causas exógenas**. Cuando un Botlet senior falla, la causa típica es algo que detendría a cualquier sistema estable: corte de energía, hardware caído, red catastróficamente perdida, recurso externo (proveedor de tools, sistema regulado) caído. Estos fallos no son aprendizaje pendiente — son lo mismo que cualquier sistema operativo encuentra ocasionalmente y resuelve con redundancia, restart o intervención humana.

Operativamente, un Botlet senior puede operar **offline confiablemente**. La razón es estructural: si sus únicos modos de fallo son exógenos, la presencia o ausencia de la cognición no cambia la probabilidad de fallo significativamente — la cognición no tiene cómo rescatar de un corte de energía. El Botlet senior, contra una BD local y Conectores edge-resident, sostiene la operación del sitio físico aunque la cognición esté inalcanzable. Esta propiedad es la base estructural del modo offline en sistemas con Capa 3 distribuida (Capítulo 5 §1).

#### Implicaciones de la trayectoria

La distinción entre las tres fases tiene tres implicaciones que conviene retener.

**Primera**, el offline confiable es propiedad de Botlets senior, no de Botlets en general. Pretender que un Botlet recién deployado en un local nuevo pueda operar offline es violar la spec — todavía es junior, depende de la cognición. La trayectoria de un nodo edge desde puesta en producción hasta operación offline plena requiere tiempo de exposición al ambiente, no es propiedad instantánea.

**Segunda**, la **garantía de fallback agéntico es lo que produce la madurez**. Cada fallo del Botlet por cambio de ambiente activa la cognición; cada activación de la cognición regenera el Botlet incorporando la variante. Sin fallback agéntico, el Botlet quedaría atrapado en su versión inicial, sin manera de aprender. La conexión con la sección de continuidad de negocio operacional del §4 es directa: la garantía de fallback resuelve la fase junior y la transición hacia senior; la continuidad operacional resuelve los fallos exógenos de la fase senior.

**Tercera**, la madurez de un Botlet **es trazable**. El append-only log del Trust Layer registra cada invocación, cada fallo, cada regeneración. La proporción de cada fase es observable, y la trayectoria de un Botlet desde junior hasta senior es auditable. Esta trazabilidad es lo que permite que la organización tome decisiones operativas — *"este Botlet ya es senior, podemos delegarle responsabilidades críticas"* — sobre evidencia, no sobre suposición.

### Botlets seed vs Botlets emergentes — el origen del Botlet

El ciclo hasta aquí descrito supone que **Pattern Recognition** — la primitiva auxiliar que se desarrolla más abajo — activa la generación de un Botlet al detectar un patrón repetitivo no anticipado. Esa es la modalidad **emergente** de generación. Es la modalidad que el modelo neurobiológico inspira y que el ciclo `95/4/1` describe en su forma más pura. Pero **no es la única modalidad**, y para sistemas productivos reales no es ni siquiera la más frecuente.

En un sistema productivo, los Botlets críticos del MVP **no emergen**: los implementa la cognición porque el equipo de diseño los planificó como parte de la spec del producto. El equipo sabe, antes de que el sistema vea su primera transacción, que va a necesitar un Botlet de POS, un Botlet de comanda, un Botlet de cobro, un Botlet de cierre de turno. La cognición ejecuta la implementación de esos Botlets; pero la **decisión de existir** la tomó el diseño, no Pattern Recognition.

La spec distingue por tanto **dos orígenes canónicos** del Botlet:

**Botlets seed.** Generados por la cognición a pedido del equipo de diseño, como parte del producto inicial. La cognición ejecuta la implementación — escribe el código del Botlet, lo registra en el Botler, lo deploya al ambiente correspondiente — pero la decisión de qué Botlets debe haber, qué tareas cubren y bajo qué contratos operan, es del equipo de diseño. Pattern Recognition no participa en la generación seed.

**Botlets emergentes.** Generados por Pattern Recognition cuando la cognición, durante operación, detecta un patrón repetitivo no anticipado por el diseño. La cognición evalúa si el patrón merece automatización, decide afirmativamente, y genera el Botlet. Es la modalidad que la sección anterior describió.

Ambos viven y operan idénticamente una vez generados — ambos están sujetos al ciclo `95/4/1`, ambos pasan por las fases junior → en aprendizaje → senior, ambos tienen garantía de fallback, ambos son auditables. La diferencia está en el origen.

> *Pattern Recognition no es la única vía a Botlet. El diseño tampoco es deuda técnica. Las dos vías coexisten.*

La distinción tiene tres consecuencias prácticas.

**Primera**, un sistema agentivo productivo **no requiere esperar a que Pattern Recognition descubra los Botlets críticos**. Los Botlets seed se generan al inicio según la spec del producto, y el sistema entra en producción con la batería de Botlets necesaria para operar. Pattern Recognition entra después, durante la vida del sistema, para optimizar lo que el diseño no anticipó.

**Segunda**, los Botlets seed pueden vivir **en cualquier capa**, no solo en Capa 3. Las **GUIs persistentes generadas como Botlets de fachada** del Capítulo 4 §1 son Botlets seed de Capa 1 — generadas por la cognición a pedido del equipo de diseño porque el rol operativo (cajero, cocinero, operador de planta) lo justifica. La definición canónica del Botlet seed permite estas materializaciones sin que la spec las trate como excepciones.

**Tercera**, la trayectoria de madurez aplica igual a Botlets seed que a Botlets emergentes. Un Botlet seed recién deployado es **junior**; un Botlet seed que ya operó miles de veces y consolidó su saber del ambiente es **senior**. La distinción origen no cambia la trayectoria; solo el momento de inicio.

### proto-Botlet — la pieza pre-forjada

La distinción seed vs emergente describe *quién decide* que un Botlet exista. Queda una pregunta anterior: cuando la cognición genera un Botlet seed, ¿escribe su código desde cero cada vez? En la práctica operativa, no. El código del Botlet rara vez nace de la nada: nace de una pieza pre-forjada que el agente configura.

Un **proto-Botlet** es una pieza pre-forjada de capacidad operativa que el agente, en su tiempo de Ingeniería, **configura** para instanciar un Botlet específico al caso. El proto-Botlet contiene el código; el Botlet es la instancia configurada. La relación es genérico → instancia: el proto-Botlet vive en un catálogo y sirve a muchos casos; el Botlet es uno de esos casos resuelto.

<!-- FIG:g24-proto-botlet -->
![proto-Botlet — la pieza pre-forjada del catálogo (templado · platafórmico)](figuras/g24-proto-botlet.png)

La conexión con el origen del Botlet es directa. Un Botlet seed que el equipo de diseño planificó no obliga a la cognición a escribir su lógica entera: si el catálogo tiene un proto-Botlet que cubre la función — cobro de cuenta, comanda contra impresora de tickets, una operación informativa —, la cognición instancia el Botlet **configurando** ese proto-Botlet en vez de generándolo. La decisión de existir sigue siendo del diseño (es seed); la materialización del código se apoya en la pieza pre-forjada.

La spec reconoce **dos clases** de proto-Botlet, según la naturaleza de su código:

| Clase | ¿Qué es su código? | ¿Cómo se configura? | Ejemplo anonimizado |
|---|---|---|---|
| **Templado** | Código específico de su función | Parametrización acotada | Cobro de una cuenta; comanda contra impresora de tickets |
| **Platafórmico** | Código genérico cuya especialización vive en una configuración composicional | Configuración composicional, que cubre N funciones del dominio | Una pieza de operación informativa que sirve reportes y dashboards de muchas formas |

Un proto-Botlet **templado** resuelve una función y la resuelve completa; configurarlo es ajustar parámetros dentro de un rango previsto. Un proto-Botlet **platafórmico** es un motor: su código es genérico y la función específica emerge de una configuración rica — composicional, no una lista plana de parámetros —, de modo que un solo proto-Botlet platafórmico cubre N funciones de su dominio. **Mira**, en el catálogo de la implementación de referencia, es un proto-Botlet platafórmico de operación informativa.

Distintas implementaciones mantienen catálogos de proto-Botlets — públicos en AgencyDomains.org, privados en códices propietarios. Y el grado en que el agente configura la pieza pre-forjada, co-escribe su código o lo genera entero define las **generaciones del Botlet** — la sección siguiente las fija.

### Las generaciones del Botlet — `G1`, `G2`, `G3`

<!-- FIG:g51-generaciones-botlet -->
![Generaciones del Botlet — capacidad de autoría vs madurez operativa](figuras/g51-generaciones-botlet.png)

Las generaciones son el modelo evolutivo de cómo nace el código del Botlet conforme avanza el estado del arte de la cognición:

- **`G1`** — el agente, en su tiempo de Ingeniería, configura proto-Botlets pre-forjados del catálogo. Si ninguno sirve, especifica uno nuevo para forjar en la próxima Preparación.
- **`G2`** — el agente co-escribe proto-Botlets con asistencia humana o de modelo. Parte del trabajo que en `G1` ocurría en Preparación migra a la Ingeniería.
- **`G3`** — el agente genera el código completo del Botlet en su tiempo de Ingeniería, sin pre-forjar nada. Escenario asintótico.

La arquitectura es la misma en las tres generaciones; lo que cambia es el **alcance de la Ingeniería** que el agente realiza. Una implementación puede operar en `G1` hoy y migrar incrementalmente hacia `G3` conforme el estado del arte lo permita, sin re-arquitectura.

**Una generación más alta no es un destino.** La frase anterior — migrar hacia `G3` — induce, leída sola, una conclusión falsa: que `G3` es el destino y `G1` una estación de paso primitiva. El error nace de proyectar **dos ejes distintos sobre una sola flecha**:

| ¿Qué eje? | ¿Qué mide? | ¿Dirección de "avance"? |
|---|---|---|
| **Capacidad de autoría** | Cuánto puede forjar el agente: configurar (`G1`) → co-escribir (`G2`) → generar entero (`G3`) | Hacia `G3`, conforme avanza el estado del arte de la cognición |
| **Madurez operativa** | Para una operación recurrente, cuánto se reutiliza pre-forjado vs se regenera cada vez (ciclo `95/4/1`) | Hacia la reutilización (`G1`), conforme el Botlet madura junior → senior |

No son la misma flecha. Un agente con capacidad `G3` que regenera cada artefacto desde cero en cada ejecución no es avanzado: tiene el músculo y elige re-aprender el movimiento cada vez. La reconciliación es directa: la capacidad `G3` se gasta mejor **produciendo reutilización `G1`**. Las generaciones describen lo que el agente *puede* autorar; el ciclo `95/4/1` describe lo que un agente maduro *reutiliza*. El destino de la capacidad `G3` es un catálogo `G1` más rico, no la regeneración en vivo de todo.

Hay un corolario para los proto-Botlets **platafórmicos**. Para uno de ellos, `G1` es **terminal por diseño**, no estación de paso: su identidad es código genérico más configuración. Un platafórmico "en `G3`" — donde el agente regenera el motor por cada pieza — no es una versión más avanzada; disuelve el proto-Botlet y colapsa de vuelta al modo agéntico que la arquitectura existe para trascender.

**`G1` no es configuración pobre.** Lo que define `G1` es que el agente no escribe el cuerpo del proto-Botlet — pero la configuración que rellena puede ser tan rica como un `DSL` composicional con expresiones formales evaluables. La distinción `G1`/`G3` es sobre **autoría del cuerpo del proto-Botlet**, no sobre expresividad de la configuración. Un proto-Botlet platafórmico con un `DSL` rico es `G1` puro.

Eso deja un caso frontera: configuración que admite expresiones formales evaluables — `SQL`, especificaciones de gráfico, expresiones de filtro. El **filo `G1`/`G2`** lo resuelve:

- Una expresión formal evaluable que es **parámetro de una Capability bien definida** (`SQL` → `execute-sql`, una especificación de gráfico → `render-chart`, una expresión de filtro → `filter-stream`) es configuración → **`G1`**.
- Una expresión que **extiende o sobreescribe la lógica interna del proto-Botlet** — callbacks, lambdas que el proto-Botlet evalúa internamente, fragmentos que se concatenan a su cuerpo — es código escrito por el agente → **`G2`**.

El test es uno solo: *"¿el código pertenece a la Capability invocada o al proto-Botlet mismo?"*. Si lo evalúa una Capability del catálogo, `G1`; si lo evalúa el proto-Botlet en su lógica interna, `G2`.

La implementación de referencia, Vergis, opera hoy en `G1`: su catálogo expone proto-Botlets — Mira entre ellos — que el agente especializa configurando, no regenerando (Capítulo 9). El sentido profundo de las generaciones — por qué el agente avanzado genera *menos*, no más — es el ensayo con que cierra el libro.

### Garantía de fallback — la propiedad innegociable

La garantía de fallback merece tratamiento detallado porque es lo que hace al Botlet **operacionalmente confiable** en lugar de **frágilmente automatizado**. Una organización que depende de un Botlet para una operación crítica — procesar un batch nocturno, enviar reportes regulatorios, conciliar transacciones — debe poder confiar en que el Botlet va a ejecutarse o, en su defecto, alguien va a ejecutar la tarea por él. La garantía de fallback es lo que sostiene esa confianza.

Cuando un Botlet falla catastróficamente — no porque el ambiente cambió levemente y la cognición pueda regenerar el código, sino porque algo realmente impide la ejecución —, la cognición ejecuta la tarea manualmente. *Manualmente* en este contexto significa que el LLM hace el trabajo paso a paso, invocando los tools subyacentes que el Botlet usaría, pero sin la eficiencia del código compilado. El proceso es más lento y más costoso — la cognición consume tokens — pero **el trabajo se hace**. La organización no se queda detenida.

Esta garantía no es decorativa. Es lo que distingue al Botlet conforme a esta spec de cualquier "macro inteligente" o "automatización con IA" frágil. Las macros tradicionales fallan y dejan la operación detenida; los Botlets fallan y la cognición toma el relevo. La diferencia es estructural y se traduce directamente en disponibilidad operativa: una organización con Botlets correctamente diseñados puede prometer SLAs de operación que serían imposibles con automatización tradicional.

> *El Botlet no reemplaza a la cognición. La libera del trabajo repetitivo, pero queda como red de seguridad.*

La cita anterior resume bien la relación entre las dos capas. La cognición no es residual — sigue siendo la inteligencia general que sostiene el sistema. El Botlet es eficiencia operativa que opera mientras el ambiente lo permite. Cuando el ambiente sale del rango, la cognición vuelve.

### ¿Cuándo usar Botlets, y cuándo no?

No todas las tareas se benefician de ser delegadas a Botlets. La spec define criterios claros para decidir cuándo conviene generar un Botlet y cuándo conviene mantener la tarea bajo cognición continua.

**Conviene generar un Botlet** cuando la tarea es repetitiva — más de diez invocaciones es regla práctica útil —, cuando el patrón es estable en su núcleo aunque el ambiente puede cambiar, cuando el proceso es crítico y debe ser rápido, cuando el costo de cognición por invocación es relevante a escala, y cuando hay tolerancia a regeneración esporádica del código sin que eso afecte la operación.

**No conviene generar un Botlet** cuando la tarea es única o de baja frecuencia, cuando el patrón es altamente variable y cada invocación requiere juicio fresco, cuando la tarea exige razonamiento profundo que un script no puede capturar, cuando es prototipo o exploración donde la flexibilidad importa más que la eficiencia, cuando el costo total es irrelevante y la cognición continua es práctica, o cuando los cambios en el ambiente son tan constantes que el Botlet se regeneraría todo el tiempo, perdiendo su beneficio.

La regla práctica que sintetiza estos criterios: **si la tarea se ejecuta más de diez veces y su lógica es estable en su núcleo, conviene generar un Botlet**. Por debajo de ese umbral, la cognición es más eficiente. Por encima, la diferencia económica empieza a ser material.

Una observación importante: la decisión de cuándo generar Botlet no la toma un humano. La toma la cognición misma, asistida por Pattern Recognition que detecta los patrones repetitivos. El humano define las reglas generales — qué tipos de tareas son candidatas, qué umbrales de frecuencia son relevantes, qué tipos de ambientes son sensibles —, pero la decisión específica en cada caso emerge del comportamiento del agente. Esta es propiedad del sistema agentivo: la decisión de optimización es propia del agente, no externa a él.

### Manifestación y temporalidad del Botlet

Un Botlet es memoria muscular: una disposición latente, un saber-hacer almacenado que no es nada hasta que se ejerce. Cuando el Botlet se ejecuta, ese latente se actualiza en el mundo. Esa actualización es su **manifestación**: el paso de potencia a acto del Botlet, perceptible o no.

La palabra exige cuidado. **Manifestación no es aparición.** El término corriente sugiere "hacerse visible", y eso dejaría fuera casos legítimos: un Botlet que dispara una ingestión periódica se manifiesta — actualiza su latente, produce un efecto — aunque no deje ningún artefacto visible. Por eso el canon la define como *actualización del latente*, no como *aparición*: el efecto invisible cuenta tanto como el artefacto a la vista.

<!-- FIG:g25-manifestacion-temporalidad -->
![Manifestación y temporalidad del Botlet — discreta vs continua](figuras/g25-manifestacion-temporalidad.png)

La manifestación es el **género abstracto**; cada familia de Botlet la especializa, y cada práctica le pone su nombre cargado:

- familia de **información** → su manifestación deja un **Producto de Información** (`PI`),
- familia de **actuación** → un efecto sobre el mundo, sin artefacto,
- familia de **decisión** → la nombra su propia práctica.

El `PI` **no es primitiva del canon**: es la manifestación de *una* familia. El canon se queda en `manifestación`; el Producto de Información es un **término normado de esta spec** — no primitiva, pero sí vocabulario con reglas —, y su carga de gobernabilidad se añade aquí sin contaminar el nivel canónico. Esta es su descripción de referencia:

**Producto de Información multi-vista · drill-through.** Un `PI` no es necesariamente una pieza única. Puede componerse de **N piezas nombradas**: cada **vista** es una pieza más del mismo `PI`, elegible desde un selector, con una vista por defecto (la primera). El `PI` es **authz-blind** — ni las vistas ni las aristas que las conectan declaran autorización; esa política vive en el policy store, no en la composición.

La conexión entre vistas es el **drill-through**: una **arista de navegación con contexto**. Una tabla declara *"al clickear una fila, ir a la vista destino pasando la clave de esa fila"*; la vista destino se renderiza **filtrada por esa clave**. La propiedad crítica es **data-anchored / no-bypass**: el contexto que viaja con la arista **acota dentro de lo que el viewer ya puede ver** — la vista destino aplica su propia política de filas (`RLS`, *row-level security*: la seguridad a nivel de fila) sobre la fuente, y el contexto entra como filtro adicional, nunca como override de la política (**MUST**). El drill **acota, nunca amplía** — intersección con lo autorizado, jamás unión. Si el viewer no alcanza la fila origen, no llega a la arista; si llega, el destino sigue gobernado por su propia política.

Un reporte de cartera / aging de saldos ilustra el patrón: vistas nombradas (Clientes, Proveedores, Relacionados, Detalle) sobre el mismo `PI`, una tabla jerárquica Empresa→Socio, y una arista de drill-through Socio→Detalle que abre los documentos de ese socio — filtrados por la clave del socio y acotados a lo que el viewer ya tenía derecho a ver. La composición multi-vista es ortogonal a la familia del Botlet de operación: lo que cambia es cuántas piezas componen la manifestación, no su naturaleza.

<!-- FIG:g13-pi-multivista-drillthrough -->
![PI multi-vista y drill-through — navegación con contexto, data-anchored](figuras/g13-pi-multivista-drillthrough.png)

La **temporalidad** es el régimen de la manifestación. Es atributo declarado del Botlet, con dos valores:

| Temporalidad | ¿Cómo se manifiesta? | Relación con el runtime |
|---|---|---|
| **`discreta`** | En pulsos: despierta por schedule, trigger o evento, actúa, descansa | El Botler invoca o agenda; el Botlet no vive entre pulsos |
| **`continua`** | Sostenida: vive persistente y se manifiesta sin cesar | El Botler sostiene la ejecución mientras el Botlet viva |

`temporalidad: continua` equivale a la vida persistente de Capa 3: obliga al Botler a sostener la ejecución del Botlet sin re-arranque por cada manifestación. Un Botlet conforme con temporalidad continua MUST poder ser sostenido por el runtime persistente; un Botlet con temporalidad discreta se manifiesta vía schedule, trigger o evento.

La consecuencia operativa es fuerte: **el tiempo real no se elige en un canal de entrega.** No se obtiene marcando un canal como `push`; se obtiene dándole al Botlet temporalidad continua, lo que a su vez obliga al runtime persistente. El modo de entrega es el síntoma; la temporalidad continua es la causa. Esto reubica el "tiempo real" del nivel del canal al nivel del Botlet, y conecta con la distinción *Empresa en línea ≠ Empresa en tiempo real*: no son dos clases de información, sino dos puntos del continuo de temporalidad.

De aquí se sigue una economía de runtime. Un reporte — snapshot en un punto del tiempo — y un dashboard vivo no son dos tipos distintos de *qué*: son la **misma manifestación bajo distinta temporalidad**. Por eso un único runtime los cubre: se construye el caso más difícil (continua) y los casos simples son configuraciones degeneradas de ese caso, no codepaths aparte. La distinción se sostiene precisamente porque la temporalidad es ortogonal a lo que se manifiesta.

### Botler — el framework runner

**Botler** es la infraestructura que ejecuta los Botlets dentro de la Capa 3 (Autonomía). Es invisible para el usuario y para el agente; es responsabilidad de la implementación del AgencyDomain. La relación canónica es simple: un proceso del AgencyDomain contiene un Botler, y el Botler gestiona N Botlets que viven dentro de ese proceso.

El Botler provee cuatro funciones críticas. La primera es **aislamiento de ejecución** — sandboxing apropiado al ambiente, que detallamos en la próxima sección. La segunda es **gestión del ciclo de vida del Botlet**: invocación cuando se necesita, monitoreo durante ejecución, detección de fallos, disparar regeneración cuando corresponde. La tercera es **comunicación con la cognición** cuando el Botlet detecta un fallo o cambio en el ambiente que excede su capacidad de manejo. La cuarta es **trazabilidad**: cada invocación del Botlet, cada resultado, cada fallo, cada regeneración, queda registrado en el append-only log del Trust Layer. Esta trazabilidad es lo que permite reconstruir, auditablemente, qué hizo el agente y por qué — y es indispensable para gobernanza.

El Botler como abstracción importa porque desacopla la implementación de aislamiento del agente que lo usa. El agente no sabe — ni tiene por qué saber — si su Botlet corre en un contenedor Docker, en una sandbox WASM, o en una microVM. Solicita ejecución al Botler; el Botler ejecuta bajo el modelo de aislamiento que la implementación del AgencyDomain eligió. Esta separación es lo que permite que la spec sea agnóstica a tecnología de aislamiento — distintas implementaciones eligen distintas tecnologías según sus tradeoffs específicos.

#### El Botler es genérico por definición

El Botler **no entiende el dominio** de los Botlets que ejecuta. Gestiona el ciclo de vida, el aislamiento y la ejecución de *cualquier* Botlet sin saber qué hace ese Botlet ni a qué disciplina pertenece. Toda la especialización de dominio vive en los Botlets y en sus proto-Botlets, nunca en el runtime que los hospeda. La arquitectura es plana: un runtime genérico hospeda componentes especialistas autocontenidos.

De aquí se sigue una propiedad estructural: **no existen subtipos de Botler por familia de operación.** No hay un Botler "informativo", uno "transaccional", uno "para artefactos de información" — un Botlet de operación informativa ya carga su propia frescura, su caché, su distribución, de modo que un subtipo de Botler que lo duplicara contradiría la genericidad del runtime sin agregar nada.

> *Los subtipos de Botler se distinguen por topología y rol de despliegue — central, edge, fachada operativa para Botlets de Capa 1 —, **nunca por dominio**. La especialización de dominio vive íntegramente en los Botlets que el Botler ejecuta.*

Los ejes de topología y rol son legítimos porque responden a *dónde* corre el runtime y con qué autonomía, no a *qué* dominio ejecuta: un Botler central y un Botler edge difieren en conectividad y operación offline, no en conocimiento de negocio. La nota normativa es la frontera: cualquier distinción de Botler que apele a la familia de operación que ejecuta está mal planteada.

#### El Botler valida orquestando, no ejecutando

El registro de un Botlet exige que su spec sea válida contra el tipo declarado antes de aceptarlo. Esto plantea una tensión aparente: si el Botler no entiende el dominio, ¿cómo valida una spec cuyo sentido es de dominio? La respuesta distingue **orquestar** la validación de **ejecutarla**.

El Botler **hace valer** la validación; no la ejecuta con conocimiento de dominio. En el momento del registro invoca el punto de validación que el propio Botlet provee — o que provee su proto-Botlet en G1 —, le entrega el contexto genérico que sí controla (el catálogo de Capabilities disponibles, la identidad, las políticas del AgencyDomain) y actúa sobre el veredicto: acepta, rechaza, o registra el resultado en el append-only log. El juicio de qué hace válida a la spec vive enteramente en el Botlet; el Botler decide admitir o no según un veredicto que no produjo. Así, ninguna spec inválida entra — el rechazo ocurre antes de admitir el Botlet y queda trazado — sin que el runtime interprete jamás el dominio.

Este patrón tiene un hermano en la invocación de Capabilities. El Botler es el único punto por el cual un Botlet invoca Capabilities, y el bypass por canales paralelos no se prohíbe solo por política: se hace estructuralmente imposible. En cada invocación el Botler entrega al Botlet un **handle controlado** — un objeto con acceso a Capabilities y al log ligado al propio Botler — en vez de permitir que el Botlet construya accesos por su cuenta. El Botlet solo puede actuar sobre el mundo a través de ese handle. Ambos casos comparten el principio: el Botler genérico expone **puntos de control** y el especialista se enchufa en ellos; el runtime se mantiene delgado sin renunciar a las garantías que el contrato exige.

#### La interfaz Capa 2 ↔ Capa 3 vía `MCP`

El Botler es el único punto de ejecución de los Botlets, y eso incluye la operación que la propia Cognición dirige: la **Cognición** (el agente `LLM`, Capa 2) comanda al Botler (runtime de Capa 3, sin agencia) por una interfaz **interna** cuyo transporte natural es `MCP` — el Botler expone servidores `MCP` y la Cognición es el cliente. Esta interfaz **no es `A2A`**; la corrección formal de la nomenclatura `A2A` y la interfaz Capa 2 ↔ Capa 3 se desarrollan en el Capítulo 5 §1.

#### Código fuente vs spec · dos superficies · un Botlet por `PI`

La operación de un Botlet involucra dos cosas que conviene no confundir. Una es el **código fuente** del Botlet: su implementación. Para un proto-Botlet platafórmico, ese código fuente es el **motor**, compartido por todos los Botlets que de él se instancian. La otra es la **spec**: lo que especializa el comportamiento del Botlet a su instancia. La spec no es el código; lo configura.

Esa separación se proyecta en **dos superficies** de gestión:

| Superficie | ¿Qué gestiona? | Granularidad | Cadencia |
|---|---|---|---|
| Ciclo de vida del código fuente | Instalar, versionar, cargar y descargar el motor | Nivel-Botler | Releases (Producto) |
| Operación | Especializar, manifestar, consumir y controlar cada Botlet | Por-Botlet | Fluida (Instancia) |

La operación **incluye configurar el spec**. Para un proto-Botlet platafórmico, el spec es el input operacional: no hay "operar" sin spec. De ahí un principio: **configurar el spec es operar**. El agente evoluciona el spec operando — verbo `specialize` —, de forma fluida; la cristalización del spec a un registro versionado **sigue, no precede**, y la proveniencia la da el append-log. Los verbos del API de operación son `specialize`, `invoke` y `schedule` (para temporalidad discreta), `read` y `subscribe` (para temporalidad continua), y `status`, `activate`, `deactivate`, `retire`.

De esto se desprende la regla de granularidad: **un Botlet por `PI`** sobre un motor compartido. Cada Producto de Información es su propio Botlet — su propio servicio, con identidad, temporalidad, madurez y fallback propios —, especializado del motor compartido (el proto-Botlet platafórmico). No es un Botlet con N configuraciones, que perdería esa independencia; no son N programas, porque el motor es uno. Es la relación `1 Proceso = 1 Botler + N Botlets`, con los Botlets como instancias especializadas del mismo proto-Botlet. El rationale es `RISC`: muchos Botlets simples y focalizados — uno por `PI` — componen mejor que un monolito.

El consumo `subscribe` es el puente al **norte agentivo**. Hoy lo consume un humano — un navegador suscrito por `SSE` que recibe la corriente de manifestaciones de un Botlet continuo —; mañana lo consume la Cognición, alimentándose de esa misma corriente para decidir. La temporalidad continua, el runtime persistente y el verbo `subscribe` son, juntos, la infraestructura de ese norte.

### Modelo de aislamiento — sandboxing

Los Botlets son **código generado dinámicamente por un agente**. Esto exige aislamiento estricto. Un Botlet mal escrito, o un Botlet generado por un agente que fue víctima de prompt injection, podría intentar acciones maliciosas — exfiltrar datos, modificar archivos del sistema, abrir conexiones de red no autorizadas. El aislamiento es lo que contiene esos riesgos.

La spec admite cuatro estrategias de sandboxing, con sus trade-offs:

**Procesos con seccomp** ofrecen aislamiento bajo y overhead mínimo. Es estrategia útil solo en ambientes controlados donde el riesgo de código malicioso es bajo — por ejemplo, Botlets ejecutándose dentro del perímetro privado de una organización con confianza implícita en sus propios agentes. No es estrategia adecuada para Botlets que tocan datos sensibles o que operan bajo régimen público.

**Contenedores** — Docker, Podman, equivalentes — ofrecen aislamiento medio-alto con overhead medio. Es la estrategia más práctica para Botlets genéricos que necesitan invocar tools del sistema operativo o redes. Los contenedores tienen ecosistema maduro, portabilidad razonable, herramientas operacionales abundantes. Son default razonable para la mayoría de los casos.

**WASM (WebAssembly)** ofrece aislamiento alto con overhead bajo, pero el ecosistema es más limitado. WASM es ideal para Botlets transformacionales puros — cálculos, transformaciones de datos, lógica algorítmica — que no necesitan acceso al sistema operativo subyacente. La velocidad de inicio es muy rápida (milisegundos), lo que importa cuando un agente necesita invocar muchos Botlets simultáneamente.

**MicroVMs** — Firecracker, Kata Containers — ofrecen aislamiento máximo con overhead alto. Son adecuadas para Botlets que manejan datos altamente sensibles o que operan en ambientes multi-tenant compartidos donde el riesgo de cross-tenant leakage es inaceptable. El overhead típicamente significa decenas de milisegundos de inicio adicional, que en algunos casos es prohibitivo.

La recomendación canónica para implementaciones de referencia es **híbrida**: WASM para transformers puros (sin acceso al sistema), contenedores para Botlets genéricos que necesitan invocar tools del sistema operativo, MicroVMs para Botlets que manejan datos altamente sensibles o que operan en entornos multi-tenant compartidos. La elección específica para cada Botlet depende de su perfil de riesgo y de su requisitos de performance.

### Lenguaje de los Botlets

La spec es **agnóstica al lenguaje** de implementación de los Botlets. La cognición puede generar Botlets en cualquier lenguaje siempre que el Botler los pueda ejecutar dentro del sandbox elegido. Esta agnosticidad importa porque el panorama de lenguajes evoluciona — un sistema atado a un lenguaje específico puede quedar obsoleto cuando ese lenguaje pierde tracción en el ecosistema de IA.

Las recomendaciones prácticas para implementaciones de referencia son:

**Python** es primera elección. La madurez del ecosistema, las librerías para casi cualquier integración, la generación por LLM altamente confiable — los modelos contemporáneos generan Python correctamente con frecuencia muy alta —, hacen de Python el default razonable para Botlets genéricos.

**JavaScript / TypeScript** son adecuados para Botlets que tocan APIs HTTP o que automatizan browsers. El ecosistema npm tiene cobertura amplia, y la generación por LLM también es confiable.

**Bash o shell** son adecuados para Botlets que orquestan comandos del sistema operativo. La generación de bash por LLM es confiable para casos simples, menos confiable para casos complejos donde la sintaxis de bash tiene quirks.

**Rust o Go** — lenguajes compilados — son adecuados para Botlets de muy alta frecuencia donde el overhead del intérprete importa. La generación por LLM es menos confiable que Python, pero los Botlets resultantes ejecutan más rápido. Esta combinación tiene sentido cuando un Botlet va a ejecutarse millones de veces y la diferencia de milisegundos por invocación se acumula a impacto material.

Hay una propiedad importante: el Botlet **no es editable por humanos**. Es regenerado por la cognición. Esto importa porque cualquier mejora manual al código del Botlet — un humano que abre el archivo y mejora la lógica — se convierte en deuda en el momento que la cognición lo regenere por cambio de ambiente. La regeneración elimina las mejoras humanas. Por eso la spec define que los Botlets son **read-only para humanos en producción**: si un humano quiere mejorar la lógica, debe mejorar la cognición o las Capabilities, no el Botlet directamente.

### Pattern Recognition — la entrada al ciclo

<!-- FIG:g26-neurobiologia -->
![Inspiración neurobiológica · cerebro humano ↔ sistema agentivo](figuras/g26-neurobiologia.png)

Los Botlets no se generan al azar. La cognición decide generar un Botlet cuando reconoce un **patrón repetitivo** en la actividad del agente. El componente que detecta esos patrones es **Pattern Recognition** — primitiva auxiliar de la Capa 2 que ya mencionamos en el Capítulo 4.

Pattern Recognition opera sobre la traza de actividad del agente: qué tareas hizo, con qué frecuencia, con qué entradas similares, con qué resultados. Cuando un patrón cruza un umbral — la misma tarea repetida más de N veces con variabilidad acotada en sus entradas, los resultados estables —, la cognición evalúa si vale la pena generar un Botlet.

La inspiración neurobiológica que mencionamos al inicio se refleja en el diseño del Pattern Recognition. La **corteza perirrinal** del cerebro humano implementa familiaridad rápida — el "¿he visto esto antes?" que ocurre en milisegundos, sin recollection consciente. El Pattern Recognition agentivo implementa lo análogo: detección rápida de tareas similares a tareas pasadas, sin necesidad de razonamiento profundo. Si la respuesta es sí, el sistema activa el siguiente nivel.

El **hipocampo** implementa recollection: el "¿qué hice exactamente la última vez?". El Pattern Recognition recupera la traza específica de las invocaciones pasadas, con sus parámetros, sus resultados, sus duraciones. Esta información es lo que la cognición usa para decidir si generar Botlet vale la pena.

La **corteza prefrontal** implementa decisión consciente: el "¿debo automatizar esto?". Aquí la cognición evalúa los criterios — frecuencia, estabilidad del patrón, costo de cognición continua, riesgo de regeneración — y decide. Si decide sí, dispara la generación del Botlet.

Tres etapas, tres niveles de procesamiento. Pattern Recognition no es un solo paso — es un proceso jerárquico que filtra desde "potencialmente interesante" hasta "vale la pena automatizar". La especificación de Pattern Recognition como tool de Capa 2 está fuera del alcance de este libro; basta retener que es la primitiva auxiliar que activa el ciclo del Botlet.

### Botlets y la economía de la autonomía bajo suscripción

<!-- FIG:g27-tokens-suscripcion -->
![Tokens vs. Suscripción · dos modos de acceso a la cognición](figuras/g27-tokens-suscripcion.png)

Una propiedad operativa crítica del Botlet, que ya introdujimos en el Capítulo 4 §2 pero que merece desarrollo aquí, es su rol en la economía de la autonomía bajo planes de Suscripción fija — Claude Pro, ChatGPT Plus, Copilot empresa.

En estos planes, el costo marginal de invocar la cognición es **cero hasta el límite del plan**. El usuario paga una mensualidad fija y puede invocar el modelo cuantas veces quiera, hasta que el plan agota su cuota. Esta estructura económica es muy distinta de los modelos de pago por token, donde cada invocación cuesta y la economía se calcula por uso real.

El problema es que el límite existe. Un Agente Autónomo operando continuamente en background, sin Botlets, invocaría la cognición miles de veces al día — cada decisión, cada validación, cada acción consultaría al modelo. Bajo plan de Suscripción fija, el agente agotaría la cuota del usuario en horas. La autonomía continua sería económicamente imposible.

Los **Botlets son el mecanismo arquitectónico para extender autonomía sin saturar el plan**. Un agente que ejecuta su trabajo cotidiano vía Botlets — y solo invoca la cognición cuando el ambiente cambia — puede operar en background continuo sin agotar la cuota del usuario. La cognición queda disponible para razonamiento real, no para tareas repetitivas que el código tradicional ejecuta mejor.

> *Sin Botlets, la autonomía sostenida bajo Suscripción fija es económicamente imposible.*

Esto es lo que hace al Botlet **palanca económica**, no solo optimización técnica. La diferencia entre un agente que cuesta doscientos dólares por mes operar y uno que cuesta veinte dólares por mes operar, con capacidad efectiva idéntica, es casi siempre la proporción de tareas que ejecuta vía Botlets versus vía cognición continua. Una organización que adopta Botlets disciplinadamente puede operar agentes a un orden de magnitud menos costo que una organización que invoca cognición para cada operación.

La consecuencia comercial es directa: los proveedores que entregan agentes con buenos Botlets pueden ofrecer pricing competitivo y márgenes razonables; los proveedores que dependen de cognición continua para cada operación enfrentan un dilema económico — o suben pricing a niveles que el mercado no acepta, o operan con márgenes negativos. Esta presión es probablemente lo que llevará a la mayoría de los proveedores serios a adoptar arquitecturas con Botlets en los próximos dos a tres años.

### Cadena de derivación y catálogo de proto-Botlets

Los Botlets de un sistema no aparecen sueltos: se derivan de lo que el sistema necesita hacer, y se apoyan en piezas pre-forjadas del catálogo. La spec fija esa **cadena de derivación** como relación estructural:

1. **Casos de uso documentados** — cada caso requiere…
2. **Botlets necesarios** (cero, uno o varios; algunos casos los resuelve la cognición sin Botlet) — cada Botlet es instancia de…
3. **proto-Botlets requeridos del catálogo**.

La cadena es estructural, no metodológica. Un caso de uso puede no requerir Botlet alguno — la cognición lo resuelve directamente —, requerir uno, o requerir varios; cada Botlet que sí existe es instancia de algún proto-Botlet del catálogo. De aquí una propiedad exigida: todo Botlet conforme **MUST** poder trazarse en esta cadena, y el append-only log **MUST** registrar el proto-Botlet de origen de cada Botlet instanciado. El *método* por el cual se descubren los casos de uso y se derivan los Botlets no entra al canon — es uno de varios posibles y vive en los cuerpos complementarios de cada implementador; lo que el canon fija es la relación y su trazabilidad.

El extremo inferior de la cadena — los proto-Botlets — se acumula en **catálogos comunes** que producen efectos de red. Cada implementador que consume un proto-Botlet contribuye a su maduración: variantes nuevas, configuraciones probadas, refinamientos. Mientras más implementadores lo consumen, más casos cubre y más confiable se vuelve; el implementador n+1 recibe versiones refinadas por los implementadores 1 a n. Un proto-Botlet pertenece a una comunidad de catálogo bajo alguno de estos modos:

| Modo de pertenencia | ¿Qué es? |
|---|---|
| **Contrato privado** | Catálogo cerrado entre cliente y proveedor |
| **Códice propietario** | Catálogo privado que un implementador cura (ucodex es un ejemplar) |
| **Catálogo público abierto** | AgencyDomains.org: cualquier implementador consume y contribuye |
| **Acuerdo soberano** | AgencyDomains que adoptan estándares comunes sin contrato comercial directo |

Los modos coexisten sin tensión: un mismo implementador puede consumir el catálogo público abierto y, sobre él, curar un códice propietario con sus refinamientos por casos reales. La cadena de derivación y el catálogo común son, juntos, lo que hace de los proto-Botlets una economía y no una colección de piezas aisladas.

### Conformidad

Una implementación de Botlet conforme a esta especificación debe satisfacer los siguientes requisitos:

| Requisito | Nivel |
|---|---|
| Código generado por la cognición, no escrito por humanos | **MUST** |
| Ejecución sin invocar cognición en operación normal | **MUST** |
| Garantía de fallback a cognición manual ante fallo | **MUST** |
| Trazabilidad: cada invocación queda en append-only log | **MUST** |
| Aislamiento adecuado al ambiente | **MUST** |
| Regeneración automática ante cambio de ambiente | **SHOULD** |
| Pattern Recognition como activador de generación | **SHOULD** |
| Lenguaje agnóstico (no atar a un solo lenguaje) | **MUST** |
| Reconocimiento de fases de madurez (junior, en aprendizaje, senior) | **SHOULD** |
| Distinción entre origen seed y origen emergente | **SHOULD** |
| Trazabilidad de trayectoria de madurez en append-only log | **MUST** |
| Botlet trazable en la cadena casos-uso → Botlet → proto-Botlet | **MUST** |
| proto-Botlet de origen de cada Botlet registrado en append-only log | **MUST** |
| Botler genérico: sin subtipos de Botler por dominio | **MUST** |
| Botler hace valer la validación de spec sin ejecutarla con dominio | **MUST** |
| Soporte de las dos temporalidades (`discreta` y `continua`) | **MUST** |
| Runtime persistente que sostiene Botlets de temporalidad continua | **MUST** |
