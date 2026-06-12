---
type: source
status: active
created: 2026-06-08
updated: 2026-06-08
tags: [design-system, design-tokens, color-tokens, accessibility, pxd]
sources:
  - raw/web/pxd-color-token-design-2026-05-18.md
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

## Extracted Claims

- Scale tokens are fast and intuitive because they name base color values directly, but they do not preserve usage context.
- Semantic tokens reduce ambiguity by naming color roles and states, making multi-theme and accessibility-oriented systems easier to manage.
- Hybrid token architecture keeps design flexibility at the scale-token layer while preserving communication, theming, and operational consistency at the semantic-token layer.
- Token sprawl happens when new values and new meanings are added without first deciding whether the problem is value-level or semantic-level.
- APCA-style perceptual contrast checks can move readability risk detection from individual screens into the token layer.

## Concepts Linked From This Source

- [[concepts/infrastructure-dev/color-token-architecture|Color Token Architecture]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]
- [[concepts/infrastructure-dev/scaffold-design-system|Scaffold Design System]]
- [[concepts/infrastructure-dev/deterministic-ui|Deterministic UI]]

## Reliability Notes

- The source is a practitioner article from pxd story and is useful as applied design-system guidance.
- The page footer links to a Creative Commons Attribution license.
- Claims about APCA and WCAG 3.0 should be verified against primary standards documentation before being used as a formal accessibility compliance rule.
