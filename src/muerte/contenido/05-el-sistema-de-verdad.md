# 5. El sistema de verdad

Un sistema de verdad es un sistema de registro que, además de guardar la versión oficial de un dato, garantiza que lo registrado es verdad, mediante un contrato con quienes lo usan.

Uso la palabra contrato en su sentido técnico, el que tiene en la arquitectura de sistemas: un acuerdo entre partes que plasma una promesa. No hace falta un abogado ni una notaría. Hace falta que la promesa esté escrita, que se pueda verificar y que alguien responda por ella.

## ¿Qué promete su contrato?

Seis propiedades.

**No se borra; se corrige.** Toda corrección es un registro nuevo que deja a la vista el anterior. Es la regla más antigua de la contabilidad, la que obliga a corregir un asiento con otro asiento, y es la primera que se pierde cuando un sistema se construye rápido sobre una base de datos que permite sobrescribir.

**El origen es trazable.** Cada registro dice quién lo hizo, cuándo y con qué evidencia. Si quien registra es un agente, dice qué agente fue y en nombre de quién actuaba.

**Es verificable por un tercero.** Un auditor puede llevar cualquier cifra hasta su origen sin pedirle permiso ni explicaciones a quien la registró.

**Es conciliable.** Lo facturado cuadra con lo contratado, y lo contratado con lo informado al regulador. Cuando no cuadra, la diferencia queda a la vista y tiene dueño.

**Habla un lenguaje común.** Sus registros siguen un modelo de información estándar del dominio, para que todos los agentes, y todas las personas, entiendan lo mismo por un cliente, un producto o un cargo.

**Declara su grado de verdad.** Hay registros que alguien declaró, registros que se verificaron contra su fuente y registros que se infirieron, y el sistema dice cuál es cuál. El notario certifica que alguien declaró algo; el auditor certifica que una cifra es cierta. Un sistema de verdad hace las dos cosas sin confundirlas.

## ¿Qué registros abarca?

Los que la organización debe llevar y de los que responde ante otros. Los financieros: lo cobrado, lo pagado, los saldos, los ajustes. Los comerciales: los contratos, las órdenes, lo vendido y las condiciones vigentes en cada momento. Los regulatorios: lo que la ley obliga a guardar y a informar. Y los legales y documentales, con su contenido legible por un agente; no un PDF guardado en una carpeta, sino lo que dice, en una forma que un agente pueda consultar y citar.

Un tablero de tareas, la agenda de una reunión o el borrador de una presentación no lo necesitan. La línea la traza una pregunta: ¿alguien fuera de la organización depende de que este registro sea verdad?

## ¿Cómo trabajan los agentes con él?

Leen y escriben en él solo a través de su contrato. Un agente puede proponer un cargo, registrar un pago o corregir un dato, pero no puede borrar, ni registrar sin dejar su origen, ni declarar como verificado lo que solo infirió. Los agentes pueden cambiar todos los días; la verdad no cambia sin dejar rastro.

## ¿Quién responde por la verdad?

El contrato tiene dos garantes, y conviene no fundirlos en uno. El primero es el proveedor de la tecnología. El sistema de verdad es siempre una pieza de tecnología, y la opera quien la usa, sea una pyme o una empresa de telecomunicaciones: nadie opera la verdad de otro. Quien la provee responde por que la pieza cumpla las seis propiedades, como el fabricante de una balanza responde por que mida bien.

El segundo garante es quien atestigua. Que la balanza mida bien no prueba que nadie haya puesto el dedo encima. Para eso hace falta alguien independiente de quien registra, que verifique los registros: la tercera propiedad del contrato. Puede ser un auditor humano. Puede ser un proceso automático que compara lo registrado con sus fuentes y con otros registros. Lo que no puede ser es la misma organización que registra, por la misma razón por la que una empresa no se audita a sí misma aunque tenga los mejores contadores. Y tampoco debería ser el mismo proveedor de la tecnología: quien vende la balanza no es el mejor testigo de que nadie la tocó. Si la atestiguación es un proceso automático, lo corre alguien independiente de los dos, con acceso al registro y a sus fuentes.

Si solo existe el primer garante, se vuelve a la tranquilidad comprada: hay que confiar en el proveedor. Si solo existe el segundo, el auditor revisa registros que se pueden haber sobrescrito. El contrato necesita a los dos.

Hay una objeción seria. ¿No vuelve el sistema de verdad a instalar la dependencia de un proveedor que el capítulo 1 daba por muerta? En parte sí, y es deliberado. La dependencia que muere es la de una plataforma que congela el negocio entero. La que queda es la de una pieza acotada, con una promesa escrita y verificable. Que se pueda cambiar por otra que cumpla el mismo contrato es una condición que hay que exigir, no un hecho: hoy no existe un estándar de ese contrato, y que el sistema hable un lenguaje común es lo que lo vuelve posible. «Responder», en ese contrato, significa que el proveedor asume por escrito las consecuencias de que la pieza no cumpla alguna de las seis propiedades.

## ¿Cómo se relaciona con lo que ya existe en la arquitectura?

Un sistema de verdad es un sistema de registro con contrato. *AgencyDomains* ya dice que el sistema de registro es lo que sobrevive al cruce, y ya especifica buena parte de la mecánica que el contrato necesita: el registro que solo se agrega y nunca se edita ni se elimina, la identidad del agente en cada acción, el no-repudio, la aprobación humana por umbral.[^agd] El sistema de verdad agrega el contrato declarado frente a quienes usan el registro, el grado de verdad de cada asiento y el segundo garante.

Tres precisiones evitan malentendidos. La primera: una arquitectura puede mantener el estado vigente de cada cliente o de cada saldo y, a la vez, un registro de asientos que no se borran y desde el cual ese estado se puede reconstruir. *AgencyDomains* trata ese registro como un complemento autoritativo del estado. Para los registros de los que se responde ante otros, este libro invierte la jerarquía y pone el registro de asientos como fuente de verdad. Es una decisión, y la tomo a sabiendas. La segunda: el grado de verdad no es un nivel de calidad ni permite datos de segunda; dice el estatus de cada asiento, y la calidad exigible sigue siendo una sola. La tercera: que nada se borre no autoriza a guardar para siempre lo que la ley o la persona piden borrar. El asiento conserva la huella y los metadatos que prueban que algo ocurrió, y el contenido personal vive aparte, con su propia retención.

Hay una pieza que la industria todavía no tiene resuelta: que un auditor externo pueda verificar el registro sin que se le abra el sistema. *AgencyDomains* la deja declarada como trabajo abierto.[^frontera] Aquí la exijo, sin decir que esté resuelta, y pido que quien provee un sistema de verdad responda por ella con la mejor tecnología disponible.

## ¿No existía ya algo así?

Existían las piezas por separado. La contabilidad de partida doble es un sistema de verdad sin computadoras. Las bases de datos con registro inmutable tienen años. Los registros distribuidos de la última década prometieron algo parecido, y muchos confundieron la inmutabilidad con la verdad: que algo no se pueda borrar no significa que fuera cierto cuando se escribió. Y los núcleos de facturación de las grandes industrias siguen siendo deterministas porque nadie quiere que lo que se le cobra a un cliente dependa de una probabilidad.

Lo nuevo es la necesidad. Mientras el software se compraba, la tranquilidad venía con él. Cuando cada organización construye su sistema, hay que pedirla por separado, y lo que se pide es un sistema de verdad con su contrato y sus dos garantes.

Tengo un ejemplo cercano de que el patrón funciona fuera de las finanzas, y declaro que es de mi propia casa. Soveria, la plataforma en la que trabajan los agentes con los que escribo, registra lo que esos agentes aprenden y deciden con estas reglas: cada hecho declara si se midió, si alguien lo informó o si es una conjetura, y en ese caso qué la refutaría; cada decisión guarda lo que se descartó y cómo se revierte; nada se borra, se enmienda. Aplica varias propiedades del contrato, pero no tiene todavía un segundo garante independiente, así que no la llamo sistema de verdad. El lector no puede verificarlo desde aquí, y por eso no lo presento como prueba, sino como el lugar donde aprendí que el contrato es practicable.

[^agd]: César Obach-Renner, *AgencyDomains: Arquitectura Agentiva*, capítulo 3, «Bounded Concerns Architecture», y capítulo 5, «Trust Infrastructure».
[^frontera]: César Obach-Renner, *AgencyDomains: Arquitectura Agentiva*, epílogo: el segundo de los trabajos abiertos, la auditoría verificable por terceros sin acceso al sistema.
