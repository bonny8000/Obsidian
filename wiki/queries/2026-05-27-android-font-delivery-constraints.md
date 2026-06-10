---
type: query
status: active
created: 2026-05-27
updated: 2026-05-27
tags: [query]
sources: []
confidence: 0.76
---

# Which platform-level delivery constraints affect font resources specifically?

## Short Answer
On Android, the primary constraints are: (1) Dynamic Feature Modules allow locale-specific fonts to be downloaded only when needed, reducing base APK size; (2) the Google Play Asset Delivery system has size limits per delivery type; (3) fonts bundled in the base APK count against the 150 MB install size limit; and (4) Dynamic Font Delivery requires a network connection at first use if the user's locale triggers the download. These constraints collectively mean large CJK fonts are best delivered conditionally.

## Evidence
- [[concepts/infrastructure-dev/android-dynamic-feature-moduleAndroid Dynamic Feature Module]] ??"Fonts can be treated as conditional resources rather than always-bundled assets. Dynamic feature delivery can reduce unnecessary app-size cost for users outside a target locale or country. Implementation details should be verified against Android's official dynamic delivery documentation."
- [[concepts/infrastructure-dev/font-subsettingFont Subsetting]] ??"Fonts for CJK languages can be large. In mobile apps, shipping full fonts to every user can increase app size even when only a subset of users needs that script."
- [[sources/bucketplace-pretendard-jp-2026-04-17|Bucketplace: Pretendard JP in Multi-Country Android App]] ??"Android Dynamic Feature Modules can deliver country- or locale-specific font resources only when needed." This is the primary practical pattern.

## Follow-up Sources Needed
- Official Android documentation on Dynamic Feature Module size limits and download triggers.
- iOS equivalent mechanisms (App Thinning, on-demand resources) for CJK font delivery.

