---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [ai-prd, product-management, eval-plan, llm-evaluation, regression-testing, pricing-model, prompt-swamp]
source_path: raw/web/yozm-ai-prd-2026-06-22.md
source_url: https://yozm.wishket.com/magazine/detail/3809/
authors: [김영욱 (Kim Young-wook)]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# Yozm IT (2026): What an AI PRD Must Do Differently (AI PRD는 무엇이 달라야 하는가)

**Author:** 김영욱 (Kim Young-wook / ywkim36) — Yozm IT (Wishket), 2026-06-18.
**Raw capture:** [[raw/web/yozm-ai-prd-2026-06-22|yozm-ai-prd-2026-06-22]]
**URL:** [yozm.wishket.com/magazine/detail/3809](https://yozm.wishket.com/magazine/detail/3809/)

> [!note] Upgraded from partial
> The page is JavaScript-rendered (web_fetch got only the shell). Full content was captured 2026-06-22 from **Bonny's Chinese summary** of the article (a digested rewrite, not the verbatim original) — so the structure and all key claims are reliable, but exact figures (e.g. "≤100 chars", the "₩9,900" example) are the article's illustrative numbers and may be paraphrased.

## Citation

Kim, Y. (2026, June 18). *AI PRD는 무엇이 달라야 하는가 [What should be different about an AI PRD].* Yozm IT (Wishket). Captured 2026-06-22 (via Bonny's Chinese summary) into `raw/web/yozm-ai-prd-2026-06-22.md`.

## Summary

The framing analogy: **mom's recipe** ("a pinch of salt," "cook until it boils") is a loose reference for someone who already knows how to cook; a **Michelin chef's recipe** ("2.3g sea salt," "hold 75°C for 4 minutes") is a design spec anyone can reproduce identically. Traditional software PRDs are the former — software is **deterministic** (same input → same output), so defining *what should happen* ("press the button → go to checkout") sufficed. **AI features are non-deterministic**: the same prompt yields different answers each time, and different builders (or the same builder twice) produce different results. So an AI PRD must define not "what should happen" but **"what range of answers is acceptable"** and **"how to judge whether an answer is acceptable."** Its new heart is the **Eval Plan**. The author covers why traditional PRDs fail for AI, the Eval Plan in depth, an **8-item AI-PRD checklist**, and why a **pricing model** must live inside the PRD.

## Key Claims

- **Traditional PRD defines a single behavior; AI PRD defines a range of acceptable answers + how to judge them.** "Correct" needs a definition (90%? 99%? which questions to answer vs refuse? is a varying answer a bug or a feature?). Running example: the Air Canada bereavement-discount chatbot (from the series' part ①) — a PRD that just says "answer correctly" is underspecified.
- **Eval Plan = writing the evaluation standard + tooling into the PRD.** It is fundamentally a **collection of test cases** (often starting as a spreadsheet): each row = input (user question), expected output, actual output, score, pass/fail. Example: input "delivery is too slow" → expected = confirm order # then explain delivery status (+ offer return/exchange if needed); a bare "sorry for the inconvenience" = **fail** (didn't answer "what happened to my order"). Start with **20–30 cases**, add a row per new failure; ~6 months → ~**200 cases**, the team's biggest asset.
- **Eval pyramid (how to score at scale):**
  - **Rule-based** (bottom): explicit auto-checks (must contain a term, length limit, no confidential content) — fast, near-zero cost, but blind to subtle "is it actually helpful."
  - **LLM-as-a-Judge** (middle): another LLM grades quality — ~100× faster/cheaper than humans, but the judge's own bias/hallucination means it can't be fully trusted.
  - **Human Eval** (top): most accurate, slowest/most expensive; reserved for the trickiest or newly-discovered failure modes, and **required to set regression baselines.**
  - Daily = rule-based + LLM-judge; major changes add human eval. The PM pre-assigns each case's evaluation layer in the Eval Plan to keep post-launch eval cost controlled.
- **Regression testing dissolves the "Prompt Swamp (프롬프트 수렁)":** editing a prompt to fix case A breaks case B, fixing B breaks C — effort spent, no net gain. Fix = **rerun the whole accumulated Eval set on every prompt change** and confirm no case's score dropped. Putting the Eval Plan in the PRD is a **commitment** to keep measuring with the same (hardening) standard after launch — and that commitment decides the feature's fate 6 months out.
- **The 8 required AI-PRD items** (same headings as a normal PRD, but the AI content differs):
  1. **Feature overview** — what user problem this solves; the answer must be "AI is best at this problem," not "because we want to use AI" (AI-for-AI's-sake is the #1 failure start).
  2. **Input/output spec** — form/length/language of input and output; you can't control the model without defining its raw input.
  3. **System-prompt draft** — draft it at PRD stage (role, tone/format, what to reference, what not to do, the exit when stuck); don't punt to engineers. This sets the feature's "personality."
  4. **Quality standard** — what counts as pass (fact accuracy, tone, length) — the basis for the Eval Plan.
  5. **Failure definition** — explicitly define a "failed" answer (confident wrong info / hallucination, promises that violate policy, dangerous advice). *The Air Canada incident traces to a missing failure definition.*
  6. **Eval Plan** — as above.
  7. **Monitoring plan** — post-launch: which metrics on the dashboard, what triggers an alert, how often to rerun Eval (metric detail deferred to the next article, but "how to observe" belongs in the PRD).
  8. **Risks & limitations** — honest limits (weak domains, cost-blowup scenarios, regulatory risk); usually the shortest section but the one most consulted in a crisis.
- **Pricing model belongs in an AI PRD.** Unlike traditional SaaS, AI pricing can't be separated from product design because **every use incurs real token cost** (a flat "₩9,900/user/mo" can be blown 10× by one user pasting PDFs for summaries). Three evolving models: **usage-based** (per token / API call — OpenAI), **outcome-based** (per resolved case — Zendesk/Intercom AI support), **hybrid** (base + usage overage — most common in practice). Pricing choice feeds product design: outcome-based pricing means success metrics must be outcome-centric, and "resolved" must be defined in the Eval Plan. Contrast: **Salesforce Agentforce** aligned value↔price with Flex Credits usage pricing (market trust); **Adobe Firefly** didn't explain how AI investment converts to profit (stock dropped).

## Useful Examples

- The **mom-vs-Michelin recipe** analogy for deterministic vs non-deterministic specs.
- The **Eval spreadsheet row** ("delivery too slow" → expected vs failing "sorry for the inconvenience").
- The **Air Canada bereavement-discount** case as the canonical "missing failure definition / no Eval Plan" failure.
- **Salesforce Agentforce (Flex Credits) vs Adobe Firefly** as a value↔pricing-alignment contrast.

## Constraints / Caveats

- Practitioner magazine how-to (Korean), single author; opinionated framework, not research.
- **Captured via a secondary Chinese summary**, not the verbatim article — treat exact numbers/quotes as illustrative; re-verify against the original before quoting precisely.
- Metric specifics (dashboards, alert thresholds) are deferred by the author to a follow-up piece.

## Design Implications

- Add an **Eval Plan as a first-class PRD section** for any AI feature: a living test-case set + a per-case evaluation layer (rule / LLM-judge / human) + a regression rule (rerun all on every prompt change). Converges with [[concepts/ai-agents/spec-driven-development|Spec-Driven Development]] ("promise the acceptable range") and [[concepts/ai-agents/vibe-coding-agent-evaluation|"worth shipping" evaluation]].
- Always write an explicit **failure definition** — it's the cheapest insurance against Air-Canada-class incidents.
- Treat **pricing as a product-design input**, not a later sales decision, because token cost couples usage to margin; keep feature def / Eval Plan / success metrics / pricing mutually consistent.
- Use the **Eval pyramid** to keep evaluation affordable at 200+ cases.

## Tensions

- Deterministic PRD habits vs non-deterministic AI behavior (the core tension).
- **LLM-as-a-Judge cost/speed vs its own unreliability** — cheap scale traded against judge bias/hallucination.
- Velocity vs the discipline of regression-testing every prompt change (the way out of the prompt swamp).

## Open Questions

- The deferred **metrics/monitoring** detail (dashboards, alerts) — what does the follow-up article prescribe?
- How to calibrate LLM-as-a-Judge against human eval so its scores are trustworthy?
- How to define "resolved" rigorously enough to bill on it (outcome-based pricing × Eval Plan)?

## Concepts Linked

- [[concepts/product-management/ai-prd|AI PRD]]
- [[concepts/ai-agents/prd-generation|PRD Generation]]
- [[concepts/ai-agents/product-evals|Product Evals]]
- [[concepts/ux-research/ai-evals|AI Evals]]
- [[concepts/ai-agents/spec-driven-development|Spec-Driven Development]]
- [[concepts/ai-agents/vibe-coding-agent-evaluation|Vibe-Coding Agent Evaluation]]
- [[concepts/product-management/tokenomics|Tokenomics]]

## LLM Use

- **Use for:** structuring an AI-feature PRD (the 8 items), designing an Eval Plan (test-case set + Eval pyramid + regression rule), arguing why pricing belongs in the PRD, and the deterministic-vs-non-deterministic framing.
- **Do not use for:** quoting exact figures/quotes as verbatim from the original (captured via summary); the deferred metric/monitoring specifics (not in this source).
- **Best prompt pattern:** "Draft an AI-feature PRD using the 8 items; for the Eval Plan, give 10 starter test-case rows (input / expected / fail) and assign each to rule-based, LLM-judge, or human eval; then propose a pricing model (usage / outcome / hybrid) consistent with the success metrics."

## Reliability Notes

> [!warning] Caveats
> - **Practitioner how-to**, captured via Bonny's Chinese summary (not verbatim). Confidence 0.8 on the framework (8 items, Eval pyramid, regression, pricing); exact numbers are illustrative; metric detail deferred by the author.

## Backfill Status

- Upgraded 2026-06-22 from a partial stub to a full ingest using Bonny's Chinese summary of the JS-rendered article. `coverage: partial → substantial`, `llm_ready: false → true`, `confidence: 0.5 → 0.8`. To reach `full`, re-capture the verbatim original (and the follow-up metrics article).
