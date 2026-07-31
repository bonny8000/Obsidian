---
source_url: https://maily.so/makersnote/posts/x1zg5jqvoqg
captured: 2026-07-31
title: "[24호] 기획자를 위한 AI 설계 4부작 ① 가드레일 — AI에 브레이크 달기"
title_en: "[Issue 24] AI Design for Planners, a 4-part series ① Guardrails — Putting Brakes on AI"
authors: [Product Makers Note]
published: 2026-07-29
publisher: Product Makers Note (makersnote) on Maily
language: ko
format: newsletter (practitioner explainer)
series: "기획자를 위한 AI 설계 4부작, part 1 of 4"
---

# Product Makers Note #24 — Guardrails: Putting Brakes on AI

**Newsletter:** Product Makers Note — a collective of five product makers in the Korean IT industry.
**Published:** 2026-07-29 · **Captured:** 2026-07-31 · Views at capture: 495

AI-written extraction. No full-text reproduction; short quoted phrases only.

Same publisher as [[raw/web/maily-product-makers-planning-harness-2026-06-25|Product Makers Note #19 (Planning Harness)]], five issues later.

---

## Series framing

A four-part series on designing AI *services*, positioned as distinct from the existing conversation about "planning AX" (using AI to do planning work). Four core elements of AI service planning:

1. **Guardrails** — preventing harmful output (this issue)
2. **Tool Use** — letting AI execute
3. **Human-in-the-Loop** — letting humans intervene
4. **Context** — situational understanding

## Definition

> "AI가 하면 안 되는 걸 하지 못하도록 모델을 감싸는 안전장치"
> *"A safety mechanism wrapping the model so it cannot do what it must not do."*

Guardrails are presented as **three layers**, not a single point of protection. *"세 개의 겹으로 완성됩니다"* — *"it is completed in three layers."*

## The three layers

| Layer | Character | Strength | Weakness / breakthrough point |
| --- | --- | --- | --- |
| **Prompt** (system instructions) | *"가장 약한 방어선"* — the weakest defense line | easy to modify, immediate, cheap | easily circumvented; vulnerable to adversarial rewrites such as *"이전 지시 무시해"* ("ignore previous instructions") |
| **Model tuning** | *"근본적인 방어선"* — the fundamental defense | foundational; no latency cost | slow to implement; **no 100% guarantee** (*"100%보장 안됨"*) |
| **Guardrail API** (separate inspection model) | *"독립된 방어선"* — an independent defense | decisive blocking; logging capability | causes **over-refusal** (*"과차단"*); misses *"미묘한 맥락"* (subtle context) |

**Cafe metaphor used throughout:** the model is cafe staff; harmful requests are problem customers (profanity, requesting dangerous items). The three layers map to staff manual → staff training → a dedicated security guard.

### Tuning methods named

1. **Supervised fine-tuning** — *"모법답안을 그대로 따라하게"* (learn by copying exemplar answers)
2. **Preference learning** (*"선호학습 방식"*) — rank preferred vs. suboptimal responses

### Guardrail models/APIs named

- **Kakao `kanana-safeguard-8b`** — Korean harmful-speech filtering model
- **OpenAI Moderation API (`omni-moderation-latest`)** — scores text/image risk without generating
- **Google ShieldGemma**
- **Meta Llama Guard 4-12B**

### OpenAI Moderation API walkthrough

Returns JSON with `flagged` (boolean) and `category_scores` on a 0–1 scale. Worked example given: self-harm 0.87, violence 0.02, sexual 0.11. The planner sets the cutoff — 0.7 is the example used for self-harm — plus per-category policy and alternative responses beyond a binary block/allow.

> "가드레일은 온도계예요. '38.5도'라고 숫자만 알려줄 뿐"
> *"A guardrail is a thermometer. It only tells you a number, like '38.5 degrees.'"*

> "문지기를 어디 세우고 얼마나 예민하게 할지 정하는 건 기획자"
> *"Deciding where to post the gatekeeper and how sensitive to make it is the planner's job."*

## What this makes the planner responsible for

- Defining the rejection policy
- Establishing criteria for training material
- Designing operational rules for the guardrail API (thresholds, per-category handling, alternative responses)
- Supporting infrastructure: over-refusal management, red-teaming, retraining loops

## Sequencing advice

Implementation order differs by cost profile: **prompts** are immediate and cheap; **APIs** offer the best cost-benefit at launch; **tuning** requires accumulated operational data before the investment is justified.

## Conclusion

Planning is reframed from designing deterministic flows to defining **behavioral boundaries** for autonomous systems.

> "메뉴판을 짜는 걸 넘어서 '이런 손님은 어떻게 돌려보낼지'까지 기획자가 정해야 하는 시대"
> *"An era where the planner must go beyond composing the menu to deciding 'how do we turn this kind of customer away.'"*

**Next installment:** Tool Use — the inverse problem of letting AI execute beyond conversation.

## Limitations and caveats (as observed in the text)

- **No measurement anywhere.** No block rates, no over-refusal rates, no false-positive/false-negative figures, no cost numbers. The 0.7 threshold is illustrative, not derived.
- **Explainer/tutorial genre**, not a case study. No named deployment, no organization reporting results with this architecture.
- The vendor/model list is a **catalog**, not a comparison — no benchmark of `kanana-safeguard-8b` vs. ShieldGemma vs. Llama Guard vs. OpenAI Moderation is offered.
- **Over-refusal is named as a risk but not quantified**, and no method for tuning the precision/recall trade-off is given beyond "the planner decides."
- Korean-language and Korean-market framing (the Kakao model is the leading example); transfer to other regulatory contexts is not discussed.
- Newsletter written by a practitioner collective; no author-level attribution and no stated review process.
