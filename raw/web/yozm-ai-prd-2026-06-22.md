---
source_url: https://yozm.wishket.com/magazine/detail/3809/
captured: 2026-06-22
title: "AI PRD는 무엇이 달라야 하는가 (What should be different about an AI PRD)"
authors: [김영욱 (Kim Young-wook)]
published: 2026-06-18
publisher: 요즘IT / Yozm IT (Wishket)
---

# AI PRD는 무엇이 달라야 하는가 (What an AI PRD Must Do Differently)

**Author:** 김영욱 (Kim Young-wook / ywkim36) — Yozm IT, 2026-06-18.
**Capture status:** The article body is JavaScript-rendered (web_fetch returned only the shell). Content below was reconstructed 2026-06-22 from **Bonny's Chinese summary** (a digested rewrite, not the verbatim original); exact figures are the article's illustrative examples.

## Summary

Recipe analogy: mom's "a pinch of salt" (loose reference for someone who already cooks) = deterministic traditional PRD; a Michelin chef's "2.3g sea salt, 75°C for 4 min" (reproducible by anyone) = AI PRD. Traditional software is deterministic, so a PRD defining *what should happen* suffices. AI features are non-deterministic (same prompt → different answers), so an AI PRD must define **the range of acceptable answers** and **how to judge acceptability** — its new heart is the **Eval Plan**.

## Key Points

- AI PRD defines an acceptable-answer *range* + judgment method, not a single behavior (running example: Air Canada bereavement-discount chatbot).
- **Eval Plan** = the evaluation standard + tooling, written into the PRD; fundamentally a **test-case collection** (spreadsheet: input / expected / actual / score / pass-fail). Start 20–30 cases → ~200 over ~6 months.
- **Eval pyramid:** rule-based (fast, cheap, shallow) → LLM-as-a-Judge (fast/cheap, but bias/hallucination) → human eval (accurate, slow/expensive; needed for regression baselines). PM assigns each case a layer to control cost.
- **Regression testing** ends the "Prompt Swamp (프롬프트 수렁)" (fix A→break B): rerun the whole Eval set on every prompt change. Eval Plan in the PRD = a commitment to keep measuring post-launch.
- **8 required AI-PRD items:** (1) feature overview (AI must be *best* at the problem, not "AI for AI's sake"); (2) input/output spec; (3) system-prompt draft (sets the "personality"); (4) quality standard; (5) failure definition (hallucination / policy-violating promises / dangerous advice — Air Canada lacked this); (6) Eval Plan; (7) monitoring plan; (8) risks & limitations.
- **Pricing model belongs in the PRD** (every use = real token cost; flat SaaS pricing can blow up 10×). Three models: usage-based (OpenAI tokens), outcome-based (per resolved case — Zendesk/Intercom), hybrid (base + usage; most common). Pricing couples to product design (outcome pricing → outcome-centric success metrics; define "resolved" in the Eval Plan). Contrast: Salesforce Agentforce (Flex Credits, value↔price aligned) vs Adobe Firefly (unclear AI→profit, stock dropped).
- **PRD as promise:** traditional PRD promises "we'll build this"; AI PRD promises "how it behaves, how we judge it works, how we detect breakage, how we prevent cost blowup." Center = Eval Plan (turns "works well" from a feeling into a measurable standard). AI-era PM = defines feature behavior range *and* judgment standards → AI feature goes from "luck-based tech" to "manageable system."

## Follow-up

- Re-capture the verbatim original (and the author's promised follow-up on metrics/monitoring) to move the source page to `coverage: full`.
