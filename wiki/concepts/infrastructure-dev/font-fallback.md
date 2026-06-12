---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [typography, fonts, localization]
sources:
  - sources/bucketplace-pretendard-jp-2026-04-17
confidence: 0.86
---

# Font Fallback

## Summary

Font fallback happens when a requested font does not contain the needed glyph, so the system renders that character with another available font.

## Why It Matters

Fallback can be invisible in code but visible in the UI. It may create inconsistent weights, spacing, line height, or visual tone across languages.

## Key Claims

- Unsupported Japanese and CJK glyphs can fall back to a system font even when the app's intended font is set.
- Fallback should be detected by inspecting glyph coverage and rendered output.
- Design review should include multilingual text samples, not only default-language UI.

## Related Concepts

- [[concepts/infrastructure-dev/multilingual-app-typography|Multilingual App Typography]]
- [[concepts/infrastructure-dev/font-subsetting|Font Subsetting]]
- [[concepts/infrastructure-dev/localization-ux|Localization UX]]

## Sources

- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]]

## Open Questions

- What fallback chain should be documented for each target platform? (insufficient evidence in wiki — requires platform-specific font stack documentation for Android, iOS, web)

