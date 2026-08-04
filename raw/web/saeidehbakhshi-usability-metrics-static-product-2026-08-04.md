---
source_url: https://saeidehbakhshi.substack.com/p/we-are-no-longer-testing-the-same
captured: 2026-08-04
title: "Usability Metrics Assume the Product Stays Still"
subtitle: "Why adaptive systems make usability measures harder to interpret"
authors: [Saeideh Bakhshi]
published: 2026-08-02
publisher: Research Toolbox (Substack)
language: en
format: methodological critique essay
note: URL slug is taken from the first section heading, not the title.
---

# Usability Metrics Assume the Product Stays Still — Saeideh Bakhshi

**Author:** Saeideh Bakhshi, *Research Toolbox*.
**Published:** 2026-08-02 · **Captured:** 2026-08-04

AI-written extraction. No full-text reproduction; short quoted phrases only.

---

## Section headings (verbatim, in order)

1. We are no longer testing the same product
2. What counts as success keeps changing
3. The product learns from the behavior it interprets
4. Usability metrics have many assumptions that don't hold for modern products
5. Attitudes do not summarize the experience
6. A broader approach to evaluating experience quality

## Thesis

Usability measurement assumes a stationary object of study. Adaptive and personalised systems violate that assumption twice over — across users and within a single user over time — so the metric can be numerically precise while the construct it measures has changed underneath it.

> "Different users are using different versions of the product."

> "The product changes as the same person uses it."

> "The score is conditional on the user, their history, the state of the system, and the stage of use."

> "The number may be precise while the underlying construct it is measuring is not the same thing."

## Section 2 — success stops being definable

> "When a user opens a video recommendation feed, it is not clear what should count as success."

Open-ended adaptive systems have no predetermined task outcome, so task success cannot be scored the way it is in a bounded usability task.

## Section 3 — the circularity problem

> "The system shapes the behavior and it later uses that same behavior as evidence of what the user wants."

The described loop: the system observes a category preference → shows more of that category → creates more opportunity for the same behaviour → reduces exposure to alternatives → the user cannot demonstrate a broader interest → the repetition reads as confirmation. The confirmation is manufactured by the system's own narrowing.

> "Engagement may rise while the experience gets more limited and more repetitive."

## Section 4 — which assumptions break

| Metric | Assumption that fails |
| --- | --- |
| Effort / time on task | That less effort is better. *"Less effort can mean better support, and it can also mean the user had less room to compare, question, or change what happened."* |
| Completion | That completion means the user's actual goal was met |
| Errors | That the interface is stable enough for an error to be defined |
| Engagement | That more engagement indicates a better experience |

Worked cases:
- **One-click purchase** — effortless, but obscures price, alternatives, and long-term commitment.
- **More scrolling** — either bad recommendations or active exploration; the metric cannot distinguish them.
- **Video watched** — either a satisfying feed or effective clickbait.
- **Daily engagement** — compatible with a narrow, repetitive experience.

## Section 5 — attitudes do not collapse

> "Satisfaction, trust, control, and usefulness are not interchangeable summaries of quality."

Divergences named: useful but hard to control; enjoyable without being trusted; satisfied within a session but not across weeks; trusting an individual recommendation but not the system.

## Section 6 — the four-dimension alternative

| Dimension | What it asks |
| --- | --- |
| **Goal** | Whose objective, under what conditions — not fixed across users or across time |
| **Interaction** | Usability **plus steerability**: can the user redirect the adaptive system? |
| **Outcome** | Did completing the task leave the user better off, measured against their stated goal |
| **Trajectory** | How user, system, and outcomes change across sustained use |

The stated aim is explicitly *not* to replace usability with a different single north-star score.

> "Make the conditions of our measures explicit: whose goal, which product state, what outcome, and what stage of use?"

## Primary illustration

**Short-video recommendation feed.** A new user scrolls past many irrelevant items before choosing, and the novelty is itself pleasurable despite the inefficiency. An experienced user selects faster. Faster selection is not evidence of a better experience — the two users are being measured on different products at different stages.

## Practice recommendations drawn from the piece

1. Document, before measuring: whose goal, which product state, what stage of the relationship, what counts as the outcome.
2. Assess the four dimensions separately instead of computing a composite.
3. Use longitudinal designs so trajectory is observable rather than inferred from a snapshot.
4. Separate **what the user was shown** from **what the user did**; track exposure diversity to detect algorithmic narrowing.
5. Test steerability explicitly: can the user understand the personalisation, redirect it, and do the corrections persist or revert?
6. Report attitudinal constructs separately — do not composite satisfaction, trust, and control.
7. Treat low friction as a question, not a win: measure user understanding alongside ease.
8. Report the segment, product state, and stage with every finding; do not generalise across untested conditions.

## Evidence base

**None.** The piece contains no data, statistics, or empirical study. It is conceptual methodological critique.

## Limits the author acknowledges or leaves open

- No operationalisation is given for steerability or trajectory.
- No sampling guidance for how often trajectory must be measured to detect real change.
- No account of how to distinguish genuine preference change from system-induced narrowing.
- No treatment of feasibility at scale when each user has an individualised product.
- Stated tension in the piece itself: it rejects simplified scoring while proposing a four-dimensional framework with no instruments attached.
