---
source_url: https://clova.ai/en/tech-blog/split-the-conflict-merge-the-gains-merit-an-efficient-post-training-strategy-for-llms
captured: 2026-07-02
title: 'Split the conflict, merge the gains: MERIT, an efficient post-training strategy for LLMs'
authors: [Minsik Choi, Geewook Kim]
published: 2026-07-01
publisher: NAVER Cloud CLOVA Tech Blog
related_paper: https://arxiv.org/abs/2606.01717
capture_method: Defuddle Markdown extraction plus arXiv abstract verification
---

# MERIT: conflict-aware decentralized instruction tuning

## Capture status

- Full CLOVA article extracted with Defuddle on 2026-07-02.
- The linked paper title, authors, method, and headline result were checked against arXiv:2606.01717.
- Figures and equations were represented by their captions and surrounding explanation; image pixels were not copied into the vault.
- This card is an AI-authored evidence summary.

## Problem

Large instruction mixtures create two coupled costs:

1. **Gradient conflict / negative transfer:** datasets pulling parameters in different directions can improve one capability while degrading another.
2. **Communication overhead:** centralized joint training requires frequent cross-GPU gradient synchronization, which assumes dense high-bandwidth infrastructure.

## MERIT pipeline

MERIT (Merge-Ready Instruction Tuning) reframes post-training as a partition-and-merge problem:

1. Estimate one representative gradient direction per dataset from roughly 200 samples at a common merge-ready initialization.
2. Build a dataset-pair conflict matrix using cosine similarity.
3. Use PCA to identify dominant axes of disagreement.
4. Recursively create balanced groups so similar datasets train together and strongly conflicting datasets remain separate.
5. Fine-tune every group independently from the same checkpoint, with no communication between groups.
6. Merge once using token-weighted parameter averaging.

The theoretical argument assumes independently tuned models remain in a shared flat basin. Under a local quadratic approximation, merging reduces curvature-weighted variance and acts as a spectral filter, smoothing differences in directions where loss is most sensitive.

## Reported evidence

- Qwen2.5-VL-3B, 136 Vision-FLAN tasks: the paper abstract reports the eight-benchmark average rising from 54.3 under joint training to 57.0 with MERIT.
- Free-form response behavior was better preserved than under joint training; the blog reports LLaVA-W performance close to the original model rather than the short-answer collapse seen in joint fine-tuning.
- A 7B experiment on a 1.6M-example, 176-source mixture matched or exceeded centralized joint training with limited preprocessing overhead.
- The method also transferred to text-only FLAN instruction tuning.
- The blog reports roughly 1.5 hours for gradient extraction plus 30 minutes for the similarity matrix in its 3B setup.

## Durable interpretation

The important design decision is not only how to merge trained models, but which datasets should be trained together. Heterogeneous mixtures should be audited for conflict structure before defaulting to one centralized run.

## Caveats

- This is a first-party NAVER Cloud explanation of its own ICML 2026 paper.
- Merge quality depends on a shared, already aligned initialization and compatible parameter space.
- Dataset-gradient estimation, PCA dimensions, group count, and balance constraints are new hyperparameters.
- Benchmark gains do not establish improved safety, calibration, or generalization outside the evaluated mixtures.
- Independent training reduces communication but still requires enough aggregate compute to fine-tune every partition.

## Links

- [CLOVA article](https://clova.ai/en/tech-blog/split-the-conflict-merge-the-gains-merit-an-efficient-post-training-strategy-for-llms)
- [Paper: Decentralized Instruction Tuning](https://arxiv.org/abs/2606.01717)
- [MERIT code](https://github.com/naver-ai/merit)
