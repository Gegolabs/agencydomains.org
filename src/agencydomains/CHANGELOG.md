# Changelog — AgencyDomains

Historial de versiones del libro *AgencyDomains · Arquitectura del Mundo Agentivo*.

**Pre-1.0:** las referencias y las figuras pueden reorganizarse libremente entre
iteraciones. A partir de **v1.0** (primera publicación pública estable) aplica la regla
**append-only** para la numeración de figuras: cada figura nueva toma el siguiente número
disponible al final, sin re-enumerar las existentes.

## v0.5 — Julio 2026

**La pasada editorial.** Revisión integral de la trilogía (inventario en la
cocina del proyecto):

- **Las generaciones del Botlet (G1/G2/G3) se formalizan en el Cap. 5 §2** —
  donde el lector las necesita —; el Epílogo conserva el ensayo de fondo
  («La cristalización») sin carga normativa. facetas.md y Vergis apuntan al
  nuevo hogar.
- **El Producto de Información tiene casa canónica**: término normado de la
  spec de Botlets (Cap. 5 §2), con multi-vista, drill-through y sus MUST;
  el Cap. 4 presenta y remite; el Cap. 7 corrige la remisión circular.
- **Doctrina Capability restaurada**: la localidad (cloud/edge/híbrido) y la
  certificación regulatoria se predican del **Conector** — ESC/POS-Printer,
  Cash-Drawer, Pinpad y DTE-SII reclasificados; la Capability regulada porta
  el saber normativo; glosario y resumen del Cap. 4 alineados.
- **El Botler deja de llamarse primitiva** en el Cap. 9 (constructo normado
  de la spec de Botlets; el canon sigue siendo de siete).
- **Cap. 2 ↔ Cap. 7 desduplicados** (citas de industria, AtScale, consenso) y
  **Cap. 4 adelgazado** a favor del Cap. 5 (Faceta, PI, Tokens/Suscripción,
  JavaSpaces, neurobiología, reguladores, sección placeholder de
  Asistente/Agente).
- **Cifra de Gartner dosificada** (de ~8 apariciones a 3), tabla de actores del
  Cap. 6 alineada con su texto (OpenAI/Anthropic/Google), «Plataforma
  integral» corregida en el glosario, voseo eliminado, «agentive» traducido,
  errata del contraste tipográfico del Cap. 1 reparada.
- **Cap. 1 abre sin pared de marca** (la pregunta de Nadella primero); promesa
  Cap. 1 → Cap. 2 calzada; el mapping del Cap. 3 lleva nota de lectura.
- **Salto Cuántico reutilizado** (Cap. 7) y ciclo de inteligencia continua con
  formulación canónica de la trilogía (Percibir → … → Aprender).
- **Dominion adoptado** por el Epílogo (Frontera 4); Wingtraining y SME
  definidos; entrada RLS en el glosario; punteros de glosario corregidos
  (Plantilla, Trace, DLP); rastros de versionado interno eliminados.
- **Patrón tripartito** atribuido a esta operacionalización (no a un consenso
  de industria); productos de la casa encuadrados en su primera aparición.
- **Micro-sección «La trilogía»**: ancla el tránsito, glosa Data Mesh y BPM, y
  registra las **cinco** especificaciones de AURA.
- **El prólogo placeholder sale del build** hasta que llegue el texto del
  prologuista.

## v0.4 — Junio 2026

Extensiones canónicas surgidas al construir la implementación de referencia
(Vergis · su runtime Botler · el proto-Botlet Mira) y de proyectos reales:

1. **Capítulo 9 · Vergis** — la implementación de referencia pública (AGPL, AgencyDomains.org), con la nota de alcance del canon (estructura y vocabulario, no método ni catálogo) y el esquema de nombres Vergis · Botler · Mira.
2. **proto-Botlet** (séptima primitiva canónica) — pieza pre-forjada que el agente configura en tiempo de Ingeniería; dos clases (templado · platafórmico). Cap 5.
3. **Generaciones del Botlet (G1/G2/G3)** — modelo evolutivo del nacimiento del código del Botlet; reconciliación de dos ejes (capacidad de autoría vs madurez operativa). Epílogo.
4. **Manifestación y temporalidad** (`discreta`/`continua`) — atributos genéricos del Botlet; el tiempo real se elige por temporalidad continua, no por canal. Cap 5.
5. **Botler genérico** — sin subtipos por dominio; valida orquestando (handle controlado); interfaz Capa 2 ↔ Capa 3 vía MCP; corrección del misnomer "A2A interna"; un Botlet por PI sobre motor compartido. Cap 5.
6. **Vocabulario de Capabilities** — `Capability` reservada al saber-hacer cognitivo de Capa 2; Conector (Capa 4) y Plantilla (Capa 1) como entregables análogos; feature y portabilidad de la Capability. Cap 5.
7. **Interacción declarada acotada** (Faceta embebida) y **PI multi-vista con drill-through** (data-anchored, no-bypass). Cap 4 · Cap 5.
8. **Contrato declarativo de calidad**, **catálogo común y efectos de red**, y la **cadena de derivación** casos-uso → Botlets → proto-Botlets. Cap 5 · Cap 9.

**Sistema visual:** 51 figuras vectoriales (44 heredadas + 7 nuevas), re-enumeradas por orden de aparición.

## v0.3

Tres extensiones: tres tiempos del agente, composición de la Capa 1, y la Faceta.

## v0.2

Diez extensiones: madurez del Botlet, Capa 3 distribuida, portabilidad, Botlets seed/emergente,
certificación regulatoria en Capability, localidad de Capabilities, tres regímenes de GUI,
continuidad operacional, topología paralela, y el título AgencyDomains.
