---
type: concept
status: active
created: 2026-06-01
updated: 2026-06-10
tags: [concept, localization, typography, ux]
sources: [bucketplace-pretendard-jp-2026-04-17]
confidence: 0.8
---

# Localization UX

> Rebuilt 2026-06-10 after corruption ([[logs/2026-06-10-corruption-recovery|recovery log]]).

## Summary

The user-facing quality of a product across languages and markets: typography, glyph coverage, fallback behavior, layout expansion, and culturally appropriate defaults. Distinct from translation accuracy — a perfectly translated string rendered in a fallback font is still a localization defect.

## Why it matters

Multi-country products (e.g., Bucketplace KR/JP) degrade silently: fallback fonts, clipped layouts, wrong number/date formats. These defects rarely surface in source-locale QA.

## Key claims

- Font/glyph fallback is a silent localization failure mode. (conf 0.9)
- Per-market asset delivery balances size budgets against native-quality rendering. (conf 0.85)

## Related concepts

- [[concepts/infrastructure-dev/font-subsetting|Font Subsetting]]
- [[concepts/ux-research/contextual-translation|Contextual Translation]]

## Sources

- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace — Pretendard JP]]

## Open questions

- Which locales in Bonny's current products lack locale-specific visual QA?
