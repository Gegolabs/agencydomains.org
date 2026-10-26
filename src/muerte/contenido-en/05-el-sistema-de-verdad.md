# 5. The System of Truth

A system of truth is a system of record that, besides keeping the official version of a piece of data, guarantees that what is recorded is true, through a contract with those who use it.

I use the word contract in its technical sense, the one it has in systems architecture: an agreement between parties that embodies a promise. No lawyer or notary is needed. What is needed is that the promise be written, that it can be verified and that someone answers for it.

## What does its contract promise?

Six properties.

**Nothing is deleted; it is corrected.** Every correction is a new record that leaves the previous one in view. It is the oldest rule in accounting, the one that requires correcting an entry with another entry, and it is the first to be lost when a system is built quickly on a database that allows overwriting.

**The origin is traceable.** Every record says who made it, when and with what evidence. If the one recording is an agent, it says which agent it was and on whose behalf it acted.

**It is verifiable by a third party.** An auditor can take any figure back to its origin without asking permission or explanations from whoever recorded it.

**It is reconcilable.** What is billed reconciles with what is contracted, and what is contracted with what is reported to the regulator. When it does not reconcile, the difference is in view and has an owner.

**It speaks a common language.** Its records follow a standard information model of the domain, so that all agents, and all people, understand the same thing by a customer, a product or a charge.

**It declares its degree of truth.** There are records someone declared, records that were verified against their source and records that were inferred, and the system says which is which. The notary certifies that someone declared something; the auditor certifies that a figure is true. A system of truth does both without confusing them.

## Which records does it cover?

Those the organization must keep and is accountable to others for. The financial ones: what was collected, what was paid, the balances, the adjustments. The commercial ones: the contracts, the orders, what was sold and the terms in force at each moment. The regulatory ones: what the law requires keeping and reporting. And the legal and documentary ones, with their content readable by an agent; not a PDF kept in a folder, but what it says, in a form an agent can consult and cite.

A task board, a meeting agenda or the draft of a presentation do not need it. The line is drawn by one question: does anyone outside the organization depend on this record being true?

## How do agents work with it?

They read from it and write to it only through its contract. An agent can propose a charge, record a payment or correct a piece of data, but it cannot delete, nor record without leaving its origin, nor declare as verified what it only inferred. Agents can change every day; the truth does not change without leaving a trace.

## Who answers for the truth?

The contract has two guarantors, and it is best not to merge them into one. The first is the technology vendor. The system of truth is always a piece of technology, and it is operated by whoever uses it, be it a small business or a telecommunications company: nobody operates someone else's truth. Whoever provides it answers for the piece meeting the six properties, as the maker of a scale answers for it weighing correctly.

The second guarantor is the one who attests. That the scale weighs correctly does not prove that nobody put a finger on it. For that, someone independent of whoever records is needed, to verify the records: the contract's third property. It can be a human auditor. It can be an automatic process that compares what is recorded with its sources and with other records. What it cannot be is the same organization that records, for the same reason a company does not audit itself even if it has the best accountants. And it should not be the technology vendor either: whoever sells the scale is not the best witness that nobody touched it. If the attestation is an automatic process, it is run by someone independent of both, with access to the record and to its sources.

If only the first guarantor exists, we are back to bought peace of mind: one has to trust the vendor. If only the second exists, the auditor reviews records that may have been overwritten. The contract needs both.

There is a serious objection. Does the system of truth not reinstall the dependency on a vendor that chapter 1 declared dead? In part yes, and it is deliberate. The dependency that dies is that on a platform that freezes the whole business. The one that remains is that on a bounded piece, with a written and verifiable promise. That it can be swapped for another that meets the same contract is a condition to be demanded, not a fact: today no standard for that contract exists, and the system speaking a common language is what makes it possible. "Answering", in that contract, means that the vendor assumes in writing the consequences of the piece failing to meet any of the six properties.

## How does it relate to what already exists in the architecture?

A system of truth is a system of record with a contract. *AgencyDomains* already says that the system of record is what survives the crossing, and it already specifies a good part of the mechanics the contract needs: the log that is only appended to and never edited or deleted, the agent's identity in every action, non-repudiation, human approval by threshold.[^agd] The system of truth adds the contract declared before those who use the record, the degree of truth of each entry and the second guarantor.

Three clarifications avoid misunderstandings. The first: an architecture can maintain the current state of each customer or each balance and, at the same time, a log of entries that are not deleted and from which that state can be reconstructed. *AgencyDomains* treats that log as an authoritative complement to the state. For the records one is accountable to others for, this book inverts the hierarchy and places the log of entries as the source of truth. It is a decision, and I take it knowingly. The second: the degree of truth is not a quality level and does not allow second-rate data; it states the status of each entry, and the required quality remains a single one. The third: that nothing is deleted does not authorize keeping forever what the law or the person asks to delete. The entry keeps the fingerprint and the metadata that prove something happened, and the personal content lives apart, with its own retention.

There is one piece the industry has not yet resolved: that an external auditor can verify the record without the system being opened to them. *AgencyDomains* leaves it declared as open work.[^frontera] Here I demand it, without saying it is resolved, and I ask that whoever provides a system of truth answer for it with the best available technology.

## Didn't something like this already exist?

The pieces existed separately. Double-entry bookkeeping is a system of truth without computers. Databases with an immutable log have been around for years. The distributed ledgers of the last decade promised something similar, and many confused immutability with truth: that something cannot be deleted does not mean it was true when it was written. And the billing cores of the big industries remain deterministic because nobody wants what a customer is charged to depend on a probability.

What is new is the need. As long as software was bought, peace of mind came with it. When every organization builds its system, it has to be asked for separately, and what is asked for is a system of truth with its contract and its two guarantors.

I have a close example that the pattern works outside finance, and I declare that it is from my own house. Soveria, the platform where the agents I write with work, records what those agents learn and decide under these rules: every fact declares whether it was measured, whether someone reported it or whether it is a conjecture, and in that case what would refute it; every decision keeps what was discarded and how it is reversed; nothing is deleted, it is amended. It applies several properties of the contract, but it does not yet have an independent second guarantor, so I do not call it a system of truth. The reader cannot verify it from here, and so I do not present it as proof, but as the place where I learned that the contract is practicable.

[^agd]: César Obach-Renner, *AgencyDomains: Architecture of the Agentive World*, chapter 3, "Bounded Concerns Architecture", and chapter 5, "Trust Infrastructure".
[^frontera]: César Obach-Renner, *AgencyDomains: Architecture of the Agentive World*, epilogue: the second item of open work, third-party verifiable audit without access to the system.
