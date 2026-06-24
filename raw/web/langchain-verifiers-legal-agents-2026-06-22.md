---
source_url: https://www.langchain.com/blog/designing-efficient-verifiers-for-legal-agents
captured: 2026-06-22
title: Designing Efficient Verifiers for Legal Agents
authors: [Vivek Trivedy, Jake Broekhuizen, Harrison Chase, Niko Grupen, Gabe Pereyra, Spencer Poff, Julio Pereyra]
published: 2026-06-02
publisher: LangChain Blog
---
# Designing Efficient Verifiers for Legal Agents
**Author:** Vivek Trivedy, Jake Broekhuizen, Harrison Chase (LangChain); Niko Grupen, Gabe Pereyra, Spencer Poff, Julio Pereyra (Harvey) **Published:** 2026-06-02 — LangChain Blog (LangChain Labs, with Harvey)

## Summary

A joint LangChain Labs + Harvey study on how to make LLM **verifiers** (the LLM-as-judge components that score an agent's output as pass/fail against rubric criteria) cheaper while staying close to frontier-model accuracy — both for running **evals at scale** and for **RL post-training** of legal agents. It builds on Harvey's LAB (Legal Agent Benchmark), an open-source benchmark whose initial results show legal work is "far from saturated" by today's agents.

Legal work is hard for agents: it spans many documents that fill context, demands specialized knowledge, and has strict acceptance criteria. LAB verifies like a human reviewer would — every task carries a set of **criteria**, each judged by an individual LLM-judge call that receives the agent output plus the `match_criteria` and emits a `verdict`. Many tasks have 50+ criteria, so one frontier API call per criterion is expensive at scale.

The team tests two efficiency levers: (1) **use fewer tokens** via *batch scoring* (one judge call labels the whole rubric at once instead of one call per criterion); (2) **use cheaper tokens** by swapping the verifier model. Using Opus 4.7 per-criterion as the reference baseline, they compare GPT-5.5, Sonnet 4.6, Claude Haiku 4.5, and DeepSeek-V4-Flash across both per-criterion and batch modes. The headline finding: verifier cost can drop by an **order of magnitude** through batching plus open models, with DeepSeek a strong, far cheaper approximation of Opus. A final lever — targeted **prompt tuning** driven by an auto-research loop over trace divergences — further reduces false-pass rates.

## Key Points

- **Verifiers are a real cost bottleneck** for agent evaluation and RL post-training at scale; post-training amplifies cost because of multiple rollouts per task.
- **Two efficiency levers:** fewer tokens (batch scoring) and cheaper tokens (smaller / open models).
- **Per-criterion vs batch scoring:** per-criterion runs one judge call per rubric requirement (narrow decision window, many calls); batch runs one call labeling every requirement at once (cheaper/faster, but the judge must track the full rubric).
- **Experimental setup:** an agent powered by `Kimi K2.6` produced outputs over **40 public LAB tasks** across Corporate M&A, Tax, Emerging Companies/VC, and Trusts & Estates; these contained **2,348 individual rubric criteria** (each pass/fail). Opus-4.7 per-criterion is the baseline; every verifier run produces the same 2,348 scores for comparison.
- **Metrics measured per verifier run:** Agreement (match to Opus per-criterion labels), False pass (passed a criterion Opus failed), False fail (failed a criterion Opus passed), Cost (observed token cost for the 40-task run). Special attention to **false passes** — in legal, a failed criterion can be escalated for review, but a wrongly-passed one is the dangerous failure mode.
- **Batch is cheaper but drifts more:** across the board batch mode has lower match rates than per-criterion, but is an order of magnitude cheaper for the same model (saves repeated input-token cost).
- **Frontier models disagree with each other:** GPT-5.5 vs Opus reach only a **95.7% match rate**, suggesting some criteria aren't specified tightly enough for even experts/models to apply consistently — so ~95.7% may be a realistic upper bound, not 100%.
- **DeepSeek is a strong, cheap Opus approximation** both per-criterion and in batch, and can run **3 orders of magnitude (60–1000x) more cheaply**, making it a good fit for large-data and RL training domains needing scaled verification.
- **Haiku was cheap but too permissive:** false-pass rates of **48.4% per-criterion / 34.7% batch** — the wrong failure mode for legal.
- **Verification is a 3-way tradeoff** among performance, cost, and time — like most agent-system design.
- **Prompt tuning as a targeted lever:** an auto-research loop compared DeepSeek vs Opus divergences and iterated the prompt (optimizing for false-pass rate). Root cause: DeepSeek too readily passed criteria that were *related* to the requirement but didn't satisfy every material part. The final prompt made the verifier decompose each criterion into an explicit checklist and be cautious under unclear evidence — cutting DeepSeek false-pass from **10.7%→9.5% per-criterion and 15.6%→14.2% batch**.
- **Open models** also let firms **fine-tune bespoke verifiers** for crucial domains, challenging the assumption that closed frontier models are the gold standard to distill toward (since even Opus/GPT-5.5/Sonnet disagree on ~4-5% of labels).
- **Future work:** fine-tuning verifiers and studying their impact on post-training and at-scale evals.

## Diagrams (content from text/captions)

The post embeds several bare `![]()` diagrams with no alt text; their content is reconstructed from the surrounding prose:

- **LAB verification flow** (`LAB_verification_dark`): depicts the LAB scoring model — each task has a set of criteria; the verifier model receives the agent output plus a `match_criteria` per criterion and emits a `verdict` (pass/fail) per criterion; tasks can have 50+ criteria, each its own LLM call.
- **Score modes** (`score_modes_dark`): contrasts the two architectures — **Per-criterion scoring** = one judge call per rubric requirement; **Batch scoring** = one judge call per task that labels every rubric requirement at once.
- **Cost vs label drift scatter** (`cost_drift_dark`): x-axis = verifier cost per 1,000 rubric criteria; y-axis = disagreement with Opus per-criterion labels (`100% − agreement`); lower-and-further-left is better. Conveys that batch modes sit lower-cost but higher-drift than per-criterion; DeepSeek sits far left (cheap) near Opus accuracy; Haiku is cheap but high-drift/permissive; GPT-5.5 and Opus disagree ~4.3% (95.7% match).
- **RL post-training cost** (`rl_cost_dark`): illustrates that verification cost is amplified during RL post-training due to multiple rollouts per task; extrapolation shows DeepSeek can run ~60–1000x cheaper than frontier verifiers at scale, important for domains not easily programmatically verifiable that still need LLM-as-judge reward signals.

(No exact numeric tables are rendered as text in the post beyond the figures; the pass-rate and match-rate numbers above come from the body prose.)

## Short Quotes

- "Verifiers can be a cost bottleneck for running agent evaluations and RL post-training at scale."
- "We find we can reduce verifier costs by an order of magnitude by batching verifiers and using open models."
- "Even frontier models like GPT-5.5 and Opus disagree on labels — they only have a 95.7% match rate."
- "[Haiku's] false-pass rates were 48.4% per-criterion and 34.7% batch, which is the wrong failure mode for legal verification."
- "A lot of work assumes that frontier closed models are the gold standard to distill towards, but even Opus, GPT-5.5, and Sonnet disagree on roughly 4-5% of labels in this study."
