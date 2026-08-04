---
type: concept
status: active
created: 2026-06-22
updated: 2026-08-04
tags: [concept, context-engineering, agentic-ai, harness, retrieval, reliability]
sources: [bayer-prince-reliable-agentic-ai, the-new-sdlc-with-vibe-coding-day-1, nngroup-ux-context-design]
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

## The UX Branch: Curating What the Organisation Knows

> [!important] Added 2026-08-04
> [[wiki/sources/nngroup-ux-context-design|NN/g named the UX-side discipline]] of this in July 2026: **[[wiki/concepts/ux-research/ux-context-design|UX-Context Design]]** — curating research and design knowledge into the context that steers generated output, rather than into documents written to persuade humans.
>
> Two things worth importing into the engineering frame:
>
> **1. The mechanism is correctly stated as bias, not instruction.** *"Context leans a model's output in a particular direction."* Without it, generation lands on the statistical middle.
>
> **2. The success criterion is mechanical.** *"Its success is measured by whether AI output improves, not by whether stakeholders are convinced."* That is a testable standard — and NN/g's own version of it is circular, because the same party writes the context and judges the output. **If you adopt the criterion, get an independent judge.**
>
> The five proposed content types for a `UX.md`: research synthesis as *actionable constraints*, interaction standards, a glossary of the users' own vocabulary, user models, and **world models** (the circumstances of use — the component usually missing and the one that most changes output).
>
> **The practical filter that transfers cleanly: obeyability.** Could a generator act on this sentence? "Users found the flow confusing" cannot be obeyed; "never ask for a policy number before the incident date, because users file from the roadside without documents" can.
>
> Caveat: the source has **no evidence** for its central claim — *"our experiments suggest"* with no methodology, sample, or baseline. Adopt the framing; do not cite the effect.

## Additional Sources

- [[wiki/sources/nngroup-ux-context-design|Alicea (2026): UX-Context Design]] — the UX-facing formulation, the five components, and the obeyability test.

## ❓ Open Questions
- Which parts of today's context plumbing become native model capabilities, and which stay explicit?
- How to measure context quality per stage, not just end-to-end output?
- **Which artifact types actually move generated output, and by how much?** NN/g asks this and answers none of it; it is a small controlled comparison nobody has run.
- Is there a context saturation point past which more context degrades rather than plateaus?
- Does a curated context file drift toward what the model handles well rather than what is true? That is the selection pressure the improve-the-output feedback loop creates.
