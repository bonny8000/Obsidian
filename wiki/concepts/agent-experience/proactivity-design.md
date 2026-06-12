---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [agent-experience, proactivity, ax, interaction-design]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/pxd-story-ai-insights
  - sources/horvitz-1999-mixed-initiative
  - sources/amershi-2019-human-ai-guidelines
confidence: 0.78
---

# Proactivity Design

## Summary

Proactivity design defines when, how, and with what justification an agent initiates action or communication without an explicit user request. It is the dimension that separates a reactive chatbot from a proactive service agent.

## Why It Matters

Proactivity is the highest-leverage and highest-risk AX dimension: well-timed initiative feels like service, mistimed initiative feels like spam or surveillance. Most agent products fail here before they fail on capability.

## Key Claims

- Proactivity has at least four levels: silent observation, ambient suggestion, explicit proposal requiring confirmation, and autonomous action with after-the-fact reporting.
- The right level depends on three variables: confidence in the inference, cost of being wrong, and reversibility of the action.
- Proactive value is strongest when grounded in context no external system can replicate (e.g., first-party purchase history, device telemetry) — context advantage is the moat, the trigger logic is the craft.
- Every proactive touch spends attention budget; users tolerate few false positives before disabling the feature entirely.
- Proactive moments need a visible "why am I seeing this" justification to maintain [[concepts/agent-experience/trust-calibration|calibrated trust]].
- Horvitz frames the act/don't-act decision as expected utility: value if right, weighed against cost of error and cost of interruption — a gate every proactive trigger should pass — see [[sources/horvitz-1999-mixed-initiative|Horvitz 1999]].

## Design Levers

- Trigger: what signal initiates the agent (event, threshold, schedule, inferred intent)
- Timing: immediate vs. batched vs. waiting for a natural pause
- Channel: in-context surface vs. notification vs. digest
- Framing: suggestion ("you might want…") vs. report ("I did…") vs. question ("should I…?")
- Exit: one-tap dismiss, snooze, and per-category opt-out

## Related Concepts

- [[concepts/ux-research/ax-ai-experience|AX (AI Experience)]]
- [[concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/ux-research/progressive-user-control|Progressive User Control]]
- [[concepts/ux-research/haic-modalities-taxonomy|HAIC Modalities Taxonomy]]

## Conflicts & Caveats

- Core framework now grounded in Horvitz's decision-theoretic initiative model and Amershi et al.'s context guidelines (G3, G10); domain-specific thresholds (e.g., false-positive tolerance) remain unvalidated hypotheses.

## Sources

- [[sources/horvitz-1999-mixed-initiative|Horvitz (1999): Mixed-Initiative User Interfaces]]
- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019): Human-AI Guidelines]]
- [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework]]
- [[sources/pxd-story-ai-insights|PXD: AI Insights]]

## Open Questions

- What false-positive rate makes users disable proactive suggestions, and does it differ by domain (commerce vs. device health vs. content)?
- How should proactivity level adapt over time as the agent earns or loses trust?
