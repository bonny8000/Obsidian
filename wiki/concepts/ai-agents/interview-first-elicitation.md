---
type: concept
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [concept, ai-agent, requirements-elicitation, prompting, prd, claude-code, context-engineering]
sources: [claude-code-interview-first]
confidence: 0.68
---

# Interview-First Elicitation

> [!abstract] Summary
> Invert requirements gathering with a coding agent: instead of authoring a brief for the agent, have the **agent interview you** — one question at a time, offering trade-offs rather than making unilateral calls — and formalize the result only afterward.

> [!important] Why it Matters
> The economic argument is the strong part. The expensive failure is not a long prompt; it is **code generated in the wrong direction**. Regeneration dwarfs input cost, so decisions should be settled in cheap conversational turns before generation begins. For a UX audience this is a familiar principle wearing new clothes: *elicit before you build.*

## 📝 Key Claims

- **"The real cost isn't long prompts but code running in the wrong direction."**
- **Three mechanisms make interviewing cheaper:** short Q&A turns replace long generation turns; the user is spared document-writing labor; and — the strongest — a good interview **surfaces decisions the user had not consciously made**, which no amount of user-authored specification would have captured.
- **One question at a time is load-bearing.** Batched questions collapse into form-filling and lose the follow-up that surfaces the unconscious decision.
- **Non-goals anchor direction** more efficiently than additional requirements.
- **Retrospective → rules** is the compounding loop: convert each session's lessons into persistent `CLAUDE.md` constraints.

## 🧭 The Sequence

1. **Interview me, don't code** — one question at a time.
2. **Offer trade-offs**, don't choose unilaterally.
3. **Read the codebase first**; surface conflicts with what exists.
4. **Probe edge cases** systematically — happy path vs. failure modes.
5. **Formalize** into goals / non-goals / requirements / edge cases / completion criteria.
6. **Approve the plan** before implementation begins.
7. **Retrospect**, and write the lesson into `CLAUDE.md`.

## ⚖️ Conflicts & Caveats

> [!warning] Tension with "AI as a senior hire"
> You would not interrogate a senior colleague through twenty clarifying questions before they started work. This looks precisely like the micro-specification [[wiki/concepts/ai-agents/ai-as-senior-hire|Holbrook warns against]] — **unless** the distinction is *who drives the questioning*. Agent-led interrogation shifts labor from user-authored prescription to agent-identified ambiguity, which is a materially different thing. Neither source makes this distinction explicit; this wiki holds it as the reconciliation.

> [!warning] No stated limitations in the source
> The author names no failure mode and offers no measurement of the claimed token savings. A method presented as universally applicable has not been stress-tested in the writing — the main reason for **confidence 0.68**.

> [!note] Possible conflict with the Change Brief
> [[wiki/concepts/ai-agents/change-brief|Eisele]] would likely object to step 5 — formalizing into a standing PRD re-creates the document he wants to see expire.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/prd-generation|PRD Generation]]
- [[wiki/concepts/ai-agents/change-brief|Change Brief]]
- [[wiki/concepts/ai-agents/ai-as-senior-hire|AI as a Senior Hire]]
- [[wiki/concepts/ai-agents/spec-driven-development|Spec-Driven Development]]
- [[wiki/concepts/ux-research/ai-moderated-interviews|AI-Moderated Interviews]] — the same inversion, applied to research participants

## 📚 Sources

- [[wiki/sources/claude-code-interview-first|AX LABS (2026): Don't Write a PRD — Let Claude Code Interview You]]

## ❓ Open Questions

- Does it reduce total tokens, or move them? Unmeasured.
- Where is the user-fatigue threshold — how many questions before disengagement?
- Does it hold for small deltas, or only where ambiguity is genuinely high?
