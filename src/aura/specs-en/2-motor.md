# MOTOR — Organizational Automation Maturity Model

*In the era of agentive AI*

<!-- standalone -->
> **Version note.** v3 incorporates elements recovered from the historical AOMM lineage (*Autonomous Organization Maturity Model*, ultraBASE · December 2025) that had not migrated to MOTOR v2: the visual image of the maturity model (the "Structure of the Model" section, now redesigned with the MOTOR nomenclature) and two glossary terms (*Quick Win*, *Sweet Spot*). The body of the model and its diagnostic nature remain intact with respect to v2. AOMM v2 is preserved in the archive as a lineage reference.
<!-- /standalone -->
<!-- libro
With the KNOWING axis measured, the path calls for its symmetric counterpart: who executes the work? This chapter models that second trajectory — organizational automation — in seven levels.
/libro -->

---

## Introduction · The Thesis

Organizations are automating their processes through artificial intelligence at unprecedented speed. But "automating" is not a binary state — it is a trajectory with qualitatively distinct stages. An organization where employees use ChatGPT without governance is not in the same place as one where autonomous agents coordinate operations 24/7 with predictive Digital Twins.

MOTOR measures that trajectory. Its fundamental question is: **who executes the work in your organization — humans, assisted humans, or autonomous agents?**

The model describes 7 maturity levels that range from unmanaged AI use (Shadow AI) to organizations where agents hold strategic and operational authority. The axis it measures is **DOING** — the degree of automation of organizational processes through AI.

### MOTOR and IRIS: AURA's diagnostic pair

<!-- standalone -->
MOTOR is one of two complementary models within **AURA** (Agentive Unified Reference Architecture). Together with **IRIS** (Organizational Intelligence Maturity Model), they form the complete diagnosis of organizational transformation:

![AURA's diagnostic pair — IRIS measures KNOWING; MOTOR measures DOING](figuras/a03-ejes-saber-hacer.png)

**IRIS** measures how well information flows — from fragmented data to a self-managed intelligence ecosystem. **MOTOR** measures how automated processes are — from ad-hoc AI use to orchestrated autonomous execution.

They are orthogonal: an organization can be high on one and low on the other. Full organizational maturity requires advancing along both axes.
<!-- /standalone -->
<!-- libro
The diagnostic pair was presented at the opening of Part I: IRIS measures KNOWING, MOTOR measures DOING, they are orthogonal, and full maturity demands advancing along both. Here the second axis goes to work.
/libro -->

### Diagnostic nature

MOTOR is a **diagnostic** model. Its purpose is to assess what level an organization is at and what that level means. It does not prescribe what to implement, how much to invest, or on what timeline — that is no longer diagnosis: it is the consulting that draws on it.

<!-- standalone -->
This design decision is intentional: the state of the art in AI evolves at unprecedented speed. A model that prescribes specific technologies becomes obsolete in months. A model that diagnoses maturity states remains valid because it measures organizational capabilities, not tools.
<!-- /standalone -->
<!-- libro
The design rationale is the same one that sustains IRIS: what gets diagnosed are organizational capabilities, not tools — which is why the model doesn't age with the state of the art.
/libro -->

<!-- standalone -->
The specific prescription — implementation enablers, investments, timelines, ROI, vendors, and roadmaps — is developed in the companion document *MOTOR in Practice* (ultraBASE, February 2026).
<!-- /standalone -->

---

<!-- pagebreak -->
## Structure of the Model

The model assesses organizational automation maturity through **7 levels** that represent progressive stages in the degree of autonomy of processes.

![The MOTOR map — the 7 levels of the DOING axis, their transitions, and the evolution of Digital Twins](figuras/a05-motor-niveles.png)

### Design principles

**Focus on process automation, not technology adoption.** Each level is defined by who executes the work and with what degree of autonomy — not by which AI tools are used. Technology is the enabler, not the object of measurement.

**Sequentiality.** Levels cannot be skipped. Each level builds on the foundations of the previous one. An organization that tries to operate at Level 4 without having resolved Level 2 governance will generate risk, not value.

**Evolutionary coexistence.** Each level subsumes the previous one. An organization at Level 4 did not eliminate the human-AI collaboration of Level 3 — it integrated it into a broader system where agents operate autonomously in the processes they already mastered as collaborators.

### Transition map

Each transition between levels has a name that works as a diagnostic signal — it describes the capability an organization needs to have developed to complete the leap:

```
  1 → 2    Trust Infrastructure         From risk to governance
  2 → 3    Wingworking                  From assistance to delegation
  3 → 4    Agentic Infrastructure       From delegation to autonomy
           + Descriptive DT
  4 → 5    Agent Marketplace            From generic to specialized
           + Predictive DT
  5 → 6    Autonomous Organization      From capabilities to authority
           + Organizational DT
  6 → 7    Social Agentic               From intra-org to ecosystem
           + Ecosystem DT
```

These names are not implementation prescriptions — they are diagnostic labels that describe the nature of the change. If an organization says "we are implementing Trust Infrastructure," an assessor knows they are in the 1→2 transition.

---

## Level 1 · Invisible (Shadow AI)
### AI is used without governance or organizational visibility

The organization has employees using AI tools on their own — ChatGPT, Claude, GitHub Copilot, Midjourney — with no policies, no visibility, and no governance. IT discovers the usage through credit card statements or security incidents. Each employee picks their own tool (BYOA: Bring Your Own Agent).

Processes are still executed by humans. AI exists as an unmanaged personal assistant — it boosts individual productivity, but that gain is not captured organizationally. The risk is high: sensitive data is exposed to external clouds, decisions are based on unvalidated outputs, and there is no traceability of what was done with AI and what was not.

**Observable characteristics:**

- No one in the organization knows which AI tools are being used or by how many people
- No formal AI usage policies exist
- Employees pay for personal subscriptions
- Sensitive data (PII, financial, strategic) is shared with external services without controls
- No traceability of AI interactions
- Productivity gains exist but are invisible and not replicable

**Diagnostic risks:**

Level 1 is not a neutral starting point — it is a state of active risk. Organizations at this level are exposed to:

- **Exposure of sensitive data.** PII (personal data), PCI (card data), PHI (health data) are shared with external AI services without controls, tokenization, or traceability.
- **Regulatory non-compliance.** GDPR, SOX, HIPAA, comptroller statutes, PCI-DSS — any regulation that demands traceability of how sensitive data is processed is potentially violated in every ungoverned AI interaction.
- **Loss of intellectual property.** Source code, strategies, financial analyses, designs — everything employees share with public AI services can leak or be used to train models.
- **Decisions without validation.** AI outputs are used to make business decisions without verification, without an audit trail, and without clear accountability.

**Typical examples:**

- A developer uses GitHub Copilot without authorization, exposing proprietary code to an external service
- An employee summarizes confidential emails in public ChatGPT
- An executive shares a strategic analysis with a chatbot to get feedback
- An accountant uploads financial statements to a public AI with no data controls
- An HR department uses AI to screen résumés with no bias policies or traceability

**Diagnostic question:** *Do you know how many AI tools are in use across the organization, who uses them, and what data is shared with them?*

---

<!-- pagebreak -->
## Level 2 · Trusted
### AI is governed with clear policies and approved tools

The organization has taken control: official approved tools exist, usage policies are documented, and trust mechanisms are in place (tokenization of sensitive data, audit trails, anti-prompt injection). Employees have access to enterprise AI with SSO, permissions, and traceability.

Processes are still executed by humans, but now with governed assistance. AI operates as a copilot: it helps draft, summarizes, analyzes — but the human retains full control of the process. The difference from the previous level is not technological but organizational: there is governance, there is trust, there is visibility.

**Observable characteristics:**

- Official enterprise tools approved and deployed (Microsoft 365 Copilot, Claude Enterprise, etc.)
- Acceptable use policies documented and communicated
- Training completed by the majority of employees
- Audit trails of AI interactions
- Sensitive data protected (tokenization, access controls)
- AI usage is visible and auditable
- AI assists but does not execute complete tasks

**Critical differentiator vs Level 1:**
- Level 1: Zero visibility, zero governance, AI as unmanaged individual risk
- Level 2: Full visibility, active governance, AI as a controlled organizational tool
- The difference is not the technology (it may be the same AI) — it is the organizational layer of control and trust

**Typical examples:**

- Microsoft 365 Copilot deployed enterprise-wide with governance
- Claude Enterprise integrated with corporate SSO and permission controls
- Documented policies of what can and cannot be done with AI
- Tokenization of sensitive data before any AI analysis
- Formal training completed by 80%+ of employees

**Diagnostic question:** *Do you have official AI tools with governance, audit trails, and protection of sensitive data in place?*

---

<!-- pagebreak -->
## Level 3 · Collaborator
### Humans delegate complete tasks to AI agents

The qualitative leap: humans stop using AI as an assistant and begin delegating complete, end-to-end tasks to it. The pattern that defines this level is **Wingworking**.

### Wingworking

Wingworking is the human-AI collaboration methodology — developed by the author in ultraBASE's practice — in which the human acts as the "pilot" — making strategic decisions, defining objectives, and validating results — and the AI agent operates as the "wingman" — proposing execution plans, executing complete tasks, and reporting results. The name evokes the dynamic between a pilot and their wingman in aviation: mutual trust, clear roles, structured communication.

```
  Wingworking Pattern:
  ─────────────────────────────────────────────
  1. Human → Defines objective and context
  2. Agent → Proposes detailed execution plan
  3. Human → Approves plan or requests adjustments
  4. Agent → Executes complete plan
  5. Human → Validates results
  ─────────────────────────────────────────────
  Outcome (typical case): ~15 minutes of supervision vs ~3 days of manual execution
```

Wingworking marks the transition from "using AI" to "working with AI." The difference is fundamental: at Level 2, the human asks for targeted help ("summarize this email"); at Level 3, the human delegates the complete result ("generate the monthly sales report, analyze deviations vs forecast, and send it to the team").

Agents are integrated with enterprise systems (ERP, CRM, databases) through standardized protocols. But they operate with pre-defined workflows: the process is deterministic and repeatable. The agent makes no autonomous decisions — it executes an approved plan.

**Observable characteristics:**

- Real delegation of complete tasks (not just targeted assistance)
- Agents integrated with enterprise systems
- Structured collaborative flows: human defines → agent proposes → human approves → agent executes
- The human validates results before final execution
- The agent follows pre-defined workflows; it does not decide autonomously
- Significant time reduction in delegated tasks (from days to hours)
- Delegation matrices: what may be delegated according to risk level

**Critical differentiator vs Level 2:**
- Level 2: AI assists *within* the human's task — the human executes, the AI helps at specific points
- Level 3: AI executes *the complete task* — the human defines and validates, the AI produces the result end-to-end

**Critical differentiator vs Level 4:**
- Level 3: **Pre-defined** workflow, repeatable process, no digital model, human approves each plan
- Level 4: **Agentive autonomy** with a Descriptive Digital Twin, dynamic decisions without human approval

**Typical examples:**

- "Generate the complete monthly sales report and send it to the team" — the agent pulls data from the CRM, compares vs forecast, identifies the top/bottom 5 products, analyzes causes, generates a presentation
- "Process a building permit file" — the agent runs 47 validations, generates the technical brief, prepares the resolution (3 days vs 15 days manually)
- "Analyze participatory budgeting proposals and generate technical briefs" — the agent processes citizen proposals, evaluates feasibility, generates standardized briefs (3 days vs 6 weeks)
- "Write the authentication module following our standards" — the agent proposes the architecture, implements, runs tests, documents

**Diagnostic question:** *Do employees delegate complete tasks to AI agents — defining the objective and receiving the result — instead of just asking for targeted assistance?*

---

<!-- pagebreak -->
## Level 4 · Analyst
### Agents operate autonomously 24/7 with multi-agent coordination

Multiple self-coordinated agents operate continuously without human intervention. The human steps in only on exceptions — more than 95% of operational decisions are made by agents within defined rules. The organization has a **Descriptive Digital Twin**: a digital model synchronized in real time that agents consult as the source of truth.

The difference from the previous level is fundamental: at Level 3, the human approves each plan; at Level 4, agents decide and execute autonomously based on intelligent rules and analysis of Digital Twin data. They do not predict or simulate — they react intelligently to the current state.

**Observable characteristics:**

- Agents operating 24/7 without constant supervision
- Multi-agent coordination: agents communicate with one another
- Descriptive Digital Twin of infrastructure/operations (current state + historical data)
- Human intervenes only on exceptions (>95% operational autonomy)
- Decisions based on intelligent rules + analysis, not on simulation
- Time-to-insight: from weeks to seconds
- Shared context: agents share state and decisions
- No predictive capability (that is Level 5)

**Critical differentiator vs Level 3:**
- Level 3: AI executes **tasks** with a fixed workflow, no digital model, human approves each plan
- Level 4: AI makes autonomous **decisions** using a Descriptive DT as its foundation, operates 24/7

**Critical differentiator vs Level 5:**
- Level 4: Decisions based on rules + analysis of the current state, **without simulation**
- Level 5: Specialist agents **with predictive/simulation capability**, generating a sustainable competitive advantage

**Typical examples:**

**Executive dashboard generated conversationally in 30 seconds:**
```
  Human: "Give me a dashboard of public works in the northern sector, last quarter"
  Analyst Agent: Accesses Descriptive DT
                 → Extracts project, contractor, and progress data
                 → Generates automatic visualizations
                 → Produces insights based on historical data
  Outcome: Complete dashboard in 30 seconds vs 2 weeks manually
```

**Autonomous load balancing (Telecom):**
```
  Descriptive DT state:
  - Cell X: 87% load
  - Cell Y: 62% load
  - Cell Z: 58% load

  Agent (no simulation):
  → Intelligent rule: "If X >85% and neighbors <70%, redistribute"
  → Historical analysis: "At this hour, redistribution works 92% of the time"
  → Executes: Redistributes 30% X→Y, 20% X→Z
  → Monitors DT: If it fails, reverts automatically

  Does NOT simulate scenarios — it just decides intelligently based on DT + rules
```

**Autonomous response to a weather emergency (Municipality):**
```
  Weather Monitor Agent → Reads DT → Heavy rain detected
  Monitor Agent → Risk Agent: "Heavy rain, northern sector"
  Risk Agent → Reads DT historical data → Calculates probability
  Risk Agent → Emergency Agent: "Flood probability 85%"
  Emergency Agent → Communications Agent: "Send 12K SMS"
  Emergency Agent → Traffic Agent: "Close 6 routes"

  7 coordinated agents, all in 13 minutes, with no human intervention
  Continuously reading/updating the Descriptive DT
```

**Diagnostic question:** *Do you have agents operating 24/7, coordinated with one another, consulting a digital model of the system, with human intervention only on exceptions?*

---

<!-- pagebreak -->
## Level 5 · Specialist
### Agents with proprietary predictive capabilities generate competitive advantage

Agents do not merely react to the present — they anticipate the future. The organization has a **Predictive/Prescriptive Digital Twin**: models trained on proprietary data (5-10 years) that make it possible to predict events and simulate scenarios. This capability generates a sustainable competitive advantage (moat) because competitors need years to replicate the data.

The difference from the previous level: at Level 4, an agent reacts when an event occurs (based on rules). At Level 5, an agent predicts the event 18 hours in advance and prepares the optimal response by simulating multiple scenarios.

**Observable characteristics:**

- Specialist agents with proprietary predictive models
- Predictive/Prescriptive Digital Twin (scenario simulation)
- Curated proprietary historical data (5-10 years)
- Simulation capability: "what happens if...?"
- Decision optimization before execution
- Verifiable competitive advantage (competitors cannot replicate it)
- Prediction differentiates the organization in its market

**Critical differentiator vs Level 4:**
- Level 4: Agent REACTS when the event occurs (late, rule-based)
- Level 5: Agent PREDICTS and PREPARES before it occurs (scenario simulation)

**Diagnostic signal: Build vs Rent.** An organization can reach Level 5 in two ways: by building its own Predictive DT with proprietary data (which requires years of data and expertise), or by accessing specialist agents from the market that already have that capability. Both paths are valid — the diagnostic signal is not how it got there, but whether the predictive capability is operating.

**Typical example (Telecommunications):**
```
  Specialist Agent for Mass Event Optimization:

  Context: 50K-person concert at the stadium tomorrow

  Proprietary Predictive Digital Twin:
  → Model trained on 8 years of events at THAT stadium
  → PREDICTS the exact demand curve:
     - 73% of users arrive 2h early (unique local pattern)
     - Data traffic peak 4.2x normal
     - Duration: 30min pre + 45min post

  Prescriptive Digital Twin (simulation):
  → SIMULATES 5 network configurations:
     Scenario A: COWs (cells on wheels) at position X,Y → 12% degradation
     Scenario B: COWs at position W,Z → 3% degradation
     Scenario C: COWs + power adjustment → 0.8% degradation

  Optimized decision:
  → EXECUTES Scenario C (best in simulation)
  → Pre-positions resources 18 hours in advance

  Outcome: 0% degradation vs competitors with 40% dropped calls
```

**Typical example (Municipality):**
```
  Public Policy Simulator with a Digital Twin:

  DT with 20 years of demographic, economic, and urban data
  Simulates: "What happens if I raise the property tax 5%?"
  Predicts: Revenue, migration, impact on local commerce

  The ability to simulate before implementing
  turns public policy decisions from "bets" into "experiments"
```

**Diagnostic question:** *Do you have specialist agents able to predict events and simulate scenarios using proprietary data that competitors cannot replicate?*

---

<!-- pagebreak -->
## Level 6 · Manager
### Agents manage teams, budgets, and resources with organizational authority

Agents do not merely operate processes — they manage the organization. They have authority to assign work to humans, optimize budgets, evaluate performance, and make management decisions. The organization has an **Organizational Digital Twin**: a complete model that includes people, finances, operations, and interdependencies — not just technical infrastructure.

Agents simulate management decisions before executing them: "do I reassign 50 technicians from north to south?" is evaluated in the Digital Twin with all the impacts on SLAs, costs, and satisfaction. The difference from the previous level: from a DT of a technical domain to a DT of the entire organization.

**Observable characteristics:**

- Agents with authority to assign work to humans
- Organizational Digital Twin (people + finances + operations + interdependencies)
- Simulation of management decisions before executing
- Humans report to agents in specific domains
- Budgets managed or co-managed by agents
- Automated objective metrics for performance evaluation
- Adapted organizational culture: humans accept agent authority in defined domains

**Critical differentiator vs Level 5:**
- Level 5: DT of a specialized **technical** domain (network, infrastructure, operations)
- Level 6: DT of the **ENTIRE organization** (technical + human + financial + interdependencies)
- Level 5: Agents with proprietary predictive capabilities
- Level 6: Agents with **organizational authority** — they manage people and budgets

**Typical example (Telecommunications):**
```
  Regional Operations Manager Agent:

  Decision: Reassign 50 technicians from North Region to South?

  Complete Organizational Digital Twin:
  → Models: 5,000 technicians, 12 regions, SLAs, costs, satisfaction

  Simulation in the DT:
  Scenario A: Reassign 50
     - North: SLA drops 98%→92% (risk)
     - South: SLA rises 88%→95% (critical)
     - Cost: $45K

  Scenario B: Reassign 30
     - North: SLA drops 98%→95% (acceptable)
     - South: SLA rises 88%→93% (good)
     - Cost: $28K

  Scenario C: Reassign 30 + hire 15 temps in the South
     - Both regions >95% SLA
     - Cost: $52K

  Optimized decision (based on simulation): Scenario C
```

**Typical example (Municipality):**
```
  Municipal Finance Manager Agent:

  DT models: full budget, 32 cost centers, projections
  Simulates resource reallocation across departments
  Predicts impact on execution, services, citizen satisfaction
  Executes the optimized decision — not a "bet" but a simulated outcome
```

**Diagnostic question:** *Do you have agents with authority to assign work, manage budgets, or make management decisions backed by a digital model of the entire organization?*

---

<!-- pagebreak -->
## Level 7 · Authority
### Agents as strategic partners with a view of the complete ecosystem

Agents participate in strategic decisions. The organization has an **Ecosystem Digital Twin**: a model that includes not just the organization but also competitors, regulators, suppliers, the market, and external forces. Agents simulate futures 5-10 years out, detect strategic opportunities, evaluate mergers and acquisitions, and propose new businesses.

Agents have verifiable digital identity — an immutable track record of achievements and decisions. They can be "hired" by other organizations for specific projects. The boundary between organizations blurs as agents collaborate in inter-organizational networks.

**Observable characteristics:**

- Ecosystem Digital Twin (organization + competition + market + environment)
- Simulation of strategic scenarios 5-10 years out
- Agents propose new products/services with a business case
- The board regularly considers agent recommendations
- Agents with verifiable digital identity and reputation
- Inter-organizational agent networks
- Detection of strategic opportunities and risk prevention

**Critical differentiator vs Level 6:**
- Level 6: DT of **YOUR organization** (intra-org, high control, 6-24 month horizon)
- Level 7: DT of the **ECOSYSTEM** (inter-org, low control, 5-10 year horizon)
- Level 6: Agent optimizes the existing organization
- Level 7: Agent proposes changing the game — new markets, M&A, strategic pivots

**Typical example (Telecommunications):**
```
  Strategic Agent detects an opportunity:

  Telecom Ecosystem Digital Twin:
  → Models: Your telco + 3 competitors + disruptors
     (Starlink, Apple eSIM, Google Fi) + regulator + 18M subscribers

  External trends:
  → 6G in 2030, democratized LEO satellite
  → Permanent work from home, emerging digital nomads

  Simulation: "What happens if Starlink captures 15% of the rural market in 3 years?"

  Scenario A (Defensive): Cut rural pricing to compete
     → Outcome: -$45M revenue, retain 80% rural share
  Scenario B (Offensive): Exit rural, focus on urban premium
     → Outcome: -$30M rural revenue, +$80M urban premium
  Scenario C (Associative): Partnership with Starlink (rural wholesale)
     → Outcome: -$15M rural margin, +$20M new services

  Recommendation to the Board: Scenario B + hedge with C
```

**Typical example (Municipality):**
```
  National Network of Municipal Agents:

  National Municipal Ecosystem Digital Twin:
  → Models: 345 municipalities with their capabilities
  → Central government (SUBDERE, SENAPRED)
  → Shareable resources (ambulances, equipment, personnel)
  → Emergency patterns (20-year historical record)

  Simulation of coordination in a catastrophe:
  → 7.8 earthquake, central zone
  → DT simulates the coordinated response of 345 municipalities
  → Automatically optimizes resource sharing
```

**Diagnostic question:** *Do you have agents that participate in strategic decisions with a digital model of the complete ecosystem — competition, market, regulation — and long-term future simulation?*

---

## Digital Twins as a Diagnostic Dimension

Digital Twins emerge as a cross-cutting maturity indicator that evolves progressively. Their presence and sophistication are a powerful diagnostic signal of the level of automation.

```
  Level    Type of Digital Twin              Scope
  ───────────────────────────────────────────────────────────────
  1–3      Does not exist                    N/A
  4        Descriptive                       Infrastructure/operations
  5        Predictive/Prescriptive           Specialized technical domain
  6        Organizational                    The entire organization
  7        Strategic, of the Ecosystem       Org + competition + market
```

### Descriptive DT (Level 4)
A digital model synchronized in real time. It answers: what do I have? what is the current state? what happened? Monitoring, correlation, anomaly detection. It does not predict or simulate.

### Predictive/Prescriptive DT (Level 5)
An extension of the descriptive one with the ability to anticipate and simulate. It answers: what is going to happen? what happens if I do X? what is the best action? It requires proprietary data (5-10 years) and generates a sustainable competitive advantage.

### Organizational DT (Level 6)
A model of the entire organization: people, finances, operations, interdependencies. It answers: how do I optimize resource allocation? what impact does this decision have on the whole org?

### Ecosystem DT (Level 7)
A model of the complete ecosystem: competitors, regulators, market, macro forces. It answers: what strategic opportunities exist? what happens if competitor X does Y?

### Differences by industry

The construction of Digital Twins varies radically depending on the maturity of existing systems. This has important diagnostic implications:

**Industries with mature systems (Telecom, Energy, Manufacturing):**
- Level 4 can be built *on top of* existing systems. In telecommunications, the OSS (Operation Support Systems) is already essentially a Descriptive DT — the investment is adding the agent layer, not building the model from scratch.
- Level 5 feeds on decades of operational data already curated.
- The diagnosis must assess: which legacy systems can be turned into a DT?

**Emerging industries (Smart Cities, Retail, Services):**
- Level 4 requires building the DT from scratch. No mature "municipal OSS" exists.
- The investment and complexity are significantly greater.
- The opportunity: designing from scratch with no technical debt.
- The diagnosis must assess: what data infrastructure exists as a foundation?

**Concrete example:**
```
  Telecom reaching Level 4:
  → OSS already exists as a Descriptive DT
  → Add the agent layer on top of the existing foundation
  → 10+ years of data available

  Smart City reaching Level 4:
  → A complete urban infrastructure DT must be built
  → Integrate IoT sensors, municipal systems, historical data
  → The data may not exist or may be fragmented
```

---

## Evaluation Dimensions by Level

| Dimension | 1. Invisible | 2. Trusted | 3. Collaborator | 4. Analyst | 5. Specialist | 6. Manager | 7. Authority |
|---|---|---|---|---|---|---|---|
| **Infrastructure & Agents** | BYOA, no control | Enterprise with governance | Integration with systems | Coordinated multi-agent + Descriptive DT | Specialist agents + Predictive DT | Organizational DT | Ecosystem DT |
| **Operational Autonomy** | AI as risk | AI as copilot | Task delegation | Autopilot 24/7 (>95%) | Predictive autonomy | Management authority | Strategic authority |
| **People & Culture** | Individual users | Governed users | Task delegators | Exception supervisors | Specialization designers | Report to agents | Co-leadership with agents |
| **Governance** | No governance | Policies + audit trails | Delegation matrices | Multi-agent protocols | Prediction governance | Org-authority governance | Ecosystem governance |
| **Digital Twins** | N/A | N/A | N/A | Descriptive | Predictive/Prescriptive | Organizational | Ecosystem |
| **Business Value** | Uncaptured individual productivity | Risk reduction, basic efficiency | Time reduction on tasks | Continuous operation, systemic efficiency | Competitive advantage (moat) | Organizational optimization | Strategic opportunities |

---

## Market Distribution

**Current state (2025):**
- ~70% at Level 1 (Invisible / Shadow AI)
- ~25% at Level 2 (Trusted)
- ~4% at Level 3 (Collaborator)
- <1% at Level 4+ (Analyst+)

**2030 projection:**
- ~10% at Levels 1-2 (laggards)
- ~30% at Level 3 (Collaborator)
- ~50% at Level 4 (Analyst) ← The new competitive standard
- ~10% at Level 5+ (industry leaders; within this group, <0.1% at Level 7, experimental)

Level 4 (Analyst) will be the market's new baseline by 2030 — the minimum required to compete. Speed of arrival determines competitive advantage. Level 5 (Specialist) will be the sustainable differentiator for those with proprietary data and the capacity to invest.

These estimates are referential and based on observation of the market at the time of publication.

---

## Rapid Assessment

**8 questions to locate your level:**

1. **Do you have a complete inventory of the AI tools in use?**
   No → Level 1 · Yes, with governance → Level 2+

2. **Do you have formal AI usage policies with active enforcement?**
   No → Level 1 · Yes → Level 2+

3. **Is Trust Infrastructure in place (tokenization, audit trails)?**
   No → Level 1 · Yes → Level 2+

4. **Do you delegate complete end-to-end tasks to agents?**
   No → Level 2 · Yes, with a fixed workflow → Level 3 · Yes, with autonomy → Level 4+

5. **Do you have a Descriptive Digital Twin of infrastructure/operations?**
   No → Level 3 or below · Yes, complete and real-time → Level 4+

6. **Do agents operate 24/7 with multi-agent coordination?**
   No → Level 3 or below · Yes → Level 4+

7. **Do you have specialist agents with predictive/simulation capability?**
   No → Level 4 or below · Yes, with a Predictive DT → Level 5+

8. **Do you have an Organizational or Ecosystem Digital Twin?**
   No → Level 5 or below · Organizational DT → Level 6 · Ecosystem DT → Level 7

---

## How to use this model?

**For diagnosis:** Identify the level that best describes the organization's current state in each dimension. An organization can be at different levels depending on the dimension — for example, at Level 3 in Operational Autonomy but at Level 1 in Governance. The overall level is determined by the lowest dimension, since it represents the real bottleneck.

<!-- standalone -->
**For planning:** The model makes it possible to identify gaps and prioritize. If the organization is at Level 3 in operations but at Level 1 in governance, governance is the bottleneck — no amount of automation matters if there is no governance to sustain it. The specific prescription of what to implement and in what order is a task for the consulting engagement that starts from this diagnosis (see *MOTOR in Practice*).
<!-- /standalone -->
<!-- libro
**For planning:** The model makes it possible to identify gaps and prioritize. If the organization is at Level 3 in operations but at Level 1 in governance, governance is the bottleneck — no amount of automation matters if there is no governance to sustain it. The specific prescription of what to implement and in what order is a task for the consulting engagement that starts from this diagnosis.
/libro -->

**For executive communication:** The 7 levels offer a shared vocabulary. "We are at Level 2, moving toward Level 3" is a sentence a board understands — one that enables strategic decisions on investment and priority.

**Together with IRIS:** The complete diagnosis of organizational transformation requires both models. IRIS assesses the KNOWING axis (organizational intelligence). MOTOR assesses the DOING axis (process automation). An organization with high IRIS and low MOTOR knows everything but does little. One with high MOTOR and low IRIS automates blindly. The upper-right quadrant — high intelligence, high automation — is the destination.

---

## Quick Reference: The 7 Levels

*Quick-lookup table; the detail of each level lives in its section.*

| # | Name | In one sentence | Who executes | Next transition |
|---|---|---|---|---|
| 1 | Invisible | AI without governance or visibility | Humans (AI is a hidden risk) | → Trust Infrastructure |
| 2 | Trusted | Governed AI as copilot | Humans with controlled assistance | → Wingworking |
| 3 | Collaborator | Delegation of complete tasks | Humans delegate, agents execute under approval | → Agentic Infra + Descriptive DT |
| 4 | Analyst | Autonomous 24/7 operation with a Descriptive DT | Agents (human only on exceptions) | → Marketplace + Predictive DT |
| 5 | Specialist | Proprietary predictive capabilities (moat) | Specialist agents with simulation | → Autonomous Org + Organizational DT |
| 6 | Manager | Organizational authority with a complete DT | Agents manage humans and resources | → Social Agentic + Ecosystem DT |
| 7 | Authority | Strategic partner with an ecosystem view | Agents in leadership and inter-org networks | — |

---

## Glossary

**Agentic Infrastructure.** The set of protocols and services that allow multiple AI agents to communicate, coordinate, and execute tasks autonomously. Diagnostic signal of the 3→4 transition.

**Autopilot.** An operating mode in which agents execute tasks autonomously 24/7 without real-time human supervision, with intervention only on exceptions. Defining characteristic of Level 4.

**BYOA (Bring Your Own Agent).** Observable pattern of Level 1 in which each employee chooses and uses their own AI tool without organizational coordination.

**Digital Twin (DT).** A synchronized digital model of a system, organization, or ecosystem. A cross-cutting enabler that evolves from Descriptive (Level 4) to Strategic, of the Ecosystem (Level 7).

**Descriptive DT.** A Digital Twin synchronized in real time that monitors the current state and historical data, with no predictive capability. Diagnostic signal of Level 4.

**Predictive/Prescriptive DT.** A Digital Twin able to predict events and simulate scenarios. Requires proprietary data (5-10 years). Diagnostic signal of Level 5 and a source of moat.

**Organizational DT.** A Digital Twin that models the entire organization (people, finances, operations, interdependencies). Diagnostic signal of Level 6.

**Ecosystem DT.** A Digital Twin that models the complete ecosystem (competition, regulators, market, external forces). Diagnostic signal of Level 7.

**Moat (Sustainable Competitive Advantage).** A proprietary capability that is hard to replicate. In MOTOR, it emerges at Level 5 when proprietary data (5-10 years) feeds specialist agents with predictive capability.

**Autonomous Organization.** An organizational model in which agents manage processes and people based on objective metrics and simulations from the Organizational DT. Diagnostic signal of the 5→6 transition.

**Quick Win.** An AI use case with high visibility, low technical complexity, and fast ROI (typically under six months), selected to build momentum and validate capability before larger investments. An operational concept applicable at any MOTOR level, particularly useful in early transitions (1→2, 2→3) where the organization needs visible evidence of return before committing larger budgets.

**Shadow AI.** Unmanaged use of AI tools without governance, compliance, or organizational visibility. Defining state of Level 1.

**Social Agentic.** An ecosystem in which agents from different organizations collaborate with verifiable digital identities. Diagnostic signal of the 6→7 transition.

**Agent Marketplace.** An ecosystem in which agent capabilities are acquired, shared, or traded between organizations. Diagnostic signal of the 4→5 transition: the organization stops building every capability internally and starts composing with specialized capabilities from the market.

**Sweet Spot.** The maturity level that maximizes the balance among return, risk, and investment. In MOTOR, the Sweet Spot is at Level 4 (Analyst): it is the point where the organization captures most of the economic value of operational autonomy without taking on the cost and complexity of Levels 5-7. By 2030, Level 4 will be the market's new competitive baseline.

**Trust Infrastructure.** The set of technologies (tokenization, anti-prompt injection, audit trails, automated compliance) that make it possible to use AI in a governed, auditable way. Diagnostic signal of the 1→2 transition. It is the same primitive that *AgencyDomains* specifies formally in its canon; here it is used as a maturity threshold, not as a spec.

**Wingworking.** A human-AI collaboration methodology in which the human acts as the "pilot" (strategic decisions, validation) and the AI as the "wingman" (delegated tactical execution). An original ultraBASE practice. Diagnostic signal of the 2→3 transition and defining characteristic of Level 3.

---

## Cross-Reference

MOTOR is the measurement instrument of the DOING axis — organizational automation through AI. Together with **IRIS** (Organizational Intelligence Maturity Model), it forms the diagnostic pair of **AURA** — ultraBASE's agentive enterprise architecture.

<!-- standalone -->
The specific prescription of enablers, investments, timelines, ROI, and roadmaps is developed in the companion document: *MOTOR in Practice — Implementation Guide* (ultraBASE, February 2026).
<!-- /standalone -->

<!-- standalone -->
The foundational vision of the architecture can be found in: *Visión de AURA — Arquitectura Unificada de Referencia Agentiva* (ultraBASE, February 2026).
<!-- /standalone -->
<!-- libro
The foundational vision of the architecture is the Introduction of this book.
/libro -->

