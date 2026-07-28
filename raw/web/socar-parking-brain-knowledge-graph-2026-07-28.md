---
source_url: https://tech.socar.kr/dev/2026/07/27/parking-brain-1
captured: 2026-07-28
title: "이미 있는 기능을 AI가 또 만들지 않도록 하기 — 지식 그래프 도입기"
authors: [Sebastian, Olivier]
published: 2026-07-27
publisher: SOCAR Tech Blog
language: ko
series: parking-brain (part 1)
---

# Stopping AI From Rebuilding What Already Exists — A Knowledge Graph Adoption Story (SOCAR)

**Original title (ko):** 「이미 있는 기능을 AI가 또 만들지 않도록 하기 — 지식 그래프 도입기」
**Published:** 2026-07-27 · **Captured:** 2026-07-28
**Capture note:** AI-written summary of a Korean-language engineering post. Full text not reproduced. Part 1 of a series.

## Summary

SOCAR's development team, using AI agents for a significant share of their work, kept hitting **domain-knowledge failures**. The triggering example: an agent **reimplemented an existing status-modification API**, wasting half a day, because the API existed in code under non-intuitive naming, had no wiki page, and the person who knew was away. Root cause: organizational domain truth is scattered across code, issue trackers, wikis and messaging, with conflicting values for the same policy. Their answer is **parking-brain**, a knowledge graph that agents and humans query before implementing.

## Architecture — three components

1. **Knowledge graph storage (Neo4j).** Nodes = concepts, rules, decisions, code artifacts. Edges = relationships such as "this rule implements this concept" or "this code stems from that policy decision."
2. **Automated collection pipeline (hourly).**
   - Code: AST-based static analysis extracting services, endpoints, entities.
   - Issues / wikis / messaging: periodic scraping with multi-stage filtering.
3. **Query interface over MCP.** One standardized tool for developers, AI agents, and operational bots. Chat-based natural-language queries returning **evidence trails**, with `sourceRef` pointers back to the original artifacts.

## Key decisions and rationale

| Decision | Rationale |
|---|---|
| Graph over document store | Real development questions are relational ("which code is affected if this rule changes?"), not tabular |
| Pipeline-driven updates, not human-maintained | Removes synchronization lag; parsers regenerate automatically each hour |
| `sourceRef` references instead of duplication | The graph is an indexed cache/mirror, **not** the authoritative source; enables re-validation against originals |
| Human-defined seeds + automated collection | Full LLM extraction produced excessive noise and false relations; hybrid (structured seed + scoring gate) worked better |
| Filter before ingestion | ~50% of wiki content was irrelevant; structured filters + confidence scoring + human approval gates removed noise |

## Concrete numbers

- **~100** manually defined seed nodes (rules, vocabulary, decisions).
- **~17,000+** auto-populated nodes from static analysis and periodic collection.
- **1-hour** collection interval.
- Message filtering by **LLM confidence score** (e.g. a 77% score against an 85% minimum) with a **human approval queue** for borderline extractions.
- Slack messages and wiki pages failing structural quality gates are **discarded or routed for human review**, not ingested.

## Mistakes corrected during adoption

1. **Over-ingestion.** The initial instinct was comprehensive collection; inclusion without curation destroyed credibility.
2. **Full LLM extraction failed.** Autonomous concept/relationship extraction from documents produced unreliable false relations; reverted to human seeds plus selective automation.
3. **Code–meaning gap.** Code can pass type checks and tests while failing domain meaning — e.g. confusion between similarly named fields `kindSeq` and `typeSeq` produced product-classification gaps detected only by direct DB inspection.

## Limitations and caveats

- **Seed nodes remain vulnerable** — manually defined concepts have no external source to validate against. Mitigated by a "develop loop" correction: errors found during implementation update nodes in place (upsert).
- **Synchronization is not guaranteed** — the graph is a derived cache; errors can accumulate between collection cycles, bounded by the 1-hour refresh.
- **Incomplete domain coverage** — the graph addresses domain meaning and decisions only; it cannot replace code review for semantic correctness.

## Human-in-the-loop design

- **Approval gates:** confidence-scored extractions below threshold route to domain experts for accept/reject.
- **Error-driven learning:** when an outdated graph answer is discovered during implementation, the correction feeds back into the node.
- **Pre-implementation query** is a mandatory workflow step before coding begins.
- **Operational Slack bot** auto-queries the graph for first-pass answers, flagging items needing manual verification and showing evidence trails.

## Safety and transparency safeguards

- **Transparency over polish.** Non-developer interfaces emphasize `sourceRef` citation, recency timestamps, and warnings — e.g. "the related wiki doc is 3 months old and may differ from code."
- **Graduated expansion.** New user groups are served only after answer quality is validated on high-frequency questions. Extension from developers to an ops bot is done; business, planning, and CS roles are pending trust-building.
- **Advice vs. enforcement.** Confusable field pairs are tagged with historical incident context, and AI agents receive explicit warnings during reviews.

## Recommended adoption path (authors' advice)

Start with a text-based seed file (half a day of effort). Seed the most recent AI failures first. Integrate a "query before implementing" step into the workflow *before* building collection automation. Correct discovered errors in place rather than rebuilding.
