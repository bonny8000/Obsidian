---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, context-engineering, agentic-ai, harness, retrieval, reliability]
sources: [bayer-prince-reliable-agentic-ai, the-new-sdlc-with-vibe-coding-day-1]
confidence: 0.85
---

# Context Engineering

> [!abstract] Summary
> Deliberately shaping *what information each model or step receives, what it does not receive, and how context moves between steps* — distinct from prompt engineering (wording) and harness engineering (scaffolding around the model).

> [!important] Why it Matters
> Larger context windows did not remove the need to be selective. Stuffing everything into one prompt creates "context pollution" that makes agentic systems hard to steer, debug, and evaluate. Routing the right context to the right capability is what lets each stage be tested and improved in isolation.

## 📝 Key Claims
- Different stages need different context: planning context for plan steps, retrieval context for the researcher, evidence context for reflection, synthesis context for the writer.
- "Context discipline": inject only the schema/evidence relevant to the current step (e.g., only relevant DB schema for Text-to-SQL; curated chunks + citation constraints for the writer).
- Moving from a monolithic agent to context-routed stages makes evaluation, debugging, and recovery tractable.
- As model capability grows, some context plumbing may thin out, but explicit context control remains essential where trust and traceability matter.

## 🔗 Related Concepts
- [[concepts/ai-agents/agentic-rag|Agentic RAG]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/model-harness|Model Harness]]
- [[concepts/ai-agents/context-rot|Context Rot]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/infrastructure-dev/claudemd-context|CLAUDE.md Context]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Tension with "just use a bigger context window" framings. The PRINCE case argues the opposite: selectivity beats volume for steerability and evaluation.

## 📚 Sources
- [[sources/bayer-prince-reliable-agentic-ai|Bayer/PRINCE: Building Reliable Agentic AI Systems]]
- [[sources/the-new-sdlc-with-vibe-coding-day-1|Day 1 — The New SDLC With Vibe Coding]]

## ❓ Open Questions
- Which parts of today's context plumbing become native model capabilities, and which stay explicit?
- How to measure context quality per stage, not just end-to-end output?
