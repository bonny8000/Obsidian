---
type: concept
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [organizational-ontology, ontology, pre-ontology, ax, agent-context, knowledge-base, digital-twin]
sources:
  - sources/yozm-tiro-ax-ontology
confidence: 0.72
---

# Organizational Ontology

## Summary

An **organizational ontology** is a shared, formalized model of an organization's concepts, rules, and triggered actions — a "digital twin of the organization" that enforces **"same word, same meaning"** across teams. The Plato's CTO frames it as three layers: **data** (concepts, names, stakeholders), **logic** (rules — e.g. what "empty warehouse" means to each department), and **action** (what to do when a condition fires). It is the context substrate that lets AI agents make organization-aligned decisions.

## Why It Matters

Agent decision quality "hinges on what context and knowledge it carries into decision-making." Code and databases preserve *state* but not the *rationale, exceptions, and human judgment* behind decisions — that lives in discourse (meetings). An organizational ontology captures that shared meaning so agents reason like the org, not like a generic model: the same usage-decline signal becomes "upsell" to a naive agent but "offer compliance support during their security audit" to a context-aware one.

## Key Claims

- **Three layers: data + logic + action.** Concepts and entities (data), the rules that interpret them (logic), and the responses they trigger (action) together form an organizational digital twin.
- **Ontology = consensus.** Its core job is agreement that a word means the same thing org-wide — the precondition for agents (and people) not talking past each other.
- **Bootstrap via a pre-ontology.** A **pre-ontology** is unvalidated concept + relationship + source-citation candidates extracted from meeting records — drafting material *before* formal definition. It exists because "leaders mandated to define concepts often lack frontline context."
- **Meeting-records pipeline.** Transcribe → extract concepts → de-duplicate aliases → map relationships → generate a four-layer page (name+aliases / definition / source citation / related) → continuously refresh. (This is Karpathy's "LLM Wiki" applied to an organization.)
- **Gating rules.** Agents validate proposed actions against a central rule repository derived from the ontology before executing.

## Related Concepts

- [[concepts/infrastructure-dev/palantir-foundry-ontology|Palantir Foundry Ontology]] — the enterprise data-platform cousin of this idea (objects + links + actions).
- [[concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]] — modeling entities and relationships as a graph.
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] / [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] — the meeting-records→wiki mechanism that produces the pre-ontology.
- [[concepts/ai-agents/agent-digital-twin|Agent Digital Twin]] — agents that consume this ontology to act per-person.
- [[concepts/ai-agents/agent-memory|Agent Memory]] — durable, structured context an agent reasons over.
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]] — earlier ontology adoption compounds into a widening moat.

## Conflicts & Caveats

> [!warning] Branded content / single case
> The anchor source is Yozm × The Plato branded content (a vendor CTO interview); the "10 people / 300k users / 95% AI-authored code" framing and Tiro's accuracy claims are vendor-reported and unverified. The pre-ontology→ontology pipeline is a credible *pattern*; its efficacy at scale is not independently demonstrated here.

## Sources

- [[sources/yozm-tiro-ax-ontology|Yozm × The Plato (2026): Ontology Essential for AX — Starting with Meeting Records (feat. Tiro)]]

## Open Questions

- Who owns ratifying a pre-ontology into the formal ontology, and how are conflicting departmental definitions resolved?
- How is ontology drift handled as the organization and its language change?
- What stops a wrong/ambiguous ontology entry from systematically steering many agents wrong at once?
