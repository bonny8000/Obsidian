---
type: concept
status: active
created: 2026-07-02
updated: 2026-07-02
tags: [product-management, monetization, upsell, choice-architecture, trust]
sources:
  - sources/kakao-vc-upsell-design
confidence: 0.72
---

# Upsell Design

> [!abstract] Summary
> Offer a voluntary higher-value choice after base intent exists, and judge it by incremental benefit, margin, and long-term trust rather than attachment rate alone.

## Why It Matters

Upsells can improve unit economics without acquiring a new customer, but the same choice architecture can become coercive. The design challenge is to make the upgrade legible and genuinely useful while preserving a viable base option and obvious opt-out.

## Three Value Routes

| Route | Customer motivation | Typical offer | Main risk |
| --- | --- | --- | --- |
| Value | gain seeking | more quantity, capability, or specification | inflated comparison or degraded base tier |
| Reassurance | loss aversion | warranty, protection, insurance | fear exploitation and information asymmetry |
| Convenience | effort avoidance | priority, speed, reduced friction | artificial inconvenience in the base service |

## Decision Gate

1. State the incremental customer benefit in one sentence.
2. Calculate incremental gross margin including support and refund cost.
3. Place the offer only after the base price and job are understood.
4. Show total price and opt-out on the same surface.
5. Measure complaints, refunds, retention, and trust with conversion.
6. Stop if the experiment wins revenue by confusing or trapping users.

## Conflicts & Caveats

> [!warning] Dark-pattern boundary
> A preselected paid option is not evidence of preference. Defaults require explicit visibility, easy reversal, and jurisdiction-specific review.

## Related Concepts

- [[concepts/product-management/product-taste|Product Taste]]
- [[concepts/product-management/feature-vs-platform|Feature vs Platform]]
- [[concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs Benefit]]
- [[concepts/agent-experience/trust-calibration|Trust Calibration]]

## Sources

- [[sources/kakao-vc-upsell-design|Kakao Ventures: Upsell Design Through Value, Reassurance, and Convenience]]

## Open Questions

- What metric captures the trust cost of an upsell?
- Which convenience upgrades are real added value rather than withheld baseline quality?
- How should an AI agent personalize offers without exploiting vulnerability?
