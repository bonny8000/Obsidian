---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.66
---

# Which visual differences should be treated as defects versus acceptable implementation variance?

## Short Answer
Treat as defects: wrong color token, wrong typography scale or weight, broken spacing system (non-token values), missing states (hover, focus, error), and accessibility failures (contrast, target size). Treat as acceptable variance: sub-pixel rounding differences, minor anti-aliasing variation, and layout adjustments caused by real content length that the design assumed fixed. The dividing line is whether the difference contradicts a design-system rule or only reflects realistic rendering conditions.

## Evidence
- [[concepts/infrastructure-dev/design-review-automationDesign Review Automation]] ??"Automated review should augment, not replace, designer judgment. Review rules need design-system and product-context awareness." Design-system rules are the defect boundary.
- [[concepts/infrastructure-dev/design-system-implementationDesign System Implementation]] ??"Design-system implementation must verify rendered output, not only code-level configuration. Typography tokens need platform and language-specific validation."
- [[concepts/infrastructure-dev/design-to-code-workflowDesign-to-Code Workflow]] ??"The goal is a loop between design, implementation, and validation rather than a one-way handoff." The validation step needs clear defect criteria to be useful.
- [[sources/ditoday-claude-design-uiux-workflow|Digital iNSIGHT: Claude Design and UI/UX Workflow]] ??"Browser automation and screenshot comparison can help verify implementation quality."

## Follow-up Sources Needed
- A severity classification framework for design implementation issues (e.g., P1 token violation vs. P3 anti-aliasing variance).

