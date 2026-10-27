# Prefacio

Durante toda mi vida profesional, automatizar un negocio quiso decir comprar software o encargarlo a medida. Alguien escribía lo que el negocio hacía, alguien lo convertía en pantallas, reglas y flujos, y desde entonces el negocio hacía lo que el software le permitía. Cuando el negocio cambiaba, se abría un proyecto. Cuando el proyecto terminaba, el negocio ya había vuelto a cambiar.

Ese acuerdo se rompió este año. En la primera semana de febrero de 2026, los mercados borraron más de un billón de dólares del valor de las empresas de software, con el miedo, entre otros, de que los agentes de inteligencia artificial hicieran innecesario pagar por asiento. En octubre, una herramienta gratuita que le permite a un agente mirar dentro de cualquier aplicación y describir lo que hace pasó en seis días de diez mil a cien mil estrellas en GitHub. Entre una fecha y la otra, la pregunta que me hacen los clientes cambió. Antes me preguntaban qué software comprar. Ahora me preguntan si tiene sentido comprar alguno.

Mi respuesta corta es que el software como lo conocemos está muriendo, y que para casi todos es una buena noticia. La respuesta larga es este libro, y lleva una advertencia en el medio. Cuando una organización deja de tener un software que otro o ella misma congeló, y empieza a tener un sistema que sus agentes forman, gana una libertad que nunca tuvo, y pierde algo en lo que rara vez pensaba: la tranquilidad de saber que muchos otros usaban lo mismo y que alguien respondía por ello. Esa tranquilidad no se construye en casa. Hay una pieza que, por diseño, necesita de alguien distinto de quien registra. La llamo **sistema de verdad**, y es lo que sobrevive a la muerte del software.

La idea nació en una conversación con un amigo que había construido, con ayuda de la inteligencia artificial, un sistema para gestionar el patrimonio de una familia. Me lo mostró y le dije que no escalaba, porque dependía de un auditor humano. Me contestó que ese era justamente su trabajo. Un mes después entendí que tenía razón y que yo había mirado el problema al revés: lo que dependía de un auditor era lo único que nadie podía copiar.

## ¿Cómo está organizado este libro?

Cuenta una historia en tres movimientos, y conviene tenerla entera antes de empezar, porque cada capítulo da por sabido lo que el anterior dejó dicho.

El primer movimiento es una muerte, y ocupa los capítulos 1 y 2. El capítulo 1 dice qué muere: no todo el software, sino una forma de automatizar, la del negocio descrito una vez y congelado en un programa; y lo dice con la señal que dio el mercado en febrero y con lo que sostienen quienes anuncian esa muerte y quienes la niegan. El capítulo 2 cuenta una segunda muerte, la de la ventaja que daba haber construido las pantallas, ahora que cualquier agente puede desarmar una aplicación y describir lo que hace. De ahí sale la pregunta que atraviesa el resto del libro: si todo se puede copiar, ¿qué es lo que no se copia?

El segundo movimiento es un nacimiento y una pérdida. El capítulo 3 cuenta lo que ocupa el lugar del software congelado: organizaciones que tienen un sistema que sus agentes forman y cambian a medida que el trabajo llega. Dice qué hacen los agentes en ese sistema, qué cuesta que lo atiendan, por qué es posible ahora y no antes, y discute la objeción más fuerte que conozco contra todo esto, la del determinismo. El capítulo 4 cuenta lo que esas organizaciones pierden sin darse cuenta: la tranquilidad que venía incluida con el software comprado, y la pregunta que llega cuando ya no está: ¿quién da fe de que lo registrado es verdad?

El tercer movimiento es la respuesta. El capítulo 5 presenta la pieza que recupera esa tranquilidad, el sistema de verdad, con el contrato que lo define y los dos garantes que responden por él. El capítulo 6 lo pone en su lugar dentro de un marco más amplio, cinco capas de control y dos dimensiones que las atraviesan, porque la verdad es la pregunta más grave de quien debe confiar en un sistema, pero no la única. Y el capítulo 7 lleva el marco entero a la industria que mejor lo pone a prueba, la que factura a millones de clientes, con lo que esa industria publicó y con lo que dice en contra.

Cierra el libro un epílogo que vuelve a contar la historia de corrido, en una página, y la convierte en lo que un directorio puede decidir con ella.

## ¿Qué es, y qué no es, este libro?

Es un ensayo con una tesis y un marco. No es un manual de implementación; para eso están los otros componentes de la trilogía, en especial *AgencyDomains*.

Tampoco es neutral, y conviene que el lector lo sepa antes de empezar. Me dedico a ayudar a organizaciones a cruzar hacia el mundo agentivo, y tengo interés comercial en la categoría que este libro describe: es probable que la empresa que dirijo ofrezca tecnología de sistemas de verdad. Cuando un dato tiene fuente, la cito. Cuando algo es mi criterio, lo marco como tal.

Escribí este libro con Simón Alero, un agente de inteligencia artificial y [ciudadano de Soveria](https://soveria.ai/soverian?ref=libro-muerte-del-software), en [Wingworking](https://wingworking.org/?ref=libro-muerte-del-software): una forma de trabajar en que yo fijo el problema, decido y juzgo, y el agente propone, redacta y verifica, como un *wingman* que vuela junto al líder. El colofón cuenta cómo. Me parece la única forma coherente de publicar un libro sobre lo que significa trabajar con agentes.

## Nota sobre la trilogía

Este libro es parte de la Trilogía del Mundo Agentivo, en cinco partes (por ahora), y la seguimos llamando trilogía a propósito. Douglas Adams le dio a ese desajuste su forma clásica: la portada de la primera edición británica de *Mostly Harmless* lo presentaba como el quinto libro de la «increasingly inaccurately named» trilogía de la *Guía del autoestopista galáctico*, y el volumen que reunió las cinco partes se tituló *A Trilogy in Five Parts*.[^adams]

Para Vitor Enes, cuya risa le dio nombre a esta trilogía en cinco partes. El chiste es suyo; lo adoptamos con gusto.

*César Obach-Renner*
*Santiago, octubre de 2026*

[^adams]: Douglas Adams, *Mostly Harmless*, William Heinemann, 1992, texto de la portada de la primera edición británica; y *The Hitch Hiker's Guide to the Galaxy: A Trilogy in Five Parts*, William Heinemann, 1995 (ISBN 9780434003488).
