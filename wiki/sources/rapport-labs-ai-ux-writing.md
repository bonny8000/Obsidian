---
type: source
status: active
created: 2026-05-19
tags: [ai, ux-writing, rapport-labs, figma, claude]
sources: [raw/2026-05-19-rapport-labs-ai-ux-writing.md]
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 1.0
---

# AI UX Writing Principles (Rapport Labs)

## Citation

- **Title:** AI, Fix My UX Writing "Al-Jal-Ttak" (Perfectly)
- **Author:** Jiyeon Hong (Product Designer at Rapport Labs)
- **URL:** https://blog.rapportlabs.kr/ai-ux-writing
- **Date Observed:** 2026-05-19

## Summary

A case study by Rapport Labs on building an AI-powered UX writing system. They developed a Figma plugin using Claude and a Notion-based "Case DB" to automate UX writing inspections and variations. This ensures consistency in brand voice without a dedicated UX writer by integrating guidelines directly into the design workflow.

## Key Claims

- Static guideline documents are often ignored; integration into workflow (e.g., Figma plugins) is essential for effectiveness [raw/2026-05-19-rapport-labs-ai-ux-writing.md].
- Claude (Sonnet 3.5/4) is highly reliable for adhering to complex UX writing rules when paired with a reference database [raw/2026-05-19-rapport-labs-ai-ux-writing.md].
- [[concepts/ai-agents/vibe-coding|Vibe Coding]] using AI (Cursor) enables non-engineers to prototype internal tools quickly [raw/2026-05-19-rapport-labs-ai-ux-writing.md].
- A [[concepts/ux-research/human-in-the-loop|Human-in-the-loop]] approach is used where AI suggests variations and the designer makes the final choice [raw/2026-05-19-rapport-labs-ai-ux-writing.md].

## Concepts Linked

- [[concepts/ux-research/ux-writing-tf|UX Writing TF]]
- [[concepts/ai-agents/ai-inspection-bot|AI Inspection Bot]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-loop]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/2026-05-19-rapport-labs-ai-ux-writing.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/2026-05-19-rapport-labs-ai-ux-writing.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- Primary source from a practicing product designer at a well-known startup (Rapport Labs).

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ai-agents/vibe-coding]], [[concepts/ux-research/human-in-the-loop]], [[concepts/ux-research/ux-writing-tf]], [[concepts/ai-agents/ai-inspection-bot]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** research design, UX evidence, method selection, and evaluation prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `substantial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
