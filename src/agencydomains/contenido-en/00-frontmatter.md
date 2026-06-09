# AgencyDomains

### Architecture of the Agentive World

**Author:** César Obach-Renner
**Publisher:** GegoLabs
**Edition:** Development draft · June 2026 · v0.4
**License:** GNU Free Documentation License v1.3 *(proposed)*

> **A note on the version.** This is a **pre-1.0 development draft**: references and figures may be reorganized between iterations up to version **1.0**, which will be the first stable public release. In this English edition the figures are still rendered in Spanish; their English versions are forthcoming. Comments and errata are welcome in the repository. The version history lives in `CHANGELOG.md`.

## About this book

The AI industry builds agents with the same attitude it built web applications with in 2005: each vendor with its own stack, no common contracts, no clear separation of concerns. Gartner projects that more than **forty percent of agentic AI projects will be cancelled before the end of 2027** because of costs, unclear business value, or inadequate risk controls. **Only twenty-one percent of organizations have mature governance over their agents.** The root cause is structural: the category lacks a shared formal architecture — and has no concrete name for the minimal unit of deployment.

This book proposes that name and that architecture. The minimal unit of deployment is the **AgencyDomain** — the computational scope where agents dwell, Botlets execute, and Trust Infrastructure is exercised. Around the AgencyDomain, the book defines a paradigm (**the Agentive World** — *post-applications*), a formal architecture (**four layers with distinct concerns**, organized in a parallel topology), a set of canonical technical primitives (**Botlets**, **Capabilities**, **Trust Infrastructure**), and a two-dimensional model for placing any actor in the AI market (**the AI value chain** — eleven links × four depths).

The book is **product-agnostic**. The formal constructs described here admit multiple implementations. The **public reference implementation** —Vergis— is developed in Chapter 9.

## Structure

| Chapter | Content |
|---|---|
| **Prologue** | *(to be written)* |
| **Preface** | Origin of the book · who should read it · how it is organized · on terminology |
| **1 · The Nadella Line** | The canonical question · Agentic vs Agentive · the CEOs · why it matters strategically |
| **2 · The Agentive World** | The consequences of the crossing · organizational transformation · the new economics of information · field data |
| **3 · Bounded Concerns Architecture** | The pre-agentive state · three layers and seven separations · the seventh Procedural/Agentic separation · mapping to the Agentive World |
| **4 · Agentive Architecture** | The four layers in parallel topology · **the agent's three times** (Preparation · Attention · Engineering) · Layer 2 ↔ Layer 3 interface via `MCP` · cross-cutting Trust Infrastructure · the Agent First principle · GUI generated on-the-fly · **composition of Layer 1** (shell · view · operation · **multi-view PI and drill-through**) · **Facet vs Botlet** |
| **5 · Primitives** | AgencyDomains (with distributed Layer 3 + portability) · Botlets (with maturity + seed/emergent + **proto-Botlet · manifestation · temporality** + generic Botler) · Capabilities (**strict to Layer 2** + locality + regulatory certification + **portability · feature · Connector · Template**) · Trust Infrastructure (with operational continuity + **declarative quality contract**) · Assistant vs Autonomous Agent · **Facets (sixth primitive — Layer 1) · declared bounded interaction** |
| **6 · Market** | The AI value chain · depths and archetypes · per-link deep-dives · the Carbon World |
| **7 · Canonical applications** | Real-time knowledge · Varnished Kimball · conversational BI |
| **8 · Operation** | Trust Infrastructure operationalized · CRUDLEX · policies · operational business continuity |
| **9 · Vergis** | The reference implementation · note on the scope of the canon · the Vergis · Botler · Mira scheme · what it includes · production grade · adoption model · common catalog and network effects |
| **Epilogue** | Evolution frontier · **Botlet generations (G1/G2/G3)** · non-LLM cognition · federation · the Carbon World |
| **Appendices** | Glossary · references |


<!-- FIG:g01-lamina-indice -->
![Index plate · the four pillars of the proposal](figuras/g01-lamina-indice.png)


## Who should read this book?

This book is addressed to:

- **Systems architects** who design or evaluate agentive platforms and need a common frame for reasoning about separation of concerns, governance, and resilience.
- **CTOs and technical leaders** who must make agentive-stack decisions on a three-to-five-year horizon.
- **Strategists and consultants** who advise companies on their transit into the Agentive World.
- **Researchers and academics** interested in the formalization of agentive architecture as a category of study.
- **Product builders** who want to situate their contribution in a value chain broader than their particular product.

The book is introductory in the sense that it assumes no prior knowledge of specific implementations, but it does assume basic familiarity with distributed systems, language models, and operating systems in production.

## How to cite

> Obach-Renner, César. *AgencyDomains: Architecture of the Agentive World*. Development draft v0.4. GegoLabs, 2026.

## License

This book is published under the **GNU Free Documentation License v1.3** (proposed). The reader may copy, distribute, and modify the work under the terms of the license. The invariant section is the Preface.

The reason for the open licensing is deliberate: the Agentive Architecture aims to establish a category that serves the whole ecosystem, not a particular vendor. By adopting and developing it, other companies, researchers, and builders enrich it and consolidate it as a de facto standard. This serves the field and simultaneously reinforces the authority of those who coined it.

## Contact information

- **Website:** <https://agencydomains.org>
- **Repository:** <https://github.com/gegolabs/agencydomains.org>
- **Errata and comments:** <https://github.com/gegolabs/agencydomains.org/issues>
