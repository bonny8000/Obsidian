---
source_url: https://pxdstory.tistory.com/m/1911
captured: 2026-07-31
title: "AI 라이팅 어시스턴트, Writone 개선기"
title_en: "AI Writing Assistant, Writone: An Improvement Log"
authors: [Yejin.lee]
published: 2026-07-30
publisher: pxd story (pxd, Korean UX consultancy)
language: ko
format: product improvement case study
---

# AI Writing Assistant, Writone — pxd story

**Author:** Yejin.lee (pxd) · **Published:** 2026-07-30 · **Captured:** 2026-07-31
Category: pxd AI툴 이야기 (pxd AI tool stories)

AI-written extraction. No full-text reproduction; short quoted phrases only.

---

## Framing

A follow-up to a **September 2024** experiment on AI tools for UX Writing — roughly a 7-month arc to the state described here. The governing question changed:

- Before: *"Can AI learn a company's guidelines?"*
- Now: **"AI Writing 어시스턴트가 실제로 쓰이려면, 사용자의 경험 중 어디에 있어야 하는가?"** — *"For an AI writing assistant to actually get used, where in the user's experience must it live?"*

## Problem

Companies invest heavily in UX Writing guidelines, and the guidelines then lie dormant as PDFs in cloud storage. Designers and planners under deadline cannot work through hundred-page (the piece also says "thousands of pages" in its opening) documents.

The research finding that reframed the product: UX designers work in a continuous flow — planning → Figma → inserting text → review → revision — and the guideline check happens **inside Figma**, not as a separate act. The existing path requires leaving Figma, opening a PDF, finding the rule, and returning. That switching cost is what makes practitioners abandon the check.

> "UX Writing 검토의 필요성은 인지하지만, 그것을 위해 흐름을 끊는 전환 비용이 너무 크다."
> *"They recognize the need for UX Writing review, but the switching cost of breaking flow for it is too large."*

## Solution 1 — Figma plugin rather than a web app

Chosen deliberately over a web version:

- Removes the workflow interruption entirely.
- The AI can read **layer node information**, giving it context for corrections.
- The AI can distinguish **UI element types** (button vs. toast message) and apply component-specific rules.

> "기술이 아닌 사람의 흐름에서 출발했기 때문에, 제품이 있어야 할 자리가 자연스럽게 결정되었다."
> *"Because we started from the human workflow rather than the technology, the product's proper place was decided naturally."*

## Solution 2 — Hierarchical rule structure

Applied **Aaron Walter's hierarchy of user needs** to structure the rules as a hierarchy rather than a flat list, so the AI can understand relationships between rules and practitioners can grasp the logic of a correction.

Four levels:

| Level | Scope | Example given |
| --- | --- | --- |
| 1 | **Terminology** — consistency foundation (banned term → recommended term) | '익월' → '다음 달'; '당사' → 'OO증권' |
| 2 | **UI rules** — component-specific | buttons concise (noun-form ending); tooltips may explain at length |
| 3 | **Grammar** — structure, formatting, tone consistency | path notation unified as '→' |
| 4 | **Principles / tone** — brand philosophy | clarity, brevity, user-centricity |

## Solution 3 — Rule-based RAG

Moved from similarity-based search to a **Rule-based RAG** architecture: the AI autonomously extracts abstract rules from the PDF (e.g. "경로 표기는 '→'로 통일한다" — *"unify path notation as '→'"*) and matches them contextually to the user's input, so a correction can be justified rather than merely suggested.

## Solution 4 — Three principles for trust

1. **Transparency** — show the guideline source and principle page reference for every correction.
2. **Explainability** — state the reason for the correction in understandable language, not algorithmic terms. Cites the **McKinsey 2024 AI survey** identifying explainability as a major enterprise AI adoption risk.
3. **Human control** — AI proposes; the human decides the final text. Named as the counter to **automation bias**, the risk of uncritically accepting AI suggestions.

> "AI는 선택지를 제시하고, 판단은 사람이 합니다."
> *"AI presents the options; the judgment is made by a person."*

## Conclusion

Writone is positioned as "the smartest assistant" rather than an autonomous decision-maker. Practitioners keep professional judgment, and guidelines become **"살아 움직이는"** — living, moving — resources at the practitioner's fingertips rather than dormant documents.

## Limitations and caveats (as observed in the text)

- **No quantitative results of any kind.** No adoption figures, no accuracy or precision measurement, no before/after comparison of guideline-compliance rates, no time saved.
- **No failure cases described.** The piece states no scope limits for Writone and reports nothing that did not work.
- **Rule-extraction reliability unexplained** — how faithfully abstract rules are pulled from a PDF is asserted, not evidenced.
- **First-party account** by the building consultancy, on its own blog; Writone is pxd's product.
- **Korean-language context throughout**; generalization to other languages is not discussed.
- **The Aaron Walter hierarchy is used by analogy.** It is a model of user needs, not of rule precedence; the transfer is asserted rather than validated.
- **The McKinsey citation is second-hand** — survey year given, no page, sample, or question wording.
- No cost, pricing, or competitive comparison.
