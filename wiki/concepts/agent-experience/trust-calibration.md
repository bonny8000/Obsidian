---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags: [agent-experience, trust, ax, human-ai-interaction]
sources:
  - sources/andru-saksena-adobe-haic-2025
  - sources/theaxlabs-contaminated-memory-performance
  - sources/lee-see-2004-trust-in-automation
confidence: 0.8
---

# Trust Calibration

## Summary

Trust calibration is the goal of matching user trust to actual agent capability: enough trust to delegate where the agent is reliable, enough skepticism to verify where it is not.

## Why It Matters

Both failure modes are expensive. Over-trust leads to unreviewed errors shipping into real work; under-trust means users redo everything the agent did and the product delivers no leverage. The design target is appropriate reliance, not maximum trust.

## Key Claims

- Trust is dimension-specific, not global: a user can correctly trust an agent for retrieval but not for judgment calls.
- Calibration is driven more by experienced outcomes than by stated disclaimers; the first few failures shape long-term reliance.
- Uncertainty display (confidence signals, hedged language, "I could not verify X") is the main interface lever for preventing over-trust.
- Easy verification paths (citations, diffs, previews before commit) let users build trust incrementally instead of taking a delegation leap.
- Contaminated or stale memory silently miscalibrates trust because the user cannot see why the agent's behavior degraded — see [[concepts/ai-agents/memory-contamination|Memory Contamination]].
- Lee & See define three target properties: calibration (level matches capability), resolution (trust differentiates contexts), and specificity (trust attaches to the right function) — plus a misuse/disuse failure taxonomy — see [[sources/lee-see-2004-trust-in-automation|Lee & See 2004]].

## Design Levers

- Show provenance: where did this answer/action come from
- Express uncertainty honestly instead of uniform confidence
- Preview-then-commit for consequential actions
- Make agent failures legible and recoverable rather than hidden
- Progressive autonomy: earn wider permissions through demonstrated reliability

## Related Concepts

- [[concepts/agent-experience/agent-transparency|Agent Transparency]]
- [[concepts/agent-experience/error-recovery|Error Recovery]]
- [[concepts/agent-experience/proactivity-design|Proactivity Design]]
- [[concepts/ux-research/human-in-the-loop|Human in the Loop]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]

## Conflicts & Caveats

- Now grounded in Lee & See (2004), the foundational appropriate-reliance model; note it predates LLMs, so transfer of specific dynamics to generative agents should still be validated per feature.

## Sources

- [[sources/lee-see-2004-trust-in-automation|Lee & See (2004): Trust in Automation]]
- [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework]]
- [[sources/theaxlabs-contaminated-memory-performance|AX LABS: Contaminated Memory]]

## Open Questions

- Which uncertainty display format actually changes verification behavior rather than being ignored?
- How fast does trust recover after a visible agent failure, and what repair moves accelerate it?
