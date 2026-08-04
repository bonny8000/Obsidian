---
type: concept
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [concept, ux-research, ux-metrics, measurement-validity, adaptive-systems, personalization, engagement, trajectory, benchmarking]
sources: [saeidehbakhshi-usability-metrics-static-product]
confidence: 0.72
---

# Measurement Under Adaptation

> [!abstract] Summary
> Usability measurement presumes a stationary object of study. Personalised and adaptive systems violate that presumption twice — **across users** (each sees a differently-trained product) and **within a user over time** (the product changes as they use it). The consequence is not noisier metrics. It is metrics that stay numerically precise while their referent moves underneath them.
>
> *"The number may be precise while the underlying construct it is measuring is not the same thing."* — [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026)]]

## Why It Matters

Every standard usability metric — task time, completion, error rate, engagement — was defined against a fixed interface. On an adaptive product every one of them becomes conditional, and the conditions are almost never reported:

> "The score is conditional on the user, their history, the state of the system, and the stage of use."

This is a **validity** problem, not a precision problem, which is why more participants do not fix it. A benchmark run twice on a personalising product is not measuring the same thing twice.

## Key Claims

- **Two independent violations.** *"Different users are using different versions of the product."* And: *"The product changes as the same person uses it."* Either alone breaks comparability; together they make an unconditioned score uninterpretable.

- **Task success stops being definable in open-ended products.** *"When a user opens a video recommendation feed, it is not clear what should count as success."* No task was specified, so completion has no referent.

- **Low effort is ambiguous, not good.** *"Less effort can mean better support, and it can also mean the user had less room to compare, question, or change what happened."* This inverts the default reading of the field's most-used metric. One-click purchase is the case: frictionless, and it removes price comparison, alternatives, and awareness of the commitment.

- **Every behavioural metric on an adaptive surface has two readings the metric cannot distinguish:**

  | Observation | Reading A | Reading B |
  |---|---|---|
  | More scrolling | Bad recommendations | Active exploration |
  | Video watched | Satisfying feed | Effective clickbait |
  | Daily engagement | Valued habit | Narrowed loop |
  | Less effort | Better support | Less room to compare |

- **The circularity problem.** *"The system shapes the behavior and it later uses that same behavior as evidence of what the user wants."* The loop: system infers a preference → shows more of it → creates more opportunity for the same behaviour → reduces exposure to alternatives → the user cannot demonstrate breadth → repetition reads as confirmation. **The evidence is not merely correlated with the system's action; it is produced by it.**

- **Which yields the finding that should worry anyone reporting engagement:** *"Engagement may rise while the experience gets more limited and more repetitive."*

- **Attitudinal constructs do not collapse.** *"Satisfaction, trust, control, and usefulness are not interchangeable summaries of quality."* Named divergences: useful but hard to control; enjoyable without being trusted; satisfying in-session but not across weeks; trusting one recommendation but not the system.

## The Four Dimensions

Bakhshi's proposed decomposition — offered explicitly **not** as a replacement north-star score:

| Dimension | The question | Why the standard toolkit misses it |
|---|---|---|
| **Goal** | Whose objective, under what conditions? | Assumed given by the task script |
| **Interaction** | Usable *and* [[wiki/concepts/ux-research/steerability\|steerable]]? | Steerability has no standard instrument |
| **Outcome** | Did completing it leave the user better off? | Conflated with completion |
| **Trajectory** | Which way is this going across weeks? | Structurally invisible to a snapshot |

**Trajectory is the dimension a session cannot see, and on an adaptive product the direction of change is the finding.**

## The Reporting Standard

The most portable and most immediately usable thing in the concept:

> "Make the conditions of our measures explicit: whose goal, which product state, what outcome, and what stage of use?"

Four items, on the slide, next to the number. Requires no new instrument and no budget.

## Detecting Narrowing

The one operational move the source supplies: **track what the user was shown separately from what the user did**, and measure exposure diversity. Without that split, narrowing and preference are indistinguishable in the data — which is why engagement dashboards cannot see the failure they are most likely to be causing.

## ⚖️ Conflicts & Caveats

> [!warning] No evidence, and nothing operationalised
> The source is conceptual critique with no data, no worked example, and no instruments for steerability or trajectory. The argument is a *validity* argument, which does not require data to be sound — but it also supplies no next step beyond the reporting standard.

> [!warning] Trajectory has no sampling guidance
> How often you must measure to detect direction rather than noise is the question that decides affordability, and it is unaddressed.

> [!warning] The hardest inference is stated, not solved
> Separating genuine preference change from system-induced narrowing gets no method. Exposure diversity narrows the gap; it may not close it without an intervention that removes the system's constraint.

> [!warning] The incentive conflict is the real obstacle
> The critique assumes an organisation that wants to know. Where engagement *is* the business metric — and per [[wiki/concepts/product-management/ai-advertising|AI advertising]], where non-verification is commercially valuable — "engagement rose while the experience narrowed" is not a measurement flaw to be fixed. It is the product working. The source never says this, and it is why the exposure-diversity recommendation will be resisted exactly where it matters most.

> [!warning] Internal tension
> The essay rejects collapsing quality into one score, then proposes four dimensions with no instruments — which in practice is either four scores or no measurement.

**Against [[wiki/concepts/ux-research/ux-performance-benchmarking|UX performance benchmarking]] as practised.** Benchmarking's value is comparability over time and against competitors. If the score is conditional on user, history, system state, and stage, comparability is not degraded — it is *unwarranted* unless the conditions are pinned.

## 🔗 Related Concepts

- [[wiki/concepts/ux-research/steerability|Steerability]] — the interaction dimension's missing half.
- [[wiki/concepts/ux-research/ux-metrics|UX Metrics]] — the parent frame.
- [[wiki/concepts/ux-research/ai-ux-measurement-constructs|AI UX Measurement Constructs]] — an instrument whose validity conditions this concept says are moving.
- [[wiki/concepts/ux-research/ux-performance-benchmarking|UX Performance Benchmarking]] — the practice most directly undermined.
- [[wiki/concepts/ux-research/reliability-vs-validity|Reliability vs. Validity]] — the distinction this rests on.
- [[wiki/concepts/ux-research/validity-and-decision-relevance|Validity and Decision Relevance]]
- [[wiki/concepts/ux-research/algorithmic-self|Algorithmic Self]] — the same feedback loop at the individual level.
- [[wiki/concepts/ux-research/algorithmic-monoculture|Algorithmic Monoculture]] — the same loop at population level.
- [[wiki/concepts/agent-experience/satisfaction-vs-benefit|Satisfaction vs. Benefit]] — the same warning, extended here from self-report to behavioural metrics.
- [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]] — the product class this concept is about.
- [[wiki/methods/longitudinal-research|Longitudinal Research]] — the design trajectory requires.
- [[wiki/methods/benchmark-studies|Benchmark Studies]] — where the conditionality bites hardest.

## 📚 Sources

- [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026): Usability Metrics Assume the Product Stays Still]] — sole source. The two violations, the four dimensions, the circularity argument, the reporting standard, and the effort-ambiguity claim.

## ❓ Open Questions

- How often must trajectory be sampled to detect direction rather than noise?
- Can exposure diversity plus behaviour separate real preference change from induced narrowing, or does that inference require an intervention?
- What is the minimum reportable condition set that keeps benchmarking honest without making it unaffordable?
- Does the four-dimension frame survive an organisation whose business metric is the engagement number it distrusts?
- Do any of the vault's existing benchmark or metric pages currently report conditions? (Answer, as of 2026-08-04: no. That is a backfill item, not a finding.)
