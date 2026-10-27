# 2. Everything Can Be Copied

In the first week of October 2026, an open-source project called *Reverse Engineer Anything*, REA, became the fastest-growing repository I can remember. It had fewer than ten thousand stars on GitHub on October 6 and more than a hundred thousand on the 12th.[^hackernoon] Two weeks later it passed three hundred and forty thousand.[^404]

REA connects coding agents, such as Claude Code or Codex, to the professional reverse-engineering tools that specialists have used for decades to understand a program whose source code they do not have. Its documentation is cautious: it says it does not recover the original code, does not clone applications automatically and does not ship a decompiler of its own.[^hackernoon] What it does is enough to unsettle any software vendor. It puts within reach of any agent the ability to look inside a finished program and describe what it does. How it introduced itself says it all: if you see a feature in an application that you want in your product, ask your agent to investigate it with REA.[^404]

## What does it mean that it can be copied?

For decades, a software vendor's advantage had two parts: what its product did and how hard it was to reproduce. The first could be seen on the screens. The second protected the business, because rebuilding a CRM cost years and teams that almost no company had.

The difficulty did not disappear. The HackerNoon article that best tells the story offers a concrete example: ArtCraft's Photoshop clone, from a project that publishes agent-made clones of well-known applications, got only five of thirty filter tests right against the original, and an artist declared it useless. Its author concludes that today a clone that opens, edits and exports can appear in days, and that a clone you would trust your livelihood to is not there yet. What is over, she says, is the idea that having built the screens is a lasting advantage.[^hackernoon]

I had seen it on a small scale before REA. In the projects I lead we rebuilt, more than once, a report from a commercial tool by looking at what it showed, with no access to how it was made, and we had it running in days on the client's governed data. My friend, the one with the wealth-management system, did something bigger: the client who asked him for the system had seen the platform a law firm was offering, and my friend replied that this could be built with artificial intelligence and that, besides, it would be the client's own. REA made visible to everyone what could already be done.

This argument holds for a vendor's software, whatever the form in which it is held. Custom development belongs to the client itself and is weakened by another route, the cost of changing it, which is the one in chapter 1.

## Is copying legitimate?

It depends on the country, the method, the licenses and what is copied. The same HackerNoon article sums it up for whoever wants to look closely. In the European Union, reverse engineering a purchased product is permitted under trade-secret law, but decompiling is admitted only for interoperability purposes. In the United States there are rulings in favor of fair use, and nobody yet knows whether a model trained on public code counts as "clean". ArtCraft expressly forbids the agent from reading or decompiling the original code and limits it to studying the behavior, the public format specifications and the appearance, which is the classic clean-room method. And vendors are already changing their contracts to prohibit AI-assisted reverse engineering.[^hackernoon] One journalist put it more harshly: the plagiarism machine used to plagiarize.[^404]

My position is simpler than the debate. Reproducing what a program does in order to understand it, or to build one's own on one's own data, is what the software industry has always done. Copying someone else's code or assets is not. The boundary stays in the same place. What is new is that anyone can reach it.

When what I want to replace is a rented service, I do not have its code: I have what the service shows me, my data, my screens, my reports. In the European Union and in the United States, looking at that to understand what it does infringes no copyright, because what a system does has no owner. But the rental contract can prohibit using that access to build a substitute, and Salesforce's does: before starting, one has to read it.[^saas]

## And what does not get copied?

Let us suppose the legal side settled, and go back to what copying brings into view. If an application's features can be reproduced, whoever sells software is left with less than they thought. And whoever stops buying it and reproduces it at home loses something worth naming.

They lose the track record. An application that has been running for ten years in thousands of companies brings something no agent can decompile: the accumulated evidence that it works, and a vendor that answers when it fails. The clone brings the screens and the flows, and starts its track record from zero, with a single organization answering for it.

For almost all features that makes no difference. If the clone of a task board fails, someone fixes it and nobody gets hurt. It matters in the records someone is accountable to others for: the invoice charged to a customer, the balance of an account, the signed contract and its terms, the consumption reported to the regulator, the wealth of a family that trusts whoever manages it. In those records, the question is whether what they say is true, and who vouches for it.

Reverse engineering does not answer that question. It makes it urgent, because the easier it is to build a system, the more home-built systems will hold records someone answers for, and the more people will wonder whether they can believe them.

## What is left of the two deaths?

So far, two deaths. That of chapter 1 is the death of the frozen business, and a cost killed it: writing and changing software stopped being expensive. That of this chapter is the death of the advantage of having built the screens, and a tool killed it: any agent can look inside an application and describe what it does. Neither kills all software, and in both the same thing survives: the track record, the evidence that something works, and someone who answers for the records one is accountable to others for.

Both leave the same question open, what an organization has once it no longer buys the software that froze its business and can no longer lean on the advantage of having built it, and the answer comes in two parts that are best read in order. First what is born, which is a new way of having a system. Then what is lost, which is what nobody wrote into the budget.

[^hackernoon]: Maria Mendonca, "Is Software Really Dead? The Rise of AI-Powered Reverse Engineering", *HackerNoon*, October 21, 2026. <https://hackernoon.com/is-software-really-dead-the-rise-of-ai-powered-reverse-engineering>
[^404]: Jason Koebler, "'Reverse-Engineer Anything' Is the New Wild West of AI", *404 Media*, October 20, 2026. <https://www.404media.co/reverse-engineer-anything-is-the-new-wild-west-of-ai/>
[^saas]: That a program's functionality, its programming language and its file formats are not protected by copyright was settled by the Court of Justice of the European Union in *SAS Institute v. World Programming* (C-406/10, 2012); in the United States, the statute excludes procedures and methods of operation from that protection (17 U.S.C. §102(b)). I have not verified the law of other countries, Chile included. The contract is another matter: Salesforce's terms prohibit accessing the service to build a competing product or to copy its features (Main Services Agreement, §3.4(j)). In the same dispute between SAS and World Programming, the United States Court of Appeals for the Fourth Circuit (874 F.3d 370, 2017) treated running the other party's program and adjusting one's own until its results matched as reverse engineering prohibited by the license, and the jury set US$ 26.4 million in contractual damages. That was a software license and a civil suit, not a rented service: it serves as an indication that a court can enforce such a clause, not that it would do so with that of a cloud service.
