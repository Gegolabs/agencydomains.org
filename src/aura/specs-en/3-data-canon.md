# Data Canon

*Recentralized data governance in the agentive era*

<!-- libro
IRIS has just traced the trajectory of KNOWING, and its middle stages left a governance question pending: when agents — not people — are the ones consuming the data, who rules over it? This chapter answers it with a named pattern: Data Canon. It was born as a standalone paper and keeps that register — abstract, a two-part argument, falsifiers.
/libro -->

---

## Abstract

Data Mesh — formalized by Zhamak Dehghani between 2019 and 2022 — prescribes decentralizing data management by domain: distributed ownership, data as a product, self-serve platform, federated governance. This chapter argues that two contemporary forces erode the premise on which the decentralizing part of that prescription rests, and that a corporate-governance argument Data Mesh did not consider compounds them. First: the three failure modes Dehghani attributes to centralized architectures are, at bottom, limits of human cognitive scale — and the agentive era (schema mapping and entity resolution by language models, active metadata, inferred transformation, autonomous pipeline maintenance, a semantic layer over heterogeneous sources) raises that limit by an order of magnitude. Second: Data Mesh assumes that domain semantics is local and gets invented, when mature industries have produced shared information models — TM Forum's SID in telecommunications, BIAN in banking, ACORD in insurance, IFRS/IAS 41 in accounting — that externalize it; where a standard exists, there is nothing local to distribute. Third: distributed ownership puts the definer of each figure in charge of how that figure is reported — an agency risk that an internal-control framework (in the spirit of Sarbanes-Oxley / COSO) would not tolerate. What remains standing is the governance of accountability, but **recentralized — and federated under a central canon**: decision authority over what is **agency-critical** — what touches the figures by which management is reported — lives in the board (which adopts the standards and sets the quality policy) and in a thin *canon authority*; operational conformance, gap management, and the modeling of non-sensitive proprietary data are distributed across *federated groups by domain*, each tied to its standards forum. We call this pattern **Data Canon**. The chapter defines the pattern, positions it against prior work (Data Mesh, Data Fabric, lakehouse/medallion, MDM, industry information models, agency theory, internal-control frameworks), and states the falsifiers that would prove it wrong.

<!-- standalone -->
**Keywords:** Data Mesh · Data Fabric · data governance · agentic AI · data architecture · internal control · agency problem · industry information standards.
<!-- /standalone -->

---

## Introduction

Contemporary data platform roadmaps pursue, with increasing frequency, a "real-time enterprise": integrating all of the organization's applications and bringing all their data into a common platform for analytics, reporting, and AI. That direction — centralizing the ingestion of all sources — seems, at first sight, to contradict the decentralization Data Mesh prescribes. An intuitive formulation of the tension: *Data Mesh was the pragmatic solution to how to ingest data in the pre-agentive era; agentive technology makes it possible to do so in a centralized and automatic way, which renders the methodology dispensable.*

This chapter develops that intuition — corrects it where it is badly formulated, strengthens it where it is right, and carries it through to a named and bounded architectural pattern: **Data Canon**.

### Contribution

The contribution is threefold:

1. **A reframing of the Data Mesh argument.** The usual critiques of Data Mesh hold that it is complex or that organizations are not ready for it. This chapter offers a different one: Dehghani's three failure modes are limits of human cognitive scale disguised as an organizational problem — and therefore the decentralizing prescription was tied to a constraint the agentive era is releasing. It is not that Data Mesh is wrong: its premise expires.
2. **The "semantics is adopted, not invented" argument.** Dehghani's argument for domain ownership rests on an unstated assumption: that domain semantics is local and idiosyncratic. But mature industries externalized it into shared information models. The logical inference — if the standard exists, there is nothing local to distribute, and distributed ownership loses its raison d'être for those domains — does not appear to have been formulated in these terms.
3. **The critique from internal control.** Critiques of Data Mesh are technical or organizational. This one is corporate-governance: putting the domain in charge of defining *and reporting* its own figures makes the definer of the number the one reported on by it — a classic agency risk. Hence the turn: centralization (of what is agency-critical) ceases to be "the bureaucratic option" and becomes the structure an internal-control framework *would mandate*.

The pattern resulting from these three lines — and that overdetermines the recentralization (the agentive era *permits* it; control *demands* it) — is Data Canon. Its governance is not a central monolith: it is federated, but **anchored** to a central canon («Recentralized governance is federated — anchored to a central canon»).

### What does this chapter claim, and what does it not?

**It claims:** that the Data Mesh argument for decentralizing ownership rests on a premise that two contemporary forces erode; that what persists — accountability — gets recentralized at its agency-critical core and federated at its periphery, not eliminated; that this centralization of the core is preferable for internal-control reasons; that the resulting target architecture is Data Fabric with Mesh governance principles, upheld centrally in the canon and federatedly in conformance.

**It does not claim:** that Data Mesh was wrong (it solved a real problem with the tools of its time); that the agentive era solves every data-management problem (it solves one — cognitive scale — with large architectural consequences); that the recentralization is free (the canon authority and the federated groups are an organization with cost, risk, and permanence); that the platform is, by its architecture, compliant with a specific control regime (it provides the architectural precondition; effective controls still have to be designed and tested); that all the agentive capabilities assumed are available, mature, and reliable today (some are; others are trajectory — «Limits, risks, and falsifiability»).

---

## Background: Data Mesh and its rationale

Data Mesh was formalized by **Zhamak Dehghani** (ThoughtWorks) in three canonical texts: *How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh* (martinfowler.com, 2019), *Data Mesh Principles and Logical Architecture* (martinfowler.com, 2020), and *Data Mesh: Delivering Data-Driven Value at Scale* (O'Reilly, 2022).

### The three failure modes

Dehghani diagnoses three ways in which centralized architectures (data warehouse + monolithic data lake) fail at scale:

1. **Centralized, monolithic architecture that does not scale.** As sources proliferate, "the ability to consume it all and harmonize it in one place under the control of a single platform diminishes."
2. **Coupled pipeline decomposition.** Data platforms are decomposed by technical functions (ingestion, cleansing, aggregation) rather than by domains; "the whole pipeline is the smallest unit that must change to serve a new functionality" — a systemic bottleneck.
3. **Siloed, hyper-specialized ownership.** A central data team, disconnected from sources and consumers, lacks domain knowledge.

### The four principles

(i) Domain-oriented decentralized data ownership and architecture; (ii) data as a product; (iii) self-serve data infrastructure as a platform; (iv) federated computational governance.

### The declared rationale, and two silences

Dehghani articulates her motivation thus: "our aspiration to augment and improve every aspect of business with data demands a paradigm shift in how we manage data **at scale**". The operative word is *scale*. And there are two things Dehghani does not say. First: she does **not** say the problem is technological — lack of compute, insufficient tooling; she frames it as an organizational problem. But an organizational problem can be, in turn, a response to a human cognitive limit that becomes removable («The argument, part I»). Second: she does **not** weigh the agency risk her own design introduces by fusing the definer of the figure with the one reported on by it («The argument, part II»).

### Intermediate positions and their limits

The argument of this chapter settles out after discarding three intermediate positions:

| | Thesis | Why is it not enough? |
|---|---|---|
| **A** | The agentive era renders Data Mesh dispensable because it was a response to a pre-agentive technological limitation | Correct at its core (the problems Mesh solves are, at bottom, human) but a formulation that does not withstand contrast with the source: Dehghani does not pose a technological problem |
| **B** | The rationale of Data Mesh is organizational, not technological; the agentive era does not render it dispensable | A correct literal reading of Dehghani, but it underestimates that those organizational problems are, in turn, responses to human cognitive limits |
| **C** | Two planes: cognitive scale (the agentive era attenuates it) and governance (which persists, **distributed** by domain) | Real progress — it separates the absorbable from the non-absorbable — but it assumes governance has to be distributed by domain in the way Data Mesh distributes it; it considers neither external semantics, nor that the agency-critical core gets recentralized while the periphery gets federated in a different way |
| **D** | The agency-critical core of governance gets recentralized (semantics adopted from standards + structural board policy + a central canon); its periphery gets federated into domain groups tied to their standards forums. And the recentralization of the core is the structure a control framework would mandate | — *(this is the chapter's thesis; the pattern is called Data Canon)* |

---

## The argument, part I: distributing is no longer necessary

### The three failure modes are limits of human cognitive scale

| Failure identified by Dehghani | Why is it, at bottom, a human limit? |
|---|---|
| Centralization does not scale as sources proliferate | A limit on how many sources a human team can normalize, maintain, and harmonize |
| Pipelines coupled by technical functions, not by domains | A human cognitive limit on decomposing and orchestrating dynamically |
| A central team without domain knowledge | No human can be an expert in every domain simultaneously |

All three are limits of human cognitive scale. Data Mesh is the intelligent organizational response to that limit: if one processing unit cannot handle everything, divide the work among many units close to the knowledge — an application of Conway's law to the data problem. But the intelligence of that response is *contingent* on the limit. If the limit moves, the response stops being mandatory.

### The agentive era absorbs cognitive scale

"The agentive era" is not a magic invocation. It is a set of concrete capabilities, at varying degrees of maturity:

| Capability | What does it replace? | Current maturity |
|---|---|---|
| Schema mapping and entity resolution by language models | Hand-coded source→canonical mapping ETL and MDM (*master data management*, the master-record discipline) matching rules | High for bounded cases; degrades under genuine ambiguity |
| Active metadata / pipelines that self-adjust to *schema drift* | Manual maintenance when a source changes shape | Medium-high |
| Inferred transformation (deducing the transformation from examples / from the data contract) | Table-by-table transformation development | Medium; rising |
| Autonomous pipeline maintenance (monitoring, anomaly detection, self-repair) | The platform team that watches and fixes broken pipelines | Medium |
| Semantic layer over heterogeneous sources, including unstructured ones | "SQL as the interface" and the human curator who knows where everything is | Medium; it is the bet of current roadmaps |
| Generation of transformation code from requirements | The developer's role; leaves the team as "requirement modelers" who orchestrate development agents | Medium-high |

The aggregate effect: the processing unit that maintains N pipelines, discovers relationships, normalizes, and "knows" about M domains stops having N and M bounded by the headcount of a human team. Dehghani's three failure modes attenuate to the same degree that these capabilities work. The attenuation is not infinite: agents are reliable at *well-bounded* mapping, matching, and maintenance, and they degrade under genuine semantic ambiguity (when two mappings are equally defensible and one must *choose*) and in judgments that require business-strategy context. That residue does not evaporate; it is channeled through the federated governance of the section «Recentralized governance is federated — under the central canon».

### Domain semantics is not invented: it is adopted

When Dehghani argues that the domain must own the semantics of its data — what a "customer" is, what an "order" is —, she implicitly assumes that this semantics is *local*: that the organization builds it, that it is idiosyncratic, that this is why it pays to keep it close to whoever knows it. For most organizations in 2019–2022, that was a reasonable assumption.

But mature industries have produced **shared information models** that externalize semantics: TM Forum's **SID (Shared Information/Data Model)** in telecommunications (25 years of development; covering product, customer, service, resource, party); **BIAN** in banking; **ACORD** in insurance; and, cutting across every industry, **IFRS** defines accounting semantics, **XBRL** the structure of reporting, with an industry-specific standard for agriculture — **IAS 41 *Agriculture*** (biological assets, agricultural produce).

Where such a standard exists, **there is nothing local to distribute**. The meaning of "customer" is not what the commercial area prefers nor what finance prefers: it is what the standard defines. And shareholders do not want to be reported to according to an area's preference; they want to be reported to *according to the standard*. The supposed semantic contest between domains that Data Mesh resolves by giving the domain the floor dissolves by another route: there is an external, authoritative arbiter, and the organization decides to subordinate itself to it. That decision — "we report according to the industry standard, period" — is an act of governance, at board level, taken once.

Corollary: if semantics comes from outside (standard) and execution is absorbed by the agentive era («The agentive era absorbs cognitive scale»), the two functions Data Mesh fused into the domain — specifying and executing — leave the domain. What remains is the third: answering for it (see «The argument, part II» and «The Data Canon pattern»).

---

## The argument, part II: distributing is worse in governance terms

### Data Mesh structures the agency problem inward

The conflict at stake has a name in the theory of the firm: the **agency problem** (Jensen & Meckling, 1976) — managers (agents) manage resources belonging to shareholders (principals) and have an incentive to present their performance in the way that most favors them. A good part of the integrity scaffolding of financial reporting exists to contain it.

Data Mesh, without intending to, structures the problem inward. Its principles 1 and 2 (domain ownership, data as a product) put the domain in charge of defining the semantics, the quality, and the contracts of its data. That is: the person whose performance is measured by a figure comes to control how that figure is defined, calculated, and presented. The levers are concrete: choosing, between two equally defensible definitions, the one of "active customer" or "unit margin" that looks best; setting the data product's quality SLO (*service level objective* — the committed service level) low enough to avoid having to fix the embarrassing datum; designing the product contract to expose what helps and bury what does not. Even bounded by the global interoperability policies of the fourth principle, that discretion **is** the agency lever — because *the definer of the figure and the one reported on by it are the same party*. In internal-control language, that is a violation of segregation of duties.

It is not exactly an error of Dehghani's — it is a blind spot: she optimized effectiveness (closer to the knowledge = better data) and ignored control (independence of the reporting function from those reported on). For a company with shareholders, that second axis is not optional.

### Why doesn't "federated computational governance" close it?

The fourth principle of Data Mesh — federated computational governance — might seem to be the answer. It is not, *as Dehghani frames it*: it governs the *interoperability* between data products (global policies so they fit together, are discoverable, are addressable), not the *independence* of the reporting function; the federation that sets those policies includes the domains themselves (the fox helps write the rules of the henhouse); and a committee reviewing domain definitions *after the fact* would be a detective control, not a preventive one — the weaker of the two. Preventive control requires structural independence, not supervision: you do not bolt independence *on top of* a structure that fused the producer with the reported-on party; you have to design it *inside*. Data Canon preserves the federation principle — but **anchored** to a central canon that is indeed independent of the reported domain («Recentralized governance is federated — anchored to a central canon»): the federation conforms and manages gaps; the canon does not.

### The central-canon pattern as an internal-control environment

The recentralization of the agency-critical core neutralizes the agency problem not by adding supervision, but by its structure:

| Property of the pattern | What does it neutralize? | What control requirement does it amount to? |
|---|---|---|
| Reporting semantics in an external standard (IFRS / IAS 41 for the financial side) | No unit head can redefine "revenue," "biological asset," or "margin" — the definition is not theirs | The consistent, non-discretionary basis for the figures demanded by SOX §404 / the *Control Environment* component of COSO |
| Execution by the platform, faithful to source, with complete lineage | What goes up to the board is traceable to the transactional system, not curated by the domain | The *audit trail* §404 requires — and the condition for management to be able to certify honestly under SOX §302 |
| The **canon** (reporting semantics, survivorship rules, quality policy) is central and non-discretionary, in the custody of the *canon authority*; operational conformance and gap management are federated by domain | The one who defines how things are reported is independent of the one who operates | Segregation of duties: the domain *operates* (runs the transactional systems — the truth of what happened) and, via its federated group, *conforms and manages gaps* — but does not *define* the reporting semantics; that is set by the central canon. Any federated-group proposal touching reporting figures goes up to the canon authority for ratification (preventive control) |
| Pre-specified, auditable survivorship rules | Reconciliation decisions are verifiable rules, not ad hoc judgments by the interested party | Preventive rather than detective control |

Taken together: the pattern with its central canon is the structure an internal-control framework *would mandate* even if the agentive era did not exist. The direction of the implication matters — it is not that a control environment "tolerates" this architecture; it is that it would prescribe it. (Scope caveat: Sarbanes-Oxley literally applies to SEC registrants; it does not apply as such to a private company, but the principle is universal, almost every jurisdiction has analogues — corporate-liability regimes, rules of securities and insurance regulators, the internal-control requirements an external auditor evaluates when opining on financial statements under IFRS — and it is the first thing examined in an eventual IPO, capital raise, or M&A *due diligence*. The correct formulation: the pattern provides the *architectural precondition* of a control environment in the spirit of SOX / COSO, not "compliance.")

### The overdetermined recentralization

Joining the two lines: «The argument, part I» shows that distributing is no longer **necessary** (the agentive era removed the cognitive-scale constraint; semantics is adopted from external standards). «The argument, part II» shows that distributing the agency-critical core is, in addition, **worse** along the control axis Data Mesh did not weigh. Therefore the recentralization of that core is overdetermined: the agentive era *permits* it; the control of information for shareholders *demands* it. This also inverts the standard objection against centralization («The strong-Dehghani objection»): it is true that a recentralized monolith risks reintroducing the organizational bottleneck Dehghani pointed to — but in Data Canon what gets centralized is the *canon* (a thin, agency-critical core), not the whole governance operation; the latter is federated («Recentralized governance is federated — under the central canon»). This avoids at once the monolith's bottleneck and the dependence on a single "star" center; and the purely distributed alternative carries a *worse* risk — the agency risk — which the central canon does not have.

---

## The Data Canon pattern

**Data Canon** is the architecture and governance pattern that results from the two parts of the argument: distributing is no longer necessary, and distributing is worse in governance terms. The name comes from the *external, authoritative semantic anchor to which everything conforms*: a *canon* is something one adopts and abides by, not something one invents — and, by definition, what no one can redefine to their own convenience.

### The three functions — specification, execution, accountability

| Function | Traditional DWH | Canonical Data Mesh | Data Canon |
|---|---|---|---|
| **Specification** — defining the data, the semantics, the quality | Central team with domain input | The domain | The **industry standard** (where it exists); the **canon authority** (for reporting semantics and policy, agency-critical); the **federated groups by domain** (for modeling the non-sensitive proprietary core and for conformance) |
| **Execution** — moving, transforming, conforming | Central team | The domain or the self-serve platform | The **agentive platform** |
| **Accountability** — answering when something fails | Diffuse (central team by default) | The domain (explicit) | The **board** (via "we report according to the standard"); the **canon authority** (for reporting semantics and policy); the **federated groups** (for assembly, gaps, and the domain core) |

Data Mesh designs all three to fall on the domain, and that is why accountability naturally lands there. Data Canon breaks the coincidence: specification → outside (standard) and above (canon), with the non-sensitive fraction federated; execution → the machine; accountability → above (canon) and federated (groups). None ends up distributed by area *in the agency-problematic way*: the area measured by a figure does not control how that figure is defined. (The accountability of each transactional-system owner for the quality of the data *in their system* remains — but that is not a "data domain owner": it is the owner of an operational application, who exists with or without Data Mesh; the platform merely gives them visibility into what quality they contribute, via lineage.)

Accountability is the shadow of **decision authority**: whoever decides which semantics applies and what quality is demanded, answers for it. In Data Mesh that authority lives in the domain because semantics is local; in Data Canon reporting semantics is adopted from a standard and held in custody by the central canon, so the agency-critical authority lives in the board and the canon authority. Authority over the residue (ambiguous mappings, gaps, modeling of the non-sensitive proprietary core) is federated by domain, with the fraction that touches reporting figures reserved to the central canon («Recentralized governance is federated — anchored to a central canon»).

### Recentralized governance is federated — anchored to a central canon

The naive version of Data Canon would put everything in a single center of excellence. That is a mistake — and not for cognitive-scale reasons (the agents take care of that), but for a governance reason of another kind: a single all-powerful center becomes a single point of dependence. A CEO of a major telecommunications operator put it with memorable bluntness: centers of excellence *"tend to create divas the company starts depending on too much."* Key-person risk, bottleneck, capture risk.

That is why Data Canon distributes *operational* governance — but anchored. Two layers:

- **The canon authority** (thin, central). It holds in custody the agency-critical core: the canonical reporting semantics (what the board reports — IFRS/IAS 41 and whatever derives from it), the survivorship rules, the quality policy (authorized by the board), and the calibration of the agentive system (what the agent decides on its own, what it proposes for ratification, what is out of bounds). It *operates* nothing; it ratifies and maintains the canon. It is small precisely because it does almost no field work — the field work belongs to the agents and the federated groups.
- **The federated conformance groups** (one per domain / per layer). Each tied to its specialized standards forum: the finance group with the accounting standards body; the traceability group with GS1; the R&D group with the domain's scientific community; etc. They do: gap triage (a record does not fit the standard — what do we do, provisionally?), liaison with the forum (pushing the gap upstream so the standard closes it), and the modeling of their domain's *non-agency-critical* proprietary data. Anything agency-critical — anything touching reporting figures — they *propose* upward, to the canon authority, which *ratifies*. It is exactly the preventive-control pattern.

Why this does not break the argument:

- **It does not reintroduce the cognitive-scale burden.** The federated groups are *light* — they are liaison, triage, and proposal groups, not teams operating pipelines; the agents carry the bulk. The federation is small *per group* because the machine does the field work.
- **It does not reintroduce the agency problem.** Agency-critical decisions stay with the canon authority; the federation manages the periphery (conformance, gaps, forums) and the non-sensitive proprietary data; every proposal touching reporting semantics goes up for ratification — it does not go down to the area measured by the figure.

And this **truly honors the fourth principle of Data Mesh** — *federated computational governance* —, not just in name. Where Dehghani's federation was federated *all the way down* (each domain defines its own; a council coordinates interoperability), Data Canon's is federated *around a central canon*: the canon — reporting semantics plus policy — is non-negotiable and central; the federation conforms, manages gaps, and liaises with the forums. The federation does not float free; it is **anchored**. That anchoring is what keeps the federation from drifting into agency-problem territory (no domain can redefine "revenue"); and the federation is what keeps the center from becoming a diva.

A note on robustness: for the proprietary data that confers competitive advantage — which by definition no industry standard covers because it is not shared — the federated group of the corresponding domain carries its modeling, permanently. That part is not a light formality. But it remains *federated* (not concentrated in a single center) and *anchored* (whatever in that data affects reporting figures passes through the canon).

### The standard mosaic

The viability of Data Canon depends on the existence of an external semantic anchor — and where it exists varies by industry.

In **telco, banking, and insurance** there is a single mature model (SID/TM Forum; BIAN; ACORD), maintained by a body, covering the whole business: the pattern operates in its most favorable case; the federated groups only *adopt and map*; the internal semantic dispute is left without subject matter.

In a **diversified multi-vertical conglomerate** — consider, for instance, an agro-industrial group with agronomic production, genetic R&D, and commercialization across several countries — the anchor is a mosaic, uneven:

| Business layer | Authoritative external standard? | Maturity |
|---|---|---|
| Accounting / financial / consolidation | **Yes, strong** — IFRS; IAS 41 *Agriculture*; XBRL | Decades. Authoritative. It is what the board reports |
| Traceability / supply chain / product identification | **Yes, strong** — GS1 (GTIN, GLN, EPCIS) | Decades. De facto global |
| R&D / genetic breeding / phenotyping | **Yes, good within its niche** — BrAPI v2, MIAPPE 1.1, Crop Ontology, AGROVOC (FAO) | Mature within the scientific community; APIs and ontologies |
| Field operations / precision agriculture | **Partial** — AgGateway ADAPT Standard (Modus for soil labs) | Young; narrow focus |
| Commercial / operational core of the group as a business entity | **No** shared information model exists | — |

Telco produced a SID because it is a homogeneous industry — everyone sells connectivity and services over networks. A diversified group spans, within itself, several verticals; the very reason no "SID" exists for it is the reason it is hard to consolidate. Consequence: the corporate standard gets **assembled** — the federated groups adopt the external standards of their layer and, where there is no standard (the commercial/operational core), the canon authority defines the reporting semantics and the corresponding federated group the rest of the model. The structural thesis survives intact (what replaces distributed ownership is "external standards + central canon + light federated groups," and none of that gives back to the area measured by a figure the control over how that figure is defined); what does not survive is the naive version that would assume a mere formality suffices or that semantics comes whole from outside. For an important part — the core — it does not.

### The medallion stays at three floors — and the agent makes most consumption virtual

Data Canon **does not add a fourth storage layer**. The classic medallion stands:

| Layer | What is it? | Criterion for entry |
|---|---|---|
| **Bronze** | Raw landing by source — a faithful copy of the origin system | "I need it accessible." Replicating is legitimate even without a use case. Rule: if the datum lives in a transactional system, it goes to Bronze — nobody decides that |
| **Silver** | Data conformed to the unified canonical model (the standard mosaic) | "It has stable shape and agreed semantics." Binary, machine-verifiable conformance |
| **Gold** | **Materialized** data products — data marts (pre-built analytical subsets) | "It is a product that earned its materialization" — see below |

What changes with the agentive era is not the medallion's *structure* but *how it is consumed*. In the pre-agentive world, products were materialized in Gold because querying Silver directly was slow or hard; the mart was a *performance optimization*. With an **agentive semantic layer** over Silver, the agent composes any canon-conformant view **on the fly** — most consumption stops needing a pre-built mart. Two consequences:

- **Default consumption is virtual** — the agent composes the view the consumer asks for, in the canon's terms, over Silver, in real time. It is not a "fourth layer": it is the agent operating. The canonical definitions the agent applies — "margin by segment, by country, by quarter" and so on — are **part of the canon**, not a separate artifact: the agent *applies* them, it does not improvise them, and that is why two views requested by two different consumers are automatically coherent with each other.
- **Gold becomes selective for a reason, not by dogma** — a mart is materialized when the pattern *earns its freezing*: high volume, the SLA of an external system that depends on a stable physical interface, a regulatory snapshot that must be frozen, an ML feature store. A **Gold mart is the materialized/cached form of a query pattern the agentive layer would compose live** — the data equivalent of a materialized view relative to its logical view, with the property that if the mart goes stale or breaks, the system **recomputes from Silver** (the living definition is still there). The agent can materialize; the decision about *what is worth* materializing is governed by the business (use case, owner of each layer, contract — «Data products: who identifies them and who realizes them?»).

This resolves two frictions at once:

- **"Centralizing all the data is an absurdity contrary to Data Mesh"** — true for **Gold** (pushing 500 tables from an ERP up to Gold violates the four attributes of a product — use case, owner, contract, sustainable maintenance: most are auxiliary tables with no real consumer; no area answers for 500 tables; guaranteeing product quality for 500 tables is disproportionate; maintaining 500 unconsumed products is pure overhead — *when everything is a product, nothing is a product*); false for **Bronze**, a dumping ground *by design* — a faithful copy of the raw, source ingestion, not productization, and Mesh applies to the product layer, not the landing layer. The two sides of the debate are usually talking about different layers without naming them; the replication → federation trajectory that a modern roadmap declares mainly affects **Bronze** — Gold does not federate.
- **"Then how is one a real-time enterprise with a selective Gold?"** — real time is delivered by **Silver (conformed, in real time) + the agent composing over it**, not by the number of pre-built marts. Materialized Gold is the optimization exception; the living substrate is Silver-plus-agent. (And "real-time enterprise" in the strong sense — detecting, interpreting, deciding, and acting — is what the agent *does* on that substrate, not a property of storage.)

### The quality policy as a structural artifact

In Data Mesh, each product declares its quality and SLA, and the consumer decides whether it serves them — a recurring judgment ("is this data good enough for *this* use?") that someone close to the domain has to make; it is one of the anchors of distributed ownership. Data Canon dissolves it by inverting the framing: instead of levels per use case, **a single level — the strictest — for everything**, because that is what it means to be a real-time enterprise; the decision is taken once, at board level, and lives in the canon. The platform guarantees, for all data, with no per-use-case decision:

| # | Guarantee | Dimension covered | Why does it require no human judgment? |
|---|---|---|---|
| 1 | **Real time** | Freshness | The strictest setting possible; no use case can ask for more. A single level |
| 2 | **Faithful to source** | Accuracy and completeness (the part not introduced by the platform) | The value on the platform = the value at the origin at capture time. Binary, agent-verifiable |
| 3 | **Complete lineage** | Provenance / traceability | Every datum carries where it came from and when. It keeps point 2 honest; it is a platform capability, not a decision |
| 4 | **Conformant to the standard (mosaic)** | Validity / conformance | Every datum mapped to the canonical schema. Binary conformance, machine-checkable |
| 5 | **Reconciled by survivorship rules** | Cross-system consistency; uniqueness | When several sources describe the same canonical entity, a pre-specified rule (part of the canon) produces the golden record; the agent applies it. The residual ambiguity → the domain's federated group, which proposes to the canon authority if it touches reporting figures |

Points 3 and 5 are pieces the intuitive statement ("real time + faithful to source + conformant to the standard") does not name but the model needs: 5 is the classic *master data / golden record* problem, which dissolves because the standard provides the single canonical schema (there are not three definitions of "customer," there is one), the conformance step maps each source to that schema, and the survivorship rule decides the winner when values disagree — none of which asks the area measured by the figure to define the figure; it asks for one more artifact in the canon.

Two honest limits: **(A)** accuracy and completeness are bounded by the origin, not guaranteed by the platform — if the origin system has a datum wrong, the platform replicates it wrong, faithfully; improving it is an improvement project on the origin system, owned by that system's owner, who already exists, not a new domain owner. **(B)** "real time" is the *target* floor, realized progressively as each source's connectivity allows (batch legacies, third parties with daily drops); the policy is structural, its materialization is phased. Neither of the two reintroduces agency-problematic distributed ownership.

### Data products: who identifies them and who realizes them?

In Data Mesh, each domain is responsible for *identifying and realizing* the data products it shares with the rest of the company — the producer of the data is also its productizer, and that is what justifies distributed ownership. In Data Canon that responsibility decomposes, because there is no longer a single act of "productizing" but a chain with pieces in different places:

| Step | In Data Mesh | In Data Canon |
|---|---|---|
| **Identifying the need** | The domain owning the data decides what to productize for the others | **Demand** is born in the consumer — the unit that needs the view formulates it via its interlocutor — or it is raised by the **agent's pattern recognition** (push: "this pattern recurs; it is worth offering, or materializing"). The consumer and the source data can be in different domains; the agent bridges them |
| **Realizing the product** | The domain team operates a pipeline and builds a mart | The **agent** composes it — *live, virtual, by default* (in the canon's terms, over Silver). It is only *materialized to Gold* if the pattern earns its freezing («The medallion stays at three floors — and the agent makes most consumption virtual»). The domain does not operate a pipeline |
| **The product's semantics** | Set by the domain | Set by the **canon** — the view is composed of canonical definitions, not invented ones. Whatever touches reporting figures is ratified by the **canon authority**; the **federated groups** maintain the definitions catalog of their sub-tree |
| **The contract / the quality** | Negotiated by the domain with its consumers | The quality floor is already set by the canon («The quality policy as a structural artifact» — real time, faithful to source, lineage, conformant, reconciled): the view inherits it. The only product-specific part is the framing of the use case; the contract is, to a large extent, *derived*, not negotiated |
| **Answering if it is wrong** | The producing domain | It decomposes by layer, with complete lineage making the attribution mechanical: if the *origin* is wrong → the origin system's owner (who already exists); if the *semantics* is wrong → the canon authority; if the *use-case framing* is wrong → the consumer who requested it or the federated group that modeled it |
| **Discovering it** | Federated catalog (each domain publishes its own) | A single authoritative catalog — of canonical definitions (the virtual views) and of the Gold marts (the materialized ones), under the canon authority |

Thus Data Canon preserves the "data as a product" spirit of Data Mesh — the products exist, they are addressable, discoverable, with a contract and someone accountable for each layer — but without its coupling: the producer of the data does not have to be its productizer; *realizing* a product does not burden the domain (the agent does it); interoperability between products is not negotiated case by case, it comes out of the shared canon. The "domain's responsibility to identify and realize the shared products" survives only in its **identification** half — demand keeps being born close to whoever needs it, or the agent anticipates it — while **realization** is absorbed by the agent and **governance** (semantics, quality) is set by the canon.

---

## Implementation implications

**Architecture.** The right combination is **Data Fabric with Data Mesh governance principles, anchored to a central canon** — and that *is* Data Canon. The Fabric (powered by the agentive era: active metadata, inferred transformation, semantic layer) absorbs cognitive scale; the Mesh principles that persist are the governance ones (data as a product in Gold, selective; federated governance), but the federation is anchored to a central canon that holds the agency-critical core in custody. Where a program declared, in an early phase, plain "Data Mesh" and, in a later phase, "Data Fabric with Mesh principles," the difference is not an inconsistency to hide but a refinement.

**Organizational model.** The organization does not need to install data domain owners per area in the Data Mesh sense. It needs: a thin **canon authority** (the internal-control piece of «The central-canon pattern as an internal-control environment» — custodian of the reporting semantics, the survivorship rules, the quality policy, the calibration of the agents); light **federated conformance groups** per domain, each tied to its standards forum (gap triage, forum liaison, modeling of the non-sensitive proprietary core); and, at board level, deciding the quality floor and the real-time commitment, and the adoption of the industry-standards mosaic layer by layer, starting with the accounting/financial layer. What the business cannot delegate to technology is exactly this — and it is *less*, and better distributed, than the distributed discipline of Data Mesh would make one fear or than a monolithic CoE would risk.

**Change management.** If the organization only sustains anchored federated governance, the area ambassadors are not "domain owners in the making" but **interlocutors within their unit** — those who translate what matters to the local business into requirements that the federated groups and the agents execute, and, where appropriate, integrate their unit into the federated group of its layer. That lightens the training and focuses it on the business↔data translation, not on the technical administration of a domain.

**Board language.** The "cognitive scale vs. governance" distinction is sharp internally but it is not board language. Outward: *"Today's technology lets us bring in and order all of the group's data without spreading the plumbing work across every area. And it pays to do it this way for a control reason: when each area defines how its own numbers are reported, the numbers end up favoring whoever reports them; with the reporting semantics set by the industry's standards (accounting already has them, IFRS) and a complete record of where every datum comes from, that does not happen. We do not install a single all-powerful central team — that creates dangerous dependencies; we install a thin guardian of the standard and a network of domain groups that connect with the specialized forums. From the business we need a board decision: adopt those standards, staff that structure, and commit to operating in real time."*

---

## Limits, risks, and falsifiability

An argument that respects itself says what would prove it wrong.

### Falsifiers

| If it turns out that… | …then the thesis weakens like this |
|---|---|
| Proprietary / competitive-advantage data is the **bulk** of the value, not the margin | The federated groups that model it become heavy, and "anchored federated governance" is, in practice, almost indistinguishable from distributed Data Mesh — except that the central canon still bounds the reporting semantics. The thesis survives in form but loses its elegance |
| The volume of gaps (what does not fit the standard) **does not converge** — immature standard, slow forum, organization without upstream influence | The federated groups become a large, permanent apparatus; or, worse, the canon authority bloats to absorb them — the pre-Mesh monolith all over again. Viable only to the extent that the agents absorb the scale |
| Agentive capabilities have a **lower complexity ceiling** than assumed | The argument of «The agentive era absorbs cognitive scale» weakens; dividing the cognitive work becomes justified again (and the federation stops being able to stay light) |
| "Real time" is **infeasible** for critical sources | The policy defined in «The quality policy as a structural artifact» becomes aspirational for a part of the business; per-use-case levels reappear for that part |
| The control argument proves **insufficient to move the board** | The axis of «The argument, part II» loses practical traction, even if it remains valid |
| The **commercial/operational core** does have an emerging industry standard this analysis failed to detect | The thesis is *strengthened* (more external semantics, a thinner canon authority and thinner federated groups) |

### The strong-Dehghani objection

Even granting that the agentive era removes the *cognitive* limit, a recentralized structure may reintroduce the *organizational* limit Dehghani also pointed to: a single change queue, distance from the consumer, the domain waiting for the center to serve its requirement. Data Canon mitigates it by design: (a) agentive self-service shrinks the queue — the consumer describes what they need and the system produces it without going through a person; (b) the standard as contract reduces coordination — there is no semantics to negotiate, it is already set; (c) governance is federated, not monolithic — the "center" is a thin canon, not an all-powerful team, and conformance is carried by a group close to each domain; (d) the unit interlocutors shorten the distance. It is a mitigation, not a guarantee: the risk is real and worth monitoring. But the balance is not symmetric — the purely distributed alternative does not avoid this risk for free; it trades it for the agency risk («The argument, part II»), which is worse and harder to audit.

### Hype risk

Do not confuse "agents *can*" with "agents *do it well today*." Several capabilities of «The agentive era absorbs cognitive scale» are at medium maturity and rising fast — but "rising fast" is a bet, not an accomplished fact. The architecture must be designed to degrade gracefully: if an agentive capability underperforms, the fallback is human work in the federated groups (and, for the agency-critical part, in the canon authority), not the collapse of the model.

### What remains open

Is an agent's "emergent domain knowledge" equivalent to a human domain expert's, or is there a class of tacit judgment that does not transfer? Is there a third human plane beyond cognitive scale and governance — the "alignment with what matters to the business" — that neither the agentive era solves nor falls cleanly under "governance" (working hypothesis: it exists, and it is the unit interlocutor's role)? Is the replication → federation trajectory technically well-founded for each organization's concrete sources? What is the optimal split between the canon authority and the federated groups — how much of the proprietary-core modeling can be federated without reopening, through the window, the agency problem?

---

## Related work

- **Data Mesh** (Dehghani, 2019–2022) — the source this chapter revisits. Data Canon does not refute it: it dates it, and rescues its *governance* principles — data as a product, and *federated computational governance*, which Data Canon preserves but **anchored to a central canon** (the federation conforms and manages gaps; the canon — agency-critical — does not federate).
- **Data Fabric** — the current, associated with Gartner and several vendors, that emphasizes active metadata, inferred transformation, and a unified semantic layer. Data Canon adopts the Fabric as technical underpinning (the side the agentive era empowers) and complements it with anchored Mesh governance principles. The "Mesh vs. Fabric" debate predates this chapter; what the chapter contributes is the *reason* — cognitive scale absorbed by AI — and the connection to the control argument.
- **Lakehouse and medallion architecture** (the Inmon/Kimball lineage → data warehouse → data lake → lakehouse; Bronze/Silver/Gold popularized by industry practice) — Data Canon uses the medallion **without adding layers**, and makes it precise: Bronze absorbs exhaustive centralization; Gold stays selective because, with an agentive semantic layer, most consumption becomes virtual (the agent composes over Silver on the fly) — a Gold mart is the materialized/cached form of a pattern the agentive layer would compose live (materialized view vs. logical view), not a floor that keeps growing.
- **Master Data Management** — the classic golden record / survivorship discipline. Data Canon subsumes it: the canonical schema comes from the standard; the survivorship rules are part of the central canon; entity resolution is done by the agent, with the ambiguous residue in the domain's federated group.
- **Industry information models** — TM Forum SID / Open Digital Architecture (Frameworx) in telecommunications; BIAN in banking; ACORD in insurance; IFRS / IAS 41 / XBRL in accounting; GS1 in traceability; BrAPI / MIAPPE / Crop Ontology / AGROVOC in plant science. Data Canon elevates the observation "use industry standards" from implementation advice to *a premise that undercuts the distributed-ownership argument*.
- **Theory of the firm** (Jensen & Meckling, 1976) — the agency problem, from which the governance critique of «The argument, part II» is derived.
- **Internal-control frameworks** — Sarbanes-Oxley (§302 management certification; §404 assessment of internal control over financial reporting); COSO *Internal Control – Integrated Framework* (1992, updated 2013). Data Canon does not implement these frameworks; it shows that its structure — agency-critical central canon + federated conformance — is the architectural precondition of a control environment conformant to them.

---

## Conclusion

Data Mesh was not wrong. It solved a real problem — data complexity at scale overwhelmed any central team — with the tool of its time: dividing the cognitive work among many units close to the knowledge, aligning the architecture with the organization. Intelligent and contingent.

Two things changed the premise: the agentive era removed — to the extent that its capabilities perform — the cognitive limit that made dividing mandatory; and the maturity of industry information standards showed that domain semantics, which Data Mesh assumed local, is to a large extent adopted from outside. To that is added a fact Data Mesh did not weigh: distributing ownership leaves the definer of each figure in charge of the way that figure is reported — exactly the conflict internal-control frameworks would not tolerate. The recentralization of the agency-critical core is not merely possible: it is the right structure.

What persists — accountability — does not evaporate: it gets recentralized at its core and federated at its periphery. Authority over the reporting semantics and the quality policy lives above (the board and a thin canon authority); conformance, gap management, and the modeling of the non-sensitive proprietary core are distributed across federated groups by domain, each tied to its standards forum. That is governance — centralized where control demands it, federated where closeness to the domain helps, anchored in every case to a canon no domain can redefine. We call that pattern **Data Canon**: Data Fabric with Mesh governance principles, anchored to a central canon, operated by agents, accountable to the board. There is no need to take on the distributed discipline of Data Mesh nor to install a monolithic center of excellence; one must install the canon authority and the federated groups, adopt the standards mosaic, and decide — at board level — to be a real-time enterprise. And along the way, that structure *is* the foundation of internal control over the business's information — and it honors, this time for real, the federated computational governance Dehghani proposed.

<!-- standalone -->
---

## Acknowledgments

This chapter was developed in the context of a data-platform consulting practice, with AI assistance under the Wingworking collaborative methodology. Preliminary versions were submitted to critical discussion; whatever errors remain are the author's.
<!-- /standalone -->

---

## References

**Data Mesh:**
- Dehghani, Z. *How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh.* martinfowler.com, May 20, 2019.
- Dehghani, Z. *Data Mesh Principles and Logical Architecture.* martinfowler.com, December 3, 2020.
- Dehghani, Z. *Data Mesh: Delivering Data-Driven Value at Scale.* O'Reilly Media, 2022.

**Theory of the firm and internal control:**
- Jensen, M. C. & Meckling, W. H. *Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure.* Journal of Financial Economics, 3(4), 1976.
- Sarbanes-Oxley Act of 2002 (U.S.) — §302, §404.
- COSO. *Internal Control – Integrated Framework.* 1992 (updated 2013).

**Industry information standards:**
- TM Forum — *Information Framework (SID)* / *Open Digital Architecture (Frameworx).* https://www.tmforum.org/open-digital-architecture/information-framework-sid/
- BIAN — *Banking Industry Architecture Network.*
- ACORD — *Data and messaging standards for the insurance industry.*
- IFRS Foundation — *IAS 41 Agriculture*; the general IFRS framework; XBRL.
- GS1 — *Identification and traceability standards (GTIN, GLN, EPCIS).*
- AgGateway — *ADAPT Standard.* https://adaptstandard.org/
- *BrAPI (Breeding API) v2.* https://brapi.org/
- *MIAPPE 1.1 (Minimum Information About a Plant Phenotyping Experiment).* https://www.miappe.org/
- *Crop Ontology.* https://cropontology.org/
- *AGROVOC* (FAO) — multilingual agricultural vocabulary.

---

## Chapter glossary

| Term | Operative definition |
|---|---|
| **Data Mesh** | Data architecture pattern (Dehghani, 2019–2022): decentralized ownership by domain, data as a product, self-serve platform, federated governance |
| **Data Fabric** | Integration layer based on active metadata, inferred transformation, and a unified semantic layer; the technical underpinning of the architecture, empowered by the agentive era |
| **Data Canon** | The pattern proposed in this chapter: Data Fabric with Mesh *governance* principles, anchored to a central canon; reporting semantics adopted from industry standards; structural board-level quality policy; federated governance by domain (anchored to the canon) for conformance, gaps, and the proprietary core. The name comes from the *external, authoritative semantic anchor to which everything conforms* |
| **Agentive era** | The state of the art in which AI systems (language models + agent orchestration) autonomously execute schema mapping, entity resolution, transformation, pipeline maintenance, and data discovery at a scale impracticable for centralized human teams |
| **Medallion (Bronze/Silver/Gold)** | The three zones of the lakehouse: Bronze = faithful raw data by source; Silver = conformed to the canonical model; Gold = selective data products |
| **The canon** | The central, non-discretionary body to which everything conforms: the canonical reporting semantics (adopted industry standards + whatever derives from them), the survivorship rules, the quality policy. The canon authority holds it in custody; no domain can redefine it |
| **Canon authority** | The central, *thin* organ that holds the canon in custody: it ratifies and maintains the reporting semantics, the survivorship rules, and the quality policy, and calibrates the agentive system. It operates no pipelines; it does no field work. It is the internal-control piece independent of operations |
| **Federated conformance groups** | A network of groups, one per domain / layer, *light*, each tied to its specialized standards forum: they do gap triage, forum liaison (pushing the gap upstream), and the modeling of their domain's non-agency-critical proprietary data. Proposals touching reporting figures are escalated to the canon authority for ratification |
| **Survivorship rules** | The pre-specified rules (part of the canon) that decide, when several sources describe the same canonical entity with discrepant values, which value prevails in the golden record |
| **Agency problem** | (Jensen & Meckling, 1976.) The structural conflict of interest between managers (agents) and shareholders (principals): the former tend to present their performance in the way that most favors them |
| **Standard mosaic** | An organization's corporate standard: an assembly of external standards by layer plus a proprietary model for the core that no body covers |

---
