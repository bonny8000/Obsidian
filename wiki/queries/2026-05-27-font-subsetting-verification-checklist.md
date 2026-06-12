---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.78
---

# What verification checklist should be used after subsetting a font?

## Short Answer
After subsetting a font, verify: (1) all required glyphs are present in the subsetted file (check against the full target character set); (2) line metrics (ascender, descender, line height) are unchanged from the original; (3) character spacing and kerning are not altered; (4) the font renders correctly on each target platform (Android, iOS, web) with the actual localized UI text; and (5) no silent fallback to a system font occurs for any included glyph.

## Evidence
- [[concepts/infrastructure-dev/font-subsetting|Font Subsetting]] ??"Subsetting can reduce font size, but output must be checked for rendering and metrics issues. Tool choice matters: export pipelines can change padding, line metrics, or glyph behavior. Subsetting works best when the required character coverage is well defined."
- [[concepts/infrastructure-dev/font-fallback|Font Fallback]] ??"Fallback should be detected by inspecting glyph coverage and rendered output. Design review should include multilingual text samples, not only default-language UI." After subsetting, fallback can appear if a glyph was accidentally excluded.
- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]] ??"Font subsetting can reduce app size, but tooling can affect metrics and rendering." The article demonstrates both size benefits and potential tooling artifacts.
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]] ??"Design-system implementation must verify rendered output, not only code-level configuration."

## Follow-up Sources Needed
- Specific tooling recommendations (pyftsubset, glyphhanger, etc.) and their known metric-preservation behaviors.

