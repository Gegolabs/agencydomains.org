# 6. Las cinco capas de control

El sistema de verdad responde la pregunta más grave del directorio, pero no la única. Cuando una organización pone agentes a operar sobre su negocio, quien tiene que confiar en ellos pregunta varias cosas, y cada pregunta pide su control. Las ordeno en cinco **capas de control**, siempre con ese adjetivo, para no confundirlas con las cuatro capas de la arquitectura que describe *AgencyDomains*: aquellas dicen cómo se arma un sistema; estas, qué necesita saber quien debe confiar en él. Son mi criterio, no un estándar de la industria. Se apoyan en los estándares que existen y en los controles que las industrias más exigentes ya piden antes de dejar actuar a la inteligencia artificial sin intervención humana.

## ¿Cuáles son?

**1 · La verdad.** *¿Los números y los registros son correctos?* Es el sistema de verdad del capítulo 5, con su contrato y sus dos garantes, para los registros de los que la organización responde ante otros. Es la capa de control que no debería certificarse a sí misma.

**2 · La identidad y la autoridad.** *¿Quién actuó, en nombre de quién, y quién responde?* Cada agente tiene identidad propia, actúa con permisos explícitos y en nombre de alguien, y cada acto tiene una persona o un área que responde por él. Sin esta capa de control, la trazabilidad de la primera registra actos sin dueño.

**3 · El movimiento.** *¿Qué hacen los agentes, y hasta dónde deciden solos?* Los agentes y la plataforma en que corren, con supervisión humana y una autonomía que se concede por grados, proceso por proceso, como se le concede a una persona nueva en un trabajo. Ojo con el nombre: esta capa de control no es la Capa 3 de la arquitectura de *AgencyDomains*, que es una capa del sistema; aquí la pregunta es la de quien observa lo que los agentes hacen.

**4 · La medición.** *¿Cómo sabemos que lo hacen bien, hoy y mañana?* Cada agente se prueba contra casos conocidos antes de operar, y se sigue midiendo mientras opera, con alarmas cuando su desempeño se degrada.

**5 · El criterio.** *¿Lo estamos construyendo bien, y podemos cambiar de rumbo?* Los estándares de la industria como punto de partida, y un equipo de arquitectura que decida qué debe existir y con qué estándares, y que pueda juzgar lo que el agente forma por su comportamiento, sus pruebas y su rastro, aunque no lea el código. Uso «criterio» en el sentido de juicio técnico de quien construye; no es el «criterio delegado» con que *La Empresa en Tiempo Real* describe al agente.

Leídas juntas, se reparten los riesgos del capítulo 4. La quinta evita el callejón sin salida y acota el retraso. La primera y la cuarta responden por la calidad. La segunda y la tercera hacen gobernable la automatización.

## ¿Qué atraviesa las cinco?

Dos condiciones que cada capa de control tiene que cumplir.

**Las personas**: quién opera cada capa y gobierna su evolución, y con qué formación. Una construcción cuyo comportamiento no entiende nadie de la organización repite la dependencia que la organización quería dejar al dejar de comprar software.

**La reversa**: qué pasa cuando algo falla, y cómo se vuelve atrás sin detener el negocio. No tiene que ver con la reversibilidad personal del modo agentivo de *La Empresa en Tiempo Real*, que es la de una persona que entra y sale del mundo agentivo con un gesto.

| Capa de control | Las personas | La reversa |
|---|---|---|
| 1 · La verdad | Los responsables de cada registro | Una corrección es un registro nuevo |
| 2 · La identidad y la autoridad | Quien concede y retira los permisos | Un permiso se retira en el acto, y lo hecho con él queda trazado |
| 3 · El movimiento | Los supervisores de cada proceso | Detener, pausar o revertir; seguir en modo manual |
| 4 · La medición | Quien define las pruebas y atiende las alarmas | El agente que se degrada pierde autonomía |
| 5 · El criterio | El equipo de arquitectura | Un componente puede reemplazarse sin rehacer el resto |

Cada celda es una pregunta que una organización puede hacerse sobre su propio sistema o sobre cualquier oferta que reciba.

## ¿Cómo se corresponden con Trust Infrastructure?

*AgencyDomains* define Trust Infrastructure con cinco pilares: gobernanza, auditoría, validación, resiliencia y transparencia.[^pilares] Las capas de control miran el mismo terreno desde quien tiene que confiar, en vez de desde quien construye. Mi lectura de la correspondencia:

| Capa de control | Pilares de Trust Infrastructure que la sostienen |
|---|---|
| 1 · La verdad | Auditoría, más el contrato, el grado de verdad y el segundo garante |
| 2 · La identidad y la autoridad | Gobernanza |
| 3 · El movimiento | Gobernanza y resiliencia |
| 4 · La medición | Validación y transparencia |
| 5 · El criterio | Ninguno: es una condición de quien construye |

## ¿Vale también para lo que no se construye con agentes?

Sí, y por eso me parece un buen marco. Una suite licenciada y operada en casa cumple la primera capa de control con su propio núcleo de registros, y su proveedor responde por él. Cuando la misma suite agrega agentes, como están haciendo todos los proveedores, le aplican las otras cuatro igual que a una construcción propia. El marco le pide a cada forma de solución que responda las mismas preguntas. Si la suite es un servicio arrendado, quien opera ese núcleo es el proveedor, y entonces no es todavía un sistema de verdad en el sentido del capítulo 5, que lo opera quien lo usa: el segundo garante hace más falta, no menos. El desarrollo a medida responde las cinco igual que cualquier otra forma, y suele fallar en la primera: quien lo hizo y quien lo audita son la misma organización.

Lo que cambia es cuál cuesta más. A quien arrienda, suele costarle la tercera capa de control, porque los agentes que el proveedor agrega corren en su nube y se gobiernan con sus reglas. Mi observación, sin medirla: a quien licencia y opera en casa le cuesta menos, porque ve dónde corren y qué hacen. A quien construye, la primera.

[^pilares]: César Obach-Renner, *AgencyDomains: Arquitectura Agentiva*, capítulo 5, «Trust Infrastructure», «Los cinco pilares».
