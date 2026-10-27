# 6. The Five Control Layers

The system of truth answers the board's gravest question, but not the only one. When an organization puts agents to work on its business, whoever has to trust them asks several things, and each question asks for its control. I order them in five **control layers**, always with that adjective, so as not to confuse them with the four layers of the architecture *AgencyDomains* describes: those say how a system is put together; these, what whoever must trust it needs to know. They are my judgment, not an industry standard. They rest on the standards that exist and on the controls the most demanding industries already require before letting artificial intelligence act without human intervention.

## What are they?

**1 · Truth.** *Are the numbers and the records correct?* It is the system of truth of chapter 5, with its contract and its two guarantors, for the records the organization is accountable to others for. It is the control layer that should not certify itself.

**2 · Identity and authority.** *Who acted, on whose behalf, and who answers?* Every agent has an identity of its own, acts with explicit permissions and on someone's behalf, and every act has a person or an area that answers for it. Without this control layer, the traceability of the first one records acts without an owner.

**3 · Movement.** *What do the agents do, and how far do they decide on their own?* The agents and the platform they run on, with human supervision and an autonomy granted by degrees, process by process, as it is granted to a new person in a job. Mind the name: this control layer is not Layer 3 of the *AgencyDomains* architecture, which is a layer of the system; here the question is that of whoever observes what the agents do.

**4 · Measurement.** *How do we know they do it well, today and tomorrow?* Every agent is tested against known cases before operating, and keeps being measured while it operates, with alarms when its performance degrades.

**5 · Judgment.** *Are we building it well, and can we change course?* Industry standards as the starting point, and an architecture team that decides what must exist and with which standards, and that can judge what the agent shapes by its behavior, its tests and its trace, even without reading the code. I use "judgment" in the sense of the technical judgment of whoever builds; it is not the "delegated judgment" with which *The Real-Time Enterprise* describes the agent.

Read together, they divide up the risks of chapter 4. The fifth avoids the dead end and bounds the delay. The first and the fourth answer for quality. The second and the third make automation governable.

## What cuts across all five?

Two conditions every control layer has to meet.

**People**: who operates each layer and governs its evolution, and with what training. A construction whose behavior nobody in the organization understands repeats the dependency the organization wanted to leave behind when it stopped buying software.

**Reversal**: what happens when something fails, and how to go back without stopping the business. It has nothing to do with the personal reversibility of the agentive mode in *The Real-Time Enterprise*, which is that of a person who enters and leaves the agentive world with a gesture.

| Control layer | People | Reversal |
|---|---|---|
| 1 · Truth | Those responsible for each record | A correction is a new record |
| 2 · Identity and authority | Whoever grants and withdraws permissions | A permission is withdrawn on the spot, and what was done with it stays traced |
| 3 · Movement | The supervisors of each process | Stop, pause or revert; carry on in manual mode |
| 4 · Measurement | Whoever defines the tests and attends to the alarms | The agent that degrades loses autonomy |
| 5 · Judgment | The architecture team | A component can be replaced without redoing the rest |

Each cell is a question an organization can ask itself about its own system or about any offer it receives.

## How do they map to Trust Infrastructure?

*AgencyDomains* defines Trust Infrastructure with five pillars: governance, audit, validation, resilience and transparency.[^pilares] The control layers look at the same ground from the side of whoever has to trust, rather than from the side of whoever builds. My reading of the correspondence:

| Control layer | Trust Infrastructure pillars that sustain it |
|---|---|
| 1 · Truth | Audit, plus the contract, the degree of truth and the second guarantor |
| 2 · Identity and authority | Governance |
| 3 · Movement | Governance and resilience |
| 4 · Measurement | Validation and transparency |
| 5 · Judgment | None: it is a condition of whoever builds |

## Does it also hold for what is not built with agents?

Yes, and that is why I think it is a good framework. A suite licensed and operated in-house meets the first control layer with its own core of records, and its vendor answers for it. When the same suite adds agents, as all vendors are doing, the other four apply to it just as they do to a construction of one's own. The framework asks every form of solution to answer the same questions. If the suite is a rented service, the one operating that core is the vendor, and then it is not yet a system of truth in the sense of chapter 5, which is operated by whoever uses it: the second guarantor is needed more, not less. Custom development answers all five like any other form, and usually fails at the first: whoever made it and whoever audits it are the same organization.

What changes is which one costs more. Whoever rents usually struggles with the third control layer, because the agents the vendor adds run in its cloud and are governed by its rules. My observation, without measuring it: whoever licenses and operates in-house struggles less, because they see where they run and what they do. Whoever builds, the first.

[^pilares]: César Obach-Renner, *AgencyDomains: Agentive Architecture*, chapter 5, "Trust Infrastructure", "The five pillars".
