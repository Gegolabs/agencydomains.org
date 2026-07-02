# Chapter 5 · Primitives

The four layers of Chapter 4 are the architectural answer to the paradigm, but they do not stand on their own: they need reusable pieces to populate them. This chapter delivers those pieces — the **canonical technical primitives** of the Agentive World. Each section formalizes one: the **AgencyDomain** (§1), the **Botlet** with its **proto-Botlet** (§2), the **Capability** (§3), the **Trust Infrastructure** (§4), the **Assistant vs Autonomous Agent** distinction (§5), and the **Facet** (§6).

## AgencyDomains

Chapter 4 introduced the notion of the AgencyDomain as the formal construction where the Agentive Architecture materializes. This section develops that notion with the detail of a specification. What follows is the closest thing to a *normative spec* that this book delivers — a document an implementer can take and build from, knowing what is mandatory and what is optional, what properties it must satisfy and what decisions it may make freely.

### Foundational premise — Space ≠ Domain

Words carry corporeality. **Space** is born describing physical extension: office, desk, home, city. When a human says *"my space"*, they invoke place — coordinates, walls, presence. The enterprise software industry extended the word to **WorkSpace** — Google Workspace, Microsoft 365, Notion — to name the collection of solutions that digitize what the person does at their physical desk: reading email, scheduling meetings, writing documents, filing. WorkSpace is the digital prosthesis of the human Space; both terms carry the same corporeality of origin.

The agent has no body. It does not open applications. It does not work on a desktop. It does not dwell in a physical space nor in any metaphor of one: it exercises agency over a **scope of computational jurisdiction** — digital territory where its identity rules, its Capabilities apply, and its Botlets run. The Latin word that names exactly that is **Domain** (`dominium`: scope of belonging and sovereignty).

> **Where the human has Space (WorkSpace), the agent has Domain (AgencyDomain).**

### The historical parallel — JSR-000148

The historical parallel holds: just as **JavaSpaces** (JSR-000148, 1999) formalized distributed spaces for Java systems without tying the implementation to a vendor, this specification formalizes **AgencyDomains** for agentive systems with the same agnosticism. Multiple implementations arose over JavaSpaces — GigaSpaces, Blitz, others —, all mutually compatible because they respected the common contract. The spec outlived the implementations; the implementations evolved without the spec needing constant rewriting. That is the pattern **AgencyDomains** seeks to replicate for the agentive field. This book proposes the spec; implementations that comply with it may call themselves **conformant AgencyDomain**.

The difference in name from its predecessor is not a rupture — it is precision. A Java *Space* was computational space for bodiless processes; an Agency *Domain* is a scope of jurisdiction for agents with agency. What in 1999 was named "space" is better named in 2026 as "domain". The term **AgencyDomain** carries meaning in each word. *Agency* — agency, in its philosophical sense of the capacity to act — denotes that the scope is inhabited by entities with their own initiative, not by passive processes. *Domain* — `dominium`: scope of belonging and sovereignty — denotes territory where the agent's identity rules, not an ephemeral process. The union of the two words names exactly what the spec defines: a scope where the agent exercises agency.

> Terminological note: in commercial lore (brand, sales, customer communication) the short form `Domain` replaces `AgencyDomain`. It is the Apple iCloud / CloudKit, Stripe Connect / Account pattern: short brand + long technical name. The two forms are interchangeable; each record picks its own.

### Definition

An **AgencyDomain** is a computational space with its own identity where autonomous agents and running Botlets dwell, where the **Capabilities** that give them their know-how are hosted and executed, and where the resources that sustain them live — cognition, tools, persistent storage. It constitutes the **minimal unit of deployment** of a productive agentive system.

The Capability is not a support resource: it is cognitive know-how, a first-order inhabitant of the space alongside the agent and the Botlet. The relation between the two primitives is direct — an AgencyDomain **hosts and executes** Capabilities; a Capability **runs in** a host AgencyDomain.

The spec defines how those spaces must be built — layers, identity, life cycles, communication protocols — without prescribing a specific implementation. Multiple implementations are admissible as long as they respect the contract. One implementation may use Kubernetes for containerization; another may use isolated microVMs; another may use native processes on a single machine. All three are valid if they satisfy the fundamental properties the spec requires.

> *Where an agent lives, that place is an AgencyDomain. Where there is no AgencyDomain, there is no life of the agent — there is model invocation.*

The quote above distinguishes the AgencyDomain conformant to this specification from any "endpoint that invokes an LLM". An endpoint that invokes an LLM responds to requests; an AgencyDomain **hosts agents that live**. The difference is structural, not one of degree. A system without persistent state, without its own Botlets, without the capacity for proactive operation, is not an AgencyDomain — it is a service. It can be a useful service, but it does not satisfy what the agentive field requires.

The minimal unit matters. An AgencyDomain is not a subcomponent of something larger — it is the atomic unit of deployment. A larger agentive system is a collection of cooperating AgencyDomains, possibly under a single governance or federated across distinct owners, but each one preserves its own identity and its fundamental properties.

### Fundamental properties

Every implementation that intends to call itself an AgencyDomain conformant to this spec must satisfy five fundamental properties. Satisfaction is not optional — a system that does not meet them is not an AgencyDomain, but something else with another name.

The first property is **own identity**. Each AgencyDomain has a unique identity — a canonical URI — that distinguishes it on any network. The identity survives the restart of the space, migration across infrastructures, and a change of implementation. If an AgencyDomain migrates from one cloud provider to another, its identity does not change: the agents that inhabit it, the humans who interact with it, the other AgencyDomains that invoke it, all continue to recognize it as the same space. The identity is stable, not ephemeral.

The second property is **materialization of the four layers**. An AgencyDomain materializes the four layers of the Agentive Architecture — Interaction, Cognition, Autonomy, Access — and exercises cross-cutting Trust Infrastructure. The materialization may be distributed technically — the layers may live in distinct infrastructures, on distinct physical servers, even across distinct cloud providers —, but responsibility for all four rests with the space. There is no conformant AgencyDomain that delivers only three layers, or that delegates some layer to an external system without assuming responsibility for it. Completeness is non-negotiable.

The third property is **persistence**. The state of the AgencyDomain — active agents, running Botlets, capabilities data, audit logs — survives disconnections, restarts, and migrations. An AgencyDomain is not an ephemeral process; it is a persistent entity. If the system restarts for maintenance, the agents that were active continue where they were. If the connection to an external service drops temporarily, the agent waits and resumes. Persistence is what makes the AgencyDomain a **place** and not a process.

The fourth property is **isolation**. Each AgencyDomain has an explicit boundary. Internal resources — compute, memory, data — are not accessible from outside except through defined interfaces. Communication with the exterior passes through Layer 4 (Access) and is recorded. Isolation is not only security — it is **fault containment**: an AgencyDomain that goes down does not affect other AgencyDomains that share infrastructure, because the boundary contains the failure. The implementation models that offer isolation vary — from strong sandboxing via MicroVMs to lighter isolation via Kubernetes namespaces —, but the explicit boundary always exists.

The fifth property is **addressability**. Both the AgencyDomain and the agents and Botlets that inhabit it are addressable via predictable URLs. The canonical syntax the spec adopts is:

```
{domain}/                          → the space itself
{domain}/agents/{agent}            → an agent that lives in it
{domain}/agents/{agent}/botlets/{botlet}   → a specific Botlet
{domain}/tools/{tool}              → a tool exposed via Layer 4
```

Addressability matters for two operational reasons. First, it is the basis of A2A communication — an agent that needs to invoke another agent does so through its canonical URL, with no need for ad hoc discovery. Second, it is the basis of MEO (Model Engine Optimization — the SEO→MEO shift Chapter 6 §1 develops): the frontier models that learn to reference AgencyDomains do so through predictable URLs that appear in their training corpus. Chaotic or unstable URLs make the AgencyDomain invisible to models that were not trained with its specific map.

### Canonical data model

<!-- FIG:g17-anatomia-agencydomain -->
![Anatomy of the AgencyDomain](figuras/g17-anatomia-agencydomain.png)

The internal structure of a conformant AgencyDomain follows a canonical model that the spec defines with precision (figure above).

Each component of the model has its specific role. **Identity** maintains the information that identifies the space to the world: its canonical URI, the credentials with which it authenticates to external systems, the root policies that no agent may contravene. **Agents** is the collection of agents that live in the space, each with its assigned Capabilities, its running Botlets, and its persistent state. **Capabilities Registry** is the tree of capabilities available to the agents of the space — shared know-how that agents can invoke according to their role. **Tools Registry** is the collection of tools that Layer 4 exposes outward — the interface through which the AgencyDomain touches external systems. **Trust Layer** exercises cross-cutting governance and audit — policies, append-only log, validation mechanisms. **Cognition Bindings** are the bindings to the cognitive resource — which model provider the AgencyDomain invokes, under what credentials, with what usage policies.

The notion of **Account** is a commercial concept superimposed on the technical model. An Account may own multiple AgencyDomains. The spec treats the Account as an opaque entity; each implementation defines its specific semantics — a client company, a federated organization, an individual user. The distinction between AgencyDomain (technical) and Account (commercial) matters because it allows the technical model to evolve without the commercial model needing a rewrite each time.

### The regime model

<!-- FIG:g18-tres-regimenes -->
![The three regimes · private · public · hybrid](figuras/g18-tres-regimenes.png)

One aspect that significantly distinguishes the AgencyDomains spec from more limited agentive solutions is its recognition of three possible **regimes** of an AgencyDomain, analogous to the regimes of cloud computing. The three regimes are technically equivalent in their internal structure; what changes between them is the **access boundary**, not the architecture.

The **private regime** corresponds to an AgencyDomain where the space and all its components live within a perimeter controlled by an organization. There is no public access. The agents of the space are invocable only from within the organization. The data of the space do not leave the perimeter. It is the conceptual analog of the Private Cloud — the organization has total control of its resources, pays for that control in terms of operation but gains in terms of sovereignty. The private regime is typical for cases where the organization operates sensitive data or complies with regulation that demands local residency.

The **public regime** corresponds to a publicly accessible AgencyDomain. Agents, Botlets, and tools are invocable from outside the perimeter. The AgencyDomain has a public URL and the agents that inhabit it are registered in a directory that any external system can query. It is the conceptual analog of the Public Cloud — maximum accessibility, maximum exposure, a different operating model. The public regime is where the network of agents cooperates openly with the rest of the internet.

The **hybrid regime** is a combination of the two preceding ones. A hybrid AgencyDomain has components in a private perimeter and components accessible publicly via proxy. Sensitive data remain private, but the interface that exposes capabilities to the exterior is available publicly. It is the conceptual analog of the Hybrid Cloud — the organization chooses what to expose and what to retain, balancing sovereignty and accessibility. The hybrid regime is typical for organizations that need to offer public agents to their customers but want to keep customer data within the corporate perimeter.

What is critical about this regime architecture — and it is a strong property of the spec — is that **the technical structure of the AgencyDomain is the same across all three regimes**. An agent operating in a private AgencyDomain is technically equivalent to one operating in a public one; what changes is the regime, not the capability. A Botlet executing in private can move that same code to a public regime without rewriting. This structural uniformity enables **natural migration** between regimes — an agent can graduate from private to public or vice versa without changing its internal logic. The organization governs the regime; the agent's logic never notices.

This natural-migration property is structurally important because it decouples the architectural decision (how the agent is built) from the commercial decision (in which regime it operates). An organization can begin building agents in the private regime while it validates their usefulness, and migrate them to the public or hybrid regime when maturity justifies it. The initial architectural investment is not lost in the transition.

To fix the idea with concrete instances as of May 2026 — both from the house portfolio; the general frame for implementations lives at the close of this spec and in Chapter 9 —: Agentia operates AgencyDomains in the private regime for firms that keep their agents within the corporate perimeter; Soveria operates AgencyDomains in the public regime where enabled agents are hosted with a public identity and a canonical URL; the same agent can graduate from the first to the second without a technical rewrite, keeping the agent's spec intact and moving only the regime.

### Cognition access models

The spec recognizes two coexisting modes by which the components of the AgencyDomain access the cognitive resource (Layer 2). The two modes coexist because they solve distinct problems, and a serious AgencyDomain typically operates both simultaneously for distinct components.

The first mode is **Tokens**. The flow is: AgencyDomain → cognitive resource, centralized and billed to the space. The AgencyDomain centralizes credentials, billing, and policies. It provides cognitive access to all its active components. This mode applies when agents must operate in the background without user intervention, when the organization wants central control over consumption and costs, or when multiple agents share a single cognition provider. The organization that operates Autonomous Agents in the background — agents that monitor continuously, respond to events, execute asynchronous tasks — needs Tokens, because there is no human available whose individual subscription would subsidize the invocations.

The second mode is **Subscription**. The flow is: user's Assistant → cognitive resource, via the user's own subscription. The assistant the user interacts with — Claude, ChatGPT, Copilot, Gemini — accesses the cognitive resource directly under the user's subscription. The AgencyDomain consumes no tokens from the resource. This mode applies when the user already has an active subscription to the cognition provider, when the AgencyDomain exposes tools and data to the user's assistant without centralizing cognition, or when the AgencyDomain's operating economics favor minimizing inference costs. The organization that adopts ultraPRO — an implementation from the house portfolio (Chapter 9): the secure integrator between the user's agent and corporate systems — typically operates in Subscription mode, because users bring their own subscriptions to the cognition providers.

Both modes coexist in mature systems. A single AgencyDomain may operate user Assistants (Subscription mode) and background Autonomous Agents (Tokens mode), simultaneously. The spec requires the AgencyDomain to **explicitly declare** which mode applies to which component. The explicit declaration prevents the most recurrent source of economic errors in agentive systems: accidental confusion between modes, where an Autonomous Agent that should operate on Tokens ends up billing against the user's subscription and exhausts it in hours, or where an Assistant that should operate on Subscription ends up billing against the AgencyDomain and consumes tokens it should not.

The role of Botlets in the cognitive economy deserves particular emphasis. In fixed-Subscription plans, Botlets are the mechanism for achieving autonomy without additional cost: the Botlets' `95/4/1` cycle is the economic basis of autonomy under subscription. The full development of this economy lives in §2.

### Agent life cycle

An AgencyDomain conformant to the spec manages the complete life cycle of each agent that inhabits it. The cycle has six canonical phases, and each transition between phases is recorded in the Trust Layer's append-only log.

The **provisioning** phase is where the AgencyDomain creates the agent. It assigns identity, associates the initial Capabilities the agent may invoke, registers the agent in the space. The agent is born, in system terms, when this phase completes successfully. If the phase fails — by credential error, by name conflict, by quota restrictions —, the agent never comes to exist.

The **bootstrap** phase is where the agent enters operation. It loads its persistent state if it exists — if the agent had been hibernated or restarted, it recovers its prior context. It establishes bindings with the cognition and the tools it will use. It verifies that its Capabilities are available. After bootstrap, the agent is ready to respond or to operate proactively, according to its mode.

The **reactive operation** phase corresponds to the agent operating in Assistant mode. Layer 2 active. The agent responds to human requests: each request arrives, the agent processes it by invoking cognition and possibly Capabilities, returns a response. Between requests, the agent is passive — it consumes no active compute, executes nothing. This phase is the most frequent in systems that operate primarily with Assistants.

The **proactive operation** phase corresponds to the agent operating in Autonomous Agent mode. Layer 3 active. The agent pursues goals in the background, monitors events, executes Botlets when appropriate, escalates to the human when thresholds demand it. Pattern Recognition generates and maintains Botlets as the agent identifies repetitive patterns. This phase is where the model *"intelligence goes to people and acts on their behalf"* materializes — the agent is active continuously, the human intervenes only when necessary.

The **hibernation** phase is where the agent is left paused but persistent. State saved. It consumes no active compute. This phase is useful when an agent need not operate for extended periods — a support agent that only operates during business hours, for example, hibernates overnight and reactivates with the start of the next day. Hibernation preserves the context without spending resources.

The **decommissioning** phase is where the AgencyDomain retires the agent. The agent's state is archived or deleted according to policy. The Capabilities it had assigned are released. The agent's identity remains recorded in the historical log, but the agent ceases to exist as an operative entity. The decommissioning phase is important because it formally closes the cycle — a "decommissioned" agent is not the same as a "forgotten" agent. The record of the decommissioning is what allows, weeks or months later, an auditable reconstruction that the agent existed, what it did, and why it ceased to exist.

### Communication between agents

The spec reserves the term **A2A** (`agent-to-agent`) for the *relation* between agents, and an agent is an AgencyDomain. The A2A relation is, therefore, **between AgencyDomains** — between distinct agents, each with its own identity and agency. Communication within a single AgencyDomain is not A2A in this relational sense: the components that sustain it are runtimes of the same agent, not distinct agents. The spec thus distinguishes two planes: the **intra-AgencyDomain** plane (an agent commanding its own runtimes and muscle memory) and the **A2A** plane (an agent invoking another agent). When the **`A2A` protocol** is used within an AgencyDomain as transport between runtimes, one says **via the `A2A` protocol** — the proper name of the protocol —, never "internal A2A", so as not to attribute agency to runtimes that do not have it.

#### How does the Cognition command its muscle memory? — Layer 2 ↔ Layer 3 interface

The **Cognition** (the `LLM` agent, Layer 2) commands its own muscle memory — the **Botler**, a Layer 3 runtime without agency — through an **internal** interface within the same AgencyDomain. It is the Layer 2 → Layer 3 relation: the Cognition specializes, manifests, consumes, and controls the Botlets that the Botler hosts. The natural transport of this interface is **`MCP`** (`LLM`↔tool): the Botler exposes one or more `MCP` servers and the Cognition is the client. This interface **is not `A2A`** — it does not cross the AgencyDomain boundary nor mediate between distinct agents; it is an agent operating its own execution substrate. `A2A` is reserved for AgencyDomain↔AgencyDomain.

<!-- FIG:g19-interfaz-capa2-capa3-mcp -->
![Layer 2 → Layer 3 interface via MCP — internal, not A2A](figuras/g19-interfaz-capa2-capa3-mcp.png)

#### What properties does intra-AgencyDomain communication require?

All communication between components that live **in the same AgencyDomain** — be it the Layer 2 → Layer 3 interface via `MCP`, be it the transport between Botlers via the `A2A` protocol — satisfies three properties the spec requires. The first is **uniform addressability** — any component of the space can be invoked by its canonical URI, with no need for ad hoc discovery. The second is **message typing** — messages have a declarative, verifiable schema; the sender declares the schema and the receiver verifies that the message complies with it before processing it. The third is **traceability** — every invocation is recorded in the append-only log with the identity of sender and receiver. If a component invoked another, the system knows who, when, and with what content.

#### How do distinct agents communicate? — A2A between AgencyDomains

**`A2A` communication between AgencyDomains** is between agents that live **in distinct AgencyDomains**. This modality requires additional protocols that the spec recognizes as necessary but does not fully normalize in its version 1.0. The open protocols for `A2A` are in evolution — the industry is converging toward certain directions, but full consensus has not arrived. What the spec does define is that `A2A` between AgencyDomains requires three mechanisms: **discovery** — how an AgencyDomain publishes the agents it offers to be invoked externally; **cross-authentication** — how two AgencyDomains verify each other's identity; **semantic resolution** — how two AgencyDomains that may have distinct glossaries negotiate the meaning of tools and capabilities when they interoperate.

The complete normative specification of `A2A` between AgencyDomains — discovery protocol, federated message format, identity resolution — is **open work**. Reference implementations may adopt emerging protocols, for example federated `MCP`, or the `A2A` protocol proposed by **Google**. When there is industry consensus on a specific protocol, a future version of this spec will incorporate it as normative. For now, serious implementations treat `A2A` between AgencyDomains as an emerging capability, not as consolidated spec.

### Federation between AgencyDomains

<!-- FIG:g20-federacion-vs-cluster -->
![Federation vs. Cluster · a critical distinction](figuras/g20-federacion-vs-cluster.png)

**Federation** is the formal mechanism by which multiple AgencyDomains collaborate as a network. It must be distinguished from the close but distinct concept of the **Cluster** — multiple instances of the same AgencyDomain operating as a coordinated set. Cluster is operational; Federation is architectural.

| Concept | Granularity | Example |
|---|---|---|
| **Cluster** | Multiple instances of the **same** AgencyDomain | Three instances of one firm's AgencyDomain sharing load |
| **Federation** | Multiple **distinct** AgencyDomains collaborating | Firm A's AgencyDomain invokes an agent from firm B's AgencyDomain |

Federation enables ecosystems of agents that cross organizational boundaries. An AgencyDomain can invoke agents from another AgencyDomain, exchange data, coordinate operations — all under explicit trust models that each participant establishes. This extends the agentive model beyond the boundaries of an individual organization and allows cooperation networks that resemble the open internet more than closed corporate systems.

The normative specification of federation is open work. Version 1.0 of the spec recognizes the necessary mechanisms without prescribing their specific implementation:

An **open discovery protocol** must exist, possibly over DNS and well-knowns. When an AgencyDomain wants to discover what agents another AgencyDomain offers, it must be able to query a standard endpoint and obtain the list. The spec does not prescribe the exact format of the endpoint — that decision depends on the industry consensus that has not yet arrived.

**Cryptographic identity standards** for AgencyDomains and agents are necessary. Each federated AgencyDomain must be able to authenticate cryptographically — not by a shared API key, but by a verifiable mechanism that requires no central authority. Candidate technologies include W3C DIDs (Decentralized Identifiers), X.509 certificates, blockchain-based mechanisms. The spec admits any that satisfy the fundamental property: verifiable identity without central authority.

**Explicit trust models** are a requirement. When two AgencyDomains interact, each must declare the level of trust it extends to the other: what operations it permits, what data it shares, what audit it exercises. Trust is not binary — an AgencyDomain may trust another for low-impact invocations but not for high-impact ones, or may trust it for reads but not for writes. The spec requires these models to be explicit and configurable, not implicit in code.

**Conflict resolution** when two AgencyDomains apply contradictory policies. If AgencyDomain A invokes an agent from AgencyDomain B, and the policies of A and B have conflicts — A permits the operation but B prohibits it, for example —, there must be a clear mechanism to resolve the conflict. The spec defines that priority always belongs to the receiving AgencyDomain — that is, B in this case. The sender may request; the receiver decides.

### Distributed Layer 3 — canonical pattern for multiple physical presence

<!-- FIG:g21-capa3-distribuida -->
![Distributed Layer 3 · central Botler + N edge Botlers](figuras/g21-capa3-distribuida.png)

Chapter 4 (in its Layer 3 — Autonomy section) anticipated that the four layers may be distributed technically across distinct infrastructures. This section formalizes the most frequent and operationally important particular case: the **geographic distribution of Layer 3** within a single AgencyDomain. The pattern resolves a scenario that any organization with multiple physical branches invariably encounters — multi-location food service, retail with a chain of stores, distributed logistics, healthcare with a network of centers, banking with branches, industrial plants with simultaneous production lines. Without formalization, each implementer reinvents the pattern with its own vocabulary and treats it as an exception to the model. With formalization, it stands as a **canonical pattern** that any serious implementation must contemplate.

The essential distinction is between **internal distribution** and **external federation**. Internal distribution occurs when a single AgencyDomain divides its Layer 3 across multiple coordinated physical nodes — a central Botler and N edge Botlers —, maintaining a single identity, a single governance, a single log, and a single data model. External federation occurs between distinct AgencyDomains, each with its own identity and governance. Cluster is an intermediate case (same AgencyDomain, same instances sharing load). Distributed Layer 3 is Cluster in terms of identity — all the Botlers belong to the same AgencyDomain — with the additional complication that the Botlers are not interchangeable: each edge Botler is responsible for a specific physical site.

#### Three pieces of the pattern

The canonical pattern distinguishes three pieces with distinct responsibilities:

**1. Central Botler.** Hosts the Botlets of orchestration, planning, reporting, global decisions. Lives typically in the cloud. It has a consolidated view of the state of all edge nodes. It executes operations that require crossing several sites — consolidating inventory, reconciling the day's cash, planning the next day's operation, sending consolidated regulatory reports. It maintains the consolidated DB and the unified audit log. It communicates with the cognition (Layer 2) for escalations and new decisions.

**2. Edge Botlers.** One per physical site. They host the local transactional Botlets — those that execute the site's daily operation: taking orders, charging, issuing receipts, managing local inventory, controlling physical devices (pinpads, printers, sensors). Each edge Botler maintains a local DB with the site's state and an **event queue toward the center** that synchronizes when there is network. They operate with full autonomy when the network is available and with local autonomy when the network goes down — the site keeps operating against its local DB; events accumulate in the queue; when the network returns, the queue drains and consolidation with the center resumes.

**3. Coordination between Botlers via the `A2A` protocol.** The central and edge Botlers communicate **via the `A2A` protocol** — the proper name of the coordination protocol. It is not `A2A` in the relational sense: these Botlers are runtimes of the same agent — the same AgencyDomain —, not distinct agents, so the coordination between them is **intra-AgencyDomain** communication, not `A2A` between AgencyDomains. The conversation traverses the corporate network but **does not traverse the federation** — it is entirely within a single AgencyDomain. The distinction is not rhetorical: the Trust Infrastructure regime is that of the single AgencyDomain, not that of federation between AgencyDomains; the log is unified; the identity model is internal; policies apply uniformly.


#### Offline mode as an emergent property

Under the parallel topology of Chapter 4 + the distributed Layer 3 pattern, the **offline mode** of a physical site emerges as a **structural property of the system**, not as a special capability that requires separate construction. When the network goes down at a site, two things happen simultaneously: the Cognition path becomes inactive (Layer 2 lives in the cloud and is not accessible), and the central Botler is also not accessible. But the edge Botler stays active: its Botlets run against the local DB, the edge-resident Connectors (ESC/POS printer, drawer, pinpad) remain available, the site's daily operation continues. The event queue toward the center accumulates pending transactions; when the network returns, it drains and consolidates.

The condition for offline mode to operate correctly is that the edge Botlets be **senior** in terms of the maturity proposal (section §2): Botlets that have already incorporated the environment's variants and operate with a ratio close to `99+ / <1 / ~0`. An edge Botlet in the junior phase — still discovering variants — cannot operate without the possibility of fallback to cognition. A senior edge Botlet can, because its only failure modes are exogenous (power, hardware, catastrophic network), not pending learning.

#### Properties required of the pattern

An AgencyDomain implementation with distributed Layer 3 must satisfy:

| Property | Level | Description |
|---|---|---|
| Single identity of the AgencyDomain | **MUST** | All Botlers (central + edge) belong to the same AgencyDomain with a single canonical URI. |
| Local DB in each edge Botler | **MUST** | Operational state of the physical site, accessible without network. |
| Event queue toward the center | **MUST** | Eventual-synchronization mechanism; pending transactions drain when there is network. |
| Conflict resolution in consolidation | **MUST** | When an event from edge reaches the center and conflicts with the consolidated state, an explicit policy decides. |
| Unified audit log | **MUST** | A single append-only log for the entire AgencyDomain, fed by all Botlers. |
| Single internal identity model | **MUST** | The Botlers do not authenticate to each other as external AgencyDomains; they share the AgencyDomain's identity model. |
| Uniform Trust regime | **MUST** | Policies apply the same at center and edge; there is no special regime for edge. |
| Offline operation capability at edge | **SHOULD** | When the edge Botlets are senior, the site operates with intermittent network or without network. |

### Portability of the AgencyDomain across conformant platforms

The regimes section formalized **natural migration** between regimes (private, public, hybrid) without rewriting. This section formalizes a complementary but distinct property: **portability across hosting platforms conformant to the spec**. A conformant AgencyDomain can be migrated to another conformant platform without rewriting its logic, its state, or its policies. This is a structural property of the spec — not the commercial commitment of a particular provider.

The motivation is operational before philosophical. Without an explicit portability commitment, the AgencyDomain repeats the lock-in of the application era — the client remains tied to its agentive provider exactly as it used to be tied to its SaaS provider. The structural promise of the spec — that the AgencyDomain is the **real property of the client**, not of the hosting — depends on portability being a property of the spec, not a concession negotiated case by case.

#### Three technical conditions

Portability requires three technical conditions that any conformant implementation must satisfy:

**1. Botlets against canonical primitives.** The AgencyDomain's Botlets must invoke Capabilities and the conformant AgencyDomain SDK, **not the current hosting's proprietary APIs**. If a Botlet invokes a provider-specific API — `cloudprovider.lambda.exec`, `vendor.workflow.run` —, that invocation is portability debt. When the time comes to migrate, that Botlet must be regenerated to invoke the equivalent canonical primitive. A conformant implementation provides SDKs and registries that abstract from the hosting; the Botlet sees the primitive, not the implementation.

**2. Exportable operational DB.** The persistent state of the AgencyDomain — agents, Botlets, capabilities, audit log, operational data — must be exportable in a neutral format, without dependencies on the hosting's storage engine. A documented schema (portable DDL or equivalent representation). A complete dump (all the information needed to reconstruct the space on another platform). No proprietary data types. No engine-specific extensions that have no equivalent in standard engines. The DB's portability is what allows migration not to be a rewrite.

**3. Portable Trust Layer.** The policies, the append-only log, the Capabilities configuration, and the identity bindings must be maintained in a neutral reproducible format — typically structured Markdown or YAML/JSON with an explicit schema. The spec does not prescribe the exact format, but it requires the format to be **readable by any conformant implementation**, not only by the current one. A policy that only one provider's policy engine knows how to interpret is not a policy of the AgencyDomain — it is provider configuration.

#### Natural migration vs portability

The two properties — natural migration between regimes and portability across platforms — are complementary but distinct:

| Axis | Natural migration between regimes | Portability across platforms |
|---|---|---|
| **What changes?** | The AgencyDomain's regime (private → public) | The hosting platform |
| **What remains?** | The hosting platform | The AgencyDomain's regime |
| **Who decides?** | The owning organization, by usage maturity | The owning organization, by economics or strategy |
| **Expected frequency** | Once or twice in the AgencyDomain's life | Zero or few times, but the possibility must exist |

Portability is not a promise that migration will be trivial — there will always be a cost of orchestration, validation, cutover window. It is a promise that migration will be **possible without rewriting the agent's logic**. That difference — between possible-with-work and impossible-without-rewrite — is what separates a conformant AgencyDomain from a proprietary agentive system in disguise.

### Conformance

An implementation that intends to call itself **conformant AgencyDomain** to this specification must satisfy the following list of requirements. We mark them with the IETF convention: **MUST** for mandatory, **SHOULD** for strongly recommended, **MAY** for optional.

| Requirement | Level |
|---|---|
| Own identity | **MUST** |
| Materialization of the four layers | **MUST** |
| State persistence | **MUST** |
| Isolation between spaces | **MUST** |
| URL addressability | **MUST** |
| Canonical data model | **MUST** |
| Support for the three regimes | **SHOULD** (at least one; ideally all three with migration) |
| Support for Tokens and Subscription modes | **MUST** both |
| Complete agent life cycle | **MUST** |
| Intra-AgencyDomain communication (Layer 2 → Layer 3 interface via `MCP`; coordination between runtimes via the `A2A` protocol) | **MUST** |
| `A2A` between AgencyDomains | **SHOULD** |
| Federation | **MAY** (when the normative spec is available) |
| Cross-cutting Trust Infrastructure | **MUST** |
| Agent First principle | **MUST** |
| Distributed Layer 3 (central + edge Botler) | **SHOULD** (when there is multiple physical presence) |
| Portability across conformant platforms | **MUST** (Botlets against canonical primitives, exportable DB, portable Trust Layer) |

An implementation that meets all the **MUST**s is an AgencyDomain conformant to version 1.0 of the spec. An implementation that meets the **MUST**s and the **SHOULD**s is what we would call a reference AgencyDomain — an exemplary implementation the industry can take as a base. Implementations that also meet the **MAY**s are frontier implementations, which typically lead the evolution of the field.

### Reference implementations

As we mentioned in Chapter 4, this specification is agnostic to implementation. The **public reference implementation** is **Vergis**: distributed under `AGPL`, with a public repository at AgencyDomains.org, designed so that any developer or student can download it, read it, run it, and learn how the spec translates into a living system. **Chapter 9** develops it in detail; here it suffices to leave the pointer and assert that it is conformant.

On the same canonical structure, product implementations in complementary regimes also operate: **Agentia** materializes AgencyDomains in the **private regime** within the infrastructure of the client firm, and **Soveria** materializes them in the **public regime** as a network of agents with a public identity. Other implementations are admissible and welcome. The specification intends to be an industry standard, not the intellectual property of a single actor.

### Evolution frontier

Three areas of the specification are under active evolution and a future version of the book will probably normalize them in greater detail.

**Federation** is the first. As we mentioned, the normative protocol is not yet agreed upon by the industry. Version 1.0 recognizes the necessary mechanisms without prescribing them in detail. When consensus arrives — probably within the next two to three years —, the spec will incorporate it.

**Agnostic cognition** is the second. The spec admits non-LLM cognition — symbolic, multimodal, hybrid. The contemporary implementation is predominantly LLM-centric. The extension to other cognitive substrates requires refinement of the interfaces between Layer 2 and the rest of the AgencyDomain's components.

**Cryptographic identity of agents** is the third. The model of verifiable on-chain or DID-based identity is under exploration. Adoption depends on the broader decentralized-identity ecosystem maturing sufficiently to support the agentive use case.

These three frontiers coincide with those of Chapter 4 — they are frontiers of the architecture itself, not only of its materialization in AgencyDomains.
