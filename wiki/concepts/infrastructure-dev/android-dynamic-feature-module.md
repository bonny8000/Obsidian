---
type: concept
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [android, app-delivery, localization, performance]
sources:
  - sources/bucketplace-pretendard-jp-2026-04-17
confidence: 0.8
---

# Android Dynamic Feature Module

## Summary

An Android Dynamic Feature Module is an app module that can be delivered separately from the base app, allowing optional or conditional resources and features to be downloaded only when needed.

## Why It Matters

For multilingual apps, dynamic delivery can keep the base app smaller while still providing large language-specific assets such as CJK fonts to users who need them.

## Key Claims

- Dynamic feature delivery can reduce unnecessary app-size cost for users outside a target locale or country.
- Fonts can be treated as conditional resources rather than always-bundled assets.
- Implementation details should be verified against Android's official dynamic delivery documentation.

## Related Concepts

- [[concepts/infrastructure-dev/font-subsetting|Font Subsetting]]
- [[concepts/infrastructure-dev/multilingual-app-typography|Multilingual App Typography]]
- [[concepts/infrastructure-dev/localization-ux|Localization UX]]

## Sources

- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]]

## Open Questions

- [Answered → [[queries/2026-05-27-android-font-delivery-constraints|Query Page]]] Which platform-level delivery constraints affect font resources specifically?

