---
type: concept
status: active
created: 2026-05-18
updated: 2026-07-30
tags: [design, ai-design, workflow, prototyping, product-taste]
sources:
  - sources/brunch-ghidesigner-482
  - sources/christinevallaure-agentic-ai-design-systems
  - sources/designer-builder-collapse
  - sources/naver-d2-ai-hackathon-nstake
confidence: 0.70
---

# Vibe Design

## Summary

Vibe Design is a design workflow where the designer communicates intent, taste, constraints, and feedback in natural language while AI generates and iterates on visual or coded artifacts.

## Why It Matters

It shifts design effort from manual pixel manipulation toward direction, evaluation, and system-level coherence. The designer becomes a reviewer and director of generated variations.

## Key Claims

- The useful unit of work becomes intent plus review, not just a static artboard.
- AI-native design tools can connect design directly to runnable prototypes.
- Quality still depends on design judgment, critique, and consistency with a design system.
- **Efficiency-optimized assembly degrades into slop without upstream craft.** Vallaure warns that systems optimized purely for efficient assembly produce "generic, interchangeable" UI; "designing the whole page is where the finding happened," so a human "finding" phase must precede agent assembly ([[sources/christinevallaure-agentic-ai-design-systems|Vallaure, 2026]]).
- **A reusable prototyping kit is the practical unlock.** Rather than prompting from scratch each time, [[wiki/sources/designer-builder-collapse|Yousefi (2026)]] built a Claude-based kit enabling component reuse across projects, making interactive prototypes a minutes-scale activity. The most directly copyable practice in this concept.
- **Generation speed is not judgment speed.** [[wiki/sources/naver-d2-ai-hackathon-nstake|NStake]] is the counter-case: three developers generated a full UI in one hour around a cute character theme — wrong for a finance team whose spreadsheets used **cell colour as meaning**. Refinement toward a trusted corporate design language made **design the bottleneck**. Direction and evaluation are the unautomated remainder, which is what "taste" is doing work for here.

## ⚖️ Conflicts & Caveats

> [!warning] Review becomes the job, and nobody has designed that surface
> If the designer is "a reviewer and director of generated variations," the review interface *is* the design practice. That inherits the largest unresolved problem in this vault's agent work: gates that fire constantly train reflexive approval — see [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]. No source measures design quality under high-volume review load.

## Related Concepts

- [[concepts/infrastructure-dev/design-automation|Design Automation]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[concepts/ai-agents/ai-agent-workflow|AI Agent Workflow]]
- [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]] · [[concepts/infrastructure-dev/ai-native-design-system|AI-Native Design System]]
- [[wiki/concepts/agent-experience/designing-generative-systems|Designing Generative Systems]] — where this workflow leads: designing the generator, not the screen.
- [[wiki/concepts/infrastructure-dev/llm-safe-design-system|LLM-Safe Design System]] — bounding the vocabulary the generator may use.
- [[wiki/concepts/product-management/product-taste|Product Taste]]

## Sources

- [[sources/brunch-ghidesigner-482|Vibe Design and Coding with Claude Design and Claude Code]]
- [[sources/christinevallaure-agentic-ai-design-systems|Vallaure (2026): Agentic AI, Design Systems & Figma]]
- [[wiki/sources/designer-builder-collapse|Ozenc & Yousefi (2026): The Designer-Builder]] — the prototyping kit and the review-as-design-act shift.
- [[wiki/sources/naver-d2-ai-hackathon-nstake|NAVER D2 (2026): NStake]] — counter-evidence on generation speed versus audience judgment.

## Open Questions

- [Answered → [[queries/2026-05-27-vibe-design-quality-criteria|Query Page]]] What criteria should Bonny use to judge AI-generated design quality?

