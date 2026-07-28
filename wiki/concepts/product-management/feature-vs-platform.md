---
type: concept
status: active
created: 2026-06-22
updated: 2026-07-28
tags: [concept, product-strategy, platform, abstraction, ops-tooling, recommendation]
sources: [myrealtrip-polaris-cancellation-recommendation]
confidence: 0.75
---

> [!info] Not the same question as SaaS vs. Platform
> This page is about the **internal build decision** — whether to build a one-off feature or abstract it into a reusable capability. For the **company-level business model** distinction (selling connections vs. selling software that solves a problem, and the metrics that follow), see [[wiki/concepts/product-management/saas-vs-platform|SaaS vs. Platform]]. The two are commonly conflated.

# Feature vs Platform

> [!abstract] Summary
> "A good feature is used once; a good platform keeps solving new problems." When the same underlying question recurs across many requests, abstract the one-off feature into **composable axes + an ops tool** instead of building each request separately.

> [!important] Why it Matters
> Recurring asks (ads, promotions, coupons, recommendations) often reduce to one question — *who, at what moment, what content, in what form.* Recognizing that shared question lets a single structure absorb future requests, and decoupling "who builds" from "who operates" shortens idea → screen time.

## 📝 Key Claims
- The hard part is **recognizing the deeper recurring problem** beneath superficially different requests ("solving a problem leads you to a more fundamental one").
- Re-architect into **composable axes** — e.g. audience / surface / trigger / content — so a specific feature (cancellation-recommendation) becomes one case on a shared structure.
- Add an **ops tool** so the operating org can design exposure policy, placement, content, and schedule themselves — decoupling builders from operators and enabling fast try→measure→change loops.
- Trade-off: building the general structure costs more up front but pays back by absorbing future asks.

## 🔗 Related Concepts
- [[concepts/product-management/discovery-phase|Discovery Phase]]
- [[concepts/ux-research/problem-discovery-model|Problem Discovery Model]]
- [[concepts/product-management/product-roadmap|Product Roadmap]]
- [[concepts/product-management/ai-native-stack|AI-Native Stack]]
- [[concepts/product-management/role-convergence|Role Convergence]]
- [[wiki/concepts/product-management/saas-vs-platform|SaaS vs. Platform]] — the business-model question, distinct from this build decision.

## ⚖️ Conflicts & Caveats
> [!warning] Contradictions
> Premature platforming is its own failure — abstracting before the recurring problem is real adds complexity for no payoff. The case justifies the platform *after* the same question returned repeatedly.

## 📚 Sources
- [[sources/myrealtrip-polaris-cancellation-recommendation|Myrealtrip "Polaris": Cancellation as the Next Trip's Start]]

## ❓ Open Questions
- What signals indicate a feature *should* graduate to a platform vs stay a one-off?
- How far do composable messaging axes (audience/surface/trigger/content) generalize across surfaces?
