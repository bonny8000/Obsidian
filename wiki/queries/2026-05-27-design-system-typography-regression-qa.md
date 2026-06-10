---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.76
---

# How should design-system QA catch script-specific typography regressions?

## Short Answer
Design-system QA for typography regressions should: (1) maintain a visual snapshot library of each supported script rendered with the current font stack; (2) run automated screenshot comparisons against that library on every design-system update; (3) include locale-specific text strings in the component story or test fixture, not just Latin defaults; and (4) inspect font rendering at the OS/browser level to confirm which font is actually rendering each glyph (not just which font is configured).

## Evidence
- [[concepts/infrastructure-dev/design-system-implementationDesign System Implementation]] ??"Design-system implementation must verify rendered output, not only code-level configuration. Typography tokens need platform and language-specific validation."
- [[concepts/infrastructure-dev/font-fallbackFont Fallback]] ??"Fallback should be detected by inspecting glyph coverage and rendered output." Silent regressions appear at the rendered output level, not the configuration level.
- [[concepts/infrastructure-dev/design-review-automationDesign Review Automation]] ??"Browser screenshots can be compared against design references. Review rules need design-system and product-context awareness."
- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]] ??"A UI can appear to use the intended font while unsupported glyphs silently fall back to a system font." This is the regression pattern to detect.

## Follow-up Sources Needed
- Tooling for cross-platform font rendering verification (e.g., Storybook snapshot testing with CJK fixtures, Android font inspector tools).

