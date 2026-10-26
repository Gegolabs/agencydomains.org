# Glosario

Los términos de este libro, en una línea cada uno. El desarrollo de cada término vive en el capítulo indicado. Los términos que la trilogía ya definió, como la Línea Nadella o Trust Infrastructure, conservan su definición en el libro que los acuñó; aquí se repite, en una línea, la de los que este libro usa más.

**software como lo conocemos** — El negocio congelado en un software: descrito una vez, y cambiado solo cuando alguien abre un proyecto. Da lo mismo cómo se tenga: arrendado como servicio, licenciado y operado en la propia infraestructura o en la propia nube, o desarrollado a medida. Es lo que muere; no muere todo el software. *(Capítulo 1.)*

**segunda fase** — El tramo del cruce en que, con la lógica del negocio ya en la capa de agentes, las organizaciones empiezan a reemplazar los propios sistemas de debajo. La primera fase colapsa la interfaz; la segunda, la forma de tener el software: el negocio descrito una vez y cambiado por proyecto. *(Capítulo 1; la primera fase, en AgencyDomains.)*

**lectura agéntica** — La forma de entender que un agente construye y cambia el sistema en que el agente es un programador más rápido: lo que sale de él es una aplicación que persiste y que alguien despliega y mantiene. Toma su nombre del mundo agéntico de *AgencyDomains*. *(Capítulos 3 y 7.)*

**lectura agentiva** — La forma de entender que un agente construye y cambia el sistema en que nadie lo programa de antemano: el agente atiende el trabajo y cristaliza lo que se repite en piezas propias, su memoria muscular. Es la de este libro. Toma su nombre del mundo agentivo de *AgencyDomains*. *(Capítulos 3 y 7.)*

**Botlet** — Una pieza que el agente ejecuta de memoria: código que resuelve siempre igual lo que se repite, sin consultar ningún modelo. Es la memoria muscular del agente y es suya: la forma, la mantiene y la sustituye él, aunque hoy el cuerpo de la pieza de partida lo escribe quien mantiene el catálogo. El término es de *AgencyDomains*. *(Capítulo 3.)*

**Agentlet** — La pieza hermana del Botlet para lo que se repite en su forma pero pide juicio en cada caso: lleva un encargo declarado y un modelo dimensionado a la tarea, no el más grande, con presupuesto por ejecución, y escala cuando no está segura. También es del agente. El término es de *AgencyDomains*. *(Capítulo 3.)*

**escalera de tres peldaños** — La forma de ordenar el trabajo del agente por lo que cuesta atenderlo: el Botlet (código, sin modelo), el Agentlet (un modelo dimensionado a la tarea, con presupuesto) y el razonamiento pleno (el modelo de frontera, reservado para lo nuevo). Ordena tres cosas: el costo, el tiempo de respuesta y la dependencia de proveedores ajenos. Dice dónde debería bajar el costo, no cuánto. *(Capítulo 3.)*

**Wingworking** — La práctica de trabajo entre una persona y un agente de inteligencia artificial con que se escribió este libro: la persona fija el problema, decide y juzga; el agente propone, redacta y verifica, como un *wingman* que vuela junto al líder. *AURA* la describe como el paso de usar la inteligencia artificial como asistente a delegarle trabajo. *(Prefacio y colofón.)*

**wingcoding** — Wingworking aplicado a construir software: la persona especifica y decide como arquitecto, y el agente programa. Es de donde nació la práctica. *(Capítulo 1.)*

**arnés** — El entorno en que trabaja un agente: las herramientas, los permisos, la memoria y las reglas que lo rodean mientras atiende el trabajo. *(Capítulo 1.)*

**plantilla que cobra vida** — El punto de partida de un sistema propio: se instala completo y, desde el primer día, su dueño lo evoluciona con IA hasta que deja de ser la plantilla. *(Capítulo 3.)*

**trabajo que nunca se especificó** — El trabajo que ocurre alrededor de los sistemas y que hoy resuelven las personas a mano, porque el software solo automatiza lo que alguien especificó de antemano. *(Capítulos 1 y 3.)*

**tranquilidad comprada** — Lo que venía incluido al comprar software y nadie anotaba en el presupuesto: que muchos otros lo usaban, y que alguien respondía por él. Se nota recién cuando falta. *(Capítulo 4.)*

**sistema de registro** — El sistema que guarda la versión oficial de un dato. Es lo que sobrevive al cruce. *(Capítulos 4 y 5.)*

**sistema de verdad** — Un sistema de registro que, además, garantiza que lo registrado es verdad, mediante un contrato con quienes lo usan y con dos garantes. Es siempre una pieza de tecnología, y la opera quien la usa. *(Capítulo 5.)*

**dos garantes** — Quienes responden por el contrato de un sistema de verdad: el proveedor de la tecnología, que responde por que cumpla las seis propiedades, y quien atestigua, independiente de quien registra, que verifica los registros. Con solo el primero se vuelve a confiar en el proveedor; con solo el segundo se audita lo que pudo sobrescribirse. *(Capítulo 5.)*

**contrato de verdad** — La promesa escrita, verificable y respaldada de un sistema de verdad, en el sentido técnico de acuerdo entre partes. Promete seis propiedades: no se borra, se corrige; el origen es trazable; es verificable por un tercero; es conciliable; habla un lenguaje común; y declara su grado de verdad. *(Capítulo 5.)*

**grado de verdad** — El estatus de cada asiento de un sistema de verdad: declarado por alguien, verificado contra su fuente o inferido. No es un nivel de calidad: la calidad exigible es una sola. *(Capítulo 5.)*

**quien atestigua** — El segundo garante del contrato: verifica los registros de forma independiente de quien registra. Puede ser un auditor humano o un proceso automático; nunca la misma organización que registra. *(Capítulos 4 y 5.)*

**capas de control** — Las cinco capas que hacen confiable lo que se construye con agentes, cada una con la pregunta que responde: la verdad, la identidad y la autoridad, el movimiento, la medición y el criterio. No son las cuatro capas de la arquitectura de AgencyDomains. *(Capítulo 6.)*

**la verdad (capa)** — La primera capa de control: el sistema de verdad, con sus dos garantes, para los registros de los que la organización responde ante otros. Responde si los números y los registros son correctos. *(Capítulo 6.)*

**la identidad y la autoridad (capa)** — La segunda capa de control: cada agente con identidad propia, permisos explícitos y alguien en cuyo nombre actúa, y cada acto con una persona o un área que responde por él. *(Capítulo 6.)*

**el movimiento (capa)** — La tercera capa de control: los agentes y la plataforma en que corren, con supervisión humana y una autonomía que se concede por grados, proceso por proceso. *(Capítulo 6.)*

**la medición (capa)** — La cuarta capa de control: cada agente se prueba contra casos conocidos antes de operar y se sigue midiendo mientras opera. La confianza en un agente no se declara: se mide. *(Capítulo 6.)*

**el criterio (capa)** — La quinta capa de control: los estándares de la industria como punto de partida y un equipo de arquitectura que decida qué debe existir y pueda juzgar lo que el agente forma, aunque no lea el código. Es la defensa contra el callejón sin salida. *(Capítulo 6.)*

**las personas (dimensión)** — La condición que atraviesa las cinco capas de control: quién opera cada capa y gobierna su evolución, y con qué formación. *(Capítulo 6.)*

**la reversa (dimensión)** — La condición que atraviesa las cinco capas de control: qué pasa cuando algo falla y cómo se vuelve atrás sin detener el negocio. No es la reversibilidad personal del modo agentivo. *(Capítulo 6.)*
