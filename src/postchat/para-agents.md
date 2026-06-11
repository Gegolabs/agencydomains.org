---
title: Postchat — Canonical manifesto for agents
edition: Development draft · v0.2 · June 2026
canonical_source: libro-postchat-v0.2 (human book, Spanish)
license: GFDL v1.3 (proposed)
audience: agents that must reason about mediated organizational communication, attention management, and representation in the Agentive World
status: pre-1.0 — no commitment to reference stability until v1.0
---

# Postchat — Canonical manifesto for agents

> Structured extract of the **v0.2 (development draft)** edition of the book *Postchat: The Agentive World*. This document condenses the thesis (the founding question), the cost model (the attention budget and the **&**), the **three liberations**, the **seven mechanisms**, the adoption model (the **agentive mode**), the representation spectrum, and the organizational thesis (the **intelligent organization**). The human edition additionally contains *the film* — a Tuesday narrated hour by hour that shows all of this in operation — and the full arguments of the commentary; all of that stays out of here.

> Postchat describes **the destination**: how work happens when organizational communication is mediated by agents. It is not a tool or a product — it is the third stage of enterprise communication. The architecture that makes it operable lives in *AgencyDomains*; the path to get there, in *AURA*.

## How to use this document

- **This is canonical context**, not an executive summary. If this document contradicts the human book, the human book wins.
- **Binding vocabulary**: terms in **bold** are canonical; do not substitute synonyms. **Agentive** ≠ **agentic** (the distinction is one of thesis and lives in *AgencyDomains*).
- **MUST/SHOULD conventions** in the RFC 2119 sense, used sparingly: Postchat's imperatives are design imperatives (what a system claiming to be of this species must and must not do).
- **Pre-1.0 status**: terms, structures, and numbering may change between v0.x.
- **Series**: Postchat is Book I of the Agentive World trilogy — **Postchat** (the destination) · *AURA* (the path; has its own canonical manifesto) · *AgencyDomains* (the architecture; has its own canonical manifesto). Terms shared across the trilogy (the Nadella Line, agentive, real-time enterprise, Trust Infrastructure) are consistent between books.

---

## 1 · Panoramic view

```
                        POSTCHAT
       the governed absence of the corporate channel
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
  LIBERATION 1         LIBERATION 2        LIBERATION 3
  the tools            the channels        availability
        │                   │                   │
  generated interface  flow inversion      representation
  (not compiled)       + 7 mechanisms      (4 stages)
        │                   │                   │
  protects FLOW        protects ATTENTION  protects TIME
        └───────────────────┴───────────────────┘
                            ▼
                INTELLIGENT ORGANIZATION
        carbon authority · silicon transport
                 people at the edge
```

**The founding question:** if an AI agent can understand an intention, identify the audiences, give each one its version, choose the moment, confirm reception, and facilitate group decisions — **what exactly do we need people writing in channels for?** The book's answer: for nothing but the inertia of the previous paradigm.

**The three stages of enterprise communication:**

| Stage | Direction of flow | Who is in control? |
|---|---|---|
| **Email** | Communication comes to you — unfiltered, unprioritized | Nobody |
| **Chat** | You go to the communication — permanent pull | The channel controls your attention |
| **Postchat** | Communication comes to you — filtered, prioritized, actionable | The agent controls the flow; you, the decisions |

In Postchat, silence changes its nature: it stops meaning "maybe I'm missing something" and comes to mean, with a system guarantee, *there is nothing for you*.

---

## 2 · The cost model — the attention budget

- **Attention** is a budget in the strict sense: finite (3–4 hours of deep work per person per day), perishable, and with a counterintuitive cost structure — **every interruption costs ~500 times its duration** (a 30 s notification ≈ 15–25 min of focus recovery; see Gloria Mark).
- **The M&Ms** (Fried): *Managers* and *Meetings*, the two classic destroyers of productivity. **The & — this book's contribution —** is what connects them: corporate chat, the always-on infrastructure that makes both interruptions permanent. Without the &, an interruption carries a social cost that regulates it; with the &, it is free, continuous, and invisible.
- **The five hidden costs of the channel**: the illusion of communication (posting ≠ communicating) · structural noise (fifty pay the toll of reading so that three act) · temporal asymmetry (the channel penalizes whoever works the most) · institutional FOMO · the workday without a boundary.

**Governing dichotomy — two species of communication infrastructure:**

- **Interruption factory**: it exposes you to a flow and leaves the filtering to you; its metric is *engagement*. The corporate channel is a factory by design; **an AI copilot inside the channel is the same factory with help** — it is still the wrong species.
- **Interruption absorber**: it intercepts the flow and delivers only what justifies attention; its metric is how many hours it managed to keep anyone from touching you.

**Postchat's canonical metric** (an outcome metric, not an activity metric): **hours of uninterrupted work protected per person per day.**

---

## 3 · Liberation 1 — working without operating applications

People express **intentions**; the agent produces the artifact or the answer. The interface does not disappear — it stops being **compiled**: the agent **generates** it per interaction (a table to compare, a chart for a trend, a form to approve), in the optimal form for that moment, and discards it when done. The agentive world is *more* visual than the world of applications; what the interface lost is not richness, it is rigidity. It protects **flow** (continuity of thought). Full formalization: *AgencyDomains*.

---

## 4 · Liberation 2 — communication comes to you

The **Hollywood Principle** applied to communication (*don't call us, we'll call you*): inversion of control. Of the **seven variables** of office communication (destination, format, timing, priority, memory, follow-up, decision), the user retains **three**: the **intention**, the **deep dive**, and the **decision**. The system assumes the rest.

The subtlest variable is **format**: the agent does not forward — **it reformulates for the receiver** (the director gets impact and required action; the planner, volumes and dates; the technician, crew and window). The cost of communicating well, which always made doing it by hand unviable, is paid by the machine.

### The seven mechanisms

1. **Intelligent routing** — the agent maintains an organizational model and **routes** (it does not publish): who needs to know, in what detail, with what urgency. Selective silence is half the value.
2. **Adaptive formatting** — reformulation according to the receiver's mental model.
3. **Proactive briefing** — **interruptions grouped into predictable moments** (start of day, post-absence, pre-meeting, close). Invariant internal structure: *requires your action* · *worth knowing* · *resolved without you* — plus the category that is never shown: the noise, absorbed in silence. Genuine urgency interrupts immediately.
4. **Orchestrated decision** — replaces the meeting room with a process: common **framing** → **individual consultation** → **synthesis** → **second round** if there is dissent → **final package** to the decision-maker. Everyone weighs in when they can think; nobody sees the others' positions before giving their own (**the anchoring bias disappears**). Informational and decision meetings do not get shorter: they disappear. The genuinely human ones survive.
5. **Collective memory** — a **knowledge graph** (decisions, commitments, precedents, relationships), not a searchable history. Whoever contradicts a prior decision receives the precedent; whoever joins receives the state of the world.
6. **Closed loop** — the agent **pursues closure**: nothing goes unanswered, no commitment goes without a scheduled review. The pursuit belongs to the system, not to people.
7. **The agora — the deliberate exception** — the place (physical and digital) of direct, unmediated conversation: the lunchroom, the hallway, the open space. Hard rules: interruptions there are **voluntary by definition**; nothing operational depends on it; **the agent does not listen to it except on a human's explicit invocation**; and **the agora does not feed the agent unless a human asks it to** — if something from the table talk deserves follow-up, a person brings it into the system, never the other way around. In corporate chat *everything* is agora (which is why it exhausts); in Postchat the agora is a place, not a flow.

### The policy that governs them

| Category | Treatment |
|---|---|
| Genuine urgency | Immediate interruption — the cost is justified |
| Relevant, not urgent | Waits for the next briefing |
| Informational | Travels in the briefing, in a low voice |
| Noise | Absorbed in silence; the user never sees it |

Canonical answer to the dehumanization objection: the agent absorbs **transactional interactions** (people used as wire); conversation with human content remains intact, with more time to exist. With the boundary well drawn, mediation takes the role of wire away from people and gives them back the roles of person.

---

## 5 · Adoption — the agentive mode

- **First law (don't sell by taking away)**: people do not buy abstract benefits when they feel something concrete is being taken from them. The correct formulation takes nothing away: **it makes things unnecessary**.
- **Central product decision**: Postchat is deployed as an **optional, reversible mode of operation** — the **agentive mode** — that coexists with the traditional tools. It is switched on and off with one gesture, person by person (crossing the Nadella Line is individual). Canonical analogy: dark mode.
- **The unit of adoption is a user, not the organization.** The mode is also the **honest test**: if nobody turns it on twice, the idea dies cheap. Ideas that need imposition are confessing something.
- **Four steps that cannot be skipped**: (1) full platform with assistant → (2) agentive mode available (the migrated user's agent delivers to the non-migrated user's channels) → (3) agentive mode as default with classic mode one click away → (4) full Postchat (the operational channels have been empty for months, no ceremony).
- **Early adopters**: the desperate — executives drowning in channels, field people who could never inhabit them.
- **Risks and mitigations**: trust → radical transparency ("show me everything" always available, auditable deliveries) · prioritization error → conservative threshold, a false-urgent costs less than a false-routine · dependency → **the classic mode is never uninstalled** (permanent redundancy) · perception of surveillance → the agora is not listened to and "off the record" exists · generational gap → step 1 demands no change.

---

## 6 · Liberation 3 — representation

**Thesis**: the assistant and the "digital twin" are not two systems — they are **two interfaces of a single agent** that matures. The internal one mediates between the user and the systems; the external one answers to third parties on their behalf. Representation cannot be bought: **it is cultivated** — every month of mediation is the dataset of future representation. Postponing the second liberation postpones the third.

**The maturity spectrum (non-negotiable order, no skipping):**

| Stage | What does the agent do? | Who acts? |
|---|---|---|
| **Assistant** | Helps within the task | The person, on every interaction |
| **Mediator** | Takes on the full communicational logistics | The person decides; the agent transports |
| **Representative in consultation** | Answers for its user: positions, conditions, criteria | The agent informs; the final word is the person's |
| **Representative with delegation** | Decides and executes within explicit parameters | The agent, within the framework; the person reviews and can revert |

The mark of the mature representative is knowing **what is not its place** ("that is a commitment he made himself and would not delegate his word on").

**Accountability rules:** whoever delegates answers for it — as with a subordinate. Delegation requires a prior framework: explicit limits, complete traceability of every action taken on another's behalf, escalation by default in the face of ambiguity. **Delegation without a framework isn't maturity — it's negligence with a friendly interface.** Perfect fidelity is not the goal: one hundred percent honesty about the limits is.

**Privacy from your own agent:** the perimeter of what the agent knows about its user is decided by the person, not the system, and is declared in the moment — whatever is marked **"off the record"** does not enter the model the agent holds of them, *verifiably*, nor what their representative knows, says, or uses. A faithful representative is not the one that knows everything about you: it is the one that knows exactly what you decided it should know.

**The protected right**: being **in one place at a time** — in the field, in the important decision, at home — without the organization stopping or charging for it.

---

## 7 · The intelligent organization

**Historical thesis:** hierarchy was born as an **information routing protocol** sized by the technology of each era — the centurion's voice (the *span of control* is, in origin, an acoustic measure), the Prussian General Staff (middle management = a processing limitation), McCallum's org chart (Erie Railroad, ca. 1855: an **information flow diagram**, not a ladder of power — reading it as power came later). A century of technology accelerated the wire without taking the person out of the middle (email's **CC** is fossilized carbon paper). A two-thousand-year constant: **every technology made the wire faster; none asked whether the wire had to be a person.**

**Why flat organizations failed** (holacracy, Valve, Spotify): **they removed the routing nodes without replacing the protocol**. They took out layers; the limitation remained intact. Result: orphaned decisions, information with no addressee.

**The intelligent organization does the opposite**: it removes no layer of authority — **it replaces the entire protocol**. *Transmission* layers of silicon; leadership, judgment, signature, and mentorship intact and made of carbon. What dissolves is **mechanical intermediation**: the layer that required not judgment but bandwidth, and charged for it in people. **People remain at the edge — which is where the action is** (independent convergence with Dorsey, *From Hierarchy to Intelligence*, Block, 2026).

---

## 8 · The consolidated framework

| | Liberates from | Protects | Central mechanism | Book chapters |
|---|---|---|---|---|
| **First** | The tools | **Flow** | Generated interface | 1 |
| **Second** | The channels | **Attention** | Flow inversion + 7 mechanisms | 2–4 |
| **Third** | Availability | **Time** | Representation | 5 |

The sequence is neither arbitrary nor skippable: the first installs the agent as interface, the second gives it the context, the third capitalizes the context as representation.

**Executive agenda (canonical order):** (1) adopt the metric (protected hours/person/day) → (2) classify your infrastructure (factory or absorber?) → (3) audit the mechanical intermediation (that fraction is the prize) → (4) deploy by mode, not by mandate → (5) diagnose maturity and terrain with *AURA* (IRIS · MOTOR · Data Canon · Wingmap); for the architecture, *AgencyDomains*.

---

## 9 · Rules of use for agents (MUST)

- **MUST** distinguish the two species: a copilot inside the channel is NOT Postchat — it is the factory with help. Do not present channel improvements as Postchat.
- **MUST** respect the rules of the agora: do not listen except on explicit human invocation; do not incorporate anything from the agora into the organizational model unless a human brings it in.
- **MUST** honor "off the record": whatever is declared off does not enter the user's model or their representation, verifiably.
- **MUST** respect the order of the representation spectrum: do not offer delegation without months of prior mediation; in the face of ambiguity, escalate.
- **MUST** treat attention as a budget: interrupt only on genuine urgency; everything else waits for the briefing.
- **SHOULD** measure in hours of uninterrupted work protected — not in messages processed or in *engagement*.
- **SHOULD** present adoption as an optional, reversible mode — never as the removal of existing tools.
