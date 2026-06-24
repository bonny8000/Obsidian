---
type: concept
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [concept, algorithmic-self, algorithmic-experience, user-agency, identity-oriented-representation, recommender-systems, reflection]
sources: [acm-dis2026-algorithmic-self-portraits]
confidence: 0.85
---

# Algorithmic Self

> [!abstract] Summary
> The identity a platform infers about a user from their accumulated digital traces (an "algorithmic profile"), and the design approach of representing that inferred identity back to users — as an *identity-oriented representation* — so they can interpret, question, and reflect on it rather than passively receive it.

> [!important] Why it Matters
> Recommendation algorithms are **recursive** (feedback loops reinforce past behavior), **reductive** (rich identity collapsed to behavioral labels), and **invisible** (black-box inference). Most engagement with them stays at the operational level (hide a video, tweak preferences). Surfacing the *algorithmic self* shifts reflection from individual recommendation outcomes to the cumulative influence on one's identity — supporting self-awareness, "agentic awareness," and genuine user agency.

## 📝 Key Claims
- Three self-concepts frame the reflection (from Self-Discrepancy Theory): the **Perceived Self** (how you see yourself), the **Algorithmic Self** (the identity platforms infer), and the **Desired Self** (who you aspire to be). The goal is not to *close* the gap but to make it visible and reflectable.
- An identity-oriented representation (e.g., an "algorithmic self-portrait" of trait keywords, images, and explanations) can surface gaps between the perceived and algorithmic selves and position the user as an active agent who can question or negotiate it.
- Tensions to design around: **privacy** (exposing inferred traits), **social comparison** (when viewing others' algorithmic selves), and the **ambiguity/opacity** of trait-based representations.
- Distinct from transparency/controllability/explainability approaches, which keep users inside the system's categories; an identity-oriented approach asks what the profiling *means* to the user.

## 🔗 Related Concepts
- [[concepts/ux-research/ax-ai-experience|AX (AI / Algorithmic Experience)]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- [[concepts/ux-research/progressive-user-control|Progressive User Control]]
- [[concepts/ux-research/ai-persona-replication|AI Persona Replication]]
- [[concepts/ux-research/generative-ui|Generative UI]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Making the algorithmic self tangible can itself cause harm (social comparison, anxiety, or reifying a reductive label as "true"). The study also uses an LLM (GPT-3) to generate trait keywords, so the "algorithmic self" shown is itself a second-order interpretation, not the platform's actual model.

## 📚 Sources
- [[sources/acm-dis2026-algorithmic-self-portraits|Lee et al. (2026): Algorithmic Self-Portraits (TubeLens), DIS '26]]

## ❓ Open Questions
- When does surfacing the algorithmic self support agency vs reinforce a reductive identity?
- How should identity-oriented representations handle privacy and social comparison safely?
- Does reflection actually change downstream algorithmic behavior, or only awareness?
