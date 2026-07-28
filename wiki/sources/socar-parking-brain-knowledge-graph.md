---
type: source
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [agentic-engineering, ai-agent, knowledge-graph, ontology, mcp-integration, context-engineering, neo4j, human-in-the-loop, case-study]
source_path: raw/web/socar-parking-brain-knowledge-graph-2026-07-28.md
source_url: https://tech.socar.kr/dev/2026/07/27/parking-brain-1
authors: [Sebastian, Olivier]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.83
---

# SOCAR (2026): Stopping AI From Rebuilding What Already Exists — parking-brain

## Citation

Sebastian & Olivier, 「이미 있는 기능을 AI가 또 만들지 않도록 하기 — 지식 그래프 도입기」 *(Stopping AI from rebuilding existing features — a knowledge graph adoption story)*, **SOCAR Tech Blog**, 2026-07-27. Part 1 of a series.

**Source type:** First-party engineering adoption report with implementation numbers.
**Raw capture:** [[raw/web/socar-parking-brain-knowledge-graph-2026-07-28|socar-parking-brain-knowledge-graph-2026-07-28]]

## Summary

SOCAR's second contribution to this wiki, and a different failure mode from [[wiki/sources/socar-self-healing-agents|their self-healing agents post]]. There the problem was third-party drift; here it is **internal knowledge scatter**. An AI agent reimplemented an existing status-modification API and wasted half a day, because the API existed under non-intuitive naming, had no wiki page, and the person who knew was on leave.

Their answer, **parking-brain**, is a Neo4j knowledge graph of concepts, rules, decisions and code artifacts, populated hourly by AST analysis plus filtered scraping of issues/wikis/messaging, and queried over MCP by developers, agents, and an ops bot. The design commitment that makes it credible: the graph holds `sourceRef` pointers, never duplicated content — it is explicitly **an indexed cache, not the authoritative source**.

## Key Claims

- **The agent failure was an organizational failure.** Domain truth is scattered across code, issue trackers, wikis and messaging, with conflicting values for the same policy. The agent's duplicate implementation is a symptom of that, not a model defect.
- **Graph over documents, because the questions are relational.** Real development questions are "which code is affected if this rule changes?" — edges, not rows.
- **Full LLM extraction failed.** Autonomous concept and relationship extraction from documents produced excessive noise and false relations. The working design is **~100 human-defined seed nodes plus scored automated collection**.
- **Curation is a credibility precondition.** ~50% of wiki content was irrelevant; ingesting comprehensively "destroyed credibility." Content failing structural quality gates is discarded or routed to human review rather than ingested.
- **The graph must be derived, not maintained.** Pipeline regeneration every hour removes synchronization lag that human maintenance always accumulates.
- **`sourceRef` over duplication.** Because the graph mirrors rather than owns, every answer can be re-validated against the original artifact — and every answer carries an evidence trail.
- **Code can pass tests and still be wrong about meaning.** Confusion between similarly named fields `kindSeq` and `typeSeq` produced product-classification gaps that type checks and tests missed; only direct DB inspection caught it.
- **Query before implementing** is a mandatory workflow step, and the authors advise adding it *before* building any collection automation.

## Useful Examples

| Quantity | Value |
|---|---|
| Human-defined seed nodes (rules, vocabulary, decisions) | **~100** |
| Auto-populated nodes (static analysis + collection) | **~17,000+** |
| Collection interval | **1 hour** |
| Example confidence gate | 77% score against an **85% minimum** → human approval queue |
| Irrelevant share of wiki content | **~50%** |

- **Three components:** Neo4j graph storage · hourly collection pipeline (AST-based code analysis; filtered scraping of issues, wikis, messaging) · a single standardized **MCP** query tool serving developers, AI agents, and an ops bot alike.
- **Transparency over polish for non-developers:** interfaces show `sourceRef` citations, recency timestamps, and warnings such as "the related wiki doc is 3 months old and may differ from code."
- **Advice vs. enforcement:** confusable field pairs are tagged with historical incident context, and agents get explicit warnings during reviews — the graph advises, it does not block.
- **Develop-loop correction:** when an outdated graph answer surfaces during implementation, the correction upserts back into the node.
- **Graduated rollout:** developers → Slack ops bot → (pending) business, planning, CS, each gated on validated answer quality for high-frequency questions.
- **Adoption path advised:** start with a text seed file (half a day), seed the most recent AI failures first, add the pre-implementation query step, then automate collection.

## Constraints / Caveats

- **Seed nodes have no external validator.** ~100 hand-defined concepts are the graph's most authoritative layer and its least verifiable one, corrected only reactively when an implementation exposes an error.
- **No measured outcome.** The post reports a prevented duplicate implementation and qualitative benefit. There is **no before/after metric** — no reduction in duplicate work, no time saved, no answer-accuracy rate. This is the sharpest contrast with SOCAR's self-healing-agents post, which had numbers.
- **Synchronization is not guaranteed.** The graph is a derived cache; errors accumulate between cycles, bounded only by the 1-hour refresh.
- **Coverage is narrow by design** — domain meaning and decisions only. It does not replace code review for semantic correctness.
- **Part 1 of a series**, so the architecture is described ahead of results; later parts may revise claims.
- **Confidence gating depends on an LLM scoring LLM extractions.** The 77%/85% example shows the mechanism but not its calibration or false-negative rate.
- Ingested from an AI-generated extraction of a Korean post, not a verbatim read.

## Design Implications

- **Treat "the agent duplicated existing work" as a context-provisioning bug**, not a prompting problem. The fix is an addressable source of domain truth, not a longer prompt.
- **Seed by hand, grow by pipeline.** Human-authored seeds set vocabulary and authority; automation scales coverage. Neither alone worked.
- **Make the knowledge layer a mirror with pointers.** Anything that duplicates content becomes a second source of truth that drifts. `sourceRef` + timestamp + recency warning is the minimum honest interface.
- **Filter before ingesting, and say what you dropped.** Half the wiki being irrelevant means an unfiltered pipeline actively degrades trust.
- **Expose it through one interface (MCP) to all consumers** — humans, agents, bots — so the same evidence trail serves every questioner.
- **Put the query step in the workflow before building the infrastructure.** The habit is the intervention; the graph is the amplifier.
- **Design for advisory failure.** Because seeds can be wrong, the system warns and cites rather than blocking — an incorrect node misleads rather than halts.

## Tensions

- **Extends [[wiki/concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]] with an engineering-grade instance.** The prior anchor for that concept was vendor branded content; this is a first-party adoption report with node counts and named failure modes, so it materially strengthens the concept's evidence base.
- **Against the ontology concept's meeting-records pipeline:** the Plato/Tiro framing bootstraps a "pre-ontology" by LLM-extracting concepts from meeting transcripts. SOCAR **tried automated extraction and abandoned it** as too noisy. Direct methodological conflict between two sources on the same concept — recorded, not merged.
- **Against [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake's]] "judgment criteria, not document volume":** NStake found more documents degraded AI understanding; SOCAR's answer is that the problem is unstructured volume specifically, and a curated graph with authority markers is the fix. These are compatible but not identical — both agree raw document dumping fails.
- **Unresolved against its own sibling source.** SOCAR's [[wiki/sources/socar-self-healing-agents|self-healing agents]] post is production-grade with metrics; this one is architecture-grade without them. Same company, same period, very different evidence quality — do not treat SOCAR as uniformly strong.

## Open Questions

- What is the answer-accuracy rate of the graph, and how often is a `sourceRef`-cited answer stale enough to mislead?
- How are conflicting values for the same policy resolved when the graph ingests both — does the confidence score arbitrate, or does a human?
- Who owns seed-node correctness over time, and what stops one wrong seed from systematically misleading every agent that queries it?
- Does the pre-implementation query step survive contact with schedule pressure, or is it the first thing dropped?
- At 17,000 nodes with hourly regeneration, what is the cost — compute, review load on the approval queue, and Neo4j maintenance?

## Concepts Linked from This Source

- [[wiki/concepts/infrastructure-dev/domain-knowledge-graph|Domain Knowledge Graph]]
- [[wiki/concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]]
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]
- [[wiki/concepts/ai-agents/mcp-integration|MCP Integration]]
- [[wiki/concepts/infrastructure-dev/ai-readable-documentation|AI-Readable Documentation]]
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]
- [[wiki/concepts/infrastructure-dev/knowledge-linting|Knowledge Linting]]
- [[wiki/concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]]

## LLM Use

The reference case for **giving agents an addressable source of organizational domain truth**. Cite it for: the seeds-plus-pipeline hybrid, `sourceRef`-over-duplication, filtering as a credibility precondition, and the confidence-gate-plus-approval-queue pattern. It is also the concrete counter-example to "just let the LLM extract the ontology."

Do **not** cite it for efficacy — there are no outcome metrics. For that, pair with a source that measures duplicate-work reduction, which this wiki does not yet have.

## Reliability Notes

- **First-party engineering report with implementation specifics** (node counts, interval, threshold example, named failure modes) and honest reporting of three abandoned approaches.
- **Confidence 0.83:** the architecture and its failure modes are well evidenced; the *benefit* is asserted rather than measured, which caps it below the sibling SOCAR source's 0.88.
- Vendor-neutral — no product being sold, and the post names what did not work.
- Part 1 of a series; revisit when later parts publish, and update this page rather than adding a duplicate.
