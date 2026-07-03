---
title: The Agentive World Trilogy — Unified manifest for agents
composition: The Real-Time Enterprise v0.4 · AURA v0.3 · AgencyDomains v0.5 (the three canonical manifests, in full)
license: GFDL v1.3 (proposed)
audience: agents that need the complete trilogy in a single document
precedence_rule: each part mirrors its human book; upon contradiction, the human book of the corresponding part wins
---

# The Agentive World Trilogy — Unified manifest for agents

> This document **assembles, in full and unedited**, the three canonical agent manifests of the Agentive World Trilogy. It is generated automatically from the per-book manifests — which are the source of truth for each part and are versioned with their book. Use it when you need to reason over the complete trilogy; use the individual manifest when working within a single volume.

## The transition (the frame the three parts share)

The transition that occupies the trilogy is a single one: from the world where people open applications to work, to the world where AI agents are the interface of work. The boundary is **the Nadella Line** — *do you still open applications to do your work?* — and the three volumes answer, in order, the three questions of that transition:

| Vol | Book | Question | Role | Audience |
|---|---|---|---|---|
| I | **The Real-Time Enterprise** — The Agentive World | Where are we going? | the destination | Managers, directors, and business owners, no technical background |
| II | **AURA** — The Agentive Path | Which way? | the route | Consultants and architects of the transformation |
| III | **AgencyDomains** — Agentive Architecture | How do we get there? | the vehicle | Architects and engineers who build or adopt |

**Vergis** (not a book: it's code) is the reference implementation, at <https://github.com/gegolabs/vergis>. The full trilogy lives at <https://agencydomains.org>.

## Shared canon (identical across the three parts; the owning book develops it)

| Term | One-line definition | Owning book |
|---|---|---|
| **Nadella Line** | The dividing question: do you still open applications to do your work? Yes → agentic world; no → agentive world | AgencyDomains (Ch 1); The Real-Time Enterprise presents it at vision level |
| **agentive / agentic** | Agentive = agents are the interface (transformation); agentic = copilots inside applications (incremental evolution). "Agentic" is never used in a positive-technological sense | AgencyDomains (Ch 1) · AURA (Introduction) |
| **Agentive World** (capitalized) | The paradigm as a proper noun; lowercase, the adjective | AgencyDomains (typographic convention, Ch 1) |
| **online enterprise / real-time enterprise** | Accesses up-to-date information but depends on humans to act / detects, interprets, decides, and acts continuously under governance | AURA (Introduction and IRIS) · AgencyDomains (Ch 2) |
| **continuous-intelligence cycle** | Perceive → Interpret → Decide → Act → Learn — the single canonical formulation across the trilogy | AURA (Introduction) |
| **Quantum Leap** | The collapse of the cost of the analytical question (weeks to seconds); boundary between the online and the real-time enterprise | AURA (Introduction; operational as IRIS leap 4→5) · AgencyDomains (Ch 2) |
| **agentive percentage** | Crossing indicator: fraction of tasks fully delegable to an agent without opening an application (0-20 agentic · 20-50 approaching · 50-80 crossing · 80-100 agentive; measured per function) | AURA (Introduction) |
| **Trust Infrastructure** | The five pillars (Governance · Audit · Validation · Resilience · Transparency) that separate pilots from production | AgencyDomains (Ch 5 §4 and Ch 8); MOTOR uses it as the 1→2 maturity threshold |
| **evolutionary coexistence / subsumption** | Each stage subsumes the previous one; the data warehouse does not die — it becomes a source agents consume | AURA · AgencyDomains (Ch 2) |
| **the three liberations** | From tools (flow), from channels (attention), from availability (time); the order cannot be skipped | The Real-Time Enterprise |
| **canon primitives** (seven) | AgencyDomain · Botlet · proto-Botlet · Capability · Trust Infrastructure · Assistant vs Autonomous Agent · Facet | AgencyDomains (Chs 4–5) |

**Conceptual ownership map:** The Real-Time Enterprise owns the portrait of the destination (the four faces — The Quantum Leap, Postchat, The General Staff, The Watch —, people as infrastructure, the attention budget, the M&Ms and the &, the agentive mode, the seven mechanisms, representation, the intelligent organization). AURA owns measurement and the route (IRIS, MOTOR, Data Canon, Wingmap, use cases, the agentive percentage). AgencyDomains owns the architecture (the four layers, the seven primitives, CRUDLEX, the market, Vergis). When in doubt about a shared term, the operative definition lives in the owning book.

## How to read this document

The three parts that follow are the **complete, verbatim** canonical manifests of each book, in trilogy order. Each part keeps its own frontmatter, its version, and its precedence rule ("the human book wins"). The `═══` separators mark the change of volume.
