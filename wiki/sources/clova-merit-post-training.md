---
type: source
status: active
created: 2026-07-02
updated: 2026-07-02
tags: [llm, post-training, instruction-tuning, gradient-conflict, model-merging, distributed-training, merit]
sources: []
source_path: raw/web/clova-merit-post-training-2026-07-02.md
source_url: https://clova.ai/en/tech-blog/split-the-conflict-merge-the-gains-merit-an-efficient-post-training-strategy-for-llms
authors: [Minsik Choi, Geewook Kim]
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.88
---

# CLOVA: MERIT Conflict-Aware Post-Training

> [!info] Metadata
> - **Authors:** Minsik Choi and Geewook Kim
> - **Published:** 2026-07-01
> - **Type:** first-party research explainer for an ICML 2026 paper
> - **Raw card:** [[raw/web/clova-merit-post-training-2026-07-02]]
> - **Paper:** [arXiv:2606.01717](https://arxiv.org/abs/2606.01717)

## Citation

Choi, M., & Kim, G. (2026, July 1). *Split the conflict, merge the gains: MERIT, an efficient post-training strategy for LLMs.* NAVER Cloud CLOVA Tech Blog. Companion to *Decentralized Instruction Tuning: Conflict-Aware Splitting and Weight Merging*.

## Summary

MERIT replaces one synchronized instruction-tuning run with conflict-aware dataset partitioning, independent fine-tuning, and a single token-weighted model merge. It aims to reduce both negative transfer between heterogeneous datasets and the communication cost of all-reduce-heavy joint training.

## Key Claims

- A heterogeneous instruction mixture should be treated as a structure of dataset-level gradient relationships, not an undifferentiated pool.
- Dataset gradients estimated from a small sample can form a cosine-similarity conflict matrix.
- PCA exposes dominant conflict axes; balanced recursive partitioning keeps aligned datasets together and separates strongly conflicting ones.
- Models independently tuned from the same aligned checkpoint can remain merge-compatible within a shared flat basin.
- Token-weighted parameter averaging can preserve complementary learning while smoothing harmful variation, with only one communication event at the end.
- The paper reports higher average performance than joint training on Qwen2.5-VL-3B and similar benefits in 7B multimodal and text-only settings.

## Useful Examples

- The five-stage operational pipeline: gradient estimation → conflict matrix → PCA → balanced partitioning → independent training and one-shot merge.
- Qwen2.5-VL-3B on 136 Vision-FLAN tasks: 54.3 joint-training average versus 57.0 for MERIT in the paper abstract.
- Free-form-answer preservation: the blog reports that joint training sharply reduced LLaVA-W performance while MERIT stayed close to the starting model.
- Incremental dataset addition only requires new cross-similarities rather than recomputing the entire matrix.

## Constraints / Caveats

- This is a first-party explanation of the authors' own method; consult the paper and code for implementation details.
- Weight averaging assumes matching architecture and parameter alignment around a merge-ready initialization.
- The method adds preprocessing, partition-count, and balancing decisions that can fail on other mixtures.
- Communication is reduced, not total compute; every group still requires fine-tuning.
- Benchmark performance does not establish safety, calibration, or robustness under distribution shift.

## Design Implications

- Audit multi-domain post-training data for negative transfer before scaling a centralized mixture.
- Treat dataset grouping as a model-design decision with measurable diagnostics.
- In fragmented GPU environments, independent partitions can turn limited interconnect into a tractable training topology.
- Track capability and response-style retention separately; a higher aggregate average can hide a short-answer or conversation-quality collapse.
- Preserve initialization, token budgets, and merge weights as first-class provenance for reproducibility.

## Tensions

- Splitting protects conflicting capabilities but may reduce useful cross-task transfer inside a joint run.
- A simple parameter merge is operationally attractive precisely where its flat-basin assumptions may be hardest to verify.
- Conflict-aware partitions optimize gradient geometry, which may not align with human categories, safety boundaries, or deployment domains.

## Open Questions

- How stable are the partitions across checkpoints, model scales, and gradient sample sizes?
- How should safety and preference datasets be weighted when their gradients conflict with capability datasets?
- Can the conflict matrix become a reusable data-governance artifact for later ablations?
- What failure signal indicates that independently tuned models left the shared merge basin?

## Concepts Linked

- [[concepts/ai-agents/conflict-aware-instruction-tuning|Conflict-Aware Instruction Tuning]]
- [[concepts/ai-agents/model-neutrality|Model Neutrality]]
- [[concepts/ai-agents/model-escalation-gate|Model Escalation Gate]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]

## LLM Use

- **Use for:** designing decentralized instruction-tuning experiments, reasoning about gradient conflict, and comparing centralized training with split-train-merge strategies.
- **Do not use for:** assuming arbitrary fine-tuned checkpoints can be averaged safely.
- **Best prompt pattern:** provide model initialization, dataset list, gradient-estimation budget, partition count, token counts, and per-capability metrics.

## Reliability Notes

> [!warning] Caveats
> Method and headline metrics were verified against the arXiv abstract. The blog remains a first-party explainer and should not replace the paper for implementation or statistical review.

## Backfill Status

- New standard ingest completed 2026-07-02.
