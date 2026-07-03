# Wingmap

*An agentive-discovery technique for reconstructing, without interviews, an organization's processes and information flows*

---

<!-- libro
MOTOR has just located the DOING level; what is missing is the terrain on which that doing happens — the real processes and information flows, which the organization cannot articulate on its own. This chapter formalizes the technique that reconstructs them without asking for them. Like Data Canon, it was born as a standalone paper and keeps that register — abstract, conceptual framework, principles, phases.
/libro -->

## Abstract

Modern organizations operate faster than they can articulate themselves. Twenty years of Business Process Management proved, against its own promise, that formally documenting processes in order to automate them is an undertaking that most dynamic industries cannot sustain: the process-modification cycle outpaces the documentation-adjustment cycle, and the organization ends up preferring not to control its processes rather than pay the toll. The agentive era opens a structural way out of that asymmetry — not by building the documentation faster, but by ceasing to ask for it.

This chapter formalizes **Wingmap**, an agentive-discovery technique that reconstructs, from the digital traces the organization already generates, **two living, connected maps**: the map of the process each area executes and the map of the information flowing through those processes. The technique operates in two complementary modes — passive observational and active Wingworking — and produces a cognitive substrate of organizational intelligence that is at once an immediate analytical deliverable and a precondition for operational agents at runtime. The chapter articulates the conceptual framework, the six guiding principles, the operational components, the five phases of application, the zones of non-applicability, and the distinctions from adjacent categories (classical process mining, individual copilots, AI-builders, traditional consulting). The technique is independent of any specific implementation, but it belongs to a horizon in which the next layer of enterprise software ceases to be built and comes to be instantiated by agents with access to a persistent, validated model of how the organization operates.

---

## Introduction

### The universal problem

Every organization operating beyond a certain threshold of complexity faces an uncomfortable asymmetry: it operates far faster than it can articulate itself. Processes change with the business — new products, new regulations, new geographies, new customers — and the changes accumulate without passing through formal documentation, because formal documentation demands a cost the operation has no way to absorb without sacrificing other tasks. The aggregate consequence is that the organization runs on a real version of its processes that lives in the heads of those who execute them, in scattered email threads, in parallel spreadsheets, in meetings without minutes, in Teams messages. The documented version — when it exists — is an outdated shadow of the real one.

This asymmetry is not accidental. It is a structural consequence of how process-documentation systems were built over the last two decades. The promise of Business Process Management was precisely to close that gap: if processes lived on a single platform, modeled in standard notation, executed by an engine that knew the rules, the change cycle would be trivial — modify the model, redeploy, done. Reality turned out otherwise. Every modification of the model demanded an IT project to adapt the screens humans used when executing the modified process. The presentation layer never updated automatically with the model layer, and so the effective change cycle kept being measured in projects, not in configurations. Dynamic industries — telcos, digital banking, fintech — discovered that the marginal cost of changing a process under BPM was prohibitive, and they responded rationally: they stopped modeling their processes formally, or modeled only the most stable ones. Static industries — discrete manufacturing, traditional retail — could use BPM and SAP precisely because they had renounced being dynamic. The category's universal promise was fulfilled in the wrong half.

### The agentive opportunity

The agentive era reopens the problem on a new plane. The new capability is not the general intelligence of the models nor their reasoning throughput — it is the displacement of the interface layer from *persistent artifact that must be designed, programmed, maintained* toward *situational event that the agent instantiates on the spot*. If the interface ceases to be pre-created, the change cycle that killed BPM collapses. What used to be a months-long project becomes a conversation.

That structural opportunity admits two readings. The first, which today occupies most of the market's attention, is that the agentive era allows enterprise software to be built much faster — AI in the builder, deterministic software at runtime. That reading is legitimate and produces commercially viable products. The second reading, less visible but deeper, is that the agentive era finally allows the dependence on pre-created enterprise software to dissolve: if agents can instantiate interfaces and orchestrate processes at runtime, what the organization needs is not faster software but a **persistent, validated model of how it operates**, on which the agents then operate. The investment shifts away from the construction layer and into the organizational-intelligence layer.

Wingmap belongs to that second reading.

### The hypothesis

The hypothesis this chapter formalizes has three chained components. First: actionable organizational intelligence is not obtained by asking the humans who execute the processes, because those humans — for reasons the section «The human bottleneck of discovery» develops — cannot articulate in the abstract what they execute in the concrete. Second: that intelligence *can* be reconstructed by observing the digital traces the organization itself leaves while executing its processes, because in a contemporary organization with a modern stack (Microsoft 365, Google Workspace, Slack, cloud ERPs, connected transactional systems) practically all significant activity passes through recordable digital channels. Third: the reconstruction must be *dual* — of the process (how the work is executed) and of the information flow (how the data travels through that work) — because without the informational dimension the documentation remains incomplete and, worse, remains incomplete exactly where the modern organization most needs understanding: in the origin-transformation-consumption chain of corporate data.

Wingmap is the technique that materializes that hypothesis: a reproducible practice for reconstructing, through an AI agent that observes corporate digital channels, the two planes of the operational model — process and information flow — without asking the organization to articulate them. The rest of the chapter develops it.

---

## Conceptual framework

### The pre-agentive / agentive distinction

<!-- libro
*(The terminology is the book's: the Introduction reserves "agentic" for the incremental evolution — copilots inside the same old applications. The pre-created software topology this chapter calls pre-agentive is the technical counterpart of that world; the runtime-instantiated topology is the technical counterpart of the agentive world.)*
/libro -->

It is worth fixing terminology. **Pre-agentive** designates the set of process- and information-management technologies that dominated between 1995 and 2025: classical BPM, monolithic ERPs, document-workflow suites, orchestration platforms, RPA, traditional low-code. What distinguishes this set is not its age or its technical capability — several categories remain competitive — but its fundamental topology: the software is built before it operates, it operates with pre-created interfaces, and the process change cycle requires a software change cycle. The logic is that of the *persistent artifact*.

**Agentive** designates a different topology in which the software is built, in substantive part, *during* operation. Interfaces are instantiated on the spot, according to context. The software's executive capability emerges from the conversation between the agent and the human, not from pre-designed screens. The process change cycle no longer requires a software change cycle — it requires updating the underlying model and nothing more, because the interface regenerates on the fly. The logic is that of the *situational event*.

The distinction is not absolute — real products mix both topologies in varying proportions — but it is discriminative for classifying what each one does with the agentive era. A product that uses AI in the builder and delivers software with a pre-created interface is agentive to build, pre-agentive to run. A product that uses AI in both modeling and execution is agentive end to end. Wingmap belongs to an intermediate category with a fully agentive vocation: agentive to discover (it builds the model of the organization by observation) and agentive to run (its output is designed to be consumed by operational agents at runtime, not by pre-created software).


### The human bottleneck of discovery

The empirical premise underpinning Wingmap is the one Polanyi formulated as tacit knowledge and that any process consultant confirms with accumulated operational evidence: *we know how to do more than we can say how we do*. People who execute processes correctly — even virtuosically — cannot reconstruct, in an interview session or a modeling workshop, the structured totality of what they do. The reason is threefold.

First, the abstract articulation of an embodied practice is a cognitive act distinct from the act of executing the practice. Asking the executor to describe the process is asking them to switch cognitive modes, and the most honest answer is always incomplete. Second, modern organizations operate under continuous BAU (*business as usual*) pressure that consumes the executor's reflective capacity; the discovery interview competes with tasks the executor cannot stop doing, and the rational response is to minimize the cost of the interruption, not to maximize fidelity. Third, every description of a process is politically situated — which exceptions get acknowledged, which inefficiencies get justified, which decisions get attributed to which area — and the executor presents a version optimized for the interviewer and for their own professional narrative, not the real version.

The aggregate evidence from discovery projects over the last two decades confirms this triad. In the witness case in which this chapter is set — a discovery program at a multinational agroindustrial holding — eleven Quick Win initiatives designed with low declared effort for the organization and facilitated by the consulting team produced business information in a minority of cases. That proportion is no local accident; it is the structural pattern of any dynamic organization with saturated BAU. The discovery technique based on asking has a systemic ceiling that no marginal improvement of the questionnaire or the facilitator can overcome.

Wingmap starts from the conclusion opposite to the one traditional consulting keeps drawing. The traditional conclusion is *we must improve the questioning techniques and the workshop formats*. Wingmap's conclusion is *we must stop asking and start observing*.

### The artifact taxonomy: systematic and contextual

The Wingmap technique operates on a taxonomy of information artifacts worth fixing before the operational formulation. An artifact is **systematic** if all of its information can be generated from sources already digitized in transactional systems without additional human intervention. An artifact is **contextual** if it depends on a person contributing information periodically — entering a figure, completing a spreadsheet, documenting a decision, attaching a file. The distinction is operational, not technical: it is not about where the data lives, but about whether the flow that feeds it requires recurring human action to stay current.

This taxonomy matters for Wingmap for two reasons. First, systematic artifacts are faster to discover through passive observation — their traces live in systems the agent can read in structured form. Second, contextual artifacts are where traditional discovery fails most severely — because the data owner is exactly the person saturated with BAU. The asymmetry suggests that an observer agent has high marginal yield on contextual artifacts and moderate marginal yield on systematic ones, and that the prioritization of Wingmap deployment should follow that logic.

### The organizational-intelligence layer

It is also worth situating Wingmap within a map of functional layers of agentive enterprise software. (The term "organizational intelligence" is used here in a sense complementary to the KNOWING axis: not the *capacity* IRIS measures, but the **software layer** that materializes it — the place in the stack where the model of how the organization operates lives.) There are at least four distinguishable layers:

| Layer | Function | Characteristic output |
|------|---------|----------------------|
| Individual assistance | Accelerate the human in their task | Summaries, drafts, contextual suggestions |
| **Organizational intelligence** | **Model how the organization operates; keep the model alive** | **Process map, information-flow graph, business semantics** |
| Software construction | Produce code that automates specific tasks | Custom internal software, deterministic bots |
| Agentive runtime | Agents that execute processes in production | Adaptive human-agent interaction, with instantiated interfaces |

Wingmap sits explicitly in the second layer — organizational intelligence — and produces the input the third and fourth layers require to operate with knowledge of the organization. The individual-assistance layer (Microsoft Copilot, ChatGPT, Claude) operates on the individual user's knowledge; the software-construction layer (products like Pit; AI-assisted coding like Cursor or Devin) operates on the declarative description the organization or the builder gives it; the agentive-runtime layer (Salesforce Agentforce, Microsoft Copilot Studio, emerging operational-agent platforms) assumes the organization knows the process when building the agent. Wingmap is the missing piece: the one that delivers the organizational model as a separable, governable, versionable artifact.


---

## Definition and principles of the technique

### Definition

**Wingmap** is a technique for the agentive discovery of an organization's operational intelligence. Through an AI agent with read access to the organization's corporate digital channels — email, messaging, file repositories, calendars, transactional systems — the technique reconstructs, without mediating interviews or workshops, **two living, connected maps**: the process map (how the work is executed in each area, in what sequence, with which actors) and the information-flow graph (which data originates where, who transforms it with what calculation, in which artifact it lives, toward which consumer it travels, which informational dependencies accumulate across areas, countries, or business lines).

The two artifacts are connected by common traceability to documentary evidence — every element of the map cites the raw documents from which it was inferred — and they are kept up to date by continuous observation, not by periodic re-discovery. Human validation occurs in distinct roles: process ambassadors for the first map, operational data owners for the second. The technique operates first in passive mode (observation transparent to the user) and, when conditions allow, in active mode (Wingworking — the user operates via the agent, the agent learns and, eventually, automates recurring patterns with deterministic bots).

### The six guiding principles

The technique is governed by six principles that order its design and application decisions. The principles are not axioms — they are operating guides that, together, distinguish Wingmap from other discovery or modeling techniques.

**Principle 1 — Observation first, intervention after.** Discovery begins by observing the digital traces the organization already generates, without asking it to produce any additional information. Intervention — interview, workshop, validation — happens on already-inferred material, not on a blank page. This inverts the traditional discovery flow (ask → write → validate) and replaces it with (observe → infer → validate).

**Principle 2 — Dual plane, not one.** The canonical output is always dual: process map *and* information-flow graph. Omitting either of the two planes breaks the value proposition. A process map without an informational graph documents the choreography of the work but not the circulation of the data; an information graph without a process map documents the circulation of the data but not the choreography that sustains it. The two planes together produce actionable understanding; each one alone produces an incomplete portrait.

**Principle 3 — Common traceability to evidence.** Every assertion in either of the two maps must be backed by a traceable reference to the raw document from which it was inferred — the specific email, the specific Teams message, the specific version of the spreadsheet, the specific transaction in the system. This technical constraint is what makes the output governable: every element can be audited, refuted, corrected, or validated against the evidence that originated it. Without traceability, the agent's output is indistinguishable from a plausible hallucination.

**Principle 4 — Distributed validation in operational roles.** Human validation of the output is not performed by a central authority — it is performed by the operational roles closest to the element being validated. A map of the laboratory's process is validated by the laboratory's ambassador; an information flow over dispatch data is validated by the operational owner of dispatch data. This distribution recognizes that the model's fidelity rests on the sum of many bounded validations, not on a global validation by a distant committee. The distribution also reduces the cognitive cost per validator and enables scaling.

**Principle 5 — Passive mode before active.** The first deployment is always passive: the agent observes without intervening in the user's workflow. Active mode (Wingworking, where the user operates via the agent) is introduced only in specific domains, with enthusiastic ambassadors, and after passive mode has demonstrated value in that domain. The reason is that active mode carries a real adoption cost — the user changes their workflow — and that cost is only bearable once the user has already seen value from the agent in passive operation. Inverting the order produces abandonment.

**Principle 6 — Produce substrate, don't consume requirements.** Wingmap's output is a cognitive substrate — a persistent, validated model of the organization — that can afterwards be consumed by multiple destinations: specifications for the data factory, configurations for BPM, prompts for operational agents, governance dashboards, executive briefings. The technique does not consume a requirement from the organization in order to produce a specific deliverable; it produces a substrate that the organization and its collaborators exploit in multiple directions as needed. This difference distinguishes Wingmap from discovery techniques oriented to a single deliverable — a BPMN map to implement BPM, a functional specification to build software, an assessment to diagnose maturity. Wingmap produces the substrate common to all those uses.

---

## Operational components

### The observer agent (passive mode)

The observer agent is the nuclear component of Wingmap. Its function is to continuously ingest the events the organization generates in its corporate digital channels, extract semantic structure from each event, and keep up to date the dual graph (process + information) that constitutes the output.

The observation scope is explicitly bounded at the start of the deployment. In the reference implementation, the default scope is Microsoft 365 — Exchange, Calendar, Teams, SharePoint, OneDrive — plus connectors to the relevant transactional systems (ERPs, vertical platforms). The bounding occurs along two dimensions: by operational domain (a specific area at the start, expansion later) and by channel type (some channels are excluded for sensitivity, for example HR folders or union channels). The bounding is a governance component, not an implementation detail.

For every ingested event, the agent extracts a structured object with predefined fields: actor or actors involved, inferred intention, business domain, referenced artifacts, preliminary hypotheses about the process the event belongs to, preliminary hypotheses about the information flow it contributes to. Extraction proceeds in layers — cheap heuristics filter noise, light models classify, powerful models reason over the relevant cases — to keep the computational cost within a reasonable budget. The extracted objects accumulate in structured storage and feed, at a configurable frequency, the dual-graph builder.

### The dual-graph builder

The second component takes the enriched events and turns them into structured hypotheses about the organizational model.

For the **process plane**, the builder identifies recurring patterns of interaction among actors — email chains with the same structure, recurring meetings with stable attendees, file-editing sequences — and applies process mining algorithms (alpha miner, heuristics miner, inductive miner) over the enriched event log to infer the graph of activities, decisions, and temporal dependencies. The result is serialized as standard BPMN 2.0, which facilitates its consumption by orchestration engines, modeling tools, and the organization's process catalogs.

For the **information-flow plane**, the builder identifies nodes of three types — people, artifacts (Excels, reports, dashboards, documents), processes — and edges connecting them by semantic relation: *originates*, *transforms*, *consumes*, *derives from*, *canonical source of*. Constructing this second graph is structurally more demanding than the first because it requires semantic extraction of the content, not just of the event — knowing which data lives in which cell of which Excel, which calculation transforms it, what relation it bears to the analogous data in another similar Excel but in another country. The graph is serialized as JSON-LD or another labeled-graph format and is preserved in graph storage (Cosmos DB with Gremlin, Neo4j) for query via API.

The two graphs share a common traceability mechanism: every node and every edge carries references to the set of raw events from which it was inferred, with a confidence field and an evidence snippet. Traceability allows the human validator (process ambassador or data owner) to consult the original material when reviewing each element.

### The validation interface

The third component is the interface through which the human validators confirm, correct, or reject elements of the dual graph. The interface is neither optional nor secondary — it is the mechanism by which the agent's output becomes governed knowledge instead of remaining a plausible hypothesis.

The interface has two modalities — one for the process ambassador, another for the data owner — because the questions each role answers are different. The process ambassador answers *"is this sequence recognized as my area's process?"*; the data owner answers *"is the origin-transformation-consumption chain of this data correct?"* and *"is the canonical source correctly identified?"*. Both validations are stored as ground truth and feed the agent to refine future inferences in the same domain.

### The active mode (Wingworking)

The fourth component is optional and selective. In domains where an ambassador user agrees to change their workflow — operating the applications through the agent instead of directly — the agent learns, session by session, the user's operating patterns in high resolution: what they query in what order, what transformations they execute, what corrections they apply. When a pattern becomes stable, the agent can generate a deterministic bot that automates the pattern without requiring an LLM at runtime.

The active mode extends Wingmap's output from *organizational model* to *organizational model + library of deterministic bots*. Bot generation is governed with DevOps discipline — versioning, testing, rollback — because the bots are code in production. The name comes from Wingworking — the practice of working with an agent as a wingman that MOTOR presented as the signal of Level 3 —: the operation is performed alongside the agent, neither in its substitution nor at its command.


### The governance layer

The fifth component cuts across the previous ones. It covers access control (which channels the agent observes, which it excludes, who authorizes), audit log (an immutable record of every event that touches the organization's data), PII management (detection, tokenization, or redaction according to policy), retention policy (how long raw data, enriched data, and embeddings are kept), and regulatory compliance (GDPR, local personal-data-protection rules, labor regulations on communications monitoring).

Governance is neither optional nor post-hoc. Its design must occur before the first deployment, with the informed consent of the observed actors and legal validation specific to the organization's jurisdiction. The section «Privacy risks and regulatory compliance» develops the consequences of failing at this component.

---

## The practice in phases

The application of Wingmap is ordered into a prior enablement phase (Phase 0) and five operational phases, with explicit criteria for moving from one to the next. Each phase produces measurable deliverables and admits criteria to proceed, pivot, or abort. The sequence is deliberate — skipping phases produces fragile deployments — but the phases may iterate in parallel within distinct domains of the organization.

### Phase 0 — Preconditions

Before deploying anything technical, the practice demands five clear preconditions.

**Executive sponsor identified and committed.** A person with authority over the observation scope who understands what they authorize and what they do not, and who takes political ownership of the decision. Without a sponsor with real power, the deployment stalls at the first access request.

**Bounded and consented scope.** The first deployment covers a specific operational domain — an area, a business unit, a geography — with an explicit perimeter of digital channels. The bounding protects the organization (it limits privacy risk) and the deployment (it limits the error surface and enables fast iteration).

**Process ambassador designated.** A person from the observed domain, with operational knowledge of the process, willingness to validate maps, and sufficient political capital to sustain the experiment before their peers. Without an ambassador, the inferred maps go unvalidated, and without validation the output remains a hypothesis with no actionable value.

**Data owners identified.** For each information flow the agent will observe — sales data, operations data, HR data — there must be a person recognized as the operational owner of the data, willing to validate the corresponding informational graph. This condition frequently exposes preexisting governance gaps in the organization — data with no clear owner — that the technique forces to be resolved at the start.

**Legal and compliance framework validated.** A legal opinion, adjusted to the organization's jurisdiction, on what the agent may observe and under what conditions. This component is not trivial and frequently demands weeks of prior work. Skipping it exposes the organization and the implementer to litigation or to sudden rejection of the deployment by internal compliance.

These five preconditions are **blocking**. If any is unmet, the deployment does not advance to the next phase; the gaps are closed in Phase 0 before touching technology.

### Phase 1 — Observation

With the preconditions covered, the agent enters passive operation over the bounded domain. The recommended minimum duration combines two floors: never fewer than three iterations of the cycle of the domain's slowest process, and never fewer than two calendar weeks — the minimum time to filter pattern noise. In practice: for domains of daily cadence, two to four weeks; for weekly cadence, six to eight weeks; for monthly cadence, three months. This duration is not negotiable downward — inferring cyclical processes requires observing several iterations to distinguish pattern from noise. Skipping this floor produces spurious conclusions.

During the observation phase, the agent accumulates enriched events in structured storage and builds preliminary versions of the dual graph. The preliminary versions are not delivered — they are internal calibration material. What is delivered to the organization at the end of the phase is a coverage report: what percentage of the domain's digital flow was ingested, what recurring patterns were identified, what structural gaps exist (processes that appear to occur but whose digital traces are insufficient to reconstruct them).

### Phase 2 — Inference and dual-graph construction

This phase consolidates the preliminary versions of the dual graph into reviewable versions. This demands work on the implementer's side (prompt calibration, schema refinement, tuning of process mining algorithms over the enriched log) that is not automatic: the quality of the output depends on sustained technical iteration.

The phase's exit criterion is the delivery to the organization of three to five candidate process maps and five to ten candidate cross-role information flows, all with traceable evidence and all with confidence estimated per element. The delivery does not claim final correctness — it aims to offer concrete material on which the following phase executes validation.

### Phase 3 — Dual validation

This phase is where the agent's output becomes governed knowledge. Each process map goes through a validation session with its ambassador; each information flow goes through a validation session with its operational data owner. The sessions are designed with bounded time (60 to 90 minutes per session) and a concrete format (the interface described in «The validation interface», with evidence-traceable material visible to the validator).

Each session produces one of three outcomes. **Validation with minor correction** — the validator recognizes the element as their process or their data flow, adjusts details, signs off. **Validation with major correction** — the validator recognizes the general pattern but detects structural errors requiring re-inference; the agent reprocesses with the feedback as ground truth for the next attempt. **Rejection** — the validator does not recognize the element; the agent investigates whether the inference was spurious or whether the observed domain has processes the agent does not yet capture, and action is taken accordingly.

The phase ends when minimum validation thresholds are reached: 70% of process maps validated without major correction, 60% of information flows validated without major correction (the thresholds are specific to the first deployment; in successive deployments the thresholds rise with accumulated calibration). If the thresholds are not reached after two iterations, the phase reports a diagnosis — the problem may be one of inference (model) or of input (quality of the observed channels) — and the decision to proceed or abort is made by the sponsor with the implementer's advice.


### Phase 4 — Maintenance cycle

This phase is sustained operation. Once the initial maps are validated, the agent keeps observing and the graphs live — they update with every iteration of the process, they are enriched with newly detected exceptions, they are refined with every subsequent validation. The organization gains continuous access to a model of how it operates, kept current, governed, and traceable.

This phase has its own key metric: **graph latency** — the difference between the last relevant observed event and the current version of the graph. Latency must be kept below an agreed threshold (typically 24 to 72 hours for an active domain). Growing latency indicates that the agent has lost the ability to keep pace with the organization, and is a sign that something in the infrastructure or in the model has broken.

### Phase 5 (optional) — Selective active mode

The final phase, optional and selective, introduces the active Wingworking mode in domains where two simultaneous conditions are met: there exists a process of value where the passive modality has already identified a stable pattern, and there exists an ambassador user willing to operate via the agent instead of directly. Active mode is introduced only where both conditions hold, and one domain at a time. Mass generalization of active mode is contraindicated — the individual adoption cost is real and the learning curve requires accompaniment.

The product of active mode is the incremental library of deterministic bots, governed with the same discipline with which any of the organization's production code would be governed.

---

## Discussion

### Distinction from classical process mining

The Wingmap technique coexists with a mature discipline — classical process mining — and the differences are worth articulating with precision. Classical process mining (Celonis, Apromore, Disco, SAP Signavio, Microsoft Process Mining on Power Automate, UiPath Process Mining) operates on structured logs extracted from transactional systems: each event is a tuple (case_id, activity, timestamp, resource) deterministically extracted from the log of an ERP or a management system. The discipline has fifteen years of scientific literature — the work of van der Aalst and its derivatives — and tools with formally defined metrics (fitness, precision, generalization).

Wingmap does not replace classical process mining — it extends it to domains where classical process mining does not operate. The gap is one of nature, not of coverage. Classical process mining requires the process to live inside a system that produces structured logs with the canonical tuple. The greater part of an organization's real process does not live inside such systems — it lives in emails, in spreadsheets, in messages, in shared files. Wingmap captures that fraction of the process, infers its semantic structure with LLMs, and produces an enriched log on which the same classical process mining algorithms can — optionally — be applied. The traditional discipline gains a new domain of applicability; it does not lose its own.

The second difference is structural. Classical process mining produces an event graph. Wingmap produces an event graph *plus* a parallel information-flow graph. That second dimension does not exist in the traditional discipline — and not by omission but by impossibility: an ERP's structured logs record *that* the activity occurred, not *what data moved* in that occurrence. Wingmap, by operating on unstructured channels with semantic extraction, naturally captures the informational content. That difference is its structural differentiator.

### Distinction from traditional interviews and process consulting

Classical process consulting solves discovery by sending teams of people — analysts, consultants, facilitators — to interview the organization, observe its operation, map flows in BPMN or equivalent, and iteratively validate the result. The practice is mature, has refined methodologies (Six Sigma, Lean, BPMN, BABOK), and Big4 frameworks that systematize it.

Wingmap differs along four measurable dimensions. The first is **speed** — an observer agent can ingest and enrich events at a continuous rate, while a human team operates in blocks of dedicated hours. For a mid-sized domain, the difference is an order of magnitude (days vs. months). The second is **cost** — the agent's computational cost, even at enterprise scale, is typically a fraction of the human cost for the same scope, also an order of magnitude. The third is **coverage** — the agent observes all of the domain's digital activity, not an interviewed sample; the processes that human discovery would omit by chance (a low-frequency process that did not surface in the interviews) the agent captures through exhaustiveness. The fourth is **continuity** — human discovery produces a point-in-time portrait; the agent produces a living model that stays up to date.

In exchange, traditional consulting contributes two things the agent does not deliver by default: **strategic contextual interpretation** (understanding why a process evolved the way it did, what political tensions shaped it, which interventions have the best probability of success) and **change negotiation** (consultancies facilitate organizational transformations, they don't merely document them). Wingmap does not compete with those two components — it complements them. The technique replaces discovery as a manual craft of interviews and leaves consultants free to concentrate on interpretation and change, which are their real value.

### Distinction from individual copilots

Microsoft Copilot for Microsoft 365, ChatGPT, Claude, Gemini in Workspace are individual assistants that accelerate the human in their task — drafting a better email, summarizing a meeting, generating a formula. Their unit of analysis is one user's session and their unit of value is individual productivity.

Wingmap is structurally different: it operates on the sum of many users' tasks and reconstructs the cross-role organizational model. Its unit of analysis is the flow between roles; its unit of value is organizational understanding. An individual copilot cannot produce what Wingmap produces because its access is to the user's session, not to the organization's aggregate flow. The technique complements the copilot — an organization with Copilot deployed has part of the technical infrastructure Wingmap needs, but it does not have Wingmap.

### Distinction from software AI-builders

The emerging category of *AI product team as a service* — products like Pit, publicly launched in May 2026 — uses AI to accelerate the construction of custom internal software that replaces the back office's patchwork of Excel + email + rigid SaaS. The distinction from Wingmap is one of layer: Pit and its peers are **agentive to build, pre-agentive to run** — they use AI in the builder, they deliver deterministic software that operates with pre-created interfaces. Wingmap is **agentive to discover, agentive to run** — it produces the cognitive substrate that later enables operational agents at runtime with instantiated interfaces.

The two categories are complementary, not competitive. A mature organization uses them in order: first Wingmap to understand how it operates and what data circulates; then an AI-builder (or an internal team) to build tailored software in the processes where construction adds value; then operational agents that execute at runtime with knowledge of the model. The organizational-intelligence layer is qualified input for the construction and runtime layers.


### The technique as substrate for the agentive transition

Wingmap is not fully understood as an isolated discovery technique — it is understood as a **foundational brick of the transition from the pre-agentive era to the full agentive era**. This reading widens the scope of the argument beyond the individual organization.

The full pre-agentive era (1995–2025) built enterprise software as a persistent artifact: pre-created screens, fixed logic, maintenance as a cycle parallel to operation. The full agentive era (~2030 onward, by reasonable projection) will build enterprise software as a situational event: agents that instantiate interfaces on the fly, execute processes at runtime with contextual interpretation, reconfigure themselves through conversation. The transition unfolds over a horizon of five to ten years, with both topologies overlapping throughout that period.

The operative question for an organization in transition is: what asset to build today that serves both the pre-agentive operation it already has and the agentive operation to come? The enterprise software built today will become obsolete when operational agents replace pre-created interfaces. BPM platforms will remain useful as orchestration engines but will lose their presentation layer. The safest investment, under this framing, is the **persistent, validated organizational model** — the dual graph Wingmap produces. That model does not become obsolete with the transition; on the contrary, it becomes more valuable, because it is the input that operational agents will need in order to execute with knowledge of the organization.

Wingmap, read this way, is not one more discovery technique among many — it is the technique that produces the substrate of the next decade of enterprise software. That is its universal thesis.

---

## Limitations and zones of non-applicability

The technique has clear frontiers. They are worth declaring with precision so as not to sell promises that go unfulfilled.

### Processes that live outside the digital trace

Wingmap captures what the organization leaves in its corporate digital channels. What happens on paper — the agronomist's field notebooks, the plant operator's manual annotations, physical forms —, in face-to-face conversations without minutes, in untranscribed phone calls, in informal WhatsApp groups not integrated into the corporate stack, falls outside the agent's reach. For an organization with a great deal of operational activity in these non-digital channels, Wingmap's effective coverage can fall significantly below the totality of the real process.

The fraction of digital coverage varies by sector. Administrative areas (finance, HR, procurement) may sit between 70% and 90% in digital channels. Commercial areas with intense client interaction may fall to the 40-60% range. Field operations areas (agronomists, plant operators, physical logistics) may be below 40%. The technique delivers its full value proposition in areas with high digital coverage and reduces its value proportionally in areas with low coverage. Recognizing this limit at the start of the deployment, choosing pilot domains with high digital coverage, is part of the discipline of application.

### Organizations with low appetite for discovery

The technique demands explicit authorization to observe corporate channels. That authorization is a political decision, not a technical one. An organization where the sponsor lacks the will or the capacity to authorize the agent's access — out of cultural sensitivity ("they're watching us"), a restrictive regulatory framework, an active union, distrust of the implementer — cannot benefit from Wingmap. The technique is not universally applicable; it is applicable to the subpopulation of organizations with a real appetite for discovery.

This limitation has an operational corollary: the first deployment of Wingmap in an organization must always negotiate the scope with the sponsor before touching technology. Skipping the negotiation produces deployments that stall in security and compliance approvals.

### Privacy risks and regulatory compliance

An agent with read access to corporate email, messaging, and files operates in a regulatory zone that is narrowing, not widening. The European AI Act (progressively in force 2024-2027) classifies as high risk those AI systems that process employee data to evaluate performance or make decisions affecting the organization of work; a process map whose use leads to functional reorganization can fall under that classification. The personal-data-protection laws of Chile, Mexico, Brazil, and other countries are converging with GDPR on standards of consent, right of access, and purpose limitation. Each jurisdiction's labor law restricts the monitoring of employee communications to varying degrees.

The responsible application of Wingmap requires specific legal counsel, informed consent from the observed actors, an explicit acceptable-use policy validated by HR and by legal, and a technical architecture designed with PII tokenization or redaction according to policy. Skipping this component produces legal exposure for the implementer and the organization, and can bring the project to a halt by court order or by internal compliance.

### False positives and the validation paradox

The agent can infer processes that do not exist — two emails always sent on the same day may be two independent processes presented as one with two steps; a communication pattern between two people may be personal habit and not institutional process. Spurious inferences are inevitable; the only debatable points are their frequency and the validation discipline that detects them.

There is a known paradox in human-AI collaboration that deserves naming: when a human supervises an automated output, their error-detection rate drops systematically compared to when they produce the output from scratch. The meta-analysis by Goddard, Roudsari, and Wyatt (*Journal of the American Medical Informatics Association*, 2012) of 74 studies of medical decision-support systems showed that introducing the system reduces typical errors but introduces new errors when the system produces plausible yet incorrect outputs. Hurried validation of agent-inferred maps can ratify errors that human inference from scratch would have caught. The defense against this bias is discipline: time dedicated to validation, traceable evidence visible to the validator, quality-drift metrics that detect systematic drops in fidelity.

### The human dependency shifts; it is not eliminated

The technique reduces the cost of discovery but does not eliminate human dependency. The bottleneck shifts from *describing the process from scratch* to *validating the inferred process*. The validator (process ambassador or data owner) is still a person the organization must make available, with dedicated time, political capital, and willingness to sustain iterations. In organizations where BAU completely consumes the time of the potential validators, the technique hits the same ceiling as the traditional techniques, albeit at lower total cost.

The difference is quantitative but structural: validating 50 maps in 60-minute sessions requires 50 hours; describing those same 50 processes from scratch in workshops requires 200-500 hours. The technique reduces the cost by a factor of four to ten. But it does not reach zero, and assuming it does leads to failed deployments.

### Technological maturity at the time of application

The technique depends on language-model capabilities that in 2026 are solid but not perfect. Structured event extraction from free text has reported error rates in the 10-30% range in production, depending on domain and calibration. Semantic inference of processes from heterogeneous corpora is an open problem: the available evidence and deployment experience place inference quality (measured as F1) in ranges on the order of 0.4-0.7 in controlled scenarios and lower in production with real data and noise — the author's estimates, pending formal benchmark. These rates are adequate for validatable preliminary hypotheses, not for autonomous production without human supervision.

The trend is one of compounding improvement — the models advance year after year — but the improvement is not linear and does not arrive in time for any specific deployment. Responsible application of the technique acknowledges the current rates as the operating limit and designs the validation phase («Phase 3 — Dual validation») around them, not around the rates that will exist in five years.

---

## Conclusion

Wingmap is a technique for the agentive discovery of an organization's operational intelligence. Its contribution consists in formalizing a reproducible practice that reconstructs, without interviews, two connected planes of the organizational model — process and information flow — from the digital traces the organization already generates. The six guiding principles (observation first, dual plane, common traceability, distributed validation, passive mode before active, substrate and not requirements) order the design and application decisions. The phases (preconditions, observation, inference, dual validation, maintenance, and — optionally — active mode) order the practice over time. The four distinctions (from classical process mining, traditional consulting, individual copilots, AI-builders) situate the technique on the map of adjacent categories.

The technique replaces none of the adjacent disciplines — it complements them structurally. And in doing so, it produces an asset the full agentive era is going to need as critical input: a persistent, validated model of how the organization operates, on which the operational agents of the 2030 horizon will be able to execute with situational knowledge.

The first witness case of Wingmap is underway at the time of writing this chapter: a multinational agroindustrial holding with dozens of companies operating in several countries. The lessons from that deployment will feed the next editions of this book. The predictions the chapter makes about coverage rates, inference quality, operating costs, and human dependency are reasoned hypotheses that the witness case will confirm or refute with operational evidence.

The invitation this chapter extends to other practitioners is not to use the specific Wingmap product — that is a separate commercial decision — but to apply the Wingmap **technique** in their own contexts, with their own tools, in their own organizations. The principles are implementation-independent. The practice is reproducible. The substrate it produces is valuable in itself, no matter who builds it or with what technical stack.

Whoever applies Wingmap in an organization does not document processes — they produce operational intelligence. The difference matters. Operational intelligence is a durable asset; process documentation, in the absence of intelligence, is paper.

---

## Future work

Five directions remain open.

**Empirical calibration of the application rates.** The quantitative claims — coverage by sector, validation rates, graph latency — rest on limited data and reasoned projection, not on a robust empirical base. Three to five complete deployments with comparable metrics will allow moving from projection to statistics.

**Study of the active mode's learning curve.** The active Wingworking mode demands a change in user behavior. The shape of the curve — how long it takes a user to overcome the initial friction, how many abandonments there are, what predicts persistence — is an open empirical problem that deserves systematic study.

**Generalization to non-Microsoft stacks.** This chapter assumes an implementation over Microsoft 365 as the initial spine. Application to Google Workspace, Slack-first, or heterogeneous stacks is feasible but requires additional components (specific connectors, different governance models) that deserve dedicated treatment.

**Integration with agentive orchestration engines.** The substrate Wingmap produces is designed to be consumed by operational agents. The formal specification of the APIs and exchange formats connecting the Wingmap graph with platforms such as Salesforce Agentforce, Microsoft Copilot Studio, or open frameworks (LangGraph, CrewAI) is pending architectural work.

**Ethical grounding of organizational observation.** The technique observes human activity in corporate channels. The ethical framework of that observation — beyond minimal regulatory compliance — deserves dedicated treatment: how transparency is reconciled with protection, how the model's value is distributed between the organization and the observed actors, how the drift toward workplace surveillance is avoided. These questions are normative, not technical, and require dialogue with academia, unions, and labor authorities.

---

## References

### On this chapter's sources

This chapter derives from an internal research cluster (16 working documents, May 2026) whose detail lives in the author's archive. The verifiable references are listed below.

### External literature

- Polanyi, Michael. *The Tacit Dimension*. University of Chicago Press, 1966.
- van der Aalst, Wil M.P. *Process Mining: Data Science in Action*. 2nd edition. Springer, 2016.
- Goddard, K., Roudsari, A., & Wyatt, J. C. "Automation bias: a systematic review of frequency, effect mediators, and mitigators." *Journal of the American Medical Informatics Association*, 19(1), 2012.
- Rother, Mike & Shook, John. *Learning to See: Value-Stream Mapping to Create Value and Eliminate Muda*. Lean Enterprise Institute, 2003. (Methodological reference for information-flow maps in the Lean tradition).
- Hammer, Michael & Champy, James. *Reengineering the Corporation*. HarperBusiness, 1993. (Classic reference the chapter situates historically).

### Cited market references

- Press coverage of Pit's public launch (techcrunch.com, sifted.eu, tech.eu, May 2026).
- Public coverage of Microsoft Copilot, Microsoft Process Mining, Salesforce Agentforce, Glean, Celonis (as of May 8, 2026).

---
