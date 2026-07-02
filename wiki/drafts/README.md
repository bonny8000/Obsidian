---
type: guide
status: active
created: 2026-07-02
updated: 2026-07-02
tags: [ollama, draft, review, ingest]
---

# Local Ingest Drafts

This folder holds review packages created by `scripts/draft-with-ollama.ps1`.

## Commands

```powershell
# 1. Create a draft from a preserved Markdown raw card.
.\scripts\draft-with-ollama.ps1 `
  -RawPath 'raw/web/example-2026-07-02.md' `
  -Model 'qwen3:4b'

# 2. Review wiki/drafts/packages/<package>/review.md.

# 3. Preview the apply operation.
.\scripts\apply-latest-draft.ps1 -WhatIf

# 4. Apply after review. Replacement requires -AllowReplace.
.\scripts\apply-latest-draft.ps1 -Confirm

# 5. Validate independently.
.\scripts\validate-ingest.ps1
```

## Safety Rules

- Draft targets are restricted to new or existing Markdown files under `wiki/sources/` and `wiki/concepts/`.
- A local model cannot edit `raw/`, maps, indexes, logs, scripts, configuration, or Canvas files.
- Existing files require the explicit `-AllowReplace` switch and are backed up before writing.
- Failed post-apply validation triggers rollback.
- Map suggestions remain manual review notes.

## Model State

Ollama is installed on this computer. A model must be downloaded explicitly before drafting. The default script model is `qwen3:4b`.
