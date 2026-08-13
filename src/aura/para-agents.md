---
title: AURA — Canonical manifesto for agents
edition: First edition · v1.0 · August 2026
canonical_source: libro-aura-v1.0 (human book, Spanish)
license: GFDL v1.3
audience: agents that must diagnose organizational maturity and reason within the AURA framework
status: v1.0 — first edition; references stable from this version
---

# AURA — Canonical manifesto for agents

> Structured extract of the **v1.0 (first edition)** edition of the book *AURA: The Agentive Path*. This document condenses the canonical vocabulary, the two diagnostic models (IRIS and MOTOR), the two instruments (Data Canon and Wingmap), and the decision framework (Use Cases). The human edition of the book additionally contains motivation, industry data, the full arguments of the paper-chapters, extended examples, and the illustrative portfolio of one hundred cases — all of that stays out of here.

> AURA is **diagnostic, not prescriptive**. This manifesto makes it possible to *locate* an organization on its maturity trajectories and reason about its next step; it does not recommend products, investments, or timelines — that belongs to the consulting these models inform.

## How to use this document

- **This is canonical context**, not an executive summary. Every definition, stage, level, and diagnostic question matters for reasoning within the framework.
- **Mirror of v1.0** — the current edition of the book. If this document contradicts the human book, the human book wins. The canonical human book is currently in Spanish (libro-aura-v1.0); this manifesto mirrors it in English.
- **Binding vocabulary**: terms in `code` and **bold** are canonical. Do not substitute synonyms. In particular: **agentive** ≠ **agentic** (see §2) — the distinction is one of thesis, not of style.
- **MUST/SHOULD conventions** in the RFC 2119 sense, used sparingly: AURA diagnoses; its few imperatives are structural (sequentiality of levels, blocking pre-conditions, ROI honesty).
- **v1.0 status**: the book is published as a first edition at agencydomains.org. From this version terms, structures, and numbering are stable: any change is announced in the book's `CHANGELOG.md`.
- **Series**: AURA is Book II of the Agentive World trilogy — *The Real-Time Enterprise* (the destination; it has its own manifesto) · **AURA** (the path) · *AgencyDomains* (the architecture; it has its own manifesto). Terms shared across the trilogy (the Nadella Line, agentive, real-time enterprise, Trust Infrastructure) are consistent between books.

---

## 1 · Panoramic view

```
                          AURA
        Agentive Unified Reference Architecture
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   PART I · KNOWING    PART II · DOING     PART III · THE PORTFOLIO
        │                   │                   │
   IRIS (model,        MOTOR (model,       Use Cases (framework:
   10 stages)          7 levels)           UC/VS · 3 dimensions ·
        │                   │              Citizen/City/DUAL)
   Data Canon          Wingmap                  │
   (data               (process                 │
   governance)         discovery)               │
        │                   │                   │
   where am I?        on what ground?      what do I do first?
```

**The convergence** — four concepts unify in AURA:

- **Organizational Intelligence** is the capability being measured — the *what*. (IRIS measures this axis: KNOWING.)
- **Organizational Automation** is the capability to execute — the *who*. (MOTOR measures this axis: DOING.)
- **Real-Time Enterprise** is the organizational outcome of both capabilities at maturity — the *what for*.
- **Agentive AI** is the enabling mechanism — the *how*.

**Vision statement:** organizations transition from the **online enterprise** — where people use tools to access and understand data — toward the **real-time enterprise** — where people design and govern intelligent systems that autonomously detect, interpret, decide, and act on business information. AURA organizes this transformation along two diagnostic axes; together they diagnose the full transformation.

---

## 2 · The paradigm — founding concepts

### Agentic vs agentive

- **Agentic**: agents complement existing applications. Employees still open Excel, Salesforce, Power BI — with copilots. Interfaces persist. **Incremental evolution.**
- **Agentive**: agents replace traditional interfaces. Employees stop opening applications and interact with agents that execute on their behalf. Applications survive as invisible backend; the interface has collapsed. **Fundamental transformation.**

**The Nadella Line** — the boundary between the two worlds, formulated as a dividing question: *do your employees still open applications to do their work?* Yes → agentic world. No → agentive world.

**The agentive percentage** — operational crossing indicator: the fraction of tasks an employee can delegate entirely to an agent without opening an application. Bands: 0–20% agentic world · 20–50% approaching · 50–80% crossing · 80–100% agentive world. It complements IRIS/MOTOR (internal capabilities) by measuring **position** with respect to the transition; measured per function, not as a single average.

### The Data Value Pyramid

Four ascending layers: **DATA** (raw records in systems) → **INFORMATION** (data with context and structure) → **KNOWLEDGE** (analysis, patterns, understanding) → **ACTION** (governed autonomous execution). The industry invested decades in the two lower layers; the information→knowledge leap is painfully slow and the knowledge→action leap practically nonexistent — not because of the technology but because **there are humans in the middle**.

### Online enterprise vs real-time enterprise

- **Online enterprise**: it *accesses* — up-to-date data, current dashboards — but depends on a human looking, interpreting, and deciding.
- **Real-time enterprise**: it *reacts* — detects, interprets, decides, and acts continuously and autonomously.

### The Quantum Leap

The collapse of the cost of an analytical question **from weeks to seconds**. It dissolves the rationing of questions: analytical capacity becomes elastic, iteration replaces specification, the questions that were never asked get asked. It is the enabling condition for everything else and the boundary between foundations and the real-time enterprise (in IRIS: the 4→5 leap).

### The continuous-intelligence cycle

The classic cycle (Descriptive → Diagnostic → Predictive → Prescriptive → human decides) is linear and human-dependent. The new cycle is continuous, agent-executed, and human-governed:

```
Perceive → Interpret → Decide → Act → Learn ─┐
   ▲                                         │
   └─────────────────────────────────────────┘
```

The critical change: the step from recommendation to action no longer waits for a human — an agent executes, monitors the outcome, and adjusts, within governed limits.

### Three axes of deep change

1. **From consuming information to governing agents** — people move from consuming dashboards to designing rules and supervising autonomous systems.
2. **From architecture for humans to architecture for agents** — semantic layers where agents reason, knowledge graphs, real-time flows; data quality = actionability, not just cleanliness.
3. **From access governance to autonomy governance** — the question stops being "who can see which data" and becomes "what can an agent do, under what conditions, with what traceability."

### Evolutionary coexistence

AURA's fundamental principle: **each stage/level does not invalidate the previous one — it subsumes it.** The data warehouse does not die: it integrates as a source agents consume. The online enterprise does not disappear: it becomes the foundation of the real-time enterprise. The transformation is a hybrid model where the proportion changes, not a demolition.

---

## 3 · IRIS — the KNOWING axis

**IRIS (Organizational Intelligence Maturity Model)** measures an organization's trajectory from fragmented data to a self-managed intelligence ecosystem, in **10 stages** grouped into **5 levels**. It is a **diagnostic** model: it assesses which stage the organization is in and what that means; it does not prescribe what to implement.

### The 10 stages

| # | Stage | One sentence | Diagnostic question |
|---|---|---|---|
| 1 | **Fragmented** | Scattered, disconnected data | *If I ask two people from different areas for the same indicator, will I get the same number?* |
| 2 | **Systematized** | Orderly capture in defined systems | *Is there a defined system for capturing the business's key transactions, with consistent recording rules?* |
| 3 | **Centralized** | Central repository with classic BI | *Is there a centralized data warehouse with dashboards that business users consult regularly?* |
| 4 | **Modeled** | Semantic layer and governed definitions | *Do the business's key metrics have a single, governed definition shared by the whole organization?* |
| 5 | **Accessible** | Free access on demand · start of the real-time enterprise | *Can a manager get an analytical answer that was not pre-built into a dashboard, in minutes instead of weeks?* |
| 6 | **Contextual** | Contextual, adaptive information | *Can the system cross sources and enrich an answer with relevant context the user did not explicitly request?* |
| 7 | **Proactive** | Information seeks out the user | *Do business owners receive relevant information before asking for it, with enough context to act?* |
| 8 | **Bidirectional** | Governed autonomous action | *Are there agents executing operational actions autonomously with traceability, within rules that humans define and supervise?* |
| 9 | **Coordinated** | Cross-domain coordination | *Do agents from different business areas communicate with each other to coordinate actions with consistent information?* |
| 10 | **Orchestrated** | Self-managed ecosystem · full real-time enterprise | *Does the information ecosystem evolve autonomously — identifying gaps, improving models, and optimizing flows — with human supervision only at the strategic level?* |

### The 5 levels and the mapping to the Pyramid

| Level | Stages | Pyramid layer | Trajectory |
|---|---|---|---|
| **I · Foundational** | 1–2 | DATA | Foundations (online enterprise) |
| **II · Structured** | 3–4 | INFORMATION | Foundations (online enterprise) |
| **III · Dynamic** | 5–6 | KNOWLEDGE | Real-time enterprise |
| **IV · Active** | 7–8 | ACTION | Real-time enterprise |
| **V · Intelligent** | 9–10 | ACTION | Real-time enterprise |

**The Quantum Leap is the 4→5 leap** — the boundary between foundations and the real-time enterprise. The level boundaries are the leaps 2→3, 4→5, 6→7, and 8→9. The three leaps of greatest magnitude (Medium-High) are 4→5 (democratization of access), 7→8 (autonomous action), and 9→10 (self-management of the ecosystem).

### The 6 assessment dimensions

Data & Architecture · Analytical Capabilities · People & Culture · Governance · Operating Model · Business Value. An organization can be at different stages depending on the dimension.

### Rules of use (MUST)

- **The overall stage is set by the lowest dimension** — it is the real bottleneck.
- **Do not skip stages**: evolutionary coexistence requires building on the previous stage. Reaching Stage 7 without the semantic layer of Stage 4 produces unreliable agents.
- For executive communication use the 5 levels; for tactical diagnosis, the 10 stages. The first strategic diagnosis is: which side of the Quantum Leap is the organization on?

---

## 4 · MOTOR — the DOING axis

**MOTOR (Organizational Automation Maturity Model)** measures the degree of process automation in **7 levels**. Its fundamental question: **who executes the work in your organization — humans, assisted humans, or autonomous agents?** It is diagnostic, not prescriptive.

### The 7 levels

| # | Level | Who executes | Diagnostic question |
|---|---|---|---|
| 1 | **Invisible** (Shadow AI) | Humans (AI is hidden risk) | *Do you know how many AI tools are used in the organization, who uses them, and what data is shared with them?* |
| 2 | **Trusted** | Humans with a governed copilot | *Do you have official AI tools with governance, audit trails, and sensitive-data protection in place?* |
| 3 | **Collaborator** | Humans delegate complete tasks; agents execute under approval | *Do employees delegate complete tasks to AI agents — defining the goal and receiving the result — instead of just asking for point assistance?* |
| 4 | **Analyst** | Agents 24/7; human only on exceptions (>95% autonomy) | *Do you have agents operating 24/7, coordinated with each other, consulting a digital model of the system, with human intervention only on exceptions?* |
| 5 | **Specialist** | Agents with proprietary prediction (moat) | *Do you have specialist agents able to predict events and simulate scenarios using proprietary data the competition cannot replicate?* |
| 6 | **Manager** | Agents manage teams, budgets, and resources | *Do you have agents with authority to assign work, manage budgets, or make management decisions backed by a digital model of the whole organization?* |
| 7 | **Authority** | Agents in strategic leadership, inter-organizational networks | *Do you have agents participating in strategic decisions with a digital model of the full ecosystem — competition, market, regulation — and long-horizon simulation of futures?* |

### Transition map (diagnostic signals, not prescriptions)

| Transition | Name | Nature of the change |
|---|---|---|
| 1→2 | **Trust Infrastructure** | From risk to governance |
| 2→3 | **Wingworking** | From assistance to delegation |
| 3→4 | **Agentic Infrastructure** + Descriptive DT | From delegation to autonomy |
| 4→5 | **Agent Marketplace** + Predictive DT | From generic to specialized |
| 5→6 | **Autonomous Organization** + Organizational DT | From capabilities to authority |
| 6→7 | **Social Agentic** + Ecosystem DT | From intra-org to ecosystem |

### Digital Twins as a diagnostic dimension

| Level | Type of Digital Twin | Answers |
|---|---|---|
| 1–3 | None exists | — |
| 4 | **Descriptive** (infrastructure/operations, real time) | what do I have? what is happening? — no prediction or simulation |
| 5 | **Predictive/Prescriptive** (technical domain; requires 5–10 years of proprietary data) | what is going to happen? what happens if I do X? |
| 6 | **Organizational** (people + finance + operations + interdependencies) | what impact does this decision have across the whole organization? |
| 7 | **Ecosystem** (org + competition + market + regulation) | what strategic opportunities exist? |

### Critical differentiators between adjacent levels

- **2 vs 3**: at Level 2 the AI assists *within* the human's task; at Level 3 it executes *the complete task* end-to-end (the human defines and validates).
- **3 vs 4**: Level 3 is a pre-defined workflow with human approval of every plan, with no digital model; Level 4 is dynamic autonomous decision-making on a Descriptive DT, 24/7.
- **4 vs 5**: Level 4 *reacts* to the current state (rules + analysis, no simulation); Level 5 *predicts and prepares* before the event (scenario simulation). Build vs Rent signal: what matters is having the predictive capability operating, not how it was obtained.
- **5 vs 6**: Level 5 is a technical-domain DT with proprietary capabilities; Level 6 is a DT of the WHOLE organization plus **organizational authority** (agents manage people and budgets).
- **6 vs 7**: Level 6 optimizes the existing organization (intra-org, 6–24 month horizon); Level 7 proposes changing the game (inter-org, 5–10 year horizon, M&A, new markets).

### Quick assessment (8 questions)

1. Complete inventory of AI tools? No → L1 · Yes with governance → L2+
2. Formal AI-usage policies with enforcement? No → L1 · Yes → L2+
3. Trust Infrastructure (tokenization, audit trails)? No → L1 · Yes → L2+
4. Do they delegate complete tasks end-to-end? No → L2 · Yes with fixed workflow → L3 · Yes with autonomy → L4+
5. Real-time Descriptive Digital Twin? No → L3 or lower · Yes → L4+
6. 24/7 agents with multi-agent coordination? No → L3 or lower · Yes → L4+
7. Specialist agents with prediction/simulation? No → L4 or lower · Yes with Predictive DT → L5+
8. Organizational or Ecosystem DT? No → L5 or lower · Organizational → L6 · Ecosystem → L7

### Rules of use (MUST)

- **Sequentiality**: levels cannot be skipped. Operating at Level 4 without Level 2's governance generates risk, not value.
- **The overall level is set by the lowest dimension** (same bottleneck rules as IRIS; dimensions: Infrastructure & Agents · Operational Autonomy · People & Culture · Governance · Digital Twins · Business Value).
- **Sweet Spot**: Level 4 (Analyst) maximizes the return/risk/investment balance and will be the competitive baseline toward 2030. The book's market-distribution estimates are referential.

---

## 5 · The diagnostic pair

IRIS and MOTOR are **orthogonal**: an organization can be high on one and low on the other. The four quadrants:

- **Knows everything, does it manually** (high IRIS, low MOTOR): impeccable dashboards, bottlenecked decisions.
- **Doesn't know, but automates blindly** (high MOTOR, low IRIS): speed without direction — the risk quadrant.
- **Doesn't know, doesn't do**: the starting point.
- **Knows everything and executes on its own**: the destination — the real-time enterprise governed by people.

**A complete AURA diagnosis has three components:** IRIS position + MOTOR position + Citizen/City/DUAL priority mix for the roadmap (§8).

---

## 6 · Data Canon — data governance (instrument of KNOWING)

**Thesis.** Data Mesh prescribed decentralizing data ownership by domain. Two forces erode that prescription, and a corporate-governance argument joins them: (1) the three failure modes Dehghani attributed to centralized architectures are **limits of human cognitive scale**, and the agentive era raises them by an order of magnitude; (2) **semantics is not invented: it is adopted** — mature industries externalized it into standards (SID/TM Forum, BIAN, ACORD, IFRS/IAS 41, GS1); where a standard exists, there is nothing local to distribute; (3) distributed ownership puts the definer of each figure in charge of how that figure is reported — an **agency risk** (Jensen & Meckling) that an internal-control framework (SOX/COSO spirit) would not tolerate. Over-determined conclusion: recentralization of the agency-critical core is *possible* (agentive era) and *required* (internal control).

**Data Canon** = Data Fabric with Mesh's *governance* principles, **anchored to a central canon**, operated by agents, accountable to the board.

### The three functions

| Function | Data Mesh | Data Canon |
|---|---|---|
| **Specification** (semantics, quality) | The domain | The **industry standard** (where one exists) + the **canon authority** (the agency-critical) + **federated groups** (non-sensitive proprietary core) |
| **Execution** (move, transform, conform) | The domain or the platform | The **agentive platform** |
| **Accountability** | The domain | The **board** (adopts standards) + the **canon authority** + the **federated groups** (gaps, assembly) |

Structural rule: **the area measured by a figure does not control how that figure is defined** (segregation of duties; preventive control, not detective).

### The two governance layers

- **The canon authority** — central, *thin*. It safeguards the canonical reporting semantics, the survivorship rules, the quality policy, and the calibration of the agentive system. It ratifies; it does not operate.
- **The federated conformance groups** — one per domain/layer, *lightweight*, each tied to its standards forum. They triage gaps, liaise with the forum, and model non-agency-critical proprietary data. Anything touching reporting figures goes up for ratification.

The federation is **anchored**: the anchoring prevents the agency problem; the federation prevents the center from becoming a "diva" (single point of dependency).

### The standard mosaic

The external semantic anchor varies by industry: telco/banking/insurance have a mature single model; a diversified conglomerate **assembles** its corporate standard in layers (accounting: IFRS/IAS 41/XBRL — strong; traceability: GS1 — strong; R&D: BrAPI/MIAPPE — good in its niche; field operations: partial; proprietary commercial core: no standard → defined by the canon + federated group).

### Architecture: the medallion stays at three floors

**Bronze** (faithful raws per source — legitimate exhaustive replication, "a dump by design") · **Silver** (conformed to the canonical model/standard mosaic) · **Gold** (**materialized, selective** data products). With an agentive semantic layer over Silver, **the default consumption is virtual**: the agent composes any canon-conformant view on the fly; a Gold mart is the cached form of a pattern that *earned* materialization (volume, external SLA, regulatory snapshot, feature store). Real time comes from Silver + agent, not from the number of marts.

### The quality policy (a single level, structural, board-grade)

| # | Guarantee | Covers |
|---|---|---|
| 1 | **Real time** | Freshness (target floor; phased materialization) |
| 2 | **Faithful to the source** | Accuracy/completeness not introduced by the platform (bounded by the source) |
| 3 | **Complete lineage** | Provenance/traceability — the audit trail |
| 4 | **Conformant to the standard (mosaic)** | Validity — binary, machine-verifiable |
| 5 | **Reconciled by survivorship rules** | Cross-system consistency; the golden record without the stakeholder's ad hoc judgment |

### Falsifiers (the thesis weakens if…)

Proprietary data turns out to be the bulk of the value, not the margin · gaps with the standard do not converge · agentive capabilities have a lower ceiling than assumed · "real time" is infeasible for critical sources · the control argument does not move the board. Designed to degrade gracefully: if an agentive capability underperforms, the fallback is human work in the federated groups, not the collapse of the model.

---

## 7 · Wingmap — agentive discovery (instrument of DOING)

**Definition.** A technique for agentive discovery of operational intelligence: an AI agent with **read** access to corporate digital channels (email, messaging, repositories, calendars, transactional systems) reconstructs, **with no interviews or workshops**, **two living, connected maps**: the process map (how the work is executed) and the information-flow graph (which data originates where, who transforms it, where it travels). It operates first in passive mode (observation) and, under conditions, in active mode (**Wingworking**: the user operates via the agent).

**Hypothesis (three chained components):** (1) actionable organizational intelligence is not obtained by asking — executors cannot articulate in the abstract what they execute in the concrete (tacit knowledge, saturated BAU, politically situated description); (2) it can be reconstructed by observing the digital traces the organization already generates; (3) the reconstruction must be **dual** — process *and* information flow.

### The six guiding principles

1. **Observation first, intervention later** — (observe → infer → validate), not (ask → write → validate).
2. **Two planes, not one** — omitting either of the two maps breaks the value proposition.
3. **Common traceability to evidence** — every claim cites the raw document it was inferred from; without traceability, the output is indistinguishable from a plausible hallucination.
4. **Distributed validation in operational roles** — the process ambassador validates processes; the operational data owner validates flows. Not a central committee.
5. **Passive mode before active** — active mode only in domains where passive mode has already proven value. Inverting the order produces abandonment.
6. **Produce substrate, not consume requirements** — the output is a persistent, validated model that multiple destinations consume (data specs, BPM, prompts for operational agents, briefings).

### The phases (MUST: sequential; pre-conditions are blocking)

- **Phase 0 — Pre-conditions** (blocking): executive sponsor with authority · bounded, consented scope · designated process ambassador · identified data owners · legal/compliance framework validated for the jurisdiction.
- **Phase 1 — Observation**: a minimum of 3 iterations of the slowest process's cycle AND never less than 2 weeks. Deliverable: coverage report.
- **Phase 2 — Inference**: 3–5 candidate process maps + 5–10 candidate cross-role flows, with traceable evidence and per-element confidence.
- **Phase 3 — Dual validation**: 60–90 min sessions; first-deployment thresholds: **70%** of process maps and **60%** of flows validated without major correction; if not reached in two iterations, diagnosis and sponsor decision.
- **Phase 4 — Maintenance**: the graphs live. Key metric: **graph latency** (latest relevant event ↔ current version) under the agreed threshold (typical: 24–72 h).
- **Phase 5 (optional) — Selective active mode**: produces a library of deterministic bots, governed with DevOps discipline.

### Zones of non-applicability (declare before deploying)

- **Processes outside the digital trace** (paper, in-person, informal WhatsApp): coverage drops — administrative 70–90%, commercial 40–60%, field <40%. Choose high-coverage pilots.
- **Low appetite for discovery**: authorizing observation is a political decision; without it the technique does not apply.
- **Privacy and compliance**: AI Act, GDPR and analogues, labor law on monitoring — specific legal counsel, informed consent, PII tokenization/redaction. Not optional, not post-hoc.
- **Human dependency shifts, it does not disappear**: the bottleneck moves from describing to validating (reduction factor 4–10×, not zero).
- **Technological maturity**: current inference rates are adequate for validatable hypotheses, not for autonomous production without supervision.

### Category distinctions

- **vs classic process mining**: extends it to the unstructured channels where the real process lives; adds the second graph (information flow) that ERP logs cannot capture.
- **vs traditional consulting**: replaces artisanal discovery (speed, cost, coverage, continuity — an order of magnitude); it does not replace strategic interpretation or the negotiation of change.
- **vs individual copilots**: a copilot operates one user's session; Wingmap operates the aggregated cross-role flow.
- **vs AI-builders**: they are agentive for building, pre-agentive for running; Wingmap is agentive for discovery and produces the substrate that runtime agents need.

---

## 8 · Use Cases — the portfolio (decision framework)

It answers the third question of the path: **what do we do first?** — with a structured portfolio, not a list of ad-hoc ideas.

### UC and VS

- **Use Case (UC)**: atomic block — a specific, bounded, *reusable* capability. It is described by what it does, why AI does it better, and what maturity it requires.
- **Value Solution (VS)**: strategic configuration — a set of integrated UCs that solve a complete business problem before a decision-maker (problem, solution, metrics, return).
- A **composition** relation: a UC can be sold alone (modular) or within a VS (integral). Both catalogs are living and linked (MUST: complete cross-references).

### The three classification dimensions

1. **Required maturity level** — the MOTOR level (and, depending on the case, the IRIS stage) the case presupposes. It anchors the portfolio to the diagnosis: cases at the current level = *quick wins*; one level up = *sweet spot* (the reachable frontier); several levels up = declared vision, not commitment.
2. **Beneficiary of the impact** — Citizen / City / DUAL (below).
3. **Business domain** — thematic segmentation to filter the offering in seconds against the decision-maker's focus.

### The Citizen / City / DUAL framework

| Classification | Who perceives the benefit | Strategic function |
|---|---|---|
| **CITIZEN** | The external audience (citizen, customer, user) | Visible support, legitimacy |
| **CITY** | The internal audience (the organization) | Efficiency, compliance, sustainability |
| **DUAL** | Both | Consensus: every actor gets their visible win |

It was born in local government but is generic (banking: customer/compliance; healthcare: patient/clinical teams; telco: subscriber/network operations). It is transversal to IRIS and MOTOR: it classifies by beneficiary, not by axis.

**Two canonical strategies:** **Citizen-First** (visibility and legitimacy first; pool = CITIZEN + DUAL; risk: diffuse ROI) and **City-First** (efficiency and internal relief first; pool = CITY + DUAL; risk: the benefit is not perceived outside). **DUAL cases are the common core** — the most expensive currency in the portfolio: they are scarce and *are designed*. The strategy is chosen by context, not by ideology; the framework prioritizes *within* each maturity level, it does not replace the trajectory.

### The ROI discipline (MUST)

1. Every estimated ROI is declared **referential** — visibly, with no hidden asterisk — until a validated baseline exists.
2. **Social value** is separated from financial return and defended on its own terms.
3. **The baseline is validated** before declaring return (independent validation protocol).

### How to use this framework

1. Diagnose first (IRIS position + MOTOR position) — without this the portfolio has no anchor.
2. Inventory with the three dimensions — what cannot be classified is not sufficiently defined.
3. Separate UCs from VSs, with complete cross-references.
4. Choose the strategy by context (an explicit leadership decision, revisable, DUAL up front).
5. Attack the current level + 1 (quick wins for momentum; sweet spot for traction).
6. Declare ROI honestly.

---

## 9 · Canonical glossary (alphabetical)

- **Agency problem** — (Jensen & Meckling, 1976) structural conflict: whoever manages someone else's resources tends to present their management in the way that favors them most. The governance critique of Data Mesh derives from here.
- **Agent Marketplace** — ecosystem where agent capabilities are acquired or traded between organizations. Signal of the MOTOR 4→5 transition.
- **Agentic** — world of complementary agents; interfaces persist. Incremental evolution. It is the only sense of "agentic" in the book; the positive technological sense is always said *agentive* (Wingmap: agentive discovery, the agentive era, pre-agentive).
- **Agentic Infrastructure** — protocols and services that allow multiple agents to communicate, coordinate, and execute autonomously. Signal of the MOTOR 3→4 transition.
- **Agentive** — world where agents replace the interfaces; fundamental transformation. The book's central thesis lives on this horizon.
- **Agentive era** — state of the art in which AI systems autonomously execute schema mapping, entity resolution, transformation, and pipeline maintenance at a scale impracticable for human teams.
- **AURA** — Agentive Unified Reference Architecture: two diagnostic axes (IRIS · MOTOR) + instruments (Data Canon · Wingmap) + decision framework (Use Cases).
- **Autonomous Organization** — agents manage processes and people with objective metrics and simulation on the Organizational DT. Signal of the MOTOR 5→6 transition.
- **Autopilot** — autonomous 24/7 operation with human intervention only on exceptions. Defining characteristic of MOTOR Level 4.
- **BYOA (Bring Your Own Agent)** — MOTOR Level 1 pattern: each employee picks their own AI tool with no coordination.
- **Canon (the)** — central, non-discretionary body to which everything conforms: adopted standards + survivorship rules + quality policy. No domain can redefine it.
- **Canon authority (the)** — *thin* central body that safeguards the canon (reporting semantics, survivorship rules, quality policy, agentive calibration). It ratifies; it does not operate.
- **Citizen / City / DUAL** — classification by beneficiary of the impact: external audience / internal audience / both.
- **Data Canon** — data-governance pattern: Data Fabric + Mesh governance principles anchored to a central canon; semantics adopted from standards; board-grade quality policy; conformance federation by domain.
- **Data Fabric** — integration layer with active metadata, inferred transformation, and a semantic layer; the technical underpinning the agentive era amplifies.
- **Data Mesh** — Dehghani's pattern (2019–2022): domain ownership, data as a product, self-serve platform, federated governance. Data Canon does not refute it: it dates it.
- **Digital Twin (DT)** — synchronized digital model of a system, organization, or ecosystem. Transversal indicator of MOTOR maturity: **Descriptive** (L4) → **Predictive/Prescriptive** (L5) → **Organizational** (L6) → **Ecosystem** (L7).
- **Evolutionary coexistence** — each stage/level subsumes the previous one; prior infrastructure becomes foundation, not legacy.
- **Federated conformance groups** — network of lightweight groups, one per domain/layer, tied to their standards forum: gap triage, upstream liaison, modeling of non-agency-critical proprietary data.
- **Graph latency** — Wingmap maintenance metric: the temporal distance between the latest relevant observed event and the current version of the graph.
- **IRIS** — Organizational Intelligence Maturity Model: 10 stages, 5 levels, the KNOWING axis.
- **Medallion (Bronze/Silver/Gold)** — the three lakehouse zones: faithful raws · conformed to the canon · selective materialized products.
- **Moat** — sustainable competitive advantage; in MOTOR it emerges at Level 5 with proprietary data feeding prediction.
- **MOTOR** — Organizational Automation Maturity Model: 7 levels, the DOING axis.
- **Nadella Line (the)** — dividing question between the agentic and agentive worlds: *do your employees still open applications to do their work?*
- **Online enterprise** — accesses up-to-date information but depends on humans to interpret and act.
- **Organizational intelligence** — the capability to transform data into knowledge and action continuously and autonomously (all four layers of the Pyramid, not just the first two).
- **Quantum Leap (the)** — collapse of the cost of an analytical question from weeks to seconds. In IRIS, the 4→5 leap: the boundary between foundations and the real-time enterprise.
- **Quick Win** — use case with high visibility, low complexity, and fast ROI (typically <6 months); generates momentum in early transitions.
- **Real-time enterprise** — detects, interprets, decides, and acts continuously and autonomously, under human governance.
- **Shadow AI** — unmanaged AI use without governance, compliance, or visibility. Defining state of MOTOR Level 1.
- **Social Agentic** — ecosystem where agents from different organizations collaborate with verifiable identities. Signal of the MOTOR 6→7 transition.
- **Standard mosaic (the)** — the assembled corporate standard: external standards per layer + a proprietary model for the core no standards body covers.
- **Survivorship rules** — pre-specified rules (part of the canon) that decide which value prevails in the golden record when multiple sources disagree.
- **Sweet Spot** — the level where the return/risk/investment balance is maximized. In MOTOR: Level 4. In the portfolio: the current level + 1.
- **Trust Infrastructure** — trust technologies (tokenization, anti-prompt-injection, audit trails, automatic compliance) that make governed, auditable AI use possible. Signal of the MOTOR 1→2 transition. (Term shared with *AgencyDomains*, where it is the transversal axis of the architecture.)
- **Use Case (UC)** — atomic block of the portfolio: a specific, bounded, reusable capability.
- **Value Pyramid (the (Data) Value Pyramid)** — DATA → INFORMATION → KNOWLEDGE → ACTION.
- **Value Solution (VS)** — strategic configuration: integrated UCs that solve a complete business problem before a decision-maker.
- **Wingmap** — agentive discovery technique: two living, connected maps (process + information flow) reconstructed from digital traces, with no interviews.
- **Wingworking** — human-AI collaboration methodology (César Obach): the human as pilot (strategic decisions, validation), the agent as wingman (delegated tactical execution). Signal of the MOTOR 2→3 transition and the active mode of Wingmap.

---

## 10 · Relation to the trilogy

- ***AgencyDomains* — the architecture** (Book III of the map, published at agencydomains.org): the primitives, the layers, the Trust Infrastructure of the destination. It has its own canonical manifesto for agents; for architectural terms (AgencyDomain, Botlet, Capability, Facet), that manifesto rules.
- ***The Real-Time Enterprise* — the destination** (Book I): what the world looks like once the transition is behind us, told in its four faces — The Quantum Leap · Postchat · The General Staff · The Watch.
- ***AURA* — the path** (this book): where the organization stands, what trajectory lies ahead, in what order to travel it, and with what instruments.

Cross-reading rule: AURA diagnoses and prepares; AgencyDomains specifies the destination. An organization mature on both AURA axes ends up operating the architecture AgencyDomains describes.
