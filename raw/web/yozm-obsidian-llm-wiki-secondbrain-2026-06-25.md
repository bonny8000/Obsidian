---
source_url: https://yozm.wishket.com/magazine/detail/3792/
captured: 2026-06-25
title: "나만의 세컨 브레인: 옵시디언 기반 LLM 위키 구축기 (My Second Brain: Building an Obsidian-Based LLM Wiki)"
authors: [곰씨네 IT 블로그 (Gom's IT Blog)]
published: 2026-06-10
publisher: 요즘IT / Yozm IT (Wishket)
---

# My Second Brain: Building an Obsidian-Based LLM Wiki

**Author:** 곰씨네 IT 블로그 (Gom's IT Blog) — Yozm IT (Wishket), 2026-06-10.
**Capture status:** Fetched via web_fetch 2026-06-25; AI-written summary (not verbatim). **This is the blueprint article that this very vault (LLM-Wiki) implements** — the `raw/` → `wiki/` split, the `/ingest` `/lint` `/query` skills, and the Obsidian + GitHub + Claude Code stack all trace back to this design.

## Summary

The author is tired of re-explaining personal context to every AI tool (Claude, ChatGPT, Gemini) because information is scattered across Google Keep, Notion, Google Workspace, and GitHub — so no AI ever sees the whole situation. The fix (after Andrej Karpathy's "second brain" framing): a single, centralized, **AI-maintained LLM Wiki**. Result: AI answers shift from generic advice to **situation-optimized answers** that account for the user's philosophy, project priorities, and constraints at once.

## Key Points

- **Stack:** **Obsidian** (core notes, Minimal theme) + **GitHub private repo** (backup + multi-device sync) + **Claude Code CLI** (automation/maintenance). Plugins: Git sync, Terminal, template managers, visualization tools.
- **Unified capture:** web clipping via a Chrome extension (desktop) + the share sheet (mobile) — everything funnels into one inbox.
- **Three automation "skills" (slash commands):**
  - **/ingest** — process incoming material into wiki pages.
  - **/lint** — daily automated checks for sensitive data, broken links, and orphan pages.
  - **/query** — contextual Q&A against the full wiki.
- **Wiki structure — 7 categories** designed to capture complete personal context: **Identity, Thoughts, Goals, History, People, Assets, Works.**
- **Security layers:** regex-based sensitive-data masking, two-factor auth, and fine-grained GitHub tokens.
- **Results:** AI moved from generic → situation-optimized; the assistant can reason over philosophy + priorities + constraints simultaneously.
- **Limitations (honest):** OCR errors on handwritten notes need manual correction; a growing wiki increases sensitive-info exposure; a GitHub account compromise = total data breach; collaboration needs a *separate* team wiki (violates single-source-of-truth); Obsidian has a real learning curve.
- **Key recommendation:** *Don't chase a perfect structure from day one — improve incrementally* to avoid abandonment.

## Follow-up

- This is a meta-source for the vault itself: reconcile its `/ingest /lint /query` design and 7-category personal-context structure against this vault's own `AGENTS.md`/`CLAUDE.md` contract and note any deliberate divergences (this vault is research/UX-focused rather than personal-life-focused).
