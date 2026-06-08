## Facetas

Las primitivas que las cinco secciones anteriores describieron — AgencyDomain, Botlet, Capability, Trust Infrastructure, Asistente vs Agente Autónomo — viven principalmente en las Capas 2, 3 y 4 de la Arquitectura Agentiva. La Capa 1 (Interacción) había quedado sin una primitiva propia: solo descrita como **regímenes de generación** (Capítulo 4 §1) y como **composición de Botlets de presentación** (shell, vista, operación). Faltaba nombrar la pieza atómica con que esas superficies se construyen.

Esta sección formaliza la **Faceta** como **sexta primitiva canónica** — la unidad mínima de la Capa 1, instrumento que el agente invoca durante conversación o ensambla en Botlets de presentación.

> *El Botlet es memoria muscular del agente. La Faceta es instrumento que el agente toma mientras piensa.*

### Definición

Una **Faceta** es un componente atómico reusable de la Capa 1 (Interacción) que ofrece al usuario una forma específica de interacción no conversacional: una pizarra de dibujo a mano alzada, un catálogo-selector, una matriz de colores, un calendario, un mapa clickeable, un slider, un ordenamiento drag-and-drop, un selector de archivos, una vista de canvas configurable. Una de las muchas caras que la interacción con el usuario puede tomar en un momento dado.

La Faceta es **instrumento**, no proceso. Vive y opera en la Capa 1. Es invocada por la cognición durante interacciones activas o ensamblada por Botlets de Capa 1 (shells y vistas) como pieza de su composición interna.

<!-- FIG:g14-faceta-vs-botlet -->
![Faceta vs Botlet · dos primitivas, dos capas, dos naturalezas](figuras/g14-faceta-vs-botlet.png)

### Faceta vs Botlet — la distinción canónica

La Faceta y el Botlet son las dos primitivas de software del agente. Se confunden fácil porque ambas son piezas con identidad propia que el agente usa para hacer cosas. La distinción canónica:

| Eje | **Faceta** | **Botlet** |
|---|---|---|
| **Capa** | Capa 1 (Interacción) | Capa 3 (Autonomía) |
| **Naturaleza** | Instrumento de interacción | Memoria muscular del agente |
| **¿Cuándo opera?** | Durante conversación activa | En background, sin cognición presente |
| **Activación** | Cognición la invoca explícitamente | Pattern Recognition o llamado externo |
| **Garantía de fallback** | NO — si falla, agente vuelve a texto | SÍ — la cognición ejecuta manualmente |
| **Ciclo de vida** | Efímera (vive lo que dura la tarea) | Persistente entre sesiones |
| **Regeneración** | No tiene ciclo de regeneración | Ciclo `95/4/1` con regeneración |
| **Fases de madurez** | No aplica | Junior · en aprendizaje · senior |
| **Reutilización** | Catálogo plano de instrumentos | Catálogo por capacidad y dominio |

La diferencia ontológica importa: **el Botlet automatiza; la Faceta interactúa**. Un Botlet ejecuta saber consolidado sin participación humana inmediata. Una Faceta abre un canal de comunicación visual-manipulativa con un humano que está activo en la conversación.

### Dos usos canónicos

#### Uso 1 · Invocación directa por la cognición

El agente, durante una conversación, **decide** que la información que necesita del usuario se obtiene más rápido a través de una Faceta que continuando el diálogo verbal. Compone una superficie efímera con una o varias Facetas, la presenta al usuario, recibe la información, y la conversación continúa. La superficie efímera **no es un Botlet** y no persiste — vive lo que dura la tarea inmediata.

Este uso realiza directamente el régimen **GUI generada on-the-fly** del Capítulo 4 §1. La Faceta es la pieza que materializa ese régimen.

#### Uso 2 · Composición en Botlets de presentación

Los Botlets de **shell** y **vista** (Capítulo 4 §1, *Composición de la Capa 1*) ensamblan Facetas como piezas internas de su construcción. La vista de "detalle de pedido" usa la Faceta de "matriz de productos" + la Faceta de "calendario" + la Faceta de "selector de cliente". El Botlet de vista define la orquestación, el layout, el flujo de datos entre piezas; las Facetas son los instrumentos individuales que el Botlet pone en la pantalla.

Este uso permite que las superficies persistentes (régimen 3 del Capítulo 4 §1) se construyan reutilizando catálogo de Facetas, sin que cada Botlet de vista tenga que reinventar cada componente atómico.

### Interacción declarada acotada

Una pieza de información ya materializada — un snapshot autocontenido que el agente forjó en su tiempo de Ingeniería — puede portar interacción sobre sus propios datos sin dejar de ser una pieza reproducible. Pero no toda interacción es del mismo tipo. La **interacción declarada acotada** es la categoría que separa lo que una pieza puede ofrecer de lo que pertenece a otra primitiva.

La distinción se traza entre dos interactividades:

- La **exploración libre** lanza queries nuevas y arbitrarias al origen (drill o pivot ad-hoc), opera sobre un espacio abierto, pierde reproducibilidad, excede `G1` y vive fuera del proto-Botlet de información — en otro Botlet o en la cognición misma. Una pieza de información **MUST NOT** absorberla.
- La **interacción declarada acotada** opera sobre el snapshot ya materializado, dentro de un espacio declarado (dimensiones y valores acotados de antemano), mantiene la reproducibilidad, es `G1` —configuración, no código— y vive en la pieza misma, realizada vía Faceta.

| ¿Qué las distingue? | Exploración libre | Interacción declarada acotada |
|---|---|---|
| Query nueva al origen | sí, arbitraria (drill/pivot ad-hoc) | no — opera sobre el snapshot ya materializado |
| Espacio de interacción | abierto | declarado (dimensiones y valores acotados) |
| Reproducibilidad | se pierde | se mantiene (misma config + datos → mismo artefacto + mismo set de controles) |
| Generación | excede `G1` | `G1` (es configuración, no código) |
| ¿Dónde vive? | otro Botlet / cognición (Capa 2 + Capa 1) | en la pieza misma, vía Faceta |

#### Faceta embebida

El mecanismo que realiza la interacción declarada acotada ya es canónico: es la composición de Facetas (Uso 2), aplicada hacia adentro de una pieza materializada. Es la **pieza** la que compone la Faceta — no la Faceta la que compone otras —; la Faceta sigue siendo atómica. Una **Faceta embebida** es una Faceta acotada a una dimensión declarada de los propios datos de la pieza — un filtro, un segmentador, un selector de apariencia. Al activarla, los elementos *data-bound* de la pieza —KPIs y medidas como agregaciones declaradas (`sum`, `ratio`, y similares) sobre el dataset embebido, distribuciones, semáforos— se **recomputan client-side** sobre el subconjunto filtrado: la agregación se declara una vez y se reevalúa al cambiar el subconjunto. La cognición no explora; la Faceta filtra el snapshot.

El caso testigo es un dashboard de asistencia con filtro por área: el usuario elige una o varias áreas y la pieza recalcula sus KPIs y su semáforo sobre el subconjunto.

Esto reconoce un tercer uso de la Faceta — extensión del Uso 2 hacia la pieza materializada —: la distinción Faceta vs Botlet admite este tercer uso sin alterar la naturaleza de la Faceta, que sigue siendo efímera y sin garantía de fallback. Lo nuevo es que la pieza puede componerla para interacción acotada, además de la invocación por la cognición durante conversación.

### Comportamiento agentivo asociado

La existencia de la Faceta como primitiva canónica habilita un comportamiento agentivo específico: el agente, durante una conversación, **estima en tiempo real** si la información que necesita se obtiene mejor verbalmente o visualmente. Cuando estima que la vía visual gana, ofrece una Faceta apropiada.

El cálculo es cognitivo del agente, no feature pre-programada del producto. La Faceta como primitiva habilita la decisión; la heurística la ejerce.

#### Heurísticas canónicas para invocación

| Naturaleza de la información | Modalidad recomendada |
|---|---|
| Baja dimensionalidad + bien estructurada (un sí/no, una fecha, un número) | Conversación |
| Alta dimensionalidad (múltiples campos relacionados) | Faceta de formulario o composición |
| Difícil de verbalizar (color, posición, forma, gesto) | Faceta especializada (matriz de colores, mapa, dibujo) |
| El usuario ya la tiene en forma espacial o visual (un layout, un mapa, un dibujo en papel) | Faceta que reciba esa forma directamente |
| Comparación entre opciones múltiples | Faceta de catálogo-selector con vista comparativa |
| Configuración con muchas dimensiones independientes | Faceta de panel con sliders y toggles |
| Trabajo creativo abierto (no respuesta a pregunta cerrada) | Faceta de canvas o lienzo |

#### Anti-heurísticas (cuándo NO ofrecer Faceta)

- Cuando la pregunta es genuinamente cerrada y verbal — ofrecer Faceta agrega fricción, no la reduce.
- Cuando el usuario está en un canal sin capacidad gráfica (voz pura, IVR, SMS) — la Faceta no es invocable.
- Cuando el costo de cargar la Faceta supera el beneficio de la interacción visual (interacciones de un solo paso, datos triviales).
- Cuando la conversación está en flujo y la Faceta interrumpe inadecuadamente.

El agente que aprende a calibrar estas decisiones — cuándo ofrecer, cuándo no — opera en una Capa 1 plena. El que solo conversa se queda en la mitad del rango interactivo posible.

Cuando una Faceta se compone dentro de una pieza materializada (interacción declarada acotada), la decisión deja de ser conversacional y pasa a ser parte de la configuración de la pieza: el agente declara el espacio de controles en tiempo de Ingeniería, preservando la **reproducibilidad** —propiedad MUST del artefacto de información— ya establecida arriba.

### Anatomía de la Faceta

La especificación canónica de una Faceta incluye seis componentes:

1. **Identidad** — nombre canónico (ej: `pizarra-dibujo`, `matriz-colores`, `calendario-rango`) más versión.
2. **Modalidad de interacción** — qué tipo de input acepta (touch, mouse, teclado, gesto), qué tipo de output produce.
3. **Schema de entrada** — los datos que el invocador (cognición o Botlet de vista) le pasa al instanciarla.
4. **Schema de salida** — los datos que devuelve cuando el usuario completa su interacción.
5. **Estado interno** — qué mantiene mientras está activa (selecciones intermedias, edits parciales, undo stack).
6. **Compatibilidad de canal** — qué canales de Capa 1 la soportan (web, móvil, kiosk, no soportada en voz).

Las Facetas se publican en un **catálogo plano**: no hay jerarquía de Facetas porque cada una es atómica. Lo que hay es un set creciente de instrumentos disponibles, indexados por modalidad y por dominio de aplicación.

### Catálogo emergente

La industria converge gradualmente hacia un set canónico de Facetas reusables — el equivalente del catálogo de componentes de UI de las eras pre-agentivas (Material, Bootstrap, Ant Design), pero con la diferencia ontológica de que estos componentes son **invocables por la cognición** y no se sirven solo para construir aplicaciones humanamente programadas.

Algunas Facetas canónicas emergentes:

- `pizarra-dibujo` — superficie de dibujo a mano alzada.
- `catalogo-selector` — vista de items con selección.
- `matriz-colores` — selector de paleta o color individual.
- `calendario-rango` — selector de fecha o rango de fechas.
- `mapa-clickeable` — mapa con puntos seleccionables.
- `slider-multi` — uno o varios sliders relacionados.
- `dragdrop-orden` — reordenamiento de items.
- `formulario-dinamico` — formulario con campos generados al vuelo.
- `lienzo-creativo` — canvas abierto para producción de artefactos.
- `selector-archivo` — invocación al sistema de archivos del cliente.

La spec no cierra el catálogo: nuevas Facetas se acuñan a medida que la industria identifica modalidades canónicas que justifican primitiva propia.

### Conformidad

Una implementación de Facetas conforme a esta especificación debe satisfacer:

| Requisito | Nivel |
|---|---|
| Identidad y versión declaradas | **MUST** |
| Schema de entrada y salida explícito | **MUST** |
| Compatibilidad de canal declarada | **MUST** |
| Atomicidad — no compone otras Facetas internamente | **MUST** |
| Distinción explícita Faceta vs Botlet en documentación | **MUST** |
| Invocabilidad directa por la cognición durante conversación | **MUST** |
| Composabilidad dentro de Botlets de shell y vista | **MUST** |
| Compuesta en una pieza materializada como interacción declarada acotada (espacio de controles declarado, sin queries nuevas) | **MAY** |
| Preservación de la reproducibilidad de la pieza cuando se compone como Faceta embebida (recómputo client-side, sin invocar Capabilities) | **MUST** |
| Catálogo público de Facetas disponibles para el AgencyDomain | **SHOULD** |
| Heurísticas de invocación documentadas para la cognición | **SHOULD** |

### Frontera de evolución

Tres áreas activas de evolución de la Faceta como primitiva merecen mención.

La **estandarización de catálogo** es la primera. La industria todavía no ha consolidado un set canónico universal de Facetas. Cada plataforma agentiva define el suyo, con intersecciones parciales. La emergencia de un catálogo común con identidades estables permitiría agentes operar sobre cualquier AgencyDomain conforme.

La **federación de Facetas** es la segunda. Cuando dos AgencyDomains colaboran (federación, Capítulo 5 §1), las Facetas que uno expone deben poder invocarse desde el otro. La spec no define todavía un protocolo formal para invocación federada de Facetas — es trabajo abierto.

La **negociación de canal** es la tercera. Una Faceta declara qué canales soporta. La cognición debe negociar — si el usuario está en voz, no puede ofrecer la Faceta; debe degradar a conversación. Sin esta negociación explícita, las superficies fallan en canales no esperados. La spec exige declaración pero no formaliza aún el protocolo de degradación.
