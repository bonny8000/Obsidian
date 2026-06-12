---
type: source
status: active
created: 2026-05-18
updated: 2026-06-10
tags: [source, article, typography, localization, android]
sources: []
confidence: 0.9
---

# Bucketplace — Pretendard JP in a Multi-Country Android App

> [!info] Metadata
> - **Author:** Zemic (Bucketplace / 오늘의집)
> - **Date:** 2026-04-17
> - **Type:** engineering blog article
> - **Raw File:** [[raw/web/bucketplace-pretendard-jp-2026-04-17.md]]
> - **Note:** Page rebuilt 2026-06-10 after file corruption (see [[logs/2026-06-10-corruption-recovery|recovery log]]).

## 🎯 Summary

How Bucketplace introduced Pretendard JP into a multi-country Android app without inflating APK size for non-Japanese users. The original bug: the app appeared to use the intended font, but Japanese/CJK glyphs silently fell back to the system font because the existing Pretendard subset lacked those glyphs. Bundling full Pretendard JP would penalize all users, so the team subset the font (TTFont, after FontForge export caused metric/padding issues) and delivered it via an Android Dynamic Feature Module only to Japan-relevant users.

## 💎 Key Claims

- Font subsetting can silently break localization: missing glyphs fall back to system fonts without visible errors. (conf 0.9)
- Dynamic Feature Modules allow per-market font delivery, decoupling locale assets from base APK size. (conf 0.9)
- FontForge exports can introduce padding/metric issues; TTFont subsetting avoided them. (conf 0.8)

## 🧠 Concepts Extracted

- [[concepts/infrastructure-dev/font-subsetting|Font Subsetting]]
- [[concepts/infrastructure-dev/localization-ux|Localization UX]]

## ⚠️ Reliability Notes

> [!warning] Caveats
> First-party engineering account; specific to Android delivery. Korean-language original.
