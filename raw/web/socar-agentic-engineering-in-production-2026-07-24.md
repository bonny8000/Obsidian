---
source_url: https://tech.socar.kr/dev/2026/07/22/agentic-engineering-in-production
captured: 2026-07-24
title: "장애를 스스로 복구하는 AI 에이전트"
authors: [Tonic, Jensen]
published: 2026-07-22
publisher: SOCAR Tech Blog
language: ko
---

# AI Agents That Self-Repair Failures — SOCAR Tech Blog

**Original title (ko):** 「장애를 스스로 복구하는 AI 에이전트」 · Backend Engineering
**Published:** 2026-07-22 · **Captured:** 2026-07-24
**Capture note:** AI-written summary of a Korean-language engineering post. Full text not reproduced.

## Summary

A production case study — rare for its numbers — of agentic engineering at SOCAR. A discount-application batch system integrates with **50+ third-party parking operator** sites and APIs, each of which changes without notice. Rule-based automation could not keep up, costing roughly **300,000 failed applications and 165,000 refunds annually**. The team built an LLM agent that detects, diagnoses and repairs these failures inside a **strictly constrained code framework**, and reports two months of production results.

## Key Points

- **Rule-based automation fails at this kind of scale** — the failure mode is unpredictable UI/API drift across many uncontrolled third parties.
- **Constrained beats open-ended.** The LLM is confined to discrete sequential stages — login → search → discount → check → compare — rather than being allowed to categorize the problem itself.
- **Defense must be non-AI.** Hallucination cannot be prompted away; the safeguards that worked are code-level: credential isolation, structured output schemas, loop termination conditions, semantic validation.
- **HITL at the deployment boundary.** Agents recover failures automatically but only ever open **Draft pull requests**; humans gate every code change.

### Results reported

| Metric | Value |
|---|---|
| Annual failures before | ~300,000 |
| Annual refunds before | ~165,000 |
| Average incident response | 4 hours → **under 5 minutes** |
| PoC failure-classification accuracy | **100%** on 186 test cases |
| Actual recoveries, 2 months post-deploy | **7,267** |
| PoC duration | 2 weeks |

### Architecture and stack

- **LangGraph** chosen over OpenAI Agents SDK and Claude Agent SDK for low-level control of state and routing via `StateGraph`.
- **Playwright MCP** for structured accessibility-tree snapshots rather than pixel screenshots; ref-based element identification.
- **Gemini 3.1 Pro**; cost per recovery in the hundreds of KRW.
- **Structured output via Zod schemas** — predictable responses, and testability through mock substitution.
- **Few-shot prompting with confidence anchoring** — labeled examples spanning 0.75 (uncertain) to 0.95 (certain), including explicit "no change" negatives.
- **Semaphore-based concurrency limiting** caps simultaneous browser instances, preventing OOM during burst failures.
- **Baseline schema as source of truth** — per-operator JSON files storing expected screen structure and API contracts; observations are compared to these, never to model recall.
- **Context isolation** — each stage receives only its own baseline schema and hints, with no cross-stage conversation history.
- **Operator hints stored as data, not prompts** — e.g. "this site disables search results after 30 seconds if the checkbox is enabled" lives in JSON.

### The design mistake they corrected

The first design split agents **by root cause** (DOM Agent, Network Agent, Policy Agent). It failed for two reasons: pre-classification itself requires analysis, creating a circular dependency; and misclassification cascades — a login failure routed to the Network Agent is unrecoverable. The fix was **sequential stages mirroring the human workflow**, with condition-based routing on a `systemType` field replacing LLM runtime decisions wherever possible.

### The "phantom incident"

An agent detected that a major operator had silently migrated from API v1 to v2 **despite zero production errors**. Conventional monitoring would not have caught this until v1 shutdown caused mass failure.

### Credential handling

The LLM never sees passwords. It receives only element references (CSS selectors); the `login` tool injects credentials via closure, so they never appear in logs or prompts.

## Stated Caveats

- **Evaluation during PoC was manual** — offline annotation of 186 real failure logs by the two authors. No automated eval framework yet (LangWatch named as future work).
- **The compare node only runs on failure events**, so silent changes in otherwise healthy systems still go undetected without explicit triggering.
- **Cooldown policies trade latency for load** — 1-hour per-ticket and per-venue cooldowns delay recovery of later failures at the same venue.
- **Baseline schema maintenance is a real burden**; operator sites change faster than the baseline data is updated.
- **Scope limited to 50 major operators**; scalability beyond that cohort is untested.

## Practical Recommendations

1. **Separate code concerns from AI concerns** — "code should fix what code can fix; delegate to AI only what AI uniquely does."
2. **Defend at three levels:** *action* (make misuse structurally impossible — no credential access, no browsing without a snapshot), *behavior* (never trust self-reported success; validate independently), *context* (show only what is needed; data-driven hints over monolithic prompts).
3. **Enforce response schemas** for both predictability and unit testing.
4. **Calibrate confidence thresholds with labeled examples** to prevent drift.
5. **Gate deployment at HITL** — auto-recovery yes, auto-deployment no.
6. **Fix diagnostic logging before deploying agentic recovery**; error messages must support forensics.

## Emergent Benefits Observed

- The system surfaced **pre-existing batch defects** traditional monitoring never caught (false-positive failures, missing root-cause context).
- Comprehensive agent-driven observation across 50 operators exposed silent incompatibilities and deprecated API usage *before* they caused outages.
