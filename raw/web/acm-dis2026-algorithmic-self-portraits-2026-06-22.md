---
source_url: https://dl.acm.org/doi/10.1145/3800645.3812910
captured: 2026-06-22
title: "Is This the Real Me?: Investigating Algorithmic Self-Portraits as a Medium for Critical Reflection on Algorithmic Experiences on YouTube"
authors: [Yeowon Lee, Youngseo Kim, Yousang Kwon, Kyungho Lee, Dajung Kim]
published: 2026-06-13
publisher: ACM — Proceedings of the 2026 Designing Interactive Systems Conference (DIS '26)
---

# Is This the Real Me? — Algorithmic Self-Portraits (TubeLens), DIS '26

**Authors:** Yeowon Lee, Youngseo Kim, Yousang Kwon, Kyungho Lee, Dajung Kim — Design Futures Lab / Expressive Computing Lab, Department of Design, Ulsan National Institute of Science and Technology (UNIST), Republic of Korea
**Venue:** DIS '26 (Designing Interactive Systems Conference), June 13–17 2026, Singapore. 26 pages. CC BY-NC-ND 4.0.
**DOI:** 10.1145/3800645.3812910
**PDF preserved:** `raw/files/lee-2026-tubelens-algorithmic-self-portraits-dis2026.pdf` (supplied by Bonny 2026-06-22; replaces the earlier unverified stub).

## Abstract (as published)

"In this paper, we present TubeLens, a system designed to support YouTube users in reflecting on how recommendation algorithms perceive and represent their interests. TubeLens invites users to engage with their algorithmic selves through self-portraits accompanied by dispositional keywords and explanations, creating space to consider how algorithmic experiences might be interpreted and potentially reshaped over time. Rather than positioning users as passive recipients of recommendations, TubeLens foregrounds users' agency in questioning and making sense of algorithmic influence on their media consumption. We conducted an exploratory user study with 22 participants to examine users' experiences with TubeLens. Our findings suggest that algorithmic self-portraits can surface gaps between perceived and algorithmic selves, supporting self-awareness and agentic awareness, while also revealing tensions around privacy and social comparison. This work offers initial insights into how interactive representations of algorithmic profiles can support reflective engagement with algorithmic systems and inform the design of future identity-oriented interfaces."

Keywords: Algorithmic Self, Algorithmic Experience, User Agency, Identity-Oriented Representation.

## Summary

A design-research (HCI) paper introducing **TubeLens**, a research probe that turns a user's YouTube watch history into an **"algorithmic self-portrait"** — a collage of persona-style *algorithmic trait keywords* (e.g., "Family Hugger," "Curious Traveler"), representative thumbnail images sized by viewing proportion, trait explanations, and a playful animal-persona "algorithmic nickname." The aim is to shift algorithmic reflection from controlling individual recommendations to interpreting algorithmic influence at the level of *identity*. Grounded in three self-concepts (Perceived / Algorithmic / Desired self; Self-Discrepancy Theory) and a critique that recommender systems are **recursive, reductive, and invisible.** An exploratory deployment study with 22 participants (plus an 8-person preliminary study) examined RQ1 (how users perceive/interpret/respond to identity-oriented representations of their profile) and RQ2 (how such representation works as a reflective medium).

## Key Points

- **Algorithmic Self** = the identity inferred by a platform from digital traces; TubeLens reifies it as a tangible, negotiable portrait rather than a fixed system output.
- Positions users as **active agents** questioning/challenging their algorithmic self; "agentic awareness" alongside self-awareness.
- **Generative pipeline (LLM-supported, GPT-3):** Google Takeout watch history → de-identified metadata (raw history not stored) → (1) per-video keyword extraction (topic, type, emotional tone, target, trend) → (2) semantic clustering → (3) persona trait keywords + explanations → (4) thumbnail image mapping → algorithmic nickname.
- Design choices: persona-based > category-based labels; real YouTube thumbnails > abstract stock images; *intentionally constrained* user customization to preserve the portrait's "authenticity" as a system output.
- **Findings (high level):** portraits surface gaps between perceived and algorithmic selves; support reflection on interests/values/identity; engaging with *others'* portraits opens exploration of alternative interests; but raise **tensions** — privacy, social comparison, and ambiguity/opacity of trait-based representation.
- Three stated contributions: (1) the TubeLens / algorithmic-self-portrait concept; (2) empirical findings on interpretation and reflection; (3) potential + limitations of the identity-oriented approach and design insights for future identity-oriented interfaces.
- Prior approaches (explainability, controllability, transparency) keep users at the operational level and inside the system's categories; this work asks what the profiling *means* to the user.

## Capture scope

Extracted from the PDF: title, authors, abstract, introduction, related work (algorithmic recommendation risks; explainability/controllability/transparency; visual/textual data representations; self-concepts), and the TubeLens system design + generative pipeline (≈ first third). The full Findings, Discussion, and Limitations sections (study results in depth) were not transcribed in detail.
