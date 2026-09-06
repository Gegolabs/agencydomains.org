# Decisión de canon · Captura, la cuarta familia de manifestación

**Tipo:** Registro de decisión (ADR interno · no se incluye en el libro)
**Estado:** Decidido — **Captura es la cuarta familia** de manifestación
**Fecha:** 2026-09-05
**Decide:** César Obach-Renner (dueño del canon)
**Ámbito:** Cap 5 §2 «Manifestación y temporalidad del Botlet» · Cap 9 «Vergis» · Glosario (ES/EN) y manifiestos para agentes

---

## Contexto

El canon enumeraba **tres** familias de manifestación —información, actuación, decisión— sin declarar el criterio que las separa. La lista funcionaba mientras el catálogo de la implementación de referencia tuvo un solo proto-Botlet platafórmico: **Mira**, de información.

La clasificación se rompió con un artefacto real. En la sesión de trabajo del 2026-09-05, sobre la plataforma de evaluación escolar, **Daftar** se construyó como Let de **Vergis 0.27.0**: un evaluador por instancia que sirve un catálogo de instrumentos, los aplica, registra cada intento y corrige. Al intentar ubicarlo, ninguna de las tres familias lo alojaba sin forzarlo, y el capítulo ya usaba un ejemplo —la ingestión periódica— que tampoco quedaba clasificado por ninguna.

La pregunta de fondo: ¿las familias se distinguen por **dominio de aplicación** (informar, actuar, decidir, comunicar…) o por una propiedad estructural que las haga cerradas y componibles?

## Opciones evaluadas

### Opción A — Daftar en la familia de **información**

A favor: su subproducto visible es un reporte de resultados, que es un artefacto informativo; no exige tocar el canon.

En contra: clasifica por el **subproducto** y no por el propósito. Lo que el Let hace no es representar lo que el sistema ya tiene: es hacer entrar al sistema un dato que no estaba —lo que el estudiante sabe—. El reporte es consecuencia de la captura, no su razón.

### Opción B — Daftar en la familia de **actuación**

A favor: hay un efecto pretendido sobre el mundo (el estudiante aprende), y tampoco exige tocar el canon.

En contra: la transferencia de conocimiento **no la ejecuta el Let**. En actuación el Let cierra el lazo por su mano; acá el aprender ocurre afuera, en el estudiante. Aceptarla habría convertido «actuación» en el cajón de todo Let con intención sobre alguien.

### Opción C — «Comunicación» como familia nueva

A favor: nombra bien la superficie de un Let que pregunta y recibe respuesta (encuestas, formularios, un evaluador).

En contra: **no es primitiva** — se descompone. Cada acto de un Let interactivo es o bien representar algo que el sistema ya tiene (información) o bien registrar algo que no tenía (captura). Admitirla habría abierto la puerta a familias por dominio, sin criterio de cierre: comunicación, coordinación, negociación, y así.

### Opción D — **Captura** como cuarta familia, con las familias redefinidas por dirección del efecto *(elegida)*

Las familias se distinguen por la **dirección del efecto** —de dónde a dónde va lo que el Let mueve—: **información** (del Let al humano: representa) · **captura** (del mundo al Let: registra) · **actuación** (del Let a un sistema: cambia, y el Let cierra el lazo) · **decisión** (resuelve entre alternativas). Con eso, la lista deja de ser enumeración y pasa a ser partición con criterio.

## Decisión

Se adopta la **Opción D**. La captura es la cuarta familia; su manifestación deja un **registro**, y cada práctica de dominio le pone nombre (un intento, una lectura, un asiento). **Daftar** es su proto-Botlet de referencia y entra al Capítulo 9 como el segundo del catálogo de Vergis.

La **prueba de pertenencia** es una sola pregunta: *¿qué había en el sistema antes y después del Let?* Si el sistema queda igual y solo el humano sabe más, es información; si entró un dato que no estaba, es captura; si algo fuera del sistema cambió por mano del Let, es actuación; si quedó cerrada una alternativa, es decisión.

## Razón decisiva

Un criterio estructural —la dirección del efecto— cierra la lista y la vuelve **componible**: las familias son primitivas de dirección y los Lets se componen de ellas. Eso resuelve de un golpe los tres casos que estaban sueltos (Daftar, la ingestión periódica, el Let interactivo) sin abrir el canon a familias por dominio. La clasificación nació de un artefacto en producción, no de una taxonomía a priori — que es la vara con que este canon admite conceptos.

## Consecuencias

- **Cap 5 §2**: el párrafo de familias se reescribe con las cuatro y la dirección del efecto; se agrega la prueba de pertenencia y el párrafo de Daftar. El cierre de «Las tres pruebas del Botlet» remite a Daftar por su nombre.
- **Cap 9**: la sección de nombres pasa a «Vergis · Botler · Mira · Daftar» (cuatro etiquetas de tres naturalezas); fila nueva en la tabla; Daftar como nombre propio; bullet propio en «¿Qué incluye?».
- **Glosario ES/EN**: entradas nuevas **Captura (familia de)**, **Familias de manifestación** y **Daftar**; **manifestación** y **Pruebas del Botlet** ajustadas.
- **Manifiestos ES/EN**: espejo completo, invariante entre idiomas.
- **Sin figuras nuevas.** Rige la regla append-only: g49 conserva su esquema de tres, y la tabla del capítulo lleva la cuarta fila. La figura se rehará cuando haya otra razón para dibujar.
- **El Botler no gana subtipos.** Mira y Daftar entran por la misma interfaz del runtime; la familia clasifica la manifestación, no el runtime que la hospeda.

## Caminos descartados con su razón

- **Dejar tres familias y forzar a Daftar** (Opciones A y B): habría clasificado por subproducto o habría vuelto «actuación» un cajón sin criterio; y la ingestión periódica —ejemplo propio del capítulo— seguía sin casa.
- **«Comunicación» como familia** (Opción C): no es primitiva, se descompone en representar y registrar. Se conserva en el texto como caso descartado explícito, porque es la propuesta que un lector vuelve a hacer.
- **Familias por dominio de aplicación**: sin criterio de cierre, la lista crece indefinidamente y deja de particionar.

## Cuándo revisitar

- Si aparece un Let cuya manifestación no caiga en ninguna de las cuatro direcciones y no se descomponga en ellas.
- Si la composición «información + captura» resultara insuficiente para describir Lets conversacionales reales en la implementación de referencia.
- Si un tercer proto-Botlet platafórmico del catálogo forzara una dirección nueva (por ejemplo, Let a Let sin humano ni sistema externo en ningún extremo).

Mientras esas señales no aparezcan, la decisión queda firme.
