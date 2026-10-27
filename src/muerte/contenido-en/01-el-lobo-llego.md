# 1. The Wolf Has Arrived

For years, the phrase "software is eating the world" described well what was happening. Every process in a company ended up inside an application: a package licensed and installed on its servers, a custom development or, in the last decade, a service rented in a vendor's cloud, per user and per month. Software as a service was the most recent form of that arrangement, not the only one: in all of them, the business stayed within what had been decided, once, that it could do.

The arrangement rested on two premises nobody questioned because they were true. Writing software cost so much, and went wrong so often, that it was better for someone specialized to do it once and for many to use it: hence the package and the rented service. And changing what had been built cost almost as much as building it, so it was better to describe the business once and not touch it until the next project: hence custom development as well. Both lasted as long as writing code was scarce human work.

This chapter tells how that arrangement broke. It begins with the signal the market gave in February 2026, goes on to what happened to me, which is the same story in miniature, listens to those who hold that nothing dies, takes from Satya Nadella the map of the crossing we are making, and ends by saying precisely what dies and what does not, because everything that follows depends on that precision.

## What happened in February 2026?

In the first week of February, software stocks suffered a sell-off that the financial press christened the *SaaSpocalypse*. On February 11, seven Forrester analysts published an article whose title I recognize as a relative of this book, *SaaS as we know it is dead*. According to them, in seven days over a trillion dollars in market capitalization had been erased from the sector.[^forrester]

Forrester listed four fears behind the sell-off. That software vendors would not be the ones chosen by AI agents. That per-seat pricing would become obsolete. That the ease of coding with AI would let any new company replicate the features of a complex platform. And that the products were already too complex, with hundreds of applications that do not talk to each other.

The article is worth more for what it separates than for the figure. Forrester does not say all software dies. It says horizontal and point-solution vendors will be challenged, that those specialized in a domain have a greater chance of survival, and that "the brain of the enterprise remains" while its central nervous system evolves. And it recommends, before buying artificial intelligence, putting the core in order: a governed and unified data fabric.

## What changed for me?

I have been programming since 1980, and I started with Basic. In August 2025 I began using Claude Code. By November I was already programming in formation with the agent who today signs as Simón Alero, in what I call *wingcoding*, and I never went back: my IntelliJ IDEA subscription was active until November 8, 2025, and that is the date I set for myself. After forty-five years of programming, I had reached a conclusion I never thought I would write: I no longer needed to keep doing it. The quality of the code artificial intelligence wrote was better than mine, and as for speed, no contest. As a programmer, of course; not as an architect. Since then I have been an architect, and Simón is my programming wingman. The paradox is that today I program more than ever in my life: I stopped writing the code, not building things. I have been able to bring all my projects to life, and the most important of them is [Soveria](https://soveria.ai/?ref=libro-muerte-del-software-en).

What I found hardest to let go of was the architecture of object-oriented design. What I saw when I stopped programming was the methodology. Today, in a day with Simón, I specify what is to be built as a black box, adding architecture guidelines. I watch the progress. I attend to the doubts or questions Simón has. I make the decisions that, as he and I agreed, fall within the domain that depends on my word. I monitor his chain of reasoning and the actions he executes, and I interrupt him to suggest better or corrective actions. I ask a lot, and I suggest to him the learning mechanisms of the harness he works in.

In April 2026, with my partner Vitor Enes, we declared Wingworking the official practice of ultraBASE. I was then building Cibeles, a parental-protection project that relies on an intelligent agent: the agent watches over the child and protects them from digital risks, such as *grooming*, without violating their privacy, because the parents do not learn of their conversations unless the child is at risk.

At that same table were the two ways of understanding that an agent builds a system, which chapter 3 calls the two readings. I had been programming Cibeles alone, and in the two months before the definitive change I leaned more and more on Claude Code, until the change was complete: that is the agentic reading, the agent that writes the code while I decide what gets built. And Cibeles, once built, is of the other species: an agent that does not write software but does a job, caring, without each case being specified in advance. Cibeles is a product for families, not a company's system, but the agent inside it is of the species this book is about.

In 1980 I loved programming chat simulations with intelligent agents. Today I talk with one every day, and he is the one who programs.

I tell this because the thesis of this book was born at that work table before it was born in a market figure: I saw the two premises of the arrangement, the cost of writing and the cost of changing, fall in my own practice. But an experience is not an argument, and the February figure drew contrary readings that are worth hearing before going on.

## Who says no?

The opposite thesis has serious arguments. One day before Forrester, *Fortune*'s AI editor argued that agents are not eating software as a service: they are using it.[^fortune] In his reading, it is very unlikely that large companies will want to build their own CRM or their own HR system, because maintaining them would take scarce engineers away. Vendors, for their part, claim they already own the data the agents need; they may be right, he writes, but they will have to prove it.

The case most often cited as proof of the death of software as a service shows its nuances best. Klarna left Salesforce, and the headlines said artificial intelligence had replaced it. In March 2025, its chief executive corrected that: they did not replace the software with a language model, because keeping customer data in a model would have limitations. They took the data out of their many systems and gathered it in a database of their own. And he added that he did not believe it was the end of Salesforce, but perhaps the opposite.[^klarna]

I read the three and see that they agree more than they argue. Nobody is going to rewrite half a century of enterprise software from scratch, and on that Fortune is right. What was valuable to Klarna was the data and control over it. Forrester sees the core surviving. All three agree that software does not disappear. What I add, and it is my reading, not theirs, is that it stops being as we know it.

It is worth noting what these cases prove. They are signals from the market for rented services, because that is what all three are about: per-seat pricing, CRM and HR, Salesforce. They are not the definition of what dies. Licensed software operated in-house and custom development appear in none of them, and what follows in the book does not rest on these cases.

## What did Nadella say?

To say precisely what dies I need a map of the crossing we are making, and I take it from where I drew it. In *AgencyDomains*, the fourth book of this trilogy and the first I wrote, I started from a remark by Satya Nadella in December 2024 that divides two worlds: that of those who open applications to work and that of those who work with agents. There I argued that, in the first stretch of that crossing, software survives and what dies is the interface: the application stops being the work surface and becomes infrastructure that agents consult.

Nadella described two phases. In the first, the business logic migrates to the agent layer, where agents operate on the repositories without distinguishing which system is underneath. In the second, with the logic already in that layer, people start replacing the systems underneath.[^nadella] This book is about the second phase.

*AgencyDomains* calls the idea of discarding all existing infrastructure "agentive fundamentalism", and holds that the stable state of the crossing is hybrid. I still think so. What dies in the second phase I define below. The system of record survives, with a new demand that is the subject of chapter 5. Technical coexistence remains the rule. What changes is who decides about what coexists.

## What dies, then?

With Nadella's map and the contrary readings in view, I can say it precisely, and it is the definition the rest of the book rests on.

A way of automating. **What dies is the business frozen in a piece of software: described once, and changed only when someone opens a project.** It makes no difference how it is held: rented as a service, licensed and operated on one's own infrastructure or in one's own cloud, or custom-built. With the rented service the vendor improves its product every week, but what the customer described of its business does not change without a project.

What does not die is the core that must always do the same thing, like the one that rates and bills: that one stays, as a system of truth, and what dies is that around it the whole business stays frozen. That custom development dies along with the rest is my thesis, and chapter 7 says what would refute it. In its place, I hold, something else will come, which I define next.

Let me fix two verbs here for the rest of the book. "Buying" means having software that someone described and froze, whether I rent it or license it. "Building" does not mean commissioning or programming a custom development: that one stays on the side of what dies, because the business stays just as frozen, even if the specification is mine. "Building", in this book, means that the business has a system that its agents shape and change as the work arrives, without anyone opening a project.

What can be automated changes too. Every system automates what someone specified, and around every system there is work nobody specified, which people resolve by hand. In telecommunications companies, for example, TM Forum describes orders that fall out along the way and exception queues that fill up as complexity grows.[^fallout] An agent can help with that work without each case being specified in advance. Software as we know it could not.

My judgment is that the direction has no way back, because it depends on a cost and not on a fashion: writing and changing software costs far less today than two years ago. Operating it with agents is a different calculation, and it may turn out more expensive than expected; I return to that in chapters 3 and 7.

With this, the questions the rest of the book answers are on the table. If the frozen business dies, what takes its place is the subject of chapter 3, and what is lost by leaving it, that of chapter 4. Before that, a second death has to be told, because the arrangement had one more premise, not of cost but of advantage: that having built a piece of software protected whoever sold it. Eight months after the February sell-off, the market received another signal, and this time it did not come from the stock exchange but from an open-source repository.

[^forrester]: Kate Leggett et al., *SaaS As We Know It Is Dead: How To Survive The SaaS-pocalypse!*, Forrester, February 11, 2026. <https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/>
[^fortune]: Jeremy Kahn, "AI agents from Anthropic and OpenAI aren't killing SaaS—but incumbent software players can't sleep easy", *Fortune*, February 10, 2026. Author's paraphrase. <https://fortune.com/2026/02/10/ai-agents-anthropic-openai-arent-killing-saas-salesforce-servicenow-microsoft-workday-cant-sleep-easy/>
[^klarna]: Julie Bort, "Klarna CEO doubts that other companies will replace Salesforce with AI", *TechCrunch*, March 4, 2025. Statements by Sebastian Siemiatkowski. <https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai>
[^nadella]: Satya Nadella, interview on the *BG2* podcast, December 2024, quoted and analyzed in César Obach-Renner, *AgencyDomains: Architecture of the Agentive World*, chapter 1, "The Nadella Line".
[^fallout]: TM Forum, *How order management is evolving to embrace agentic AI*, 2026, pp. 2-3. Report sponsored by Amdocs.
