---
type: source
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [cognitive-science, cognitive-effort, cognitive-control, psychology, network-control-theory]
sources: []
confidence: 0.95
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
---
# Trends in Cognitive Sciences: Why is cognitive effort experienced as costly?

**Citation**: Otto, A. R., Westbrook, A., & Daunizeau, J. (2025/2026). "Why is cognitive effort experienced as costly?" *Trends in Cognitive Sciences*, S1364-6613(25)00287-6.
**Source type**: Scientific Article
**Location**: `[[raw/web/cell-tics-cognitive-effort.md]]` / [Original URL](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(25)00287-6)

## Summary
This review article critically examines three leading theoretical perspectives—architectural bottlenecks (opportunity costs), information theory, and network control theory—that attempt to explain *why* the exertion of cognitive effort feels subjectively costly. It shifts the focus from *how much* effort people exert (cost-benefit models) to the fundamental origins of the cost itself, using the N-back working memory task as a common explanatory framework.

## Key claims

### 1. Architectural Constraints and Processing Bottlenecks (Opportunity Costs)
- Cognitive control relies on shared, limited resources to prevent crosstalk and catastrophic interference between tasks.
- Prioritizing resources for one task incurs an **opportunity cost**: the forgone utility of the next-best alternative task (e.g., mind-wandering).
- Bottlenecking density per unit time increases with task complexity (e.g., a 2-back task has more subtasks than a 1-back), limiting parallel processing and thereby increasing subjective effort via opportunity costs.
- High-dimensional task representations aid in flexible task-switching but require higher neural coding levels (metabolic costs).

### 2. Information-Theoretic View
- Effort costs arise from the computational burden of updating prior beliefs to posterior beliefs (inference).
- This informational cost is proportional to the **Kullback-Leibler (KL) divergence** between the prior and posterior probability distributions.
- In complex tasks, selecting a response among many possibilities reduces uncertainty significantly. The larger the reduction in uncertainty (KL divergence), the larger the required effort cost.

### 3. Network Control Theory (The "Controllosphere")
- Grounded in connectomics, this view posits that "automatic" processes guide the brain to easy-to-reach target states, whereas "controlled" processes guide the brain to unstable, hard-to-reach states.
- Reaching and sustaining hard-to-reach states requires substantial metabolic energy (input). 
- Subjective effort is the perceived inefficiency of this energy outlay. The **Controllosphere** is the region of the state space containing these hard-to-reach states.
- Flow states feel effortless because energy expenditure induces motion *outside* the controllosphere, providing detectable progress that offsets the feeling of exertion.

### Convergence between theories
- The information-theoretic and network control views share a metabolic foundation: the KL divergence between prior and posterior distributions essentially approximates the energetic cost of neural control inputs.
- The network control account bridges a tension between the other two models by acknowledging that energy is consumed both by *sustaining* representations (bottleneck view) and *updating* them (information-theoretic view).

## Useful examples
- **N-back load differences:** The theories explain why a 2-back is harder than a 1-back. Bottleneck theory cites higher bottleneck density per trial. Information theory cites a larger KL divergence to represent currently irrelevant items for future trials. Network control theory cites a larger distance between pre- and post-stimulus brain states requiring more energy.

## Concepts linked from this source
- [[wiki/concepts/cognitive-science/opportunity-cost-of-effort|Opportunity Cost of Effort]]
- [[wiki/concepts/cognitive-science/information-theoretic-effort|Information-Theoretic View of Effort]]
- [[wiki/concepts/cognitive-science/network-control-theory-effort|Network Control Theory of Effort]]
- [[wiki/concepts/ux-research/cognitive-load|Cognitive Load]]

## Reliability notes
- Published in *Trends in Cognitive Sciences*, a highly reputable peer-reviewed journal. Represents state-of-the-art theoretical synthesis.
