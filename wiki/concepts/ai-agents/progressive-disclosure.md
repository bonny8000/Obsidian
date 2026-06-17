---
type: concept
status: active
created: 2026-06-17
updated: 2026-06-17
tags: [agent-skills, context-engineering, token-economics, progressive-disclosure]
sources:
  - sources/agent-skills-day-3
confidence: 0.9
---

# Progressive Disclosure

> [!abstract] Summary
> The three-level loading model used by Agent Skills: metadata is always in the agent's context, the SKILL.md body loads only when the description matches, and bundled resources (`scripts/`, `references/`, `assets/`) load strictly on demand. Scripts execute without ever polluting the token window.

> [!important] Why it Matters
> Progressive disclosure is the architectural answer to [[concepts/ai-agents/context-rot|Context Rot]]. It is what makes a library of 50–100 Skills practical: instead of paying the full token cost of every workflow on every turn, the agent pays the tiny metadata cost always and the body cost only when needed. This collapses the "more capability vs more context" tradeoff that broke earlier agent architectures.

## 📝 Key Claims

- **Three loading levels:**
  1. **Metadata** (name + description) — always loaded, ~50 tokens per skill.
  2. **SKILL.md body** — loaded only when the skill description matches, ~2,000 tokens active.
  3. **Bundled resources** (`scripts/`, `references/`, `assets/`) — loaded strictly on demand. Scripts run out-of-process, returning only their results.
- **Token math (per the paper):** an agent with 50 workflows as a single system prompt loads ~15,000 tokens every turn. As a Skills library it loads ~4,000 tokens of descriptions + ~2,000 tokens of one active body ≈ 6,000 tokens total, with the other 49 bodies on disk.
- **Anthropic published a workflow** converted from ~150,000 active tokens to ~2,000 — a **98%+ reduction**.
- **Capacity is the wrong metric.** A 1M-token context window can show significant degradation at 50K tokens. Treat active context as a *budget*, not a vessel.
- The principle generalizes: **load instructions dynamically only when explicitly invoked**. Always-on instructions ("ALWAYS DO X") accumulate Context Debt and get ignored by the model — see [[concepts/ai-agents/agent-skills|Agent Skills]] and the "Shift Intelligence Left" pattern.
- Progressive disclosure decouples *available* capability (effectively unbounded, on disk) from *active* capability (small, in context).

## How to apply

- If your SKILL.md body is getting long, the next paragraph probably belongs in `references/`, not in the body.
- Deterministic work (parsing exports, math, formatting) belongs in `scripts/`, not as prose instructions.
- Templates, schemas, and output scaffolds belong in `assets/`.
- The description field is the *only* thing the model sees during routing — spend disproportionate authoring time there.

## 🔗 Related Concepts

- [[concepts/ai-agents/agent-skills|Agent Skills]] — the format that uses progressive disclosure.
- [[concepts/ai-agents/context-rot|Context Rot]] — the failure mode progressive disclosure resolves.
- [[concepts/ai-agents/skill-system|Skill System]]
- [[concepts/infrastructure-dev/text-space-optimization|Text-Space Optimization]] — related principle of treating documents as load-bearing optimizable artifacts.
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]] — the runtime scaffolding that implements the loading mechanism.

## ⚖️ Conflicts & Caveats

> [!warning] Boundary
> Progressive disclosure works only when the description is sharp enough to reliably trigger the right skill. A vague description means an unloaded body — and possibly worse, an over-loaded body that crowds out other workflows. The discipline is in the description, not the mechanism.

## 📚 Sources

- [[sources/agent-skills-day-3|Singhal et al. (2026): Agent Skills (Day 3)]] — primary source for the three-level model and token math.

## ❓ Open Questions

- How should progressive disclosure interact with prompt caching? Are cached prefixes a competing or complementary optimization?
- For Skills with very long `references/`, when should the agent be told to *summarize* a reference vs *read* it in full?
