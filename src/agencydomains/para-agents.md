---
title: AgencyDomains — Canonical manifesto for agents
edition: Development draft · v0.6 · July 2026
canonical_source: libro-agency_domains-v0.6 (human book, Spanish)
license: GFDL v1.3 (proposed)
audience: agents that must reason within the framework
status: pre-1.0 — no commitment to reference stability until v1.0
---

# AgencyDomains — Canonical manifesto for agents

> Structured extract of the **v0.6 (development draft)** edition of the book *AgencyDomains: Architecture of the Agentive World*. This document condenses the canonical vocabulary, the formal constructs, and the required properties. The human edition of the book additionally carries motivation, industry data, extended examples, and derivations — all of that lives outside this document.

> This canon contains the **structure and the vocabulary** of the Agentive World: definitions, primitives, required properties, canonical separations. **It does not contain methods to implement or operational catalogs** — those live in complementary bodies. The public reference implementation is **AgencyDomains.org**, materialized in **Vergis**, designed so that any developer or student can download it, read it, run it, and learn how the canon translates into living systems. Other implementers (commercial products, proprietary codices) offer their own complementary bodies over the same canonical structure.

## How to use this document

- **It is canonical context**, not an executive summary. Every definition and property matters for reasoning within the framework.
- **Series**: AgencyDomains is Book III of the Agentive World trilogy — *The Real-Time Enterprise* (the destination; has its own manifesto) · *AURA* (the path; has its own manifesto) · **AgencyDomains** (the architecture). Shared trilogy terms (the Nadella Line, agentive, real-time enterprise, Trust Infrastructure) are consistent across books.
- **A mirror of v0.6** — the current in-development edition of the book. If this document contradicts the human book, the human book wins.
- **Mandatory vocabulary**: terms in `code` and **bold** are canonical. Do not substitute synonyms.
- **MUST/SHOULD conventions**: the spec uses those verbs in the RFC 2119 sense.
- **pre-1.0 status**: the book is published as a development draft at agencydomains.org and remains under active development. Terms, structures, and numbering may change between v0.x. Reference stability is committed from v1.0 (first stable release).
- **Changes v0.6 vs v0.5**: the **Agentlet** is incorporated as the **eighth canonical primitive** — the Botlet's sibling unit whose body invokes **bounded inference**; the home of the task recurrent in form but interpretive in every instance (Chapter 5 §7). With it: the **unit** genus (`1 Process = 1 Botler + N units`; the Botler hosts Botlets and Agentlets with one more control point in the handle — `cognition_call`); the **Agent** umbrella grows to three members (Assistant · Autonomous Agent · Agentlet; **the Agent has an agenda, the Agentlet has a charter**, with a three-question border test); the bidirectional **smuggling rule** (inference in the body → Agentlet; deterministic body → Botlet); the **proto-Agentlet** in the derivation chain and the catalogs; **maturity semantics of its own** (spec stabilization and decreasing escalation rate — no convergence to determinism; offline only with a declared edge model); the **three-rung economics** (Botlet ~0 · bounded Agentlet · full Cognition); and the **Validation pillar with a seat in Layer 3** over the bounded inference.
- **Changes v0.5 vs v0.4**: a full editorial pass over the trilogy — the **Botlet generations** `G1`/`G2`/`G3` are formalized in Chapter 5 §2 (the Epilogue keeps the background essay without normative weight); the **Information Product** gains its canonical home as a normed term of the Botlet spec (multi-view, drill-through, and their MUSTs); **Capability doctrine restored** — locality (cloud/edge/hybrid) and regulatory certification are predicated of the **Connector** (ESC/POS-Printer, Cash-Drawer, Pinpad, and DTE-SII reclassified) and the **regulated Capability** carries the normative knowledge; the **Botler** is no longer called a primitive (a normed construct of the Botlet spec; the canon remains seven); Chapters 2 ↔ 7 de-duplicated and Chapter 4 slimmed in favor of Chapter 5; the Chapter 6 actor table aligned with its text and "Comprehensive platform" corrected in the glossary; **foundational rescue** from the original document *The Nadella Line* (Nadella's full quote with its CRUD mechanics and its two phases, the spectrum with its extreme pole, counter-arguments with the canon's answers, the historical precedents of coexistence in Chapter 2, the SaaS monetization crisis in Chapter 6); the "The trilogy" micro-section with AURA's five specifications; **Dominion** adopted by the Epilogue; Wingtraining, SME, and RLS defined in the glossary.
- **Changes v0.4 vs v0.3**: canonical extensions that emerged while building the reference implementation and real projects — **Vergis** (public reference implementation, AGPL, AgencyDomains.org) with the naming scheme Vergis · Botler · Mira; the **proto-Botlet** added to the cast of primitives (tempered · platform) and the **derivation chain** use-cases → Botlets → proto-Botlets; **Botlet generations** G1/G2/G3 with the reconciliation of two axes; **manifestation** and **temporality** (`discrete`/`continuous`) as Botlet attributes; **generic Botler** (no per-domain subtypes; validates by orchestrating; Layer 2 ↔ Layer 3 interface via `MCP`; source code vs spec; one Botlet per `PI`); correction of the "internal A2A" misnomer (`A2A` reserved for the relation between AgencyDomains); `Capability` reserved for the cognitive know-how of Layer 2, with **Connector** (Layer 4), **Template** (Layer 1), **feature**, and **Capability portability**; **declared bounded interaction** (embedded Facet) and **multi-view `PI` with drill-through**; **declarative quality contract** in Trust Infrastructure.
- **Changes v0.3 vs v0.2**: the agent's three times (Preparation · Attention · Engineering), composition of Layer 1 (shell · view · operation), and the Facet as Layer 1's atomic primitive.
- **Changes v0.2 vs v0.1**: the main title *AgencyDomains* + ten extensions (Botlet maturity, distributed Layer 3, portability, seed/emergent, certification in the Capability, Capability locality, GUI on-the-fly, operational continuity, parallel topology, title).

---

## 1 · Panoramic view

```
                    THE PARADIGM
                          │
                          ▼
              ┌─────────────────────────┐
              │                         │
      The Nadella Line          The Agentive World
      (the question)            (the consequences)
                          │
                          ▼
                THE AGENTIVE ARCHITECTURE
                          │
          ┌───────────────┼───────────────┐
          │               │               │
     4 layers         Trust Infra      Agent First
     (parallel        cross-cutting    (governing principle)
     topology)
                          │
                          ▼
                   THE PRIMITIVES
                          │
   ┌──────────┬───────────┼───────────┬──────────┐
AgencyDomain Botlet    Capability   Trust    Assistant
+ proto-     + Agentlet (Layer 2 ·   Infra    vs Autonomous
Botlet       (units:    Connector ·           Agent
(pre-forged) manifest./ Template)             + Facet
             tempor.)
                          │
                          ▼
                   THE MARKET POSITIONING
                   (AI value chain · 11 × 4)
                          │
                          ▼
                   THE APPLICATIONS
                   (Real-time knowledge ·
                    Varnished Kimball · conversational BI)
                          │
                          ▼
                   THE OPERATION
                   (Trust Infra operationalized ·
                    policies · CRUDLEX · log ·
                    operational continuity)
```

**The eight canonical primitives**: **AgencyDomain** · **Botlet** · **proto-Botlet** · **Agentlet** · **Capability** · **Trust Infrastructure** (cross-cutting axis) · **Assistant vs Autonomous Agent** · **Facet**. The **proto-Botlet** is the pre-forged piece the agent configures to instantiate a Botlet; the **Agentlet** is the Botlet's sibling unit with bounded inference; the **Facet** is the atomic primitive of Layer 1.

> **Numbering note**: when the canon labels the Facet as the *sixth primitive*, the proto-Botlet as the *seventh primitive* and the Agentlet as the *eighth primitive*, the ordinal indicates the **order of incorporation into the canon** (Facet in v0.3, proto-Botlet in v0.4, Agentlet in v0.6), **not** the position in this list.

**Pre-agentive layer (BCA)**: cartography of the state *prior* to crossing the Nadella Line. Three layers (Presentation · Business Logic · Domain), seven structural separations (the seventh, canonical: Procedural / Agentic), with explicit mapping of how each cell migrates into the Agentive World.

**Reference implementation**: **Vergis** — the public reference implementation of AgencyDomains (AGPL, AgencyDomains.org), category **Meta-Cognitive Platform**. It materializes the canon in an executable runtime.

---

## 2 · The paradigm — the Nadella Line

### The dividing question

> *Does the human open applications to do their work?*

Origin of the name: Satya Nadella on the BG2 podcast (December 2024) — *"The notion that business applications exist — that's probably where it all collapses, in the era of agents."*

### Two worlds

```
◄──── Agentic World ────┤├──── Agentive World ────►
Apps complemented          Apps collapse
by copilots                Conversation with agents
Incremental evolution      Applications survive
                           as invisible backend
                           Fundamental transformation
```

- **Agentic** — agents are complementary tools that extend existing applications. Humans keep opening applications. Traditional interfaces persist; agents enhance them.
- **Agentive (Agentive World)** — agents as the sole interface. Applications collapse. The human stops opening applications; they converse with agents that have access to systems and data.

### Online enterprise vs Real-time enterprise

- **Online enterprise** — data current to the second, dashboards up to date, but it **depends on humans** to look, interpret, and decide.
- **Real-time enterprise** — it **detects, interprets, decides, and acts** continuously and autonomously, within governed frames. The product of crossing the Nadella Line.

### Three axes of deep change

Crossing the Nadella Line changes **six dimensions** of operation simultaneously (human-information relationship, nature of data, roles of human work, economics of information, governance, operating model). None changes in isolation. Those six dimensions group into **three axes**:

1. **Human-information relationship + roles of human work.**
2. **Data + operating model.**
3. **Governance + economics of information.**

The three are interdependent: advancing in one alone without the others produces **successful pilots but no real transformation**. The crossing is systemic or it is not.

### Evolutionary coexistence

```
Stage 1 (Initial):    Assistant 90%  ████████████████░░  Autonomous Agent 10%
Stage 2 (Adoption):   Assistant 70%  ████████████░░░░░░  Autonomous Agent 30%
Stage 3 (Maturity):   Assistant 50%  █████████░░░░░░░░░  Autonomous Agent 50%
Stage 4 (Advanced):   Assistant 30%  █████░░░░░░░░░░░░░  Autonomous Agent 70%
```

---

## 3 · The pre-agentive state — Bounded Concerns Architecture

> Formal cartography of the state *prior* to the crossing. It is not the architecture of the destination — it is the architecture of the transition.

### Operational principle — the thinness of the domain

Agents are **volatile** (statistical correctness, evolution by retraining). Business invariants **cannot be** (binary correctness, structural cadence). If they coexist in the same layer without an explicit boundary, agentic volatility contaminates the reliability of the domain.

→ **The authoritative core is kept strictly thin**, expelling all volatile logic outward. The agentic incursion is confined to the layer designed to tolerate volatility.

### Three layers

| Layer | Content |
|---|---|
| **1 · Presentation** | UI (humans) · API (systems) — treated as parallel citizens. |
| **2 · Business Logic** | Orchestration. Two parallel boxes: **Procedural** (explicitly programmed) · **Agentic** (contextually derived from a model). |
| **3 · Domain** | Stable core. Two orthogonal dimensions: **SOR** (System of Record, own domain) vs **External** (foreign domain) on the vertical axis; **Logic** vs **Persistence** on the horizontal axis. Each cell subdivides into a synchronous and an asynchronous path. |

Deliberate lexical asymmetry in the asynchronous leg: **Streams** (SOR side — outgoing, own authorship) vs **Hooks** (External side — incoming, foreign authorship).

### The seven structural separations

| # | Separation | Materialized by |
|---|---|---|
| 1 | Human presentation vs external contract | UI and API in Layer 1 |
| 2 | Orchestration vs domain rules | Layer 2 / Layer 3 boundary |
| 3 | Logic vs persistence | Horizontal bands in Layer 3 |
| 4 | Own vs foreign domain | SOR / External columns in Layer 3 |
| 5 | Synchronous vs asynchronous communication | Parallel paths within each cell |
| 6 | Mutable state vs event log | Repository/Streams and Proxies/Hooks pairs |
| 7 | Procedural vs agentic behavior | Procedural / Agentic boxes in Layer 2 |

The **seventh separation** is the initial crack through which the Agentive World enters the enterprise system.

### Mapping of BCA cells to the Agentive World

| BCA cell | Trajectory | Destination |
|---|---|---|
| **UI** | Progressively emptied | Replaced by Layer 1 — Interaction (conversational modalities, GUI on-the-fly, persistent GUI as facade Botlet, signage); the traditional UI survives only in specialized tools with complex surfaces |
| **API** | Persists and intensifies | Becomes a **Connector** within Layer 4 — Access (NOT in Capability) |
| **BL · Procedural** | Contracts | Replaced by Botlets. Only workflows with strict regulatory traceability survive |
| **BL · Agentic** | Expands until it dominates | **Operational seed of the Botlet**. The seventh separation widens until it consumes the layer |
| **SOR · Logic** | Preserved | Invariant logic within the AgencyDomain |
| **SOR · Persistence** | Preserved | Storage layer of the AgencyDomain |
| **External · Logic** | Preserved, repositioned | Federation patterns managed by Trust Infrastructure |
| **External · Persistence** | Preserved | Storage layer of the federation |
| **Events (sync/async SOR)** | Preserved, gain weight | Coordination substrate between Botlets and AgencyDomains |

**Four general patterns of the crossing**:

1. **Layer 3 survives almost intact** — it becomes the substrate of the AgencyDomains.
2. **Layer 2 transforms deeply** — Procedural contracts; Agentic dominates; both become Botlets that compose behavior from Capabilities.
3. **Layer 1 bifurcates asymmetrically** — UI dies; API thrives as a **Connector** (Layer 4).
4. **Trust Infrastructure appears as a new cross-cutting concern** — what in BCA was implicit and scattered is elevated to an explicit cross-cutting layer.

---

## 4 · The architecture — four layers in parallel topology

> **Canonical clarification**: the four layers are an **X-ray of the individual agent** — the four behaviors every agent must exhibit. **They are NOT links in an industrial value chain** nor slots where a product is assigned to each. The industrial chain is treated in Chapter 6 — they are distinct lenses that cross cleanly when kept separate.

### The parallel topology

**Layers 2 (Cognition) and 3 (Autonomy) are parallel paths between Layer 1 and Layer 4, not stages in series.** The numbering 1 → 2 → 3 → 4 has didactic value — Layer 1 is the surface the human meets, Layer 4 is where the system touches the real world — but **it does not describe the order in which operations traverse the system**. An operation enters through Layer 1 and reaches Layer 4 by traversing one of the two paths — or both in different stretches — but never both in mandatory series.

```
                ┌──────────────────────────┐
                │  Layer 1 · Interaction   │
                └────┬───────────────────┬─┘
                     │                   │
                     ▼                   ▼
           ┌─────────────────┐ ┌─────────────────┐
           │  Layer 2        │ │  Layer 3        │
           │  Cognition      │ │  Autonomy       │
           │                 │ │                 │
           │  Conversation   │ │  Botlets        │
           │  New decision   │ │  Stable pattern │
           │  New case       │ │  (95/4/1 cycle) │
           └────────┬────────┘ └────────┬────────┘
                    │                   │
                    ▼                   ▼
                ┌──────────────────────────┐
                │  Layer 4 · Access        │
                │  (Capabilities)          │
                └──────────────────────────┘

         Trust Infrastructure (cross-cutting to all four)

         Interaction 2 ↔ 3 (internal · via `MCP`):
           · Cognition delegates to Botlet (2 → 3)
           · Botlet escalates fallback to Cognition (3 → 2)
           · Cognition observes the Botlets' log (2 ← 3)
```

**Layer 2 ↔ Layer 3 interface via `MCP`**: the **Cognition** (`LLM` agent, Layer 2) commands its muscle memory — the **Botler** (Layer 3 runtime, no agency) — over an **internal** interface within the same AgencyDomain. The natural transport is `MCP`: the Botler exposes `MCP` server(s), the Cognition is the client. **This is NOT `A2A`**: `A2A` (the agent-to-agent relation) is reserved for communication **between distinct AgencyDomains**.

**Regime of each path**:

- **Cognition Path** — slow, costly, decisive. For conversation, new decisions, unanticipated cases.
- **Autonomy Path** — fast, cheap, repetitive. For Botlet execution over stable patterns.

**Five structural consequences** of the parallel topology:

1. **Trivial offline mode** — without network, the Cognition path (cloud) falls; the Autonomy path (edge) stays active. The operation traverses the AgencyDomain by whichever path stays alive.
2. **Evident cognitive economics** — the organization chooses which path each operation flows through: repetitive → path 3 (cheap); new or decisive → path 2 (costly). Total cost is the mix of the two paths.
3. **Trust Infrastructure is exercised on both paths** — policies apply before invoking Layer 4 regardless of which path the invocation comes from.
4. **It distinguishes two kinds of Botlets** — **operational facade Botlets** (invocable from Layer 1, stable contract, propagated human identity) vs **internal tool Botlets** (invocable only from Layer 2). Both live in Layer 3; they differ in their invocation surface.
5. **`Layer 1 → Layer 3 → Layer 4` is a canonical path** — an operational surface (POS, kitchen screen, industrial panel) that invokes a senior Botlet traverses this path without touching Layer 2. **It is not a bypass; it is one of the two structural paths.**

### The agent's three times

The parallel topology describes **where** each operation lives. The three times describe **when** the agent operates. A canonical temporal frame, complementary to the spatial one.

| Time | Regime | Metrics | Cognitive path |
|---|---|---|---|
| **Preparation** | Batch · off-peak | Catalog quality · Botlet precision · Capability coverage | Cognition over consolidated data |
| **Attention** | Real time · priority | Satisfaction · latency · resolution rate without escalation | Cognition + Autonomy per pattern |
| **Engineering** | Medium term (minutes to hours) | Coverage · first-deploy success rate · average iterations | Cognition decides · Autonomy persists |

**Operational implications**:
- **Scheduling of cognitive capacity**: Attention is priority; Preparation uses the valleys; Engineering is intermediate. Without the distinction, Preparation is relegated and the agent stops improving itself.
- **Metrics separated by time**: a single dashboard lies; catalog quality is measured differently from operational satisfaction.
- **Availability model**: a well-operated agent is **not 100% in Attention** — it needs Preparation windows. The promise "always-available agent" is understood as "Attention always available".

> *The agent does not attend at every moment — but it can attend at any moment because it dedicates time to preparing.*

**Required properties**:
- Explicit recognition of the three times in operation (MUST).
- Metrics separated by time (MUST).
- Reserved, not optional, Preparation windows (SHOULD).
- Scheduling of cognitive capacity by time priority (SHOULD).
- Traceability in the log of which time executed which operation (SHOULD).

### Structural diagram — all layers with parallel topology

```
                ┌──────────────────────────────────────────────────────────┐
                │  LAYER 1 · INTERACTION                                   │
                │  Pure conversational · GUI on-the-fly · persistent GUI    │
                │  (facade Botlets) · Voice · API · Channels · Signage      │
                └────┬─────────────────────────────────────────────────┬───┘
                     │                                                 │
                     ▼                                                 ▼
       ┌────────────────────────────┐               ┌────────────────────────────┐
       │  LAYER 2 · COGNITION       │               │  LAYER 3 · AUTONOMY        │
       │  Multi-LLM · Capabilities  │               │  Botlets and Agentlets     │
       │  Pattern Recognition       │  ◄── 2 ↔ 3 ──►│  Botler (central + edge)   │
       │  Botlet generation         │               │  Asynchronous tasks        │
       │  Reactive assistant        │  ◄── `MCP` ──►│  Monitoring · A2A protocol │
       │  Slow · costly · new       │   internal    │  Fallback guarantee        │
       └─────────────┬──────────────┘               └─────────────┬──────────────┘
                     │                                             │
                     ▼                                             ▼
                ┌──────────────────────────────────────────────────────────┐
                │  LAYER 4 · ACCESS                                        │
                │  Tools (MCP) · A2A between AgencyDomains · CRUDLEX       │
                │  Human approval · Append-only log · Routing              │
                │  Semantic cache · Connectors                            │
                │  (cloud · edge · hybrid)                                │
                └──────────────────────────────────────────────────────────┘

   ═══════════════════════════════════════════════════════════════════════
   TRUST INFRASTRUCTURE — cross-cutting to all four layers
   Governance · Audit · Validation · Resilience · Transparency

   GOVERNING PRINCIPLE — Agent First
```

### Layer 1 — Interaction (with three GUI regimes)

Responsible for all communication between humans and the system. Pure interface, no business logic.

**Six canonical modalities** (the **generated GUI** is a single modality with three generation regimes):

- **Textual conversational** — direct chat; the agent answers in text. Sufficient when the information is sequential and the decision is flexible.
- **Voice conversational** — virtual assistants, calls, audio bots.
- **Corporate channels** — Slack, Teams, WhatsApp, email.
- **Programmatic API** — machine-to-machine invocation without human mediation.
- **Generated GUI** — graphical surface generated by the cognition (never by a human UI/UX team), in three regimes: **(1) pure conversational** — no surface, when none is needed; **(2) on-the-fly** — adapted to the immediate task, lives as long as the task lasts, may regenerate differently next time; **(3) persistent as a facade Botlet** — for repetitive operational roles (cashier at peak hour, kitchen panel, register dashboard, industrial panel), a stable surface consolidated as a **facade Botlet** — a Layer 3 Botlet (typically seed) that exposes it in Layer 1 —, which the agent regenerates when the environment changes.
- **Passive signage** — surfaces that communicate continuously without requiring interaction.

> *The GUI does not disappear in the Agentive World. What disappears is the pre-created GUI. Every GUI in an agentive Layer 1 is generated by the cognition — some ephemeral, others stabilized as facade Botlets.*

**Layer 1 calibration**: the question is not whether there is a GUI or how pretty it is. The question is **who generated it**. If a human UI/UX team generated it in traditional application sprints, it is not an agentive Layer 1. If the cognition generated it — ephemeral or persistent as a Botlet — it is.

**Three required properties (MUST)**:
1. **Channel-agnostic** — the conversation logic does not depend on the medium.
2. **Register adaptation** — the agent understands the channel's register without conditional code.
3. **Context persistence** — the conversation survives a channel change.

#### Surface composition · shell, view, operation

A non-trivial surface **is not a monolithic Botlet**. It is a composition of three kinds of Botlets in distinct roles:

| Role | Layer | Nature | Reuse |
|---|---|---|---|
| **Surface Botlet (shell)** | Layer 1 | Container: layout · navigation · session · shared state | Product-specific (little reuse) |
| **View Botlet** | Layer 1 | A screen or panel within the shell · assembles Facets + orchestration | Highly reusable across shells |
| **Operation Botlet** | Layer 3 | Business execution (charge, print, close shift, consolidate) | Most reusable in the catalog · stable contract |

**Key distinction**: shell and view are surface (Layer 1); operation is execution (Layer 3). A surface is a composition of Layer 1 Botlets that orchestrate and invoke Layer 3 Botlets.

```
Layer 1: SHELL → VIEW(s) ─── invokes ───▶ Layer 3: OPERATION(s)
```

Operations accumulate durable architectural value; reusable views are extracted and cataloged; shells remain specific but their construction accelerates by assembling existing pieces.

#### Multi-view Information Product · drill-through

An **Information Product (`PI`)** — the manifestation an informational operation Botlet leaves when consumed — is not necessarily a single piece. It can be composed of **N named pieces/pages**: each **view** is one more piece of the same `PI`, selectable from a picker, with the first as default. The `PI` remains **authz-blind** — neither the views nor the edges connecting them declare authorization; that policy lives in the policy store.

**Drill-through** is the **navigation edge with context**: a table/column declares *"on clicking a row, go to view X passing the key K of this row"*; the destination view renders **filtered by K**.

**Data-anchored / no-bypass (MUST)**: the context `K` **bounds within what the viewer can already see** — the destination view applies its own `RLS` over the source and `K` enters as an additional filter, **never as an override** of the policy. The drill **narrows, never widens** (intersection with the authorized, never union). If the viewer cannot reach the origin row, they do not reach the edge; if they reach it, the destination is still governed by its own policy. Multi-view composition is orthogonal to the Botlet's family: it changes how many pieces compose the manifestation, not its nature.

#### Facet · atomic primitive of Layer 1

The **Facet** is the atomic reusable component of Layer 1: drawing board, catalog-picker, color matrix, calendar, clickable map, slider, drag-and-drop. **Sixth canonical primitive** — distinct from the Botlet (described fully in §7).

**A Facet is NOT a Botlet**:
- A Facet lives in Layer 1 (Interaction) · a Botlet lives in Layer 3 (Autonomy).
- A Facet is an **instrument** the cognition invokes during conversation · a Botlet is **muscle memory** that executes without cognition.
- A Facet has NO fallback guarantee · a Botlet DOES.
- A Facet is ephemeral · a Botlet is persistent.

**Agentive behavior**: the agent **estimates in real time** whether the information is best obtained verbally or visually. If the visual path wins, it offers a Facet. Heuristics: high dimensionality → Facet; low dimensionality → conversation; hard to verbalize (color, position, shape) → Facet; the user already has it in visual form → Facet.

### Layer 2 — Cognition

The agent's brain. Interpretation, reasoning, planning, application of specialized knowledge, the decision to delegate.

**Five canonical components**:
1. **Multi-LLM** — the cognition is not tied to a single provider.
2. **Capabilities** — units of modular, composable cognitive know-how (reserved to this layer).
3. **Pattern Recognition** — detection of repetitive patterns. Inspired by neurobiological architecture. Trigger of emergent Botlet generation.
4. **Botlet generation** — the cognition decides when to delegate repetitive tasks to Layer 3.
5. **Reactive assistant** — agent operating in request-response mode.

**`Capability` reserved for the cognitive know-how of Layer 2**: a **Capability** is **cognitive**, interpretive, decisional know-how. **It is NOT a plugin, NOT a prompt, NOT a system prompt, NOT a tool — it is knowledge.** The Capability decides which tool to invoke. Two analogous terms live in other layers and are named for what they are, without appending the term Capability:

- **Connector** — knowing how **to access source systems** (a connection with execution power; NOT cognitive knowledge). **Layer 4 · Access.** In the legacy→agentive map, an **API** becomes a **Connector** (Layer 4), not a Capability.
- **Template** — client-specific tailoring over a **canonical instrument** (report/dashboard) in a particular format or rule. **Layer 1 · Interaction**, alongside Facets and surface/view Botlets.

**feature** — an internal operation a Capability exposes (the practical equivalent of *feature/operation/skill/method*). **Capability vs feature test** (all three must be yes to treat it as its own Capability): (1) operational independence? (2) cognitive identity — distinct data model and SME? (3) reusability? If one or more is no → it is a **feature** of the containing Capability.

**Capability vs non-Capability test** (all three yes → Capability): (1) is it cognitive know-how? (2) does it have an identifiable SME? (3) does it pass the five Wingtraining steps without forcing? If not: access to systems → **Connector** (Layer 4); tailoring of a canonical instrument → **Template** (Layer 1); operation within a larger Capability → **feature**.

**Capability portability (MUST)**: a conformant Capability can be installed and run on **any conformant AgencyDomain** without rewriting, which makes it **real property of the client** — not of the AgencyDomain nor of the hosting. Relationship: an AgencyDomain **hosts and runs** Capabilities; a Capability **runs on** a host AgencyDomain. Distinct from AgencyDomain portability (across hosting platforms).

**Two modes of access to cognition**:
- **Tokens** — the system centralizes credentials, billing, and policies.
- **Subscription** — the user's assistant (Claude, ChatGPT, Copilot, Gemini) accesses directly under the user's subscription.

Both modes coexist. The spec requires explicitly declaring which mode applies to which component.

**Botlets as economic lever under a fixed Subscription**: on capped plans, an agent that executes via Botlets and invokes cognition only when the environment changes operates continuously without exhausting the quota. Without Botlets, sustained autonomy under a fixed Subscription is economically impossible.

**BYOModel (SHOULD)** — Bring Your Own Model. The agent's spec MUST be independent of the cognition runtime. It enables multi-tenancy with heterogeneous cognition and respects the client's **cognitive sovereignty**.

### Layer 3 — Autonomy (with distributed Layer 3)

Where the agent lives. Persistent life, continuous execution, action on its own initiative. Where the **Autonomous Agents** dwell.

**Six canonical components**:
- **Proactive processing**, **asynchronous tasks**, **continuous monitoring**.
- **Units in execution** — two sibling species: **Botlets** (muscle memory, non-LLM code) and **Agentlets** (packaged routine judgment, bounded inference; §7).
- **Botler** — generic runtime that executes the units of both species. Invisible. **1 Process = 1 Botler + N units**.
- **Intra-AgencyDomain coordination (via the `A2A` protocol)** — communication between runtimes of the same agent. It is NOT `A2A` between AgencyDomains.

**Non-negotiable property — Fallback guarantee (MUST)**: if a Botlet fails catastrophically, the cognition executes the task manually. **The process never stops.**

**Three required properties (MUST)**:
1. **Persistence between sessions**.
2. **Execution isolation** — units (Botlets and Agentlets) under sandboxing.
3. **Structural resilience**.

**The Botler is generic by definition (MUST)**: it manages the lifecycle, isolation, and execution of *any* Botlet **without understanding its domain**. **No Botler subtypes exist by family of operation** (informational, transactional, etc.) — that specialization lives in the Botlets and their proto-Botlets. Botler subtypes are distinguished by **deployment topology and role** (central/edge; operational facade), **never by domain**. A flat architecture: a generic runtime hosts self-contained specialist components.

**The Botler validates by orchestrating, not by executing (MUST)**: it enforces the spec's validation against the Botlet's type without executing it with domain knowledge. It invokes the validation point the type (or its proto-Botlet in G1) provides, hands it the **generic context** it controls (Capability catalog, identity, AgencyDomain policies), and acts on the verdict — accept, reject, record in the append-only log. Sibling pattern: on each invocation the Botler hands the Botlet a **controlled handle** (an object with `capability_call` and `log` bound to the Botler); bypass is **structurally impossible**, not merely forbidden. Principle: the generic Botler exposes **control points** and the specialist plugs into them.

**Distributed Layer 3** (canonical pattern for multiple physical presence): a single AgencyDomain with a **central Botler** (cloud, orchestration, consolidated DB) + **N edge Botlers** (one per physical site, local DB, queue toward central), coordinated by **the `A2A` protocol** (intra-AgencyDomain coordination). Distinct from federation between AgencyDomains; distinct from a simple Cluster. Full detail in §7 (Primitives).

### Layer 4 — Access

Where cognition becomes real action. Every decision MUST pass through governance before touching the world.

**Eight canonical components**:
- **Tool servers** — canonical protocol **MCP**.
- **Connectors** — knowing how to access source systems (the legacy API brought into the Agentive World).
- **`A2A` between AgencyDomains** — federation between distinct agents.
- **Trust Infrastructure exercised at the point of action**.
- **CRUDLEX** — Create, Read, Update, Delete, List, Execute.
- **Human approval**.
- **Intelligent routing and semantic cache**.
- **Immutable append-only log**.

**Four MUST properties in enterprise production**:
1. **Non-repudiation** — every action recorded with identity, context, and result.
2. **Reversibility where applicable**.
3. **Policy before execution** — policy is evaluated **before**, not after.
4. **Uniform observability**.

---

## 5 · Trust Infrastructure — the cross-cutting axis

**It is not an additional layer. It is cross-cutting to all four.**

### Five pillars

| Pillar | Canonical mechanisms | Primary layers |
|---|---|---|
| **Governance** | Configurable policies · CRUDLEX · human approval · AI registry | Layer 4 (primary), cross-cutting |
| **Audit** | Append-only log · trace of each action · decision lineage · per-action identity tagging | Layer 4 (primary), cross-cutting |
| **Validation** | Hallucination detection · response validation · prompt injection prevention · DLP · tokenization | Layer 2 (partial) + Layer 3 (Agentlets' bounded inference) + Layer 4 (primary) |
| **Resilience** | Fallback guarantee · error handling · sandboxing · circuit breakers · rate limiting | Layer 3 (primary), cross-cutting |
| **Transparency** | Full observability · metrics · end-to-end traces · proactive alerts · governance dashboards | Cross-cutting to all four |

### Pillar × layer matrix

```
                    Layer 1        Layer 2        Layer 3        Layer 4
                    Interaction    Cognition      Autonomy       Access

Governance                                                       ████████ (primary)
Audit                                                            ████████ (primary)
Validation                         ████ (partial)                ████████ (primary)
Resilience                                        ████████ (primary)
Transparency        ────────────────────── cross-cutting ──────────────────
```

### Tripartite deployment pattern — Cloud + Client + Local

Three components coordinated in physically distinct places: **Cloud** (the provider's control plane), **Client** (governance plane in the client's internal network), **Local** (execution plane on the user's device).

### Declarative quality contract

Any conformant Botlet MAY declare its quality attributes as **structured properties, not embedded code**, so Trust Infrastructure audits them uniformly, routes them through global policies, and reports them as standard metrics without coupling to each Botlet's implementation. Five canonical attributes:

- **Freshness** — maximum admissible age of the data.
- **SLA** — expected end-to-end latency (`p50`/`p99`).
- **Degradation policy** — `refuse` · `warn_and_show` · `show_last_valid` · `agentic_fallback`.
- **Audience** — `RLS`/`CRUDLEX` policy of who may consume the manifestation.
- **Refresh policy** — `on-demand` · `scheduled` · `push`.

It serves two pillars: **Resilience** reads degradation and refresh as auditable configuration (not fragile scattered logic), with Freshness and SLA as explicit thresholds; **Audit** routes them through global policies and reports them as metrics comparable across Botlets.

---

## 6 · The governing principle — Agent First

> *Faced with any trade-off, the agent's experience is prioritized over the human's. The agent is the primary user; the human's needs are resolved in a management layer without degrading what the agent sees and can do.*

### Operational implications

- Any new capability is specified first as a **tool with a declarative JSON schema**.
- **Structured, actionable errors**.
- **Idempotency where applicable**.
- **Uniform pagination and filters** across tools.
- **Machine-readable documentation**.

Agent First is a **governing rule**: any trade-off that violates it requires explicit, documented justification.

---

## 7 · The primitives

### AgencyDomain

A computational scope with its own identity where autonomous agents and Botlets in execution dwell, **where the Capabilities that give them their know-how are hosted and run**, and where the resources that sustain them live. **Minimal unit of deployment.** The Capability is a first-order inhabitant, not a support resource.

**Foundational premise — Space ≠ Domain**:
- **Space** / **WorkSpace** (Google Workspace, M365, Notion) — human corporeality. Reserved for humans.
- **Domain (AgencyDomain)** — the agent has no body; it has jurisdiction (`dominium`).

Formal lineage: just as **JavaSpaces (JSR-000148, 1999)** standardized distributed spaces for Java without binding the implementation, **AgencyDomains** does the equivalent for agentive environments.

#### Five fundamental properties (MUST — a system that does not meet them is not an AgencyDomain, it is something else with another name)

1. **Own identity** — a unique canonical URI that distinguishes it on any network; survives restart, migration across infrastructures, and change of implementation. Stable, not ephemeral.
2. **Materialization of the four layers** — it materializes Interaction · Cognition · Autonomy · Access and exercises cross-cutting Trust Infrastructure. The layers may be distributed technically, but responsibility for the four rests with the space. No conformant space delivers only three nor delegates a layer without assuming responsibility.
3. **Persistence** — the state (active agents, Botlets in execution, Capability data, audit logs) survives disconnections, restarts, and migrations. It is what makes the AgencyDomain a **place**, not a process.
4. **Isolation** — an explicit boundary; internal resources (compute, memory, data) are not accessible from outside except through defined interfaces (via Layer 4, registered). Not only security: it is **fault containment** — an AgencyDomain that falls does not affect others sharing infrastructure.
5. **Addressability** — AgencyDomain, agents, and Botlets addressable via predictable URLs. Canonical syntax:

```
{domain}/                                  → the space itself
{domain}/agents/{agent}                     → an agent that lives in it
{domain}/agents/{agent}/botlets/{botlet}    → a specific Botlet
{domain}/tools/{tool}                       → a tool exposed via Layer 4
```

Addressability sustains two things: `A2A` (an agent invokes another by its canonical URL, without ad hoc discovery) and **MEO** (frontier models reference AgencyDomains via predictable URLs that appear in their training corpus). Chaotic or unstable URLs → an AgencyDomain invisible to the models.

#### Canonical data model — six spec components

Internal anatomy of a conformant AgencyDomain:

1. **Identity** — canonical URI, credentials with which it authenticates against external systems, root policies no agent may contravene.
2. **Agents** — collection of the space's agents; each with its assigned Capabilities, its Botlets in execution, and its persistent state.
3. **Capabilities Registry** — tree of Capabilities available to the space's agents (shared know-how, invocable by role).
4. **Tools Registry** — collection of tools that Layer 4 exposes outward (the interface through which the AgencyDomain touches external systems).
5. **Trust Layer** — cross-cutting governance and audit: policies, append-only log, validation mechanisms.
6. **Cognition Bindings** — bindings to the cognitive resource: which model provider is invoked, under what credentials, and with what usage policies.

#### Three regimes (technically equivalent; the regime changes, not the capability)

```
Private   = controlled perimeter, no public access     (analogous to Private Cloud)
Public    = externally accessible, registered agents   (analogous to Public Cloud)
Hybrid    = private core + partial public exposure     (analogous to Hybrid Cloud)
```

**Natural migration between regimes without rewriting.**

#### Distributed Layer 3 — canonical pattern for multiple physical presence

A single AgencyDomain with Layer 3 distributed geographically: a **central Botler** (cloud, orchestration, planning, reporting, global decisions, consolidated DB) + **N edge Botlers** (one per physical site, local transactional Botlets, local DB + event queue toward central), coordinated by **the `A2A` protocol** (intra-AgencyDomain coordination between runtimes of the same agent — not `A2A` between AgencyDomains).

```
                        ┌────────────────────────┐
                        │   CENTRAL Botler       │
                        │   (cloud)              │
                        └────────┬───────────────┘
                                 │ A2A protocol
                  ┌──────────────┼──────────────┐
                  ▼              ▼              ▼
          ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
          │ EDGE Botler │ │ EDGE Botler │ │ EDGE Botler │
          │ (site 1)    │ │ (site 2)    │ │ (site N)    │
          └─────────────┘ └─────────────┘ └─────────────┘

         All within the same AgencyDomain
         (single identity · single log · single governance)
```

**Offline mode as an emergent property**: when the edge Botlets are **senior**, the physical site operates against the local DB + edge-resident Connectors without network. The event queue toward central accumulates transactions; when the network returns, it drains.

**Required properties**:
- Single identity of the AgencyDomain (MUST)
- Single internal identity model (MUST) — the Botlers do not authenticate as external AgencyDomains to each other; they share the AgencyDomain's identity model.
- Local DB in each edge Botler (MUST)
- Event queue toward central (MUST)
- Conflict resolution on consolidation (MUST)
- Unified audit log (MUST)
- Uniform Trust regime between central and edge (MUST)
- Offline operation capability at the edge (SHOULD) — when the edge Botlets are senior, the site operates with intermittent network or none.

#### Portability between conformant platforms

A conformant AgencyDomain **MUST** be migratable to another **conformant hosting platform** without rewriting its logic, its state, or its policies. Distinct from migration between regimes (private → public), which changes the regime but not the platform.

**Three technical conditions**:
1. **Botlets against the canonical primitives** of the conformant SDK, not proprietary APIs of the current hosting.
2. **Exportable operational DB** in a reproducible neutral format (documented schema, complete dump, no proprietary types).
3. **Portable Trust Layer** — policies, log, and configuration in a format readable by any conformant implementation.

It guarantees that the AgencyDomain is **real property of the client**, not of the hosting.

#### Account vs AgencyDomain · Domain vs AgencyDomain · Dominion · Cluster vs Federation

- **Account** — a commercial concept; it may own multiple AgencyDomains.
- **Domain** — commercial synonym for AgencyDomain (brand lore, sales, client communication).
- **Dominion** — a Domain obtained by an agent in a public AgencyDomain under the **AgentNation** model.
- **Cluster** — instances of the **same** AgencyDomain sharing load.
- **Federation** — communication between **distinct** AgencyDomains.

#### Agent lifecycle — six canonical phases (each transition → append-only log of the Trust Layer)

1. **Provisioning** — the AgencyDomain creates the agent: assigns identity, associates the initial Capabilities, registers it in the space. It is born when the phase ends successfully; if it fails (credentials, name conflict, quota), it never comes to exist.
2. **Bootstrap** — it enters operation: loads its persistent state if it exists (recovers context after hibernation or restart), establishes bindings with cognition and tools, verifies Capability availability.
3. **Reactive operation** — Assistant mode, Layer 2 active. Responds to the human's requests; between requests it stays passive (no active compute).
4. **Proactive operation** — Autonomous Agent mode, Layer 3 active. Pursues objectives in the background, monitors events, executes Botlets, escalates to the human at thresholds; Pattern Recognition generates and maintains Botlets. Materializes *"intelligence goes to people and acts on their behalf"*.
5. **Hibernation** — persistent pause: state saved, no active compute. Preserves context without spending resources (e.g., an agent that hibernates outside business hours and reactivates the next day).
6. **Decommissioning** — the AgencyDomain retires the agent: state archived or deleted per policy, Capabilities released, identity recorded in the historical log. It formally closes the cycle — "decommissioned" ≠ "forgotten": the record allows auditable reconstruction that the agent existed, what it did, and why it ceased to exist.

#### Communication · Layer 2 ↔ Layer 3 interface vs `A2A`

`A2A` (`agent-to-agent`) is a name reserved for the **relation between distinct AgencyDomains** — distinct agents, each with identity and agency; federation, open work.

- **Layer 2 → Layer 3 interface via `MCP`** — the Cognition commands the Botler (its muscle memory) within the same AgencyDomain. The Botler exposes `MCP` server(s); the Cognition is the client. **It is NOT `A2A`.**
- **Intra-AgencyDomain coordination (via the `A2A` protocol)** — the transport between Botlers of the same AgencyDomain uses **the `A2A` protocol** (the protocol's proper name). One says "via the `A2A` protocol", **never "internal A2A"** — those Botlers are runtimes of the same agent, not two agents.
- **`A2A` between AgencyDomains** — between agents that live in distinct AgencyDomains; it requires discovery, cross-authentication, and semantic resolution. Open spec at v1.0.

### Botlet

**Self-evolving automation unit.** Traditional (non-LLM) code generated by an agent. **Muscle memory.**

#### Canonical 95/4/1 cycle

95% normal execution, 4% detected change, 1% regeneration.

**Fallback guarantee (MUST)**: if the Botlet fails catastrophically, the cognition executes manually.

**Botler** — generic runtime (without understanding the domain) that executes the layer's units: Botlets and Agentlets. **1 Process = 1 Botler + N units**.

#### Botlet maturity — junior, learning, senior

The `95/4/1` cycle describes the steady state; Botlets transit through phases with distinct proportions:

| Phase | Typical proportion | Behavior |
|---|---|---|
| **Junior** | `60 / 35 / 5` | Just generated. Knows the environment only in the version observed at creation. Depends heavily on cognition. |
| **Learning** | `85 / 12 / 3` | Has gone through its first invocations, was regenerated several times, incorporated variants. Operates with intermittent network. |
| **Senior** | `99+ / <1 / ~0` | Incorporated the environment's variants. **Its only failure modes are exogenous** (power, hardware, catastrophic network) — not pending learning. **Reliably operable offline**. |

**Three implications**:
1. Reliable offline operation is a property of **senior** Botlets, not Botlets in general.
2. The **agentic fallback guarantee is what produces maturity**. Each Botlet failure activates the cognition; each activation regenerates incorporating the variant. **Without agentic fallback, the Botlet does not mature.**
3. Maturity is **traceable** in the append-only log.

#### Seed Botlets vs emergent Botlets

Two canonical origins of the Botlet:

- **Seed Botlet** — generated by the cognition at the **design team's** request, as part of the initial product. The decision to exist is the design's, not Pattern Recognition's. **Persistent GUIs generated as facade Botlets** are seed facade Botlets — Layer 3 Botlets whose stable surface lives in Layer 1.
- **Emergent Botlet** — generated by **Pattern Recognition** during operation, when the cognition detects an unanticipated repetitive pattern.

Both live and operate identically once generated. The difference is in the origin. A productive agentive system **does not need to wait for Pattern Recognition** to discover critical Botlets — the seeds are generated at the start per the product spec.

#### proto-Botlet — the pre-forged piece

A **proto-Botlet** is a pre-forged piece of operational capability that the agent, in its **Engineering** time, **configures** to instantiate a Botlet specific to the case. The proto-Botlet contains the code; the Botlet is the configured instance. A generic → instance relation: the proto-Botlet lives in a catalog and serves many cases. It is added to the cast of canonical primitives.

**Two classes**:

| Class | What is its code? | How is it configured? |
|---|---|---|
| **Tempered** | Code specific to its function (e.g., `account-charge`, `esc-pos-printer-command`) | Bounded parameterization |
| **Platform** | Generic code (an engine) whose specialization lives in compositional configuration (e.g., `Mira`) | Compositional configuration; covers N functions of the domain |

Different implementations maintain **proto-Botlet catalogs** — public at AgencyDomains.org, private in proprietary codices. The degree to which the agent configures, co-writes, or generates the code defines the **Botlet generations** (§11).

#### Derivation chain

```
Documented use cases
     │ each case requires
     ▼
Required Botlets  (zero, one, or several; some the cognition resolves without a Botlet)
     │ each Botlet is an instance of
     ▼
Required proto-Botlets from the catalog
```

Required structural property: every conformant Botlet **MUST** be traceable along this chain; the append-only log **MUST** record the origin proto-Botlet of each instantiated Botlet. The *method* of Discovery does not rise to the canon; only the structural relation and its traceability.

**Common catalog and network effects**: proto-Botlets accumulate in catalogs shared by communities of implementers; each consumer contributes to maturation (variants, tested configurations, refinements); implementer n+1 receives versions refined by implementers 1..n. Four membership modes: **private contract** · **proprietary codex** · **open public catalog** (AgencyDomains.org) · **sovereign agreement**.

#### Manifestation and temporality

**Manifestation** — the actualization of the Botlet's latent disposition in the world, perceptible or not (potency → act). **It is NOT "appearance"**: a Botlet that fires a periodic ingestion manifests even if it leaves no visible artifact. It is the abstract genus; each family specializes it: **information** → leaves an **Information Product (`PI`)**; **action** → an effect on the world; **decision** → per its practice. The `PI` is **not a canon primitive** — it lives in the practice of information, one level more concrete.

**Temporality** — the regime of the manifestation. A declared attribute, two values:

| Temporality | How does it manifest? | Runtime |
|---|---|---|
| **`discrete`** | In pulses: wakes on schedule/trigger/event, acts, rests | The Botler invokes or schedules; the Botlet does not live between pulses |
| **`continuous`** | Sustained: lives persistently | The Botler sustains execution while the Botlet lives |

`temporality: continuous` ⟺ persistent Layer 3 life (MUST: a persistent runtime that sustains it). **"Real time" is not chosen on a delivery channel** (`push`); it is chosen by giving the Botlet **continuous temporality**, which mandates the persistent runtime. It connects with *Online enterprise ≠ Real-time enterprise*: points on the temporality continuum. A report (snapshot) and a live dashboard are the **same manifestation under different temporality** → a single runtime (one builds the continuous case; the simple ones are degenerate configurations).

#### Source code vs spec · two surfaces · one Botlet per `PI`

**Source code** (below) = the implementation; for a platform proto-Botlet = the **engine**, shared by all its Botlets. **Spec** (above) = specializes the behavior to the instance; it is not the code, it configures it.

| Surface | What does it manage? | Granularity | Cadence |
|---|---|---|---|
| **Source code lifecycle** | Install/version/load/unload the engine | Botler-level | Releases (Product) |
| **Operation** (includes configuring the spec) | Specialize/manifest/consume/control each Botlet | Per-Botlet | Fluid (Instance) |

**Configuring the spec is operating**: for a platform Botlet the spec is the operational input. The agent evolves the spec **by operating** (verb `specialize`); **crystallization** into a versioned registry **follows, it does not precede**; provenance is given by the append-log. **Verbs of the operation API**: `specialize` · `invoke`/`schedule` (discrete) · `read`/`subscribe` (continuous) · `status`/`activate`/`deactivate`/`retire`.

**One Botlet per `PI`** over a shared engine: each Information Product is its own Botlet/service — with its own `identity`, temporality, maturity, and fallback —, specialized from the shared engine (platform proto-Botlet). Not one Botlet with N configs; not N programs. It is `1 Process = 1 Botler + N Botlets` with the Botlets as specialized instances of the same proto-Botlet. **RISC** rationale: many simple, focused Botlets compose better than a monolith. The `subscribe` consumption is the bridge to the **agentive north** — today a human consumes it (`SSE` in the browser), tomorrow the Cognition.

### Agentlet · eighth canonical primitive

**Packaged unit of Layer 3, sibling of the Botlet, whose execution body invokes bounded inference** — a model sized to the task, within a charter declared in the spec. The canonical home of the task **recurrent in form but interpretive in every instance** (classify, triage, summarize, extract, judge): stable pattern, fresh judgment on every execution, with no possible convergence to determinism. An instance of a **proto-Agentlet** (same tempered · platform classes); hosted by the Botler; engendered and maintained by the agent.

> *The Botlet is muscle memory. The Agentlet is packaged routine judgment. Cognition is reserved for the genuinely new.*

**The "unit" genus**: the Botler hosts **units** — Botlets and Agentlets, its two species. The shared apparatus is predicated of the genus (proto-/instance, catalogs and network effects, spec vs source code, manifestation, temporality, declarative quality contract, derivation chain, append-only log, operation verbs); the differential guarantees, of each species. Canonical relation: **1 Process = 1 Botler + N units**.

**Agentlet vs Botlet** (the differential; everything else is identical by genus):

| Axis | **Botlet** | **Agentlet** |
|---|---|---|
| Body | Non-LLM code; zero inference | Bounded inference via the Botler's handle |
| Natural task | Recurrent, **crystallizable** into code | Recurrent in form, **interpretive** in every instance |
| Determinism | Converges with maturity | Does not converge — statistical correctness by nature |
| Marginal cost | ~0 | Tokens per execution, budgeted in the spec |
| Maturity | Junior → senior (exogenous-only failures) | Spec stabilization + decreasing escalation rate |
| Offline | Senior operable offline | Only with an edge-resident model, **declared** (MUST) |
| Fallback | Cognition executes manually | Escalates to **full Cognition** |

**Smuggling rule (bidirectional, MUST)**: if there is inference in the body, it is an Agentlet — a Botlet with a hidden `llm_call` is non-conformant. If there is none, it is a Botlet — an Agentlet resolvable with deterministic code is **crystallized** into a Botlet. The mature system migrates work down the ladder: Cognition → Agentlets → Botlets.

**Agentlet vs Agent — agenda vs charter**: the **Agent** umbrella covers three members — Assistant · Autonomous Agent · **Agentlet**. **The Agent has an agenda; the Agentlet has a charter**: its inference is spent on *how* to do its own work, never on deciding *what* its work is. Border test (any "yes" on the autonomy side → it is an Agent, not an Agentlet): (1) does it choose its own goals or receive them declared in the spec? (2) can it alter its process or engender other units? (3) is its identity that of an inhabitant (provisioning) or an instance (`specialize`)?

| Axis | **Autonomous Agent** | **Agentlet** |
|---|---|---|
| Nature | **Inhabitant** of the AgencyDomain | **Catalog piece** (instance of a proto) |
| Born through | Provisioning (six phases) | `specialize` over a proto-Agentlet |
| Agenda | Pursues goals; decides what to do | Fixed charter declared in the spec |
| Cognition | Full (bindings, complete tree, multi-LLM) | Bounded (sized model, the spec's Capabilities) |
| Engenders | Generates and regenerates Botlets and Agentlets | Engenders nothing; it is maintained |
| Fallback | *Is* the fallback (above it, only the human) | Escalates to Cognition via the Botler |
| Governance | Exercises the five pillars (MUST) | Control points of the Botler's handle |

**The Botler as sole guardian (MUST)**: the Agentlet brings no runtime of its own. The controlled handle gains a third control point — **`cognition_call`** — alongside `capability_call` and `log`: the body's only path to a model. All of its inference is thus metered, budgeted, **validated** (Pillar 3 gains a seat in Layer 3) and audited in the same append-only log. Segregation by resource profile is a deployment role (pools), never a parallel runtime per species. The two relations cover both species equally: the **agent** engenders and maintains (parent); the **Botler** hosts and executes (butler).

**Three-rung economics**: Botlet (zero inference, ~0 cost) · Agentlet (bounded inference, budgetable per unit) · Cognition (full, for the new). The Autonomy Path remains the cheap one, but stops being uniformly free: the mix is declared per unit. Under fixed Subscription, Agentlets consume quota — bounded and visible in the log —; their share of the mix is an explicit economic decision.

**Required properties**: declared charter — task, inputs, outputs, limits (MUST) · declared bounded inference — model, Capabilities, budget (MUST) · all inference via `cognition_call` (MUST) · fallback to full Cognition (MUST) · zero inference outside the handle (MUST) · hosting by the generic Botler, no parallel runtime (MUST) · traceability of every execution and inference call in the log (MUST) · traceable in the derivation chain with the proto-Agentlet recorded (MUST) · declared locality of the bounded cognition and offline behavior (MUST) · Pillar 3 Validation at the control point (MUST) · Agentlet vs Autonomous Agent distinction in API and documentation (MUST) · maturity metrics of its own (SHOULD) · crystallization into Botlets (SHOULD) · pool segregated by resource profile (MAY).

### Capability

**Unit of specialized cognitive know-how**, modular and composable. Organized in a hierarchical tree. **Reserved in the strict sense to Layer 2 · Cognition.**

**NOT a plugin. NOT a prompt. NOT a system prompt. NOT a tool. It is knowledge.** The Capability **decides which tool to invoke**. Analogous terms in other layers: **Connector** (knowing how to access source systems · Layer 4), **Template** (tailoring of a canonical instrument · Layer 1), **feature** (internal operation of a larger Capability). **Capability portability (MUST)**: it runs on any conformant AgencyDomain; it is real property of the client.

**Four rules of the tree**: any node is a valid Capability · it is scalable (new branches without breaking existing ones) · it is heritable (inherits context and vocabulary from ancestors) · composable.

**Canonical anatomy — nine components**: (1) **identity** (name + position in the tree) · (2) **vocabulary** · (3) **procedural knowledge** · (4) **declarative knowledge** · (5) **heuristics** · (6) **associated tools** (Layer 4) · (7) **parent Capabilities** (inheritance) · (8) **maturity state** (`Draft` / `Current` / `Deprecated`) · (9) **version**. Components 2–5 (vocabulary · procedural · declarative · heuristics) are the body of know-how that distinguishes a Capability from an elaborate prompt.

**Conformance (MUST/SHOULD/MAY)**: hierarchical tree structure (MUST) · any node is a valid Capability (MUST) · composability (MUST) · anatomy with vocabulary + procedural + declarative + heuristics (MUST) · explicit versioning (MUST) · **declared maturity state `Draft`/`Current`/`Deprecated` (MUST)** · selection by the cognition, not direct execution (MUST) · declaration of locality and offline availability (MUST) · portability across conformant AgencyDomains (MUST) · **verticals as a dedicated root (SHOULD)** · open marketplace (MAY).

#### Locality and availability — operational classification of Connectors

The classification is predicated on the **Connector** (access is what resides and needs a network; knowledge has no locality). Every conformant Connector MUST declare its position on two orthogonal axes:

**Locality axis**:
- **Cloud-resident** — lives in a remote service (DTE-SII, Transbank, weather API).
- **Edge-resident** — lives at the physical site, associated with hardware (ESC/POS-Printer, Cash-Drawer, Local-Pinpad).
- **Hybrid** — local component + cloud component (Client-DTE, Client-Pinpad-Deferred-Processing).

**Offline availability axis**:
- **Online-only** — requires network to execute.
- **Offline-capable** — executes without network; queues if it emits outward.

**Canonical matrix**:

|   | Online-only | Offline-capable |
|---|---|---|
| **Cloud-resident** | DTE-SII (no local client) · Transbank Onepay | (typically migrates to hybrid) |
| **Edge-resident** | (unusual combination) | ESC/POS-Printer · Cash-Drawer · Sensor |
| **Hybrid** | (unusual combination) | Client-DTE · Client-Pinpad |

Operational rule with distributed Layer 3: **a senior edge Botlet, without network, operates by invoking exclusively edge-resident Connectors and the local part of hybrid ones**.

**Required properties (locality/availability)**:
- Explicit declaration of the Connector's locality — cloud-resident / edge-resident / hybrid (MUST).
- Explicit declaration of offline availability — online-only / offline-capable (MUST).
- Specification of offline behavior for offline-capable — what it does without network, what it queues, how it drains (MUST).
- Deterministic resolution of which component runs in hybrids — under what conditions the local runs; under which it invokes the cloud (MUST).

#### Regulatory certification resides in the certified component, not the Botlet

For regulated operations (DTE-SII, PCI-DSS, sanitary registry, etc.), **regulatory certification resides in the certified component the Botlet invokes — the certified Connector, accompanied by the regulated Capability that carries the normative knowledge —, not in the Botlet**. The separation is justified because the Botlet is **generated, regenerable code**; certifying it a priori is impossible and certifying it between regenerations contradicts its nature.

**Canonical pattern**: the **Botlet orchestrates** (knows the flow, validates pre-conditions, captures the event, formats the request) and the **certified Connector executes the regulated operation** (receives the request, executes under norm, returns the receipt); the **regulated Capability** supplies the normative knowledge with which cognition governs the pair. Uniform by industry: `Charge-Table`→`DTE`, `Process-Payment`→`PCI-DSS-Gateway`, `Dispense-Prescription`→`Sanitary-Registry`, etc.

**Required properties (regulated)**:
- Regulated components declare their regulatory regime — which norm, before which regulator, with what certification number (MUST).
- Certified Connectors immutable between audits; they change only under a regulatory process (MUST).
- Botlets may invoke certified components without restriction — the contract is stable; they are invoked like any other (MUST).
- Auditability of the boundary — the log distinguishes Botlet operations (business logic) from certified-component operations (regulated operation) (MUST).

### Assistant vs Autonomous Agent

A critical distinction that cuts across Layer 2 and Layer 3. **It is not hierarchical**.

| Axis | **Assistant** | **Autonomous Agent** |
|---|---|---|
| Layer | Layer 2 (Cognition) | Layer 3 (Autonomy) |
| Mode | Reactive | Proactive |
| Activation | Waits for the human's input | Pursues objectives without continuous input |
| State | No persistent state | Persistent state |
| Botlets | No own Botlets | Maintains and regenerates Botlets |
| Life | Per session | Persistent in the background |

**They are governed differently**: the Assistant operates under the human's immediate control (conversational validation, light governance); the Autonomous Agent operates without immediate supervision (systemic validation). **The Autonomous Agent exercises the five pillars of Trust Infrastructure (MUST)** — robust governance, not just access controls.

The **Agent** umbrella covers a third member beyond these two modes: the **Agentlet** (packaged agent of bounded charter; a catalog piece, not an inhabitant — see its section above). The modes describe how the full agent operates; the Agentlet is a piece the full agent engenders and maintains.

### Facet · sixth canonical primitive

Atomic reusable component of **Layer 1 (Interaction)**: drawing board, catalog-picker, color matrix, calendar, clickable map, slider, drag-and-drop, dynamic form, creative canvas. One of the many faces interaction can take.

**Facet vs Botlet — ontological distinction**:

| Axis | **Facet** | **Botlet** |
|---|---|---|
| Layer | Layer 1 (Interaction) | Layer 3 (Autonomy) |
| Nature | Instrument of interaction | The agent's muscle memory |
| When it operates | During active conversation | In the background, without cognition present |
| Activation | The cognition invokes it explicitly | Pattern Recognition or external call |
| Fallback guarantee | NO — the agent returns to conversation | YES — the cognition executes manually |
| Cycle | No regeneration | `95/4/1` cycle with regeneration |
| Persistence | Ephemeral (lives as long as the task lasts) | Persistent between sessions |
| Maturity | Not applicable | Junior · learning · senior |
| Reuse | Flat catalog of instruments | Catalog by capability and domain |

> *The Botlet is muscle memory. The Facet is an instrument the agent picks up while it thinks.*

**Two canonical uses**:
1. **Direct invocation by the cognition** — during conversation, the agent composes an ephemeral surface with Facets; the user interacts; information returns. It realizes the *GUI on-the-fly* regime.
2. **Composition in presentation Botlets** — shells and views (Layer 1 Botlets) assemble Facets plus orchestration logic.

**Declared bounded interaction (embedded Facet)**: a piece of already-materialized information can carry interaction over its own data without ceasing to be reproducible. The canon distinguishes two interactivities:

| What distinguishes them? | **Free exploration** | **Declared bounded interaction** |
|---|---|---|
| Query to the source | yes, arbitrary (ad-hoc drill/pivot) | no — operates on the already-materialized snapshot |
| Space | open | declared (bounded dimensions and values) |
| Reproducibility | lost | maintained |
| Generation | exceeds `G1` | `G1` (configuration, not code) |
| Where it lives | another Botlet / cognition | in the piece itself, via Facet |

**Free exploration** stays **OUTSIDE** the information proto-Botlet (a conformant Botlet **MUST NOT** absorb it). **Declared bounded interaction** is realized via an **embedded Facet** bounded to a declared dimension of the piece's own data: on activation, the *data-bound* elements (KPIs as declared aggregations — `sum`, `ratio` —, distributions, traffic lights) are **recomputed client-side** over the filtered subset, **without new Capability invocations**. It refines (does not contradict) the Facet vs Botlet distinction: the Facet stays ephemeral and without fallback, but its role as an embedded Facet within a piece is recognized.

**Agentive behavior**: the agent **estimates in real time** whether the information is best obtained verbally or visually. Heuristics:
- Low dimensionality + well structured → conversation.
- High dimensionality or hard to verbalize (color, position, shape) → Facet.
- The user already has it in visual form → Facet.
- Comparison among multiple options → Facet.
- Open creative work → canvas Facet.

**Anti-heuristics**: closed and verbal question · channel without graphical capability (voice, IVR, SMS) · the cost of loading a Facet exceeds the benefit · it interrupts the conversational flow.

**Anatomy of the Facet** — six canonical components:
1. Identity (canonical name + version).
2. Interaction modality (input/output).
3. Input schema.
4. Output schema.
5. Internal state (selections, edits, undo stack).
6. Channel compatibility (web, mobile, kiosk, unsupported on voice).

**Flat catalog**: Facets are not hierarchized; each is atomic. Emergent catalog: `drawing-board`, `catalog-picker`, `color-matrix`, `range-calendar`, `clickable-map`, `multi-slider`, `dragdrop-order`, `dynamic-form`, `creative-canvas`, `file-picker`. The spec does not close the catalog.

**Required properties**:
- Declared identity and version (MUST).
- Explicit input and output schemas (MUST).
- Declared channel compatibility (MUST).
- Atomicity — it does not internally compose other Facets (MUST).
- Explicit Facet vs Botlet distinction in documentation (MUST).
- Direct invocability by the cognition during conversation (MUST).
- Composability within shell and view Botlets (MUST).
- Preservation of the piece's reproducibility when composed as an embedded Facet — client-side recompute, no Capability invocations (MUST).
- Declared bounded interaction composed in a materialized piece — declared control space, no new queries (MAY).
- Public catalog of Facets available to the AgencyDomain (SHOULD).
- Documented invocation heuristics for the cognition (SHOULD).

### The agent's three evolutionary phases

1. **Specialized** — one agent per domain. The market's current phase (early 2026).
2. **Orchestrators** — one agent coordinates multiple specialists.
3. **Multi-specialists** — deep multi-domain expertise in a single agent. A future phase.

**The architecture is the same in all three phases.**

---

## 8 · The market — AI value chain

A two-dimensional model: **eleven sequential links × four depths**.

### Eleven links (coverage)

1. **Data** · 2. **Model** · 3. **Access** · 4. **Agents** · 5. **Specializations** · 6. **Runtime** · 7. **Firewall** · 8. **Observability** · 9. **Tools** · 10. **Integrations** · 11. **Environment**

### Four depths

- **Wrapper** — consumes via third-party APIs/SDKs.
- **Platform** — operates its own capability over Core components.
- **Core** — builds the foundational capability with its own technology.
- **Infrastructure** — provides the substrate.

### Canonical matrix

| Link | 4 · Infrastructure | 3 · Core | 2 · Platform | 1 · Wrapper |
|---|---|---|---|---|
| **1 · Data** | AWS/GCP/Azure | Scale AI/Labelbox · Hugging Face | — | — |
| **2 · Model** | NVIDIA · AWS/GCP/Azure | OpenAI · Anthropic · Google · Meta · DeepSeek/Qwen/Ernie | Hugging Face | — |
| **3 · Access** | — | Anthropic · DeepSeek/Qwen/Ernie | OpenAI · Google · Perplexity · ultraPRO | — |
| **4 · Agents** | — | Perplexity · DeepSeek/Qwen/Ernie · Agentia (priv.) · Soveria (pub.) · (LangChain/Graph) · (AutoGPT/CrewAI) | OpenAI · Anthropic · Google · GitHub Copilot | — |
| **5 · Specializations** | — | Perplexity · GitHub Copilot · Cursor/Replit · Devin · Harvey/Jasper/Fin · umeeta | OpenAI | — |
| **6 · Runtime** | — | OpenAI · Devin · Agentia · Soveria · ultraPRO · (LangChain/Graph) · (AutoGPT/CrewAI) | — | — |
| **7 · Firewall** | — | Guardrails/NeMo/Lakera · ultraPRO | — | — |
| **8 · Observability** | — | Langfuse/LangSmith/W&B · ultraPRO | — | — |
| **9 · Tools** | — | OpenAI · Anthropic · Google · Devin · ultraPRO · (LangChain/Graph) · (Pinecone/Weaviate) | — | — |
| **10 · Integrations** | — | Zapier/Make/n8n · ultraPRO | — | — |

Derived from the actor table of Chapter 6 (representative product families of the current market). Parentheses — e.g. (LangChain/Graph) — indicate a framework or meta-tool (to build with, not to use).

> ultraPRO occupies the architectural category **complete enterprise gateway** — simultaneous Core in links 6-10 plus a Platform extension in Access, under the tripartite Cloud + Client + Local pattern.

> **Link 11 · Environment**: it stays outside the matrix — it is the territory on which links 1-10 act (the enterprise systems the agent turns into invisible backend), not a link an AI actor occupies at some depth.

### Four strategic archetypes

- **Comprehensive platform** — broad coverage (3+ links); Core in its native link, Platform in the adjacent ones.
- **Vertical specialist** — focal coverage, Core depth.
- **Domain infrastructure** — zonal coverage, Core depth in several links.
- **Substrate provider** — minimal coverage, Infrastructure depth.

### Observability (link 8) · six canonical capabilities

A complete implementation of Observability for agentive systems covers six distinct capabilities:

1. **Tracing** — end-to-end traceability of each operation (structured events correlated by trace ID).
2. **Cost monitoring** — token/resource consumption in real time per model/user/project/tool; in mature systems it is prediction, not just recording.
3. **Quality evaluation** — systematic verification of responses; two sub-modes: automated (eval as a service) and human (sample review).
4. **Performance metrics** — latency (p50/p95/p99), throughput, availability, success rate (distinguished by Botlet/agent/system).
5. **Debugging and reproducibility** — replay of invocations; complexity added by the probabilistic LLM, persistent state, and Botlet regeneration.
6. **Alerts and anomalies** — proactive out-of-pattern detection; may trigger circuit breakers, rollback, or escalation.

> A market fragmented by design: a mature organization combines two or three products (an "observability stack"), not a monolithic solution.

### Carbon World · MEO

- **Carbon World** — link 11 extended to the physical world (IoT, industrial processes). Patterns: edge computing, digital twin.
- **Four sub-categories of the Environment** (decreasing maturity, increasing regulation):
  1. **Traditional enterprise systems** — legacy ERPs/CRMs/DBMS; digital but institutional; the most mature (integration: Zapier · Make · Workato · MuleSoft, still mostly agentic, not autonomous).
  2. **Industrial physical world** — manufacturing and energy (SCADA · MES · PLCs · sensors); higher capturable value and more conservative (plant-safety regulation).
  3. **Mobile physical world** — transport, logistics, agriculture (fleets, drones, agricultural equipment); adds intermittent connectivity and geographic coordination; faster adoption.
  4. **Biological world** — genomics, medical monitoring, EHR, pharmacovigilance; greatest human impact and maximum Trust demand (HIPAA · health GDPR).
- **MEO — Model Engine Optimization** — practices for getting frontier models to reference the actor. The equivalent of SEO in agentive discovery.

---

## 9 · Canonical application — Real-time knowledge

```
┌──────────────────────────────────────────────────────────────────┐
│      VARNISHED KIMBALL = CLASSIC KIMBALL + AGENTIVE LAYER         │
│                                                                  │
│    SOURCE → ETL → PRESENTATION → BI APPS → AGENT → HUMAN          │
│                                                                  │
│    ─────────────────────────────────────────────────────────     │
│    METADATA + SEMANTIC LAYER + TRUST SCORE + AI CERTIFICATION    │
│         (cross-cutting — strategic asset)                        │
└──────────────────────────────────────────────────────────────────┘
```

**Essential components** that distinguish Varnished Kimball from classic Kimball:

- **Explicit semantic layer**.
- **Trust Score per datum**.
- **AI Certification**.
- **Observability of agentive queries**.

**Mapping to the hyperscalers** — each implements base Kimball with its own terminology; the functional equivalence is direct:

| Provider | Warehouse / ETL | BI App | Governance | Unifying layer |
|---|---|---|---|---|
| **Azure** | Synapse Analytics | Power BI | Purview | Fabric |
| **AWS** | Redshift | QuickSight | DataZone | Lake Formation |
| **Google Cloud** | BigQuery | Looker | Dataplex | — |
| **Databricks** | Lakehouse + Medallion | — | Unity Catalog | — |

Medallion → Kimball: **Bronze** = Source (raw) · **Silver** = ETL (clean/conformed) · **Gold** = Presentation. No hyperscaler yet has a complete implementation of the **agentive layer** of Varnished Kimball.

---

## 10 · Operation

### CRUDLEX

Canonical model of granular permissions: **C**reate, **R**ead, **U**pdate, **D**elete, **L**ist, **E**xecute. Applicable per user, agent, and context.

**Preconfigured levels** (level → enabled CRUDLEX):

| Level | CRUDLEX enabled |
|---|---|
| **FULL** | `C R U D L E` |
| **READ-WRITE** | `C R U D L` (no E) |
| **READONLY** | `R L` |
| **SAFE** | `R L E` (E limited to reversible operations) |
| **NO-SEND** | `C R U L` (no E) |
| **NO-DELETE** | `C R U L E` (no D) |

### Policy catalog — five categories

A well-designed agentive system has active policies in **all five**:

1. **Tool policies** — which tools the agent may invoke, over which resources (granularity by agent, tool, and scope).
2. **Data policies** — which classes of data it may query or emit, by sensitivity.
3. **Schedule and threshold policies** — when and with what magnitude/risk thresholds it acts.
4. **Identity policies** — which identities operate on behalf of the agent and how they authenticate (federated identity).
5. **Validation policies** — which validations apply before executing (they connect with Pillar 3).

**Hierarchical composition with downward monotonicity** (MUST): the agent's policy inherits the restrictions of the higher ones and may only **add** restrictions, never remove them. It prevents accidental privilege escalations.

### Append-only log

An immutable, cryptographically chained record of every action. A central component of Audit.

**Minimum content of each trace**: the agent's identity, invoked capability, executed tool, **hash of parameters and result** (not the raw content — sensitive data lives in a separate store with its own retention policy), timestamp, context, and `previous_log_hash` that chains with the prior record. Non-negotiable property: the log keeps **hashes, not content**.

### Human approval

Halts an operation and requests authorization before executing. Triggered by: **explicit policy**, **threshold**, **agent uncertainty**.

### Canonical validation (Pillar 3)

- Hallucination detection · validation of structured responses · prompt injection prevention · DLP · tokenization.

### Operational business continuity vs agentic fallback guarantee

Two complementary mechanisms:

| Mechanism | When it operates | What it resolves | Provided by |
|---|---|---|---|
| **Agentic fallback guarantee** | Junior, learning, or senior Botlet with a new variant (cognition available) | Environment changes the Botlet did not anticipate | Agentive spec (Layer 2 + Layer 3) |
| **Operational business continuity** | Senior Botlet down by exogenous cause, no cognition available | Continuity when no computational component operates | Client's protocol |

The agentic fallback guarantee **produces the Botlet's maturity** (without it, it does not mature); operational continuity operates over senior Botlets down by exogenous cause and does not bear on maturity. Recognizing them as separate prevents the client from attributing to the architecture a failure that belongs to their protocol.

### AgencyDomain degradation modes

Four canonical modes according to the failure scenario. The organization must be able to identify at every moment which mode each site operates in.

| Mode | Condition | Who sustains operation |
|---|---|---|
| **Normal** | All components active | Full parallel topology |
| **Cognition down** | Layer 2 unreachable, edge OK | **Autonomy Path** sustains; cognition will rescue on return |
| **Edge offline** | Edge Botler without connection to central; isolated site | **Senior Botlets** against local DB + edge-resident Connectors |
| **Total operational continuity** | Cognition + edge down by exogenous cause | **Site's manual protocol** |

**Automatic transition up to `Edge offline`** — the architecture degrades on its own. **Transition to `Total operational continuity` is governed by the site's protocol** — a human activates it explicitly. Key difference: the first three modes are the architecture's responsibility; the fourth is the client's responsibility.

### Transition traceability — canonical log tags

- `mode-change: continuity-operational` — when the site activates the manual protocol.
- `provenance: manual-continuity` + `original-timestamp` — physical records entered retroactively.
- `provenance: edge-queue-replay` — drainage of the edge queue after the network returns.
- `agentic-fallback` vs `operational-continuity` — auditable distinction between cognition rescuing and human sustaining.

### Required properties (Resilience Pillar + Continuity)

| Property | Level |
|---|---|
| Explicit distinction in product documentation | MUST |
| Operational continuity protocol documented per site | MUST |
| Drills at minimum quarterly frequency | SHOULD |
| Four degradation modes recognizable by the organization | MUST |
| Traceability of the transition to continuity mode in the append-only log | MUST |
| Auditable distinction between agentic fallback and operational continuity | MUST |
| Retroactive reconciliation of physical records into the system | MUST |

---

## 11 · Evolution frontier

Three live **technical** horizons:

1. **Non-LLM cognition** — Layer 2 admits symbolic, hybrid, multimodal cognition.
2. **Federation (`A2A` between AgencyDomains)** — open protocols in evolution. Intra-AgencyDomain coordination (via the `A2A` protocol) is already mature; `A2A` *between* distinct AgencyDomains is open work.
3. **Carbon World** — extension of Layer 4 to the physical world.

The human book counts **four live frontiers**: these three technical horizons plus a **fourth institutional frontier** — agentive sovereignty and citizenship (**AgentNation**, below).

### Botlet generations — G1/G2/G3

An evolutionary model of how the Botlet's code is born as the state of the art of cognition advances. **The architecture is the same in all three**; what changes is the **scope of Engineering**. An implementation can operate in `G1` today and migrate toward `G3` without re-architecture.

- **G1** — the agent configures pre-forged proto-Botlets from the catalog (it does not write the body). If none fits, it specifies a new one to forge in the next Preparation.
- **G2** — the agent co-writes proto-Botlets with human or model assistance.
- **G3** — the agent generates the Botlet's complete code at Engineering time (the asymptotic scenario).

**G1 admits rich expressive configuration**: what defines `G1` is that the agent does not write the proto-Botlet's body; the configuration may be as rich as a compositional `DSL` with evaluable formal expressions. The `G1`/`G3` distinction is about **authorship of the body**, not expressiveness of the config.

**`G1`/`G2` edge** (test: *"does the code belong to the invoked Capability or to the proto-Botlet itself?"*): a formal evaluable expression that is a **parameter of a well-defined Capability** (`SQL`→`execute-sql`, a chart specification→`render-chart`, filter→`filter-stream`) is configuration → **`G1`**. An expression that **extends/overrides the proto-Botlet's internal logic** (callbacks, lambdas it evaluates internally) is the agent's code → **`G2`**.

**Reconciliation — two distinct axes, not the same arrow**:

| Axis | What does it measure? | Direction of "advance" |
|---|---|---|
| **Authoring capacity** | How much it can forge: configure (`G1`) → co-write (`G2`) → generate (`G3`) | Toward `G3`, with the state of the art of cognition |
| **Operational maturity** | For a recurring operation, how much pre-forged is reused vs regenerated (`95/4/1` cycle) | Toward reuse (`G1`), as the Botlet matures junior → senior |

`G3` capacity **is better spent producing `G1` reuse**: the destiny of `G3` is a richer `G1` catalog, not the live regeneration of everything. For a **platform** proto-Botlet, `G1` is **terminal by design**, not a way station. The most advanced agent **generates less because it has crystallized more**, and reserves generation for the edge (the 4%+1% of the cycle). Brain parallel: cortex = Cognition (Layer 2); cerebellum + basal ganglia = Autonomy (Layer 3). Sophistication is **stratifying so that the cognition does not have to do everything**.

### AgentNation

A public-regime AgencyDomain that adopts the model of agentive citizenship. The agents are **citizens**, not products. Ontological distinction: a marketplace lists products; AgentNation recognizes citizens. Open architectural work.

---

## 12 · Canonical glossary (alphabetical)

### A

- **A2A — Agent-to-Agent** — a name reserved for the **relation between distinct AgencyDomains** (distinct agents; federation). Communication within a single AgencyDomain **is not "internal A2A"**: it is **intra-AgencyDomain coordination**, and when it uses that transport one says **via the `A2A` protocol**. The Layer 2 → Layer 3 interface goes over `MCP`, not `A2A`.
- **Account** — a commercial concept; it may own multiple AgencyDomains.
- **AgencyDomain** — computational scope with its own identity where autonomous agents and Botlets dwell, **where the Capabilities are hosted and run**, and where the resources that sustain them live. Minimal unit of deployment.
- **AgencyDomain degradation modes** — Normal · Cognition down · Edge offline · Total operational continuity. The first three transitions are automatic; the fourth requires human activation by protocol.
- **AgencyDomain portability** — structural property: a conformant AgencyDomain migratable to another conformant platform without rewriting. Three conditions: Botlets against canonical primitives, exportable DB, portable Trust Layer.
- **Agent** — umbrella term covering three members: the **Assistant** (Layer 2, reactive), the **Autonomous Agent** (Layer 3, proactive, an inhabitant) and the **Agentlet** (Layer 3, packaged, a catalog piece). The distinction is not hierarchical.
- **Agentlet** — **eighth canonical primitive**. Packaged unit of Layer 3, sibling of the Botlet, whose body invokes **bounded inference** within a charter declared in the spec. The home of the task recurrent in form but interpretive in every instance. **The Agent has an agenda; the Agentlet has a charter.** An instance of a proto-Agentlet; hosted by the Botler (`cognition_call`); fallback to full Cognition. The intermediate economic rung between Botlet and Cognition.
- **Agent First** — governing principle: the agent's experience takes precedence over the human's.
- **Agentic** — the world of complementary agents. Incremental evolution.
- **Agentic fallback guarantee** — the cognition executes when the Botlet fails. **The process never stops.** **What produces the Botlet's maturity.**
- **Agentive (Agentive World)** — agents as the sole interface. Fundamental transformation.
- **Agentive Architecture** — technical design that materializes the Agentive World. Four layers (Interaction, Cognition, Autonomy, Access), governed by cross-cutting Trust Infrastructure and ordered by the Agent First principle.
- **AgentNation** — public AgencyDomain with a model of agentive citizenship.
- **AI value chain** — two-dimensional model of 11 links × 4 depths.
- **Append-only log** — immutable, cryptographically chained record.
- **Assistant** — reactive agent, no Botlets, no persistent life. Layer 2.
- **Attention** — one of the **agent's three times**. The time in which the agent interacts with users or events in real time. Layer 1 active, critical path, priority.
- **Audit** — Pillar 2 of Trust Infrastructure. Reconstructing after the fact **what the agent did, when, why, and over what data**. Central mechanism: the append-only log; completed by trace, lineage, and identity tagging.
- **Autonomous Agent** — proactive, persistent life, maintains Botlets. Layer 3.
- **Autonomy Path** — one of the two paths of the parallel topology. Fast, cheap, repetitive. For Botlets over stable patterns.

### B

- **BCA — Bounded Concerns Architecture** — architecture of the pre-agentive state.
- **Botlet** — self-evolving automation unit. Non-LLM code. Muscle memory. `95/4/1` cycle.
- **Botlet, emergent** — generated by Pattern Recognition when it detects an unanticipated repetitive pattern.
- **Botlet, facade** — Layer 3 Botlet that exposes an operational surface with a stable contract in Layer 1, propagated human identity.
- **Botlet, junior** — initial phase. `60/35/5` proportion. Depends on cognition.
- **Botlet, learning** — intermediate maturity phase. `85/12/3` proportion.
- **Botlet, operation** — **Layer 3** Botlet that executes business logic invoked from Layer 1 (views and shells). Most reusable in the catalog. Examples: charge a table, print a kitchen ticket, close a shift.
- **Botlet, seed** — generated by cognition at the design team's request, as part of the initial product.
- **Botlet, senior** — mature phase. `99+/<1/~0` proportion. Only exogenous failures. Offline-operable.
- **Botlet, surface (shell)** — **Layer 1** Botlet acting as a container: layout, navigation, session, shared state. Specific to each product.
- **Botlet, view** — **Layer 1** Botlet that materializes a screen or panel within a shell. Assembles Facets + orchestration logic. Reusable across shells.
- **Botlet generations — G1/G2/G3** — evolutionary model of the birth of the Botlet's code. **G1**: configures pre-forged proto-Botlets (does not write the body). **G2**: co-writes the proto-Botlet. **G3**: generates the complete code (asymptotic). It changes the scope of Engineering, not the architecture. G3 capacity is better spent producing G1 reuse; for a platform proto-Botlet, G1 is terminal by design.
- **Botler** — **generic** Layer 3 runtime (does not understand domain) that executes the **units** of the layer: Botlets and Agentlets. A type (a normed construct of the Botlet spec), not a proper name. No subtypes by domain; validates by orchestrating (controlled handle with `capability_call` · `log` · `cognition_call`); exposes an `MCP` server to the Cognition. **1 Process = 1 Botler + N units**.
- **Botler, central** — orchestration, planning, reporting Botler in distributed Layer 3.
- **Botler, edge** — local-transaction Botler in distributed Layer 3. One per physical site.
- **BYOModel** — Bring Your Own Model. Substitution of the default provider. SHOULD for regulated markets.

### C

- **Capability** — **cognitive** know-how, modular and composable, reserved to **Layer 2 · Cognition**. NOT a plugin, NOT a prompt, NOT a tool. **It is knowledge.** Exposes **features**; is **portable** (runs on any conformant AgencyDomain).
- **Connector, cloud-resident** — lives in a remote service. Typically online-only.
- **Connector, edge-resident** — lives at the physical site, associated with hardware. Typically offline-capable.
- **Connector, hybrid** — local component + cloud component. Offline-capable with queuing.
- **Connector, offline-capable** — executes without network. Queues if it emits outward.
- **Connector, online-only** — requires network.
- **Capability, regulated** — carries the normative knowledge of an operation subject to certification (DTE-SII, PCI-DSS, etc.). Regulatory certification resides in the **certified Connector** that executes the operation, not in the Capability nor in the Botlet.
- **Capability portability** — a conformant Capability runs on any conformant AgencyDomain; it makes it real property of the client. Distinct from AgencyDomain portability.
- **Carbon World** — link 11 extended to the physical world.
- **Cluster** — instances of the same AgencyDomain sharing load.
- **Codex, proprietary** — private catalog of proto-Botlets, Capabilities, and patterns that an implementer curates over the public reference implementation, refined by its real cases. One of the four membership modes of a catalog community. The runtime is common; the codex is one's own (it encapsulates the competitive advantage). Canonical instance: **ucodex** (Grupo Ultra).
- **Cognition Path** — one of the two paths of the parallel topology. Slow, costly, decisive. For conversation, new decisions, unanticipated cases.
- **Common catalog** — proto-Botlets accumulate in shared catalogs with network effects. Modes: private contract · proprietary codex · open public catalog · sovereign agreement.
- **Conformed dimensions** — a Kimball concept: dimensions shared across data marts that guarantee inter-mart consistency.
- **Connector** — knowing how **to access source systems** (a connection with execution power; NOT cognitive knowledge). **Layer 4 · Access.** The legacy API brought into the Agentive World becomes a Connector, not a Capability.
- **CRUDLEX** — Create, Read, Update, Delete, List, Execute.

### D

- **Declarative quality contract** — a Botlet's quality attributes declared as structured properties: Freshness · SLA · Degradation policy · Audience · Refresh policy. Trust Infrastructure audits them uniformly.
- **Declared bounded interaction** — interaction that operates over the **already-materialized snapshot** of a piece, in a **declared** space, that **maintains reproducibility** and is **`G1`** (configuration, not code). Lives in the piece itself via an **embedded Facet** (client-side recompute, no Capability invocations). Distinct from **free exploration** (arbitrary query to the source, exceeds `G1`).
- **Depth** — vertical dimension: Wrapper / Platform / Core / Infrastructure.
- **Derivation chain** — structural relation `use cases → required Botlets → proto-Botlets from the catalog`. Every conformant Botlet MUST be traceable along it; the log records the origin proto-Botlet.
- **Digital twin** — a pattern for the Carbon World.
- **DLP — Data Loss Prevention** — detection of unauthorized PII.
- **Domain** — commercial synonym for AgencyDomain.
- **Dominion** — a Domain obtained by an agent in a public AgencyDomain under the AgentNation model.

### E

- **Edge computing** — distribution of Layer 3 near the physical process.
- **Engineering** — one of the **agent's three times**. Bridge between Preparation and Attention: converts latent capacity into executable capacity for a concrete case. Configures seed Botlets, validates deploy. Medium term (minutes to hours).
- **Enterprise AI gateway** — Core in Runtime+Firewall+Observability+Tools+Integrations.

### F

- **Facet** — **sixth canonical primitive**. Atomic reusable component of Layer 1: drawing board, catalog-picker, calendar, map, slider, drag-and-drop. An instrument the cognition invokes during conversation or that presentation Botlets assemble. **It is NOT a Botlet** (Layer 1 vs Layer 3 · ephemeral vs persistent · without agentic fallback vs with).
- **feature** — an internal operation a Capability exposes (the equivalent of *feature/operation/skill/method*). Capability vs feature test: operational independence + cognitive identity + reusability; if one fails → it is a feature of the containing Capability.
- **Federation** — communication between distinct AgencyDomains.
- **Firewall** — link 7. Security, governance, prompt injection prevention.

### G

- **Governance** — Pillar 1 of Trust Infrastructure.
- **GUI on-the-fly** — Regime 2 of Layer 1. A graphical surface adapted to the task, lives as long as the task lasts.
- **GUI, persistent (as facade Botlet)** — Regime 3 of Layer 1. The stable surface of a facade Botlet (Layer 3, typically seed) for repetitive operational roles.

### H

- **Hallucination** — a factually incorrect statement. Detection in the Validation Pillar.
- **Human approval** — authorization before executing a critical operation.
- **Hybrid (regime)** — AgencyDomain with a private core + partial public exposure.

### I

- **Information Instrument** — the canonical **type** of the information family (the class: report / dashboard). Distinct from the **Information Product**, which is its manifested instance.
- **Information Product (`PI`)** — manifested/delivered instance of the information family (the concrete manifestation of an Information Instrument). Each `PI` is its own Botlet/service specialized from a shared engine (platform proto-Botlet). **It is NOT a canon primitive** — it lives in the practice of information.
- **intra-AgencyDomain coordination** — communication between runtimes (Botlers) of the **same** AgencyDomain. **It is NOT "internal A2A"**: they are runtimes of the same agent, not distinct agents. When it uses that transport one says **via the `A2A` protocol**. Counter-concept of `A2A` (relation between distinct AgencyDomains).

### J

- **JSR — Java Specification Request** — canonical format of Java specifications (Sun Microsystems / Oracle). **JavaSpaces (JSR-000148, 1999)** is the conceptual analog of AgencyDomains.

### K

- **Kimball / Varnished Kimball** — dimensional modeling + agentive layer.

### L

- **Layer 1 — Interaction** — human-AI interface with three GUI regimes.
- **Layer 2 — Cognition** — the agent's brain.
- **Layer 3 — Autonomy** — persistent life. Admits geographic distribution (distributed Layer 3).
- **Layer 3, distributed** — canonical pattern for multiple physical presence. Central Botler + N edge Botlers.
- **Layer 4 — Access** — execution power with Trust Infrastructure.
- **Link** — functional layer of the value chain (1 to 11).
- **LLM** — Large Language Model.

### M

- **manifestation** — actualization of the Botlet's latent disposition in the world, perceptible or not (potency → act). NOT "appearance". Abstract genus: information → leaves a `PI`; action → effect on the world; decision → per its practice.
- **MCP — Model Context Protocol** — open canonical protocol for Layer 4 tools and for the internal Layer 2 → Layer 3 interface (Cognition client, Botler server). Anthropic, November 2024.
- **MEO — Model Engine Optimization** — the equivalent of SEO in agentive discovery.
- **Meta-Cognitive Platform** — a platform category that administers the **economics of cognition** (G1 pre-forged muscle vs fresh-cognition fallback, `95/4/1` cycle, junior→senior maturation, crystallization). **Vergis** is the reference implementation. **NOT abbreviated to "MCP"** (the acronym taken by Model Context Protocol).
- **Mira** — proper name of a **platform** proto-Botlet for informational operation from the reference implementation's catalog.
- **Muscle memory** — the canonical metaphor of the Botlet.
- **Nadella Line** — see N.

### N

- **Nadella Line** — threshold between the Agentic World and the Agentive World. *Does the human open applications to do their work?* (canonical formulation; *The Real-Time Enterprise* conjugates it in the second person and *AURA* in the executive's voice — the three are official equivalents).

### O

- **Observability** — link 8 of the value chain: the layer that **observes, measures, and feeds back** on the AI system in production. Its question: *how does it work?* Without it, agents are black boxes.
- **Online enterprise** — data current to the day, depends on humans to interpret.
- **Operational business continuity** — manual protocols for a senior Botlet down by exogenous cause with cognition unavailable. Distinct from and complementary to agentic fallback.

### P

- **Parallel topology** — canonical model of the four layers. Layers 2 and 3 are **parallel paths** between Layer 1 and Layer 4, not stages in series.
- **Pattern Recognition** — detection of repetitive patterns. Activates emergent Botlet generation.
- **Preparation** — one of the **agent's three times**. *Mise en place* — the agent refines the catalog, improves capabilities, outside the service window. Batch / off-peak regime.
- **Private (regime)** — AgencyDomain in a controlled perimeter. No public access.
- **Prompt injection** — manipulation via malicious inputs.
- **proto-Agentlet** — a pre-forged piece of interpretive capability that the agent **configures** in its Engineering time to instantiate an Agentlet. It contains the body (the charter's structure, the skeleton of the operating prompt, input/output contracts, escalation thresholds); the Agentlet is the configured instance. Same classes (tempered · platform), same derivation chain and same catalogs as the proto-Botlet.
- **proto-Botlet** — **seventh canonical primitive**. A pre-forged piece of operational capability that the agent **configures** in its Engineering time to instantiate a Botlet. The proto-Botlet contains the code; the Botlet is the configured instance. Two classes: **tempered** (specific code; bounded parameterization) · **platform** (generic engine; compositional configuration; covers N functions). Public catalogs (AgencyDomains.org) or private (proprietary codices).
- **Public (regime)** — publicly accessible AgencyDomain.

### Q

- **Quantum Leap** — threshold enabled by the collapse of the cost of the analytical question: when asking the data stops being expensive, slow, or mediated by a human, the organization crosses from **online enterprise** to **real-time enterprise**. A change of operating regime, not an incremental BI improvement.

### R

- **RAG — Retrieval-Augmented Generation**.
- **Real-time enterprise** — detects, interprets, decides, and acts autonomously.
- **Regime** — deployment mode of an AgencyDomain by access boundary. **Technically equivalent structure; the regime changes, not the capability.**
- **Resilience** — Pillar 4 of Trust Infrastructure.
- **Runtime** — link 6. The agent's operating environment. Corresponds to Layer 3.

### S

- **Sandbox** — execution isolation of Botlets. Four strategies: processes+seccomp, containers, WASM, MicroVMs.
- **Semantic layer** — encodes the meaning of dimensions, facts, hierarchies. Essential for Varnished Kimball.
- **Signage** — passive dashboards without requiring interaction.
- **SME — subject-matter expert** — the human expert whose knowledge is transferred to the agent in Capability construction. Opening workshop and ALPHA validation of Wingtraining.
- **Space / WorkSpace** — human habitat. Reserved for humans.
- **Strategic archetype** — pattern of positioning in the coverage × depth space of the value chain. Four canonical: Comprehensive platform (broad coverage; Core in its native link and Platform in the adjacent ones) · Vertical specialist (focal coverage, Core depth) · Domain infrastructure (zonal coverage, Core in several links) · Substrate provider (minimal coverage, Infrastructure depth).

### T

- **Template** — client-specific tailoring over a **canonical instrument** (report/dashboard) in its own format or rule. **Layer 1 · Interaction.** NOT a Capability nor a Connector.
- **temporality** — regime of the Botlet's manifestation. Declared attribute: **`discrete`** (pulses: schedule/trigger/event) and **`continuous`** (persistent life; mandates the persistent Layer 3 runtime). "Real time" is chosen by giving continuous temporality, not by marking a `push` channel.
- **Three times of the agent** — canonical temporal frame: **Preparation** (mise en place, batch / off-peak), **Attention** (critical path, real time), **Engineering** (bridge, medium term). The parallel topology describes WHERE; the three times describe WHEN.
- **Tokenization** — replacement of sensitive data with tokens before cognition.
- **Tool** — an invocable instrument. Link 9. Canonical protocol: MCP. **NOT a Capability.**
- **Trace** — end-to-end traceability.
- **Transparency** — Pillar 5 of Trust Infrastructure. Understanding in real time **what the agent is doing and why**, with enough detail to intervene. It connects the other four pillars.
- **Tripartite pattern Cloud + Client + Local** — canonical deployment pattern of enterprise Trust Infrastructure.
- **Trust Infrastructure** — five pillars: Governance, Audit, Validation, Resilience, Transparency.

### U

- **ucodex** — proper name of the **proprietary codex** of Grupo Ultra: its private catalog of proto-Botlets, Capabilities, and patterns, curated by real cases over the reference implementation (Vergis). An instance that exemplifies the *proprietary codex* mode; same drawer of proper names as Soveria, Agentia, ultraPRO — not a type of the canon.
- **unit (of Layer 3)** — the genus of the packaged pieces the Botler hosts and executes. Two species: **Botlet** (non-LLM code) and **Agentlet** (bounded inference). The shared apparatus is predicated of the genus; the differential guarantees, of each species. Canonical relation: **1 Process = 1 Botler + N units**.

### V

- **Validation** — Pillar 3 of Trust Infrastructure.
- **Vergis** — proper name of the public reference implementation of AgencyDomains (the platform; the AgencyDomain made operational). Category: **Meta-Cognitive Platform**. Distributed **AGPL**, public repo, **AgencyDomains.org**. An instance proper name (like Soveria, Agentia, ultraPRO), not a type like Botler.

### W

- **Wingtraining** — canonical development scheme of a Capability in five steps: workshop with the SME · creation · customization · ALPHA · BETA.
- **Wingworking** — collaborative human-AI practice. The methodological frame under which the book was produced.
- **WorkSpace** — see Space.
- **Wrapper / Platform / Core / Infrastructure** — the four canonical depths.

---

## 13 · Reference implementations

The architecture is **product-agnostic**. It admits multiple cooperating implementations.

**Canonical clarification**: the four layers are an X-ray of the individual agent. **They are not slots where a product is assigned to each.**

**Note on the scope of the canon**: this canon contains the structure and the vocabulary of the Agentive World — definitions, primitives, required properties, canonical separations. **It does not contain methods to implement or operational catalogs**: those live in complementary bodies. The public reference implementation is **AgencyDomains.org**, materialized in **Vergis**.

### Vergis — public reference implementation

**Vergis** is the public reference implementation of AgencyDomains — the AgencyDomain made operational. Distributed under **`AGPL`** (code) and **`GFDL`** (docs), public repository at **AgencyDomains.org**, designed to be downloaded, read, run, and learned from to see how the canon translates into living systems. Its full development is **Chapter 9** of the book.

**Naming scheme — type vs proper name**:

| Layer | Type / category | Proper name |
|---|---|---|
| Platform · *Meta-Cognitive Platform* | reference implementation of AgencyDomains | **Vergis** |
| Layer 3 runtime | **Botler** (normed construct of the Botlet spec, generic) | — (no proper name) |
| Catalog component | platform proto-Botlet for informational operation | **Mira** |

- **Botler** is a **type** (a normed construct of the Botlet spec — not one of the eight primitives). Any conformant Layer 3 runtime *is a* Botler.
- **Vergis** and **Mira** are **proper names** of instances (same drawer as Soveria, Agentia, ultraPRO).
- Vergis's category: **Meta-Cognitive Platform** — it administers the **economics of cognition** (G1 pre-forged muscle vs fresh-cognition fallback, `95/4/1` cycle, junior→senior maturation, crystallization). **NOT abbreviated to "MCP"** — that acronym names the Model Context Protocol. The descriptor is used spelled out.

**What it includes**: the abstract contract of the **Botler** (generic, with control points `capability_call`/`log` and validation by delegation) · **Mira** (a platform proto-Botlet operating in `G1`) · a starter set of **Capabilities** and **Connectors** · Trust Infrastructure templates (policies, append-only log, declarative quality contract) · executable examples that walk the chain `use case → Botlets → proto-Botlets`.

**Production grade**: it is the **same runtime** that operates the commercial products (Agentia · Soveria · ultraPRO). The difference from those products **is not the quality of the code but the catalog**: the products consume the public reference **plus a proprietary codex** (ucodex is one exemplar) that curates proto-Botlets, Capabilities, and patterns refined by real cases.

**Adoption model** (replicable without permission or central contract): (1) **consume** the public reference; (2) **curate** its own codex; (3) **offer** its products on that base. AgencyDomains.org is not the property of one actor: it is common ground.

**Common catalog and network effects**: proto-Botlets accumulate in shared catalogs; each consumer contributes to maturation and implementer n+1 receives versions refined by implementers 1..n. Four membership modes: **private contract** · **proprietary codex** · **open public catalog** (AgencyDomains.org) · **sovereign agreement**. The runtime is common; the curation is each one's own.
