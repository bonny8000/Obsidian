---
type: concept
status: active
created: 2026-06-01
updated: 2026-08-04
tags: [ai, haic, control, ux-design]
sources: [andru-saksena-adobe-haic-2025, saeidehbakhshi-usability-metrics-static-product]
confidence: 0.90
---

# Progressive User Control

## Summary
Progressive User Control is a design principle for AI systems that allows users to adjust the level of autonomy and agency the AI has over a task. It ensures that the user remains "in the loop" and can take over or override the AI at any time.

## Levels of Control
- **Manual:** User performs all steps; AI is passive.
- **Assisted:** AI suggests or automates discrete steps (e.g., autocomplete).
- **Collaborative:** AI and user share the task (e.g., pair programming).
- **Autonomous with Review:** AI performs the task; user approves the result.
- **Full Autonomy:** AI performs the task independently (e.g., background agent).

## Why it matters
High-autonomy systems can cause anxiety and loss of trust if users feel they have no control. Progressive control provides a "safety valve," allowing users to dial back the AI's agency as needed, which is critical for complex or high-stakes workflows.

## Not the Same as Steerability

> [!note] Added 2026-08-04
> Progressive control is about **how much autonomy the user grants**, set in advance along the ladder above. [[wiki/concepts/ux-research/steerability|Steerability]] ([[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi, 2026]]) is about whether the user can **change a model the system has already built of them** — and crucially, whether the correction *persists across sessions or reverts*.
>
> They are adjacent and they fail differently. A system can sit at "Assisted" on this ladder — low autonomy, user firmly in the loop — and still be unsteerable, because every control works and none of them changes what it shows you tomorrow. The persistence question belongs only to steerability, and it is the question adaptive products fail.
>
> **A correction that reverts is a placebo button:** control offered without being granted.

## Related Concepts
- [[concepts/ux-research/haic-modalities-taxonomy|HAIC Modalities Taxonomy]]
- [[concepts/ux-research/designing-for-agency|Designing for Agency]]
- [[concepts/ai-agents/autonomous-ai-agent|Autonomous AI Agent]]
- [[wiki/concepts/ux-research/steerability|Steerability]] — the adaptive-systems counterpart; see above.
- [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]]

## Sources
- [[sources/andru-saksena-adobe-haic-2025|Adobe HAIC Framework]]
- [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026): Usability Metrics Assume the Product Stays Still]] — for the steerability distinction.
