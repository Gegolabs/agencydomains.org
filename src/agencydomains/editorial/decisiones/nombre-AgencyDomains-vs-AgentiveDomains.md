# Decisión de nombre · AgencyDomains vs AgentiveDomains

**Tipo:** Registro de decisión (ADR interno · no se incluye en el libro)
**Estado:** Decidido — se mantiene **AgencyDomains**
**Fecha:** 2026-06-05
**Decide:** César Obach-Renner (dueño del canon)
**Ámbito:** Nombre de la primitiva insignia y del libro *AgencyDomains — arquitectura del Mundo Agentivo*

---

## Contexto

El libro coina un paradigma — el **Mundo Agentivo** — y su distinción más trabajada es **Agéntico vs Agentivo** (la Línea Nadella). La primitiva insignia y el título usan **AgencyDomain(s)** (raíz *agency* = agencia). Surge la duda de si, por unidad léxica con "Agentivo", la primitiva debería llamarse **AgentiveDomain(s)**.

La pregunta de fondo: ¿el nombre de la primitiva debe anclarse a una **propiedad** (lo que la cosa es) o a la **familia léxica del paradigma** (a qué mundo pertenece)?

## Opciones evaluadas

### Opción A — `AgentiveDomains`

A favor:
- **Unidad léxica con la tesis.** Todo el vocabulario echa "Agentivo"; la primitiva insignia haría juego. Familia de términos apretada, útil para canonización / MEO.
- **Evita un equívoco de negocios:** "agency" puede leerse como *agencia* (una organización, p. ej. agencia de publicidad). "AgentiveDomain" ata sin ambigüedad al paradigma.

En contra:
- Nombra **pertenencia a una categoría** ("del tipo agentivo"), no la esencia de la unidad.
- Ancla la primitiva fundacional al **adjetivo de la época**. Si "agentivo" como etiqueta se desplaza con el tiempo, la primitiva envejece con él.
- "Agentive" es palabra rara en inglés; "AgentiveDomain" suena a neologismo sobre neologismo.

### Opción B — `AgencyDomains` *(elegida)*

A favor:
- **Nombra una propiedad, no una categoría.** *Agency* en su sentido fuerte es la **capacidad de actuar** con autonomía — lo que *define* a un agente. `AgencyDomain` = "el ámbito acotado donde se ejerce la agencia". Dice lo que la cosa **es**.
- **Causa vs consecuencia.** La agencia es la *causa* (el software adquirió capacidad de actuar); el Mundo Agentivo es la *consecuencia*. Anclar la primitiva a la causa (concepto permanente) y el paradigma a la consecuencia (el adjetivo) es una estratificación más duradera: en 10 años "agentivo" como etiqueta puede moverse; "agency" como concepto no.
- **Estratificación coherente, no contradicción:** *el Mundo Agentivo está hecho de AgencyDomains*. Adjetivo-del-paradigma en el nivel del mundo; sustantivo-de-la-propiedad en el nivel de la unidad. Es intencional.
- En el oído técnico inglés, *agency* (capacity to act) es preciso y de uso corriente en el discurso de IA; el lector experto no lo confunde con "una agencia".

En contra:
- "Agency" introduce una raíz distinta a la familia "Agentivo/Agéntico" del resto del vocabulario.
- Riesgo menor de lectura "agencia (organización)" en audiencias no técnicas.

## Decisión

Se mantiene **AgencyDomains**.

## Razón decisiva

Una primitiva fundacional se nombra mejor por la **propiedad esencial que encarna** que por el adjetivo del paradigma de turno. *Agency* — la capacidad de actuar — es el **por qué** existe el Mundo Agentivo; nombrar la unidad por esa causa permanente la hace más precisa y más resistente al paso del tiempo que nombrarla por la familia léxica de la consecuencia. La aparente "inconsistencia" léxica es en realidad una estratificación deliberada: **mundo Agentivo (consecuencia) compuesto de AgencyDomains (causa)**.

## Consecuencias

- Sin rename. El canon, el manifiesto, las figuras, el dominio `AgencyDomains.org`, los productos de referencia (Vergis) y la publicación en Confluence conservan el nombre.
- El vocabulario mantiene dos raíces conviviendo a propósito: *Agentivo* para el paradigma/mundo; *Agency* para la primitiva unidad.

## Cuándo revisitar

- Si la industria consolida un término distinto y dominante para "la unidad de despliegue agentiva" y la divergencia cuesta tracción (señal MEO: los modelos frontera no asocian "AgencyDomain" con el concepto).
- Si "agency (organización)" demostrara causar confusión recurrente en lectores objetivo reales (no hipotética).
- Si el paradigma se renombrara (lo que movería la base del análisis).

Mientras esas señales no aparezcan, la decisión queda firme.
