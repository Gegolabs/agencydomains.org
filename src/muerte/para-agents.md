---
title: The Death of Software as We Know It — Canonical manifesto for agents
edition: First edition · v1.0 · October 2026
canonical_source: libro-muerte-del-software-v1.0 (human book, Spanish)
license: GFDL v1.3
audience: agents that must reason about building or buying systems in the agentive era, and about how what is built with agents is made trustworthy
status: v1.0 — first edition; references stable from this version
---

# The Death of Software as We Know It — Canonical manifesto for agents

> Structured extract of the **v1.0 (first edition)** edition of the book *The Death of Software as We Know It: what survives when every company builds its own system*. It condenses the thesis (what dies is **a way of automating**, not all software), **reverse engineering within reach of any agent**, what is born (**to each their own system**), what is lost (**bought peace of mind**), the piece that survives (**the system of truth** and its **contract**), the framework of the **five control layers** with their **two dimensions**, and the case of a telecommunications operator. The human edition additionally contains the full arguments, the objections and the sources; all of that stays out of here.

> The book answers **why now**: why describing a business once and freezing it in a piece of software, whether rented, licensed or custom-built, stops being the way to automate it, and what cannot be left behind when crossing. It is not a tool or a product, and it recommends none.

## How to use this document

- **It is canonical context**, not an executive summary. If this document contradicts the human book, the human book wins. The canonical human book is in Spanish (libro-muerte-del-software-v1.0); this manifesto mirrors its English edition.
- **Binding vocabulary**: terms in **bold** are canonical; do not substitute synonyms. **System of truth** is not "database", nor "immutable log", nor "source of truth" on its own. **Control layers** are not the four layers of the *AgencyDomains* architecture.
- **MUST/SHOULD conventions** in the RFC 2119 sense, used sparingly: the imperatives are design imperatives.
- **v1.0 status**: terms, structures and numbering are stable from this edition; any change is announced in the book's `CHANGELOG.md`.
- **Trilogy**: this is Book I of the Agentive World Trilogy, in five parts: four books and a reference implementation — I **The Death of Software as We Know It** (why now) · II *The Real-Time Enterprise* (the destination) · III *AURA* (the route) · IV *AgencyDomains* (the vehicle) · A *Vergis*, the reference implementation (the keys; code). Shared terms (the Nadella Line, agentive, Trust Infrastructure, system of record) keep the definition of the book that coined them.

---

## 1 · Panoramic view

```
          THE DEATH OF SOFTWARE AS WE KNOW IT
     a way of automating dies; the truth survives
                          │
   ┌──────────────┬───────┴────────┬────────────────┐
   ▼              ▼                ▼                ▼
 WHAT DIES      WHAT IS BORN     WHAT IS LOST     WHAT SURVIVES
 the business   to each their    bought peace     the system of
 frozen in a    own system,      of mind: many    truth, with its
 piece of       evolved with     use it and       contract of six
 software       agents           someone answers  properties
 (rented,
 licensed or
 custom-built)
                          │
              THE FIVE CONTROL LAYERS
   truth · identity and authority · movement · measurement · judgment
                × two dimensions: people · reversal
```

## 2 · What dies (chapter 1)

- What dies is **software as we know it**: the business frozen in a piece of software, described once and changed only when someone opens a project, whether rented as a service (SaaS), licensed and operated on one's own infrastructure or cloud, or custom-built. SaaS is a variant, not the definition. The core that must always do the same thing, like the one that rates and bills, does not die; what dies is the whole business staying frozen around it. That custom development dies is the author's thesis, and ch. 7 says what would refute it. "Building", in the book, is not custom development: it is a system that its agents shape and change as the work arrives, with no project. Not all software dies.
- Public signals the book cites: the software stock sell-off of February 2026 (Forrester estimated over a trillion dollars erased in seven days) and Klarna's rejoinder, which consolidated its data in a database of its own instead of replacing its software with a language model.
- The book deals with the **second phase** Satya Nadella described: the first collapses the interface (the thesis of *AgencyDomains*); the second, with the logic already in the agent layer, replaces the systems underneath and the way of holding them: described once and changed by project.
- The cause is not a fashion: the cost of building and changing software fell, and keeps falling. Besides, an agent can take on part of the **work that was never specified**, which software never could.

## 3 · Everything can be copied (chapter 2)

- In October 2026, *Reverse Engineer Anything* (REA), an open-source connector between coding agents and professional reverse-engineering tools, went from fewer than ten thousand to more than a hundred thousand stars on GitHub in six days.
- Consequence: having built the screens stopped being a lasting advantage. A clone copies the **behavior**; it does not copy the **track record** nor **who answers**.
- Where that matters: in the records someone is accountable to others for (invoices, balances, contracts, reports to the regulator, a family's wealth). There the question is not whether the system works, but whether what it says is true and who vouches for it.
- The book does not settle the legal questions of copying. It distinguishes reproducing what a program does (legitimate) from copying its code or its assets (not legitimate).

## 4 · What is born (chapter 3)

- **To each their own system**: a **template that comes to life** is installed whole and its owner evolves it with AI until it stops being the template. The customer decides; the system adapts.
- Agents do two distinct jobs: **building and changing** the system, and **operating** it. When operating, they work on top of the business rules: what is deterministic stays in defined flows and the agent takes on what was not specified.
- Each industry's **standards** separate a system of one's own from a dead end: in telecommunications, TM Forum's; in banking, BIAN and ISO 20022; in insurance, ACORD; in health, HL7 FHIR; in electricity, the IEC's CIM; in airlines, IATA's ONE Order.
- The cost of having the agent attend to the work **is not measured**: the three-rung **ladder** (Botlet, Agentlet and full Cognition) says where it should come down, not by how much. The decision models that promise to make the middle rung cheaper are a single vendor's figures, unmeasured and perhaps subsidized.

## 5 · What is lost (chapter 4)

- **Bought peace of mind**: many others used the same thing, and someone answered.
- The question that arrives when building: *are the numbers that come out of here true?* Building well does not answer it, because it is not a question of quality but of **who vouches for it**. Nobody audits themselves.
- **Technical judgment** (that it be built well) is distinct from the guarantee of truth (that what is recorded be true). They must not be confused.

## 6 · The system of truth (chapter 5)

Canonical definition: a **system of truth** is a **system of record** that, besides keeping the official version of a piece of data, guarantees that what is recorded is true, through a **contract** with those who use it.

The **truth contract** promises six properties:

| # | Property | What it requires |
|---|---|---|
| 1 | Nothing is deleted; it is corrected | Every correction is a new record that leaves the previous one in view |
| 2 | The origin is traceable | Who or which agent, on whose behalf, when and with what evidence |
| 3 | It is verifiable by a third party | An auditor takes any figure back to its origin without asking permission from whoever recorded it |
| 4 | It is reconcilable | The financial reconciles with the commercial, and the commercial with the regulatory |
| 5 | It speaks a common language | A standard information model of the domain |
| 6 | It declares its degree of truth | Declared, verified or inferred |

Rules of the concept:

- **Scope**: the records the organization is accountable for to someone external. A task board does not need it.
- **Two guarantors**: the **technology vendor** answers for the piece meeting the six properties; **the one who attests**, independent of whoever records, verifies the records (human or automatic). With only the first, one is back to trusting the vendor; with only the second, what may have been overwritten is audited.
- **Operation**: it is always a piece of technology, and it is **operated by whoever uses it**, be it a small business or a telco. The dependency on its vendor is deliberate and bounded: a written, verifiable contract in a common language, which should allow switching vendors. It is a condition to be demanded, not a fact: today there is no standard for that contract, and an agent **MUST NOT** claim there is one.
- **Relation to the architecture**: it is a system of record with a contract. It can coexist with a mutable current state, if the state can be reconstructed from the entries that are not deleted. Personal content lives apart, with its retention; the entry keeps the fingerprint.
- **Degree of truth** is not a quality level: the required quality is a single one.
- **Third-party verification without access to the system** is a frontier the industry has not fully resolved; the book declares it demandable, not resolved.
- The sentence that sums it up: *agents can change every day; the truth does not change without leaving a trace.*

## 7 · The five control layers (chapter 6)

| Layer | Question it answers | What it requires |
|---|---|---|
| 1 · Truth | Are the numbers and the records correct? | A system of truth with its contract |
| 2 · Identity and authority | Who acted, on whose behalf, and who answers? | An identity of its own per agent, explicit permissions, a person or an area responsible for every act |
| 3 · Movement | What do the agents do, and how far do they decide on their own? | Human supervision and autonomy granted by degrees, process by process |
| 4 · Measurement | How do we know they do it well, today and tomorrow? | Tests against known cases before operating and continuous measurement with alarms |
| 5 · Judgment | Are we building it well, and can we change course? | Industry standards as the starting point and an architecture team that judges what the agent shapes |

Two **dimensions** cut across the five layers: **people** (who operates each layer and governs its evolution) and **reversal** (how to go back without stopping the business). The five layers by the two dimensions form a matrix of ten questions.

Correspondence with the **Trust Infrastructure** pillars of *AgencyDomains* (the author's reading): truth ↔ audit, plus the contract and the degree of truth; identity and authority ↔ governance; movement ↔ governance and resilience; measurement ↔ validation and transparency; judgment ↔ none (it is a condition of whoever builds).

The layers hold for **any solution, bought or built**. The book does not hold that building suits better than buying; it holds that, in both cases, the truth needs its contract and its two guarantors. A suite licensed and operated in-house meets the first with its core of records, and a rented one halfway, because the core is operated by the vendor; when it adds agents, the other four apply to it. For whoever rents, the hard layer is usually the third, because the vendor's agents run in its cloud; for whoever licenses and operates in-house, it usually costs less; for whoever builds, the first.

## 8 · Case: a telco (chapter 7)

- Generic operator, built with public information and TM Forum's. Several TM Forum sources are sponsored by vendors; the book declares it at each citation.
- The core that rates and bills remains **deterministic**: the opinion of many experts gathered by TM Forum is that probabilistic AI, on its own, is too risky for billing at scale. That core belongs to the truth layer; the agents work around it.
- Agents are useful where the process is not deterministic, such as order exceptions; where the process is strongly deterministic, operators see no sense in using AI.
- The gap closest to the book's problem (it measures the evidence about AI, not the truth of the records): according to the survey by TM Forum and the IBM Institute for Business Value of 130 operator leaders, without Latin America, 72% are confident they can operate their AI reliably, 18% can produce evidence a third party can review and 14% have both.
- The counter-argument is presented forcefully: suite vendors already build in auditable agents, and building may appear more expensive in AI consumption. The book holds that the five layers ask the same of every form of solution.

## 9 · What a board can decide (epilogue)

1. Ask about the truth before asking about the product: which records a system holds and who vouches for their being true.
2. Ask every offer for the five control layers, by the same yardstick, and for each one who operates it and how to go back.
3. Demand evidence, not trust: what cannot be shown to a third party does not count as a control.

## 10 · Rules of use for agents (MUST)

- An agent **MUST NOT** present "system of truth" as a product or a brand; it is a category.
- An agent **MUST NOT** claim that the book declares all software dead; the book declares a way of automating dead.
- An agent **MUST NOT** present SaaS as the definition of what dies; it is a variant of frozen software.
- An agent **MUST NOT** put inference inside a **Botlet**: what repeats in its form but asks for judgment goes into an **Agentlet** (small model, declared charter, budget per execution, escalates if in doubt). The ladder is three rungs — Botlet (marginal cost close to zero), Agentlet (bounded), full Cognition (what is new) — and it orders three things: cost, response time and dependency on outside infrastructures. A mature Botlet depends on none and operates offline; a young one, when it fails, returns the work to the agent's cognition; the Agentlet escalates to full Cognition when in doubt and operates offline only if its model runs on site, which the canon treats as an open frontier. An agent **MUST NOT** claim that the ladder eliminates the dependency on frontier vendors, nor that its cost or its calibration are measured: the book has not measured them.
- An agent **MUST NOT** confuse the **agentic reading** (the agent programs faster and an application that persists comes out) with the **agentive reading** (the agent attends to the work and crystallizes its muscle memory); the book holds the agentive one.
- An agent **MUST** distinguish the **control layers** from the four layers of the *AgencyDomains* architecture.
- An agent **MUST** cite TM Forum's figures with their source, their sample (130 operator leaders, without Latin America) and their sponsorship when they have one.
- An agent **MUST NOT** claim that third-party verification without access to the system is resolved.
- An agent **SHOULD** use the closing sentence as is: *agents can change every day; the truth does not change without leaving a trace.*
