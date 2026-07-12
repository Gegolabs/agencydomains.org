## Agentlets

At the entrance of an emergency room there is a triage nurse. Her task is the same all day: receive the patient, assess them, classify them — red, yellow, green — and route them. The task is repetitive in its form; no repetition is identical to the previous one. Every patient arrives with different symptoms, different histories, signals that appear in no manual exactly as they present. The nurse cannot do her job on muscle memory — every classification demands fresh judgment —, but neither does she need the chief of internal medicine for every patient: her judgment operates within a bounded protocol, and when the case exceeds the protocol, she escalates. The triage nurse is neither a reflex nor the hospital's full deliberation. She is a third thing: **routine judgment, packaged into a role**.

Agentive systems are full of work with that shape. Classifying the emails that arrive at an operational inbox. Triaging monitoring alerts. Summarizing every new document that enters a case file. Extracting the entities from an invoice never seen before. Judging whether a message warrants immediate interruption or can wait for the morning briefing. These are tasks **recurrent in their form but fresh in every instance**: the pattern is stable, the execution demands interpretation. They do not mature toward determinism — not for lack of regenerations, but by nature.

The canon, up to this point, gave them two homes and neither was the right one. The first home is the **Botlet**: but the Botlet is non-LLM code by definition, and forcing an interpretive task into deterministic code produces exactly the fragility the architecture exists to avoid. The second home is the full **Cognition** of Layer 2: it works, but at the cost of the system's most expensive path — deliberative, conversational, sized for the genuinely new — applied to a pattern that repeats a hundred times a day. Between muscle memory and full deliberation, the middle rung was missing.

This section formalizes the **Agentlet** as the **eighth canonical primitive** — the Botlet's sibling unit whose execution body invokes bounded inference. The Agentlet is the home of routine judgment: packaged pattern on the outside, bounded judgment on the inside.

> *The Botlet is muscle memory. The Agentlet is packaged routine judgment. Cognition is reserved for the genuinely new.*

### Definition

An **Agentlet** is a packaged unit of Layer 3 (Autonomy), sibling of the Botlet, whose execution body **invokes bounded inference**: a model sized to the task, applied within a charter the spec declares. Like the Botlet, it is a configured instance of a pre-forged piece — the **proto-Agentlet** —, it is hosted by the Botler, and it is engendered and maintained by the agent. Unlike the Botlet, each of its executions exercises judgment: it interprets the concrete instance in front of it rather than executing deterministic code.

The phrase that fixes the sibling doctrine: **an Agentlet is a Botlet with judgment inside — no more, no less**. It lives exactly like its sibling. It inherits by structure, not by exception, the entire apparatus of Layer 3 units: the proto-/instance pattern, the catalogs and their network effects, the source-code vs spec separation, **manifestation** and **temporality** (`discrete`/`continuous`), the declarative quality contract, the derivation chain, the append-only log, and the operation API verbs (`specialize` · `invoke`/`schedule` · `read`/`subscribe` · `status`/`activate`/`deactivate`/`retire`). What changes is a single attribute — the body invokes inference — and from that attribute follow, in cascade, the differences the rest of this section develops.

Four properties define the conformant Agentlet. The first is that its **charter is declared in the spec**: what task it resolves, over what inputs, with what outputs, within what limits. The Agentlet does not choose what to do — its inference is spent on *how* to do its own work, never on deciding *what* its work is. The second is that its **inference is bounded**: the spec declares the model (sized to the task, not the frontier model of Cognition), the Capabilities it may consult, and the budget per execution. The third is that **all of its inference passes through the Botler**: the controlled handle the Botler hands it includes the cognition control point, so that every model call is metered, budgeted, validated and audited — bypass is structurally impossible, not merely forbidden. The fourth is that it carries a **fallback guarantee toward full Cognition**: when its bounded inference cannot resolve the case — the charter does not reach, the verdict's confidence falls below threshold, the input resembles nothing anticipated —, the Agentlet escalates and Layer 2 Cognition rescues. The process never stops.

### The smuggling rule

The border between the Botlet and the Agentlet is a binary attribute, and the spec protects it in both directions:

- **If there is inference in the body, it is an Agentlet.** A Botlet with a model call hidden in its code is non-conformant — it smuggles cost and non-determinism into a unit whose guarantees (near-zero marginal cost, converging maturity, senior offline operation) depend on having neither.
- **If there is no inference in the body, it is a Botlet.** An Agentlet whose charter turned out to be resolvable with deterministic code is a misclassified Botlet — and a misbudgeted one: it pays tokens for work muscle memory would do for free. Cognition, upon detecting it, crystallizes it: it generates the Botlet that replaces it.

The second direction of the rule also describes a **natural trajectory**: there are tasks that enter the system as Agentlets — because at first every instance seemed to demand judgment — and that, with accumulated operation, reveal a crystallizable core. Cognition extracts that core into a Botlet and leaves the Agentlet only the genuinely interpretive residue, or retires it altogether. The mature system migrates work down the cost ladder: from Cognition to Agentlets, from Agentlets to Botlets.

### Agentlet vs Botlet — the canonical distinction

| Axis | **Botlet** | **Agentlet** |
|---|---|---|
| **Execution body** | Non-LLM code; zero inference | Invokes bounded inference, via the Botler's handle |
| **Metaphor** | Muscle memory | Packaged routine judgment |
| **Natural task** | Recurrent and **crystallizable** into code | Recurrent in form, **interpretive** in every instance |
| **Determinism** | Converges with maturity | Does not converge — correctness is statistical by nature |
| **Marginal cost** | ~0 (traditional compute) | Tokens per execution, budgeted in the spec |
| **Maturity** | Junior → senior; senior = exogenous-only failures | Its own semantics: stabilized spec, decreasing escalation rate |
| **Offline** | Senior reliably operable offline | Only with an edge-resident model, declared in the spec |
| **Fallback** | Cognition executes manually | Escalates to full Cognition |

What the table does **not** contain matters as much as what it does: proto-/instance, catalogs, spec, manifestation, temporality, quality contract, derivation chain, log, operation verbs, hosting by the Botler, genesis by the agent — all of that is identical, because it is predicated of the genus and not of the species. The spec calls the genus **units**: the Botler hosts units; the Botlet and the Agentlet are its two species. The canonical runtime relation is stated in its general form — **1 Process = 1 Botler + N units** — and each context instantiates it to the species at hand.

### Agentlet vs Agent — agenda vs charter

The primitive's name claims membership in the **Agent** family, and the spec grants it: the umbrella term *Agent* covers, from this version of the canon onward, **three members** — the **Assistant** (Layer 2, reactive), the **Autonomous Agent** (Layer 3, proactive, an inhabitant) and the **Agentlet** (Layer 3, packaged). The concession is honest — the creature genuinely reasons, with a genuine model — but it demands drawing the border with the Autonomous Agent with the same rigor with which the canon drew Facet vs Botlet, because the two live in the same layer and both use inference.

The border fits in one line: **the Agent has an agenda; the Agentlet has a charter.** The Autonomous Agent pursues goals — it decides what to do, when, with what means, and engenders the units it needs. The Agentlet executes the task its spec declares — its judgment operates within the charter, never over the charter.

| Axis | **Autonomous Agent** | **Agentlet** |
|---|---|---|
| **Nature** | **Inhabitant** of the AgencyDomain | **Catalog piece** — instance of a proto |
| **Born through** | Provisioning (six-phase lifecycle, first-order identity) | `specialize` over a proto-Agentlet |
| **Agenda** | Pursues goals; decides what to do and when | Fixed charter declared in the spec |
| **Cognition** | Full: its own bindings, complete Capability tree, multi-LLM | Bounded: sized model, the Capabilities the spec declares |
| **Engenders** | Generates and regenerates Botlets and Agentlets | Engenders nothing; it is maintained |
| **Fallback** | *Is* the fallback — above it, only the human | Escalates to Cognition via the Botler |
| **Governance** | Exercises the five Trust Infrastructure pillars (MUST) | Governed through the control points of the Botler's handle |

The **border test** protects the category from bleeding upward. Three questions; any answer on the side of autonomy means the piece is an Agent, not an Agentlet:

1. Does it choose its own goals, or does it receive them declared in the spec?
2. Can it alter its own process or engender other units?
3. Is its identity that of an inhabitant (provisioning) or of an instance (`specialize`)?

An Agentlet with a fat charter, an internal loop and its own criteria about what to pursue is not an advanced Agentlet: it is an Autonomous Agent in disguise, operating without the governance its nature demands — the agentive version of anti-pattern C in §5.

### The Botler as guardian — same runtime, one more control point

The Agentlet brings no runtime of its own. It is hosted by **the same Botler** that hosts the Botlets, and this decision is one of principle, not convenience. The Botler is generic by definition: it manages lifecycle, isolation and execution of any unit without understanding its domain — and calling a model is not domain; it is a runtime service. The extension follows the pattern the Botler already practices: alongside `capability_call` and `log`, the controlled handle the Botler delivers on each invocation exposes a third control point — **`cognition_call`** —, the only path by which the Agentlet's body reaches a model.

The governance consequence is the entire argument: **because all of the Agentlet's inference passes through the handle, Trust Infrastructure sees it whole.** Every model call is metered (tokens, latency), budgeted (against the limit the spec declares), validated (the Pillar 3 mechanisms — hallucination detection, DLP, tokenization — apply at the control point) and audited (in the same append-only log, under the same identity, under the same governance as the rest of the AgencyDomain). A parallel runtime for Agentlets would have to duplicate all of that machinery — a second sandbox, a second handle scheme, a second escalation chain, a second presence in the distributed Layer 3 — only to end up delivering the same guarantees. The Botler's flat architecture already delivers them.

The legitimate concern that might push toward a separate runtime — the resource profile: model latency, per-token cost, eventual hardware acceleration — is a deployment matter, and the canon already holds the door open: Botler subtypes are distinguished **by topology and deployment role, never by domain**. A segregated execution pool for inference-heavy units is exactly a deployment-role distinction: one conceptual Botler, N processes if the operation calls for it.

It is worth making explicit the **two relations** that sustain the units, because they operate on different floors and both cover both species equally:

| Relation | Who exercises it | Over Botlets | Over Agentlets |
|---|---|---|---|
| **Hosting / execution** — runtime without agency: lifecycle, isolation, controlled handle, log | The **Botler** | Yes | Yes (same handle, plus `cognition_call`) |
| **Genesis / maintenance** — deciding it exists, specializing it, regenerating it, answering for it | The **agent** (cognition) | Yes | Yes |

The agent is the parent of both species; the Botler is the butler of both. No unit gets a separate house.

### Agentlet maturity — stabilization, not convergence

The Botlet's junior → senior trajectory converges because each regeneration **crystallizes** variants into code: the senior is deterministic and that is why its only failures are exogenous. The Agentlet does not walk that trajectory — its correctness is statistical by nature and no amount of operation makes it deterministic. Pretending that an Agentlet "matures to senior" in the Botlet's sense is a category error with operational consequences: it can never be promised the offline reliability of the senior Botlet on the same basis.

The spec defines for the Agentlet a **maturity semantics of its own**, observable in the same append-only log that already tracks Botlets:

- **Spec stabilization** — the charter, the operating prompt and the configuration stop changing between revisions; `specialize` edits grow sparse.
- **Decreasing escalation rate** — the fraction of executions the Agentlet resolves within its charter without escalating to full Cognition grows and stabilizes. It is the functional analogue of `95/4/1`: the proportion between bounded judgment that suffices and full judgment that rescues.
- **Sustained quality under the declarative contract** — its declared quality attributes (freshness, SLA, degradation) hold within threshold over a sustained period.

The Agentlet's **offline** behavior demands explicit declaration, not inheritance from its sibling. A senior Botlet operates offline because it needs no model at all; an Agentlet operates offline only if its model resides on the edge. The spec of every conformant Agentlet **MUST** declare the locality of its bounded cognition — cloud-resident, edge-resident or hybrid, with the same vocabulary the spec already uses for Connectors — and its behavior without a network. Without that declaration, the "trivially explainable offline mode" consequence of the parallel topology breaks silently: the site that counted on its Autonomy Path discovers, with the network down, that half of its units needed a model on the other end of the wire.

### proto-Agentlet — the pre-forged piece of judgment

Like its sibling, the Agentlet rarely springs from nothing: it springs from a **proto-Agentlet** — the pre-forged piece the agent configures in its Engineering time to instantiate an Agentlet specific to the case. The proto-Agentlet contains the body (the scaffolding of the interpretive task: the charter's structure, the skeleton of the operating prompt, the input and output contracts, the escalation thresholds); the Agentlet is the configured instance. The proto-Botlet's two classes apply unchanged: a **tempered** proto-Agentlet resolves one interpretive function and is configured through bounded parametrization (an operational email classifier, an invoice field extractor); a **platform** proto-Agentlet is a generic judgment engine whose specialization lives in compositional configuration and covers N functions of its domain.

The **derivation chain** extends without friction: documented use cases require units — zero, one or several, of either species —, and each unit is an instance of some proto in the catalog. Every conformant Agentlet **MUST** be traceable in that chain, and the append-only log **MUST** record the proto-Agentlet of origin of each instance. The common catalogs — public and open at AgencyDomains.org, proprietary codices, private contracts, sovereign agreements — accumulate proto-Agentlets with the same network effects with which they accumulate proto-Botlets: implementer n+1 receives charters, operating prompts and thresholds refined by implementers 1 through n.

The **generations** (`G1`/`G2`/`G3`) apply with a natural reading: in `G1` the agent configures the proto-Agentlet — fills in the charter, adjusts the operating prompt within the scaffolding, sets thresholds — without writing its body. The `G1`/`G2` edge is the same as the Botlet's: configuration that a well-defined Capability evaluates is `G1`; extension of the proto's internal logic is `G2`.

### The economics of the three rungs

With the Agentlet, the agentive system's economic ladder is complete. Chapter 4 presented two paths — costly Cognition, cheap Autonomy —; the fine-grained view distinguishes **three rungs of per-execution cost**:

| Rung | Unit | Inference | Marginal cost |
|---|---|---|---|
| 1 | **Botlet** | Zero | ~0 — traditional compute |
| 2 | **Agentlet** | Bounded: sized model, declared budget | Low and **budgetable per unit** |
| 3 | **Cognition** | Full: deliberative, frontier model, complete tree | High — reserved for the new |

The middle rung is the one that was missing. Without it, every recurrent interpretive task paid rung-3 prices — or was forced, fragile, onto rung 1. With it, the organization assigns each pattern to its natural cost, and the mature system migrates work down the ladder: Cognition cedes interpretive routines to Agentlets; Agentlets cede crystallizable cores to Botlets.

The Agentlet's arrival **qualifies, but does not break**, the economic promise of the Autonomy Path. The path remains the cheap one — but it stops being uniformly free: it contains units of ~0 marginal cost and units of bounded cost, and the mix is declared per unit, not averaged away. Under **fixed Subscription** plans, the argument of Chapter 5 §2 refines in the same direction: Botlets remain the mechanism that makes sustained autonomy possible without exhausting the quota, and Agentlets consume quota — bounded, budgeted, visible in the log — so their share of the mix is an explicit economic decision of the organization, exactly as the decision of which patterns to consolidate into Botlets is.

There is a second cross-cutting consequence: **the Validation pillar gains a seat in Layer 3.** Until this version of the canon, Validation was exercised in Layer 2 (partial) and Layer 4 (principal), because Layer 3 contained only deterministic code. With Agentlets, statistical correction enters the muscle-memory zone — exactly the volatility the Bounded Concerns Architecture (Chapter 3) teaches to confine —, and the Pillar 3 mechanisms (hallucination detection, structured-output validation, DLP, tokenization) apply at the Botler's `cognition_call` control point, over every execution of every Agentlet. The thinness of the domain is preserved: statistical judgment stays confined to declared, governed, auditable units — never scattered through the runtime.

### When to use an Agentlet — and when not?

The decision among the three homes — Botlet, Agentlet, Cognition — resolves with two questions in cascade:

**First: is the task recurrent?** If not — if it is one-off, exploratory, or its pattern has not yet stabilized —, it belongs to Cognition. The practical ten-invocations rule of §2 applies to both unit species alike.

**Second: does each instance demand judgment?** If not — if the logic is crystallizable into deterministic code —, **Botlet**, always: it is the cheapest rung and the only one that matures toward reliable offline operation. If yes — if the pattern is stable but each execution interprets a new instance —, **Agentlet**.

Three signals confirm that a task is Agentlet territory: the input is **natural language or unstructured content** (emails, documents, transcripts, free-form descriptions); the output requires **classifying, summarizing, extracting or judging** rather than computing or transporting; and attempts to solve it with rules produce **exception lists that grow without converging**. And two anti-signals return the task to its neighbors: if the "judgment" turned out to be a stable decision table, it is a Botlet not yet crystallized; if the charter cannot be declared — the task requires deciding what to do, not merely how —, it is Agent work, with Agent governance.

### Conformance

An Agentlet implementation conformant with this specification must satisfy:

| Requirement | Level |
|---|---|
| Charter declared in the spec: task, inputs, outputs, limits | **MUST** |
| Bounded inference declared: model, accessible Capabilities, per-execution budget | **MUST** |
| All inference routed through the `cognition_call` control point of the Botler's handle | **MUST** |
| Fallback guarantee: escalation to full Cognition on out-of-charter cases or sub-threshold confidence | **MUST** |
| Zero inference outside the handle (the smuggling rule, Botlet→Agentlet direction) | **MUST** |
| Hosting by the generic Botler — no parallel runtime per species | **MUST** |
| Traceability: every execution and every inference call in the append-only log | **MUST** |
| Traceable in the use-cases → units → protos chain; proto-Agentlet of origin recorded | **MUST** |
| Declared locality of the bounded cognition (cloud / edge / hybrid) and offline behavior | **MUST** |
| Pillar 3 Validation applied at the cognition control point | **MUST** |
| Explicit Agentlet vs Autonomous Agent distinction in API and documentation (the border test) | **MUST** |
| Maturity metrics of its own: spec stabilization and escalation rate | **SHOULD** |
| Crystallization: detection of deterministic cores and extraction into Botlets | **SHOULD** |
| Execution pool segregated by resource profile (deployment role) | **MAY** |

### Evolution frontier

Three active areas of evolution of the Agentlet deserve mention in closing.

**Edge models for bounded judgment** are the first. The viability of the offline Agentlet depends on small models running at the physical site with sufficient quality for bounded charters. The state of the art advances quickly; the spec already provides the declaration vocabulary (locality of the bounded cognition) so implementations can adopt edge models without a contract change.

**Confidence calibration** is the second. The Agentlet's escalation to full Cognition depends on the Agentlet itself estimating when its verdict does not reach the threshold — an open problem of statistical calibration. While it matures, conservative implementations compensate with low thresholds: over-escalating costs tokens; under-escalating costs trust.

**Assisted crystallization** is the third. The automatic detection of deterministic cores inside Agentlet charters — the Agentlet → Botlet trajectory of the smuggling rule — is today a judgment of cognition in its Preparation time. Its formalization as an inverse Pattern Recognition mechanism (detecting what *stopped* needing judgment) is open work.

---

With the Agentlet, the roster of formal constructions of this chapter closes — **eight canonical primitives**: AgencyDomain, Botlet, proto-Botlet, Agentlet, Capability, Trust Infrastructure, the Assistant vs Autonomous Agent distinction, and the Facet. Whoever has followed Chapters 4 and 5 holds the complete constructive vocabulary with which the agentive category can be reasoned about and built — from the computational space that contains it all to the three-rung ladder by which work finds its natural cost.

Chapter 6 shifts the gaze from the individual system to the market. It allows whoever builds or invests to answer with discipline the question of where each actor — one's own or someone else's — competes, and why the same link in the chain can be a hotly contested zone or still-open territory.
