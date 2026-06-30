---
source_url: https://maily.so/makersnote/posts/1gz2e564z3q
captured: 2026-06-25
title: "[19호] Why Sasha plans high-level with AI but does detailed planning by hand — build a Planning Harness"
authors: [Product Makers Note]
published: 2026-06-24
publisher: Maily (makersnote)
shared_via: https://share.google/8fBtlCIzPeLGTa8CG
---

# Planning Harness — Product Makers Note (Issue #19)

**Author/Newsletter:** Product Makers Note (makersnote) — Maily, 2026-06-24. Reached via a `share.google` short link.
**Capture status:** Fetched via web_fetch 2026-06-25; AI-written summary (not verbatim). The "planning harness" framing and 10-minute setup are the author's.

## Summary

Most PMs use AI well for **high-level strategy** but revert to **manual work for detailed specs** — and when something changes, the AI loses context and produces unreliable output. The fix is a **"planning harness"**: a system that converts loose chat into a *tightly controlled automation factory* for product planning. The punchline role shift: stop being an "AI sitter" babysitting hallucinations and become a **"planning harness engineer"** who designs the guardrails.

## Key Points

- **Four principles of a harness:**
  1. **Context** — embed core service policies permanently into the AI's reasoning (not re-pasted each session).
  2. **Tool definition** — restrict the AI to predefined commands (**skills**) only.
  3. **Guardrails** — safety rules; sensitive decisions require human approval.
  4. **Validation** — the AI self-verifies output against the original planning intent.
- **Harness vs. just sharing files:** a harness gives a *permanent pipeline* (no per-session setup), *actual execution* (AI directly edits local files like `spec.md`, `flow.mermaid`), and a *team asset* (shareable via GitHub, consistent results across teammates).
- **10-minute setup:** (1) create a folder (`local-harness`); (2) write a rules file — `CLAUDE.md` (or `.cursorrules` / `.clinerules`); (3) define custom skills (`/sequence_diagram`, `/user-flow`, `/make-html`); (4) include a reference `spec.md`; (5) optionally push to GitHub.
- **Worked example:** adding a comment feature to a memo app — the harness auto-generated a sequence diagram (client–server–DB flow), a user-flow chart, and an HTML visualization. Without a harness this needed manual prompting across multiple tools.
- **Future vision:** split **design (Figma)** from **logic planning (harness-based code/artifact generation)** to kill duplicate effort.
- **Key quote:** "Stop wasting time chatting aimlessly with AI. Design your own sturdy guardrails instead."

## Follow-up

- Verify the Korean original's exact section titles; capture the example screenshots if needed for citation.
