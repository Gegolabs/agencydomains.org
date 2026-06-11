# 1. Trabajar sin abrir aplicaciones

*En la película: la superficie del comparativo de rutas, que apareció para una decisión y murió con ella; el briefing que nadie diagramó; el análisis que Elena declinó para hacerlo a lápiz. Nadie abrió una aplicación en todo el martes — y ninguna pantalla fue menos rica por eso.*

## La intención reemplaza a la operación

La primera liberación es la más visible y la más documentada, de modo que este capítulo la establece con brevedad: en el mundo agentivo, las personas no operan aplicaciones. No abren un procesador de texto para producir una carta, ni una hoja de cálculo para producir un análisis, ni una herramienta de BI para responder una pregunta de negocio. Expresan la intención a su agente — "responde que sí y confirma la fecha", "muéstrame el avance del reporte", "¿cómo van las ventas del trimestre contra el anterior?" — y el agente produce el artefacto o la respuesta.

El trabajo deja de incluir la operación de software como peaje. Lo que esa capa devuelve es **flujo**: la continuidad del pensamiento que el paradigma anterior trituraba a golpe de abrir, buscar, alternar, copiar y pegar entre ventanas. La pregunta de productividad cambia de "¿domina usted la herramienta?" a "¿sabe usted qué quiere?".

## Generada, no compilada

La objeción inmediata — la más frecuente y la más equivocada — es que esto suena a regresión: ¿volver a interfaces de texto, como en los años ochenta?

La respuesta exige una distinción precisa. Lo que define al mundo agentivo no es la ausencia de interfaz gráfica sino la ausencia de interfaz **compilada**. La interfaz existe, y es rica: cuando hay que comparar, aparece una tabla; cuando hay que ver una tendencia, un gráfico; cuando hay que aprobar, un formulario con su trazabilidad. Pero esas superficies no pertenecen a ninguna aplicación: el agente las **genera** para la interacción que las necesita, con la forma óptima para ese momento, y las descarta al terminar. La conversación es el modo de *entrada* del humano; la salida del agente es lo que el momento requiera.

El contraste puede resumirse en cuatro dimensiones:

| | Interfaz compilada | Interfaz generada |
|---|---|---|
| ¿Quién la diseña? | Un equipo humano, una vez | El agente, en cada interacción |
| ¿Cuándo existe? | Siempre (la aplicación instalada) | Solo mientras sirve |
| Forma | Fija — el usuario se adapta a ella | Óptima para el caso — ella se adapta al usuario |
| Costo de cambio | Un proyecto de desarrollo | Ninguno: la próxima generación ya es distinta |

El mundo agentivo es, por tanto, *más* visual que el de las aplicaciones, no menos. Lo que la interfaz perdió no es riqueza: es rigidez.

## Lo que este libro no repite

La formalización de esta capa — las primitivas de la interfaz generada, su arquitectura de cuatro capas, la infraestructura de confianza que la gobierna — es la materia de *AgencyDomains*, el libro de arquitectura de esta trilogía, y no la duplicaremos. Para el argumento que sigue basta retener dos cosas: que la generación de artefactos e interfaces bajo demanda es el comportamiento normal del mundo que describiremos, y que la misma capacidad que genera una tabla puede generar algo más consecuente — el mensaje correcto, para la persona correcta, en el formato de esa persona. Esa extensión, de la interfaz a la comunicación, es la segunda liberación y el corazón de este libro.

> **Lo esencial**
>
> - En el mundo agentivo no se operan aplicaciones: se expresan intenciones y el agente produce el artefacto.
> - La interfaz no desaparece — deja de estar compilada: se genera por interacción, con la forma óptima, y se descarta.
> - La primera liberación protege el flujo; su formalización completa vive en *AgencyDomains*.
