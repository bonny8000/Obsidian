---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.78
---

# What should the minimum multilingual QA sample set include?

## Short Answer
The minimum multilingual QA sample set should include: (1) a representative screen for each supported locale with real (not placeholder) translated text; (2) a string that tests the longest expected text expansion in each language; (3) CJK glyphs covering the full glyph range used in each locale; (4) mixed-script content where two scripts appear in the same UI element; and (5) the localized app running on a physical device or verified emulator for each platform.

## Evidence
- [[concepts/infrastructure-dev/localization-ux|Localization UX]] ??"Multilingual QA should test real localized content and visual rendering. Locale-specific improvements should not unnecessarily degrade performance for other users."
- [[concepts/infrastructure-dev/font-fallback|Font Fallback]] ??"Design review should include multilingual text samples, not only default-language UI." Silent fallback only appears when the actual localized text is tested.
- [[concepts/infrastructure-dev/multilingual-app-typography|Multilingual App Typography]] ??"Typography must be verified per script and glyph range. Font family assignment alone does not guarantee the displayed glyphs come from that font."
- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]] ??"A UI can appear to use the intended font while unsupported glyphs silently fall back to a system font." Only real localized content reveals this.

## Follow-up Sources Needed
- A standardized CJK glyph coverage test string covering the most common characters in Japanese, Simplified Chinese, and Traditional Chinese.

