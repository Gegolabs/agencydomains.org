# Chapter 6 · Market

An architecture does not live in a vacuum: it competes in a market. This chapter situates any actor by means of the **AI value chain** —eleven links × four depths—, drills into select links with *deep-dives*, and extends the model to the **Carbon World**. §1 develops the general model; the sections that follow apply it.

## The AI value chain

> **Note on the datability of the products mentioned.** The listings of specific products in this chapter describe the state of the agentive AI market as of **May 2026**. The conceptual structure of the value chain's links is stable; the actors listed are illustrative of the moment. Later readings should take the names as a snapshot, not as permanent coverage.

The Artificial Intelligence industry presents itself, as of May 2026, as a dense ecosystem where dozens of products, platforms, and frameworks compete and coexist. Without a clear classification model, it becomes difficult to answer the fundamental questions any serious executive, architect, or strategist asks when facing the field: where does each actor play? which links does it dominate? where is there concentration and where is there room? in what territory does my proposal compete, and against whom?

The fragmentation of the field is no accident. It is the result of explosive growth where each new entrant builds its own category, chooses its own vocabulary, defines its own positioning. The consumer — be it an enterprise buyer, a market analyst, an investor — ends up overwhelmed by a language that each actor molds to its own convenience. *Agent platform, AI gateway, LLM framework, agentive infrastructure, autonomous agent, vertical assistant, model marketplace* — all terms that circulate without precise definition, all terms that different vendors use with different meanings.

This chapter proposes a map that disciplines that conversation. The map does not resolve every ambiguity in the field — the industry is too young for a single map to capture all its complexity —, but it delivers a shareable frame: a precise language that allows one to situate any actor in its position, compare actors with one another, and reason about a particular product's strategy relative to the broader field. The map that follows is the **AI value chain**, in its two-dimensional version. It is an original contribution of this book, derived from the author's prior work conceptualizing the field, and it is offered as an open tool for the industry, not as proprietary intellectual property.

### The two dimensions

The model organizes the AI technology value chain along **two dimensions**. The two dimensions operate orthogonally — an actor situates itself on each one independently —, and the combination of the two produces the positioning space where the actor lives. The two dimensions are **coverage** and **depth**.

**Coverage** is the horizontal dimension: which links of the value chain the actor touches. An actor may touch a single one, several, or many. Coverage is a metric of **reach** — how much of the field's territory the actor operates. An actor with broad coverage touches many links; an actor with focal coverage touches one or a few.

**Depth** is the vertical dimension: with what level of control the actor operates within each link. An actor may consume a link superficially — using third-party APIs — or build the link deeply — manufacturing the base technology. Depth is a metric of **control** — how much of the link the actor dominates. An actor with shallow depth depends on underlying providers; an actor with deep depth builds the substrate on which others operate.

Each actor can position itself in one or more links, at different depths in each one. A single actor may operate at Core depth in its native link and at Platform depth in adjacent links — a common pattern in the contemporary market.

The result is a **map that allows one** to classify any AI product by the links it spans, compare actors by coverage and depth in the chain, identify zones of concentration and zones of opportunity, and strategically position one's own products against the market.

### The eleven links

<!-- FIG:g33-once-eslabones -->
![The eleven links of the AI value chain](figuras/g33-once-eslabones.png)

The AI value chain decomposes into eleven sequential links, each with a clear and separable function. The separation is not arbitrary: each link corresponds to a distinct functional capability that an actor can operate independently, with its own economics and competitive dynamics.

We lay out each link with its functional description. The sequence is not linear in the sense that a data process passes through all the links in order, but it does reflect a conceptual progression from the field's raw material (data) to where the agent touches the real world (the environment).

**Link 1 · Data** (Data Layer). Acquisition, annotation, management of training datasets. It is the raw material that feeds the foundation models. The actors in this link produce curated datasets, annotation tools, large-scale data-processing pipelines. Without this link, the models do not exist.

**Link 2 · Model** (Foundation Model). Base AI models: LLMs and multimodal models that provide fundamental capabilities of language, reasoning, and generation. It is where the great labs — OpenAI, Anthropic, Google, Meta, DeepSeek — concentrate capacity. The actors here build the models that the rest of the field consumes.

**Link 3 · Access** (Access Layer). APIs and model access layers. Quota control, authentication, and monetization of consumption. It is where inference is sold as a service: OpenAI's, Anthropic's APIs, AWS Bedrock, Google's Vertex AI. It is also where products such as model gateways (Portkey) operate, offering abstraction over multiple models.

**Link 4 · Agents** (AI Agents). Conversational interfaces and assistants. From reactive agents — chat — to autonomous agents capable of executing complex tasks. It is where the most visible products appear: ChatGPT, Claude, GPT-4 with plugins, orchestrated agent systems.

**Link 5 · Specializations** (Domain Experts). Autonomous agents specialized by vertical domain: coding, legal, marketing, support, productivity, professional-work memory. It is where the vertical specialists appear: Cursor for coding, Harvey for legal, Jasper for marketing, Fin for customer support, umeeta for the memory of consulting engagements. The difference from link 4 is one of know-how depth in a specific domain.

**Link 6 · Runtime** (Agent Runtime). The operational environment where agents live and operate autonomously. Lifecycle, state persistence, identity, scheduling, and multi-agent orchestration. It is where Layer 3 of the Agentive Architecture materializes as a product. An emergent link — most traditional actors still do not cover it explicitly.

**Link 7 · Firewall** (Security Layer). Security, control, and governance. Protection against prompt injection, hallucinations, content filtering, and usage auditing. Products such as Lakera, Lasso Security operate here. It is a critical link for enterprise production — without a firewall, the agentive system cannot operate in regulated industries.

**Link 8 · Observability** (Observability). Monitoring, traceability, costs, and quality of AI systems in production. The operational feedback loop. Products such as Langfuse, LangSmith, Helicone, Arize operate here. It is a mature link — AI observability has several Core-depth products actively competing.

**Link 9 · Tools** (Tools). Specific capabilities that agents can invoke. Includes meta-tools: protocols (MCP), vector databases (Pinecone, Weaviate), RAG frameworks. It is where the agent extends its capability to touch specific systems.

**Link 10 · Integrations** (Integration Layer). The bridge between the AI world and the Environment. Orchestration, transformation, and mapping of integration logic between systems. Products such as Zapier, Make, n8n operate in this link in their traditional form; the agentive equivalent is still an emergent category.

**Link 11 · Environment** (Environment). What is external to the chain: enterprise systems (ERPs, CRMs, databases), the physical world (IoT, industrial processes), and biological systems. It is the least developed link, and we develop its implications in detail in the Carbon World section.

The links are not arbitrary. Each one corresponds to an **operational design decision** in any productive AI system. Skipping a link is not elegance: it is architectural debt that is paid in production.

### The four depths

The links define **where** an actor participates in the chain. But within a single link, actors operate at different levels of depth. An actor that consumes a model API and another that trains the foundation model **both participate in the Model link**, but their differentiation, dependency, and competitive moat are radically different.

The model defines four levels of depth, from lesser to greater control over the link's capability. The four depths apply to any link — an actor may be Wrapper in Data, Platform in Model, Core in Access. The uniformity enables cross-comparison between distinct links.

**Wrapper** (level 1). The actor consumes capabilities via third-party APIs or SDKs. It adds user experience or business logic without building the underlying capability. Characteristics: low differentiation relative to other wrappers that use the same underlying providers, high dependency on the provider, low switching cost. An app that calls the OpenAI API to answer questions is a Wrapper in the Model link.

**Platform** (level 2). The actor operates and manages its own capability over third-party Core components. It adds orchestration, SLAs, and operational control. Moderate differentiation: the customer pays for the operational capabilities the Platform adds, not for the underlying capability that remains third-party. Azure OpenAI is a Platform in Model: it operates OpenAI's models with SLAs and enterprise governance, but the models belong to the original provider.

**Core** (level 3). The actor builds the link's foundational capability with its own technology: differentiated models, engines, or algorithms. High competitive moat based on intellectual property. OpenAI is Core in Model: it builds its own models. Anthropic, Google with Gemini, Meta with Llama — all are Core in Model. The distinction between Core and the higher levels is where most of the value captured in the AI field resides.

**Infrastructure** (level 4). The actor provides the computational, storage, or connectivity substrate on which the higher levels operate. A very high moat based on scale and capital. NVIDIA is Infrastructure in Model: the GPUs NVIDIA manufactures are the substrate on which the models operate. AWS, GCP, Azure are Infrastructure in many links — they provide the compute and storage underlying almost the entire industry.

The progression Wrapper → Platform → Core → Infrastructure is one of **increasing control** over the link. Wrapper consumes; Platform operates; Core builds; Infrastructure sustains. Each level of depth typically implies greater investment, greater technical specialization, a greater competitive moat. It also implies greater risk: a Core that bet on a technology the market discarded is left with an asset hard to reposition; a Wrapper that bets wrong switches providers in hours.

### Coverage × Depth — the positioning space

<!-- FIG:g34-cobertura-profundidad -->
![Two-dimensional space · coverage × depth](figuras/g34-cobertura-profundidad.png)

The combination of coverage (links) and depth (levels) produces a **two-dimensional space** where any actor is positioned. The horizontal axis shows **how many links** an actor spans; the vertical axis shows **at what depth** it participates in each one.

A single actor may operate at different depths in different links. OpenAI is Core in Model but Platform in Access (its APIs) and Platform in Agents (ChatGPT). This per-link heterogeneity is the rule, not the exception. Few actors have uniform depth across all the links they touch — and when they do, they are typically very focused actors such as NVIDIA in computational Infrastructure.

The diversity of positions in the two-dimensional space allows one to identify positioning archetypes that recur in the market, with distinct strategic properties. The next section develops the four canonical archetypes.

### Emerging strategic archetypes

<!-- FIG:g35-cuatro-arquetipos -->
![The four strategic archetypes](figuras/g35-cuatro-arquetipos.png)

From this two-dimensional space, **four recurring archetypes** emerge. Each archetype describes a positioning pattern with characteristic strategic properties. The four archetypes are: Comprehensive platform, Vertical specialist, Domain infrastructure, Substrate provider.

#### Comprehensive platform

The **Comprehensive platform** archetype combines broad coverage (three or more links) with **Core** depth in its native link and **Platform** depth in adjacent links. It is the archetype of the great AI labs that dominate the field in 2026.

OpenAI exemplifies the archetype: Core in Model (builds GPT), Platform in Access (sells the API), Platform in Agents (operates ChatGPT and Operator), Platform in emerging Specializations (the verticalized GPTs). Anthropic follows a similar pattern but with a different emphasis: Core in Model (builds Claude), Core in Access via MCP (its open contribution to Tools), Platform in Agents. Google with Gemini does the analogous. Meta with Llama is a particular case: Core in Model distributing open source, with no proprietary Access or Agents platform — its moat is model distribution, not operation.

The competitive moat of the Comprehensive platform is the intellectual property of the Core combined with vertical integration into adjacent links. A Wrapper that calls OpenAI cannot easily replicate what OpenAI does in its entirety — to do so, it would have to train its own model (Model link at Core depth), build its own Access infrastructure, operate its own Agents platform. That complete chain requires capital and talent that few actors have.

#### Vertical specialist

The **Vertical specialist** archetype combines focal coverage (one or two links) with **Core** depth. It is the archetype of the actors that have concentrated on specific domains and build depth there.

Cursor exemplifies the archetype in coding: Core in Specializations for programming. Harvey AI does the same in legal. Jasper in marketing. Fin (from Intercom) in customer support. Devin aims for Core in Specializations of autonomous coding. umeeta operates the same archetype in professional consulting, with Core in the engagement-memory layer. Each one has narrow coverage — one or a few links — but Core depth in its specific vertical.

The competitive moat of the Vertical specialist is the depth of vertical know-how, which typically materializes as dense Capabilities — the codified professional knowledge we discussed in Chapter 5. A generic GPT can answer legal questions, but Harvey AI answers them at much higher quality because it has Legal Capabilities built with discipline. The difference is not marketing — it is structural. A competitor that wanted to replicate Harvey would have to build the Legal Capability tree with the same rigor, which takes years.

#### Domain infrastructure

The **Domain infrastructure** archetype is the most recent in the industry and the least populated. It combines zonal coverage (two or more contiguous links) with **Core** depth across a functional domain, with possible extensions to non-contiguous links at lesser depth.

An actor that is Core in Runtime, Firewall, Observability, Tools, and Integrations — links 6, 7, 8, 9, 10 — with a Platform extension in Access constitutes the paradigmatic case of the archetype. The combination of zonal coverage across five contiguous links with Core depth constitutes an **enterprise gateway**: the foundational layer for connecting and controlling AI in production.

The competitive moat of Domain infrastructure is the deep integration between links that other actors treat separately. Building Core in Runtime is a merit; building Core simultaneously in Runtime, Firewall, Observability, Tools, and Integrations, **coherently integrated**, is architectural property that few actors have. The structural reason is that these five links operate together in production — without one, the others lose value — and building only one leaves the actor dependent on complements that typically do not exist as an integrated product.

#### Substrate provider

The **Substrate provider** archetype combines minimal coverage (one link) with **Infrastructure** depth. It is the archetype of the actors that sustain the industry from the deepest layer.

NVIDIA exemplifies the archetype in Model: the GPUs NVIDIA manufactures are the computational substrate on which the models operate. AWS, GCP, and Azure are Substrate providers across multiple links — Data, Model, Compute in general. Cisco is one in networking for distributed AI.

The competitive moat of the Substrate provider is scale, capital intensity, and network effects in hardware or the data center. Building a company that competes with NVIDIA in GPUs requires investments of trillions of dollars and accumulated generations of R&D. Building a company that competes with AWS in compute at scale requires global physical infrastructure. These moats are the highest in the field, but they are also the ones that require the greatest initial capital and have the longest return cycles.

### Mapping the principal actors

By way of example, the following table classifies representative product families from the current market by the links they span and the depth in each one. The figures are **depth levels** (1-4); the parentheses indicate a framework or meta-tool (to build with, not to use).

| Actor | Da | Mo | Ac | Ag | Xp | Ru | Fi | Ob | He | In |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Data and annotation** | | | | | | | | | | |
| Scale AI / Labelbox | 3 | | | | | | | | | |
| Hugging Face | 3 | 2 | | | | | | | | |
| **Comprehensive platforms** | | | | | | | | | | |
| OpenAI (ChatGPT, GPT API) | | 3 | 2 | 2 | 2 | 3 | | | 3 | |
| Anthropic (Claude, MCP) | | 3 | 3 | 2 | | | | | 3 | |
| Google (Gemini) | | 3 | 2 | 2 | | | | | 3 | |
| Meta (Llama) | | 3 | | | | | | | | |
| Perplexity | | | 2 | 3 | 3 | | | | | |
| DeepSeek / Qwen / Ernie | | 3 | 3 | 3 | | | | | | |
| **Vertical specializations** | | | | | | | | | | |
| GitHub Copilot | | | | 2 | 3 | | | | | |
| Cursor / Replit | | | | | 3 | | | | | |
| Devin | | | | | 3 | 3 | | | 3 | |
| Harvey / Jasper / Fin | | | | | 3 | | | | | |
| umeeta (engagement memory) | | | | | 3 | | | | | |
| **Agentive substrates** | | | | | | | | | | |
| Agentia (private regime) | | | | 3 | | 3 | | | | |
| Soveria (public regime) | | | | 3 | | 3 | | | | |
| **Frameworks and tools** | | | | | | | | | | |
| LangChain / Graph | | | | (3) | | (3) | | | (3) | |
| AutoGPT / CrewAI | | | | (3) | | (3) | | | | |
| Pinecone / Weaviate | | | | | | | | | (3) | |
| **Operations and governance** | | | | | | | | | | |
| Guardrails / NeMo / Lakera | | | | | | | 3 | | | |
| Langfuse / LangSmith / W&B | | | | | | | | 3 | | |
| Zapier / Make / n8n | | | | | | | | | | 3 |
| ultraPRO (enterprise gateway) | | | 2 | | | 3 | 3 | 3 | 3 | 3 |
| **Computational infrastructure** | | | | | | | | | | |
| NVIDIA | | 4 | | | | | | | | |
| AWS / GCP / Azure | 4 | 4 | | | | | | | | |

Legend of links: **Da** Data · **Mo** Model · **Ac** Access · **Ag** Agents · **Xp** Specializations · **Ru** Runtime · **Fi** Firewall · **Ob** Observability · **He** Tools · **In** Integrations. Depth levels: **1** Wrapper · **2** Platform · **3** Core · **4** Infrastructure. The parentheses — e.g. (3) — indicate a framework or meta-tool (to build with, not to use).

> **Note.** The table covers links 1 through 10. Link 11 (Environment) is omitted as being external to the chain — it is the territory on which the preceding links act, not a link that an AI actor occupies at some depth. Its implications are developed in the Carbon World section.

The table, read as a whole, lets one see patterns that the individual inspection of each product does not reveal. The comprehensive platforms tend to concentrate in links 2-4. The vertical specialists accumulate in link 5. The operations and governance products distribute across links 7-10. Computational infrastructure occupies principally link 2 at depth 4.

### Strategic readings of the map

The map is not merely descriptive — it is a tool for strategic analysis. Three readings of the 2026 map make it possible to understand the state of the field and where the opportunities lie.

#### Concentration by archetype

The **vertical specialists** dominate link 5 (Specializations). Cursor, Harvey, Jasper, Fin, Devin: each built dense vertical Capabilities and captures market in its domain. The concentration is healthy — multiple actors with little overlap, each owner of its vertical. It is where innovation is most vibrant in 2026.

The **comprehensive platforms** concentrate links 2-4 (Model, Access, Agents). Five dominant global actors — OpenAI, Anthropic, Google, Meta, DeepSeek/Qwen/Ernie — and derived positions. The concentration is high and grows over time, because building Core in Model requires capital and talent that few actors can sustain. It is the link with the highest barrier to entry.

The **infrastructure** is concentrated in NVIDIA for compute and the hyperscalers for data and compute at scale. An extreme capital moat. The concentration here is structural and probably persistent — it is reasonable to expect that no significant entrant will appear in these links at Infrastructure depth within the foreseeable horizon.

#### The less-contested spaces

There are zones of the map where Core depth is open and where an actor with discipline can build a competitive position without facing massive incumbents.

**Link 1 (Data) at Core depth**: few Core actors (Scale AI, Labelbox); the rest are commodity. There is room for actors that build their own capability in specialized data.

**Links 6-10 simultaneously** — Runtime, Firewall, Observability, Tools, Integrations — at Core depth with zonal coverage: the territory of Domain infrastructure. Actors that combine these five links at Core depth are rare. It is the space where the category of the **complete enterprise gateway** is opening.

**Link 11 (Environment)** with connection to IoT and the physical world: practically empty in terms of actors specifically designed for the Agentive World. It is the frontier of the next generation, and the Carbon World section develops the implications.

#### The trajectory of the giants

<!-- FIG:g36-trayectoria-gigantes -->
![The trajectory of the giants · and the open window](figuras/g36-trayectoria-gigantes.png)

The giants — OpenAI, Anthropic, Google, Microsoft — advance **link by link**: from Model to Access, from Access to Agents, from Agents to Specializations. The progression is historically observable. OpenAI was born as a Model lab, expanded to Access (API), expanded to Agents (ChatGPT), is expanding to Specializations (GPTs).

But reaching the Integrations link — where the agent touches the real systems of the enterprise — demands an integrative effort, company by company, that does not scale with these actors' logic. OpenAI can offer ChatGPT Enterprise with connectors to Slack and Salesforce, but integrating deeply with each customer's ERP, with its particular CRM, with its legacy data warehouse — that is not platform work, it is integration work. **This creates a temporal window** for actors specialized in links 6-10 (domain infrastructure) to build a position before the giants arrive. The window is not indefinite — the giants eventually reach integrations, possibly via acquisition — but it exists now and offers strategic opportunity to whoever understands it.

#### The enterprise gateway as a category

<!-- FIG:g37-gateway -->
![The enterprise AI gateway · connect and control](figuras/g37-gateway.png)

The combination **Core in Runtime + Firewall + Observability + Tools + Integrations**, with a **Platform extension in Access**, defines an architectural category with a unique function: to **connect and control simultaneously** the operation of enterprise agents. It is the formal materialization of Layer 4 of the Agentive Architecture over the market links.

This category is called the **enterprise AI gateway** (figure above).

To **connect** without **controlling** is Zapier — integration capability without governance. To **control** without **connecting** is Lakera — security capability without integration. The combination of both in a single architectural point is a recent and still sparsely populated category. The actors that occupy it first capture the space before the giants arrive.

### Competitive analysis of the enterprise gateway

When evaluating actors that aim to occupy the enterprise gateway, a useful rubric compares nine capabilities across the principal actors in the field.

| Capability | Portkey | Lasso | Lakera | Langfuse | Credo AI | Noma | Complete enterprise gateway |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| LLM routing | ✓ | | | | | | ✓ |
| Semantic cache | ✓ | | | | | | ✓ |
| Prompt security | | ✓ | ✓ | | | ✓ | ✓ |
| Tokenization | | ✓ | | | | ✓ | ✓ |
| DLP | | ✓ | ✓ | | | ✓ | ✓ |
| Policies / CRUDLEX | △ | △ | | | ✓ | △ | ✓ |
| Human approval | | | | | △ | | ✓ |
| Response validation | | | △ | △ | △ | △ | ✓ |
| Observability | △ | | | ✓ | △ | △ | ✓ |
| **Enterprise connectivity (Tools + Integrations)** | | | | | | | ✓ |

The rubric documents, column by column, the thesis already stated in the previous section: each actor covers some capabilities — Portkey covers routing and cache, Lasso covers prompt security and DLP, Langfuse covers observability —, but none integrates deep enterprise connectivity and control under a single architecture. The last row — **complete enterprise gateway** — is the only one with integral coverage of the rubric.

This is the clearest strategic opportunity the map reveals. The complete enterprise gateway is a category that is only just emerging, with room for actors that build it with architectural discipline. ultraPRO is one of the actors positioning itself in this category, integrating the five links of control and connectivity under the tripartite Cloud + Client + Local pattern that Chapter 8 develops in detail.

### Implications for builders

The value chain map has three operational readings for whoever builds in the AI field.

The first: **do not compete in the wrong link**. If a small company tries to be Core in the Model link, it competes against OpenAI, Anthropic, Google, Meta — labs with trillion-dollar backing. The defeat is structural. If the same company seeks Domain infrastructure in links 6-10, it competes in a sparsely contested category with a buildable moat. The asymmetry is real and favorable. Choosing the link well is probably the most important strategic decision for a company entering the field.

The second: **Core depth requires discipline**. Reaching Core depth in any link demands building deep technical capability — not third-party integration. The difference between Wrapper, Platform, and Core is not a matter of opinion: it is measured by the product's structural dependencies. A Wrapper stops operating if the provider turns it off; a Core operates independently. If your product stops working when OpenAI changes its pricing, you are a Wrapper. If your product keeps working, you are a Core.

The third: **broad coverage demands integration**. A company that aims to cover multiple links at Core depth (domain infrastructure) must solve the problem of internal integration between those links. Operating Runtime + Firewall + Observability + Tools + Integrations as five separate products produces a company with five products. Operating them as a coherent architecture produces a gateway. The difference is what the customer perceives as value.

### Agentive discoverability — the displacement of the discovery layer

<!-- FIG:g38-discoverability -->
![From SEO to MEO · web discovery vs. agentive discovery](figuras/g38-discoverability.png)

The value chain model describes where value is *produced*. But there is a structural property of the Agentive World that the chain model on its own does not capture: **where** the produced value **is discovered**. The discovery layer of enterprise software changed, and the chain does not operate well if the reader does not understand that change.

In the world of applications, discovery happened in search engines: Google for web services, the app stores for mobile, the vertical marketplaces for SaaS. The human who needed a capability found it by typing a search, and the actors invested in positioning — SEO, ASO, content, ads — to be found. The layer was the search engine, and the search engines were a handful.

In the Agentive World, the human who needs a capability does not open Google — they ask the assistant they already have open. *"Where can I publish this agent?"*, *"What tool serves me for this task?"*, *"Is there an AgencyDomain that covers this domain?"*. The answer does not come from the web's index — it comes from the trained model. The discovery layer shifted from the *search index* to the *model of cognition*.

This has three structural consequences for any actor building in the agentive value chain.

The first consequence is that **trained presence matters more than ranking**. An actor that does not appear in the training corpus of the frontier models is invisible, regardless of its SEO or its traditional marketing. The conceptual equivalent of SEO in this new world is what the industry is beginning to call **MEO — Model Engine Optimization**: the set of practices that ensure the frontier models (Claude, GPT, Gemini, Llama, whichever come) have the actor in their trained and operative knowledge. It is built with structured public presence — open source repositories with READMEs rich in use cases, abundant documentation with citable examples, papers, native integration with the MCP spec, mentions in relevant technical blogs and forums.

The second consequence is that **the dynamic is persistent and asymmetric**. Once a frontier model "learns" an actor in the chain, the reference scales with the model's usage. It does not depend on paying per click nor on maintaining continuous investment in positioning. It is a cumulative advantage that survives marketing cycles, and it has a winner-take-all tendency: if an actor is the first that the frontier models systematically reference for a category, the following ones fight against that default. Whoever builds today with an MEO vision captures a temporal advantage that becomes progressively hard to reverse.

The third consequence is that **integration with MCP is a diffusion vector**. When an actor publishes capabilities as Model Context Protocol tools that a model can invoke natively, that model does not merely *mention* the actor — it *executes* it. Repeated invocation builds the model's structural familiarity with the actor, distinct from the citational familiarity that public documentation produces. The MCP spec is then, besides a protocol of technical integration, a vector of presence in the frontier models.

For the architect and for the investor, the operational conclusion is that **the AI value chain operates over an agentive discovery layer**, and that layer has rules distinct from those of web discovery. Whoever builds agentive products must think of trained presence as an investment category of its own — not as a sub-problem of traditional marketing.

---

The value chain model is the map. The next two sections of Chapter 6 drill into specific links where whoever builds or invests will find distinct but equally operational readings: one on an already-mature link that separates the serious actors from those who improvise, and another on the least developed and most promising link of the field, where the next decade of economic value is going to be defined.
