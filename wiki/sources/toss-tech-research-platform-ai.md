---
type: source
status: active
created: 2026-05-27
tags: [ux-research, ai-assistant, usability-testing, toss, fintech]
sources: [raw/web/toss-tech-research-platform-ai.md]
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.95
---

# Source: Toss Tech ??Huribot Story #1

- **URL:** https://toss.tech/article/research-platform-ai
- **Title:** ?渠收賵??渥篣?#1: ???AI 賵?窶??科???貲賰圉未 ? (Huribot Story #1: How Toss Has an AI Bot Do User Interviews)
- **Author:** Choi Jung-eun (黖??), UX Research Operation Manager, Toss
- **Published:** 2024-12-02
- **Publisher:** Toss Tech Blog
- **Raw file:** `raw/web/toss-tech-research-platform-ai.md`
- **Captured:** 2026-05-27

## Summary

Toss, the Korean fintech super-app, developed "Huribot" ??an AI assistant trained on proprietary Toss user data ??to enable designers to perform rapid, lightweight usability checks without the overhead of traditional user testing (UT). The article documents the problem, the three-phase prompting development workflow, and the demonstrated impact.

## Key Claims

- Toss's existing "User Mumul Day" remote UT program required a minimum one-hour preparation time per session, creating psychological barriers for designers.
- Huribot allows designers to upload screen images and receive usability feedback in seconds rather than ~1 hour.
- Huribot is positioned as a "check" tool, not a replacement for formal research; it supplements rather than supersedes traditional UT.
- The development process used a three-phase prompting workflow:
  - **Pre-Prompting:** narrow the problem, define goals, build team consensus
  - **During Prompting:** validate early via lightweight chatbot prototype with real designers, iterate on prompts based on usage
  - **Post-Prompting:** define MVP features; core: image upload, question input, response generation
- Designers use Huribot to catch issues ??misleading graphics, dark patterns, unclear messaging ??during early design iteration.
- Formal UT is reserved for deeper validation questions.
- Huribot was trained on Toss-specific user data (proprietary; not a generic foundation model).

## Concepts Linked

- [[concepts/ux-research/huribot|Huribot]]
- [[concepts/ux-research/automated-ut-setup|Automated UT Setup]]
- [[concepts/ux-research/ux-research-automation|UX Research Automation]]
- [[concepts/ux-research/ai-usability-analysis|AI Usability Analysis]]
- [[concepts/ux-research/design-research-automation|Design Research Automation]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-loop]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/toss-tech-research-platform-ai.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/toss-tech-research-platform-ai.md` when used for recommendations, metrics, or external-facing work.

## Citation

- Source record: `Source: Toss Tech ??Huribot Story #1`.
- Raw evidence: `raw/web/toss-tech-research-platform-ai.md`.

## Reliability Notes

Primary source from the team that built Huribot. Author is the UX Research Operations Manager at Toss, so claims about internal tooling and workflow impact are first-hand. No independent verification of time-savings claim ("seconds vs. 1 hour"). Confidence: 0.95.

## Design Implications

- Use this source to shape research design, UX evidence, method selection, and evaluation prompts.
- Connect it with [[concepts/ux-research/huribot]], [[concepts/ux-research/automated-ut-setup]], [[concepts/ux-research/ux-research-automation]], [[concepts/ux-research/ai-usability-analysis]] before turning it into a project recommendation.

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
