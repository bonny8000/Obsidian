---
type: concept
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [concept, agentic-engineering, reliability, safety, production, structured-output, ai-agent]
sources: [socar-self-healing-agents, openworker-andrew-ng]
confidence: 0.85
---

# Agent Defense in Depth

> [!abstract] Summary
> The principle that agent reliability is achieved in **code, not in prompts**. Hallucination and misbehavior are treated as certainties to be structurally contained rather than risks to be instructed away. Defenses are layered at three levels — **action**, **behavior**, and **context**.

> [!important] Why it Matters
> This is the highest-confidence pattern in the agentic-engineering cluster because it comes with production numbers behind it, not argument. SOCAR ran it against 50+ uncontrolled third-party systems for two months: mean incident response fell from 4 hours to under 5 minutes, with 7,267 real recoveries. The lesson is that "prompt it not to do that" is not a control.

## 📝 Key Claims

**The three layers:**

| Layer | Rule | Example |
|---|---|---|
| **Action** | Make misuse structurally impossible | The LLM never receives credentials — it gets element references, and the `login` tool injects secrets via closure |
| **Behavior** | Never trust self-reported success | Validate independently; the agent saying "done" is not evidence |
| **Context** | Show only what is needed | Operator-specific hints live in JSON data, not in the prompt |

- **Separate code concerns from AI concerns:** "code should fix what code can fix; delegate to AI only what AI uniquely does."
- **Constrain the workflow, not just the output.** Confining the model to sequential stages (login → search → discount → check → compare) beat letting it categorize problems itself.
- **Structured output schemas** (Zod) buy two things at once: predictable parsing, and unit-testability via mock substitution.
- **Loop termination is a safety control** — halt after 3 attempts, 3 minutes, or confidence above threshold.
- **Retry asymmetry:** read operations may retry freely; write operations must not, or you get double execution.
- **Confidence calibration needs labeled anchors** spanning the range (0.75 uncertain → 0.95 certain), including explicit negatives, or the scores drift into decoration.

## 🧭 Design Rule of Thumb

> Ask of every safeguard: *would this still hold if the model returned adversarial nonsense?* If the answer depends on the model behaving, it is not a defense — it is a hope.

## ⚖️ Conflicts & Caveats

> [!warning] Costs real engineering
> Baseline schemas, structured outputs and per-stage isolation are a standing maintenance burden. SOCAR names it explicitly: operator sites change faster than baselines are updated. This only pays at sufficient volume — below some threshold, the constraint architecture costs more than the failures it prevents.

> [!note] Evidence boundary
> The 100% classification accuracy is on 186 hand-labeled cases annotated by the two authors, not an automated evaluation. Read it as "100% on a small curated set."

## 🔗 Related Concepts

- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]] — the deployment-boundary layer
- [[wiki/concepts/infrastructure-dev/agentic-engineering|Agentic Engineering]]
- [[wiki/concepts/ux-research/human-in-the-loop|Human in the Loop]]
- [[wiki/concepts/ai-agents/ai-as-senior-hire|AI as a Senior Hire]] — the position this most directly constrains
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]
- [[wiki/concepts/ai-agents/layered-content-guardrails|Layered Content Guardrails]] — **a different three layers, deliberately not merged.** This page layers *action / behavior / context* for **reliability**; that one layers *prompt / tuning / API* for **content safety**. They agree on the meta-claim — defense is layered, and the prompt is the weakest layer — but they are not the same taxonomy and should not be collapsed into one.

## 📚 Sources

- [[wiki/sources/socar-self-healing-agents|SOCAR (2026): AI Agents That Self-Repair Failures]]
- [[wiki/sources/openworker-andrew-ng|AX LABS (2026): OpenWorker]]

## ❓ Open Questions

- Does the sequential-stage design generalize beyond workflows that mirror a human script?
- At what integration count does baseline-schema maintenance exceed the cost it saves?
- Can the context layer be automated, or does it always require hand-authored per-target knowledge?
