---
type: source
status: active
created: 2026-06-25
updated: 2026-06-25
tags: [hanwha-life, claude-code, project-based-learning, citizen-development, ai-adoption, domain-expert, ax-labs]
source_path: raw/web/theaxlabs-hanwha-life-claude-code-pbl-2026-06-25.md
source_url: https://theaxlabs.com/cases/한화생명-현업-claude-code-6주-풀스택-빌드
authors: [AX LABS]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---

# AX LABS (2026): Hanwha Life — Business Teams Build Agents Themselves (6-Week Claude Code PBL)

**Publisher:** AX LABS (TheAxLabs), case study (author/date not stated).
**Raw capture:** [[raw/web/theaxlabs-hanwha-life-claude-code-pbl-2026-06-25|theaxlabs-hanwha-life-claude-code-pbl-2026-06-25]]
**URL:** [theaxlabs.com/cases/한화생명-…-풀스택-빌드](https://theaxlabs.com/cases/한화생명-현업-claude-code-6주-풀스택-빌드)

## Citation

AX LABS. (2026). *한화생명 Project Based Learning — 현업이 직접 빌드한 에이전트* [Hanwha Life PBL — Agents Built Directly by Business Teams]. theaxlabs.com. Captured 2026-06-25 into `raw/web/theaxlabs-hanwha-life-claude-code-pbl-2026-06-25.md`.

## Summary

A 6-week **Project-Based-Learning (PBL)** program where **20 Hanwha Life (한화생명) business experts with no coding background** built working AI agents themselves using **Claude Code**, supported by 4 AX LABS consultants. Thesis: connecting domain expertise to an AI coding environment requires **running a full project cycle** (not lectures), so deliverables remain **owned, extendable assets of the business teams** rather than contractor output.

## Key Claims

- **Cohort:** 20 domain experts (7–10+ yrs, no coding) in **5 units of 4**; support = 1 PM + 3 on-site advisors, daily 8 AM–6 PM.
- **6-week arc:** Wk1 Definition (design thinking, personas, journeys → spec + architecture draft) → Wk2 Data & Architecture (**real** sources/schema/access → live data env) → Wk3–4 Building (Claude Code; mid-Wk4 cross-unit review) → Wk5 Refinement (live-data validation, UX) → Wk6 Executive presentations.
- **Four method principles:** (1) **Boundary-setting before code** — define what the agent does/doesn't + role boundaries + **Human-in-the-Loop** decision points up front; (2) **Real-data-first** (not demo data); (3) **Direct code ownership** (participants write the code; consultants advise, don't ghost-write); (4) **Parallel, non-uniform pacing** (5 units, different topics/speeds; consultants rotate 2-team ↔ 1:1; same-day unblocking).
- **Quoted principle:** problem definition, data verification, feasible structuring, and code-unblocking must live in **one continuous flow** ("…한 흐름 안에 있어야 했습니다").
- **Outcomes:** 20 non-developers delivered near-full-stack agents independently; retained ability to extend/maintain; all 5 units passed executive demos with business-led explanations.

## Useful Examples

- **5 units × 4 non-developers** each shipping an agent in 6 weeks as a concrete capability-building model.
- **Week-2 "real data environment" gate** — locking real sources/schema/permissions before building, so outputs reflect actual business conditions.
- **Boundary + HITL definition before code** as the anti-scope-creep move.

## Constraints / Caveats

- **Vendor case study (AX LABS)** — success-biased; no failure rate, post-program sustainment metrics, or agent-quality audit captured.
- Heavy hands-on support (4 consultants, on-site daily) — results may not hold for self-serve or lightly-supported rollouts.
- Regulated insurer context (data access, compliance) shapes the "real-data-first" emphasis; may differ elsewhere.
- AX LABS already in vault via [[sources/theaxlabs-contaminated-memory-performance|Contaminated Memory]] — same vendor, independent topic.

## Design Implications

- A **structured-cohort** template for [[concepts/infrastructure-dev/ai-adoption-culture|AI Adoption Culture]] — the complement to Toss's **bottom-up** [[sources/toss-tossplace-ai-surf-day|AI Surf Day]] model.
- Strong evidence for [[concepts/product-management/domain-expert-as-builder|Domain Expert as Builder]]: with the right scaffold (boundaries, real data, direct ownership), non-developers ship and *keep* agents.
- The "one continuous flow" principle (define → data → structure → unblock) mirrors [[sources/dusskapark-product-designer-codex|Park's planning-first + verification-loop]] discipline — same lesson from two very different builders.
- Reinforces [[concepts/ai-agents/vibe-coding|Vibe Coding]] with [[concepts/ux-research/human-in-the-loop|HITL]] gates as the responsible default.

## Tensions

- **Heavy support vs. scalability** — 1 consultant per ~1–2 teams makes results real but expensive to scale.
- **Empowerment vs. maintainability/governance** — business-owned agents avoid contractor lock-in but raise long-term quality/security ownership questions (cf. [[sources/theaxlabs-contaminated-memory-performance|memory contamination]], agent security).

## Open Questions

- What did the agents actually do (per-unit topics), and did they survive in production after the program?
- How transferable is the model to lighter-touch or non-regulated orgs?

## Concepts Linked

- [[concepts/product-management/domain-expert-as-builder|Domain Expert as Builder]]
- [[concepts/infrastructure-dev/ai-adoption-culture|AI Adoption Culture]]
- [[concepts/ai-agents/claude-code|Claude Code]]
- [[concepts/ai-agents/vibe-coding|Vibe Coding]]
- [[concepts/ux-research/human-in-the-loop|Human in the Loop]]
- [[concepts/product-management/role-convergence|Role Convergence]]

## LLM Use

- **Use for:** designing a hands-on AI-enablement cohort (boundary-setting → real-data gate → direct ownership → parallel pacing → exec demo); arguing domain-experts-as-builders with HITL.
- **Do not use for:** quantified ROI/sustainment claims (vendor case, success-biased).
- **Best prompt pattern:** "Design a 6-week PBL to teach N non-developer domain experts to build an agent with Claude Code: week-by-week deliverables, the real-data gate, boundary/HITL definitions, and a parallel-pacing support model."

## Reliability Notes

> [!warning] Caveats
> Vendor case study, success-biased, no hard metrics. Confidence 0.8 on the program *design*; lower on outcome magnitude and durability.

## Backfill Status

- New ingest 2026-06-25 from full web_fetch. To reach `full`, capture per-unit agent topics, publish date/author, and any post-program metrics.
