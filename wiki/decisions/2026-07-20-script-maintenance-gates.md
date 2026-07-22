---
type: decision
status: active
created: 2026-07-20
updated: 2026-07-20
tags: [decision, vault-maintenance, automation, governance]
sources: []
---

# Decision: Bulk Scripts Get the Same Gates as Agents

## Context & Background

On 2026-06-12, `scripts/backfill_llm_ready.py` retrofitted source pages for LLM-readiness — and silently wrote duplicate boilerplate into 66 of 160 source pages, including 20 pages whose body contradicted their own frontmatter (``ingest level is `deep` `` vs `standard`). The damage sat unnoticed for five weeks until the 2026-07-20 health check. Agent edits go through the Safe Ingest Promotion Workflow; scripted edits had no equivalent gate.

## Options Considered

1. **Ban maintenance scripts.** Removes the risk and the leverage; unrealistic for a 600+ page vault.
2. **Gate scripted bulk edits like agent edits**: dry-run first, bounded diff review, post-run validation, logged outcome.
3. **Status quo** (scripts run ungated). Proven failure.

## Decision Made

**Option 2.** Any script that edits more than ~5 wiki pages must follow the gate sequence in [[wiki/playbooks/safe-script-maintenance|Safe Script Maintenance playbook]]: dry-run → spot-check diff → apply on a clean git tree → re-run the relevant audit → log in change-log. Scripts live in `scripts/` and are git-tracked.

## Evidence & Justification

- The 2026-07-20 cleanup itself demonstrated the pattern working: the fix script ran dry-run first, was applied to a committed tree, and was verified by re-audit (66 → 0 duplicates, 20 → 0 contradictions).
- Consistent with AGENTS.md Core Rule 9 (gates for destructive graph edits).

## Consequences & Next Steps

- New playbook page added; AGENTS.md Core Rules reference it.
- Existing scripts (`backfill_llm_ready.py` if rerun, `obsidian-safe.py`, `rag_query.py`) must comply before their next run against `wiki/`.
