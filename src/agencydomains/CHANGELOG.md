# Changelog — AgencyDomains

Historial de versiones del libro *AgencyDomains · Arquitectura del Mundo Agentivo*.

**Numeración de figuras:** desde **v1.0** (primera edición) rige la regla
**append-only** — cada figura nueva toma el siguiente número disponible al final, sin
re-enumerar las existentes. En las iteraciones previas a v1.0 podían reorganizarse.

## v1.0 — Agosto 2026

**Primera edición.** El libro se sanciona como obra publicada: el corpus queda
estable y citable, y las ediciones ES/EN quedan a la par. Respecto de la v0.7 no
hay cambios de contenido — lo que cambia es el estatuto: deja de presentarse como
borrador de desarrollo. **Desde esta versión rige la regla append-only** para la
numeración de figuras, según se anunció desde el inicio del changelog.

## v0.7 — Julio 2026

**El género tiene nombre propio: los Lets.** Las piezas empaquetadas que el
Botler hospeda — hasta ahora «unidades» — se consagran como **Lets** (singular
**Let**): nombre derivado de la morfología de la propia familia (Botlet ·
Agentlet), vocabulario normado del canon al rango de Botler — no una novena
primitiva. «Unidad empaquetada de Capa 3» queda como su definición descriptiva.
Resuelve la sobrecarga de «unidad» (que colisionaba con «unidad mínima de
despliegue») y completa la familia nominal Botler · Botlet · Agentlet · Lets.
Invariante ES/EN. Careo de origen: doc 012 v1.2 de la cocina del proyecto.

- Relación canónica del runtime: **1 Proceso = 1 Botler + N Lets** (Cap 5 §2,
  glosario, manifiestos).
- Coronación aplicada en Cap 4 (componentes de Capa 3, Resiliencia,
  aislamiento), Cap 5 §2 (Botler), §4 (Validación y Resiliencia), §7 (sede del
  género), Cap 8 (spec y tags del log) y glosario — la entrada **Let (plural:
  Lets)** reemplaza a «unidad (de Capa 3)» y se muda a su lugar alfabético.
- Diligencia de colisión: nadie usa «Lets» en el espacio agéntico; homónimo
  LETS (Local Exchange Trading System) en dominio ajeno — riesgo bajo, anotado.

## v0.6 — Julio 2026

**El Agentlet — octava primitiva canónica.** El canon incorpora la unidad hermana
del Botlet cuyo cuerpo de ejecución invoca inferencia acotada: la casa de la tarea
recurrente en forma pero interpretativa en cada instancia (clasificar, triar,
resumir, extraer, juzgar), que hasta ahora pagaba precio de Cognición plena o se
forzaba, frágil, a código determinístico. Careo de origen en la cocina del proyecto
(doc 012).

- **Sección nueva Cap. 5 §7 — Agentlets**: definición y charter, la regla de
  contrabando (bidireccional), tablas canónicas Agentlet vs Botlet y Agentlet vs
  Agente (agenda vs charter), test de frontera de tres preguntas, el Botler como
  tutor único (handle con punto de control `cognition_call`), semántica de madurez
  propia (estabilización, no convergencia; offline solo con modelo edge declarado),
  proto-Agentlet con cadena de derivación y catálogos, la economía de los tres
  peldaños, criterios de uso y conformidad.
- **El género «unidad»**: el Botler hospeda unidades — Botlets y Agentlets —; la
  relación canónica se generaliza a `1 Proceso = 1 Botler + N unidades` (Cap. 5 §2,
  glosario). El aparato compartido se predica del género; las garantías
  diferenciales, de cada especie.
- **El paraguas «Agente» pasa a tres miembros**: Asistente · Agente Autónomo ·
  Agentlet (Cap. 5 §5, glosario).
- **El pilar de Validación gana sede en Capa 3**: los mecanismos del Pilar 3 aplican
  sobre la inferencia acotada de los Agentlets en el punto de control del Botler
  (Cap. 4, Cap. 5 §4).
- **Economía de la vía Autonomía matizada**: tres peldaños de costo (Botlet ~0 ·
  Agentlet acotado y presupuestado · Cognición plena); el mix se declara por unidad
  (Cap. 4).
- Conteo del elenco actualizado en Cap. 4, Cap. 9, Epílogo y frontmatter; glosario
  con entradas nuevas **Agentlet**, **proto-Agentlet** y **unidad (de Capa 3)**;
  la transición de cierre del Cap. 5 se reubica al final real del capítulo.

## v0.5 — Julio 2026
> **Revisiones dentro de v0.5** (auditoría integral + decisiones editoriales,
> 2026-07-03): frontmatter.tex a v0.5; doctrina del Botlet de fachada fijada
> (Capa 3, superficie en Capa 1); Botler «constructo normado» ×5; glosario
> Conector de los manifiestos; 5 entradas nuevas de glosario (Auditoría ·
> Transparencia · Observabilidad · Wingtraining · SME); desduplicación Cap 2↔7;
> dosificación Gartner; canon de la pregunta Nadella declarado con sus
> conjugaciones. Detalle en
> `editorial/auditorias/_correcciones-aplicadas-v0.5.md`.

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
- **Rescate fundacional** (del documento original *La Línea Nadella*,
  dic-2024): la **cita completa de Nadella** con su mecánica CRUD y sus dos
  fases entra al Cap. 1 junto al **espectro con el polo extremo** (Musk) y una
  sección nueva de **contra-argumentos** («Por qué la línea podría no
  cruzarse») con las respuestas del canon; los **precedentes históricos** del
  patrón de coexistencia (mainframe/web/nube) entran al Cap. 2; la **crisis de
  monetización del SaaS** y sus cuatro modelos emergentes entran al Cap. 6; el
  **porcentaje agentivo** se enlaza a *AURA*, donde vive como indicador.

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
