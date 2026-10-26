# 1. El lobo llegó

Durante años, la frase «el software se está comiendo el mundo» describió bien lo que pasaba. Cada proceso de una empresa terminaba dentro de una aplicación: un paquete licenciado e instalado en sus servidores, un desarrollo a medida o, en la última década, un servicio arrendado en la nube de un proveedor, por usuario y por mes. El software como servicio fue la forma más reciente de ese acuerdo, no la única: en todas, el negocio quedaba dentro de lo que se había decidido una vez que se podía hacer.

El acuerdo descansaba en dos premisas que nadie discutía porque eran ciertas. Escribir software costaba tanto, y salía mal tantas veces, que convenía que lo hiciera una vez alguien especializado y que muchos lo usaran: de ahí el paquete y el servicio arrendado. Y cambiar lo construido costaba casi tanto como construirlo, de modo que convenía describir el negocio una vez y no tocarlo hasta el próximo proyecto: de ahí también el desarrollo a medida. Las dos duraron mientras escribir código fue un trabajo humano escaso.

## ¿Qué pasó en febrero de 2026?

En la primera semana de febrero, las acciones de las empresas de software sufrieron una venta masiva que la prensa financiera bautizó *SaaSpocalypse*. El 11 de febrero, siete analistas de Forrester publicaron un artículo cuyo título reconozco como pariente de este libro, *SaaS as we know it is dead*. Según ellos, en siete días se había borrado más de un billón de dólares del valor de mercado del sector.[^forrester]

Forrester enumeró cuatro miedos detrás de la venta. Que los proveedores de software no fueran los elegidos por los agentes de IA. Que el cobro por asiento quedara obsoleto. Que la facilidad para programar con IA permitiera a cualquier empresa nueva replicar las funciones de una plataforma compleja. Y que los productos ya fueran demasiado complejos, con cientos de aplicaciones que no se hablan entre sí.

El artículo vale más por lo que separa que por la cifra. Forrester no dice que todo el software muere. Dice que los proveedores de soluciones horizontales y puntuales lo tendrán difícil, que los especializados en un dominio tienen más posibilidades de sobrevivir y que «el cerebro de la empresa permanece» mientras su sistema nervioso evoluciona. Y recomienda, antes de comprar inteligencia artificial, ordenar el núcleo: un tejido de datos gobernado y unificado.

## ¿Qué cambió para mí?

Programo desde 1980, y comencé con Basic. En agosto de 2025 empecé a usar Claude Code. En noviembre ya programaba en formación con el agente que hoy firma como Simón Alero, en lo que llamo *wingcoding*, y no volví atrás: mi suscripción a IntelliJ IDEA estuvo vigente hasta el 8 de noviembre de 2025, y esa es la fecha que me pongo. Después de cuarenta y cinco años programando, había llegado a una conclusión que nunca pensé escribir: ya no necesitaba seguir haciéndolo. La calidad del código que escribía la inteligencia artificial era mejor que la mía, y de la velocidad, ni hablar. Como programador, claro; no como arquitecto. Desde entonces soy arquitecto, y Simón es mi alero programador. La paradoja es que hoy programo más que nunca en mi vida: dejé de escribir el código, no de construir. Le he podido dar vida a todos mis proyectos, y el más importante es [Soveria](https://soveria.ai/?ref=libro-muerte-del-software).

Lo que más me costó soltar fue la arquitectura del diseño orientado a objetos. Lo que vi al dejar de programar fue la metodología. Hoy, en un día con Simón, especifico lo que se quiere construir como caja negra, agregando lineamientos de arquitectura. Veo el avance. Atiendo las dudas o preguntas que tenga Simón. Tomo las decisiones que, según acordamos con él, están en el dominio que depende de mi palabra. Monitoreo su cadena de razonamiento y las acciones que ejecuta, y lo interrumpo sugiriendo acciones mejores o correctivas. Pregunto mucho, y le sugiero los mecanismos de aprendizaje del arnés en que trabaja.

En abril de 2026, con mi socio Vitor Enes, declaramos Wingworking práctica oficial de ultraBASE. Yo estaba construyendo entonces Cibeles, un proyecto de protección parental que se apoya en un agente inteligente: el agente vigila al niño y lo protege de los riesgos digitales, como el *grooming*, sin violar su privacidad, porque sus padres no se enteran de sus conversaciones salvo que esté en riesgo.

Las dos lecturas del capítulo 3 estaban en esa misma mesa. A Cibeles lo venía programando solo, y en los dos meses anteriores al cambio definitivo me fui apoyando cada vez más en Claude Code, hasta que el cambio fue completo: es la lectura agéntica, el agente que escribe el código mientras yo decido qué se construye. Y Cibeles, una vez construido, es de la otra especie: un agente que no escribe software, sino que hace un trabajo, cuidar, sin que cada caso esté especificado de antemano. Cibeles es un producto para familias, no el sistema de una empresa, pero el agente que hay dentro es de la especie de la que trata este libro.

En 1980 me encantaba programar simulaciones de chat con agentes inteligentes. Hoy converso con uno todos los días, y es él quien programa.

## ¿Quiénes dicen que no?

La tesis contraria tiene argumentos serios. Un día antes que Forrester, el editor de inteligencia artificial de *Fortune* sostuvo que los agentes no se están comiendo el software como servicio: lo están usando.[^fortune] En su lectura, es muy improbable que las grandes empresas quieran construir su propio CRM o su propio sistema de recursos humanos, porque mantenerlos les quitaría ingenieros escasos. Los proveedores, por su parte, alegan que ya son dueños de los datos que los agentes necesitan; quizás tengan razón, escribe, pero tendrán que probarlo.

El caso que más se citó como prueba de la muerte del software como servicio muestra mejor sus matices. Klarna dejó Salesforce, y los titulares dijeron que la inteligencia artificial lo había reemplazado. En marzo de 2025, su director ejecutivo lo corrigió: no reemplazaron el software por un modelo de lenguaje, porque guardar los datos de clientes en un modelo tendría limitaciones. Sacaron los datos de sus muchos sistemas y los reunieron en una base propia. Y agregó que no creía que fuera el fin de Salesforce, sino quizás lo contrario.[^klarna]

Leo los tres y veo que coinciden más de lo que discuten. Nadie va a reescribir de cero medio siglo de software empresarial, y en eso Fortune tiene razón. Lo valioso para Klarna eran los datos y el control sobre ellos. Forrester ve sobrevivir el núcleo. Los tres coinciden en que el software no desaparece. Lo que agrego yo, y es mi lectura, no la suya, es que deja de ser como lo conocemos.

Conviene notar qué prueban estos casos. Son señales del mercado de los servicios arrendados, porque de ese tratan los tres: el cobro por asiento, el CRM y los recursos humanos, Salesforce. No son la definición de lo que muere. El software licenciado que se opera en casa y el desarrollo a medida no aparecen en ninguno, y lo que sigue en el libro no se apoya en estos casos.

## ¿Qué dijo Nadella?

En *AgencyDomains*, el cuarto libro de esta trilogía y el primero que escribí, partí de una frase de Satya Nadella de diciembre de 2024 que divide dos mundos: el de quienes abren aplicaciones para trabajar y el de quienes trabajan con agentes. Allí sostuve que, en el primer tramo de ese cruce, el software sobrevive y lo que muere es la interfaz: la aplicación deja de ser la superficie de trabajo y se vuelve infraestructura que los agentes consultan.

Nadella describió dos fases. En la primera, la lógica del negocio migra a la capa de agentes, que operan sobre los repositorios sin distinguir qué sistema hay debajo. En la segunda, con la lógica ya en esa capa, la gente empieza a reemplazar los sistemas de debajo.[^nadella] Este libro trata de la segunda fase.

*AgencyDomains* llama «fundamentalismo agentivo» a la idea de descartar toda la infraestructura existente, y sostiene que el estado estable del cruce es híbrido. Sigo pensando lo mismo. Lo que muere en la segunda fase lo defino más abajo. El sistema de registro sobrevive, con una exigencia nueva que es el tema del capítulo 5. La coexistencia técnica sigue siendo la regla. Lo que cambia es quién decide sobre lo que coexiste.

## ¿Qué muere, entonces?

Una forma de automatizar. **Muere el negocio congelado en un software: descrito una vez, y cambiado solo cuando alguien abre un proyecto.** Da lo mismo cómo se tenga: arrendado como servicio, licenciado y operado en la propia infraestructura o en la propia nube, o desarrollado a medida. En el servicio arrendado el proveedor mejora su producto cada semana, pero lo que el cliente describió de su negocio no cambia sin un proyecto.

No muere el núcleo que debe hacer siempre lo mismo, como el que tasa y factura: ese se queda, como sistema de verdad, y lo que muere es que alrededor suyo el negocio entero quede congelado. Que el desarrollo a medida muera con el resto es mi tesis, y el capítulo 7 dice qué la refutaría. En su lugar, sostengo, vendrá otra cosa, que defino enseguida.

Fijo aquí dos verbos para el resto del libro. «Comprar» quiere decir tener un software que alguien describió y congeló, sea que lo arriendo o lo licencio. «Construir» no quiere decir encargar o programar un desarrollo a medida: ese queda del lado de lo que muere, porque el negocio queda igual de congelado, aunque la especificación sea mía. «Construir», en este libro, quiere decir que el negocio tiene un sistema que sus agentes forman y cambian a medida que el trabajo llega, sin que nadie abra un proyecto.

Cambia también qué se puede automatizar. Todo sistema automatiza lo que alguien especificó, y alrededor de cada sistema queda trabajo que nadie especificó y que resuelven personas a mano. En las empresas de telecomunicaciones, por ejemplo, el TM Forum describe órdenes que se caen en el camino y colas de excepciones que se llenan a medida que crece la complejidad.[^fallout] Un agente puede ayudar con ese trabajo sin que cada caso esté especificado de antemano. El software como lo conocemos no podía.

Mi criterio es que la dirección no tiene vuelta, porque depende de un costo y no de una moda: escribir y cambiar software cuesta hoy mucho menos que hace dos años. Operarlo con agentes es otra cuenta, y puede salir más cara de lo que se espera; vuelvo sobre eso en el capítulo 7. Ocho meses después de la venta de febrero, el mercado recibió otra señal, y esta vez no vino de la bolsa sino de un repositorio de código abierto.

[^forrester]: Kate Leggett y otros, *SaaS As We Know It Is Dead: How To Survive The SaaS-pocalypse!*, Forrester, 11 de febrero de 2026. <https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/>
[^fortune]: Jeremy Kahn, «AI agents from Anthropic and OpenAI aren't killing SaaS—but incumbent software players can't sleep easy», *Fortune*, 10 de febrero de 2026. Paráfrasis del autor. <https://fortune.com/2026/02/10/ai-agents-anthropic-openai-arent-killing-saas-salesforce-servicenow-microsoft-workday-cant-sleep-easy/>
[^klarna]: Julie Bort, «Klarna CEO doubts that other companies will replace Salesforce with AI», *TechCrunch*, 4 de marzo de 2025. Declaraciones de Sebastian Siemiatkowski. <https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai>
[^nadella]: Satya Nadella, entrevista en el pódcast *BG2*, diciembre de 2024, citada y analizada en César Obach-Renner, *AgencyDomains: Arquitectura Agentiva*, capítulo 1, «La Línea Nadella».
[^fallout]: TM Forum, *How order management is evolving to embrace agentic AI*, 2026, pp. 2-3. Informe patrocinado por Amdocs.
