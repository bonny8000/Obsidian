---
type: source
status: active
created: 2026-07-31
updated: 2026-07-31
tags: [guardrails, content-safety, moderation-api, model-tuning, over-refusal, red-teaming, ai-planning, product-management, makersnote, korea]
source_path: raw/web/maily-product-makers-guardrails-2026-07-31.md
source_url: https://maily.so/makersnote/posts/x1zg5jqvoqg
authors: [Product Makers Note]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.68
---

# Product Makers Note (2026, #24): Guardrails — Putting Brakes on AI

## Citation

Product Makers Note, 「[24호] 기획자를 위한 AI 설계 4부작 ① 가드레일 — AI에 브레이크 달기」 *(AI Design for Planners, part 1 of 4: Guardrails — Putting Brakes on AI)*, **Maily / makersnote**, 2026-07-29.

**Source type:** Practitioner newsletter explainer by a collective of five product makers in the Korean IT industry. First of a four-part series.
**Raw capture:** [[raw/web/maily-product-makers-guardrails-2026-07-31|maily-product-makers-guardrails-2026-07-31]]
**Coverage note:** `coverage: substantial` — the three-layer model, the comparison table, the vendor list, and the Moderation API walkthrough were all captured. This is issue 1 of 4; the series' other three elements are not yet ingested.

Second Product Makers Note source, five issues after [[wiki/sources/maily-product-makers-planning-harness|#19 on the planning harness]].

## Summary

A planner-facing explainer that takes one element of AI service design — **guardrails** — and makes it concrete enough to specify. Its organising claim is that guardrails are not a single filter but **three layers**, and that a planner's job is to decide where each sits and how sensitive it is.

The series frame matters for this vault: four elements of AI service planning are named — **guardrails, tool use, human-in-the-loop, context** — which maps almost exactly onto the four reusable elements already recorded on [[wiki/concepts/product-management/planning-harness|planning harness]] from issue #19 (context, tool definition, guardrails, validation). Issue #24 takes the guardrail element and expands it from "human approval" into a technical architecture.

The best line in it is a scoping claim, not a technical one:

> "가드레일은 온도계예요. '38.5도'라고 숫자만 알려줄 뿐"
> *"A guardrail is a thermometer. It only tells you a number, like '38.5 degrees.'"*

The tool reports; the policy is the planner's.

## Key Claims

- **Guardrails are three defensive layers, not one.** *"세 개의 겹으로 완성됩니다."* Prompt-level instructions, model tuning, and a separate guardrail API each fail differently, so they are stacked rather than chosen between.

- **The prompt layer is the weakest defense** (*"가장 약한 방어선"*). Cheap and immediately editable, but circumvented by adversarial rewrites of the *"ignore previous instructions"* family. This is the same conclusion [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|agent defense in depth]] reaches from reliability rather than safety: *"prompt it not to do that" is not a control.*

- **Model tuning is the fundamental defense but guarantees nothing.** Explicitly *"100%보장 안됨"* — no 100% guarantee. It carries no latency cost, but is slow to implement and, per the sequencing advice, only justified once operational data has accumulated. Two methods named: supervised fine-tuning (*"모법답안을 그대로 따라하게"* — learn by copying exemplar answers) and preference learning.

- **A guardrail API is the independent defense, and its cost is over-refusal.** It blocks decisively and logs, but produces *"과차단"* — over-blocking — and misses *"미묘한 맥락"*, subtle context. The over-refusal cost is named plainly rather than elided, which is the source's most honest move.

- **The threshold is a product decision, not a technical one.** The OpenAI Moderation API returns `flagged` plus `category_scores` on a 0–1 scale; the worked example (self-harm 0.87, violence 0.02, sexual 0.11) exists to make the point that **someone has to choose the cutoff** — 0.7 in the example — plus per-category policy and what happens instead of a bare block. *"문지기를 어디 세우고 얼마나 예민하게 할지 정하는 건 기획자"* — where to post the gatekeeper and how sensitive to make it is the planner's job.

- **Binary block/allow is the wrong output space.** The piece pushes for alternative responses rather than refusal, treating a block as a UX event with a design, not just a policy outcome.

- **Planning changes shape.** From designing deterministic flows to defining behavioural boundaries for an autonomous system: *"메뉴판을 짜는 걸 넘어서 '이런 손님은 어떻게 돌려보낼지'까지 기획자가 정해야 하는 시대"* — beyond composing the menu, deciding how to turn a certain customer away. This is the same role shift [[wiki/concepts/product-management/role-convergence|role convergence]] tracks, arriving from the safety side.

- **Sequencing is by cost profile, not by strength.** Prompts first because they are immediate and cheap; **guardrail APIs offer the best cost-benefit at launch**; tuning last, once there is operational data to justify it. Note this ordering is the *inverse* of the strength ordering — a useful, non-obvious piece of practical advice.

## Useful Examples

**The three-layer comparison** — the reusable artifact:

| Layer | Character | Strength | Weakness / how it is broken |
|---|---|---|---|
| **Prompt** | weakest defense line | immediate, cheap, easily edited | circumvented by adversarial rewrites |
| **Model tuning** | fundamental defense | no latency cost, embeds values | slow; no 100% guarantee |
| **Guardrail API** | independent defense | decisive blocking, logging | over-refusal; misses subtle context |

**The cafe metaphor** running through the piece: the model is cafe staff, harmful requests are problem customers, and the three layers are the staff manual → staff training → a dedicated security guard. Unusually apt, because it also carries the failure modes — a manual can be argued with, training is expensive and imperfect, and a guard turns away paying customers.

**Guardrail models and APIs named** (a catalog, not a comparison):

| Provider | Model / API |
|---|---|
| Kakao | `kanana-safeguard-8b` — Korean harmful-speech filtering |
| OpenAI | Moderation API (`omni-moderation-latest`) — scores text/image without generating |
| Google | ShieldGemma |
| Meta | Llama Guard 4-12B |

**What this puts on the planner's desk:** rejection policy definition; criteria for training material; guardrail-API operating rules (thresholds, per-category handling, alternative responses); and the supporting apparatus — over-refusal management, red-teaming, and retraining loops.

## Constraints / Caveats

- **No measurement at all.** No block rates, over-refusal rates, false-positive/negative figures, latency, or cost. The 0.7 threshold is illustrative and explicitly arbitrary.
- **Explainer, not case study.** No named deployment, no organisation reporting results with this architecture, no incident described.
- **The vendor list is not a comparison.** Four guardrail models are named with no benchmark, no coverage differences, no language-support notes, and no basis for choosing among them.
- **Over-refusal is named but not operationalised.** It is identified as the central cost of the strongest layer, and the only guidance for managing the precision/recall trade-off is that the planner decides. That leaves the hardest problem in the piece unaddressed.
- **Korean-market framing** — the leading example is a Kakao model, and regulatory context is not discussed. Transfer to other jurisdictions is untreated.
- **Collective authorship with no individual attribution** and no stated review process.
- **Part 1 of 4.** The human-in-the-loop and context installments are exactly where this vault's existing material is densest; ingesting this one alone gives a partial view of the series' argument.

## Design Implications

- **Stack the layers; do not choose between them.** Each has a different failure mode, so a single layer leaves a specific, predictable hole.
- **Treat the score as input to a policy, not as the policy.** The thermometer framing is the cleanest available statement of why a safety API cannot be shipped as-is: it produces a number and no decision.
- **Design the refusal.** If a block is inevitable, the alternative response is a product surface, and leaving it undesigned converts a safety success into a UX failure.
- **Sequence by cost, not by strength** — API at launch, tuning once data exists. This inverts the intuitive ordering and is the most practically actionable claim in the source.
- **Budget for over-refusal from the start.** It is a standing operational cost with an owner and a review loop, not a launch-time tuning exercise.

## Tensions

- **Two different three-layer models now sit in this vault, and they are not the same.** [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent defense in depth]] layers **action / behavior / context** for *reliability*; this source layers **prompt / tuning / API** for *content safety*. They agree on the meta-claim — defense is layered and prompts are the weakest layer — and should be linked, not merged. Recorded on both pages.
- **Against this vault's better-evidenced constraint sources.** [[wiki/sources/socar-self-healing-agents|SOCAR]] and [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] achieve control by making misuse *structurally impossible* — removing the capability. This source's strongest layer is a *post-hoc classifier* that scores output. Those are different strategies with different cost profiles, and the source does not consider the structural option at all. See [[wiki/comparisons/where-to-put-the-constraint|Where to Put the Constraint]].
- **Continuity with #19, with an escalation.** Issue #19's guardrail element was "human approval"; #24 replaces that with three technical layers and never returns to human approval. Whether human-in-the-loop is now a separate element (it is part 3 of the series) or a demoted one is unclear from this issue alone.

## Open Questions

- What over-refusal rate do these APIs actually produce at a 0.7 threshold, and how much does it vary by language? For a Korean-market piece, Korean-language false-positive behaviour is the obvious missing number.
- How do the four named guardrail models actually differ? A benchmark would turn this catalog into a decision.
- Does the layered approach compose, or do the layers correlate — does a request that slips past tuning also tend to slip past the API?
- Does part 3 (human-in-the-loop) restore the approval gate that #19 treated as the guardrail, and how is it reconciled with an autonomous three-layer filter?

## Concepts Linked from This Source

- [[wiki/concepts/ai-agents/layered-content-guardrails|Layered Content Guardrails]] *(new)*
- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]]
- [[wiki/concepts/ai-agents/permission-boundary-guardrails|Permission-Boundary Guardrails]]
- [[wiki/concepts/product-management/planning-harness|Planning Harness]]
- [[wiki/concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[wiki/concepts/product-management/role-convergence|Role Convergence]]
- [[wiki/concepts/ai-agents/red-blue-green-agent-teaming|Red/Blue/Green Agent Teaming]]

## LLM Use Guidance

- Use for the **three-layer content-safety vocabulary** and the **cost-based sequencing advice** — both are clean and directly usable when scoping an AI feature.
- Use the **thermometer framing** whenever someone proposes to "just add a moderation API": it names precisely what such an API does and does not supply.
- **Do not cite for any quantitative safety claim.** There are none. Do not treat the vendor list as a recommendation or a ranking.
- Pair with the structural-containment sources before making an architecture decision — this source's option space omits removing the capability entirely.

## Reliability Notes

- **Confidence 0.68.** The framework is coherent, the vendor and API details are checkable, and the over-refusal cost is stated honestly rather than hidden. The score is capped by the genre — a tutorial with no deployment, no measurement, and no case — and by an option space that excludes the structural approach this vault has better evidence for.
- Second source from this publisher; #19 was scored 0.8 with the same genre limits, and on reflection this batch's lower score reflects that #24 is further from evidence (it describes vendor tooling rather than a practice the authors ran).
- **Highest-value follow-up:** ingest parts 2–4 of the series when they publish, particularly part 3 (human-in-the-loop), which touches this vault's densest existing cluster.
