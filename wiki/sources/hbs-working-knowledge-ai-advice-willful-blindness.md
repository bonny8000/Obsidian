---
type: source
status: active
created: 2026-07-07
updated: 2026-07-07
tags: [explainable-ai, willful-blindness, checkbox-transparency, human-in-the-loop, trust-calibration, behavioral-experiment, hbs]
source_path: raw/web/hbs-working-knowledge-ai-advice-employees-2026-07-07.md
source_url: https://www.library.hbs.edu/working-knowledge/when-ai-gives-advice-employees-rarely-ask-why
authors: [Alex Chan]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# When AI Gives Advice, Employees Rarely Ask Why
**Author:** Alex Chan (Harvard Business School) — **Published:** 2026 — HBS Working Knowledge
**Raw capture:** [[raw/web/hbs-working-knowledge-ai-advice-employees-2026-07-07|hbs-working-knowledge-ai-advice-employees-2026-07-07]]
**URL:** [library.hbs.edu/working-knowledge/when-ai-gives-advice-employees-rarely-ask-why](https://www.library.hbs.edu/working-knowledge/when-ai-gives-advice-employees-rarely-ask-why)

## Citation

Chan, A. (2026, February). *Preference for Explanations: Case of Explainable AI.* Harvard Business School Working Knowledge. Written by HBS Editorial based on Alex Chan's working paper. Captured 2026-07-07 into `raw/web/hbs-working-knowledge-ai-advice-employees-2026-07-07.md`. 

## Summary

The article presents the results of an empirical behavioral study conducted by Harvard Business School Assistant Professor Alex Chan with 2,512 participants acting as loan officers. The study investigated how humans interact with Explainable AI (XAI) predictions and explanations in a high-stakes decision context (loan approvals). The findings challenge the assumption that people naturally want transparency. Instead, participants frequently engaged in active information-avoidance ("willful blindness"), choosing to follow AI recommendations without looking at the explanations—especially when they had financial incentives tied to outcomes (loan repayment bonuses) or when they suspected the AI's explanation might reveal moral discomfort (bias based on race/gender).

## Key Claims

- **Humans are not perfectly rational Bayesian agents in AI interaction:** They behave strategically and are often "willfully ignorant" to avoid moral discomfort or decision-making friction.
- **High demand for advice, low demand for explanations:** 80% of participants wanted to see the AI's risk predictions, but only 46% chose to view the explanations behind those predictions.
- **Financial incentives reduce the desire for transparency:** When compensation depended on loan repayment (outcome-based incentives), participants were nearly 20% more likely to decline viewing explanations compared to flat-fee participants.
- **Potential bias drives information avoidance:** When warned that an explanation might indicate demographic bias (race or gender), explanation avoidance rose by an additional 10+ percentage points (up to 23%).
- **Viewing explanations increases critical engagement and overrides:** Participants who viewed explanations were 6 percentage points more likely to override the AI's recommendations, showing that explanations do drive critical reasoning when actually processed.
- **"Checkbox transparency" fails in practice:** Providing access to explanations is insufficient because individual incentives often align toward willful blindness. Explainability must be built into organizational structures, training, and incentive designs.
- **Devaluation of human judgment:** Deploying AI without forcing users to examine reasoning risks "training people to stop asking why."

## Useful Examples

- **The Loan Officer Bonus Dilemma:** A loan officer accepts an AI's "high risk" classification of a minority applicant because rejecting the applicant ensures loan repayment and preserves the officer's bonus. The officer actively avoids clicking the "View Explanation" button to avoid learning that the AI used race/gender as a primary risk predictor, which would create a moral conflict and force an override.

## Constraints / Caveats

- **Simulated Loan-Approval Setting:** The study was conducted online with 2,512 participants in a controlled experimental environment. Real-world corporate accountability, compliance audits, and legal liabilities might alter loan officer behavior.
- **Simple Explanation Model:** The paper uses standard risk-factor lists. More interactive, conversational, or visual explanation models were not tested.

## Design Implications

- **Enforce mandatory explanation review gates:** For high-stakes decisions (hiring, credit, medical), do not make viewing AI explanations optional. Embed explanation review as a required step in the UX flow.
- **Avoid "Checkbox Transparency" UI:** Design interfaces that require active cognitive engagement with the explanation (e.g., matching the explanation factors to a checklist or writing a brief justification for accepting/rejecting the AI's logic).
- **Decouple incentive models from blind AI compliance:** Align organizational incentives so that employees are rewarded for critical audit behavior and appropriate overrides, rather than just outcome metrics that encourage blind algorithmic adherence.

## Tensions

- **Efficiency vs. Ethical Oversight:** Forcing users to review explanations increases decision latency and cognitive load, directly opposing the "productivity and speed" goals driving corporate AI adoption.
- **Outcome-based incentives vs. Process-based compliance:** Rewarding employees purely on outcomes (e.g., loan repayments, hiring retention) encourages them to offload liability to the AI and avoid looking at biased mechanisms.

## Open Questions

- What UX patterns best encourage critical engagement with explanations without causing user fatigue?
- How do legal frameworks (like the EU AI Act or GDPR) enforce actual explanation review rather than simple disclosure?
- How can organizations mathematically model the cost of "willful blindness" in their risk management frameworks?

## Concepts Linked

- [[wiki/concepts/agent-experience/willful-blindness|Willful Blindness]] (new) — active avoidance of information or explanations to escape moral conflict or operational friction.
- [[wiki/concepts/agent-experience/checkbox-transparency|Checkbox Transparency]] (new) — superficial transparency where explanations are available but ignored due to misaligned incentives.
- [[wiki/concepts/ux-research/explainable-ai|Explainable AI (XAI)]] (new) — tools and design paradigms aimed at making AI reasoning transparent to human operators.
- [[wiki/concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] (existing) — human review gates, which are shown to be vulnerable to cognitive offloading and willful blindness.
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]] (existing) — calibrating trust so that operators override AI recommendations when appropriate.

## LLM Use

- **Use for:** Designing UX flows for high-stakes decision tools; building human-in-the-loop audit gates; structuring compliance workflows under explainability regulations.
- **Do not use for:** Modeling employee behavior where strict, audited compliance checks are actively enforced (which would override voluntary information avoidance).

## Reliability Notes

> [!note] Methodological Rigor
> - **High experimental control.** The study uses a large, randomized sample (n=2,512) and isolates the effect of financial incentives and bias warnings. Confidence **0.90** on the behavioral findings regarding information avoidance and incentive-driven compliance.

## Backfill Status

- Written 2026-07-07 from HBS Working Knowledge summary. `coverage: substantial` (covers experimental setup, quantitative results, and organizational recommendations).
