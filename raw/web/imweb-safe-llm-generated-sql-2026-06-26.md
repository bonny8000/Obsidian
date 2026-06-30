---
source_url: https://tech.imweb.me/posts/safe-llm-generated-sql/
captured: 2026-06-26
title: "How to Safely Use SQL Written by AI"
authors: [Yehee Choi]
published: 2026-06-22
publisher: Imweb Tech (아임웹 테크), Analytics Squad
---

# How to Safely Use SQL Written by AI

**Capture status:** AI-written summary (not verbatim), captured 2026-06-26. Fetched fully via web_fetch from the Imweb Tech blog; no paywall or access limit encountered. Summary is in English; Korean proper nouns and column names preserved.

## Summary
Imweb (아임웹), a Korean website/commerce builder, shipped a natural-language chatbot that lets non-technical sellers ask data questions (sales, repurchase rate, customer insights) and auto-generates the SQL to answer them, replacing a data-team bottleneck of hand-written queries. Because an LLM can rewrite the entire query structure (not just input values), the team treats LLM-generated SQL as inherently untrusted and wraps it in a deterministic safety harness: judgment is separated from execution, domain rules live in a database rather than code, and every query passes three sequential AST-level validation gates plus a bounded self-repair loop before it runs. The post is an engineering retrospective with concrete failure modes, a golden-set regression eval, and operational metrics from a 13-site closed beta (CBT).

## Key Points
- **Problem framing:** sellers need data answers but lack SQL; the data team hand-writing queries was the bottleneck. A NL chatbot auto-generates SQL to remove it.
- **Threat model:** LLM-generated SQL endangers the *whole query structure* — hallucinated columns, NULL-arithmetic math errors, and unauthorized cross-tenant access — not just user-supplied values, so input sanitization is insufficient.
- **Principle 1 — Judgment/Execution Separation:** split into a "brain" (intent detection, response synthesis) and a "toolbox" (SQL generation, validation, execution). Security is localized at the data layer, so any future UI/API/agent passes the same gates.
- **Principle 2 — Domain-Knowledge Externalization:** business rules move out of code into a PostgreSQL table `query_knowledge_base` with pgvector embeddings, so rules can be fixed by editing data and re-embedding, without redeploying code.
- **Gate 1 — Schema Integrity ("Existence"):** parse SQL into an AST; verify every referenced table/column exists in the warehouse catalog (allowlist); return corrected column suggestions instead of silently rejecting. Catches model-invented columns like `member_order_rank`.
- **Gate 2 — Security Policy ("Policy"):** force a tenant-isolation filter on every query; block full-table scans on large tables; detect NULL-arithmetic traps (e.g. `revenue - refunds` where `refunds` is NULL nullifies the result) and suggest `COALESCE`; block destructive keywords (DELETE/UPDATE/INSERT/DROP).
- **Gate 3 — Query Form ("Shape"):** SELECT-only; reject Korean characters used as unquoted identifiers (treated as hallucinations; Korean allowed only in output labels); enforce valid SQL syntax.
- **Knowledge base ("백과사전"/encyclopedia), two-tier injection:** (a) Pinned Rules cached in memory each request — e.g. revenue defined as net `pg_amount - pg_cancel_price` (not gross), `member_code` starting with "m" = real member; (b) Retrieved Rules via pgvector cosine-distance search, pulling contextual rules (ROAS, funnel conversion, cohort) dynamically.
- **Self-Repair Loop:** gate violations are returned to the model as human-readable correction instructions; capped at 2 regeneration attempts, then escalate to the user.
- **DESCRIBE QUERY** is run pre-execution in the same session to resolve name bindings in complex CTEs/JOINs.
- **Output scrubbing:** mask internal identifiers and PII (names, emails, phones) before display.
- **Eval:** golden set of ~100 representative queries; multi-stage pipeline judged by secondary LLM models (a separate judge per pipeline stage), with pass/fail aggregation logic in *code*, not the LLM.
- **Metrics:** golden-set pass rate rose ~67% (early June) → ~80% (mid June) via prompt refinement + KB expansion; user re-queries that hit the max regeneration cap are single-digit % of questions. Monthly blocking log across a 13-site CBT ranks hallucinated columns as the most frequent blocker, then tenant-isolation, full-scans, division-by-zero, and Korean-identifier violations.
- **Silent logic errors** (valid grammar + valid columns + wrong semantics, e.g. repurchase rate including guest orders) cannot be caught pre-execution; they need golden-set regression plus post-deploy monitoring.
- **Hard-won lesson:** the stronger you make a gate, the more you must manage its own false positives (e.g. a parser mistaking a result label for a column), so over-broad gates break legitimate queries.

## Follow-up
- Verify the exact gate ordering and whether all three gates run on every query or short-circuit on first violation; confirm the regeneration cap (2) is global or per-gate.
- Re-capture later for updated golden-set pass rate and CBT→GA metrics; check whether silent-logic-error monitoring graduated to an automated check.
- Confirm the `query_knowledge_base` schema (pinned vs retrieved partitioning) and the embedding model used for pgvector retrieval.
