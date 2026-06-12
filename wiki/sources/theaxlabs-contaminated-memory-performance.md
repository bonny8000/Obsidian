---
type: source
status: active
created: 2026-06-12
tags: [source, ai-agent, memory, evals, contamination, agent-operations]
sources:
  - raw/web/theaxlabs-contaminated-memory-performance-2026-06-12
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.86
---

# AX LABS: Contaminated Memory Eats Away Performance

## Citation

AX LABS. "Contaminated Memory Eats Away Performance." AX LABS Blog, 2026-06-08.

URL: https://theaxlabs.com/blog/%EC%98%A4%EC%97%BC%EB%90%9C-%EA%B8%B0%EC%96%B5%EC%9D%80-%EC%84%B1%EA%B3%BC%EB%A5%BC-%EA%B0%89%EC%95%84%EB%A8%B9%EB%8A%94%EB%8B%A4

Raw source card: `raw/web/theaxlabs-contaminated-memory-performance-2026-06-12.md`

## Summary

This Korean AX LABS article argues that agent memory quality is not only a retrieval problem. In production, memory can become contaminated when wrong summaries, stale exceptions, or the agent's own inferred patterns are promoted into long-term memory and later reused as facts.

The operational recommendation is to evaluate memory as a lifecycle: search, context injection, use in answers or tool calls, and post-run update or deletion. The source is useful for building agent memory evals, debugging traces, and knowledge-base governance rules.

## Key Claims

- Memory quality should be judged by contamination resistance, not just recall or retrieval rate.
- A correct final answer can still hide bad memory routing if the agent retrieved or injected the wrong memory.
- Memory contamination often starts during the write stage when transient reasoning becomes durable memory.
- Write gates should distinguish user statements, system records, and agent inference.
- Promotion criteria should distinguish one-off facts from repeated operational rules.
- Conflict handling should record whether new memory replaces, coexists with, or invalidates old memory.
- Memory drift can hide behind average scores, so replay tests need contamination probes, temporal-order tests, and canary memories.
- Trace, tool-call, state, and memory-update logs are necessary to debug agent memory failures.

## Useful Examples

- Replay an agent with empty memory and real memory, then compare behavior.
- Inject a known contaminated memory and inspect whether behavior changes.
- Reorder old and new memories to see whether stale context overrides newer instruction.
- Add canary memories to detect unauthorized or out-of-scope recall.

## Constraints / Caveats

- The article is a practitioner methodology piece from AX LABS, not an independent benchmark.
- It cites MemoryAgentBench, NIST CAISI, AgentRx, OpenAI trace grading, LangChain deep-agent evals, and Microsoft Foundry memory, but this source page does not independently validate those references.
- The article is in Korean; this wiki note uses an English working summary and should be checked against the raw source card for exact wording.

## Design Implications

- Treat memory writes as governed events, not passive notes.
- Add source labels to memory items: user statement, system record, agent inference, or derived rule.
- Add promotion and expiration rules before memory becomes long-term context.
- Build evals around traces and memory lifecycle transitions, not only final-answer grading.
- For this Obsidian LLM-Wiki, avoid letting chat summaries become durable wiki claims unless they are linked to source records.

## Tensions

- Memory improves personalization, but ungoverned memory can become a hidden source of false authority.
- More retrieval can lower quality if the extra context is stale, conflicting, or over-injected.
- Agent-generated summaries are useful compression artifacts, but risky when promoted as source truth.

## Open Questions

- What fields should this vault use to distinguish source-grounded memory from inference?
- Should future agent memory pages include `promotion_criteria`, `expiry`, and `conflict_policy` fields?
- Can this wiki's source readiness model double as a memory contamination control?

## Concepts Linked

- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/memory-contamination|Memory Contamination]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]

## LLM Use

- **Use for:** designing memory evals, trace review, memory write gates, and durable-knowledge governance.
- **Do not use for:** quantitative claims about memory benchmark performance without checking the cited benchmark papers.
- **Best prompt pattern:** Ask the LLM to map an agent failure across retrieval, context injection, action, and memory update, then identify where contamination could have entered.

## Reliability Notes

- Practitioner source with useful operational framing and citations to adjacent eval work.
- `coverage: substantial` because the article was captured and summarized, but cited references were not separately ingested in this pass.

## Backfill Status

- Created directly in LLM-ready format on 2026-06-12.
- This is a new source page, not a retrofit of an older note.
