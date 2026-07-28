---
type: concept
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [concept, knowledge-graph, ontology, agent-context, context-engineering, mcp, neo4j, provenance]
sources: [socar-parking-brain-knowledge-graph]
confidence: 0.80
---

# Domain Knowledge Graph

> [!abstract] Summary
> A queryable graph of an organization's **concepts, rules, decisions, and code artifacts** — with edges recording relationships like *this rule implements this concept* or *this code stems from that policy decision* — built as a **derived mirror** of existing systems rather than a new place to write things down. Every node carries a `sourceRef` pointer back to the original artifact, so the graph is an indexed cache that can always be re-validated, never the authority.

> [!important] Why it Matters
> The failure it prevents is specific and expensive: an agent **reimplements something that already exists** because the existing thing has non-intuitive naming, no documentation, and the person who knew is unavailable. That is not a model defect — it is a context-provisioning defect, and no amount of prompting fixes it. A domain knowledge graph makes organizational truth *addressable*, so "query before implementing" becomes possible as a workflow step.

## 📝 Key Claims

- **Graph, because the questions are relational.** Real development questions are "which code is affected if this rule changes?" — edges, not rows. A document store answers the wrong shape of question.
- **Seeds by hand, growth by pipeline.** SOCAR's working split: **~100 human-defined seed nodes** (rules, vocabulary, decisions) plus **~17,000+ auto-populated nodes** from AST analysis and filtered scraping. Full LLM extraction was tried and abandoned — it produced excessive noise and false relations.
- **Derived, not maintained.** Hourly pipeline regeneration removes the synchronization lag that human-maintained documentation always accumulates. Nobody updates the graph; the graph re-reads the world.
- **`sourceRef` over duplication.** Because the graph mirrors rather than owns, every answer carries an evidence trail and can be re-checked against the original. Duplicated content would become a second source of truth that silently drifts.
- **Curation is a credibility precondition.** ~50% of wiki content was irrelevant; ingesting comprehensively *destroyed* trust in the answers. Content failing structural quality gates is discarded or routed to human review, not ingested.
- **Confidence-gated ingestion with a human queue.** LLM extractions are scored (e.g. 77% against an 85% minimum) and borderline items go to domain experts for accept/reject.
- **One interface for all consumers.** A single MCP tool serves developers, AI agents, and an ops bot — so the same evidence trail answers every questioner.
- **Advisory, not enforcing.** Confusable field pairs get historical incident context and agents receive warnings during review. A wrong node misleads; it does not block.
- **Transparency over polish for non-experts.** Answers show `sourceRef` citations, recency timestamps, and staleness warnings — "the related wiki doc is 3 months old and may differ from code."

## Adoption path

The source's advice, ordered by leverage rather than by build effort:

1. **Text seed file, half a day.** Not a graph yet — just written-down vocabulary, rules, and decisions.
2. **Seed the most recent AI failures first.** The duplicate implementations and misunderstandings you already had are the highest-value nodes.
3. **Add "query before implementing" to the workflow** — *before* building any collection automation. The habit is the intervention; the infrastructure is the amplifier.
4. **Then automate collection**, with filtering and confidence gates from the start.

## ⚖️ Conflicts & Caveats

> [!warning] Methodological conflict with the pre-ontology pipeline
> [[wiki/concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]]'s anchor source bootstraps a "pre-ontology" by **LLM-extracting concepts from meeting transcripts**. SOCAR **tried automated extraction and rejected it** as too noisy, reverting to human seeds. Two sources, same concept space, opposite methodological conclusions. Recorded, not merged — the difference may be input type (structured code vs. unstructured speech) rather than a genuine disagreement, but no source establishes that.

> [!warning] The seed layer is the least verifiable layer
> The ~100 hand-defined seeds are the graph's most authoritative nodes and its only nodes with **no external validator**. They are corrected reactively, when an implementation exposes an error. One wrong seed can systematically mislead every agent that queries it, and nothing in the design detects that proactively.

> [!warning] No measured benefit
> The anchor source reports a prevented duplicate implementation and qualitative improvement. There is **no before/after metric** — no reduction in duplicate work, no time saved, no answer-accuracy rate. The architecture is well evidenced; its efficacy is asserted.

> [!warning] Standing costs
> Hourly regeneration over 17,000+ nodes, a human approval queue, and Neo4j operation are all recurring. Like every constraint architecture in this cluster, it trades maintenance burden for reliability, and the break-even volume is unstated.

## 🔗 Related Concepts

- [[wiki/concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]] — the broader idea this instantiates at engineering grade, and the source of the methodological conflict above.
- [[wiki/concepts/infrastructure-dev/palantir-foundry-ontology|Palantir Foundry Ontology]] — the enterprise-platform cousin (objects + links + actions).
- [[wiki/concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]] — modeling entities and relationships as a graph.
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]] — the graph is a context-provisioning mechanism, queried on demand rather than pre-loaded.
- [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]] — the delivery interface.
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]] — the always-on counterpart to on-demand graph queries.
- [[wiki/concepts/infrastructure-dev/llm-wiki|LLM Wiki]] / [[wiki/concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] — the same instinct in prose form; this vault is one.
- [[wiki/concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]] — the quality-gate discipline the ingestion filter implements.
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]] — the human queue for borderline extractions.
- [[wiki/concepts/ai-agents/context-rot|Context Rot]] — why ingesting everything degrades rather than improves answers.

## 📚 Sources

- [[wiki/sources/socar-parking-brain-knowledge-graph|SOCAR (2026): Stopping AI From Rebuilding What Already Exists — parking-brain]] — primary source: architecture, node counts, three abandoned approaches, adoption path.

## ❓ Open Questions

- What is the graph's answer-accuracy rate, and how often does a `sourceRef`-cited answer mislead because it is stale?
- When the pipeline ingests two conflicting values for the same policy, who arbitrates — the confidence score or a human?
- Who owns seed correctness over time, and what would detect a wrong seed *before* an implementation fails?
- Does the pre-implementation query step survive schedule pressure, or is it the first thing dropped?
- Is the extraction disagreement with the pre-ontology approach about input type (code vs. speech), or about LLM extraction as such?
