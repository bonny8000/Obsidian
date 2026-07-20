---
type: concept
status: active
created: 2026-07-07
updated: 2026-07-07
tags: [concept, explainable-ai, xai, human-computer-interaction, trust, design-patterns]
sources: [hbs-working-knowledge-ai-advice-willful-blindness]
confidence: 0.85
---

# Explainable AI

> [!abstract] Summary
> A subfield of AI and design focused on making the inner logic, risk factors, and decision criteria of machine learning models transparent and understandable to human operators, as opposed to black-box decision systems.

> [!important] Why it Matters
> As AI is deployed in high-stakes areas like lending, hiring, medicine, and judicial systems, explainability is essential for ensuring fairness, detecting bias, and complying with legal mandates. However, XAI must be designed to overcome human cognitive limitations, such as offloading, over-reliance, and willful blindness.

## 📝 Key Claims
- **Explanations promote critical reasoning:** When human operators actively engage with AI explanations, they are statistically more likely to challenge the recommendations and perform necessary overrides (e.g., 6% higher override rate in HBS loan approval experiments).
- **Legally mandated in high-stakes settings:** Frameworks like the EU AI Act, GDPR, and US CFPB regulations require specific disclosures explaining automated adverse decisions (e.g., credit denials).
- **Explanation design dictates engagement:** Passively presenting a list of features or weights (checkbox transparency) is often bypassed. Design must actively scaffold user comprehension.

## 🔗 Related Concepts
- [[wiki/concepts/agent-experience/willful-blindness|Willful Blindness]]
- [[wiki/concepts/agent-experience/checkbox-transparency|Checkbox Transparency]]
- [[wiki/concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[wiki/concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]]

## ⚖️ Conflicts & Caveats
> [!warning] Cognitive Overload and Offloading
> Complex explanations can lead to user fatigue, causing operators to blindly agree to recommendations. Alternatively, if explanations are always convincing, they can induce over-trust. XAI must calibrate user skepticism rather than just explaining choices.

## 📚 Sources
- [[sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan (2026): When AI Gives Advice, Employees Rarely Ask Why]]

## ❓ Open Questions
- What visualization formats (e.g., natural language summaries, counterfactual examples, or feature highlights) lead to the best human trust calibration?
- How can we design explanation interfaces that automatically adapt to different user expertise levels?
---
