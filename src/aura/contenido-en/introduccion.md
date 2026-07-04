# Introduction

*AURA — Agentive Unified Reference Architecture*

## The Concept: Agentive AI
The technology industry is debating between two radically different futures for artificial intelligence in the enterprise.

In the **agentic** world, AI agents are integrated as complementary tools. Employees keep opening Excel, Salesforce, Power BI — now with copilots that help them work faster. Traditional interfaces persist; agents enhance them. It is incremental evolution.

In the **agentive** world, agents completely replace traditional interfaces. Employees stop opening applications — they interact directly with agents that execute tasks on their behalf. Applications may continue to exist as invisible backend infrastructure, but the interface has collapsed. It is fundamental transformation.

The frontier between the two worlds is what we call **the Nadella Line**: do your employees still open applications to do their work? If the answer is yes, you are in the agentic world. If the answer is no, you have crossed into the agentive world.

To grasp concretely what this means: a CFO who today opens Power BI builds margin dashboards and produces conclusions in two or three hours. In the agentive future, that same CFO simply asks "Why did margins drop in Q3?" and within minutes an agent analyzes data, generates visualizations, and identifies root causes. The critical point: the CFO never opened an application.

The industry's most disruptive voices are betting on the agentive world. Satya Nadella (CEO of Microsoft) declared: *"The notion that business applications exist, that's probably where they'll all collapse, right, in the agent era."* If the agentive future materializes, the implications run deep: graphical interfaces collapse, technical skills are redefined, technology investment migrates from SaaS licenses toward agent governance, and competitive advantage shifts from having better applications to having better agents and extraordinarily skilled employees directing them.

**Why "agentive" and not "agentic"?** Because they are not the same thing. The industry has adopted "agentic AI" to describe agents that assist — copilots, assistants, smarter tools. But this book points to something qualitatively different: a world where agents do not complement the way we work but transform it. Using "agentic" would limit the scope to incremental evolution. Using "agentive" points to fundamental transformation — which is the central thesis of this book.

**The crossing indicator: the agentive percentage.** The Nadella Line admits an operational indicator, and it is worth installing from the start because it turns the paradigm into a measurement any board understands: *what percentage of the times an employee needs to get something done can they delegate it entirely to an agent, without opening an application?* Between 0 and 20 percent, the organization lives in the agentic world — agents are complementary tools. Between 20 and 50, it is approaching the line. Between 50 and 80, it is crossing it. Above 80, it inhabits the agentive world. The indicator complements this book's two models without replacing them: IRIS and MOTOR measure the internal **capabilities** (knowing and doing); the agentive percentage measures the organization's **position** with respect to the transition. And it does not move uniformly: structured-knowledge functions — finance, operations, customer service — push it up fast; regulated industries — health, banking, government — push it up slowly, by legal mandate before technical limit. Measuring it per function, not as a single average, is what makes it actionable.

**The transformation this book traverses is set on the agentive horizon.** To navigate that transformation, ultraBASE has developed **AURA** — an agentive enterprise architecture that organizes the transformation along two complementary maturity axes:

**IRIS** (Organizational Intelligence Maturity Model) measures the **KNOWING** axis — an organization's trajectory from fragmented data to a self-managing intelligence ecosystem. From the online enterprise — which accesses up-to-date information but depends on humans to act — to the real-time enterprise — where intelligent systems detect, interpret, decide, and act autonomously.

**MOTOR** (Organizational Automation Maturity Model) measures the **DOING** axis — the trajectory from processes executed by humans to autonomous execution orchestrated through AI agents.

Both models are **diagnostic**: they assess what level an organization is at and what that level means. They do not prescribe what to implement — that is the province of specialized consulting. They are orthogonal: an organization can be high on one and low on the other. Full organizational maturity requires advancing along both axes. AURA integrates both axes into a reference architecture that makes it possible to diagnose the complete state of the transformation.

> The world on the other side of this transition is portrayed in *The Real-Time Enterprise*, and its formal architecture specified in *AgencyDomains* — volumes I and III of this trilogy.

## The Industry's Stagnation

### The Value Pyramid
Every organization accumulates data. Sales transactions, inventory movements, customer interactions, operational metrics — enterprise systems generate records continuously. But raw data, on its own, has no executive value.

Value emerges through a progression we call **the Data Value Pyramid**:

![The Data Value Pyramid — and the two leaps where the industry stalled](figuras/a02-piramide-valor.png)

Organizations have invested decades and fortunes in the two lower layers: transactional systems, data warehouses, ETL pipelines, visualization tools. But the leap from information to knowledge remains painfully slow — and the leap from knowledge to action is practically nonexistent.

Why? Not because the technology is slow, but because **there are humans in the middle**. When an executive needs to understand something about the business — why sales dropped, where the operational inefficiency lies, which customers are at risk — a process begins that rarely takes less than a week: calendar coordination, requirements gathering, technical development, iterative validation. The real bottleneck is the transfer of knowledge between people, not the capacity of the systems.

This diagnosis is the starting point of the transformation we measure.

### From information management to organizational intelligence
Well-established information management maturity models exist in the industry — Gartner, CMMI, DAMA-DMBOK. They measure critical aspects: data quality, governance, architecture, integration. But they concentrate on the first two layers of the Value Pyramid: DATA and INFORMATION.

This book spans all four layers, from fragmented data to orchestrated autonomous action. That is no longer information management — it is an organization's capacity to transform data into actionable intelligence. That is why we speak of **organizational intelligence**: it is not about how well you manage your data, but about how capable your organization is of generating knowledge and acting on it continuously and autonomously. Information management is the necessary foundation — but not the destination.

## The Leap

### The new economics of information: from weeks to seconds
The most immediate and tangible change enabled by agentive AI is the **elimination of the marginal cost of an analytical question**. We call that collapse — from weeks to seconds — **the Quantum Leap**, and it will be a reference throughout the book. In the traditional model, every new business question entails a project: coordination, requirements gathering, development, validation. The cost — in time, in person-hours, in opportunity cost — leads organizations to *ration* their questions. Only what someone had the foresight to pre-build into a dashboard or report ever gets analyzed.

When that cost collapses from weeks to seconds, the very nature of the relationship between an organization and its information changes:

- **Analytical capacity becomes elastic.** It adapts in real time to the current need, not to whatever someone managed to pre-define months ago. There is no fixed menu — there is unlimited responsiveness.
- **Iteration replaces specification.** Instead of defining requirements up front and waiting for the result, the executive explores, refines, drills deeper in a continuous conversation with the information. Knowledge emerges from dialogue, not from a project.
- **The questions that were never asked now get asked.** When asking is free, the organization discovers insights it didn't even know it needed. Analytical curiosity stops being constrained by the BI budget.

This transformation in the economics of information is an **enabling condition** for everything else in this book: the continuous-intelligence cycle cannot exist if every iteration takes weeks. Autonomy governance makes no sense if agents do not operate in real time. The transformation of roles does not happen if access to knowledge still depends on human intermediaries.

### The inversion of the flow
For 30 years, the information management paradigm was **"people go to the data"**: you build a warehouse, mount dashboards, train users, and hope someone looks at the right report at the right moment and makes the right decision. The entire model rests on *human attention* as the bottleneck.

As [Tellius](https://www.tellius.com/resources/blog/agentic-analytics-explained-from-questions-to-autonomous-action) describes it: *"Dashboards still tell you what happened, but rarely why — and never what to do next."* [Superwise](https://superwise.ai/blog/ai-agents-beyond-dashboards/) puts it bluntly: the industry is moving "beyond dashboards" because *"BI was built for a slower business environment — that assumption no longer holds true."*

Agentive AI inverts that flow: **"intelligence goes to the people — and acts on their behalf."** A system of agents monitors, interprets, decides, and executes within the limits the organization has defined, and escalates to a human only when warranted. This inversion marks the frontier between two fundamentally different kinds of organization — the **online enterprise** and the **real-time enterprise** — the same distinction fixed further below on the continuous-intelligence cycle (Perceive → Interpret → Decide → Act → Learn).

[Tableau](https://www.tableau.com/agentic-analytics) articulates this as the move from traditional BI to "agentic analytics," where AI doesn't just visualize data but activates it. [Cube](https://cube.dev/blog/why-agentic-analytics-is-the-new-modern-analytics) declares it openly: *"The modern data stack is beginning to show its age."* [BCG](https://www.bcg.com/publications/2025/agentic-ai-industrial-goods-driving-change) takes it to the operational plane, describing how agentive AI orchestrates actions across the entire value chain, "closing the loop between insight and execution."

> Agentive AI is not an incremental improvement to the analytics stack — it is a change of operating model. Measuring maturity in this context requires assessing not only the technology, but the organization's capacity to operate in a fundamentally different paradigm.

### Paradigm shifts
| Before | After |
|---|---|
| People go to the data | Intelligence goes to the people and acts on their behalf |
| Dashboards as the end product | Agents as the operating system of decisions |
| Human attention as the bottleneck | Human governance as the control system |
| Analytics as a support function | Continuous intelligence as a business capability |

### From the classic cycle to the continuous-intelligence cycle
#### Classic cycle · Linear · Human-dependent

```
Descriptive → Diagnostic → Predictive → Prescriptive → [!] Human decides
(What happened?) (Why?)  (What will happen?) (What to do?)  (bottleneck)
```

#### New cycle · Continuous · Agent-executed · Human-governed

```
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  ▼                                                     │
Perceive → Interpret → Decide → Act → Learn ────────────┘
 Agents      Semantic     Within     Autonomous   Continuous
 monitor     context +    defined    execution    feedback
 data        reasoning    rules and  with         and
 continuously             thresholds traceability adjustment
```

**The critical change:** the step from "Prescriptive" to action is no longer a recommendation a human evaluates. It is a decision an agent executes, whose outcome it monitors and adjusts. The organization stops "doing analytics" and starts *being* an intelligent system.

**What the industry is saying:**

[Tableau](https://www.tableau.com/blog/ai-agentic-analytics-upend-cycle-of-visual-analysis) describes how agentive AI "upends the cycle of visual analysis" — transforming a linear, human-dependent process into a cycle where agents participate actively at every stage. [Tellius](https://www.tellius.com/resources/blog/agentic-analytics-explained-from-questions-to-autonomous-action) formalizes it as the move "from questions to autonomous action."

[Ampcome](https://www.ampcome.com/post/ai-agents-in-analytics) documents 11 enterprise use cases where analytical agents are already transforming decisions in 2026. [CDO Trends](https://www.cdotrends.com/story/4839/agentic-analytics-how-semantic-layers-are-powering-next-era-ai-driven-decision-making) describes how semantic layers are powering this new era of AI-driven decision-making.

Gartner had already introduced the concept of "continuous intelligence" as one of its strategic trends, defining it as real-time analytics integrated directly into business operations. Agentive AI takes that vision to its logical conclusion: not just continuous analytics, but **continuous action**.

### Context data
- **40%** of enterprise apps will include AI agents by the end of 2026, vs. <5% in 2025 ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025))
- **>40%** of agentive projects will be canceled before the end of 2027 — due to costs, unclear business value, or inadequate risk controls ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027))
- **80%** of organizations report risky behaviors from their agents; only 21% have mature governance ([MindStudio](https://www.mindstudio.ai/blog/ai-agent-governance))
- **75%** of current roles will require redesign by 2030 ([McKinsey](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-organization-blog/rethink-management-and-talent-for-agentic-ai))
- **58%** of heavy adopters expect fundamental changes in governance within 3 years ([BCG](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain))
- **48%** cite data discoverability among the main barriers to their AI automation strategy ([Deloitte](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html))
- Only **14%** have production-ready agentive solutions; 11% in real-world use ([Deloitte](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html))
- Agentive AI market: **$7.3B** in 2025 → projected **$139.2B** by 2034 (CAGR ≈39%; aggregated market projections)

## Three Axes of Deep Change
### Axis 01 · From consuming information to governing agents

**Current paradigm:**

- Analysts build reports
- Users consume dashboards
- Key competency: data literacy
- Value lies in understanding the information

**Emerging paradigm:**

- People design rules for agents
- Agents monitor, interpret, and act
- Key competency: designing and supervising autonomous systems
- Value lies in governing intelligent action

> *"The CFO doesn't review a cashflow dashboard — they define the thresholds and protocols that a financial agent executes autonomously."*

**What the consulting firms are saying:**

[McKinsey](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-organization-blog/rethink-management-and-talent-for-agentic-ai) describes the "Agentic Organization," where employees shift from executing tasks to orchestrating outcomes, supervising agents, setting objectives, and managing trade-offs. Humans move "above the loop." McKinsey estimates that 75% of current roles will require redesign, upskilling, or redeployment by 2030.

[BCG](https://www.bcg.com/publications/2025/as-ai-changes-work-ceos-must-change-how-work-happens) notes that 45% of AI leaders expect to need fewer layers of middle management, as work centers on supervision, orchestration, and continuous improvement of agentive processes — not on manual execution.

[Deloitte](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html) frames the new human role around judgment and orchestration governance: *"human ingenuity and judgment will continue to play a key role in selecting and guiding agent outputs."*

A [CIO.com](https://www.cio.com/article/4060162/the-new-org-chart-unlocking-value-with-ai-native-roles-in-the-agentic-era.html) article details the emerging new roles: AI Agent Orchestrator, Human-Agent Interaction Designer, AI Ethics & Governance Specialist, and AgentOps Specialist. It is an entirely new org chart.

### Axis 02 · From architecture for humans to architecture for agents

**Current paradigm:**

- Data warehouses optimized for SQL
- Data quality = cleanliness
- Data models for visualization
- Batch and on-demand integration

**Emerging paradigm:**

- Semantic layers where agents reason
- Data quality = actionability
- Knowledge graphs for autonomous inference
- Real-time, contextual data flows

> *"If an agent cannot reliably interpret and act on a piece of data, that data is useless — no matter how 'clean' it is."*

**What the industry is saying:**

[AtScale](https://www.atscale.com/blog/semantic-layers-agentic-ai/) demonstrated that agents without a semantic layer fail on 80%+ of queries, while with a semantic layer they reach ~100% accuracy. Its conclusion: *"For AI agents, the semantic layer isn't just a nice-to-have — it's the foundation that makes AI actually useful."*

[ThoughtSpot](https://www.thoughtspot.com/blog/introducing-the-agentic-semantic-layer) coined the concept of the "Agentic Semantic Layer" — dynamic, context-aware, and designed to work hand in hand with agents. [Salesforce](https://architect.salesforce.com/fundamentals/agentic-enterprise-it-architecture) proposes an Enterprise Knowledge Graph (EKG) as the central layer of its agentive enterprise architecture. [Databricks](https://www.databricks.com/blog/delivering-agentic-bi-how-unify-infrastructure-data-and-semantics) speaks of unifying infrastructure, data, and semantics to enable "Agentic BI."

[Informatica](https://www.informatica.com/resources/articles/enterprise-ai-agent-engineering.html) warns that giving an agent access to data is not enough: *"Because agents act without human approval loops, the data they use must be fully trusted, verified, and monitored."* It proposes data-quality SLAs: less than 5 minutes of freshness for transactional agents, less than 1 hour for analytical agents — a direction Data Canon (Part I) will push further: a single quality level, the strictest, for the entire canon.

[eWeek](https://www.eweek.com/artificial-intelligence/how-will-agentic-ai-change-enterprise-data-management/) introduces the concept of "agent-ready data" and projects that by 2026, enterprise data management will be radically different — with autonomous agents cleaning, validating, and enriching data within governed limits.

[Deloitte](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html) found that 48% of organizations cite data discoverability and 47% cite reusability as main barriers to their AI automation strategy. It proposes a paradigm shift: from traditional ETL pipelines to enterprise search and indexing, contextualizing data through knowledge graphs.

### Axis 03 · From access governance to autonomy governance

**Current paradigm:**

- Who can see which data
- Static roles and permissions
- Compliance as a checklist
- Access auditing

**Emerging paradigm:**

- What an agent can do, under what conditions
- Dynamic levels of human supervision
- Governance as an enabler of scale
- Auditing of autonomous decisions

> *"Organizations that fail to solve autonomy governance will not be able to scale agents beyond isolated pilots."*

**What regulators, consulting firms, and industry are saying:**

[Singapore IMDA](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) published in January 2026 the first state-issued governance framework for agentive AI (MGF), establishing that although agents act autonomously, *"human responsibility continues to apply"* — organizations must make human accountability meaningful and keep the human-in-the-loop effective over time.

The [World Economic Forum](https://www.weforum.org/stories/2025/12/ai-agents-onboarding-governance/) proposes progressive governance: logging and traceability for all agents, identity tagging per action, and real-time monitoring. Its key distinction: *"autonomy entails decision-making flexibility; automation emphasizes execution reliability"* — these are design choices, not inherent properties of the system.

[BCG](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain) reports that 58% of heavy AI adopters expect a fundamental change in their governance structure within the next 3 years, and a third believe AI will hold more decision authority over the same period.

[NACD](https://www.nacdonline.org/all-governance/governance-resources/directorship-magazine/online-exclusives/2025/q3-2025/autonomous-artificial-intelligence-oversight/) (National Association of Corporate Directors) warns that agentive AI impacts board oversight, regulatory compliance, and risk exposure — it is no longer just an IT matter.

[KPMG](https://kpmg.com/us/en/articles/2025/ai-governance-for-the-agentic-ai-era.html) sums it up: *"The winners won't be the ones with the most pilots but the ones investing now in scalable data architectures, agent governance models, and workforce readiness."*

[Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) predicts that more than 40% of agentive AI projects will be canceled before the end of 2027 — due to costs, unclear business value, or inadequate risk controls. Governance is not optional; it is what separates pilots from production.

The scale of the problem is significant: according to [MindStudio](https://www.mindstudio.ai/blog/ai-agent-governance), 80% of organizations report risky behaviors from their agents (unauthorized data access, unexpected interactions), and only 21% have mature governance models. [ISACA](https://www.isaca.org/resources/news-and-trends/industry-news/2025/the-growing-challenge-of-auditing-agentic-ai) highlights that agentive AI poses a growing challenge for audit functions because its decision processes lack clear traceability.

## AURA: The Map of the Path

### Online enterprise vs. real-time enterprise
The preceding sections laid out the distinction; it is time to fix it as the axis of the trajectory: the **online enterprise** *accesses* — up-to-date data, current dashboards — but depends on a human to look, interpret, and decide; the **real-time enterprise** *reacts*: it runs the full continuous-intelligence cycle, waiting for no one.

IRIS maps this trajectory: stages 1–4 build the **foundations** — the infrastructure of the online enterprise; stages 5–10 build the **real-time enterprise**. **The Quantum Leap** — the collapse of the cost of the analytical question — is the frontier between the two trajectories.

And the Nadella Line maps naturally onto this trajectory: the foundations (stages 1–4) are inherently agentic — they are built with tools and copilots. From Stage 5 onward, the organization becomes progressively agentive — agents detect, interpret, and act autonomously.

### The convergence

Four concepts converge in AURA:

**Organizational Intelligence** is the capability being measured — the *what*. (IRIS measures this axis: KNOWING.)
**Organizational Automation** is the capability to execute — the *who*. (MOTOR measures this axis: DOING.)
**Real-Time Enterprise** is the organizational outcome of both capabilities at maturity — the *what for*.
**Agentive AI** is the enabling mechanism that makes the transformation possible — the *how*.

AURA is the architecture that unifies these four concepts into an actionable reference framework.

![AURA, the map of the path — two maturity axes, two field instruments, one decision framework](figuras/a01-camino-aura.png)

### Vision statement
> **Organizations are moving from the online enterprise — where people use tools to access and understand data — to the real-time enterprise — where people design and govern intelligent systems that autonomously detect, interpret, decide, and act on business information. AURA organizes this transformation along two diagnostic axes: IRIS measures the KNOWING trajectory (organizational intelligence); MOTOR measures the DOING trajectory (organizational automation). Together, within AURA, they diagnose the complete transformation.**

AURA integrates into a unified architecture what multiple industry players are proposing separately: Tableau and Cube on agentive analytics, Salesforce and AtScale on semantic architecture for agents, McKinsey and BCG on the transformation of human roles, Gartner and WEF on autonomy governance, and Deloitte and Informatica on data readiness for agents.

**What sets AURA apart** is that it is not confined to a single layer (technology, people, or governance) but integrates them as an interdependent transformation system — recognizing that advancing in one dimension without the others produces successful pilots but no real transformation. And it is operationalized in two complementary diagnostic models: IRIS for the knowledge axis and MOTOR for the execution axis.

### The nature of the transition: evolutionary coexistence
It is important to be honest about how this transformation happens in practice. It is not "throw everything out and start from scratch." Organizations do not jump from the current paradigm to the emerging one overnight.

The reality is a **hybrid model** in which existing infrastructure (data warehouses, ETL pipelines, BI tools) coexists with the new agentive capabilities. Traditional architecture remains valid for large-scale historical data warehousing, highly complex analytical models that require pre-computation, pipelines with very specific business logic, and regulatory requirements for retention and formal lineage.

What changes is the proportion. In the early stages, 90% is static infrastructure and the agent is an occasional assistant. In the advanced stages, the agent orchestrates most analytical operations and the static infrastructure becomes one more data source — robust and governed, but consumed by agents, not by humans.

This evolutionary coexistence is a fundamental principle of AURA and has a direct implication for IRIS: **each level does not invalidate the previous one — it subsumes it.** An organization at IRIS stages 7–8 did not eliminate its data warehouse — it integrated it into a semantic layer — a *fabric* — that agents consume autonomously. The online enterprise does not disappear when the real-time enterprise emerges — it becomes its foundation.

### Dimensions of AURA
| Dimension | Transformation trajectory |
|---|---|
| **Data & Architecture** | Data warehouse → semantic layer → agent-actionable knowledge fabric |
| **Analytical Capabilities** | Static BI → augmented analytics → autonomous intelligence → continuous cycle |
| **People & Culture** | Information consumers → designers of intelligent systems → governors of autonomy |
| **Governance** | Access control → governance of autonomous decisions → auditing of agent actions |
| **Operating Model** | Data competency centers → agent factories → ecosystem orchestration |
| **Business Value** | Insights for deciding → autonomous actions under supervision → self-optimizing business |

Each dimension progresses through the Value Pyramid: from organizations focused on the Data layer (accumulating and structuring), through Information (contextualizing and visualizing), then Knowledge (analyzing and understanding in real time), to Action (executing autonomously within governed frameworks). This progression marks the path from the foundations (online enterprise) to the real-time enterprise — the trajectory that IRIS operationalizes in its 10 stages, complemented by MOTOR, which measures the degree of automation of the processes that execute that action.

## Main Sources
| Source | Topic | Link |
|---|---|---|
| Gartner | Predictions on agents in enterprise apps | [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) |
| Gartner | Cancellation of agentive projects | [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) |
| McKinsey | Agentic organization and role redesign | [mckinsey.com](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-organization-blog/rethink-management-and-talent-for-agentic-ai) |
| BCG | AI at Work 2025: governance and roles | [bcg.com](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain) |
| BCG | Agents across the industrial value chain | [bcg.com](https://www.bcg.com/publications/2025/agentic-ai-industrial-goods-driving-change) |
| Deloitte | Agentive AI strategy and data readiness | [deloitte.com](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html) |
| Deloitte | Agent orchestration | [deloitte.com](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/ai-agent-orchestration.html) |
| KPMG | Governance in the agentive era | [kpmg.com](https://kpmg.com/us/en/articles/2025/ai-governance-for-the-agentic-ai-era.html) |
| Tableau | Agentic Analytics | [tableau.com](https://www.tableau.com/agentic-analytics) |
| Tableau | AI and the cycle of visual analysis | [tableau.com](https://www.tableau.com/blog/ai-agentic-analytics-upend-cycle-of-visual-analysis) |
| Salesforce | Agentive enterprise architecture | [architect.salesforce.com](https://architect.salesforce.com/fundamentals/agentic-enterprise-it-architecture) |
| AtScale | Semantic layer for AI agents | [atscale.com](https://www.atscale.com/blog/semantic-layers-agentic-ai/) |
| ThoughtSpot | Agentic Semantic Layer | [thoughtspot.com](https://www.thoughtspot.com/blog/introducing-the-agentic-semantic-layer) |
| Databricks | Agentic BI: infrastructure + semantics | [databricks.com](https://www.databricks.com/blog/delivering-agentic-bi-how-unify-infrastructure-data-and-semantics) |
| Informatica | Enterprise AI Agent Engineering | [informatica.com](https://www.informatica.com/resources/articles/enterprise-ai-agent-engineering.html) |
| eWeek | Agent-ready data and enterprise management | [eweek.com](https://www.eweek.com/artificial-intelligence/how-will-agentic-ai-change-enterprise-data-management/) |
| Singapore IMDA | Governance framework for agentive AI | [imda.gov.sg](https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf) |
| World Economic Forum | AI agents and progressive governance | [weforum.org](https://www.weforum.org/stories/2025/12/ai-agents-onboarding-governance/) |
| NACD | Board-level oversight of autonomous AI | [nacdonline.org](https://www.nacdonline.org/all-governance/governance-resources/directorship-magazine/online-exclusives/2025/q3-2025/autonomous-artificial-intelligence-oversight/) |
| ISACA | The challenge of auditing agentic AI | [isaca.org](https://www.isaca.org/resources/news-and-trends/industry-news/2025/the-growing-challenge-of-auditing-agentic-ai) |
| CIO.com | A new org chart for the agentive era | [cio.com](https://www.cio.com/article/4060162/the-new-org-chart-unlocking-value-with-ai-native-roles-in-the-agentic-era.html) |
| Cube | Agentic Analytics as the new modern analytics | [cube.dev](https://cube.dev/blog/why-agentic-analytics-is-the-new-modern-analytics) |
| Tellius | From questions to autonomous action | [tellius.com](https://www.tellius.com/resources/blog/agentic-analytics-explained-from-questions-to-autonomous-action) |
| Superwise | Beyond dashboards | [superwise.ai](https://superwise.ai/blog/ai-agents-beyond-dashboards/) |
| Ampcome | Use cases for analytical agents | [ampcome.com](https://www.ampcome.com/post/ai-agents-in-analytics) |
| CDO Trends | Semantic layers and AI-driven decisions | [cdotrends.com](https://www.cdotrends.com/story/4839/agentic-analytics-how-semantic-layers-are-powering-next-era-ai-driven-decision-making) |
| MindStudio | Enterprise AI agent governance | [mindstudio.ai](https://www.mindstudio.ai/blog/ai-agent-governance) |
