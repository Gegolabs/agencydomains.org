## Capabilities

When an experienced finance consultant faces a new problem at a client, they do not start from scratch. They bring along an organized body of know-how that they apply to the particular case: accounting principles, regulatory frameworks, analytical frameworks, professional practices that the industry has consolidated over decades. When an operations consultant tackles a supply-chain problem, they do the same with their own body of knowledge: SCOR, Six Sigma, lean manufacturing, demand planning. Every professional discipline has its tree of know-how, and the consultant's quality depends in good part on how deep and well organized that tree is in their head.

AI agents face the same problem. An agent operating in finance needs to know finance; an agent operating in legal needs to know legal; an agent operating in marketing needs to know marketing. But "knowing" in this context does not simply mean that the underlying model read finance documentation during training. It means that the agent has modular, composable access to an organized body of professional know-how that it can apply selectively according to the task. This organization is what the Agentive Architecture calls **Capabilities**.

This section develops the concept of Capability as the canonical primitive of Layer 2 (Cognition). What makes the Capability special with respect to other nearby concepts in the field is its **hierarchical structure**, its **composability**, and its explicit distinction from plugins and prompts. An agent without Capabilities has monolithic cognition that conflates domains; an agent with well-organized Capabilities operates with the discipline of a professional who knows the distinctions of their field.

### Definition

A **Capability** is a unit of specialized know-how that an agent understands and applies. It encapsulates the procedural and declarative knowledge of a domain: what is known, how it is applied, what is decided, what is asked when data is missing. Capabilities reside in **Layer 2 (Cognition)** of the Agentive Architecture. Cognition selects and applies Capabilities according to the task — in the same way that an expert consultant selects and applies professional frameworks according to the problem in front of them.

> *The agent does not know what the model knows. It knows what its Capabilities allow it to know.*

The quotation above distinguishes what Layer 2 knows from what the underlying model knows. The underlying model — Claude, GPT, Gemini — was trained on a massive amount of information that includes, among many other things, professional knowledge. But the agent that lives in Layer 2 **does not operate directly with the model's knowledge**. It operates with the Capabilities assigned to it, which are specific curations of know-how applied to particular contexts. An agent that has the *General Ledger* Capability but not the *Tax* Capability answers with authority on general accounting but knows that it is not the right source for tax questions. An agent without specific Capabilities operates with the model's diffuse knowledge, which may be correct in general but is rarely precise on the professional plane.

### What is NOT a Capability?

To fix the definition with the precision the spec demands, we contrast the Capability with neighboring concepts that the industry uses carelessly. Each of these neighboring concepts has its legitimate role in AI systems, but none is a Capability, and conflating them leads to architectures that end up being poorly integrated collages.

The term **Capability** is reserved, in the strict sense, for the **cognitive know-how** of **Layer 2 (Cognition)**: knowledge that interprets, decides, and reasons about a domain. This reservation matters because other agentive deliverables — connections to source systems, presentation makings — live in other layers, have a different nature, and are built with their own development schemes. Treating them all as Capabilities would force a qualifier onto the term at every use and dilute its value. The section *Capability, Connector, and Template — three deliverables per layer* fixes the proper terms for each layer.

A **plugin** lives in the context of a host application. It extends that application with a new function. It is tied to the host: the Excel plugin only operates within Excel, the Notion plugin only operates within Notion. A Capability is not tied to a host — it lives in the agent's Capability tree and is invocable from any context where the agent operates.

A **prompt** is a specific linguistic formulation injected into the model on a particular invocation. Prompts are useful, but they are a transient artifact: they change from invocation to invocation, they do not encode persistent knowledge. The Capability can use prompts internally as one of its implementation mechanisms, but it does not reduce to a prompt. A well-designed Capability includes vocabulary, procedural knowledge, declarative knowledge, heuristics, and references to tools — the prompt is only one of the components.

A **system prompt** establishes the model's general tone and behavior. It is configuration of the mode of operation, not modular know-how. Capabilities **are not system prompts** — they can coexist with one, but they capture something else: domain knowledge applicable according to the task, not the agent's global configuration.

A **tool** lives in Layer 4 (Access). It is an executable action on the external world: invoking an API, reading a file, sending an email. The Capability **decides which tool to invoke and how to interpret its result**, but it is not the tool itself. The Capability is knowledge; the tool is action. A finance agent with the *Treasury* Capability knows when and how to invoke the tool that queries bank balances — but the tool itself is a separate component that lives in another layer.

A **skill**, in the field's popular terminology, is a term the industry uses so carelessly that it has practically lost meaning. Various vendors call "skills" plugins, prompts, tools, configurations — without precise distinction. The Capability is not a skill in the generic sense, but the partial overlap of popular usage may confuse the reader. To avoid the confusion, this book reserves the term Capability with a precise definition and avoids using "skill" except when quoting sources that use it.

Three traits distinguish a genuine Capability. **Modular**: it can be activated or deactivated independently of the others. If an agent has *Finance* and *Legal* Capabilities and *Legal* is withdrawn, the agent keeps operating coherently with *Finance* alone. **Composable**: multiple Capabilities can coexist in a single agent and combine when the task crosses domains. An agent that has *Finance* and *Operations* can handle a logistics case with financial components without tripping in the transition. **Knowledge, not action**: the Capability knows; the tools (Layer 4) act. The Capability decides which tool to invoke and how to interpret its result.

### Capability, Connector, and Template — three deliverables per layer

An agentive delivery project rarely delivers only a Capability. The cognitive Capability is the protagonist, but it usually comes accompanied by deliverables that live in other layers and are built with different schemes. The spec canonizes three terms, one per layer, so that each deliverable is named for what it is without qualifying the term Capability.

<!-- FIG:g28-tres-entregables -->
![Three deliverables per layer — Capability (Layer 2) · Connector (Layer 4) · Template (Layer 1)](figuras/g28-tres-entregables.png)

A **Capability** (strict sense) is **cognitive** know-how — interpretive, decisional. It lives in **Layer 2 · Cognition**. It is the project's protagonist.

A **Connector** is knowing how **to access source systems** — a connection with execution power. **It is not cognitive knowledge.** It lives in **Layer 4 · Access**. The Connector is what the pre-agentive field knows as the technical integration that touches the external world. A legacy API, when brought into the Agentive World, becomes a **Connector** (Layer 4), not a Capability.

A **Template** is the **client-specific making** over a canonical instrument — a report or dashboard that the Capability produces — in a particular format or rule required by the client. It lives in **Layer 1 · Interaction**, alongside the Facet, the surface Botlet, and the view Botlet. Anonymized examples: a regulatory template of a basic interconnection offering over the canonical cost report; a managerial monthly financial-close format over the canonical profitability dashboard. The Template is not a Capability, not a Facet, and not a Botlet: the buyer already knows the term "template" from the pre-agentive vocabulary and does not need to learn a new one.

#### How is each deliverable developed?

Each term has its layer, its nature, and its own development scheme:

| Deliverable | Layer | Nature | Development scheme |
|---|---|---|---|
| **Capability** (protagonist) | Layer 2 · Cognition | Cognitive, interpretive, decisional know-how | Wingtraining 5 steps (SME workshop · creation · customization · ALPHA · BETA) |
| **Connector** (companion, if it requires access to source systems) | Layer 4 · Access | Knowing how to access systems; not cognitive knowledge | Integration scheme (survey · configure · test · certify) |
| **Template** (companion, if the delivery must conform to a presentation expectation) | Layer 1 · Interaction | Making of a canonical instrument in a client format or rule | Making scheme (survey the expectation · make over the canonical instrument · validate) |

#### What is the conceptual structure of an agentive delivery project?

An agentive delivery project is structured as a **protagonist Capability** (Layer 2) typically accompanied by one or more **Connectors** (Layer 4) and one or more **Templates** (Layer 1). In addition, the Capability itself produces, with no extra effort, its **information instruments** — canonical reports and dashboards —, which remain implicit in the delivery: they require no development scheme of their own because they emerge from the Capability and its interaction layer. The Template appears only when one of those instruments must conform to a specific client form.

#### Capability or deliverable of another layer? — the test

To decide whether a scope is a Capability in the strict sense, the following three tests must all be **yes**:

1. **Is it cognitive know-how?** Does it interpret, decide, or reason about a domain — beyond merely connecting or merely formatting?
2. **Does it have an identifiable SME?** Is there a human expert whose knowledge is transferred to the agent?
3. **Does it pass through the five Wingtraining steps without forcing?** Does it make sense to apply SME workshop · creation · customization · ALPHA · BETA to it?

If one or more are **no**, the scope is not a Capability: it belongs to another layer — Connector or Template, per the mapping in the section *Capability, Connector, and Template* — or, if it is cognitive knowledge but subordinate to a larger Capability, it is a **feature** of that Capability (see the next section).

### The hierarchical structure — the tree of knowledge

<!-- FIG:g29-arbol-capabilities -->
![The tree of knowledge + functional × vertical orthogonality](figuras/g29-arbol-capabilities.png)

Capabilities are organized in a **hierarchical tree**. The structure is not decoration — it is the natural way professional knowledge is organized in any serious discipline. Financial analysts think hierarchically: finance has sub-disciplines (accounting, corporate finance, treasury, tax), each sub-discipline has areas (general ledger, accounts payable, reconciliation), each area has specific practices. The hierarchical organization reflects how the professional masters the field.

Below is an example of the canonical tree the spec proposes as a starting point. The tree is not exhaustive — it extends according to the needs of each implementation —, but it illustrates the structure (figure above).

Four structural rules govern the tree. The first: **any node is a valid Capability**. Both leaf nodes — *Reconciliation*, *Demand generation*, *Quality* — and intermediate nodes — *Accounting*, *Sales & Marketing*, *Manufacturing* — are valid Capabilities. Granularity is decided by context. An agent specialized in daily accounting operation adopts leaf nodes with high specificity; an orchestrator agent that coordinates several specialists adopts intermediate nodes with a panoramic view; a multi-specialist agent combines several roots.

The second rule: **it is composable**. Capabilities can be shared across agents. A *Customer success* Capability can live in a commercial team's agent and simultaneously in a support team's agent, without duplication. This is operationally critical — the organization does not need to re-build the knowledge for each new agent, but rather assigns already-built Capabilities according to the agent's role.

The third rule: **it is scalable**. New branches are added without breaking the existing ones. The *Telecom* Capability can rise in sophistication — adding sub-branches *Network APIs*, *5G core*, *Customer experience* — without the other branches of the tree changing. This property is what allows the tree to grow with the organization: each time the organization enters a new domain, it adds branches; each time it deepens an existing domain, it extends branches. The tree never needs a complete rewrite.

The fourth rule: **it is inheritable**. A Capability inherits context and vocabulary from its ancestors. A *General Ledger* Capability does not need to re-explain what Accounting or Finance is — that contextualization comes from the tree. This matters in implementation because it allows leaf Capabilities to be more concise: they only need to describe what is specific to their node, not what is already implicit in the tree path.

### Anatomy of a Capability

The canonical specification of a Capability includes nine components, which we lay out one by one. Components one and nine are metadata; components two through seven are the body of the know-how; component eight is the binding with the action layer.

The first component is **identity**: canonical name plus position in the tree. Identity is what makes the Capability referenceable — agents invoke it by name, policies are applied to specific Capabilities, logs record which Capability was invoked.

The second component is **vocabulary**: technical terms of the domain that the agent must recognize and use correctly. An agent with the *General Ledger* Capability must distinguish debit from credit without hesitation, must know the difference between manual and automatic entries, must use the concept of fiscal period correctly. Vocabulary is what allows the agent to converse with domain professionals without sounding amateur.

The third component is **procedural knowledge**: how the typical tasks of the domain are done. How an account is reconciled. How an invoice is validated. How a monthly close is prepared. Procedural knowledge is sequential and operational — it describes steps, not just concepts.

The fourth component is **declarative knowledge**: verifiable facts and rules of the domain. That accounts payable have due dates. That revenue is recognized when certain criteria are met. That bank reconciliation must occur monthly. Declarative knowledge is factual and permanent — it describes what is true of the domain.

The fifth component is **heuristics**: professional decision rules of the domain. When an invoice deviates more than five percent from the typical amount, escalate. When a reconciliation has more than ten unmatched transactions, suspend the process and escalate. When a supplier has three claims in six months, flag for review. Heuristics are professional judgment encoded — they capture not what is true of the domain, but what decision a professional would make in each situation.

The sixth component is the **associated tools**: Layer 4 tools that the Capability typically invokes. The *General Ledger* Capability invokes tools that query the accounting database, that post entries, that generate reports. The Capability declares which tools it uses so that the agent knows what it needs available when it exercises that Capability.

The seventh component is the **parent Capabilities**: the hierarchical position from which the Capability inherits context. A *General Ledger* Capability declares that it is a child of *Accounting*, which in turn is a child of *Finance*. The declaration of parents is what enables the inheritance described in the previous section.

The eighth component is the **maturity state**: Draft / Active / Deprecated. The maturity state is operational metadata — it lets the organization manage the lifecycle of its Capabilities. A Capability in Draft is still being validated; an Active one is approved for productive use; a Deprecated one is legacy that is kept for compatibility but should not be used in new agents.

The ninth component is **version**: traceability of evolution. Capabilities change over time — professional practices evolve, regulations change, accumulated knowledge is refined. Versions let the organization track the evolution of knowledge and let different agents operate with different versions according to their requirements.

Components two through five — vocabulary, procedural, declarative, heuristics — are what **deeply differentiates** a well-built Capability from an elaborate prompt. A prompt gives the model context transiently, for a single conversation. A Capability encodes professional knowledge with persistence and modularity. The difference is structural: the agent can consult the *General Ledger* Capability without the accounting knowledge flooding all its other conversations — it can at the same time have the *Marketing* Capability without marketing frameworks contaminating the accounting rigor. This separation is what allows agents to operate with the discipline of a professional who switches frameworks according to the task.

### Features of a Capability

A Capability exposes internal operations. The spec canonizes the term **feature** to name them — the practical equivalent of what other vocabularies call *feature*, *operation*, *skill*, or *method*. A feature is an internal operation that the Capability exposes; it shares with the containing Capability its data model, its SME, its installation, and its runtime. A single costing Capability, for example, exposes as features cost allocation, profitability, and *pricing*: three dimensions of a single know-how, not three Capabilities.

#### Capability or internal feature? — the test

A scope is treated as its own Capability if and only if the following three tests are **yes**:

1. **Operational independence?** Can it be installed and operate without the other capability?
2. **Cognitive identity?** Does it have a data model and SME distinct from the other capability?
3. **Reusability?** Does it have value for more than one consumer or context outside this case?

If one or more are **no**, the scope is a **feature** of the containing Capability, not its own Capability.

#### ID convention

An implementation MAY adopt an identifier convention to trace the tree of deliverables: the Capability (or deliverable) carries the ID `E<n>` —`E1`, `E2`—; the feature carries the composite ID `F<n>.<m>` —`F1.1`, `F1.2`— where `<n>` is the ID of the containing Capability. The convention is optional; what is canonical is that the feature construct has a name.

#### What pathologies does the test prevent?

Distinguishing feature from Capability prevents two pathologies observed in real projects:

- **Inflation of the deliverable codomain** — dimensions of a single Capability are documented as separate Capabilities, multiplying the inventory and diluting portability. The costing example already cited —allocation, profitability, and *pricing* treated as three Capabilities when they are features of a single one— is the typical case.
- **Hiding lock-in** — scopes that really are their own Capabilities, with independent lifecycle, data model, and reusability, end up embedded as "sub-capabilities" of another, hiding that they could be installed and ported separately.

The two tests are applied in order: the first decides whether the scope is cognitive at all; only then does the second decide its granularity within Layer 2. If the scope is not cognitive, it is classified directly as Connector or Template by its layer, without running the feature test.

### How does cognition operate over Capabilities?

Given an agent with a set of active Capabilities, when the agent receives a request, the processing follows a canonical seven-step flow.

**Step one**: the user's request reaches the agent. The agent receives it in natural language — *"reconcile last month's revenue account"*, for example.

**Step two**: cognition classifies the domain of the request. This operation is semantic routing — the agent identifies that the request is about accounting, specifically reconciliation. This identification is based on the vocabulary that the active Capabilities provide to the agent.

**Step three**: cognition selects the relevant Capabilities. In the example's case, *Finance/Accounting/Reconciliation* is the most specific applicable Capability. Cognition selects it together with its ancestors — Accounting, Finance — to have all the inherited context.

**Step four**: cognition applies the procedural and declarative knowledge of the selected Capabilities. It knows what steps make up a reconciliation, what rules it must follow, what typical errors it may encounter.

**Step five**: cognition invokes the tools the Capability indicates. It queries the accounting database for last month's entries, queries the bank statement, runs the matching process.

**Step six**: cognition composes the response using the domain's vocabulary and the Capability's heuristics. It reports the matches found, the unmatched items, the recommendations on how to proceed with the discrepancies. It uses terminology that an accounting professional would recognize as correct.

**Step seven**: if the request is repetitive — the agent has already done similar reconciliations in the past —, Pattern Recognition suggests generating a Botlet that automates the cycle one through six for future similar requests. Cognition evaluates the suggestion and, if conditions are appropriate (high frequency, stable pattern), generates the Botlet.

An important observation: the Capability **does not execute** — it is executed by cognition. This matters structurally: the same Capability can be applied with different depth — fast and superficial, or slow and exhaustive — according to the agent's cognitive model and mode of operation. An agent with sophisticated cognition can apply the *General Ledger* Capability with all the rigor of an experienced controller; an agent with more limited cognition can apply the same Capability with the depth of a junior. The Capability defines the know-how; cognition defines how deeply it is applied.

### Industry verticals as root Capabilities

The tree includes a root dedicated to **industry verticals** — Telecom, Healthcare, Retail, Banking, Public sector. This is deliberate: each vertical has its own vocabulary, its own regulations, its own canonical processes. The existence of a vertical root separate from the functional roots (Finance, Sales, Operations) reflects a structural property of professional knowledge: verticals and functions are **orthogonal**.

A generalist finance consultant has functional knowledge — Finance — but no specific vertical knowledge. A finance consultant for telecom has both: Finance (the function) and Telecom (the vertical). The telecom consultant can apply generalist financial frameworks, but also knows the particularities of the sector — the revenue-assurance models specific to telecom, the regulations of the sector's regulator, the operational systems typical of a carrier. Vertical knowledge is **additional**, not a substitute, to functional knowledge.

The Capability tree reflects this orthogonality. An agent can simultaneously have *Finance/Treasury* and *Industry verticals/Telecom* Capabilities — and the combination produces an agent that operates with functional and vertical knowledge at the same time, exactly like the sector's expert consultant.

This architecture has two important consequences. The first: **vertical specialization is not a prompt — it is a Capability**. A "legal agent" or "medical agent" or "telco agent" is not a sophisticated prompt of the general model. It is an agent that loads the corresponding vertical Capability, with its own vocabulary, heuristics, and normative knowledge. This distinguishes Capabilities from generic System Prompts: vertical knowledge is modular, persistent, and composes with other non-vertical Capabilities without contamination.

The second consequence is commercial. This architecture explains the commercial success of the **vertical specialists** of today's market: Cursor (coding), Harvey (legal), Jasper (marketing), Fin (customer support). What these products sell is not "a specialized GPT" in their vertical — it is a robust vertical Capability that cognition applies with confidence. The difference from a generic GPT is not marketing; it is structural. The user who tries Cursor for programming does not notice that the difference is the *Coding* Capability the tool loads; they notice that the answers are correct more often than with a generic GPT, and that is exactly what the well-built Capability produces.

> *The vertical Capability is the difference between a useful agent and an agent serious about the domain.*

### Capabilities Marketplace

An emergent property of the architecture is that Capabilities admit a **market**. A well-built Capability can be distributed across AgencyDomains, versioned and maintained by a specialized provider distinct from the AgencyDomain operator, charged by subscription or license, and audited by third parties as to its correctness and completeness.

This gives shape to a **Capabilities economy** analogous to the open-source software package economy. Whoever builds and maintains expert Capabilities — for example *General Ledger* IFRS-compliant, or *Telecom 5G core* — can operate as a specialized provider without building agents or AgencyDomains of their own. Their product is the Capability itself. Their business model is license or subscription of the Capability. Their clients are organizations that operate AgencyDomains and need verified professional know-how.

The emergent economy has clear precedents. The software industry has had similar economies of specialized components for decades: compiled libraries sold or licensed, certified modules for specific frameworks, best-practice configurations that consultancies sell as assets. The Capabilities economy would be the natural evolution of those models to the agentive field.

The normative specification of the **Capabilities Marketplace protocol** — package format, versioning model, signature system, charging model — is **open work** in version 1.0 of this book. Contemporary implementations may adopt ad-hoc packages; consolidation as an industry standard is pending. When consensus arrives, a future version of the book will incorporate it as normative spec.

### Locality and availability — operational classification of Capabilities

The canonical description above treats Capabilities as access to know-how applicable in any context. The operational reality of systems with multiple physical presence — restaurants with locations, bank branches, retail stores, industrial plants — requires an additional classification that the spec formalizes explicitly: **locality** and **offline availability**. Without that classification, decisions about which Capabilities can be invoked from an edge Botlet in offline mode are made in the dark.

The classification operates over **two orthogonal axes**:

#### Locality axis

Where the Capability's components physically reside:

- **Cloud-resident** — the Capability lives in a remote service. Canonical examples: Capability `DTE-SII` (Chile's SII service for issuing electronic receipts and invoices), `Transbank-Onepay` (bank gateway), `Stripe-Connect` (payment processing). The agent invokes them over the network; without network there is no Capability.

- **Edge-resident** — the Capability lives at the physical site, associated with local hardware or systems. Canonical examples: Capability `ESC/POS-Printer` (thermal printer for tickets and receipts with the ESC/POS protocol connected by USB or serial), `Cash-Drawer` (the cash drawer of the till), `Local-Pinpad` (card pinpad connected to the POS), `Sensor-Temperatura` (cold-room sensor connected by GPIO). The agent invokes them against the site's hardware; they need no network to operate.

- **Hybrid** — the Capability has a local component and a cloud component. Canonical examples: Capability `Client-DTE` (signs the document locally, queues it if there is no network, sends it to the SII when the network returns), `Client-Pinpad-Deferred-Processing` (authorizes locally with PIN and batch, sends to the acquirer when the network returns). The local part operates offline; the cloud part synchronizes when there is network.

#### Offline availability axis

Whether the Capability can execute without network:

- **Online-only** — requires network to execute. Without network, the invocation fails. Cloud-resident Capabilities are typically online-only in the strict sense, although some have variants with a local client that turn them hybrid.

- **Offline-capable** — executes without network. If its external contract eventually requires cloud communication (a voucher that must reach the SII, a transaction that must consolidate at headquarters), it **queues** and emits outward when the network returns. Edge-resident Capabilities are typically offline-capable; hybrid Capabilities are too, by design.

#### Canonical classification matrix

Each conformant Capability explicitly declares its position in the matrix:

|   | Online-only | Offline-capable |
|---|---|---|
| **Cloud-resident** | DTE-SII (without local client) · Transbank Onepay · weather API | (unusual combination; typically migrates to hybrid) |
| **Edge-resident** | (unusual combination) | ESC/POS-Printer · Cash-Drawer · Sensor-Temperatura · Local-Pinpad |
| **Hybrid** | (unusual combination) | Client-DTE · Client-Pinpad-Deferred-Processing · Sync-Inventario |

#### Connection with distributed Layer 3

The classification is structurally necessary when Layer 3 is distributed (Chapter 5 §1). An edge Botler must **know** which Capabilities it can invoke offline. If it does not know, its edge Botlets will attempt to invoke cloud-resident Capabilities without network and will fail catastrophically — without network, not even the agentic fallback applies, because cognition lives in the cloud.

The operational rule the classification enables is direct: **a senior edge Botlet, at a physical site without network, operates by invoking exclusively edge-resident Capabilities and the local part of hybrid Capabilities**. The cloud-resident ones and the cloud part of the hybrids remain temporarily inaccessible; the deferred effects (sending to the SII, consolidation with headquarters) are queued; when the network returns, the queues drain.

#### Required properties

| Property | Level | Description |
|---|---|---|
| Explicit declaration of locality | **MUST** | Cloud-resident, edge-resident, or hybrid. |
| Explicit declaration of offline availability | **MUST** | Online-only or offline-capable. |
| Specification of offline behavior for offline-capable | **MUST** | What it does when there is no network, what it queues, how it drains. |
| Deterministic resolution of which component runs in hybrids | **MUST** | Under what conditions the local component runs; under which it invokes the cloud. |

### Capability portability

The previous section classifies *where* a Capability physically resides — cloud, edge, or hybrid. A distinct property, which the spec formalizes explicitly, is **Capability portability**: a conformant Capability can be installed and run on **any conformant AgencyDomain**, without rewriting. This portability is what makes the Capability **real property of the client** — not of the AgencyDomain that hosts it, nor of the hosting that sustains that AgencyDomain.

The argument is the same no-lock-in one the canon makes for the AgencyDomain, applied one level lower. Just as a conformant AgencyDomain migrates to another conformant hosting platform without being held captive by it, a conformant Capability migrates to another conformant AgencyDomain without being held captive by it. The client who acquires a Capability acquires a portable asset, not a rental tied to a platform.

#### The two portabilities?

It is worth not confusing two portabilities that operate at different levels:

| Portability | What migrates? | To where? |
|---|---|---|
| **AgencyDomain portability** | The complete AgencyDomain | To another conformant hosting platform |
| **Capability portability** | A single Capability | To another conformant AgencyDomain |

#### What is the Capability ↔ AgencyDomain relation?

The relation is asymmetric and explicit: an **AgencyDomain hosts and runs** Capabilities; a **Capability runs on** a host AgencyDomain. The Capability is a first-order inhabitant of the AgencyDomain's Layer 2 — the know-how that gives cognition to its agents —, not a support resource. This is the reason the canonical definition of AgencyDomain names Capabilities among what the AgencyDomain hosts and runs, on a par with autonomous agents and Botlets.

### Regulatory certification resides in the Capability, not in the Botlet

A structural property that appears with force in productive agentive systems in regulated industries — gastronomy, health, finance, retail with DTE, pharmacy, telecommunications — and which the spec needs to formalize explicitly: **the regulatory certification of operations resides in the invoked Capability, not in the Botlet that invokes it**. The separation is necessary because the generated nature of the Botlet makes it impossible to certify a priori, and certifying it a posteriori contradicts its regenerable nature.

#### The problem

The book defines that cognition generates the Botlet's code (Chapter 5 §2). But some operations a Botlet executes are **regulated**: issuance of DTE under SII norm, card payment under PCI-DSS, pharmaceutical dispensing under sanitary registration, financial communication under SBIF / SVS / equivalent norm. For these operations, **the regulation requires certification of the component that executes the operation**. A system that issues an electronic receipt without SII certification is not legal; a system that charges a card without PCI certification cannot operate.

If certification resided in the Botlet, each Botlet that executes a regulated operation would have to be certified individually. But a Botlet is **code generated by cognition** that regenerates when the environment changes. Each regeneration would produce a technically distinct Botlet that would require re-certification. Regulatory certification over Botlets turns the `95/4/1` cycle into an operational impossibility: each 1% change would require a regulatory process.

#### The canonical solution

The spec resolves the tension by separating responsibilities with discipline:

- **The Botlet orchestrates**. It knows the process flow, validates operational pre-conditions (are there products?, is the table open?, does the customer have their tax ID registered?), captures the event, formats the request according to the Capability's contract.
- **The certified Capability executes the regulated operation**. It receives the request from the Botlet, executes the regulated operation under all applicable norms, returns the voucher. The `DTE-SII` Capability receives the sale's detail, signs with the tax certificate, transmits to the SII, receives the folio and electronic stamp, returns the voucher to the Botlet.

The separation has three structural consequences:

**First, certification is of the certifiable component.** The `DTE-SII` Capability can be formally certified — its code is stable, its contract with the SII is explicit, its behavior is auditable. Certification is one-time work; it holds for all the Botlets that invoke it.

**Second, generated Botlets coexist naturally with regulatory compliance.** A `Charge-Table-9` Botlet that regenerates when the kitchen changes its menu does not break the tax certification — it keeps invoking the same certified `DTE-SII` Capability. The Botlet's regeneration affects orchestration logic, not the regulated operation.

**Third, the audit boundary becomes sharp.** When the regulator audits, the AgencyDomain exposes: the Botlet (business logic, mutable, regenerable) and the Capability (regulated operation, certified, auditable). The regulatory inspection concentrates on the Capability — where the certification resides —, while the business logic is governed with the Trust mechanisms of Chapter 5 §4 without contradicting the regulation.

#### Canonical pattern

The pattern applies to any regulated industry:

| Industry | Botlet (orchestrates) | Certified Capability (executes the regulated operation) |
|---|---|---|
| **Gastronomy** | `Charge-Table` | `DTE-SII` (electronic receipt or invoice) |
| **Banking** | `Process-Payment` | `Gateway-PCI-DSS` (tokenization + authorization) |
| **Pharmacy** | `Dispense-Prescription` | `Sanitary-Registry` (validation and registration of dispensing) |
| **Telecom** | `Activate-Service` | `Subtel-Registry` (regulatory registration of activation) |
| **Health** | `Issue-Prescription` | `MINSAL-E-Prescription` (certified medical signature) |

The pattern is uniform: the Botlet contains the mutable business logic; the Capability contains the certified regulated operation. The boundary between the two is the boundary between what the organization can freely regenerate and what it must keep frozen under certification.

#### Required properties

| Property | Level | Description |
|---|---|---|
| Regulated Capabilities declare their regulatory regime | **MUST** | Which norm it complies with, before which regulator, with what certification number. |
| Regulated Capabilities are immutable between audits | **MUST** | The certified Capability's code does not regenerate; it changes only under a regulatory process. |
| Botlets may invoke regulated Capabilities without restriction | **MUST** | The Capability's contract is stable; the Botlet invokes it like any other. |
| Auditability of the boundary | **MUST** | The log clearly distinguishes Botlet operations (business logic) from regulated-Capability operations (certified operation). |

### Capabilities and Botlets — the relation

Capabilities and Botlets live in different layers and solve different problems, but they interact in a structured way. The Capability lives in Layer 2 (Cognition). It is know-how. The Botlet lives in Layer 3 (Autonomy). It is learned doing. The Capability has the form of vocabulary plus procedures plus heuristics plus tools. The Botlet has the form of traditional executable code. The Capability is persistent and versioned. The Botlet is self-regenerable and ephemeral. The Capability is applied when the agent recognizes its domain. The Botlet is invoked when the agent recognizes the pattern. The Capability is created by human experts or by specialized providers. The Botlet is created by the agent's cognition, automatically.

The canonical interaction is the following: a Capability can give rise to multiple Botlets. The agent that applies *General Ledger* repeatedly for a specific company begins to generate Botlets that automate the routine steps of the process — classifying transactions, reconciling accounts, generating monthly reports — without invoking cognition. The Capability remains the same; the Botlets are the efficient residue of its repeated application in a particular context.

This relation is what allows the agentive system to scale economically. Capabilities are the stable knowledge that the organization acquires, maintains, evolves. Botlets are the efficient residue that cognition generates by applying Capabilities repeatedly in specific contexts. The organization invests in Capabilities; the Botlets emerge from use. The investment in knowledge generates savings in operation.

### Conformance

An implementation of Capabilities conformant to this specification must satisfy the following requirements:

| Requirement | Level |
|---|---|
| Hierarchical tree structure | **MUST** |
| Any node is a valid Capability | **MUST** |
| Composability across Capabilities | **MUST** |
| Anatomy with vocabulary + procedural + declarative + heuristics | **MUST** |
| Explicit versioning | **MUST** |
| Declared maturity state (Draft / Active / Deprecated) | **MUST** |
| Selection by cognition, not direct execution | **MUST** |
| Verticals as a dedicated root | **SHOULD** |
| Open marketplace | **MAY** (when the normative spec exists) |
| Explicit declaration of locality (cloud / edge / hybrid) | **MUST** |
| Explicit declaration of offline availability | **MUST** |
| Portability across conformant AgencyDomains | **MUST** |
| Regulated Capabilities: declaration of the regulatory regime | **MUST** |
| Regulated Capabilities: immutability between audits | **MUST** |

### Evolution frontier

Three active areas of evolution of the Capability primitive deserve mention.

The **Capabilities marketplace** is the first. The normative protocol is not yet consolidated; when it is, version 2.0 of this book will incorporate it.

**Cross-vertical Capabilities** are the second. How a Capability can be combined with multiple verticals without contradictions — an agent operating in finance for banking and for telecom simultaneously, for example — requires refinement of the inheritance mechanisms that version 1.0 of the spec describes.

**Capability auditing** is the third. How to certify that a Capability does what it says it does — that an *IFRS Compliance* Capability effectively reflects IFRS and not its informal approximation — is a governance problem that the field has not yet solved. The likely solutions will come from the side of traditional professional auditing adapted to the agentive context.
