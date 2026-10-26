# 4. La tranquilidad que se compraba

Quien compraba software se llevaba dos cosas y pagaba solo por una. Pagaba por las funciones. La otra venía incluida y nadie la anotaba en el presupuesto: la tranquilidad.

## ¿De qué estaba hecha esa tranquilidad?

De dos certezas. Muchos otros usaban lo mismo, y les funcionaba: en mi criterio, un ERP que corre en miles de empresas ha pasado por miles de cierres contables, y un error grave tiene menos lugares donde esconderse, aunque la historia del software tiene sus contraejemplos famosos. Y alguien respondía: si el sistema calculaba mal un impuesto, había un proveedor con contrato, con nombre y con algo que perder.

Esa tranquilidad es de lo que se compra: del servicio que se arrienda y del paquete que se licencia. El desarrollo a medida casi nunca la tuvo, porque lo usa una sola empresa y responde un equipo que suele irse. Quien viene de ahí pierde poco al pasar a un sistema propio. Lo que descubre es que la pregunta de abajo, ¿quién da fe?, nunca tuvo respuesta.

## ¿Qué pregunta llega cuando se construye?

Imaginemos al directorio de una empresa que decide construir su sistema en lugar de comprarlo. El área de sistemas pone manos a la obra, los agentes empiezan a operar, y un día alguien en la mesa pregunta lo que nunca preguntó de la plataforma que compraba: ¿lo están haciendo bien? ¿Los números que arroja este sistema son correctos?

La misma pregunta aparece en otras escalas. Los miembros de una familia cuyo patrimonio administra un tercero pueden dudar, con razón, de si lo que ven en el reporte es verdad o está manipulado. El cliente de un contador que lleva su contabilidad con un sistema hecho por el propio contador se pregunta lo mismo. Y el regulador, que recibe los informes de una empresa, no tiene por qué creer que el sistema que los produjo hace lo que dice.

Detrás de la pregunta hay riesgos concretos. De cualquier construcción: llegar a un callejón sin salida, retrasarse y gastar más de lo previsto, entregar algo de menor calidad que lo esperado. De los agentes en particular: que uno se equivoque en algo que toca el dinero o al cliente, que actúe sin una autoridad clara o sin dejar rastro, y que su desempeño se degrade sin que nadie lo note.

## ¿No basta con construir bien?

No basta, porque la pregunta no es sobre la calidad del trabajo. Es sobre quién da fe.

Un proceso auditado es uno que observa alguien sin relación con quien lo ejecuta. De esa definición sale una consecuencia: una organización puede construir su sistema todo lo bien que quiera y aun así no puede ser ella la que garantiza a sus clientes, a sus accionistas y al regulador que lo registrado es verdad.

Hay que separar esto de otra cosa que también se necesita. Una organización que construye necesita criterio técnico: un director de tecnología, un socio experto o un proveedor de confianza que asegure que lo que se hace se haga bien. Ese criterio se puede contratar o formar en casa, y asegura la calidad de la construcción. La garantía de que lo registrado es verdad viene de otro lado.

## ¿Qué pieza es esa?

La conversación con mi amigo me llevó a un nombre provisional. Le propuse mirarla como una caja negra: le metes cosas, sacas reportes, y su valor está en que lo que sale no es lo que alguien registró como quiso, sino algo que un proceso auditable garantiza. Él me corrigió: nadie quiere una caja negra. Lo que se necesita es algo que cualquiera pueda abrir y verificar.

La llamé después base de verdades, por parentesco con la base de datos, pero la palabra «base» sugería una repisa. Terminé en el nombre que uso en el resto del libro, construido sobre un término que los arquitectos de sistemas ya usan. Un **sistema de registro** guarda la versión oficial de un dato. Lo que hace falta es un paso más: un **sistema de verdad**.
