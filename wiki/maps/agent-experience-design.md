---
type: map
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [map, agent-experience, ax, ux-design, ux-research]
sources:
  - sources/lee-see-2004-trust-in-automation
  - sources/horvitz-1999-mixed-initiative
  - sources/amershi-2019-human-ai-guidelines
  - sources/andru-saksena-adobe-haic-2025
  - sources/pxd-story-ai-insights
  - sources/theaxlabs-contaminated-memory-performance
  - sources/google-io-2026-agentic-gemini
confidence: 0.78
---

# Agent Experience (AX) Design

## Core Idea

This cluster organizes the design and research knowledge for agentic products: systems that perceive context, take initiative, and act on the user's behalf. The central tension is leverage versus control — every increase in agent autonomy must be paid for with transparency, reversibility, and calibrated trust.

## Concept Layer

### Initiative — when the agent acts
- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[concepts/agent-experience/collaboration-patterns|Collaboration Patterns]]

### Trust — why the user lets it
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/error-recovery|Error Recovery]]
- [[concepts/agent-experience/mental-model-onboarding|Mental Model Onboarding]]

### Foundations already in the vault
- [[concepts/ux-research/ax-ai-experience|AX (AI Experience)]]
- [[concepts/ux-research/haic-modalities-taxonomy|HAIC Modalities Taxonomy]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- [[concepts/ux-research/progressive-user-control|Progressive User Control]]
- [[concepts/ux-research/human-in-the-loop|Human in the Loop]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/ai-agents/memory-contamination|Memory Contamination]]
- [[concepts/ai-agents/long-horizon-tasks|Long-Horizon Tasks]]
- [[concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]]

## Research Layer

- [[concepts/agent-experience/agent-evaluation-ux|Agent Evaluation UX]]
- [[methods/wizard-of-oz-testing|Wizard of Oz Testing]]
- [[methods/longitudinal-research|Longitudinal Research]]
- [[methods/diary-studies|Diary Studies]]
- [[methods/usability-testing|Usability Testing]]
- [[concepts/ux-research/ai-evals|AI Evals]]

## Working Decision Path

1. Pick the collaboration pattern for the task: stakes × reversibility × user expertise.
2. Set the proactivity level and interruption budget.
3. Design the trust surface: provenance, uncertainty, preview-then-commit.
4. Design failure first: detection, admission, undo, repair.
5. Evaluate longitudinally: intervention rate, verification effort, trust trajectory — not single-session SUS alone.

## Evidence Base

The cluster is grounded in three foundational sources, all ingested 2026-06-12:

- [[sources/lee-see-2004-trust-in-automation|Lee & See (2004)]] — appropriate reliance, misuse/disuse, calibration/resolution/specificity, purpose/process/performance
- [[sources/horvitz-1999-mixed-initiative|Horvitz (1999)]] — decision-theoretic initiative, attention cost, graded autonomy
- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019)]] — 18 validated guidelines across four interaction phases; usable as heuristic-evaluation criteria

All three predate generative LLM agents; transfer is well supported by current literature but per-feature validation is still required.

## Gaps To Fill Next

- Ingest recent empirical agent-UX field studies (2024-26) to test transfer of the classic frameworks to long-horizon generative agents.
- Add a comparison table: proactivity level × use case × required trust surface.
- Add a project analysis memo when this cluster is applied to a real proactive-agent design decision.
