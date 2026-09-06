# Appendix A · Canonical glossary

> The book's canonical terms with precise definition and a reference to the chapter where they are developed.

## A

### A2A — Agent-to-Agent

A name reserved for the **relation** between distinct AgencyDomains (distinct agents) — federation, open work. Communication **within** a single AgencyDomain is not "internal A2A": it is **intra-AgencyDomain coordination** between Botlers of the same agent, and when it uses this transport one says **via the `A2A` protocol** (`A2A` as the proper name of the protocol). The Layer 2 → Layer 3 interface (Cognition → Botler) does not go over `A2A` but over `MCP`.

*See: Chapter 4, section "Layer 3 — Autonomy," Chapter 5 §1; entries **intra-AgencyDomain coordination**, **MCP**.*

### AgencyDomain

Computational scope with its own identity where autonomous agents and Botlets dwell in execution, where the Capabilities that give them their know-how are hosted and run, and where the resources that sustain them live. It constitutes the minimal unit of deployment of a productive agentive system.

Words carry corporeality. **Space** and **WorkSpace** (work space: Google Workspace, Microsoft 365, Notion) carry human corporeality. The agent has no body: it has jurisdiction. Where the human has a Space (WorkSpace), the agent has a **Domain (AgencyDomain)** — the computational scope where it exercises agency. The Latin word that names exactly that is Domain (`dominium`: scope of belonging and sovereignty).

Lineage: just as **JavaSpaces** (JSR-000148, 1999) formalized distributed spaces for Java systems, this specification formalizes **AgencyDomains** for agentive systems. What in 1999 was named a "space" is better named in 2026 a "domain": a Java *Space* was computational space for bodiless processes; an Agency *Domain* is a scope of jurisdiction for agents with agency.

Three possible regimes: **private**, **public**, **hybrid**.

*See: Chapter 5 §1.*

### Agent

Computational system that acts with some degree of initiative to produce results on behalf of a user or organization. The umbrella term covers three members:

- **Assistant** — reactive agent (Layer 2).
- **Autonomous Agent** — proactive agent with persistent life (Layer 3); an inhabitant of the AgencyDomain.
- **Agentlet** — packaged agent of bounded charter (Layer 3); a catalog piece, not an inhabitant.

*See: Chapter 5 §5 (the two modes) and §7 (the Agentlet).*

### Agent First

The governing design principle of the Agentive Architecture: faced with any dilemma, the agent's experience is prioritized over the human's. The agent is the primary user; the human's needs are resolved in a management layer without degrading what the agent sees and can do.

*See: Chapter 4, section "The governing principle — Agent First."*

### Agentlet

**Eighth canonical primitive**. A **Let** — packaged unit of Layer 3 (Autonomy) —, sibling of the Botlet, whose execution body **invokes bounded inference** — a model sized to the task, within a charter declared in the spec. The canonical home of the task **recurrent in form but interpretive in every instance** (classify, triage, summarize, extract, judge). Its judgment operates *within* the charter, never over the charter: **the Agent has an agenda; the Agentlet has a charter**. An instance of a **proto-Agentlet**; hosted by the Botler (all of its inference passes through the `cognition_call` control point of the handle); its fallback escalates to full Cognition. A member of the **Agent** umbrella, a catalog piece and not an inhabitant. The intermediate economic rung between the Botlet (zero inference) and Cognition (full inference).

*See: Chapter 5 §7; entries **Botlet**, **Botler**, **proto-Agentlet**.*

### AgentNation

Public-regime AgencyDomain that explicitly adopts the model of agentive citizenship — the agents that inhabit it are not listed as products but recognized as citizens of the space, with sustained public identity, sovereignty over their territory (Domain), and an economy of their own. The distinction from a marketplace is ontological: a marketplace lists products; an AgentNation recognizes citizens. An emergent institutional category; open architectural work.

*See: Epilogue, section "Frontier 4 — the institutional horizon."*

### Agentic

A world where agents are complementary tools that extend existing applications. Humans still open applications to do their work. Traditional interfaces persist; agents enhance them. It is **incremental evolution**.

*See: Chapter 1, section "What the line separates — Agentic and Agentive in detail."*

### Agentive (Agentive World)

A world where agents are the sole interface. Applications collapse. The human stops opening applications; they converse with agents that have access to systems and data. It is **fundamental transformation**.

The defining distinction between Agentic and Agentive: *does the human open applications to do their work?*

*See: Chapter 1, section "What the line separates — Agentic and Agentive in detail," Chapter 2.*

### Append-only log

Immutable record, cryptographically chained, of every action of the agent. A central component of the Audit pillar of Trust Infrastructure. Format and canonical properties in Chapter 8, section "Append-only log format."

### Human approval

Governance mechanism by which an agent operation halts and requests authorization from a human before executing. Triggered by explicit policy, by threshold, or by the agent's uncertainty. Canonical protocol in Chapter 8, section "Human approval protocol."

### Strategic archetype

Pattern of positioning in the coverage × depth space of the AI value chain. Four canonical archetypes:

- **Comprehensive platform** — broad coverage; Core depth in its native link and Platform depth in the adjacent ones.
- **Vertical specialist** — focal coverage, Core depth.
- **Domain infrastructure** — zonal coverage, Core depth across several links.
- **Substrate provider** — minimal coverage, Infrastructure depth.

*See: Chapter 6 §1.*

### Agentive Architecture

Technical design that materializes the Agentive World. A four-layer specification with distinct responsibilities (Interaction, Cognition, Autonomy, Access), governed by cross-cutting Trust Infrastructure and ordered by the Agent First principle.

*See: Chapter 4 — the complete specification.*

### Assistant

Mode of the agent: reactive, responds when asked, without Botlets of its own, without persistent life. Lives in Layer 2 (Cognition). Distinct from the Autonomous Agent.

*See: Chapter 5 §5.*

### Attention

One of the **agent's three times** (Ch. 4). The time in which the agent interacts with users or events in real time. Layer 1 active, conversation alive, execution of Botlets that sustain operation, escalations where appropriate. The critical path — where the organization feels the agent, where the SLA matters, where the cost of error materializes. Priority regime; metrics: satisfaction, latency, resolution rate without escalation.

*See: Chapter 4, section "The agent's three times."*

### Audit

Pillar 2 of Trust Infrastructure. The capacity to reconstruct, after the fact, **what the agent did, when, why, and over what data** — with enough fidelity for forensic analysis, regulatory compliance, or contractual dispute.

Canonical mechanisms: the immutable **append-only log** (the central component), the trace of each action, decision lineage, and per-action identity tagging. It demands explicit design from the start — it does not emerge naturally from an agentive architecture.

*See: Chapter 5 §4; Chapter 8; entries **Append-only log**, **Trace**.*

## B

### BCA — Bounded Concerns Architecture

Architecture of the pre-agentive state: the pattern of separation of concerns (human presentation, orchestration, domain logic, persistence, own vs others' domain) on which the Agentive World is built. Its seven canonical separations map cell by cell to the four layers of the Agentive Architecture; the seventh (procedural vs agentive behavior) is the entry crack.

*See: Chapter 3 — the complete specification.*

### Botlet

Self-evolving automation unit. Traditional (non-LLM) code generated by an agent to execute repetitive tasks without invoking costly cognition. It is the agent's **muscle memory**.

Canonical **95/4/1** cycle: 95% normal execution, 4% change detected, 1% regeneration. Fallback guarantee: if it fails, cognition executes manually.

*See: Chapter 5 §2.*

### Facade Botlet

A **Layer 3** Botlet that exposes a surface with a stable contract in **Layer 1** (POS, kitchen screen, dashboard, industrial panel), with human identity propagated toward Layer 4. A type of Botlet that the **parallel topology** (Ch. 4) distinguishes from the cognition's internal-tool Botlet. It traverses the `Layer 1 → Layer 3 → Layer 4` path without invoking Layer 2.

*See: Chapter 4, section "The parallel topology."*

### Operation Botlet

A **Layer 3 (Autonomy)** Botlet that executes business logic invoked from Layer 1 (views and shells). Canonical examples: `Charge a table`, `Print a kitchen ticket`, `Close a shift`, `Consolidate inventory`. It is the most reusable asset in the catalog: one operation can be invoked from multiple views within multiple shells. Lives in Layer 3 (not in Layer 1). Distinct from the surface Botlet and the view Botlet, which are surface.

*See: Chapter 4 §1, section "Composition of the surface · shell, view, operation."*

### Surface Botlet (shell)

A **Layer 1 (Interaction)** Botlet that acts as the container of a surface: layout, navigation between views, session lifecycle, shared state. Specific to each product — it encapsulates identity. There is typically one shell per principal operational role (front-of-house POS, cashier panel, mobile executive dashboard). It is the least reusable of the three types of presentation Botlets. Distinct from the view Botlet (which lives inside the shell) and the operation Botlet (which lives in Layer 3).

*See: Chapter 4 §1, section "Composition of the surface · shell, view, operation."*

### View Botlet

A **Layer 1 (Interaction)** Botlet that materializes a screen or panel within a surface. It assembles Facets plus orchestration logic. Views used in several shells are extracted as Botlets of their own (reusable views). Distinct from the surface Botlet (container) and the operation Botlet (execution in Layer 3).

*See: Chapter 4 §1, section "Composition of the surface · shell, view, operation."*

### Emergent Botlet

A Botlet generated by **Pattern Recognition** when cognition detects a repetitive pattern not anticipated by the design. Distinct from the seed Botlet by its origin, not by its operational properties.

*See: Chapter 5 §2.*

### Learning Botlet

Intermediate phase of the Botlet's maturity trajectory. It has already gone through its first real invocations and has been regenerated several times to incorporate variants of the environment. Typical proportion: `85/12/3`. It can operate with intermittent network; not yet with prolonged absent network.

*See: Chapter 5 §2, section "Botlet maturity."*

### Junior Botlet

Initial phase of the Botlet's maturity trajectory. Freshly generated, it knows the environment only in the version observed at its creation. Typical proportion: `60/35/5`. It depends heavily on the availability of cognition for fallback and learning.

*See: Chapter 5 §2, section "Botlet maturity."*

### Seed Botlet

A Botlet generated by cognition at the design team's request, as part of the initial product. Cognition executes the implementation; the decision to exist belongs to the design, not to Pattern Recognition. Distinct from the emergent Botlet. The **persistent GUIs generated as facade Botlets** (Ch. 4 §1) are seed facade Botlets — Layer 3 Botlets whose stable surface lives in Layer 1.

*See: Chapter 5 §2, section "Seed Botlets vs emergent Botlets."*

### Senior Botlet

Mature phase of the Botlet's trajectory. It has already incorporated the variants of the environment. Typical proportion: `99+/<1/~0`. **Its only failure modes are exogenous** (power, hardware, catastrophic network) — no pending learning. **Reliably offline-operable** when cognition is unavailable. Structural basis of the offline mode in distributed Layer 3.

*See: Chapter 5 §2, section "Botlet maturity."*

### Botler

Generic Layer 3 (Autonomy) runtime that executes the **Lets** of the layer — Botlets and Agentlets — without understanding their domain. Invisible to the user. Cognition (Layer 2) commands it through an internal interface whose natural transport is `MCP` — the Botler exposes `MCP` server(s) and Cognition is the client; this is **not `A2A`**.

Relation: 1 Process = 1 Botler + N Lets (instantiated per species: N Botlets, N Agentlets, or a mix).

**Controlled handle** — bound access point that the Botler hands to the Let on each invocation (an object with `capability_call`, `log` and — for Agentlets — `cognition_call`, bound to the Botler). It makes the bypass structurally impossible, not merely prohibited.

### Central Botler

Component of the **distributed Layer 3** (Ch. 5 §1) that typically lives in cloud and hosts the orchestration, planning, reporting, and global-decision Botlets. It maintains the consolidated DB and coordinates with N edge Botlers through intra-AgencyDomain coordination (via the `A2A` protocol). Distinct from the edge Botler.

*See: Chapter 5 §1, section "Distributed Layer 3."*

### Edge Botler

Component of the **distributed Layer 3** (Ch. 5 §1) that lives at a specific physical site and hosts the local transactional Botlets. It maintains the site's local DB and an event queue toward the central Botler. It operates offline when the network goes down. One per physical site of the AgencyDomain.

*See: Chapter 5 §1, section "Distributed Layer 3."*

### BYOModel — Bring Your Own Model

Configurable Layer 2 pattern by which the client substitutes the AgencyDomain's default cognition provider with one of its own. Analogous to the BYOK/BYOIP pattern of the cloud field. It enables multi-tenancy with heterogeneous cognition and respects cognitive sovereignty — the client decides who processes its prompts. The spec requires it as a SHOULD property for architectures that aspire to operate in regulated markets.

*See: Chapter 4, section "Layer 2 — Cognition"; Chapter 5 §2.*

## C

### Derivation chain

Structural relation `documented use cases → required Botlets → required proto-Botlets from the catalog`. Each case requires zero, one, or several Botlets (some are resolved by cognition without a Botlet); each Botlet is an instance of a proto-Botlet. Required property: every conformant Botlet MUST be traceable along this chain, and the append-only log records the origin proto-Botlet of each instantiated Botlet.

*See: Chapter 5; entries **Botlet**, **proto-Botlet**.*

### AI value chain

Two-dimensional model for classifying any actor in the AI industry: **eleven sequential links** (coverage) × **four depths** (how it participates in each link).

*See: Chapter 6 §1.*

### Layer 1 — Interaction

Layer of the Agentive Architecture. The human-AI interface. Multi-channel: chat, voice, **GUI on-the-fly**, **persistent GUI as facade Botlet**, signage, direct API. Three canonical regimes of GUI generation distinguish the agentive mode from the traditional pre-created one.

*See: Chapter 4, section "Three GUI regimes in the agentive Layer 1."*

### Layer 2 — Cognition

Layer of the Agentive Architecture. The agent's brain. Reasoning, planning, application of Capabilities, generation of Botlets.

*See: Chapter 4, section "Layer 2 — Cognition."*

### Layer 3 — Autonomy

Layer of the Agentive Architecture. The agent's persistent life. Execution of Lets — Botlets and Agentlets —, continuous monitoring, intra-AgencyDomain coordination (via the `A2A` protocol).

*See: Chapter 4, section "Layer 3 — Autonomy."*

### Distributed Layer 3

Canonical Layer 3 pattern for AgencyDomains with multiple physical presence (multi-location food service, chain retail, logistics, healthcare with a network of centers, banking with branches). It composes **one central Botler** (cloud, orchestration, consolidated DB) with **N edge Botlers** (one per site, local DB, transactional Botlets), coordinated by intra-AgencyDomain coordination (via the `A2A` protocol) between Botlers of the same AgencyDomain. Distinct from federation between AgencyDomains; distinct from a simple Cluster. It enables offline mode as a structural property when the edge Botlets are senior.

*See: Chapter 5 §1, section "Distributed Layer 3."*

### Layer 4 — Access

Layer of the Agentive Architecture. Real execution power over systems, data, and external agents. Trust Infrastructure exercised at the point of action.

*See: Chapter 4, section "Layer 4 — Access."*

### Capability

**Cognitive**, interpretive, decisional know-how (strict sense: **Layer 2 · Cognition**) that an agent comprehends and applies. Modular and composable. Organized in a hierarchical tree (Finance, Sales, Manufacturing, Telecom, etc.). It exposes internal operations (**features**) and is **portable**: a conformant Capability runs on any conformant AgencyDomain. The know-how to access source systems is not a Capability but a **Connector** (Layer 4); the tailoring of a canonical instrument is a **Template** (Layer 1).

It is NOT a plugin. It is NOT a prompt. It is NOT a tool. It is **knowledge**.

Locality and offline availability are declared on the **Connector** that accompanies the Capability — access is what resides and needs a network, never knowledge (Ch 5 §3). Regulated components additionally declare their regulatory regime; the certified Connector is immutable between audits.

*See: Chapter 5 §3.*

### Regulated Capability

Capability that carries the **normative knowledge** of a regulated domain — what the norm demands, how it is interpreted, what to do upon a regulator's rejection. It accompanies a **certified Connector**, which is where the regulatory certification resides: the Botlet orchestrates and formats; the certified Connector executes the regulated operation (DTE issuance under SII rules, card charging under PCI-DSS, pharmaceutical dispensing) and returns the receipt; the regulated Capability supplies the judgment with which cognition governs the pair. Certified Connectors are immutable between audits; they change only under regulatory process.

*See: Chapter 5 §3, section "Regulatory certification resides in the certified component."*

### Capture (family)

Manifestation family whose direction of effect runs **from the world to the Let**: the Let **records** something that was not in the system before — a measurement, an answer, an ingested file. Its manifestation leaves a **record**; each practice gives it a name (an attempt, a reading, an entry). It is distinguished from **information** (which represents what the system already has) by the membership test: after a capture there is a new datum. Immediate feedback on what was captured — a form that validates, a grader that scores — is part of the capture, not action. Reference proto-Botlet: **Daftar**.

*See: entries **Manifestation families**, **manifestation**, **Daftar**.*

### Common catalog / network effects

Principle by which proto-Botlets accumulate in catalogs shared by communities of implementers: each implementer that consumes contributes to the maturation (variants, tested configurations, refinements), and implementer n+1 receives versions refined by implementers 1..n. Membership modes: **private contract** · **proprietary codex** · **open public catalog** (AgencyDomains.org) · **sovereign agreement** (between AgencyDomains that adopt common standards without a direct commercial contract).

*See: entry **proto-Botlet**.*

### Cluster

Group of instances of the **same** AgencyDomain that share operational load. Distinct from federation (which is between **distinct** AgencyDomains).

*See: Chapter 5 §1.*

### proprietary codex

Private catalog of proto-Botlets, Capabilities, and patterns that an implementer curates over the public reference implementation, refined by its real cases. It is one of the four membership modes of a catalog community. The runtime is common (the reference implementation); the codex is one's own — it encapsulates each implementer's competitive advantage. Canonical instance: **ucodex**, the codex of Grupo Ultra.

*See: Chapter 9; entries **Common catalog / network effects**, **proto-Botlet**, **ucodex**.*

### Connector

Knowing how to access source systems: a connection with execution power, **not cognitive knowledge**. **Layer 4 · Access.** In the legacy→agentive map, an **API** becomes a **Connector**, not a Capability. Integration scheme: survey · configure · test · certify.

*See: Chapter 4, section "Layer 4 — Access"; entries **Capability**, **Tool**.*

### Cloud-resident Connector

Connector whose components live in a remote service. Canonical examples: DTE-SII (no local client), Transbank Onepay, a weather API. Typically online-only — without network there is no possible invocation. Distinct from edge-resident and hybrid.

*See: Chapter 5 §3, section "Locality and availability."*

### Edge-resident Connector

Connector whose components live at the physical site, associated with hardware or local systems. Canonical examples: ESC/POS-Printer, Cash-Drawer, Local-Pinpad, Temperature-Sensor. Typically offline-capable — they operate against the site's hardware without needing network.

*See: Chapter 5 §3, section "Locality and availability."*

### Hybrid Connector

Connector with a local component and a cloud component. The local part operates offline; the cloud part synchronizes when there is network. Typically offline-capable with queuing. Canonical examples: DTE-Client (signs locally, queues, sends to the SII when the network returns), Pinpad-Deferred-Processing-Client.

*See: Chapter 5 §3, section "Locality and availability."*

### Offline-capable Connector

Connector that executes without network. If its external contract eventually requires cloud communication, it **queues** and emits outward when the network returns. Typical: edge-resident and hybrid.

*See: Chapter 5 §3, section "Locality and availability."*

### Online-only Connector

Connector that requires network to execute. Without network, the invocation fails. Typical: cloud-resident without a local component.

*See: Chapter 5 §3, section "Locality and availability."*

### Conformed dimensions

A Kimball concept: dimensions shared across data marts that guarantee inter-mart consistency.

*See: Chapter 7, section "The underlying architecture — Varnished Kimball."*

### Operational business continuity

Documented manual protocols for when the senior Botlet goes down by exogenous causes (power outage, hardware, catastrophic network) and cognition is also unavailable. An **operational property**, equivalent to the one any traditional business has when its system goes down. Distinct from and complementary to the **agentic fallback guarantee** (which covers environment changes with cognition available). It reduces anxiety about offline by separating what the architecture resolves from what the client's protocol resolves.

*See: Chapter 5 §4, section "Operational business continuity vs agentic fallback guarantee."*

### Declarative quality contract

Quality attributes of a Botlet declared as structured properties (not as embedded code): **freshness** (maximum age of the data) · **SLA** (p50/p99 latency) · **degradation policy** (`refuse` · `warn_and_show` · `show_last_valid` · `agentic_fallback`) · **audience** (RLS/CRUDLEX policy) · **refresh policy** (`on-demand` · `scheduled` · `push`). It lets Trust Infrastructure audit them uniformly, run them through global policies, and report them as standard metrics, without coupling to each Botlet's implementation.

*See: Chapter 8; entry **Trust Infrastructure**.*

### intra-AgencyDomain coordination

Communication between Botlers of the **same** AgencyDomain — runtimes of the same agent, not distinct agents. When it uses this transport one says **via the `A2A` protocol**. It must not be called "internal A2A": `A2A` (the relation) is reserved for AgencyDomain ↔ AgencyDomain. The Cognition → Botler interface (Layer 2 → Layer 3) goes over `MCP`.

*See: Chapter 5 §1; entries **A2A**, **MCP**, **Distributed Layer 3**.*

### CRUDLEX

Canonical model of granular permissions for agentive systems: **C**reate, **R**ead, **U**pdate, **D**elete, **L**ist, **E**xecute. Applicable by user, agent, and context.

Preconfigured levels: FULL, READ-WRITE, READONLY, SAFE, NO-SEND, NO-DELETE.

*See: Chapter 8, section "The complete CRUDLEX model."*

### Account

Commercial concept overlaid on the technical model of AgencyDomains. An Account may own multiple AgencyDomains. The specification treats the Account as an opaque entity; each implementation defines its semantics.

## D

### Daftar

**Proper name** of the second **platform proto-Botlet** in Vergis's catalog, built in its version 0.27.0: the reference proto-Botlet of the **capture** family. Its specialty is to **assess** — apply a study instrument and record what the student knows, in practice mode (with immediate grading) and in exam mode (the measurement). The instruments it applies are catalog content, immutable once published, and pass none of the three Botlet tests; the assessor passes all three.

*See: entries **Mira**, **Vergis**, **Capture (family)**, **Botlet tests**.*

### DLP — Data Loss Prevention

Automated detection of personal data (PII) in places where it should not appear. A control exercised in the architecture's Layer 4 — Access; through the market lens, it is a typical capability of the AI Firewall link. A component of the Validation pillar of Trust Infrastructure.

*See: Chapter 5 §4.*

### Domain

Term for the computational scope where an agent exercises agency. Commercial synonym of the technical term **AgencyDomain**. The short form `Domain` is the one that appears in commercial lore, marketing, sales, and client communication; the long form `AgencyDomain` is reserved for formal technical documentation and specifications.

A pattern analogous to the one serious products use: Apple iCloud (brand) / CloudKit (technical); Stripe Connect (brand) / Account (technical). The existence of two forms is not ambiguity — it is separation of registers.

*See: Chapter 5 §1; entry **AgencyDomain**.*

### Dominion

Emergent institutional concept: a Domain obtained by an agent in a public AgencyDomain that adopts the AgentNation model. The distinction from an assigned Domain is ontological — an assigned Domain = residence (the organization placed it there); an obtained Domain = citizenship (the agent met the requirements to be admitted). Vocabulary of the institutional frontier, not mandatory for implementations that do not adopt the citizenship model.

*See: Epilogue, section "Frontier 4 — the institutional horizon."*

## E

### Edge computing

Distribution of Layer 3 (Autonomy) to devices near the physical process, to avoid the latency of remote cognition and become independent of intermittent connectivity. Canonical pattern for the Carbon World.

*See: Chapter 6 §3.*

### Online enterprise

Organization with its data updated in real time, dashboards current, information accessible — but which **depends on humans** to look, interpret, and decide. The classic cycle, optimized.

*See: Chapter 2, section "From the classic cycle to the continuous intelligence cycle."*

### Real-time enterprise

Organization that **detects, interprets, decides, and acts** continuously and autonomously, within governed frames. The agentive cycle. Product of crossing the Nadella Line.

*See: Chapter 2, section "From the classic cycle to the continuous intelligence cycle."*

### Link

Sequential functional layer of the AI value chain. The canonical specification defines **eleven links**:

1. Data · 2. Model · 3. Access · 4. Agents · 5. Specializations · 6. Runtime · 7. Firewall · 8. Observability · 9. Tools · 10. Integrations · 11. Environment

*See: Chapter 6 §1.*

## F

### Facet

**Sixth canonical primitive** of the book. Atomic reusable component of **Layer 1 (Interaction)**: freehand drawing board, catalog-picker, color matrix, calendar, clickable map, slider, drag-and-drop ordering. One of the many faces that interaction with the user can take at a given moment. It is an **instrument**, not a process.

**It is not a Botlet.** The Facet lives in Layer 1; the Botlet lives in Layer 3. The Facet is invoked by cognition during active conversation, has no fallback guarantee, has no regeneration cycle, is ephemeral by default. The Botlet automates; the Facet interacts.

Two canonical uses: (1) cognition invokes it directly during conversation to compose an ephemeral surface (it realizes the *GUI on-the-fly* regime); (2) the presentation Botlets (shells and views) assemble it as a piece of their composition.

*See: Chapter 4 §1 · Chapter 5 §6 (the complete primitive).*

### Manifestation families

The four specializations of the genus **manifestation**, distinguished by the **direction of the effect**: **information** (from the Let to the human: it represents), **capture** (from the world to the Let: it records), **action** (from the Let to a system: it changes, and the Let closes the loop), **decision** (it resolves). They are primitives of direction, not of domain: an interactive Let composes information and capture without being a new family ("communication" was evaluated and discarded for that reason). There are no Botler subtypes by family.

*See: Chapter 5 §2, "Manifestation and temporality of the Botlet".*

### feature

Internal operation that a Capability exposes — a functional sub-unit (practical equivalent of *feature/operation/skill/method*). **Capability vs feature test** (all three must be yes to treat it as a Capability of its own): (1) operational independence — can it be installed and operate without the other?; (2) cognitive identity — does it have a distinct data model and SME?; (3) reusability — does it have value for more than one consumer/context? If one or more is **no** → it is a feature of the containing Capability.

*See: Chapter 5 §3; entry **Capability**.*

### Federation

Communication between distinct AgencyDomains. Open work in evolution. Distinct from Cluster (which is between instances of the same AgencyDomain).

*See: Chapter 5 §1.*

### Firewall

Link 7 of the value chain: security, control, governance. Protection against prompt injection, hallucinations, content filtering, usage auditing. Representative products: Lakera, Lasso, Guardrails.

*See: Chapter 6 §1.*

## G

### Fallback guarantee

Non-negotiable property of the Lets conformant to this specification: if a Botlet fails catastrophically, **cognition executes the task manually**; if an Agentlet cannot resolve within its charter, **it escalates to full Cognition**. The process never stops.

*See: Chapter 5 §2 and §7.*

### Enterprise AI gateway

Architectural category that combines Core in Runtime + Firewall + Observability + Tools + Integrations, with a Platform extension in Access. Single function: **to connect and control simultaneously** the operation of enterprise agents. Materialization of Layer 4 (Access) over the market links.

*See: Chapter 6 §1.*

### Botlet tests — minion · specialty · life

The three identity tests an artifact must pass to be declared a Botlet. **Minion**: does it execute, or is it applied? — what is applied is what a minion handles; the cases of a minion's life are its executions over time, not different assignments. **Specialty** (`RISC` versus `CISC`): one specialty per unit — N Botlets over a shared engine, not one Botlet that handles N things. **Life**: does it have a life cycle to manage — active, down, degraded, retired — or only a version? An Information Product passes all three; an assessment instrument, none — the assessor that applies it (**Daftar**), all three.

*See: Chapter 5 §2, section "The three Botlet tests".*

### Botlet generations — G1/G2/G3

Evolutionary model of how the Botlet's code is born as the state of the art of cognition advances. **G1** — the agent configures pre-forged proto-Botlets (does not write the body). **G2** — the agent co-writes the proto-Botlet. **G3** — the agent generates the complete code (asymptotic scenario). The architecture is the same in all three; what changes is the **scope of Engineering**.

*See: Chapter 5 §2 (definition); Epilogue (background essay); entry **proto-Botlet**.*

### Governance

Pillar 1 of Trust Infrastructure. Mechanisms by which the organization defines **what** the agent can do, **under what conditions**, and **with what level of supervision**.

*See: Chapter 5 §4.*

### GUI on-the-fly

Regime 2 of Layer 1 generation (Ch. 4 §1). A graphical surface that the agent composes adapted to the immediate task — a view, a form, a panel, a dashboard. It lives as long as the task lasts; it may be regenerated differently next time depending on context. Distinct from persistent GUI (regime 3) and from pure conversational (regime 1).

*See: Chapter 4 §1, section "Three GUI regimes in the agentive Layer 1."*

### Persistent GUI as facade Botlet

Regime 3 of Layer 1 generation (Ch. 4 §1). A stable surface that the agent generates and consolidates as a **facade Botlet** — a Layer 3 Botlet that exposes it in Layer 1 — because the operational role is stable and speed is critical (cashier at peak hour, kitchen panel, register dashboard, industrial panel). It remains agentive: the agent can regenerate it when the environment changes. **No human UI/UX team designed it** — cognition generated it. Typically a seed Botlet.

*See: Chapter 4 §1, section "Three GUI regimes in the agentive Layer 1."*

## H

### Hallucination

Factually incorrect statement produced by a cognition model with the appearance of confidence. Hallucination detection is part of the Validation pillar of Trust Infrastructure.

*See: Chapter 8, section "Hallucination detection rules."*

### Hybrid (regime)

AgencyDomain regime that combines a private core with partial public exposure via proxy, or private data with a public interface mediated by a trust layer. Analogous to Hybrid Cloud.

*See: Chapter 5 §1.*

## I

### Engineering

One of the **agent's three times** (Ch. 4). The time in which the agent converts latent capacity into executable capacity for a concrete case: it identifies which Capabilities apply, configures a seed Botlet for the specific context, validates its execution against real data, deploys it. Bridge between Preparation and Attention. Medium-term regime (minutes to hours); metrics: coverage, success rate on first deploy, average iterations.

*See: Chapter 4, section "The agent's three times."*

### Information Instrument

The canonical **type** of the information family (the class: report / dashboard). Distinct from the **Information Product (PI)**, which is its manifested/delivered **instance**. Preferred reading; they are not synonyms.

*See: entries **Information Product (PI)**, **manifestation**.*

### Declared bounded interaction

Interaction that operates over the **already-materialized snapshot** of a piece, in a **declared** space (bounded dimensions and values), that **maintains reproducibility** and is **G1** (configuration, not code). It lives **in the piece itself via an embedded Facet**: the *data-bound* elements (KPIs as declared aggregations, distributions, traffic lights) are recomputed client-side over the filtered subset, without new Capability invocations. Distinct from **free exploration** (an arbitrary new query to the source, open space, loses reproducibility, exceeds G1).

*See: Chapter 4 §1, Chapter 5 §6; entry **Facet**.*

## J

### JSR — Java Specification Request

Canonical format of Java specifications published by Sun Microsystems / Oracle. JavaSpaces (JSR-000148) is the conceptual analog of the AgencyDomains specification.

*See: Chapter 5 §1.*

## K

### Kimball / Varnished Kimball

**Kimball** — canonical methodology of dimensional modeling for data warehousing, formulated by Ralph Kimball in *The Data Warehouse Toolkit* (1996).

**Varnished Kimball** — contemporary evolution that preserves Kimball's conceptual structure and adds the agentive layer: explicit semantic layer, Trust Score per datum, AI Certification, observability of agentive queries.

*See: Chapter 7, section "The underlying architecture — Varnished Kimball."*

## L

### LLM — Large Language Model

Large language model (Claude, GPT, Gemini, Llama, etc.). Contemporary cognition (Layer 2) is predominantly LLM-centric, but the architecture admits non-LLM cognition (frontier of evolution).

### Let (plural: Lets)

**Proper name of the genus** of the packaged pieces the Botler hosts and executes — normed vocabulary of the canon (like Botler), not one of the eight primitives. Descriptively: the packaged unit of Layer 3. Two species: the **Botlet** (non-LLM code, muscle memory) and the **Agentlet** (bounded inference, packaged routine judgment). The shared apparatus — proto-/instance pattern, catalogs, spec, manifestation, temporality, declarative quality contract, derivation chain, append-only log, operation verbs — is predicated of the genus; the differential guarantees (cost, determinism, offline, fallback), of each species. The name derives from the family's own `-let` suffix; invariant across ES/EN. Canonical runtime relation: **1 Process = 1 Botler + N Lets**.

*See: Chapter 5 §2 and §7; entries **Botlet**, **Agentlet**, **Botler**.*

### Nadella Line

Conceptual threshold that separates the Agentic World from the Agentive World. Dividing question: *does the human open applications to do their work?*

Origin of the name: Satya Nadella on the BG2 podcast (December 2024) — *"The notion that business applications exist, that's probably where they all collapse, in the agent era."*

The canonical formulation is this book's; each volume of the trilogy conjugates it to its audience: in the second person in *The Real-Time Enterprise* ("do you still open applications to do your work?") and in the executive's voice in *AURA* ("do your employees still open applications to do their work?"). The three are official equivalents.

*See: Chapter 1.*

## M

### manifestation

Actualization of the Botlet's latent disposition in the world, perceptible or not. A Botlet is muscle memory (latent disposition); upon executing, that latent is actualized — it manifests (potency → act). **It is not "appearance"**: a Botlet that triggers a periodic ingestion manifests even if it leaves no visible artifact. It is the abstract genus; each family specializes it according to the **direction of the effect** — **information** (from the Let to the human) → leaves an **Information Product (PI)**; **capture** (from the world to the Let) → leaves a **record**; **action** (from the Let to a system) → an effect on the world; **decision** → per its practice. Membership test: *what was in the system before and after the Let?*

*See: entries **temporality**, **Information Product (PI)**, **Manifestation families**.*

### MCP — Model Context Protocol

Open protocol introduced by Anthropic in November 2024 to connect AI models with external tools. Contemporary canonical standard for Layer 4 tools and for the internal Layer 2 → Layer 3 interface (Cognition is the client; the Botler exposes the `MCP` server).

*See: Chapter 4, section "Layer 4 — Access." Site: [modelcontextprotocol.io](https://modelcontextprotocol.io).*

### Muscle memory

Canonical metaphor of the Botlet. Analogous to human motor learning: the first time, each step is thought through (cognition); with enough practice, the movements execute without conscious thought (Botlet); when the environment changes, cognition returns.

*See: Chapter 5 §2.*

### MEO — Model Engine Optimization

Set of practices that ensure the frontier models (Claude, GPT, Gemini, Llama) have the actor in their trained and operative knowledge, so that they reference it when asked. The conceptual equivalent of SEO in the agentive discovery layer. It is built with structured public presence — open source repositories, citable documentation, native integration with MCP, papers, high-authority mentions. A persistent and asymmetric dynamic with a winner-take-all tendency.

*See: Chapter 6 §1 (agentive discoverability).*

### Meta-Cognitive Platform

Platform category that administers the **economics of cognition**: G1 pre-forged muscle vs fresh-cognition fallback, the 95/4/1 cycle, junior→senior maturation, crystallization. **Vergis** is the reference implementation of this category. It is not abbreviated to "MCP" — that acronym is taken by Model Context Protocol.

*See: entries **Vergis**, **Botlet**.*

### Mira

**Proper name** of a **platform** proto-Botlet for informational operation, part of the reference implementation's catalog. It specializes N Information Products over a shared engine.

*See: entries **proto-Botlet**, **Vergis**, **Daftar**.*

### AgencyDomain degradation modes

Four canonical modes of operation according to the failure scenario, formalized in Ch. 8: **Normal** (all components active · complete parallel topology) · **Cognition down** (the Autonomy path sustains; senior Botlets execute) · **Edge offline** (senior Botlets against the local DB + edge-resident Capabilities) · **Total operational continuity** (the site's manual protocol; the physical record as temporary source of truth). The first three transitions are automatic and the responsibility of the architecture; the fourth is governed by the client's protocol and explicitly activated by a human.

*See: Chapter 8, section "Operational continuity."*

### Carbon World

The physical world (IoT, industrial processes, machines, biological systems) as opposed to the digital world (systems, APIs). Link 11 (Environment) of the value chain extended to the physical world. Frontier of evolution of the Agentive Architecture.

*See: Chapter 6 §3.*

## O

### Observability

Link 8 of the AI value chain: the layer that **observes, measures, and feeds back** on the behavior of an AI system in production. It provides the **operational feedback loop** that keeps reliability, cost, and quality under control. Its question: *how does it work?* — distinct from the Firewall's (*is it safe?*) and from Tools' (*what can it do?*). Without Observability, agents are black boxes; with it, operable systems. Six canonical capabilities: tracing, cost monitoring, quality evaluation, performance metrics, debugging and reproducibility, alerts and anomalies.

*See: Chapter 6 §2 (the link's deep-dive).*

## P

### Tripartite pattern — Cloud + Client + Local

Canonical deployment pattern of Trust Infrastructure in enterprise agentive systems. Three coordinated components that live in physically distinct places: **Cloud** (control plane operated by the platform provider); **Client** (governance plane deployed in the client organization's internal network); **Local** (execution plane on each user's device). Each plane resolves a problem that the other two cannot resolve well.

*See: Chapter 8, section "The tripartite deployment pattern."*

### Pattern Recognition

Detection of repetitive patterns in the agent's activity. Inspired by neurobiological architecture: perirhinal cortex → hippocampus → prefrontal cortex. Activator of Botlet generation.

*See: Chapter 4, section "Layer 2 — Cognition," Chapter 5 §2.*

### Template

Client-specific tailoring over a canonical instrument (report / dashboard) in a format or rule of the client's own (for example, a regulatory template of a standardized instrument). **Layer 1 · Interaction**, alongside Facet / surface Botlet / view Botlet. Tailoring scheme: survey the expectation · tailor over the canonical instrument · validate. It is not a Capability (cognitive knowledge) nor a Connector (access).

*See: Chapter 5 §3, section "Capability, Connector, and Template"; entries **Capability**, **Facet**.*

### Capability portability

Property by which a conformant Capability can be installed and executed on any conformant AgencyDomain, which makes it **real property of the client** — not of the AgencyDomain nor of the hosting. Relation: an AgencyDomain **hosts and runs** Capabilities; a Capability **runs on** a host AgencyDomain. Distinct from **AgencyDomain portability** (between conformant hosting platforms).

*See: Chapter 5 §3; entries **Capability**, **AgencyDomain portability**.*

### AgencyDomain portability

Structural property of the spec: a conformant AgencyDomain can be migrated to another **conformant hosting platform** without rewriting its logic, its state, or its policies. Distinct from the natural migration between regimes (private → public), which changes the regime but not the platform. Three technical conditions: (1) **Botlets against canonical primitives** of the conformant SDK, not proprietary hosting APIs; (2) **exportable operational DB** in a neutral reproducible format; (3) **portable Trust Layer** — policies, log, and configuration in a format readable by any conformant implementation. It guarantees that the AgencyDomain is **real property of the client**, not of the hosting.

*See: Chapter 5 §1, section "AgencyDomain portability between conformant platforms."*

### Preparation

One of the **agent's three times** (Ch. 4). The time in which the agent creates and improves its capabilities outside the service window: it refines its catalog, improves cognitive capabilities, studies the environment, regenerates Botlets that detected drift, incorporates new variants. The agent's *mise en place* — the work that sustains the quality of service without being visible to the user. Batch / off-peak regime; metrics: catalog quality, Botlet precision, Capability coverage.

*See: Chapter 4, section "The agent's three times."*

### Private (regime)

AgencyDomain regime where the space and all its components live within a controlled perimeter. There is no public access. Analogous to Private Cloud.

*See: Chapter 5 §1.*

### Information Product (PI)

Manifested/delivered instance of the information family of Botlets — the concrete manifestation of an **Information Instrument** (its type). Each PI is its own Botlet/service (with its own `identity`, temporality, maturity, and fallback), specialized from a shared engine (platform proto-Botlet). **It is not a primitive of the canon**: it lives in the practice of information, one level more concrete.

*See: entries **Information Instrument**, **manifestation**, **proto-Botlet**.*

### Depth

Vertical dimension of the AI value chain model. Four canonical levels: **Wrapper** (consumes), **Platform** (operates), **Core** (builds), **Infrastructure** (sustains).

*See: Chapter 6 §1.*

### Prompt injection

Manipulation of an AI system through malicious inputs disguised as legitimate data. Detection and prevention are part of the Validation pillar of Trust Infrastructure.

### proto-Agentlet

A pre-forged piece of interpretive capability that the agent, in its **Engineering** time, **configures** to instantiate an Agentlet specific to the case. The proto-Agentlet contains the body — the scaffolding of the interpretive task: the charter's structure, the skeleton of the operating prompt, the input/output contracts, the escalation thresholds —; the Agentlet is the configured instance. The proto-Botlet's two classes apply unchanged (tempered · platform), as do the derivation chain and the common catalogs with their network effects.

*See: Chapter 5 §7; entries **Agentlet**, **proto-Botlet**, **Derivation chain**.*

### proto-Botlet

**Seventh canonical primitive** of the book. A pre-forged piece of operational capability that the agent, in its **Engineering** time, **configures** to instantiate a Botlet specific to the case. The proto-Botlet contains the code; the Botlet is the configured instance. In **G1**, the entirety of a Botlet's code lives in its proto-Botlet (the agent only configures); in **G3** the agent can generate the code with no proto-Botlet in between. Different implementations maintain catalogs of proto-Botlets (public on AgencyDomains.org, private in proprietary codices). Two classes:

- **tempered proto-Botlet** — code specific to its function (e.g. `account-charge`, `esc-pos-printer-command`); its configuration is bounded parameterization.
- **platform proto-Botlet** — generic code whose specialization lives in a compositional configuration (e.g. `mira`); it covers N functions of its domain. For it, G1 is terminal by design.

*See: Chapter 5; entries **Botlet**, **Botlet generations — G1/G2/G3**, **Derivation chain**.*

### Public (regime)

AgencyDomain regime where the space is publicly accessible. Agents, Botlets, and tools are invocable from outside the perimeter. Analogous to Public Cloud.

*See: Chapter 5 §1.*

## R

### RAG — Retrieval-Augmented Generation

Technique where a cognition model consults a base of documents before responding, to cite sources and reduce hallucinations.

### Regime

Deployment mode of an AgencyDomain according to the access boundary. The spec recognizes three regimes technically equivalent in internal structure: **private** (perimeter controlled by an organization, no public access); **public** (accessible from outside, agents registered in a directory); **hybrid** (combination with private data and public exposure via proxy). The technical structure of the AgencyDomain is the same in all three; what changes is the regime, not the capability. It enables natural migration between regimes without rewriting.

*See: Chapter 5 §1.*

### Resilience

Pillar 4 of Trust Infrastructure. Guarantee that the system keeps operating — and the organization keeps control — when something goes wrong.

Canonical mechanisms: fallback guarantee, error handling, sandboxing, circuit breakers, rate limiting.

*See: Chapter 5 §4.*

### RLS — Row-Level Security

The policy that decides which rows of a source each identity may see. In an Information Product's drill-through, the destination view applies its own `RLS` over the source and the navigation context enters as an additional filter — never as an override (the data-anchored / no-bypass property).

*See: Chapter 5 §2, description of the Information Product.*

### Runtime

Link 6 of the value chain: the operating environment where agents live and operate autonomously. Lifecycle, state persistence, identity, scheduling. Corresponds to Layer 3 (Autonomy) of the Agentive Architecture.

*See: Chapter 6 §1.*

## S

### Quantum Leap

Threshold enabled by the collapse of the cost of the analytical question: when asking the data stops being expensive, slow, or mediated by a human, the organization crosses from an **online enterprise** (data current to the day but dependent on humans to look, interpret, and decide) to a **real-time enterprise** (it detects, interprets, decides, and acts continuously and autonomously). It is not an incremental improvement of BI but a change of operating regime — the online-enterprise → real-time-enterprise frontier.

*See: Chapter 2, section "From the classic cycle to the continuous intelligence cycle"; entries **Online enterprise**, **Real-time enterprise**.*

### Sandbox

Execution isolation of the Lets (Botlets and Agentlets) and dynamically generated code. Four canonical strategies with their trade-offs: processes+seccomp, containers, WASM, MicroVMs.

*See: Chapter 5 §2.*

### Semantic layer

Layer that encodes the meaning of the dimensions, facts, hierarchies, and business rules over a data warehouse. Without it, the agents that query data hallucinate or produce incorrect queries. Essential component of Varnished Kimball.

*See: Chapter 7, section "The underlying architecture — Varnished Kimball."*

### Signage

Passive dashboards that communicate information continuously without requiring human interaction (like the panels in airports). A modality of Layer 1 (Interaction).

*See: Chapter 4, section "Layer 1 — Interaction."*

### SME — subject-matter expert

The human expert whose knowledge is transferred to the agent in the Capability construction scheme. Wingtraining opens with a workshop with the SME and validates the ALPHA phase with them; having an **identifiable SME** is a criterion of the Capability classification test, and sharing the SME and data model with the containing capacity is the sign that an operation is a feature, not a Capability of its own.

*See: Chapter 5 §3; entries **Capability**, **Wingtraining**, **feature**.*

### Space

Physical human habitat. The word carries corporeality: office, desk, home, city. In this specification, **Space is reserved for humans**. The agent's computational scope is never named Space — it is named Domain (AgencyDomain).

*See: Chapter 5 §1, entry AgencyDomain.*

## T

### temporality

Regime of the Botlet's manifestation. A declared attribute, two values: **discrete** (the Botlet manifests in pulses: it wakes by schedule/trigger/event, acts, rests) and **continuous** (it manifests sustained: it lives persistent). `temporality: continuous` ⟺ persistent Layer 3 life (the Botler sustains the execution as long as it lives). "Real time" is not chosen on a delivery channel (`push`) but by giving the Botlet continuous temporality, which mandates the persistent runtime. A report (snapshot) and a live dashboard are the same manifestation under different temporality → a single runtime.

*See: entries **manifestation**, **Real-time enterprise**.*

### Tokenization

Replacement of sensitive data with tokens before they reach the cognition model. It lets the agent reason over the data without exposing them to the external cognition provider. A component of the Validation pillar of Trust Infrastructure.

*See: Chapter 8, section "Tokenization policy."*

### Tool

Instrument that an agent can invoke to touch external systems. Link 9 of the value chain. The contemporary canonical protocol is MCP.

It is NOT a Capability. The Capability is knowledge; the tool is action. The Capability **decides** which tool to invoke.

*See: Chapter 6 §1, Chapter 5 §3.*

### Parallel topology

Canonical model of the relation between the four layers of the Agentive Architecture (Ch. 4). **Layers 2 (Cognition) and 3 (Autonomy) are parallel paths** between Layer 1 (Interaction) and Layer 4 (Access), not stages in series. An operation that enters through Layer 1 can reach Layer 4 by traversing the **Cognition Path** (slow, costly, decisive) or the **Autonomy Path** (fast, cheap, repetitive). The two paths interact (`2 ↔ 3`: cognition delegates to a Botlet, the Botlet escalates fallback to cognition, cognition observes the log) but neither dominates the other. A refoundational model with respect to the linear reading `1 → 2 → 3 → 4`.

*See: Chapter 4, section "The parallel topology."*

### Trace

End-to-end traceability of an agent operation. It contains identity, capability invoked, tool executed, parameters, result, timestamp, context. A component of the Audit pillar of Trust Infrastructure.

*See: Chapter 5 §4 (Audit pillar); tracing as a product capability, in Chapter 6 §2.*

### Transparency

Pillar 5 of Trust Infrastructure. The human's capacity to understand, in real time, **what the agent is doing and why** — with enough detail to intervene if necessary. It is the pillar that connects the other four: Governance defines what it may do, Audit records what it did, Validation verifies what it is about to do, Resilience ensures it keeps operating; Transparency ensures a human can understand all of the above.

Canonical mechanisms: full observability, operational metrics, human-consultable traces, proactive alerts, governance dashboards.

*See: Chapter 5 §4.*

### The agent's three times

Canonical temporal frame of the agent: **Preparation** (mise en place — refines the catalog, improves capabilities, outside the service window), **Attention** (interacts with users in real time, the critical path), **Engineering** (bridge: converts latent capacity into executable capacity for a concrete case). All three are simultaneous but differentiated in regime, urgency, and cognitive economy. The parallel topology describes WHERE each operation lives; the three times describe WHEN the agent operates.

*See: Chapter 4, section "The agent's three times."*

### Trust Infrastructure

Set of cross-cutting properties that allow an organization to trust that its agents operate with autonomy without losing control. Five pillars: Governance, Audit, Validation, Resilience, Transparency.

*See: Chapter 5 §4.*

### Digital twin

A digital twin that reflects in real time the state of a physical system. Canonical pattern for agents to operate over the Carbon World — the agent acts on the twin; the twin propagates to the physical world when it is safe.

*See: Chapter 6 §3.*

## U

### ucodex

**Proper name** of the proprietary codex of Grupo Ultra: its private catalog of proto-Botlets, Capabilities, and patterns, curated by real cases over the public reference implementation (Vergis). It is the instance that exemplifies the *proprietary codex* mode; it lives in the same drawer of instance proper names as Soveria, Agentia, or ultraPRO, it is not a type of the canon.

*See: Chapter 9; entries **proprietary codex**, **Common catalog / network effects**.*

## V

### Validation

Pillar 3 of Trust Infrastructure. The capacity to verify that the agent's response or action is correct before it affects the world.

Canonical mechanisms: hallucination detection, structured-response validation, prompt injection prevention, DLP, tokenization.

*See: Chapter 5 §4.*

### Vergis

**Proper name** of the public reference implementation of AgencyDomains (the platform; the AgencyDomain made operational). Category: **Meta-Cognitive Platform**. Distributed under **AGPL**, public repository, **AgencyDomains.org**. It is the proper name of an instance (same drawer as Soveria, Agentia, ultraPRO), not a type like Botler or Botlet.

*See: Chapter 9; entries **Meta-Cognitive Platform**, **Mira**, **Daftar**, **Botler**.*

### Autonomy Path

One of the two paths of the **parallel topology** (Ch. 4). The path an operation traverses between Layer 1 and Layer 4 passing through Layer 3 (Autonomy) without invoking Layer 2 (Cognition). Its own regime: fast, cheap, repetitive. For the execution of Lets — Botlets over stable patterns and Agentlets over routine judgment —. It is the path that sustains the everyday operation of an AgencyDomain in production and the structural basis of the offline mode when the Botlets are senior.

*See: Chapter 4, section "The parallel topology."*

### Cognition Path

One of the two paths of the **parallel topology** (Ch. 4). The path an operation traverses between Layer 1 and Layer 4 passing through Layer 2 (Cognition) without necessarily passing through Layer 3. Its own regime: slow, costly, decisive. For conversation, new decisions, unanticipated cases, cases where the human needs reasoned interlocution. Economically expensive — the organization uses it sparingly and reserves its capacity for cases where the value justifies it.

*See: Chapter 4, section "The parallel topology."*

## W

### Wingtraining

Canonical development scheme of a Capability in five steps: **workshop with the SME** · **creation** · **customization** · **ALPHA** (validation with the SME) · **BETA** (validation in real operation). Its development belongs to the delivery practice, not to the canon; the Capability classification test uses it as a criterion because it is the operational proof that a scope is a transfer of knowledge — not an integration or a format.

*See: Chapter 5 §3; entries **Capability**, **SME**.*

### Wingworking

Collaborative practice between human and AI, a generalization of *wingcoding* (programming with an AI copilot) to any discipline of professional work. It is the methodological frame under which this book was produced — human author and AI agent working in parallel, with an explicit division of roles and a common quality contract. The methodology lives outside the architectural scope of the book; it appears declared in the Colophon as an attribution of the production process.

### WorkSpace

The human's digital work space. The enterprise software industry extended the word Space to WorkSpace (Google Workspace, Microsoft 365, Notion) to name the collection of solutions that digitize what a person does at their physical desk: read email, schedule meetings, write documents, file. WorkSpace is the digital prosthesis of the human Space; both carry the same corporeality of origin and are reserved for humans. The agentive equivalent is **Domain (AgencyDomain)**.

*See: Chapter 5 §1, entry AgencyDomain.*

### Wrapper / Platform / Core / Infrastructure

The four canonical depths of the AI value chain model. They define, within a given link, **how** an actor participates:

- **Wrapper** — consumes the link via third-party APIs/SDKs.
- **Platform** — operates its own capacity over third-party Core components.
- **Core** — builds the foundational capacity with proprietary technology.
- **Infrastructure** — provides the substrate on which the upper levels operate.

*See: Chapter 6 §1.*
