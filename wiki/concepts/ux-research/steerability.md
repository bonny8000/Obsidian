---
type: concept
status: active
created: 2026-08-04
updated: 2026-08-04
tags: [concept, ux-research, steerability, adaptive-systems, personalization, agency, control, ux-metrics, agent-experience]
sources: [saeidehbakhshi-usability-metrics-static-product]
confidence: 0.68
---

# Steerability

> [!abstract] Summary
> Usability asks whether a user can **operate** the interface. Steerability asks whether a user can **redirect a system that has already built a model of them** — and whether the redirection lasts.
>
> Named as usability's missing partner for adaptive systems by [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026)]], as half of the Interaction dimension in her four-dimension framework.

## Why It Matters

A static interface either affords an action or does not, and usability testing settles it. A personalising system has a *representation of the user* sitting between their intent and the output. Operating the controls is no longer sufficient: the question is whether the user can change that representation.

The three questions, in increasing order of how often products fail them:

1. **Legibility** — can the user work out how the system is personalising for them?
2. **Redirection** — can the user change it?
3. **Persistence** — **do the corrections survive the next session, or revert?**

The third is the one that distinguishes steerability from every neighbouring concept, and it is the one products fail. A system that accepts a correction and quietly reverts to its learned model has offered control without granting it — the interaction equivalent of a placebo button.

## Key Claims

- **Steerability is additional to usability, not a subtype.** A perfectly usable feed can be unsteerable: every control works, and none of them changes what you are shown tomorrow.

- **Persistence is the diagnostic.** Redirection that does not persist is indistinguishable from redirection that never happened, from the user's side and from the data.

- **It is directly observable.** Unlike most attitudinal constructs, steerability can be measured behaviourally: issue a correction, return in a later session, check whether the change held. This makes it one of the more tractable open measurement problems in the vault.

- **Its absence is what makes the circularity problem stick.** [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement under adaptation]] describes a loop in which a system's inference manufactures its own confirming evidence. Steerability is the escape hatch: a user who can effectively redirect the model can break the loop. Where steerability fails, the loop is closed and the narrowing continues while engagement looks healthy.

- **It is a precondition for meaningful consent to personalisation.** Agreeing to be personalised for means little if the resulting model cannot be corrected.

## Distinguished From Neighbours

| Concept | The question it asks | Difference |
|---|---|---|
| **Steerability** | Can I change the model the system has of me, durably? | About a *learned representation*; persistence is part of the test |
| [[wiki/concepts/ux-research/progressive-user-control\|Progressive User Control]] | How much autonomy do I grant the system? | About *autonomy level*, set in advance, not about correcting a model |
| [[wiki/concepts/ux-research/designing-for-agency\|Designing for Agency]] | Do I have meaningful choice and authorship? | Broader value frame; steerability is one mechanism under it |
| [[wiki/concepts/agent-experience/error-recovery\|Error Recovery]] | Can I undo this action? | Single action, immediate scope; steerability is about the model that produced it |
| [[wiki/concepts/agent-experience/trust-calibration\|Trust Calibration]] | Should I rely on this? | About appropriate reliance; unsteerability is a reason not to |

The clean way to hold it: **error recovery undoes an output; steerability changes the thing that produces outputs.**

## Practical Guidance

- **Add a three-part steerability probe** to any study of an adaptive product: ask the participant to explain how it personalises, ask them to change it, then bring them back and check whether the change held.
- **Test persistence across sessions, not within one.** Within-session compliance is cheap for a system to fake.
- **Distinguish a correction that is recorded from one that is weighted.** Many systems accept the signal and let the learned model outvote it — which looks like steerability in the UI and is not.
- **When designing controls, state the half-life.** "Show me less of this" with no stated scope or duration is not a control the user can reason about.
- **Report steerability separately from satisfaction.** Per Bakhshi, users routinely find products *"useful but hard to control."*

## ⚖️ Conflicts & Caveats

> [!warning] No instrument exists
> The concept is named and defended; nothing in the source or this vault operationalises it. There are no items, no scoring, no benchmark. What exists is the three-question structure above, which is this page's reading of the source rather than a validated protocol.

> [!warning] Single source, no evidence
> Bakhshi's essay is conceptual critique with no data. Nothing here has been demonstrated on a real product.

> [!warning] Steerability may trade against personalisation quality
> A system that fully obeys corrections learns less from behaviour. The trade-off is real and unexamined by the source — a maximally steerable recommender is a manual filter, which is a product users have historically rejected.

> [!warning] Not obviously wanted by the business
> Where the learned model drives the business metric, durable user override is a cost. Expect the persistence test to be the hardest thing to get shipped, for the same reason it is the most informative.

## 🔗 Related Concepts

- [[wiki/concepts/ux-research/measurement-under-adaptation|Measurement Under Adaptation]] — the parent argument; steerability is half its Interaction dimension.
- [[wiki/concepts/ux-research/progressive-user-control|Progressive User Control]] — adjacent, about autonomy level rather than model correction.
- [[wiki/concepts/ux-research/designing-for-agency|Designing for Agency]] — the value this serves.
- [[wiki/concepts/agent-experience/error-recovery|Error Recovery]] — the output-level counterpart.
- [[wiki/concepts/agent-experience/trust-calibration|Trust Calibration]]
- [[wiki/concepts/agent-experience/natively-adaptive-interfaces|Natively Adaptive Interfaces]] — the product class where this becomes necessary.
- [[wiki/concepts/agent-experience/delegation-spectrum|Delegation Spectrum]] — steerability is what remains of control at higher delegation tiers.
- [[wiki/concepts/ai-agents/agent-memory|Agent Memory]] — an agent's persistent memory of a user is exactly the representation steerability asks about.
- [[wiki/concepts/ux-research/algorithmic-self|Algorithmic Self]] — what an unsteerable model becomes.
- [[wiki/concepts/ux-research/ux-metrics|UX Metrics]]

## 📚 Sources

- [[wiki/sources/saeidehbakhshi-usability-metrics-static-product|Bakhshi (2026): Usability Metrics Assume the Product Stays Still]] — sole source. Names steerability, places it in the Interaction dimension, and supplies the persistence question.

## ❓ Open Questions

- What does a validated steerability instrument look like? This is the most buildable open measurement problem currently in the vault.
- Is persistence binary or graded — how much weight must a correction carry to count?
- Does steerability trade measurably against recommendation quality, and where is the useful point on that curve?
- For agents with long-term memory, is steerability the same construct? The representation is explicit rather than statistical, which should make it *easier* to correct — and no source in the vault has tested whether it is.
- Do users notice when a correction reverts, or do they simply disengage?
