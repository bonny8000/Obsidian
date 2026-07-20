---
type: source
status: active
created: 2026-05-20
tags: [gemini, agentic-ai, enterprise-ai]
sources: [https://blog.google/intl/ko-kr/company-news/technology/gemini-3-5-kr/]
updated: 2026-06-12
ingest_level: standard
coverage: partial
llm_ready: false
raw_preserved: false
confidence: 1.0
---

# Source: Introducing Gemini 3.5: Cutting-Edge Intelligence with Action

## Citation

Google Korea. (2026). *[I/O 2026] 黖疏???貲?謔科??木? ?欠??伉?鴔 穈? ??諯賈???3.5?未 ???拘???(Introducing Gemini 3.5: Combining Cutting-Edge Intelligence with Action)*.

## Source Type

Company News / Official Blog

## Location

[URL](https://blog.google/intl/ko-kr/company-news/technology/gemini-3-5-kr/)

## Summary

Google DeepMind's Gemini 3.5 family represents a major leap in AI "actionability," allowing models to not only reason but also execute complex multi-step plans. The 3.5 Flash model is positioned as the industry leader in speed-to-intelligence ratio, making it ideal for large-scale enterprise agent deployments. The release is supported by the "Frontier Safety Framework," ensuring that these highly autonomous agents operate within strict cybersecurity and ethical guardrails.

## Key Claims

- Gemini 3.5 is specifically designed for "long-horizon" tasks and autonomous agent workflows.
- The "Flash" model outperforms the previous 3.1 Pro in coding and agentic benchmarks while being 4x faster and 50% cheaper than other frontier models.
- Enterprise adoption is already high, with companies like Salesforce, Shopify, and Macquarie Bank using it to automate weeks-long workflows into minutes.

## Concepts Linked

- [[concepts/ai-agents/gemini-3-5|Gemini 3.5]]
- [[concepts/ai-agents/agentic-ai|Agentic AI]]
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]]
- [[concepts/frontier-safety-framework|Frontier Safety Framework]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/` evidence before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `partial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/` evidence when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- Claims should be checked against `raw/` evidence when used for recommendations, metrics, or external-facing work.

Official company blog.

## Design Implications

- Use this source to shape product strategy, roadmap framing, operating model, and prioritization prompts.
- Connect it with [[concepts/ai-agents/gemini-3-5]], [[concepts/ai-agents/agentic-ai]], [[concepts/ai-agents/long-horizon-tasks]], [[concepts/frontier-safety-framework]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** product strategy, roadmap framing, operating model, and prioritization prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `partial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
