---
type: concept
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [concept, ai-agents, guardrails, content-safety, moderation, over-refusal, model-tuning, red-teaming, product-management]
sources: [maily-product-makers-guardrails]
confidence: 0.66
---

# Layered Content Guardrails

> [!abstract] Summary
> Content safety built as **three stacked defenses** rather than one filter — system-prompt instructions, model tuning, and a separate inspection model or moderation API — because each layer fails in a different way. The layer strengths run prompt < tuning < API, but the *deployment* order runs the other way, because cost and time do too.

> [!important] Why it Matters
> This is where a product decision hides inside what looks like a technical one. A moderation API returns a number, not a policy: *"가드레일은 온도계예요. '38.5도'라고 숫자만 알려줄 뿐"* — a guardrail is a thermometer, it only tells you a number. Somebody has to choose the cutoff, decide what happens instead of a bare refusal, and own the over-blocking that follows. [[wiki/sources/maily-product-makers-guardrails|Product Makers Note]] assigns that to the planner, which reframes planning from designing flows to **defining behavioural boundaries**.

## 📝 Key Claims

| Layer | Character | Strength | How it fails |
|---|---|---|---|
| **Prompt** — system instructions | *"가장 약한 방어선"* (weakest defense line) | immediate, cheap, editable | circumvented by adversarial rewrites of the "ignore previous instructions" family |
| **Model tuning** — SFT or preference learning | *"근본적인 방어선"* (fundamental defense) | no latency cost; embeds the values | slow to build; explicitly **no 100% guarantee** |
| **Guardrail API** — separate inspection model | *"독립된 방어선"* (independent defense) | decisive blocking; logs everything | **over-refusal** (*"과차단"*); misses subtle context |

- **Deploy in the inverse of the strength order.** Prompts first (immediate, cheap); a **guardrail API at launch**, where the cost-benefit is best; tuning last, once operational data justifies the investment. The non-obvious part is that the strongest layer is the one you build last.

- **The score is not the decision.** A moderation API returns `flagged` plus `category_scores` on a 0–1 scale. Threshold selection (0.7 in the worked example), per-category policy, and the alternative response are all product decisions downstream of the number.

- **Binary block/allow is the wrong output space.** A refusal is a UX event with a design. Leaving it undesigned turns a safety success into a product failure.

- **Over-refusal is a standing operational cost**, not a launch-time tuning task — it needs an owner, monitoring, red-teaming, and a retraining loop.

- **Prompts are not a control.** Arrived at here from content safety; [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|agent defense in depth]] reaches the identical conclusion from reliability, with production evidence behind it.

**Models and APIs named** (a catalog, explicitly not a benchmark): Kakao `kanana-safeguard-8b` (Korean harmful speech) · OpenAI Moderation API `omni-moderation-latest` · Google ShieldGemma · Meta Llama Guard 4-12B.

## 🔗 Related Concepts

- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]] — **a different three layers.** That page layers *action / behavior / context* for **reliability**; this layers *prompt / tuning / API* for **content safety**. They agree that defense is layered and that prompts are the weakest layer, and they are deliberately kept separate rather than merged.
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]] — the structural alternative: remove the capability instead of scoring the output.
- [[wiki/concepts/product-management/planning-harness|Planning Harness]] — same publisher, five issues earlier; guardrails were one of its four elements, expanded here.
- [[wiki/concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[wiki/concepts/ai-agents/red-blue-green-agent-teaming|Red/Blue/Green Agent Teaming]] — red-teaming is named as required supporting infrastructure.
- [[wiki/concepts/ai-agents/frontier-safety-framework|Frontier Safety Framework]]
- [[wiki/comparisons/where-to-put-the-constraint|Where to Put the Constraint]]

## ⚖️ Conflicts & Caveats

- **A post-hoc classifier is a weaker instrument than structural containment.** [[wiki/sources/socar-self-healing-agents|SOCAR]] and [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] achieve control by making misuse *impossible* — the model never receives the credential, never gets the tool. Scoring the output after the fact is a different and generally weaker strategy, and the source never considers the structural option.
- **No measurement anywhere.** No block rates, over-refusal rates, false-positive figures, latency, or cost. The 0.7 threshold is illustrative and admittedly arbitrary.
- **The vendor list is a catalog, not a comparison.** Four models, no benchmark, no coverage or language-support differences, no basis for choosing.
- **Over-refusal is named and then abandoned.** It is identified as the central cost of the strongest layer, and the only guidance for managing the precision/recall trade-off is that the planner decides — leaving the hardest problem unaddressed.
- **Single source, tutorial genre.** No deployment, no case, no incident.

## 📚 Sources

- [[wiki/sources/maily-product-makers-guardrails|Product Makers Note (2026, #24): Guardrails]]

## ❓ Open Questions

- What over-refusal rate do these APIs produce at a 0.7 threshold, and how much does it vary by language? For Korean-market deployment that is the decisive unknown.
- Do the layers compose or correlate — does a request that evades tuning also tend to evade the API?
- How do the four named guardrail models actually differ in coverage and language support?
- When is scoring the output the right choice over removing the capability? See [[wiki/comparisons/where-to-put-the-constraint|the comparison]].
