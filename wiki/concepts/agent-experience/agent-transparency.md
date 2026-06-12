---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [agent-experience, transparency, explainability, ax]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/amershi-2019-human-ai-guidelines
  - sources/lee-see-2004-trust-in-automation
confidence: 0.75
---

# Agent Transparency

## Summary

Agent transparency is the practice of making an agent's reasoning, data use, capabilities, and limits legible to the user at the right granularity — enough to support verification and trust, not so much that it becomes noise.

## Why It Matters

Probabilistic systems break the predictability assumptions of traditional UI. Users cannot form a working mental model of an agent unless the interface exposes what it considered, what it did, and what it cannot do.

## Key Claims

- Transparency operates at three layers: capability (what the agent can do), process (what it is doing now and why), and provenance (what evidence an output rests on).
- Full reasoning traces are rarely the right default; progressive disclosure (summary by default, detail on demand) preserves both legibility and flow.
- "Why am I seeing this" explanations matter most at proactive moments, where the agent acted without being asked.
- Transparency about data use (which personal context the agent read) is a trust and privacy requirement, not just a UX nicety.
- Honest capability boundaries ("I can't access X") outperform vague deflection in long-run trust.
- Lee & See's purpose/process/performance dimensions give the three-layer structure its empirical basis: users build trust from why the system exists, how it works, and its track record — see [[sources/lee-see-2004-trust-in-automation|Lee & See 2004]].

## Related Concepts

- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/mental-model-onboarding|Mental Model Onboarding]]
- [[concepts/ux-research/ax-ai-experience|AX (AI Experience)]]

## Conflicts & Caveats

- Tension exists between transparency and cognitive load; more explanation is not always better. Amershi et al.'s G11 (explain why the system acted) and Lee & See's purpose/process/performance dimensions now ground the framework, though both predate long-horizon generative agents.

## Sources

- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019): Human-AI Guidelines]]
- [[sources/lee-see-2004-trust-in-automation|Lee & See (2004): Trust in Automation]]
- [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework]]

## Open Questions

- What is the minimum process visibility users need during long-horizon agent tasks to stay comfortable without babysitting the agent?
- Does provenance display change decisions, or only confidence?
