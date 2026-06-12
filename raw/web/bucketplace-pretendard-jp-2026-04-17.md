# Source Card: Bucketplace - Pretendard JP in Multi-Country Android App

URL: https://www.bucketplace.com/post/2026-04-17-%EB%A9%80%ED%8B%B0-%EA%B5%AD%EA%B0%80-%EC%95%B1%EC%97%90%EC%84%9C-pretendard-jp-%EB%8F%84%EC%9E%85%ED%95%98%EA%B8%B0/

Retrieved: 2026-05-18

Source type: Engineering blog article

Publisher: Bucketplace / 오늘의집

Author: Zemic

Published: 2026-04-17

Original title: 멀티 국가 앱에서 Pretendard JP 도입하기

## Collection Notes

- This article describes introducing Pretendard JP into a multi-country Android app while limiting the size impact to Japanese-service users.
- The original problem was that the app appeared to apply the intended font, but Japanese and CJK glyphs were actually falling back to a system font because the existing Pretendard subset did not include those glyphs.
- Directly bundling the full Pretendard JP font would increase APK size for all users, including users outside Japan.
- The team investigated font contents with FontForge, then used TTFont for subsetting after FontForge export caused unexpected padding/metric issues.
- The final solution used a Dynamic Feature Module so the Japanese font resource could be delivered only to relevant users, while non-Japanese users kept the existing experience.

## Extracted Claims

- Font fallback can produce subtle UX bugs such as incorrect perceived weight.
- Font coverage must be verified at the glyph/Unicode level when supporting multilingual interfaces.
- Font subsetting can reduce font size, but tooling can affect metrics and rendering.
- Android Dynamic Feature Modules can conditionally deliver locale- or country-specific font resources.

## Potential Wiki Concepts

- Multilingual app typography
- Font fallback
- Font subsetting
- Android Dynamic Feature Module
- Localization UX
- Design system implementation

## Verification Notes

- Primary engineering blog source from Bucketplace.
- Android delivery claims should be cross-checked with official Android documentation if used for implementation decisions.

Copyright note: this card records metadata, extracted claims, and a paraphrased summary, not a full copy of the article.

