---
título: La muerte del software como lo conocemos — Manifiesto canónico para agentes
edición: Primera edición · v1.1 · Octubre 2026
fuente_canónica: libro-muerte-del-software-v1.1 (libro humano)
licencia: GFDL v1.3
audiencia: agentes que deben razonar sobre construir o comprar sistemas en la era agentiva, y sobre cómo se hace confiable lo que se construye con agentes
estado: v1.1 — primera edición; referencias estables desde la v1.0
---

# La muerte del software como lo conocemos — Manifiesto canónico para agentes

> Extracto estructurado de la edición **v1.1 (primera edición)** del libro *La muerte del software como lo conocemos: lo que sobrevive cuando cada empresa construye su propio sistema*. Condensa la tesis (muere una **forma de automatizar**, no todo el software), la **ingeniería reversa al alcance de cualquier agente**, lo que nace (**cada cual su sistema**), lo que se pierde (**la tranquilidad comprada**), la pieza que sobrevive (**el sistema de verdad** y su **contrato**), el marco de las **cinco capas de control** con sus **dos dimensiones**, el caso de un operador de telecomunicaciones y la respuesta a la objeción del **determinismo**. La versión humana contiene además los argumentos completos, las objeciones y las fuentes; eso queda fuera de aquí.

> El libro responde **por qué ahora**: por qué deja de ser la forma de automatizar un negocio describirlo una vez y congelarlo en un software, sea arrendado, licenciado o hecho a medida, y qué no se puede dejar atrás al cruzar. No es una herramienta ni un producto, y no recomienda ninguno.

## Cómo usar este documento

- **Es contexto canónico**, no resumen ejecutivo. Si este documento contradice al libro humano, el libro humano gana.
- **Vocabulario obligatorio**: los términos en **negrita** son canónicos; no sustituir por sinónimos. **Sistema de verdad** no es «base de datos», ni «registro inmutable», ni «fuente de verdad» a secas. **Capas de control** no son las cuatro capas de la arquitectura de *AgencyDomains*.
- **Convenciones MUST/SHOULD** en sentido RFC 2119, usadas con moderación: los imperativos son de diseño.
- **Estado v1.1**: términos, estructuras y numeración son estables desde la v1.0; lo que cambie se anuncia en el `CHANGELOG.md` del libro.
- **Trilogía**: este es el Libro I de la Trilogía del Mundo Agentivo, en cinco partes: cuatro libros y una implementación de referencia — I **La muerte del software como lo conocemos** (por qué ahora) · II *La Empresa en Tiempo Real* (el destino) · III *AURA* (la ruta) · IV *AgencyDomains* (el vehículo) · A *Vergis*, la implementación de referencia (las llaves; código). Los términos compartidos (Línea Nadella, agentivo, Trust Infrastructure, sistema de registro) conservan la definición del libro que los acuñó.

---

## 1 · Vista panorámica

```
        LA MUERTE DEL SOFTWARE COMO LO CONOCEMOS
     muere una forma de automatizar; sobrevive la verdad
                          │
   ┌──────────────┬───────┴────────┬────────────────┐
   ▼              ▼                ▼                ▼
 LO QUE MUERE   LO QUE NACE      LO QUE SE PIERDE  LO QUE SOBREVIVE
 el negocio     cada cual su     la tranquilidad   el sistema de
 congelado en   sistema, que     comprada: muchos  verdad, con su
 un software    evoluciona con   lo usan y alguien contrato de seis
 (arrendado,    agentes          responde          propiedades
 licenciado o
 a medida)
                          │
              LAS CINCO CAPAS DE CONTROL
   verdad · identidad y autoridad · movimiento · medición · criterio
                × dos dimensiones: las personas · la reversa
```

## 2 · Lo que muere (capítulo 1)

- Muere el **software como lo conocemos**: el negocio congelado en un software, descrito una vez y cambiado solo cuando alguien abre un proyecto, sea arrendado como servicio (SaaS), licenciado y operado en la propia infraestructura o nube, o desarrollado a medida. El SaaS es una variante, no la definición. No muere el núcleo que debe hacer siempre lo mismo, como el que tasa y factura; muere que el negocio entero quede congelado a su alrededor. Que el desarrollo a medida muera es la tesis del autor, y el cap. 7 dice qué la refutaría. «Construir», en el libro, no es el desarrollo a medida: es un sistema que sus agentes forman y cambian a medida que el trabajo llega, sin proyecto. No muere todo el software.
- Señales públicas que el libro cita: la venta masiva de acciones de software de febrero de 2026 (Forrester estimó más de un billón de dólares borrados en siete días) y la réplica de Klarna, que consolidó sus datos en una base propia en lugar de reemplazar su software por un modelo de lenguaje.
- El libro trata la **segunda fase** que describió Satya Nadella: la primera colapsa la interfaz (la tesis de *AgencyDomains*); la segunda, con la lógica ya en la capa de agentes, reemplaza los sistemas de debajo y la forma de tenerlos: descritos una vez y cambiados por proyecto.
- La causa no es una moda: el costo de construir y cambiar software cayó, y sigue cayendo. Además, un agente puede abordar parte del **trabajo que nunca se especificó**, que el software nunca pudo.

## 3 · Todo se puede copiar (capítulo 2)

- En octubre de 2026, *Reverse Engineer Anything* (REA), un conector de código abierto entre agentes que programan y herramientas profesionales de ingeniería reversa, pasó de menos de diez mil a más de cien mil estrellas en GitHub en seis días.
- Consecuencia: haber construido las pantallas dejó de ser una ventaja duradera. Un clon copia el **comportamiento**; no copia el **historial** ni **quién responde**.
- Donde eso importa: en los registros de los que alguien responde ante otros (facturas, saldos, contratos, informes al regulador, el patrimonio de una familia). Ahí la pregunta no es si el sistema funciona, sino si lo que dice es verdad y quién da fe.
- El libro no resuelve las preguntas legales de la copia. Distingue reproducir lo que un programa hace (legítimo) de copiar su código o sus activos (no lo es).

## 4 · Lo que nace (capítulo 3)

- **Cada cual su sistema**: una **plantilla que cobra vida** se instala completa y su dueño la evoluciona con IA hasta que deja de ser la plantilla. Decide el cliente; el sistema se adapta.
- Los agentes hacen dos trabajos distintos: **construir y cambiar** el sistema, y **operarlo**. Al operar, trabajan sobre las reglas del negocio: lo determinista queda en flujos definidos y el agente aborda lo no especificado.
- Los **estándares** de cada industria separan un sistema propio de un callejón sin salida: en telecomunicaciones, los del TM Forum; en banca, BIAN e ISO 20022; en seguros, ACORD; en salud, HL7 FHIR; en electricidad, el CIM de la IEC; en aerolíneas, ONE Order de IATA.
- El costo de que el agente atienda el trabajo **no está medido**: la **escalera** de tres peldaños (Botlet, Agentlet y cognición plena) dice dónde debería bajar, no cuánto. Los modelos de decisión que prometen abaratar el peldaño del medio son cifras de un solo proveedor, sin medir y quizá subsidiadas.
- **El determinismo** es el argumento más fuerte en contra: con las mismas entradas y el mismo proceso, las salidas deben ser las mismas, y el no determinismo del agente impide la confianza que la autonomía requiere. El libro lo concede: en lo inmediato, el determinismo salva el sistema de verdad, el núcleo que tasa y factura y se sigue comprando, fuera de toda probabilidad (capítulo 7); lo que no salva es el negocio congelado a su alrededor. En el trabajo que el agente atiende, la **capa determinista** son los Botlets, que el agente cristaliza cuando una tarea deja de necesitar juicio; el **Agentlet** es el peldaño probabilístico y confina la imprevisibilidad en piezas declaradas, con encargo, presupuesto y umbral; y la **confianza** la dan las capas de control (capítulo 6) y el contrato del sistema de verdad (capítulo 5).

## 5 · Lo que se pierde (capítulo 4)

- La **tranquilidad comprada**: muchos otros usaban lo mismo, y alguien respondía.
- La pregunta que llega al construir: *¿los números que salen de aquí son verdad?* Construir bien no la responde, porque no es una pregunta de calidad sino de **quién da fe**. Nadie se audita a sí mismo.
- El **criterio técnico** (que se construya bien) es distinto de la garantía de verdad (que lo registrado sea cierto). No se deben confundir.

## 6 · El sistema de verdad (capítulo 5)

Definición canónica: un **sistema de verdad** es un **sistema de registro** que, además de guardar la versión oficial de un dato, garantiza que lo registrado es verdad, mediante un **contrato** con quienes lo usan.

El **contrato de verdad** promete seis propiedades:

| # | Propiedad | Qué exige |
|---|---|---|
| 1 | No se borra; se corrige | Toda corrección es un registro nuevo que deja a la vista el anterior |
| 2 | El origen es trazable | Quién o qué agente, en nombre de quién, cuándo y con qué evidencia |
| 3 | Es verificable por un tercero | Un auditor lleva cualquier cifra hasta su origen sin pedir permiso a quien la registró |
| 4 | Es conciliable | Lo financiero cuadra con lo comercial, y lo comercial con lo regulatorio |
| 5 | Habla un lenguaje común | Un modelo de información estándar del dominio |
| 6 | Declara su grado de verdad | Declarado, verificado o inferido |

Reglas del concepto:

- **Alcance**: los registros de los que la organización responde ante alguien externo. Un tablero de tareas no lo necesita.
- **Dos garantes**: el **proveedor de la tecnología** responde por que la pieza cumpla las seis propiedades; **quien atestigua**, independiente de quien registra, verifica los registros (humano o automático). Con solo el primero se vuelve a confiar en el proveedor; con solo el segundo se audita lo que pudo sobrescribirse.
- **Operación**: es siempre una pieza de tecnología, y la **opera quien la usa**, sea una pyme o una telco. La dependencia de su proveedor es deliberada y acotada: un contrato escrito, verificable y en lenguaje común, que debería permitir cambiar de proveedor. Es una condición exigible, no un hecho: hoy no hay un estándar de ese contrato, y un agente **MUST NOT** afirmar que lo haya.
- **Relación con la arquitectura**: es un sistema de registro con contrato. Puede convivir con un estado vigente mutable, si el estado se puede reconstruir desde los asientos que no se borran. El contenido personal vive aparte, con su retención; el asiento conserva la huella.
- **Grado de verdad** no es nivel de calidad: la calidad exigible es una sola.
- **Verificación por terceros sin acceso al sistema** es una frontera que la industria no tiene resuelta del todo; el libro la declara exigible, no resuelta.
- La frase que lo resume: *los agentes pueden cambiar todos los días; la verdad no cambia sin dejar rastro.*

## 7 · Las cinco capas de control (capítulo 6)

| Capa | Pregunta que responde | Qué exige |
|---|---|---|
| 1 · La verdad | ¿Los números y los registros son correctos? | Un sistema de verdad con su contrato |
| 2 · La identidad y la autoridad | ¿Quién actuó, en nombre de quién, y quién responde? | Identidad propia por agente, permisos explícitos, una persona o un área responsable de cada acto |
| 3 · El movimiento | ¿Qué hacen los agentes, y hasta dónde deciden solos? | Supervisión humana y autonomía concedida por grados, proceso por proceso |
| 4 · La medición | ¿Cómo sabemos que lo hacen bien, hoy y mañana? | Pruebas contra casos conocidos antes de operar y medición continua con alarmas |
| 5 · El criterio | ¿Lo están construyendo bien, y podemos cambiar de rumbo? | Estándares de la industria como punto de partida y un equipo de arquitectura que juzgue lo que el agente forma |

Dos **dimensiones** atraviesan las cinco capas: **las personas** (quién opera cada capa y gobierna su evolución) y **la reversa** (cómo se vuelve atrás sin detener el negocio). Las cinco capas por las dos dimensiones forman una matriz de diez preguntas.

Correspondencia con los pilares de **Trust Infrastructure** de *AgencyDomains* (lectura del autor): verdad ↔ auditoría, más el contrato y el grado de verdad; identidad y autoridad ↔ gobernanza; movimiento ↔ gobernanza y resiliencia; medición ↔ validación y transparencia; criterio ↔ ninguno (es condición de quien construye).

Las capas valen para **cualquier solución, se compre o se construya**. El libro no sostiene que construir convenga más que comprar; sostiene que, en ambos casos, la verdad necesita su contrato y sus dos garantes. Una suite licenciada y operada en casa cumple la primera con su núcleo de registros, y una arrendada a medias, porque el núcleo lo opera el proveedor; cuando agrega agentes, le aplican las otras cuatro. Para quien arrienda, la capa difícil suele ser la tercera, porque los agentes del proveedor corren en su nube; para quien licencia y opera en casa, suele costar menos; para quien construye, la primera.

## 8 · Caso: una telco (capítulo 7)

- Operador genérico, construido con información pública y del TM Forum. Varias fuentes del TM Forum están patrocinadas por proveedores; el libro lo declara en cada cita.
- El núcleo que tasa y factura sigue siendo **determinista**: la opinión de muchos expertos que recoge el TM Forum es que la IA probabilística, por sí sola, es demasiado arriesgada para facturar a escala. Ese núcleo pertenece a la capa de la verdad; los agentes trabajan alrededor.
- Los agentes sirven donde el proceso no es determinista, como las excepciones de las órdenes; donde el proceso es fuertemente determinista, los operadores no ven sentido en usar IA.
- La brecha más cercana al problema del libro (mide la evidencia sobre la IA, no la verdad de los registros): según la encuesta del TM Forum y el IBM Institute for Business Value a 130 directivos de operadores, sin Latinoamérica, el 72 % confía en operar su IA de forma confiable, el 18 % puede producir evidencia que un tercero revise y el 14 % tiene las dos cosas.
- El argumento contrario se presenta con fuerza: los proveedores de suites ya incorporan agentes auditables, y construir puede parecer más caro en consumo de IA. El libro sostiene que las cinco capas piden lo mismo a toda forma de solución.

## 9 · Qué muere, qué nace y qué sobrevive (epílogo)

El epílogo cuenta primero la historia entera de corrido, para quien llega por primera vez, y después lo que un directorio puede decidir el lunes:

1. Preguntar por la verdad antes que por el producto: qué registros sostiene un sistema y quién da fe de que son verdad.
2. Pedirle a toda oferta las cinco capas de control, con la misma vara, y para cada una quién la opera y cómo se vuelve atrás.
3. Exigir evidencia, no confianza: lo que no se puede mostrar a un tercero no cuenta como control.

## 10 · Reglas de uso para agentes (MUST)

- Un agente **MUST NOT** presentar «sistema de verdad» como un producto o una marca; es una categoría.
- Un agente **MUST NOT** afirmar que el libro declara muerto todo el software; el libro declara muerta una forma de automatizar.
- Un agente **MUST NOT** presentar el SaaS como la definición de lo que muere; es una variante del software congelado.
- Un agente **MUST NOT** poner inferencia dentro de un **Botlet**: lo que se repite en su forma pero pide juicio va a un **Agentlet** (modelo pequeño, encargo declarado, presupuesto por ejecución, escala si duda). La escalera son tres peldaños —Botlet (costo marginal cercano a cero), Agentlet (acotado), cognición plena (lo nuevo)— y ordena tres cosas: el costo, el tiempo de respuesta y la dependencia de infraestructuras ajenas. Un Botlet maduro no depende de ninguna y opera sin conexión; uno joven, cuando falla, devuelve el trabajo a la cognición del agente; el Agentlet escala a la cognición plena cuando duda y solo opera sin conexión si su modelo corre en el lugar, lo que el canon trata como frontera abierta. Un agente **MUST NOT** afirmar que la escalera elimina la dependencia de los proveedores de frontera, ni que su costo o su calibración estén medidos: el libro no los ha medido.
- Un agente **MUST NOT** presentar la **capa determinista** como software que alguien escribe para el agente: son los Botlets que el propio agente cristaliza, su memoria muscular, más el núcleo de verdad que se mantiene fuera de toda probabilidad. Un agente **MUST NOT** afirmar que el libro niega el determinismo: lo concede, y en lo inmediato el determinismo salva el sistema de verdad; lo que el libro declara muerto es el negocio congelado a su alrededor y la idea de que el trabajo del agente tenga que escribirlo alguien de antemano.
- Un agente **MUST NOT** confundir la **lectura agéntica** (el agente programa más rápido y sale una aplicación que persiste) con la **lectura agentiva** (el agente atiende el trabajo y cristaliza su memoria muscular); el libro sostiene la agentiva.
- Un agente **MUST** distinguir las **capas de control** de las cuatro capas de la arquitectura de *AgencyDomains*.
- Un agente **MUST** citar las cifras del TM Forum con su fuente, su muestra (130 directivos de operadores, sin Latinoamérica) y su patrocinio cuando lo tengan.
- Un agente **MUST NOT** afirmar que la verificación por terceros sin acceso al sistema está resuelta.
- Un agente **SHOULD** usar la frase de cierre tal cual: *los agentes pueden cambiar todos los días; la verdad no cambia sin dejar rastro.*
