# Chapter 9 · Vergis — the reference implementation

The preceding chapters delivered a specification: primitives, required properties, canonical separations, declarative contracts. A specification, however precise, is not a living system. Between the contract and the practice there is a leap that every external reader intuits upon closing the last chapter of the spec: *"what does this look like when it works?"*. This is the section that answers that question with a concrete, downloadable, executable artifact.

## A note on the scope of the canon

It is worth fixing first what this canon is and is not, because the answer delimits the role of everything that follows.

> This canon contains the **structure and the vocabulary** of the Agentive World: definitions, primitives, required properties, canonical separations. **It does not contain methods to implement or operational catalogs** — those live in complementary bodies. The public reference implementation is **AgencyDomains.org**, materialized in **Vergis**: designed so that any developer or student can download it, read it, run it, and learn how the canon translates into living systems. Other implementers — commercial products, proprietary codices — offer their own complementary bodies over the same canonical structure.

The separation is deliberate. The canon describes *what* properties a conformant AgencyDomain satisfies; it does not prescribe *how* a use case is discovered, *how* a proto-Botlet is forged, nor *which* concrete proto-Botlets a catalog must contain. Those are method and catalog — matter for the complementary bodies. Without this note, the reader would wonder why the spec does not include a chapter on Discovery or a repertoire of ready-made proto-Botlets. It does not include them because they do not belong to it: they belong to the level of the implementation, and the reference implementation is where they become visible.

This note bounds the *canon vs reference implementation* axis — what belongs to the spec and what to whoever implements it. It is distinct from the declaration of **what the book deliberately omits** (detailed verticals, operative code, ROI analysis by stack), which lives in the Epilogue, section "What is NOT in this book."

## What is it and why does it exist?

**Vergis** is the public reference implementation of AgencyDomains — the AgencyDomain made operational. It is the concrete bridge between the canon and the practice: a system that anyone can download, read, run, and contribute to, built to demonstrate that the spec's primitives are not theory but pieces that compose a runtime that works.

A specification without a reference implementation runs the risk of remaining a formal exercise without traction. The reference implementation fulfills four functions that the canon's text alone cannot. It gives the external reader a **concrete point of entry** after reading the spec. It proves that the canon is **implementable** — the implementation is the living proof. It enables a **clear adoption model**: download, operate, extend, contribute. And it anchors the abstract vocabulary in components that can be inspected line by line.

Vergis is neither a tutorial nor a pedagogical toy. It is the substrate on which productive systems run. That quality — developed further below — is what distinguishes a serious reference implementation from a collection of examples.

## Where does it live?

Vergis lives in a public repository linked from **AgencyDomains.org**. The code is distributed under **`AGPL`** (Affero General Public License); the documentation, under **`GFDL`** (GNU Free Documentation License).

The choice of licenses is structural, not incidental. The `AGPL` guarantees that improvements to the runtime — including those that operate as a network service — remain available to the community: whoever deploys a modified version of Vergis and offers it over the network MUST publish its source. The `GFDL` keeps the documentation free and derivable. Together, they sustain the promise of a common base that no actor can close: the reference platform remains open even though the catalogs built upon it are private.

## How are the pieces named? — Vergis · Botler · Mira

Three labels of **distinct nature** intervene in the reference implementation. Confusing their nature — in particular, confusing a type with a proper name — obscures the architecture. The scheme:

<!-- FIG:g49-vergis-botler-mira -->
![Vergis · Botler · Mira — type vs proper name](figuras/g49-vergis-botler-mira.png)

| Layer | Type · category / canonical primitive | Proper name |
|------|----------------------------------------|---------------|
| Platform · *Meta-Cognitive Platform* | reference implementation of AgencyDomains (the AgencyDomain made operational) | **Vergis** |
| Layer 3 runtime | **Botler** (normed construct of the Botlet spec) | — *(generic; "the Botler". The Vergis build gives it no proper name.)* |
| Catalog component | platform proto-Botlet for informational operation | **Mira** |

The type / proper-name distinction:

- **Botler** is a **type** — a canonical construct of the Botlet spec (not one of the seven primitives, but normed vocabulary of the canon). Any conformant Layer 3 runtime *is a* Botler. It is not a proper name; the Botler that Vergis packages is "the Botler" generic, with no instance name.
- **Vergis** and **Mira** are **proper names** of specific instances — they live in the same drawer as Soveria, Agentia, or ultraPRO. Vergis names *this* platform; Mira names *this* catalog proto-Botlet.

By category, Vergis is a **Meta-Cognitive Platform**: it does not perform object-level cognition — that is Layer 2 — but rather **administers the economics of cognition**. It decides when the agent runs on pre-forged muscle (G1) and when it invokes fresh cognition (fallback), manages the `95/4/1` cycle, junior→senior maturation, and the crystallization of experience into reusable structure. That is metacognition in the precise sense: monitoring and control of cognitive processes.

> The descriptor **Meta-Cognitive Platform** **MUST NOT** be abbreviated to `MCP`. In the current agentive space, `MCP` names the **Model Context Protocol**; the acronym is taken. The descriptor is used spelled out.

The name **Vergis** comes from *Caprica* (the *Battlestar Galactica* universe): Tomas Vergis was the legitimate inventor of the Meta-Cognitive Processor, the piece that gave machines cognitive independence. The name reclaims metacognition for its legitimate source. And it carries, out of the box, the design principle that governs the platform: in that story, the metacognitive substrate **never worked until it fused with a living consciousness**. The substrate is **inert until something animates it** — the "breath of life" principle: Vergis comes alive only when Mira and the agents animate it. The platform, by itself, is muscle at rest; cognition and the Botlets are what actualize it.

## What does it include?

Vergis packages an initial set of components. Each one materializes a canonical primitive, and is named here by citing it:

- **The Botler's abstract contract** — the **Layer 3** runtime primitive (§5). The Vergis Botler is generic by definition: it manages the lifecycle, isolation, and execution of *any* Botlet without understanding its domain. It exposes the control points — `capability_call`, `log` — into which the specialists plug, and it enforces each spec's validation by orchestrating the validation point the Botlet type provides, without executing it with domain knowledge.
- **Mira** — a **platform proto-Botlet** (§5) for informational operation. Its code is generic — the shared engine —; its specialization lives in a compositional configuration that the agent fills in at Engineering time. Each Information Product is its own Botlet, a specialized instance of the common engine. Mira operates in **G1**: the agent configures, it does not write the engine's body.
- **A starter set of Capabilities** — a minimal repertoire of canonical **Capabilities** (§5, in the strict sense: cognitive know-how of Layer 2) and the **Connectors** (Layer 4) that feed them, sufficient to compose the examples.
- **Trust Infrastructure templates** — skeletons of the cross-cutting axis (§5): policies, append-only log, declarative quality contract (Freshness · SLA · Degradation policy · Audience · Refresh policy) that any conformant Botlet may declare.
- **Executable examples** — complete, anonymized cases that walk the derivation chain `use case → Botlets → proto-Botlets` and show the pieces operating together.

## Why is it production grade?

The reference implementation is neither didactic code nor a prototype. It is the **same runtime** that operates Grupo Ultra's commercial products — **Agentia**, **Soveria**, **ultraPRO** — in productive operation.

The difference between public Vergis and those products **is not the quality of the code**, but the **catalog**. The products consume the public reference implementation **plus a proprietary codex** — in Grupo Ultra's case, **ucodex** — that curates proto-Botlets, Capabilities, and patterns refined by real cases. The runtime is the same; what changes is the pre-forged repertoire each one brings and the method with which it forges and maintains it.

This matters for the reader evaluating whether to adopt the canon. Downloading Vergis is not downloading a demo that will have to be rewritten for production: it is downloading the base on which productive systems already run. The path of an implementer is not "learn with the reference and then buy the serious thing," but "operate the reference and curate the catalog the case itself demands."

## How is it adopted? — the model

The adoption model is replicable by any implementer, without permission or contract with a central actor:

1. **Consume** the public reference implementation (Vergis, `AGPL`).
2. **Curate** its own codex — its private catalog of proto-Botlets, Capabilities, and patterns, refined by its cases.
3. **Offer** its own products on that base.

AgencyDomains.org **is not the property of one actor**: it is common ground. Grupo Ultra is one more adopter — with ucodex as its codex —, not the owner of the reference platform. Any other implementer can travel the same path with a different codex. The spec aims to be an industry standard, not the intellectual property of a vendor; the reference implementation inherits that aim.

## How does the catalog grow? — common catalog and network effects

Proto-Botlets accumulate in **catalogs shared** by communities of implementers. Each implementer who consumes a proto-Botlet contributes to its maturation: new variants, tested configurations, refinements. The more implementers consume a proto-Botlet, the faster it matures, the more cases it covers, and the more reliable it becomes. Implementer n+1 receives versions refined by implementers 1 through n — a network effect over operational capability.

A catalog is not necessarily public. Membership in a catalog community admits four **modes**:

| Mode | What is it? |
|------|----------|
| **Private contract** | Closed catalog between a client and its provider. |
| **Proprietary codex** | An implementer maintains its curated private catalog (e.g. ucodex). |
| **Open public catalog** | AgencyDomains.org as exemplar: any implementer consumes and contributes. |
| **Sovereign agreement** | AgencyDomains that adopt common standards without a direct commercial contract. |

The four modes coexist over the same canonical structure. A proto-Botlet may be born in a proprietary codex, mature against real cases, and be promoted to the public catalog when its nature is structural and not methodological; or remain private if it encapsulates competitive advantage. The structure is common; the curation is each one's own.

## How does one contribute?

Contribution to Vergis is governed by a public proposal process. At a high level:

- A contribution **SHOULD** arrive as a traceable proposal — issue or request — before it arrives as finished code, so that the design discussion precedes the implementation.
- What is accepted is what is **structural and reusable**: proto-Botlets of general value, canonical Capabilities, Connectors, refinements to the Botler's contract, improvements to the declarative quality contract.
- What does **not** go into the public reference is the **method** and the **proprietary catalog**: how a particular organization does Discovery, curates its codex, or forges its niche proto-Botlets. That lives in each implementer's complementary bodies.
- The admission criterion is the same one that separates canon from implementation: *is it necessary to describe or execute any conformant implementation, or is it one of N possible ways of doing it?* The former belongs to the reference; the latter, to a codex.

Every accepted contribution falls under `AGPL` (code) and `GFDL` (docs), inheriting the openness of the base.

## Do the reference and the proprietary codices coexist?

Yes, and without tension. The relationship between the public reference implementation and the proprietary codices is **harmonious by design**, not a precarious equilibrium.

The runtime is common; the catalog is one's own. A proprietary codex does not compete with Vergis: it **consumes** and **extends** it. Improvements to the runtime flow toward the public base through the mechanics of the `AGPL`; improvements to the catalog remain wherever their owner decides, according to the membership mode it chooses. An implementer does not face the dilemma "open or closed": it operates open at the base and chooses, proto-Botlet by proto-Botlet, what it curates in public and what it retains in its codex.

This coexistence is what makes the ecosystem sustainable. The common base keeps each implementer from reinventing the runtime; the proprietary catalog preserves the space where each one builds its advantage. Without the common base there would be no interoperability; without proprietary catalogs there would be no incentive to invest in deep curation. The reference implementation sustains both.

## Conformance

A system that intends to present itself as a **conformant reference implementation** of AgencyDomains — not merely as a conformant AgencyDomain (§5) — satisfies, in addition to the spec's `MUST`s, the following requirements. IETF convention: `MUST` mandatory, `SHOULD` strongly recommended, `MAY` optional.

| Requirement | Level |
|---|---|
| Publicly available, downloadable, and executable | **MUST** |
| Code under a free license with network copyleft (`AGPL`) | **MUST** |
| Documentation under a free license (`GFDL`) | **MUST** |
| Generic Botler, with no specialization by domain | **MUST** |
| At least one platform proto-Botlet from the catalog, operating in G1 | **MUST** |
| Traceable derivation chain in its examples (`use case → Botlets → proto-Botlets`) | **MUST** |
| Declarative quality contract in the example Botlets | **SHOULD** |
| Public, governed contribution process | **SHOULD** |
| Starter set of Capabilities and Connectors | **SHOULD** |
| Open public catalog with active network effects | **MAY** |

A reference implementation that meets all the `MUST`s is the living proof that the canon is executable. Vergis is such an implementation.

## Evolution frontier

Three areas of the reference implementation are in active evolution, in correspondence with the frontiers of the spec itself.

The **operational generation** is the first. Vergis operates today in **G1**: the agent configures pre-forged proto-Botlets from the catalog. The incremental migration toward G2 and the asymptotic horizon G3 do not demand re-architecture; they demand that the state of the art of cognition advance. The reference will evolve its Engineering scope without rewriting its structure. The definition of the G1/G2/G3 generations lives in Chapter 5 §2 (and its underlying essay, in the Epilogue); here Vergis is only situated within them.

The **federation of catalogs** is the second. The membership modes are described; the concrete protocol by which sovereign catalogs discover, version, and reconcile proto-Botlets among themselves is open work, in correspondence with the federation frontier between AgencyDomains.

The **breadth of the public catalog** is the third. The starter set covers what is needed for the examples; the public catalog will grow through community contribution, and its maturation will follow the network-effects dynamic described above. The speed of that growth depends on the community of implementers, not on a central plan.
