---
type: map
status: active
created: 2026-06-12
updated: 2026-08-04
tags: [map, agent-experience, ax, ux-design, ux-research]
sources:
  - sources/lee-see-2004-trust-in-automation
  - sources/horvitz-1999-mixed-initiative
  - sources/amershi-2019-human-ai-guidelines
  - sources/andru-saksena-adobe-haic-2025
  - sources/pxd-story-ai-insights
  - sources/theaxlabs-contaminated-memory-performance
  - sources/google-io-2026-agentic-gemini
  - sources/hbs-working-knowledge-ai-advice-willful-blindness
  - sources/toyota-voice-interaction-humanoid-robots
  - sources/paxton-yao-voice-ai-thinking-state
  - sources/google-search-io-2026-agents
confidence: 0.82
---

# Agent Experience (AX) Design

## Core Idea

This cluster organizes the design and research knowledge for agentic products: systems that perceive context, take initiative, and act on the user's behalf. The central tension is leverage versus control — every increase in agent autonomy must be paid for with transparency, reversibility, and calibrated trust.

## Concept Layer

### Initiative — when the agent acts
- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/agent-experience/initiative-and-interruption|Initiative and Interruption]]
- [[concepts/agent-experience/collaboration-patterns|Collaboration Patterns]]

### Legibility — what is it doing right now
- [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]] — the layer *beneath* transparency: listening, thinking, speaking, or waiting for your turn.
- [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]] — what fills the second LLM inference added.
- [[wiki/concepts/agent-experience/modality-intent-matching|Modality–Intent Matching]] — which channel, and what latency it can afford.

### Trust — why the user lets it
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/error-recovery|Error Recovery]]
- [[concepts/agent-experience/mental-model-onboarding|Mental Model Onboarding]]
- [[concepts/agent-experience/willful-blindness|Willful Blindness]]
- [[concepts/agent-experience/checkbox-transparency|Checkbox Transparency]]
- [[concepts/ux-research/explainable-ai|Explainable AI]]

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

The cluster is grounded in foundational sources:

- [[sources/lee-see-2004-trust-in-automation|Lee & See (2004)]] — appropriate reliance, misuse/disuse, calibration/resolution/specificity, purpose/process/performance (Ingested 2026-06-12)
- [[sources/horvitz-1999-mixed-initiative|Horvitz (1999)]] — decision-theoretic initiative, attention cost, graded autonomy (Ingested 2026-06-12)
- [[sources/amershi-2019-human-ai-guidelines|Amershi et al. (2019)]] — 18 validated guidelines across four interaction phases; usable as heuristic-evaluation criteria (Ingested 2026-06-12)
- [[sources/hbs-working-knowledge-ai-advice-willful-blindness|Chan (2026)]] — empirical evidence of strategic information avoidance (willful blindness) in Explainable AI interaction under outcome-based incentives (Ingested 2026-07-07)

Lee & See, Horvitz, and Amershi predate generative LLM agents; Chan (2026) provides direct empirical behavioral data on explainable AI interaction.

## The Response Gap (added 2026-08-04)

A sub-cluster that did not exist before LLM inference latency. Two sources published a day apart solved the same problem in different media without knowing about each other.

- **Memo:** [[wiki/analyses/2026-08-04-the-response-gap|The Response Gap — What Fills the Second That LLMs Added]] — argues the gap is better framed as a **turn-taking** problem than as a loading state.
- **Decision table:** [[wiki/comparisons/filling-the-response-gap|Filling the Response Gap]] — six options, their costs, and by-context recommendations.
- **Concepts:** [[wiki/concepts/agent-experience/response-latency-masking|Response Latency Masking]] (covering the wait) · [[wiki/concepts/agent-experience/system-state-signaling|System State Signaling]] (labelling it).
- **Sources:** [[wiki/sources/toyota-voice-interaction-humanoid-robots|Toyota FRC (2026)]] · [[wiki/sources/paxton-yao-voice-ai-thinking-state|Yao (2026)]].

**Evidence status: nothing in this sub-cluster is measured.** Treat it as an architecture menu.

## Gaps To Fill Next

- Ingest recent empirical agent-UX field studies (2024-26) to test transfer of the classic frameworks to long-horizon generative agents.
- Add a comparison table: proactivity level × use case × required trust surface.
- Add a project analysis memo when this cluster is applied to a real proactive-agent design decision.
- **A latency-versus-perceived-responsiveness study for voice agents.** Highest-value single result for the response-gap sub-cluster; would decide whether half its techniques are worth their complexity.
- **The automotive-HMI literature on glance behaviour and assistant state ambiguity** — Yao's safety argument rests on it and cites none of it.
- **Conversational turn-taking literature** (gap/overlap timing, repair). Both new sources reinvent it, and it would ground the ~1 second figure properly.
- **Third-party consent in agent-mediated contact.** Google's agentic calling reaches a party with no interface, no disclosure, and no seat on the [[wiki/concepts/agent-experience/delegation-spectrum|delegation spectrum]]. No concept in this vault covers it; open one when a second source appears.
