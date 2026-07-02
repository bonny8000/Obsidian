---
type: concept
status: active
created: 2026-07-02
updated: 2026-07-02
tags: [llm, post-training, instruction-tuning, gradient-conflict, model-merging]
sources:
  - sources/clova-merit-post-training
confidence: 0.86
---

# Conflict-Aware Instruction Tuning

> [!abstract] Summary
> Measure how datasets pull a model, train compatible groups independently, and merge once instead of forcing every task through one synchronized mixture.

## Why It Matters

Instruction mixtures can produce negative transfer and expensive synchronization. Conflict-aware tuning makes dataset grouping an explicit optimization artifact and offers a path for fragmented compute without treating all examples as equally compatible.

## Key Claims

- Dataset gradients can represent task direction at a shared initialization.
- Cosine similarity exposes aligned and opposing datasets.
- PCA can compress a large conflict matrix into dominant disagreement axes.
- Balanced partitions keep training workloads practical while separating strong conflicts.
- Merge-ready initialization is a precondition, not an implementation detail.
- Per-capability and style metrics are necessary because aggregate averages can hide collapse.

## MERIT Pattern

```mermaid
flowchart LR
    A[Dataset gradients] --> B[Conflict matrix]
    B --> C[PCA conflict axes]
    C --> D[Balanced partitions]
    D --> E[Independent fine-tuning]
    E --> F[Token-weighted merge]
```

## Conflicts & Caveats

> [!warning] Applicability boundary
> Parameter averaging is not safe for arbitrary checkpoints. Architecture, initialization, optimization path, and token weighting must remain compatible.

## Related Concepts

- [[concepts/ai-agents/model-neutrality|Model Neutrality]]
- [[concepts/ai-agents/multi-agent-coordination|Multi-Agent Coordination]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/ai-agents/product-evals|Product Evals]]

## Sources

- [[sources/clova-merit-post-training|CLOVA: MERIT Conflict-Aware Post-Training]]

## Open Questions

- Should safety and preference datasets be protected as separate conflict groups?
- How stable is a conflict map across model scales and checkpoints?
- Can dataset-conflict provenance become part of a reusable post-training data catalog?
