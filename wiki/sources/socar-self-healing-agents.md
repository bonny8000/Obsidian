---
type: source
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [agentic-engineering, ai-agent, production, langgraph, mcp-integration, human-in-the-loop, reliability, structured-output, case-study, automation]
source_path: raw/web/socar-agentic-engineering-in-production-2026-07-24.md
source_url: https://tech.socar.kr/dev/2026/07/22/agentic-engineering-in-production
authors: [Tonic, Jensen]
sources: []
ingest_level: deep
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.88
---

# SOCAR (2026): AI Agents That Self-Repair Failures

## Citation

Tonic & Jensen, 「장애를 스스로 복구하는 AI 에이전트」 *(AI Agents That Self-Repair Failures)*, **SOCAR Tech Blog**, Backend Engineering, 2026-07-22.

**Source type:** First-party production engineering case study, with reported metrics.
**Raw capture:** [[raw/web/socar-agentic-engineering-in-production-2026-07-24|socar-agentic-engineering-in-production-2026-07-24]]

## Summary

The most evidentially strong source in this cluster: a **two-month production deployment** of an LLM agent that detects, diagnoses and repairs integration failures against 50+ third-party parking operators whose sites and APIs change without notice. The headline is not the model — it is the **constraint architecture** around the model. Rule-based automation had been costing roughly 300,000 failed applications and 165,000 refunds a year; the agent cut mean incident response from 4 hours to under 5 minutes and recovered 7,267 real cases in two months.

## Key Claims

- **Rule-based automation fails against uncontrolled third-party drift** — the failure mode is unpredictable UI/API change across many parties you do not own.
- **Constrained sequential stages beat open-ended agency.** Confining the LLM to login → search → discount → check → compare outperformed letting it categorize the problem itself.
- **Hallucination is a code problem, not a prompt problem.** The safeguards that worked were structural: credential isolation, structured output schemas, loop termination, semantic validation.
- **HITL belongs at the deployment boundary.** Automatic recovery is acceptable; automatic deployment is not. Agents open **Draft PRs only**.
- **Agentic observation surfaces failures monitoring cannot see** — the "phantom incident," where an operator silently migrated API v1 → v2 with zero production errors.

## Useful Examples

| Metric | Before | After |
|---|---|---|
| Annual failures | ~300,000 | — |
| Annual refunds | ~165,000 | — |
| Mean incident response | 4 hours | **under 5 min** |
| PoC classification accuracy | — | **100%** (186 cases) |
| Recoveries in first 2 months | — | **7,267** |

- **Credential isolation:** the LLM receives only element references (CSS selectors); the `login` tool injects credentials via closure, so passwords never enter prompts or logs.
- **Retry asymmetry:** popups are auto-dismissed and read-only operations retried — but retry is *blocked* for write operations, preventing double discount application.
- **The design mistake they corrected:** the first architecture split agents by root cause (DOM / Network / Policy). It failed because pre-classification itself requires analysis (circular dependency) and misclassification cascades unrecoverably.

## Constraints / Caveats

- **PoC evaluation was manual** — two authors annotating 186 failure logs offline. No automated eval framework; LangWatch named as future work. The 100% figure should be read as "100% on a small hand-labeled set," not a general accuracy claim.
- **The compare node runs only on failure events**, so silent drift in healthy systems still escapes detection without explicit triggering.
- **Cooldowns trade latency for load** — 1-hour per-ticket and per-venue windows delay later recoveries at the same venue.
- **Baseline schema maintenance is a standing burden**; operator sites change faster than baselines are updated.
- **Scope is 50 major operators**; scalability beyond that cohort is untested.

## Design Implications

- **Separate code concerns from AI concerns**: "code should fix what code can fix; delegate to AI only what AI uniquely does."
- **Defend at three levels** — *action* (make misuse structurally impossible), *behavior* (never trust self-reported success; validate independently), *context* (show only what is needed; hints as data, not prompt text).
- **Store operator-specific knowledge as data, not prompt text**, so it can be updated without touching the model layer.
- **Fix diagnostic logging before deploying agentic recovery** — the agent's forensics are only as good as the error messages beneath it.
- **Calibrate confidence with labeled examples** spanning the range (0.75 uncertain → 0.95 certain), including explicit negatives.

## Tensions

- **Against [[wiki/sources/ai-as-senior-hire-not-intern|"AI as a senior hire"]]:** this is the strongest counter-evidence in the cluster. SOCAR's result came from *removing* agent discretion, not granting it. The reconciliation: seniority of *briefing* is compatible with tight bounds on *action*, and consequence decides which dominates.
- Structured constraint raises maintenance cost (baseline schemas) — it trades model flexibility for engineering burden, which only pays at sufficient volume.

## Open Questions

- Does the sequential-stage design generalize beyond workflows with a natural human script?
- What is the real accuracy outside the 186-case hand-labeled set?
- At what integration count does baseline-schema maintenance exceed the cost it saves?

## Concepts Linked from This Source

- [[wiki/concepts/infrastructure-dev/agent-defense-in-depth|Agent Defense in Depth]]
- [[wiki/concepts/infrastructure-dev/agentic-engineering|Agentic Engineering]]
- [[wiki/concepts/ai-agents/approval-gate|Approval Gate]]
- [[wiki/concepts/ux-research/human-in-the-loop|Human in the Loop]]
- [[wiki/concepts/ai-agents/context-engineering|Context Engineering]]

## LLM Use

The **reference case** for any argument about agents in production. Cite it for: constraint architecture, HITL placement, the cost of open-ended agency, and realistic reliability numbers. It is the strongest available rebuttal to "just give the agent more autonomy." Prefer it over opinion sources when the two conflict.

## Reliability Notes

- **First-party production report with concrete metrics** — the highest evidential grade in this cluster, hence confidence 0.88 rather than higher: the numbers are self-reported and not independently audited.
- **Ingested from an AI-generated extraction of a Korean-language post, not a verbatim read.** Figures should be re-verified against the original before external citation.
- Vendor-neutral: the team names trade-offs against alternatives they rejected (OpenAI Agents SDK, Claude Agent SDK), which raises credibility.
