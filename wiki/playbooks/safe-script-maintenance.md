---
type: playbook
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [playbook, vault-maintenance, automation]
sources: []
confidence: 0.9
---

# Playbook: Safe Script Maintenance

Gates for any script that edits more than ~5 pages under `wiki/`. Companion to [[wiki/decisions/2026-07-20-script-maintenance-gates|the decision record]]; sibling of [[wiki/playbooks/safe-ingest-promotion-workflow|Safe Ingest Promotion Workflow]].

## Gate Sequence

1. **Clean tree first.** `git status` must be clean (or current work committed) so the script's effect is exactly one diff.
2. **Dry-run mode is mandatory.** The script must support a no-write mode that prints which files it *would* change and how many. If the count surprises you, stop.
3. **Spot-check before apply.** Read the full before/after for at least 2–3 representative files, including one edge case (shortest page, page with callouts/canvas links, page with non-ASCII text).
4. **Apply, then re-audit.** Run the check that motivated the script (link scan, duplication count, frontmatter validation) and confirm the target metric moved to the expected value — not just "ran without error."
5. **Idempotence check.** Running the script a second time must change zero files. If it changes anything, the transform is unstable — revert and fix.
6. **Log it.** One change-log entry: what ran, how many files, verification result, and the commit hash.

## Red Flags (stop and hand to a human)

- The script touches `raw/` in write mode — raw is immutable.
- Regex transforms on frontmatter without a YAML-aware guard.
- "While I'm at it" scope creep inside a mechanical script — one script, one transform.
- No way to express the change as a reviewable diff (e.g., in-place binary edits).

## Why These Gates

The 2026-06-12 backfill incident (66 damaged pages, 5 weeks undetected) failed gates 3, 4, and 5 specifically: no edge-case spot-check, no post-run duplication audit, and a non-idempotent append that stacked boilerplate on each run.
