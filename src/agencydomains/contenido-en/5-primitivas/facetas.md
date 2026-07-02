## Facets

The primitives the five preceding sections described — AgencyDomain, Botlet, Capability, Trust Infrastructure, Assistant vs Autonomous Agent — live mainly in Layers 2, 3, and 4 of the Agentive Architecture. Layer 1 (Interaction) had been left without a primitive of its own: only described as **generation regimes** (Chapter 4 §1) and as **composition of presentation Botlets** (shell, view, operation). What was missing was a name for the atomic piece out of which those surfaces are built.

This section formalizes the **Facet** as the **sixth canonical primitive** — the minimal unit of Layer 1, an instrument the agent invokes during conversation or assembles into presentation Botlets.

> *The Botlet is the agent's muscle memory. The Facet is an instrument the agent picks up while it thinks.*

### Definition

A **Facet** is an atomic, reusable component of Layer 1 (Interaction) that offers the user a specific form of non-conversational interaction: a freehand drawing board, a catalog-picker, a color matrix, a calendar, a clickable map, a slider, a drag-and-drop ordering, a file picker, a configurable canvas view. One of the many faces that interaction with the user can take at a given moment.

The Facet is an **instrument**, not a process. It lives and operates in Layer 1. It is invoked by cognition during active interactions or assembled by Layer 1 Botlets (shells and views) as a piece of their internal composition.

<!-- FIG:g14-faceta-vs-botlet -->
![Facet vs Botlet · two primitives, two layers, two natures](figuras/g14-faceta-vs-botlet.png)

### Facet vs Botlet — the canonical distinction

The Facet and the Botlet are the agent's two software primitives. They are easily confused because both are pieces with an identity of their own that the agent uses to do things. The canonical distinction:

| Axis | **Facet** | **Botlet** |
|---|---|---|
| **Layer** | Layer 1 (Interaction) | Layer 3 (Autonomy) |
| **Nature** | Interaction instrument | Agent's muscle memory |
| **When does it operate?** | During active conversation | In the background, with no cognition present |
| **Activation** | Cognition invokes it explicitly | Pattern Recognition or external call |
| **Fallback guarantee** | NO — if it fails, the agent reverts to text | YES — cognition executes manually |
| **Life cycle** | Ephemeral (lives as long as the task) | Persistent across sessions |
| **Regeneration** | No regeneration cycle | `95/4/1` cycle with regeneration |
| **Maturity phases** | Not applicable | Junior · learning · senior |
| **Reuse** | Flat instrument catalog | Catalog by capability and domain |

The ontological difference matters: **the Botlet automates; the Facet interacts**. A Botlet executes consolidated know-how without immediate human participation. A Facet opens a visual-manipulative channel of communication with a human who is active in the conversation.

### Two canonical uses

#### Use 1 · Direct invocation by cognition

The agent, during a conversation, **decides** that the information it needs from the user can be obtained faster through a Facet than by continuing the verbal dialogue. It composes an ephemeral surface with one or several Facets, presents it to the user, receives the information, and the conversation continues. The ephemeral surface **is not a Botlet** and does not persist — it lives as long as the immediate task.

This use directly realizes the **GUI generated on-the-fly** regime of Chapter 4 §1. The Facet is the piece that materializes that regime.

#### Use 2 · Composition in presentation Botlets

The **shell** and **view** Botlets (Chapter 4 §1, *Composition of Layer 1*) assemble Facets as internal pieces of their construction. The "order detail" view uses the "product matrix" Facet + the "calendar" Facet + the "customer picker" Facet. The view Botlet defines the orchestration, the layout, the data flow between pieces; the Facets are the individual instruments the Botlet puts on the screen.

This use lets persistent surfaces (regime 3 of Chapter 4 §1) be built by reusing a Facet catalog, without each view Botlet having to reinvent every atomic component.

### Declared bounded interaction

A piece of information already materialized — a self-contained snapshot the agent forged in its Engineering time — can carry interaction over its own data without ceasing to be a reproducible piece. But not all interaction is of the same kind. **Declared bounded interaction** is the category that separates what a piece can offer from what belongs to another primitive.

The distinction is drawn between two interactivities:

- **Free exploration** launches new and arbitrary queries against the source (ad-hoc drill or pivot), operates over an open space, loses reproducibility, exceeds `G1` (the Botlet generations, Chapter 5 §2), and lives outside the information proto-Botlet — in another Botlet or in cognition itself. A piece of information **MUST NOT** absorb it.
- **Declared bounded interaction** operates over the already-materialized snapshot, within a declared space (dimensions and values bounded in advance), preserves reproducibility, is `G1` —configuration, not code— and lives in the piece itself, realized via a Facet.

| What distinguishes them? | Free exploration | Declared bounded interaction |
|---|---|---|
| New query against the source | yes, arbitrary (ad-hoc drill/pivot) | no — operates over the already-materialized snapshot |
| Interaction space | open | declared (bounded dimensions and values) |
| Reproducibility | lost | preserved (same config + data → same artifact + same set of controls) |
| Generation | exceeds `G1` | `G1` (it is configuration, not code) |
| Where does it live? | another Botlet / cognition (Layer 2 + Layer 1) | in the piece itself, via a Facet |

#### Embedded Facet

The mechanism that realizes declared bounded interaction is already canonical: it is the composition of Facets (Use 2), applied inward into a materialized piece. It is the **piece** that composes the Facet — not the Facet that composes others —; the Facet remains atomic. An **embedded Facet** is a Facet bounded to a declared dimension of the piece's own data — a filter, a segmenter, an appearance selector. When it is activated, the piece's *data-bound* elements —KPIs and measures as declared aggregations (`sum`, `ratio`, and the like) over the embedded dataset, distributions, traffic lights— are **recomputed client-side** over the filtered subset: the aggregation is declared once and re-evaluated when the subset changes. Cognition does not explore; the Facet filters the snapshot.

The witness case is an attendance dashboard with a filter by area: the user selects one or several areas and the piece recomputes its KPIs and its traffic light over the subset.

This recognizes a third use of the Facet — an extension of Use 2 toward the materialized piece —: the Facet vs Botlet distinction admits this third use without altering the nature of the Facet, which remains ephemeral and without a fallback guarantee. What is new is that the piece can compose it for bounded interaction, in addition to invocation by cognition during conversation.

### Associated agentive behavior

The existence of the Facet as a canonical primitive enables a specific agentive behavior: the agent, during a conversation, **estimates in real time** whether the information it needs is best obtained verbally or visually. When it estimates that the visual path wins, it offers an appropriate Facet.

The calculation is the agent's own cognitive act, not a pre-programmed feature of the product. The Facet as a primitive enables the decision; the heuristic exercises it.

#### Canonical heuristics for invocation

| Nature of the information | Recommended modality |
|---|---|
| Low dimensionality + well structured (a yes/no, a date, a number) | Conversation |
| High dimensionality (multiple related fields) | Form or composition Facet |
| Hard to verbalize (color, position, shape, gesture) | Specialized Facet (color matrix, map, drawing) |
| The user already has it in spatial or visual form (a layout, a map, a drawing on paper) | Facet that receives that form directly |
| Comparison among multiple options | Catalog-picker Facet with comparative view |
| Configuration with many independent dimensions | Panel Facet with sliders and toggles |
| Open creative work (not an answer to a closed question) | Canvas or easel Facet |

#### Anti-heuristics (when NOT to offer a Facet)

- When the question is genuinely closed and verbal — offering a Facet adds friction, it does not reduce it.
- When the user is on a channel with no graphical capability (pure voice, IVR, SMS) — the Facet is not invocable.
- When the cost of loading the Facet exceeds the benefit of the visual interaction (single-step interactions, trivial data).
- When the conversation is in flow and the Facet interrupts it inappropriately.

The agent that learns to calibrate these decisions — when to offer, when not to — operates in a full Layer 1. The one that only converses stays at the middle of the possible interactive range.

When a Facet is composed inside a materialized piece (declared bounded interaction), the decision ceases to be conversational and becomes part of the piece's configuration: the agent declares the space of controls at Engineering time, preserving the **reproducibility** —a MUST property of the information artifact— already established above.

### Anatomy of the Facet

The canonical specification of a Facet includes six components:

1. **Identity** — canonical name (e.g.: `pizarra-dibujo`, `matriz-colores`, `calendario-rango`) plus version.
2. **Interaction modality** — what kind of input it accepts (touch, mouse, keyboard, gesture), what kind of output it produces.
3. **Input schema** — the data the invoker (cognition or view Botlet) passes to it when instantiating it.
4. **Output schema** — the data it returns when the user completes their interaction.
5. **Internal state** — what it keeps while active (intermediate selections, partial edits, undo stack).
6. **Channel compatibility** — which Layer 1 channels support it (web, mobile, kiosk, not supported on voice).

Facets are published in a **flat catalog**: there is no hierarchy of Facets because each one is atomic. What there is is a growing set of available instruments, indexed by modality and by application domain.

### Emergent catalog

The industry converges gradually toward a canonical set of reusable Facets — the equivalent of the UI component catalog of the pre-agentive eras (Material, Bootstrap, Ant Design), but with the ontological difference that these components are **invocable by cognition** and do not serve solely to build humanly programmed applications.

Some emergent canonical Facets:

- `pizarra-dibujo` — freehand drawing surface.
- `catalogo-selector` — view of items with selection.
- `matriz-colores` — palette or individual color picker.
- `calendario-rango` — date or date-range picker.
- `mapa-clickeable` — map with selectable points.
- `slider-multi` — one or several related sliders.
- `dragdrop-orden` — reordering of items.
- `formulario-dinamico` — form with fields generated on the fly.
- `lienzo-creativo` — open canvas for artifact production.
- `selector-archivo` — invocation of the client's file system.

The spec does not close the catalog: new Facets are coined as the industry identifies canonical modalities that justify a primitive of their own.

### Conformance

A Facet implementation conformant to this specification must satisfy:

| Requirement | Level |
|---|---|
| Identity and version declared | **MUST** |
| Explicit input and output schema | **MUST** |
| Channel compatibility declared | **MUST** |
| Atomicity — does not internally compose other Facets | **MUST** |
| Explicit Facet vs Botlet distinction in documentation | **MUST** |
| Direct invocability by cognition during conversation | **MUST** |
| Composability within shell and view Botlets | **MUST** |
| Composed in a materialized piece as declared bounded interaction (declared space of controls, no new queries) | **MAY** |
| Preservation of the piece's reproducibility when composed as an embedded Facet (client-side recomputation, no Capability invocation) | **MUST** |
| Public catalog of Facets available to the AgencyDomain | **SHOULD** |
| Invocation heuristics documented for cognition | **SHOULD** |

### Evolution frontier

Three active areas of evolution of the Facet as a primitive deserve mention.

The **catalog standardization** is the first. The industry has not yet consolidated a universal canonical set of Facets. Each agentive platform defines its own, with partial intersections. The emergence of a common catalog with stable identities would let agents operate over any conformant AgencyDomain.

The **federation of Facets** is the second. When two AgencyDomains collaborate (federation, Chapter 5 §1), the Facets one exposes must be invocable from the other. The spec does not yet define a formal protocol for federated Facet invocation — it is open work.

The **channel negotiation** is the third. A Facet declares which channels it supports. Cognition must negotiate — if the user is on voice, it cannot offer the Facet; it must degrade to conversation. Without this explicit negotiation, surfaces fail on unexpected channels. The spec requires declaration but does not yet formalize the degradation protocol.
