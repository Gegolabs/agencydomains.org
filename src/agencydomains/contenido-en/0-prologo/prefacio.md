# Preface

*By César Obach-Renner · July 2026*

---

After eighteen months watching the industry build AI agents — some as a demo's whim, others as enterprise pilots that died on the way to production — I synthesized a formal architecture for the problem. I call it the **Agentive Architecture**. This book is its specification.

I came to the problem by the least elegant route: I needed it. In 2025 I began building, inside my company, a portfolio of products in which humans and agents had to coexist as first-class digital citizens. I soon discovered that the category did not exist with the maturity required to sustain that design. There was a great deal of loose language — *"agentic AI"*, *"AI copilots"*, *"AI agents"*, *"autonomous workflows"* —, much marketing and little architecture. The industry named the horizon; but there was no common specification of the technical substrate, nor a shared vocabulary to discuss it.

Faced with that, I had two paths: improvise over the scattered pieces, or build the frame my company needed. I chose the second. I built it first as internal notes; then as the project's canonical documents; then as the backbone of the entire portfolio. At some point it became evident that the result had value beyond my company — that any organization building toward this horizon faces the same problem and needs the same frame.

This book is the formalization of that frame. It defines the paradigm (**the Agentive World**), a formal four-layer architecture, the technical primitives that inhabit it (**Botlets**, **Capabilities**, **AgencyDomains**), a cross-cutting trust infrastructure (**Trust Infrastructure**), and a two-dimensional market model (**the AI value chain**). The purpose is not to convince the reader to adopt my particular implementation. The purpose is to offer the whole ecosystem a common language for reasoning about productive agentive systems.

I am clear about where I come from. Almost twenty years ago I wrote a similar book for another category that was then beginning to take shape — *SOAr: El concepto* (2008), a formalization of Service-Oriented Architecture for enterprise integration. That work, too, was born of a real project where the methodology did not exist, so I created it and documented it. What I learned then, and apply here, is that technical categories are established not when someone invents them, but when someone **writes them down with enough discipline that others adopt them**. This book is that attempt.

## Who should read this book?

This book is addressed to those who are building, evaluating, or governing productive agentive systems.

If you are a **systems architect** or a **CTO**, you will find a common frame for reasoning about separation of concerns, governance, technical primitives, and stack positioning on a three-to-five-year horizon. If you are a **product strategist** or a **consultant**, you will find a two-dimensional market map for situating any actor — your own or another's — in the AI value chain. If you are a **researcher** or an **academic**, you will find a reasonably rigorous formalization of a category still in consolidation.

The book is introductory in the sense that it assumes no prior knowledge of specific implementations. But it assumes basic familiarity with distributed systems, language models, and operating systems in production. It is not an implementation manual — it is the specification a manual ought to respect.

## How is this book organized?

The book advances from the paradigm to the implementation, in a sequence where each part rests on the previous one:

- **The paradigm** — The Nadella Line (the question) · The Agentive World (the consequences).
- **The Agentive Architecture** — four distinct layers · cross-cutting Trust Infrastructure · Agent First (the governing principle).
- **The primitives (seven)** — AgencyDomain · Botlet · proto-Botlet (+ manifestation + temporality) · Capability (cognitive, Layer 2) · Trust Infrastructure · Assistant vs Autonomous Agent (axis primitive) · Facet (Layer 1).
- **The market positioning** — The AI value chain (11 × 4) · Observability · the Carbon World.
- **The applications** — Real-time knowledge (the canonical case: Varnished Kimball · conversational BI).
- **The operation** — Trust Infrastructure operationalized (policies · CRUDLEX · log).
- **The reference implementation** — Vergis (Chapter 9).
- **The epilogue** — the evolution frontier (non-LLM cognition · federation · the Carbon World · AgentNation).

The path chains the chapters like this: **The Nadella Line** (the question) → **The Agentive World** (the consequences) → **the Agentive Architecture** (the four layers) → **the primitives** that populate them → **the market positioning** → **the canonical application** → **the operation** → **Vergis**, the reference implementation → **the epilogue**. The glossary at the end fixes the canonical vocabulary.

## A note on terminology

Much of this category's technical vocabulary is native to English and lacks Spanish translations that are at once precise and recognized: *agent*, *agentic*, *agentive*, *runtime*, *guardrails*, *tool*, *prompt injection*, among others. This book was first written in Spanish, where it adopted the English originals whenever a translation would be forced or the term already circulated with authority in the field. In this English edition that tension largely dissolves; what remains is the discipline of a fixed vocabulary.

The canonical concepts coined in this book — **Agentive Architecture**, **Nadella Line**, **AgencyDomains**, **Botlet**, **Capability**, **Trust Infrastructure**, **Agentive World** — are kept in their original form throughout the work, capitalized, as proper names. Their precise definitions live in the glossary at the end of the book.

As the category matures across languages and communities, consensus terminology may emerge. If it does, future editions will gather it. For now, the priority is not to break the traceability of a concept across the communities that use it.
