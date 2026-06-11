# 2. Communication Comes to You

*In the film: 9:30. Elena said "notify whoever needs to know," four destinations received four versions of the same fact, and nobody was interrupted. Fourteen seconds that buried an hour of emails. This chapter explains the inversion that makes it possible.*

## The Hollywood Principle

Software engineering has known for decades a design principle called the Hollywood Principle: *don't call us, we'll call you*. It describes the inversion of control — instead of each component chasing what it needs, the system delivers to each component what belongs to it, when it belongs to it.

Applied to business communication, the principle illuminates the three stages of its history:

| Stage | Direction of flow | Who controls? |
|---|---|---|
| **Email** | Communication comes to you — unfiltered, unprioritized, unactionable | Nobody: chaos in the inbox |
| **Chat** | You go to the communication — permanent pull, channel by channel | The channel controls your attention |
| **Postchat** | Communication comes to you — filtered, prioritized, actionable, at the right moment | The agent controls the flow; you control the decisions |

Email had the right direction and no governance. Chat added immediacy at the price of inverting the direction: it made you the hunter of your own information. Postchat takes the best of each and removes the worst: communication arrives — but it arrives governed. And silence changes its nature: it stops meaning "maybe I'm missing something" and comes to mean, with the system's guarantee, *there is nothing for you*. It is the difference between anxiety and operational peace, and it is the difference no incremental improvement of the channel can produce.

<!-- FIG:f01-tres-estadios -->
![The three stages of enterprise communication](figuras/f01-tres-estadios.png)

## The seven variables

The depth of the inversion is measured by taking inventory of the variables that office communication forces you to manage by hand. There are seven:

| Variable | In chat (the user manages them) | In Postchat (the agent manages them) |
|---|---|---|
| **Destination** | Choose the channel and whom to mention | The agent derives who needs to know from a model of the organization |
| **Format** | One generic message for the whole audience | Reformulation per recipient, by role and mental model |
| **Timing** | The channel interrupts when it wants; the user scrolls when they can | Delivery in scheduled briefings; interruption only for genuine urgency |
| **Priority** | Assessed by reading everything | Classification by urgency and relevance |
| **Memory** | The user remembers (or excavates the history) | An organizational knowledge graph, queryable |
| **Follow-up** | The user chases replies and acknowledgments | The agent closes the loops: nothing goes unanswered |
| **Decision** | The user convenes, moderates, and synthesizes | The agent facilitates the process; the person decides |

Of the seven, the Postchat user retains exactly three: the **intention** (what they want to communicate, with its nuances), the **deep-dive** (what they want to go into after the briefing), and the **decision**. The other four the system assumes entirely. The difference from today's office is not one of degree: it is the difference between driving with a stick shift, a clutch, and a map on your knees — and telling the vehicle where you want to go.

The subtlest variable deserves underlining: format. The agent does not forward the same text to several destinations — it **reformulates for each recipient**. From the same operational fact, the director receives the impact on the target and whether action is required; the planner, actionable volumes and dates; the technician, the equipment and the window. The cost of communicating well — tailoring the message to each audience — which always made doing it by hand unviable, is paid by the machine.

## Factories and absorbers

The inversion makes it possible to formulate the dichotomy that orders this book. Every communication infrastructure belongs to one of two species:

- **Interruption factories**: systems whose model is to expose you to a flow and leave you the work of filtering. Their natural metric is *engagement* — how many times they recapture you. The corporate channel is a factory by design; the AI assistant *inside* the channel is the same factory with a copilot inside.
- **Interruption absorbers**: systems that intercept the flow and deliver only what justifies attention. Their natural metric is the opposite — how many hours they kept anyone from touching you.

These are not degrees of the same thing: they are opposite directions. One species generates interruptions; the other consumes them. And the choice between them is not technological but a matter of design: with the same AI models you can build a copilot that helps you scroll faster — or an agent that makes scrolling not exist.

<!-- FIG:f02-fabricas-absorbedores -->
![Two species of communication infrastructure](figuras/f02-fabricas-absorbedores.png)

> **The essentials**
>
> - Postchat inverts the direction of the flow: communication comes to you, governed; silence becomes a guarantee, not a threat.
> - Of the seven variables of communication, the user retains three: intention, deep-dive, and decision.
> - Reformulation per recipient — impossible by hand — is the standard: everyone receives their version of the fact.
> - There are two species of infrastructure: interruption factories and absorbers. The channel is the first; Postchat, the second.
