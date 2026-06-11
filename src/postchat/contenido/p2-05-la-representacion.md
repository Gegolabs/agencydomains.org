# 5. El agente que da la cara por ti

*En la película: las 15:00. Andrés estaba en una subestación sin señal, exactamente donde debía estar, y su agente respondió por él — con sus condiciones, y con un límite: "es un compromiso que él hizo y no delegaría su palabra". Este capítulo explica qué madurez hace posible esa escena, y quién responde por ella.*

## Dos interfaces de un mismo agente

La conversación de la industria sobre "gemelos digitales" de las personas imagina, por lo general, dos sistemas: el asistente personal que te sirve, y el gemelo que te representa — el segundo como un proyecto futuro, separado, a construir "cuando la tecnología madure". La tesis de este capítulo es que esa imagen está equivocada en lo esencial: **son el mismo actor con dos interfaces**.

La **interfaz interna** mira hacia el usuario: media entre él y los sistemas, administra su atención, ejecuta sus intenciones — todo lo descrito en los capítulos 2 a 4. La **interfaz externa** mira hacia los demás: responde consultas en nombre del usuario, sostiene sus criterios, decide lo que él delegó.

No hay dos construcciones, hay **una maduración**. Un agente que lleva meses mediando la comunicación de su usuario — observando cómo prioriza, qué condiciones pone, qué delega y qué jamás — ya es un representante en estado embrionario. La pregunta de diseño no es "¿construimos el gemelo?" sino **"¿cuándo sabe lo suficiente como para dar la cara?"**. Y la transición no es un proyecto: es una habilitación — el mismo agente, el mismo contexto acumulado, una nueva interfaz expuesta.

La consecuencia gerencial de esta tesis es inmediata: la representación no se compra, **se cultiva**. Cada mes de operación en modo agentivo es el dataset de entrenamiento de la futura capacidad de representación. La organización que pospone la segunda liberación pospone, sin saberlo, la tercera.

## El espectro de madurez

Ningún agente nace representando. La capacidad progresa por un espectro de cuatro estadios, y lo que separa cada uno del siguiente no es tecnología — es contexto acumulado y confianza otorgada:

| Estadio | ¿Qué hace el agente? | ¿Quién actúa? |
|---|---|---|
| **Asistente** | Ayuda dentro de la tarea: redacta, resume, busca | La persona, en cada interacción |
| **Mediador** | Asume la logística comunicacional completa (capítulos 2–4) | La persona decide; el agente transporta |
| **Representante en consulta** | Responde por su usuario ante otros: informa posiciones, verifica condiciones, anticipa criterios | El agente informa; la palabra final es de la persona |
| **Representante con delegación** | Decide y ejecuta dentro de parámetros explícitos: aprueba lo menor, agenda lo rutinario, responde lo frecuente | El agente, dentro del marco; la persona revisa y puede revertir |

El orden es innegociable: nadie delega su firma en un agente que no ha demostrado, durante meses de mediación, que entiende cómo piensa su usuario.

<!-- FIG:f04-espectro-representacion -->
![El espectro de madurez de la representación](figuras/f04-espectro-representacion.png)

Un ejemplo basta para fijar el estadio tercero. Un gerente está en campo, sin señal — exactamente donde debe estar. Una directora necesita saber si su programa de mantenimiento tolera un desplazamiento de cuarenta y ocho horas. Consulta al agente del gerente, que responde con la holgura verificada, las dos condiciones que su usuario pondría — y un límite: una de esas condiciones involucra un compromiso personal que el gerente hizo, y el agente la marca como no delegable, ofreciendo dejar el cambio pre-aprobado para ratificación. Esa frase — *esto no me toca decidirlo a mí* — es la marca del representante maduro: sabe, sobre todo, lo que no le corresponde.

## Las preguntas incómodas

**¿Puede un agente representar fielmente a una persona?** No perfectamente — y la pregunta está mal calibrada. Un asistente ejecutivo humano tampoco representa perfectamente a su jefe, y las organizaciones funcionaron sobre esa imperfección durante un siglo. La utilidad de la representación no exige perfección: exige acertar en lo delegado y **escalar lo que lo excede**. El diseño correcto no persigue el cien por ciento de fidelidad sino el cien por ciento de honestidad sobre los límites.

**¿Quién responde cuando el agente se equivoca?** El que delegó — exactamente como cuando se delega en un subalterno. Si el agente aprueba un gasto menor dentro de la política definida y resulta un error, la responsabilidad es de quien definió la política. El caso difícil es el restante: el agente que actúa *fuera* de sus parámetros, por falla o por interpretación. Ahí la responsabilidad se vuelve difusa, y por eso la delegación exige un marco previo: límites explícitos, trazabilidad completa de cada actuación en nombre de otro, y la regla por defecto de que ante la ambigüedad se escala. **La delegación sin marco no es madurez — es negligencia con interfaz amable.**

**¿Qué sabe mi agente de mí — y quién decide el perímetro?** La representación se alimenta del contexto acumulado, y eso vuelve urgente una frontera que el paradigma anterior nunca necesitó nombrar: la **privacidad frente al propio agente**. La regla de este mundo es que el perímetro lo decide la persona, no el sistema, y se declara en el momento: lo que se marca *fuera de registro* no entra al modelo que el agente tiene de ti — verificablemente — y por tanto tampoco a lo que tu representante sabe, dice o usa en tu nombre. La escena de los zapatos es el caso doméstico de un principio serio: un representante fiel no es el que lo sabe todo de ti — es el que sabe exactamente lo que tú decidiste que supiera.

**¿Y la disponibilidad no era una virtud?** La oficina del canal confunde disponibilidad con compromiso: quien contesta a las once de la noche "está puesto". La tercera liberación propone la medida inversa de salud organizacional: que la gente pueda estar **en un solo lugar a la vez** — en campo, en la decisión importante, en su casa — sin que la organización se detenga ni se lo cobre. La representación no reemplaza a las personas: les devuelve el derecho a no ser ubicuas.

> **Lo esencial**
>
> - Asistente y "gemelo" no son dos sistemas: son dos interfaces de un mismo agente que madura.
> - El espectro tiene cuatro estadios — asistente, mediador, representante en consulta, representante con delegación — y el orden no se salta.
> - La representación se cultiva con meses de mediación; posponer la segunda liberación pospone la tercera.
> - La delegación exige marco: límites explícitos, trazabilidad, escalamiento ante la duda. La responsabilidad es de quien delega.
> - El perímetro de lo que el agente sabe de ti lo decides tú, y se declara: lo "fuera de registro" no entra a tu modelo ni a tu representación.
