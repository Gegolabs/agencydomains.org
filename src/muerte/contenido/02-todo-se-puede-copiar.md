# 2. Todo se puede copiar

En la primera semana de octubre de 2026, un proyecto de código abierto llamado *Reverse Engineer Anything*, REA, se volvió el repositorio de crecimiento más rápido que recuerdo. Tenía menos de diez mil estrellas en GitHub el 6 de octubre y más de cien mil el 12.[^hackernoon] Dos semanas después pasaba las trescientas cuarenta mil.[^404]

REA conecta a los agentes que programan, como Claude Code o Codex, con las herramientas profesionales de ingeniería reversa que los especialistas usan desde hace décadas para entender un programa del que no tienen el código fuente. Su documentación es prudente: dice que no recupera el código original, que no clona aplicaciones de forma automática y que no trae un descompilador propio.[^hackernoon] Lo que hace basta para inquietar a cualquier proveedor de software. Pone al alcance de cualquier agente la capacidad de mirar dentro de un programa terminado y describir lo que hace. Con qué se presentaba lo dice todo: si ves en una aplicación una función que quieres en tu producto, pídele a tu agente que la investigue con REA.[^404]

## ¿Qué significa que se pueda copiar?

Durante décadas, la ventaja de un proveedor de software tuvo dos partes: lo que su producto hacía y lo difícil que era reproducirlo. Lo primero se veía en las pantallas. Lo segundo protegía el negocio, porque reconstruir un CRM costaba años y equipos que casi ninguna empresa tenía.

La dificultad no desapareció. El artículo de HackerNoon que mejor cuenta el fenómeno trae un ejemplo concreto: el clon de Photoshop de ArtCraft, un proyecto que publica clones de aplicaciones conocidas hechos con agentes, acertaba en apenas cinco de treinta pruebas de filtros frente al original, y un artista lo declaró inservible. Su autora concluye que hoy un clon que abre, edita y exporta puede aparecer en días, y que un clon al que uno le confiaría su sustento todavía no. Lo que se terminó, dice, es la idea de que haber construido las pantallas sea una ventaja duradera.[^hackernoon]

Yo lo había visto en pequeño antes de REA. En los proyectos que dirijo reconstruimos más de una vez un reporte de una herramienta comercial mirando lo que mostraba, sin acceso a cómo estaba hecho, y lo pusimos a funcionar en días sobre los datos gobernados del cliente. Mi amigo, el del sistema patrimonial, hizo algo más grande: el cliente que le pidió el sistema había visto la plataforma que le ofrecía un bufete de abogados, y mi amigo le contestó que eso se podía construir con inteligencia artificial y que, además, sería suyo. REA hizo visible para todos lo que ya se podía hacer.

Este argumento vale para el software de un proveedor, sea cual sea la forma en que se tenga. El desarrollo a medida es del propio cliente y se debilita por otra vía, el costo de cambiarlo, que es la del capítulo 1.

## ¿Es legítimo copiar?

Depende del país, del método, de las licencias y de lo que se copie. El mismo artículo de HackerNoon lo resume para quien quiera mirarlo de cerca. En la Unión Europea, la ingeniería reversa de un producto comprado está permitida por el derecho de secretos comerciales, pero descompilar solo se admite con fines de interoperabilidad. En Estados Unidos hay fallos a favor del uso legítimo, y nadie sabe todavía si un modelo entrenado con código público cuenta como «limpio». ArtCraft prohíbe expresamente que el agente lea o descompile el código original y lo limita a estudiar el comportamiento, las especificaciones públicas de formatos y la apariencia, que es el método clásico de sala limpia. Y los proveedores ya están cambiando sus contratos para prohibir la ingeniería reversa asistida por IA.[^hackernoon] Un periodista lo dijo con más dureza: la máquina del plagio usada para plagiar.[^404]

Mi posición es más simple que el debate. Reproducir lo que hace un programa para entenderlo, o para construir uno propio sobre los datos propios, es lo que la industria del software hizo siempre. Copiar el código o los activos de otro, no. La frontera sigue en el mismo lugar. Lo nuevo es que cualquiera puede llegar hasta ella.

Cuando lo que quiero reemplazar es un servicio arrendado, no tengo su código: tengo lo que el servicio me muestra a mí —mis datos, mis pantallas, mis reportes—. En la Unión Europea y en Estados Unidos, mirar eso para entender qué hace no infringe derechos de autor, porque lo que un sistema hace no tiene dueño. Pero el contrato de arriendo puede prohibir usar ese acceso para construir un sustituto, y el de Salesforce lo hace: antes de empezar hay que leerlo.[^saas]

## ¿Y qué no se copia?

Supongamos resuelto lo legal, y volvamos a lo que la copia deja a la vista. Si las funciones de una aplicación se pueden reproducir, a quien vende software le queda menos de lo que creía. Y quien deja de comprarlo y lo reproduce en casa pierde algo que conviene nombrar.

Pierde el historial. Una aplicación que lleva diez años en miles de empresas trae algo que ningún agente puede descompilar: la evidencia acumulada de que funciona y un proveedor que responde cuando falla. El clon trae las pantallas y los flujos, y empieza su historial desde cero, con una sola organización respondiendo por él.

Para casi todas las funciones eso da igual. Si falla el clon de un tablero de tareas, alguien lo arregla y nadie sale herido. Importa en los registros de los que alguien responde ante otros: la factura que se le cobra a un cliente, el saldo de una cuenta, el contrato firmado y sus condiciones, el consumo que se informa al regulador, el patrimonio de una familia que confía en quien lo administra. En esos registros, la pregunta es si lo que dicen es verdad, y quién da fe.

La ingeniería reversa no responde esa pregunta. La vuelve urgente, porque cuanto más fácil es construir un sistema, más sistemas hechos en casa van a sostener registros de los que alguien responde, y más gente va a preguntarse si puede creerles.

## ¿Qué queda de las dos muertes?

Hasta aquí, dos muertes. La del capítulo 1 es la del negocio congelado, y la mató un costo: escribir y cambiar software dejó de ser caro. La de este capítulo es la de la ventaja que daba haber construido las pantallas, y la mató una herramienta: cualquier agente puede mirar dentro de una aplicación y describir lo que hace. Ninguna de las dos mata todo el software, y en las dos sobrevive lo mismo: el historial, la evidencia de que algo funciona, y alguien que responde por los registros de los que se responde ante otros.

Las dos dejan abierta la misma pregunta, qué tiene una organización cuando ya no compra el software que congelaba su negocio ni puede apoyarse en la ventaja de haberlo construido, y la respuesta va en dos partes que conviene leer en orden. Primero lo que nace, que es una forma nueva de tener un sistema. Después lo que se pierde, que es lo que nadie anotaba en el presupuesto.

[^hackernoon]: Maria Mendonca, «Is Software Really Dead? The Rise of AI-Powered Reverse Engineering», *HackerNoon*, 21 de octubre de 2026. <https://hackernoon.com/is-software-really-dead-the-rise-of-ai-powered-reverse-engineering>
[^404]: Jason Koebler, «'Reverse-Engineer Anything' Is the New Wild West of AI», *404 Media*, 20 de octubre de 2026. <https://www.404media.co/reverse-engineer-anything-is-the-new-wild-west-of-ai/>
[^saas]: Que la funcionalidad de un programa, su lenguaje de programación y sus formatos de archivo no están protegidos por el derecho de autor lo resolvió el Tribunal de Justicia de la Unión Europea en *SAS Institute contra World Programming* (C-406/10, 2012); en Estados Unidos, la ley excluye de esa protección los procedimientos y los métodos de operación (17 U.S.C. §102(b)). No he verificado el derecho de otros países, Chile incluido. El contrato es otra cosa: las condiciones de Salesforce prohíben acceder al servicio para construir un producto competidor o copiar sus funciones (Main Services Agreement, §3.4(j)). En la misma disputa entre SAS y World Programming, la corte de apelaciones del cuarto circuito de Estados Unidos (874 F.3d 370, 2017) trató como ingeniería reversa prohibida por la licencia el correr el programa ajeno y ajustar el propio hasta igualar sus resultados, y el jurado fijó US$ 26,4 millones de daños contractuales. Era una licencia de software y un pleito civil, no un servicio arrendado: sirve de indicio de que un tribunal puede hacer cumplir una cláusula así, no de que lo haga con la de un servicio en la nube.
