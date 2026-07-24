---
type: map
status: active
created: 2026-07-24
updated: 2026-07-24
tags: [map, dashboard, kanban, llm-wiki, operations]
sources: []
confidence: 1.0
---

# 📊 Vault Dashboard

> [!abstract] What this is
> The in-Obsidian control surface for the wiki — a kanban board of everything asking for attention, plus health and pipeline views. Everything below is a live [[vault-dashboard.base|Bases]] view, so it updates as you edit notes. No plugin required.

---

## 🗂️ Work Queue — the board

> [!tip] How the lanes work
> Each note lands in exactly one lane, first match wins:
> **🟠 Needs review** → **🟡 Draft** → **🔴 Low confidence** (< 0.7) → **🕰️ Stale** (untouched 60+ days) → **✅ Healthy**.
> Healthy notes are hidden from this board — it shows only what needs work. Move a card by editing the note's `status` or `confidence` frontmatter.

![[vault-dashboard.base#🗂️ Work Queue Kanban]]

---

## 🩺 Knowledge health

> [!info] Reading these
> Confidence follows the [[AGENTS|AGENTS.md]] scale: `0.90–1.00` directly supported · `0.70–0.89` well supported, one verification step missing · `0.40–0.69` plausible but partial · `0.00–0.39` weak or contradicted.

![[vault-dashboard.base#🩺 Confidence Bands]]

![[vault-dashboard.base#🔴 Low Confidence (< 0.7)]]

![[vault-dashboard.base#🕰️ Stale Concepts (60+ days)]]

---

## 📥 Source pipeline

![[vault-dashboard.base#📥 Source Readiness]]

![[vault-dashboard.base#🆕 Recent Ingests]]

---

## 🗺️ Library composition

![[vault-dashboard.base#🗺️ Library by Type]]

![[vault-dashboard.base#⚠️ Lost Content Awaiting Re-ingest]]

---

## 🔗 Related boards

- [[dashboard.base|Ingest & Quality Dashboard]] — the original source-focused views
- [[wiki/project-kanban.base|Project Kanban]] — active projects only
- [[index|LLM Wiki Index]] · [[wiki/index|Wiki Index]] · [[wiki/overview|Overview]]
- [[log|Operations Log]] · [[wiki/logs/change-log|Change Log]]

## ❓ Maintenance notes

- Lanes are computed by the `triage` formula in `vault-dashboard.base`. To change a threshold (e.g. stale at 90 days instead of 60), edit that formula in one place.
- **🗃️ Board by Status** is a fallback view grouped by the raw `status` field, in case formula-based grouping misbehaves in your Obsidian version.
- Notes without a `confidence` value may fall through the triage chain unpredictably — the long-term fix is backfilling frontmatter on the 297 untyped raw captures, not patching the formula.
