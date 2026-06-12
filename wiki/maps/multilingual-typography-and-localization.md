---
type: map
status: active
created: 2026-05-18
updated: 2026-05-18
tags: [map, typography, localization, android, design-system]
sources:
  - sources/bucketplace-pretendard-jp-2026-04-17
confidence: 0.84
---

# Multilingual Typography and Localization

## Core Idea

This cluster tracks how multilingual apps maintain visual consistency and performance when different scripts require different font coverage and delivery strategies.

## Concepts

- [[concepts/infrastructure-dev/multilingual-app-typography|Multilingual App Typography]]
- [[concepts/infrastructure-dev/font-fallback|Font Fallback]]
- [[concepts/infrastructure-dev/font-subsetting|Font Subsetting]]
- [[concepts/infrastructure-dev/android-dynamic-feature-module|Android Dynamic Feature Module]]
- [[concepts/infrastructure-dev/localization-ux|Localization UX]]
- [[concepts/infrastructure-dev/design-system-implementation|Design System Implementation]]

## Source Path

- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]]

## Working Interpretation

The important lesson is that localization quality lives at the intersection of design, engineering, typography, asset size, and platform delivery. A font can be configured correctly in code while still rendering incorrectly if glyph coverage and fallback are not verified.

