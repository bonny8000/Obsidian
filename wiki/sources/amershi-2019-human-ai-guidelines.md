---
type: source
status: active
created: 2026-06-12
tags: [source, paper, human-ai-interaction, guidelines, agent-experience]
sources: []
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.92
---

# Amershi et al. (2019): Guidelines for Human-AI Interaction

> [!info] Metadata
> - **Author:** Saleema Amershi, Daniel Weld, Mihaela Vorvoreanu, et al. (Microsoft Research)
> - **Date:** CHI 2019
> - **Type:** paper + practitioner toolkit (HAX), ~1,400 citations
> - **Raw File:** [[raw/web/amershi-2019-human-ai-guidelines]]

## Citation

Amershi, S., Weld, D., Vorvoreanu, M., et al. (2019). Guidelines for Human-AI Interaction. CHI 2019. DOI 10.1145/3290605.3300233. Captured 2026-06-12 from ACM abstract plus the Microsoft Design announcement and HAX Toolkit materials.

## Summary

18 validated design guidelines for AI products, synthesized from 150+ recommendations across two decades and tested with 49 practitioners against 20 real AI products. Organized by interaction phase: initially, during interaction, when wrong, and over time. The most directly actionable of the three foundational AX sources — closer to a design checklist than a theory.

## Key Claims

- Classic guidelines like consistency break for AI components that learn and change; AI products need phase-specific guidance.
- Initially (G1-G2): set capability and quality expectations up front; over-promising damages perception of the whole service.
- During interaction (G3-G6): time services to the user's context, surface contextually relevant information, fit social norms, mitigate biases.
- When wrong (G7-G11): cheap invocation, cheap dismissal, cheap correction; scope down or ask when uncertain; explain why the system acted.
- Over time (G12-G18): remember recent interactions, learn from behavior, change cautiously, invite granular feedback, convey consequences, give global controls, announce changes.
- Guidelines were validated as observable at the UI level — usable as heuristic-evaluation criteria, not just design intentions.

## Useful Examples

- The four-phase structure doubles as an audit rubric: walk any agent feature through initially / during / when-wrong / over-time and score guideline coverage.
- "When wrong" phase (G7-G11) is effectively a specification for [[concepts/agent-experience/error-recovery|Error Recovery]].

## Constraints / Caveats

- Validated on 2019-era AI-infused products (recommenders, autocomplete, navigation); coverage of autonomous long-horizon agents and generative UI is an open transfer question.
- Guideline phrasing here is paraphrased; consult the HAX Toolkit for canonical wording and per-guideline patterns.

## Design Implications

- Use as the default heuristic set for agent-feature design reviews and expert evaluations.
- Map every proactive feature against G3 (timing), G8 (dismissal), G10 (scope when uncertain), and G11 (explain why) before shipping.
- Treat G12-G18 as the requirements spine for agent memory UX.

## Tensions

- G13 (learn from behavior) and G14 (update cautiously) are in deliberate tension; the pair encodes the stability-adaptation tradeoff.

## Open Questions

- Which guidelines need extension for multi-step autonomous agents — e.g., does "explain why" scale to 40-step tool-use chains?

## Concepts Linked

- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/error-recovery|Error Recovery]]
- [[concepts/agent-experience/mental-model-onboarding|Mental Model Onboarding]]
- [[concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]

## LLM Use

- **Use for:** heuristic evaluation criteria for AI/agent features, design-review checklists, grounding onboarding and error-recovery claims.
- **Do not use for:** canonical guideline wording (paraphrased here) — link to HAX Toolkit for exact text.
- **Best prompt pattern:** Ask the LLM to audit a specific agent flow against the four phases and report which guidelines are violated with evidence.

## Reliability Notes

> [!warning] Caveats
> Rigorously validated and industry-standard, but pre-generative-agent. Strongest evidence among the three foundational AX sources.

## Backfill Status

- Standard coverage from announcement and toolkit; promote with full paper PDF if needed.
