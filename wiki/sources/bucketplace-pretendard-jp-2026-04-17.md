---
type: source
status: active
created: 2026-05-18
tags: [source, article, typography, localization, android]
sources: []
updated: 2026-06-12
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.9
---

# Bucketplace — Pretendard JP in a Multi-Country Android App

> [!info] Metadata
> - **Author:** Zemic (Bucketplace / 오늘의집)
> - **Date:** 2026-04-17
> - **Type:** engineering blog article
> - **Raw File:** [[raw/web/bucketplace-pretendard-jp-2026-04-17.md]]
> - **Note:** Page rebuilt 2026-06-10 after file corruption (see [[logs/2026-06-10-corruption-recovery|recovery log]]).

## Summary

How Bucketplace introduced Pretendard JP into a multi-country Android app without inflating APK size for non-Japanese users. The original bug: the app appeared to use the intended font, but Japanese/CJK glyphs silently fell back to the system font because the existing Pretendard subset lacked those glyphs. Bundling full Pretendard JP would penalize all users, so the team subset the font (TTFont, after FontForge export caused metric/padding issues) and delivered it via an Android Dynamic Feature Module only to Japan-relevant users.

## Key Claims

- Font subsetting can silently break localization: missing glyphs fall back to system fonts without visible errors. (conf 0.9)
- Dynamic Feature Modules allow per-market font delivery, decoupling locale assets from base APK size. (conf 0.9)
- FontForge exports can introduce padding/metric issues; TTFont subsetting avoided them. (conf 0.8)

## Concepts Linked

- [[concepts/infrastructure-dev/font-subsetting|Font Subsetting]]
- [[concepts/infrastructure-dev/localization-ux|Localization UX]]

## Useful Examples

- Current example source: use examples, tables, cases, or named artifacts already present elsewhere in this note; otherwise return to `raw/web/bucketplace-pretendard-jp-2026-04-17.md` before asking an LLM for concrete examples.

## Constraints / Caveats

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/bucketplace-pretendard-jp-2026-04-17.md` when used for recommendations, metrics, or external-facing work.

## Citation

- Source record: `Bucketplace — Pretendard JP in a Multi-Country Android App`.
- Raw evidence: `raw/web/bucketplace-pretendard-jp-2026-04-17.md`.

## Reliability Notes

- Coverage is `substantial` and ingest level is `standard`; do not treat this source as fully digested unless `coverage: full`.
- Claims should be checked against `raw/web/bucketplace-pretendard-jp-2026-04-17.md` when used for recommendations, metrics, or external-facing work.

> [!warning] Caveats
> First-party engineering account; specific to Android delivery. Korean-language original.

## Design Implications

- Use this source to shape design-system, design automation, and UI-quality prompts.
- Connect it with [[concepts/infrastructure-dev/font-subsetting]], [[concepts/infrastructure-dev/localization-ux]] before turning it into a project recommendation.

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
