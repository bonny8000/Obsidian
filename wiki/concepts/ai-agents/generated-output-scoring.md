---
type: concept
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [concept, ai-agents, evals, scorers, verification, determinism, llm-as-judge, design-system, quality-gate]
sources: [karrot-kraft-design-system-agent, socar-self-healing-agents]
confidence: 0.7
---

# Generated-Output Scoring

> [!abstract] Summary
> Automatically scoring every generated artifact against system rules *before* a human reviews it — and splitting the scorers by what each check actually requires. Checks that can be decided mechanically (is this a semantic token or a hex value?) run as deterministic static analysis; only checks that need judgment (is this interaction pattern appropriate?) spend a model call.

> [!important] Why it Matters
> The failure mode that destroys trust in a generation tool is not a bad output — it is an **inconsistent** one. [[wiki/sources/karrot-kraft-design-system-agent|Kraft]] reports the same prompt twice yielding one screen that used design tokens and handled error states, and another that hardcoded hex and implemented only the happy path. *"두 번째로 생성한 화면이 첫 번째와 전혀 다른 스타일이면, 도구로서의 신뢰가 깨져요"* — if the second screen's style differs completely from the first, trust in the tool breaks. Human review does not scale to catching this, so the machine has to filter first.

## 📝 Key Claims

- **Split the scorers by what the check needs.** Kraft runs **11**: **7 code-based** (deterministic, fast, free) and **4 LLM-based** (qualitative, slow, metered). The split is the transferable idea — most compliance checking is mechanical and should never cost a model call.

| Code-based (deterministic) | LLM-based (judgment) |
|---|---|
| `color-tokens` — semantic tokens vs. hardcoded hex | `ux-patterns` — pattern fits the screen type |
| `typography` — logical size steps | `interaction-quality` — flow feels natural |
| `layout-structure` — stack primitives vs. system patterns | `flow-patterns` — inter-screen flow matches intent |
| `spacing-rules` — context-appropriate tokens | `form-patterns` — error/loading/empty states handled |
| `component-compliance` — correct props | |
| `icon-usage` — library rules | |
| `animation-stability` | |

- **Score, then feed back.** A low score is not a rejection but an input: the agent receives *where* it failed and can self-correct. Kraft bounds this at **two** attempts before re-verification — an unbounded retry loop on a failing validator burns budget and hides the failure rather than surfacing it.

- **The machine filters before the human reviews.** The purpose is not to replace review but to change what review is spent on — the same effect [[wiki/concepts/infrastructure-dev/llm-safe-design-system|Polar Orbit]] reports from CI enforcement, where review attention moved from policing style drift to discussing behaviour.

- **Never trust self-reported success.** Scoring is the concrete form of [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|defense in depth's]] behaviour layer: the agent saying "done" is not evidence. An independent scorer is.

- **A scorer suite is a maintained asset.** Eleven scorers, four of them model calls, is standing cost — they drift as the system's rules change, and the LLM-based four carry per-run expense. No source states the break-even.

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/product-evals|Product Evals]] — evals as a product-quality discipline; this is its build-time, per-artifact instance.
- [[wiki/concepts/ai-agents/agent-verifiers|Agent Verifiers]]
- [[wiki/concepts/ai-agents/agent-trajectory-evaluation|Agent Trajectory Evaluation]] — scores the *path*; this scores the *artifact*.
- [[wiki/concepts/ai-agents/rule-statistical-external-validation|Rule / Statistical / eXternal Validation]] — the same instinct to classify a check by what can decide it.
- [[wiki/concepts/ai-agents/design-spec-intermediate-representation|Design Spec as Intermediate Representation]] — validation *before* generation; this is validation *after*.
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]]
- [[wiki/concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]]

## ⚖️ Conflicts & Caveats

- **No score data has ever been published.** Kraft describes eleven scorers and reports not one score, distribution, or trend. The architecture is well specified; its effect is entirely unevidenced.
- **The LLM-based scorers have the judge problem.** Using a model to score another model's output inherits the judge's biases and gives no calibration against human judgment. None of the four is validated against a human rater in any source here.
- **Scorers encode the rules at the time they were written** and silently rot when the design system moves. Nobody scores the scorers.
- **A passing score is not a good screen.** Every code-based check is a compliance check; none asks whether the screen solves the user's problem. [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] is the standing warning here — features that existed, passed, and were never wired into the user's flow.

## 📚 Sources

- [[wiki/sources/karrot-kraft-design-system-agent|Karrot (2026): Kraft]] — the 11-scorer suite and the deterministic/LLM split
- [[wiki/sources/socar-self-healing-agents|SOCAR]] — independent validation over self-reported success, with production numbers behind it

## ❓ Open Questions

- What do the scores actually look like in production, and does the distribution tighten over time as memory accumulates?
- How do the four LLM-based scorers correlate with human reviewers? Without that, they are unvalidated instruments.
- What is the cost per generation of running four model-based scorers, and at what volume does that exceed the review time saved?
- Who maintains a scorer suite as the design system evolves, and what detects a scorer that has gone stale?
