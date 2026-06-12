---
type: concept
status: active
created: 2026-06-01
updated: 2026-06-10
tags: [concept, typography, performance, localization]
sources: [bucketplace-pretendard-jp-2026-04-17]
confidence: 0.85
---

# Font Subsetting

> Rebuilt 2026-06-10 after corruption ([[logs/2026-06-10-corruption-recovery|recovery log]]).

## Summary

Removing unused glyphs from a font file to cut size. Essential for CJK fonts (tens of thousands of glyphs), but risky: if a needed script is subset out, text silently falls back to system fonts — layout and brand typography break without errors.

## Why it matters

App/web size budgets collide with multilingual coverage. Subsetting decisions are localization decisions.

## Key claims

- Missing glyphs fail silently via fallback, so subsetting bugs evade QA unless tested per locale. (conf 0.9)
- Tooling matters: FontForge exports introduced metric/padding issues; TTFont (fontTools) subsetting did not. (conf 0.8)
- Delivery mechanisms (e.g., Android Dynamic Feature Modules) let teams ship script-specific subsets per market. (conf 0.9)

## Related concepts

- [[concepts/infrastructure-dev/localization-ux|Localization UX]]

## Sources

- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace — Pretendard JP]]

## Open questions

- What is a reliable automated test for glyph-coverage regressions across locales?
