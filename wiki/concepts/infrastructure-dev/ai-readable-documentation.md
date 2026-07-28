---
type: concept
status: active
created: 2026-07-27
updated: 2026-07-28
tags: [ai, documentation, retrieval, ux-writing]
sources:
  - sources/ux-writing-bot-follow-up
  - sources/veronikapj-whats-new-android-2026
  - sources/socar-parking-brain-knowledge-graph
confidence: 0.80
---

# AI-Readable Documentation

## Summary

AI-readable documentation is reference material designed for reliable retrieval and application by an AI system, not only for human comprehension.

## Why It Matters

An elegant document can still be skipped when rules, examples, exceptions, and scope are hard to locate or distinguish.

## Key Claims

- Structure and retrieval cues are part of documentation quality.
- Machine-usable boundaries should be explicit.
- Documentation needs operational tests, not only editorial review.
- **A platform now enforces this.** In Android's **App Functions**, a method annotated `@AppFunction` becomes an agent-callable tool and its **KDoc comment is the agent-readable description** — the text an agent reads to decide whether and how to invoke the capability. Doc quality becomes runtime behavior, and doc review becomes interface review ([[wiki/sources/veronikapj-whats-new-android-2026|Android 2026]], preview-stage, secondary source).
- **Volume is not the goal; authority and recency are.** [[wiki/sources/socar-parking-brain-knowledge-graph|SOCAR]] found ~50% of wiki content irrelevant and that ingesting comprehensively *destroyed* credibility in the answers. Their non-developer interfaces surface `sourceRef` citations, recency timestamps, and explicit staleness warnings ("the related wiki doc is 3 months old and may differ from code"). [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] found the same failure from the other side: as documents accumulated, terms and as-of dates mixed and **which file was authoritative became ambiguous** — what was needed was judgment criteria, not more material.
- **Therefore: mark authority, date, and scope, or the document degrades the agent.** An unmarked stale document is worse than a missing one.

## Related Concepts

- [[concepts/infrastructure-dev/deterministic-ai-workflows|Deterministic AI Workflows]]
- [[concepts/infrastructure-dev/design-md|Design.md as Context Infrastructure]]
- [[wiki/concepts/agent-experience/agent-invocable-app-functions|Agent-Invocable App Functions]] — where doc comments become the tool contract.
- [[wiki/concepts/infrastructure-dev/domain-knowledge-graph|Domain Knowledge Graph]] — the on-demand, provenance-carrying counterpart to always-on documentation.
- [[wiki/concepts/ai-agents/context-rot|Context Rot]] — what unfiltered documentation volume causes.
- [[wiki/concepts/infrastructure-dev/claudemd-context|CLAUDE.md / AGENTS.md Context]]

## Sources

- [[sources/ux-writing-bot-follow-up|UX라이팅봇 후속편]]
- [[wiki/sources/veronikapj-whats-new-android-2026|배필주 (2026): What's New in Android 2026]] — KDoc as agent-readable tool description. Preview-stage, secondary reporting.
- [[wiki/sources/socar-parking-brain-knowledge-graph|SOCAR (2026): parking-brain]] — filtering, `sourceRef`, recency warnings, and the credibility cost of over-ingestion.

## Open Questions

- How can teams measure whether an AI actually retrieved and applied the intended rule?
- What is the minimum authority metadata a document needs — owner, as-of date, supersedes, scope?
- If doc comments become tool contracts, who reviews them, and against what standard?
