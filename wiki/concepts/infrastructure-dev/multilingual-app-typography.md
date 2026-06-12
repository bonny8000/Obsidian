---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [typography, localization, app-ux, design-system]
sources:
  - sources/bucketplace-pretendard-jp-2026-04-17
confidence: 0.86
---

# Multilingual App Typography

## Summary

Multilingual app typography is the design and engineering practice of making text render consistently and legibly across languages, scripts, glyph sets, weights, and platforms.

## Why It Matters

Localization quality is not only translation. If a font lacks glyph coverage, the app may silently fall back to a different typeface, causing weight, rhythm, and brand consistency problems.

## Key Claims

- Typography must be verified per script and glyph range.
- Font family assignment alone does not guarantee the displayed glyphs come from that font.
- Multilingual typography decisions can affect app size, runtime delivery, and design-system consistency.

## Related Concepts

- [[concepts/infrastructure-dev/font-fallback|Font Fallback]]
- [[concepts/infrastructure-dev/font-subsetting|Font Subsetting]]
- [[concepts/infrastructure-dev/localization-ux|Localization UX]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]

## Sources

- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]]

## Open Questions

- Which languages and glyph ranges must Bonny's design systems explicitly support? (insufficient evidence in wiki — requires Bonny's specific project scope information not in wiki)

