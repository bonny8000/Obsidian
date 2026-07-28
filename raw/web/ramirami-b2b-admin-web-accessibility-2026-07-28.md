---
source_url: https://ramirami.tistory.com/m/234
captured: 2026-07-28
title: "B2B 어드민 서비스에 웹 접근성 적용하기"
authors: [rami_]
published: 2026-07-27
publisher: Tech Epilogue (Tistory)
language: ko
---

# Applying Web Accessibility to a B2B Admin Service — rami_

**Original title (ko):** 「B2B 어드민 서비스에 웹 접근성 적용하기」
**Published:** 2026-07-27 · **Captured:** 2026-07-28
**Capture note:** AI-written summary of a Korean-language front-end engineering post. Full text not reproduced.

## Summary

A working account of applying web accessibility to an internal **B2B admin** service. The argument for prioritizing it there is economic rather than compliance-driven: the *same* operators perform the *same* repetitive tasks daily, so small interaction improvements compound into daily workflow speed — unlike a consumer commerce site with many one-time visitors.

## Key claims

- **WCAG's POUR foundation** — Perceivable, Operable, Understandable, Robust — benefits all users, not only users with disabilities.
- **B2B admin has an unusually good payback.** Table-heavy interfaces used repetitively justify the investment. Screen readers cannot distinguish data types without header associations; icon-only buttons without labels force repeated mouse navigation.
- **Implementation order used:** keyboard operability → form labels → icon labels. AI-assisted planning with human validation was treated as standard practice.

## Concrete examples and numbers

- **One-line language fix:** `<html lang>` changed from `en` to `ko` for a Korean-language service.
- **Icon labels:** `aria-label` added to download, delete, refresh and similar buttons.
- **Table headers:** `scope="col"` applied so data cells are structurally associated with headers.
- **The grep discrepancy (the most transferable finding):** an initial automated scan reported **168 missing `alt` attributes and 166 missing `th` tags**. After opening the actual files and verifying manually, the real counts were **6 and 141**. Line-based grep searches were unreliable against this codebase's multi-line attribute formatting.

## Practical guidance

- Distinguish decorative images (`alt=""`) from meaningful ones (with i18n-managed alt text).
- **Validate automation results by opening the actual files.** Line-based searches over multi-line markup produce false positives.
- Embed accessibility rules in team documentation (`CLAUDE.md`) to prevent regression.
- Reuse existing localization keys before creating new ones.

## Caveats

- Pre-commit ESLint validation and zero-missing-`alt` audits give only partial assurance.
- The grep-versus-reality gap is specific to this codebase's multi-line attribute formatting style.
- This is an initial implementation, not comprehensive coverage; accessibility work is ongoing.
