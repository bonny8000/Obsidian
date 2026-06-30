---
source_url: https://medium.com/heyratel/%EB%8F%84%EA%B5%AC%EA%B0%80-%EC%95%84%EB%8B%88%EB%9D%BC-%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C-ios-%ED%8C%80%EC%9D%98-ai-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%EA%B8%B0-d37625b00af2
captured: 2026-06-26
title: "Not a Tool but a Standard: How an iOS Team Built Its AI Agent Environment"
authors: [Jinyoo (유진영)]
published: 2026-06
publisher: Ratel And Partners (라텔앤드파트너즈) — HeyRatel, Medium
---

# Not a Tool but a Standard: How an iOS Team Built Its AI Agent Environment

**Capture status:** AI-written summary (not verbatim), captured 2026-06-26. Fetched fully via web_fetch from the HeyRatel Medium publication; no paywall or access limit observed. Original is in Korean; this is an English summary preserving Korean terms/quotes where load-bearing.

## Summary

A practitioner field report from an iOS team (Ratel And Partners / HeyRatel) on building an AI-agent development environment governed by explicit decision *criteria* rather than tool hype. The team derived four architecture principles — small/clean context, validate inefficiency before automating, single-responsibility composable skills, and inviolable human-judgment gates — and built a stack of Claude Code agents, distributed CLAUDE.md instruction files, and narrow custom skills around them. Their headline framing: "Tools don't set the standard; the standard chooses the tools." Notable choices include rejecting MCP in favor of custom curl-based skills (for token compression), symlinking AGENTS.md to CLAUDE.md so Claude Code and Codex share one source of truth, and an escalation/advisor protocol that lets a Sonnet-class implementer call Opus 4.8 only for high-stakes decisions.

## Key Points

- **Core thesis ("standard over tool"):** automation scope is chosen from explicit criteria, not from what tools happen to exist. Quote: "도구가 기준을 정하는 게 아니라, 기준이 도구를 고릅니다." (Tools don't set the standard; the standard chooses the tools.)
- **Problem motivating the work:** repetitive manual tasks (ticket creation, branch naming, PR formatting, docs); specs siloed across Confluence/Figma; risk of AI making unilateral architecture decisions; token/cost waste from oversized context; unclear automation-vs-judgment boundary.
- **Four architecture principles:** (1) Context Optimization — keep context small and clean (token cost scales ~linearly with context size, cites Anthropic); (2) validate inefficiency first — only automate proven, repeated pain; (3) composability — one skill = one responsibility; (4) preserve human-judgment gates — never automate irreversible decisions. "자동화하는 것은 기계적 비효율이지 판단이 아닙니다." (Automation targets mechanical waste, not judgment.)
- **Agent roster:** Claude Code as the main agent (dialogue, requirement clarification, architecture decisions); an `ios-developer` agent on Sonnet (code implementation, escalates architectural ambiguity); a `markdown-writer` agent (docs/specs); a `Codex` agent for independent code review / second opinion.
- **Instruction management:** distributed CLAUDE.md files, one per module, each ≤200 lines (per Anthropic guidance). Root CLAUDE.md (shared) plus per-project files (DesignSystem, DataLayer, Features/<module>).
- **Symlink trick:** `AGENTS.md` is a symbolic link to `CLAUDE.md` (`ln -s CLAUDE.md AGENTS.md`) so Claude Code and Codex read the identical source of truth and instructions never drift.
- **Skills (narrow, single-responsibility):** `task` (ticket + branch naming + base-branch update), `confluence`/`figma` (fetch specs), `grill-me` (surfaces design ambiguity via structured questioning), `epic` (splits features into Phase-sized, testable, reversible units), `ios-developer` (implements a Phase, escalates), `markdown-writer`, `codex-opinion` (independent review against plan/task docs), `pr` (auto Korean PR title/body, validates destination branch), `pr-review` (rule + quality checks; never posts comments without explicit approval), and `mission-plan` + `mission-run` orchestrators that compose the smaller skills.
- **API integration is NOT MCP:** custom curl-based skills for Jira/Confluence/Figma instead of MCP servers, because MCP responses are verbose; custom skills fetch only needed fields and summarize before feeding the model, saving tokens.
- **Escalation / model tiers ("advisor" mode):** `ios-developer` runs on Sonnet but can call Opus 4.8 for high-stakes decisions rather than deciding alone; ambiguous or architecture-altering decisions escalate to the main agent or the human. Advisor mode reportedly reduced escalation frequency after rollout — quality held without paying for Opus on every call.
- **Process integration (stage → automation → gate):** Assignment → `task` → (none); Planning → `grill-me` + Codex review → person decides design branches; Implementation → `ios-developer` + Phase escalation → Codex + on-device test; Review → `pr-review` → user approval before any comment posts; PR → `pr` (title + branch validation) → person confirms and merges.
- **Documentation as guardrails:** spec/plan/task docs live in a `Doc/` folder as contracts plus "why did we do this?" rationale to prevent drift.
- **Before/after:** before — manual spec gathering, ad-hoc design decisions during coding, hand-written PRs, single-reviewer blind spots, frequent rework. After — design locked before coding, ambiguity surfaced early via grill-me, reversible until merge, decisions documented; mission-plan + mission-run compose the whole flow.
- **Lessons:** symlink prevents instruction drift; narrow skills are easier to test/compose than monolith orchestrators; escalation keeps a lighter model's quality high; distributed CLAUDE.md cut per-request context vs a single ~1000-line file. Pitfalls avoided: no wholesale MCP, no automated approval/merge, no single bloated guideline doc.

## Follow-up

- Verify the quantitative claims (advisor mode "reduced escalation frequency"; token savings from custom skills vs MCP) — the post gives directional, not measured, evidence.
- Re-capture if the team publishes a follow-up with concrete metrics or the actual skill/CLAUDE.md file contents.
- Cross-check the "≤200 lines per CLAUDE.md" and "token cost scales linearly with context" attributions against current Anthropic guidance.
