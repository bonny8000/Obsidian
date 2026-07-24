---
type: source
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [claude-code, prd, requirements-elicitation, prompting, ai-agent, context-engineering, interview, agentic-engineering]
source_path: raw/web/axlabs-claude-code-interview-first-2026-07-24.md
source_url: https://theaxlabs.com/blog/claude-code-interview-first
authors: [AX LABS]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.68
---

# AX LABS (2026): Don't Write a PRD — Let Claude Code Interview You

## Citation

AX LABS, 「PRD를 쓰지 마세요. Claude Code가 당신을 인터뷰하게 하세요」, **AX LABS Blog**, 2026-07-23. Korean.

**Source type:** Practitioner prompt guide. No evaluation, no stated limitations.
**Raw capture:** [[raw/web/axlabs-claude-code-interview-first-2026-07-24|axlabs-claude-code-interview-first-2026-07-24]]

## Summary

Invert the direction of requirements gathering: rather than authoring a PRD for the agent, have the agent **interview you**, one question at a time, and formalize the result afterward. The economic argument is the interesting part — the expensive failure is not a long prompt but **code generated in the wrong direction**, so decisions should be settled in cheap conversational turns before any generation begins.

## Key Claims

- **"The real cost isn't long prompts but code running in the wrong direction."** Regenerating wrong output dwarfs the input cost.
- **Three mechanisms make interviewing cheaper:** short Q&A turns replace long generation turns; the user avoids document-writing labor; and a good interview *surfaces decisions the user had not consciously made* — the strongest of the three, since it addresses requirements that would otherwise never have been elicited at all.
- **Decision-first:** "finish decisions through inexpensive conversation before code generation."

## Useful Examples

**Pre-launch — elicitation**
- Open with "interview me, don't code," one question at a time.
- Offer trade-off options rather than making unilateral choices.
- Read the codebase first; identify conflicts with what exists.
- Probe edge cases systematically.
- Formalize into a PRD: goals / non-goals / requirements / edge cases / completion criteria.

**Execution — holding direction**
- Require approval of the implementation plan before coding.
- Ask rather than assume when uncertain.
- Record code preferences in `CLAUDE.md`.

**Post-completion — iteration**
- Interview before fixing bugs; diagnose first.
- Run retrospective interviews and convert lessons into `CLAUDE.md` rules — the loop that makes the practice compound.

## Constraints / Caveats

- **The author states no limitations whatsoever.** This is itself a reliability signal and the main reason for the lower confidence score: a method presented as universally applicable, with no failure mode named, has not been stress-tested in the writing.
- Assumes access to Claude Code specifically, though the technique is tool-agnostic in principle.
- No measurement of the claimed token savings is offered.

## Design Implications

- **Elicitation is cheaper than correction** — a general principle worth applying beyond coding agents, and one that maps directly onto UX research practice (interview before building).
- **Non-goals deserve equal weight to goals** in any agent brief; they anchor direction more efficiently than additional requirements.
- **Retrospective → rules** is the compounding mechanism: each session's lesson becomes a persistent constraint in `CLAUDE.md`.
- One question at a time is a real constraint — batched questions collapse back into form-filling and lose the follow-up that surfaces unconscious decisions.

## Tensions

- **Against [[wiki/sources/ai-as-senior-hire-not-intern|"AI as a senior hire"]]:** you would not interrogate a senior colleague through twenty clarifying questions before they started. This source's method looks precisely like the micro-specification Holbrook warns against — *unless* the distinction is that the agent drives the questioning, which shifts the labor from user-authored prescription to agent-identified ambiguity. That distinction is the reconciliation, and neither source makes it explicit.
- **With [[wiki/sources/spec-driven-development-exit-strategy|Eisele]]:** both agree the artifact should serve one decision. Eisele would likely object to the final "formalize into a PRD" step as re-creating the standing document he wants to eliminate.

## Open Questions

- Does interview-first actually reduce total tokens, or move them? No measurement is offered.
- How many questions before the user disengages — where is the fatigue threshold?
- Does it hold for small deltas, or only for new features where ambiguity is genuinely high?

## Concepts Linked from This Source

- [[wiki/concepts/ai-agents/interview-first-elicitation|Interview-First Elicitation]]
- [[wiki/concepts/ai-agents/prd-generation|PRD Generation]]
- [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]]
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]

## LLM Use

Use as a **prompting pattern**, not as evidence. The elicitation sequence is directly reusable for feature work. When citing the cost argument, flag that it is asserted rather than measured.

## Reliability Notes

- **Confidence 0.68** — practical and internally coherent, but unmeasured, and the complete absence of stated caveats is a mark against it rather than for it.
- Token-cost claims are plausible on first principles but unquantified in the source.
- **Ingested from an AI-generated extraction of a Korean-language post, not a verbatim read.**
