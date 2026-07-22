---
type: source
status: active
created: 2026-06-08
tags: [design-system, design-tokens, color-tokens, accessibility, pxd]
sources:
  - raw/web/pxd-color-token-design-2026-05-18.md
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# pxd: Color Token Design Patterns

## Citation

pxd story. (2026-05-18). *컬러 토큰 설계 3가지 방식 (스케일 / 시멘틱 / 하이브리드).* Retrieved 2026-06-08 from https://story.pxd.co.kr/1888

## Source Type

Korean pxd story article / design-system practice note.

## Location

- Raw capture: `raw/web/pxd-color-token-design-2026-05-18.md`
- Original URL: https://story.pxd.co.kr/1888

## Summary

The article explains three ways to structure color tokens in a design system: scale tokens, semantic tokens, and a hybrid structure that connects scale values to semantic roles. It frames token design as a system-infrastructure decision that matters more as AI-assisted design automation increases the speed and volume of UI output.

## Key Claims

- Scale tokens are fast and intuitive because they name base color values directly, but they do not preserve usage context.
- Semantic tokens reduce ambiguity by naming color roles and states, making multi-theme and accessibility-oriented systems easier to manage.
- Hybrid token architecture keeps design flexibility at the scale-token layer while preserving communication, theming, and operational consistency at the semantic-token layer.
- Token sprawl happens when new values and new meanings are added without first deciding whether the problem is value-level or semantic-level.
- APCA-style perceptual contrast checks can move readability risk detection from individual screens into the token layer.

## Concepts Linked

- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/pxd-color-token-design-2026-05-18.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/pxd-color-token-design-2026-05-18.md` when used for recommendations, metrics, or external-facing work.

## Reliability Notes

- The source is a practitioner article from pxd story and is useful as applied design-system guidance.
- The page footer links to a Creative Commons Attribution license.
- Claims about APCA and WCAG 3.0 should be verified against primary standards documentation before being used as a formal accessibility compliance rule.

## Design Implications

- Use this source to shape design-system, design automation, and UI-quality prompts.
- Connect it with [[concepts/infrastructure-dev/color-token-architecture]], [[concepts/infrastructure-dev/design-system-implementation]], [[concepts/infrastructure-dev/scaffold-design-system]], [[concepts/infrastructure-dev/deterministic-ui]] before turning it into a project recommendation.

## Tensions

- Backfill note: source-specific tensions were not separately extracted in the earlier ingest. Compare this source with related concepts and maps before treating its framing as settled.

## Open Questions

- What evidence, examples, or counterexamples should be extracted from the raw source before marking this as `coverage: full`?
- Which linked concept would change most if this source were contradicted?

## LLM Use

- **Use for:** design-system, design automation, and UI-quality prompts.
- **Do not use for:** unsupported exact claims beyond the source note's `substantial` coverage.
- **Best prompt pattern:** Ask the LLM to combine this source with its linked concepts, then verify any specific claim against the raw source before final use.

## Backfill Status

- Retrofitted on 2026-06-12 by `scripts/backfill_llm_ready.py` from the existing source note.
- This standardizes the note for LLM use; it does not by itself mean the raw source has been fully re-read.
