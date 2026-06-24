---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [algorithmic-self, algorithmic-experience, user-agency, identity-oriented-representation, recommender-systems, hci, dis-2026, reflection, youtube]
source_path: raw/web/acm-dis2026-algorithmic-self-portraits-2026-06-22.md
source_url: https://dl.acm.org/doi/10.1145/3800645.3812910
authors: [Yeowon Lee, Youngseo Kim, Yousang Kwon, Kyungho Lee, Dajung Kim]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.85
---

# Lee et al. (2026): Is This the Real Me? — Algorithmic Self-Portraits (TubeLens)

**Authors:** Yeowon Lee, Youngseo Kim, Yousang Kwon, Kyungho Lee, Dajung Kim (Design Futures Lab / Expressive Computing Lab, Dept. of Design, UNIST, Republic of Korea)
**Venue:** DIS '26 — Designing Interactive Systems Conference, June 13–17 2026, Singapore (26 pages, CC BY-NC-ND 4.0)
**Raw capture:** [[raw/web/acm-dis2026-algorithmic-self-portraits-2026-06-22|acm-dis2026-algorithmic-self-portraits-2026-06-22]]
**PDF:** `raw/files/lee-2026-tubelens-algorithmic-self-portraits-dis2026.pdf`
**DOI:** [10.1145/3800645.3812910](https://dl.acm.org/doi/10.1145/3800645.3812910)

> [!note] Upgraded from partial
> Originally a partial stub with an unverified title (ACM anti-bot wall). Bonny supplied the PDF on 2026-06-22; title, authors, abstract, and method are now confirmed from the source.

## Citation

Lee, Y., Kim, Y., Kwon, Y., Lee, K., & Kim, D. (2026). *Is this the real me?: Investigating algorithmic self-portraits as a medium for critical reflection on algorithmic experiences on YouTube.* In Proceedings of the 2026 Designing Interactive Systems Conference (DIS '26). ACM. https://doi.org/10.1145/3800645.3812910. PDF preserved at `raw/files/lee-2026-tubelens-algorithmic-self-portraits-dis2026.pdf`.

## Summary

An HCI design-research paper presenting **TubeLens**, a research probe that turns a user's YouTube watch history into an **algorithmic self-portrait** — a collage of persona-style *algorithmic trait keywords* (e.g., "Family Hugger"), thumbnail images sized by viewing proportion, trait explanations, and a playful animal-persona "algorithmic nickname." The goal is to shift algorithmic reflection from *controlling individual recommendations* to *interpreting algorithmic influence on one's identity*. It is grounded in three self-concepts — **Perceived / Algorithmic / Desired self** (Self-Discrepancy Theory) — and a critique that recommender systems are **recursive, reductive, and invisible**. An exploratory deployment study with **22 participants** (plus an 8-person preliminary study) found the portraits surface gaps between perceived and algorithmic selves and support self-/agentic awareness, while raising tensions around privacy and social comparison.

## Key Claims

- **Identity-oriented representation** of an algorithmic profile (vs operational controls like hiding videos) opens reflection at the level of interests, values, and identity.
- Recommendation algorithms carry three risks: **recursive** (feedback loops reinforce past behavior → filter bubbles), **reductive** (identity collapsed to behavioral labels), **invisible** (black-box inference limits reflection/autonomy).
- The **algorithmic self-portrait** positions users as active agents who can question/negotiate their inferred identity rather than passively receive recommendations.
- **Findings:** portraits surface perceived-vs-algorithmic gaps; support self-awareness and "agentic awareness"; engaging with *others'* portraits enables exploring alternative interests/trajectories; but produce tensions — privacy, social comparison, and ambiguity/opacity of trait-based representation.
- Prior explainability / controllability / transparency approaches keep users at the operational level and inside the system's own categories; this work asks what profiling *means* to the user.
- **Three contributions:** the TubeLens / algorithmic-self-portrait concept; empirical findings on interpretation and reflection; the potential + limitations of the identity-oriented approach with design insights for future identity-oriented interfaces.

## Useful Examples

- **The algorithmic self-portrait** (trait-keyword + thumbnail collage + animal-persona nickname) as a concrete artifact for making algorithmic profiling tangible and reflectable.
- **LLM-supported generative pipeline (GPT-3):** Google Takeout history → de-identified metadata (raw history not stored) → per-video keyword extraction (topic/type/emotional tone/target/trend) → semantic clustering → persona trait keywords + explanations → thumbnail mapping → nickname.
- **Design choices as findings:** persona-based labels beat category labels; real thumbnails beat abstract stock imagery; user customization was *intentionally constrained* to preserve the portrait's authenticity as a system output.
- **Spotify year-end "taste summaries"** cited as a real-world identity-oriented representation that prompts reflection.

## Constraints / Caveats

- **Coverage substantial, not full:** the abstract, framing, related work, and system/pipeline design were extracted; the detailed Findings, Discussion, and Limitations sections (full study results) were not transcribed in depth — read the PDF for specifics before citing results.
- **Exploratory, small-N, single platform/culture:** 22 participants (preliminary study 8, Korean), YouTube only; findings are qualitative and "initial insights," not generalizable effect sizes.
- **LLM-generated self (GPT-3):** the portrait is itself a model's interpretation, not the platform's actual recommender state — a second-order representation.
- Peer-reviewed conference paper (DIS '26) — high credibility for the design contribution and qualitative findings; not a quantitative evaluation.

## Design Implications

- For **AX / algorithmic-experience** work: an identity-oriented representation is a design lever distinct from explainability/control — useful when the goal is reflection and agency, not optimization.
- Surface the **gap between perceived and algorithmic selves** as a feature, not a bug; do not assume "closing the gap" is the goal.
- Budget for **privacy and social-comparison safeguards** (anonymized exploration, opt-in disclosure, controlled detail) when showing inferred traits — the study had to add these.
- Relevant to [[concepts/agent-experience/agent-transparency|agent transparency]] and [[concepts/product-management/geo-generative-engine-optimization|GEO]]: how systems represent their inference of a user shapes trust and behavior.

## Tensions

- **Reflection vs harm:** making the algorithmic self tangible can reinforce a reductive label or trigger social comparison/anxiety — the intervention cuts both ways.
- **Authenticity vs control:** constraining customization preserves the portrait's "given output" authenticity but limits user agency over the representation.
- **Tangibility via LLM vs fidelity:** an LLM-generated portrait is interpretable and engaging but is not the platform's real model — readability traded against accuracy.

## Open Questions

- When does surfacing the algorithmic self increase agency vs entrench a reductive identity?
- Do reflective encounters change downstream algorithmic *behavior*, or only awareness?
- How do identity-oriented representations scale beyond YouTube and beyond a 22-person exploratory study?

## Concepts Linked

- [[concepts/ux-research/algorithmic-self|Algorithmic Self]] (new)
- [[concepts/ux-research/ax-ai-experience|AX (AI / Algorithmic Experience)]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- [[concepts/ux-research/progressive-user-control|Progressive User Control]]
- [[concepts/ux-research/ai-persona-replication|AI Persona Replication]]
- [[concepts/ux-research/generative-ui|Generative UI]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/product-management/geo-generative-engine-optimization|Generative Engine Optimization]]

## LLM Use

- **Use for:** designing identity-oriented / reflective representations of algorithmic profiles; framing the recursive/reductive/invisible risks of recommenders; the Perceived/Algorithmic/Desired self lens; privacy and social-comparison considerations for showing inferred traits.
- **Do not use for:** quantitative claims (qualitative exploratory study); generalizing beyond YouTube / the 22-person sample; citing detailed findings not captured here (read the PDF).
- **Best prompt pattern:** "Using Lee et al.'s algorithmic-self-portrait approach, design an identity-oriented representation of how [system] profiles a user that supports reflection and agency, and enumerate the privacy / social-comparison / reductiveness risks to mitigate."

## Reliability Notes

> [!warning] Caveats
> - **Peer-reviewed DIS '26 paper**, primary source (PDF preserved). Confidence 0.85: high for the design contribution, framing, and qualitative findings; the full results detail is not yet transcribed (`coverage: substantial`, not `full`).
> - Exploratory, small-N, single-platform, LLM(GPT-3)-mediated — treat findings as initial insights.

## Backfill Status

- Upgraded 2026-06-22 from a partial/unverified stub to a full ingest using Bonny-supplied PDF (preserved in `raw/files/`). Title/authors/abstract/method confirmed. `coverage: partial → substantial`, `llm_ready: false → true`, `confidence: 0.3 → 0.85`. Deepen the Findings/Discussion sections on demand for `coverage: full`.
