---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [agent-experience, onboarding, mental-models, ax]
sources:
  - sources/pxd-story-ai-insights
  - sources/amershi-2019-human-ai-guidelines
confidence: 0.72
---

# Mental Model Onboarding

## Summary

Mental model onboarding is how an agent product teaches users what the agent can do, what it cannot, and how to get good results — building an accurate capability model before the user forms a wrong one from a bad first attempt.

## Why It Matters

Open-ended input is a discoverability dead end: a blank chat box communicates nothing about capability boundaries. Users who fail on their first realistic task rarely return to discover what would have worked.

## Key Claims

- Capability discovery beats capability listing: contextual suggested actions, worked examples, and templates teach more than a features page.
- First-task design is disproportionately important; route new users toward tasks with high success probability and visible value.
- Boundaries need teaching too: an agent that demonstrates honest "I can't do X, but I can do Y" early sets durable, accurate expectations.
- Mental models drift as models improve; onboarding is continuous (release notes in-context, "newly possible" prompts), not a one-time tour.
- For proactive agents, onboarding must also cover data use: what context the agent reads and how to control it.
- Amershi et al. open their guideline set with exactly this problem: make clear what the system can do (G1) and how well (G2), because over-promising damages perception of the whole service — see [[sources/amershi-2019-human-ai-guidelines|Amershi et al. 2019]].

## Related Concepts

- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/product-management/ai-product-onboarding|AI Product Onboarding]]
- [[concepts/ux-research/ax-ai-experience|AX (AI Experience)]]

## Conflicts & Caveats

- Overlaps with [[concepts/product-management/ai-product-onboarding|AI Product Onboarding]]; this note focuses on the mental-model formation mechanism rather than funnel design. Expectation-setting claims are grounded in Amershi et al. G1-G2; continuous-onboarding claims align with G14 and G18.

## Sources

- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019): Human-AI Guidelines]]
- [[sources/pxd-story-ai-insights|PXD: AI Insights]]

## Open Questions

- What is the most efficient way to measure a user's capability mental model accuracy in usability testing?
