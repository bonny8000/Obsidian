---
type: source
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [text-to-sql, llm-safety, deterministic-validation, ast-validation, pgvector, multi-tenant-security, self-repair-loop, golden-set-eval, agent-harness, postgresql]
source_path: raw/web/imweb-safe-llm-generated-sql-2026-06-26.md
source_url: https://tech.imweb.me/posts/safe-llm-generated-sql/
authors: [Yehee Choi]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.82
---

# Choi / Imweb (2026): How to Safely Use SQL Written by AI

**Author:** Yehee Choi, Backend Engineer, Analytics Squad — Imweb Tech (아임웹 테크), 2026-06-22.
**Raw capture:** [[raw/web/imweb-safe-llm-generated-sql-2026-06-26|imweb-safe-llm-generated-sql-2026-06-26]]
**URL:** [tech.imweb.me/posts/safe-llm-generated-sql](https://tech.imweb.me/posts/safe-llm-generated-sql/)

## Citation

Choi, Y. (2026, June 22). *AI가 쓴 SQL을 안전하게 쓰는 법 (How to Safely Use SQL Written by AI).* Imweb Tech (아임웹 테크), Analytics Squad. Captured 2026-06-26 into `raw/web/imweb-safe-llm-generated-sql-2026-06-26.md`.

## Summary

Imweb, a Korean website/commerce builder, shipped a natural-language chatbot that turns seller questions ("what's my repurchase rate?") into executable SQL, removing the bottleneck of a data team hand-writing every query. The core engineering insight is that **LLM-generated SQL is a structurally different threat from classic SQL injection**: the model can rewrite the entire query — inventing columns, choosing wrong tables, doing NULL-poisoned arithmetic, or omitting tenant isolation — so sanitizing inputs is useless. Imweb's answer is a deterministic safety harness around an untrusted generator: separate judgment from execution, push domain rules into a `pgvector` knowledge base instead of code, and run every query through three sequential AST-level validation gates (Existence → Policy → Shape) plus a bounded self-repair loop before it ever touches the warehouse. The post is a candid practitioner retrospective with named failure modes, a ~100-query golden-set regression eval judged stage-by-stage by secondary LLMs (with pass/fail aggregation in code), and operational metrics from a 13-site closed beta. Its central maxim: **don't trust the model, trust the boundary.**

## Key Claims

- **The threat is structural, not value-level.** LLM-generated SQL can corrupt the *whole query structure* — hallucinated columns, wrong tables, NULL-arithmetic errors, missing tenant filters — so input sanitization (the classic injection defense) does not apply. The defense must validate the generated query itself.
- **Judgment/Execution Separation.** The system is split into a "brain" (intent detection, response synthesis) and a "toolbox" (SQL generation, validation, execution). **Localizing security at the data layer** means any future UI, API, or agent entry point inherits the same gates rather than re-implementing them.
- **Domain knowledge belongs in data, not code.** Business rules live in a PostgreSQL table `query_knowledge_base` with **pgvector** embeddings. Fixing a wrong rule is "edit one row's wording, recalculate the embedding, and the next query is correct" — no redeploy.
- **Three deterministic gates run on the AST.** **Gate 1 (Existence / Schema Integrity)** parses to an AST and checks every table/column against the warehouse catalog allowlist, returning corrected-column suggestions rather than silent rejection. **Gate 2 (Policy / Security)** forces a tenant-isolation filter, blocks full-table scans on big tables, catches NULL-arithmetic traps (suggesting `COALESCE`), and blocks destructive keywords (DELETE/UPDATE/INSERT/DROP). **Gate 3 (Shape / Query Form)** enforces SELECT-only, valid syntax, and rejects Korean characters used as unquoted identifiers (a hallucination signal; Korean is allowed only in output labels).
- **Two-tier knowledge injection.** **Pinned Rules** are cached in memory every request (e.g. revenue = net `pg_amount - pg_cancel_price`, not gross; `member_code` starting with "m" = a real member). **Retrieved Rules** come from cosine-distance pgvector search on the embedded question, pulling contextual definitions (ROAS, funnel conversion, cohort) on demand.
- **Bounded self-repair.** Gate violations are fed back to the model as human-readable correction instructions; regeneration is **capped at 2 attempts**, then escalated to the user — explicitly to prevent unbounded loops.
- **Pre-execution binding check.** `DESCRIBE QUERY` is run in the same session to resolve name bindings in complex CTEs/JOINs before real execution.
- **Output scrubbing.** Internal identifiers and PII (names, emails, phones) are masked before display.
- **Silent logic errors are uncatchable pre-execution.** A query with valid grammar, valid columns, and *wrong semantics* (e.g. a repurchase rate that wrongly includes guest orders) runs cleanly — so it needs golden-set regression and post-deploy monitoring, not a gate.
- **Stronger gates create their own false positives.** "The stronger you make a gate, the more you must manage its own false positives" — e.g. a parser mistaking a result label for a column. Over-broad gates break legitimate queries; gate precision is itself an engineering cost.

## Useful Examples

- **The NULL-arithmetic trap:** `revenue - refunds` where `refunds` is NULL silently nullifies the entire result — "SQL executed normally with no errors." Gate 2 detects this and suggests `COALESCE`.
- **Hallucinated column** `member_order_rank` — a plausible-but-nonexistent column the model invented; Gate 1 catches it via the catalog allowlist and suggests the real column.
- **Net-vs-gross revenue definition** pinned in the KB: revenue = `pg_amount - pg_cancel_price`. A semantic rule that no syntax check could enforce, so it lives in pinned domain knowledge.
- **Eval pipeline:** ~100-query golden set; each pipeline stage judged by a *separate* secondary LLM, with pass/fail **aggregation logic in code, not LLM**.
- **Operational metrics:** golden-set pass rate ~67% (early June) → ~80% (mid June) via prompt + KB work; max-regeneration re-queries are single-digit % of questions; across a 13-site CBT, the monthly blocking log ranks hallucinated columns as the top blocker, then tenant-isolation, full-scans, division-by-zero, Korean-identifier violations.

## Constraints / Caveats

- **Single-vendor engineering blog, self-reported metrics.** The ~67%→80% pass rate, single-digit re-query rate, and blocker ranking are Imweb's own CBT observations with no external benchmark, disclosed model, or reproducible test set. Treat as directional.
- **Closed beta scale.** Metrics come from a 13-site CBT, not general availability; numbers will drift at scale.
- **Stack-specific.** The design assumes PostgreSQL + pgvector and a known warehouse catalog; the AST-allowlist approach depends on having a complete, current schema catalog.
- **The hardest failure mode is unsolved.** The author is candid that silent logic errors can't be gated and rely on regression + monitoring — i.e. the safety story is incomplete by design.
- **No model named** for either generation or the secondary LLM judges, so accuracy figures aren't apples-to-apples comparable.

## Design Implications

- **For agentic-engineering practice:** this is a clean, reusable template for [[concepts/ai-agents/text-to-sql|Text-to-SQL]] safety — treat the generator as untrusted and put the trust in a deterministic boundary. The "validate the generated artifact, not the input" stance is the SQL-specific instance of [[concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]].
- **Localize security at the resource, not the entry point.** Imweb's judgment/execution split is a concrete [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]] pattern: gate at the data layer so UI, API, and agent callers all inherit the same guarantees. Directly applicable to any tool-calling agent Bonny designs that touches sensitive data.
- **AST-level deterministic gates are [[concepts/ai-agents/agent-verifiers|Agent Verifiers]].** Three precise, code-level checks (Existence/Policy/Shape) that return *actionable* corrections, not just rejections — the verifier-with-repair shape is the transferable idea, and it belongs in the [[concepts/ai-agents/harness-engineering|Harness Engineering]] layer around the model.
- **Bounded repair is [[concepts/ai-agents/loop-engineering|Loop Engineering]].** Feed violations back as instructions, but cap at 2 and escalate — a copyable rule for any self-correcting agent loop to avoid runaway regeneration and token burn.
- **Domain rules as retrieved data = [[concepts/ai-agents/agentic-rag|Agentic RAG]] for governance.** Pinned + pgvector-retrieved business definitions are a [[concepts/ai-agents/context-engineering|Context Engineering]] move: edit-a-row-and-re-embed beats redeploy, and it keeps the prompt lean (a [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]] win since only relevant rules are injected per query).
- **The eval design is an [[concepts/ux-research/ai-evals|AI Evals]] pattern worth copying:** a golden set, a *separate judge per pipeline stage*, and pass/fail aggregation in deterministic code rather than trusting an LLM to score the whole pipeline.

## Tensions

- **Gate strength vs. false positives.** The post's own lesson — stronger gates breed more false positives — is in direct tension with the [[concepts/ai-agents/zero-trust-agent-development|zero-trust]] instinct to over-constrain. Precision, not aggressiveness, is the goal; this complicates the "just add more guardrails" reflex.
- **Deterministic gates vs. silent semantic errors.** [[concepts/ai-agents/agent-verifiers|Verifiers]] catch structural faults but are blind to valid-but-wrong semantics — so a fully deterministic boundary is *necessary but not sufficient*, and the system still leans on probabilistic [[concepts/ux-research/ai-evals|evals]] and monitoring it admits are incomplete.
- **Externalized rules vs. correctness.** Moving domain knowledge into a [[concepts/ai-agents/agentic-rag|retrieved]] KB makes fixes fast, but retrieval quality now gates correctness — a wrong/missing embedding silently degrades answers, shifting risk from code review to data hygiene.

## Open Questions

- Do all three gates run on every query, or short-circuit on first violation — and is the 2-attempt regeneration cap global or per-gate?
- How are silent logic errors actually detected post-deploy — automated monitors, sampling, or user-reported only?
- What embedding model and similarity threshold drive the pgvector retrieval, and how is the pinned-vs-retrieved boundary decided?
- How does the secondary-LLM-judge eval guard against the judges sharing the generator's blind spots?
- Does the catalog-allowlist approach hold up as the warehouse schema evolves rapidly, or does staleness become a new false-positive source?

## Concepts Linked

- [[concepts/ai-agents/text-to-sql|Text-to-SQL]]
- [[concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]]
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]]
- [[concepts/ai-agents/agent-verifiers|Agent Verifiers]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/loop-engineering|Loop Engineering]]
- [[concepts/ai-agents/agentic-rag|Agentic RAG]]
- [[concepts/ai-agents/context-engineering|Context Engineering]]
- [[concepts/infrastructure-dev/token-efficiency|Token Efficiency]]
- [[concepts/ux-research/ai-evals|AI Evals]]

## LLM Use

- **Use for:** a concrete, copyable architecture for safe LLM-to-SQL — the judgment/execution split, three AST gates (Existence/Policy/Shape), pinned+retrieved pgvector domain rules, bounded self-repair, and a stage-wise golden-set eval with code-side aggregation; grounding "validate the generated artifact, not the input" as a zero-trust principle; citing named failure modes (hallucinated columns, NULL-arithmetic, missing tenant filter).
- **Do not use for:** generalizable benchmarks (the ~67%→80% figures are single-vendor CBT, no model/test set named); a complete safety guarantee (silent logic errors are explicitly out of scope for the gates); stack-agnostic claims (design assumes PostgreSQL + pgvector + a current catalog).
- **Best prompt pattern:** "Using Imweb's safe-LLM-SQL design, draft a safety harness for a Text-to-SQL agent on [stack]: specify the judgment/execution split, the deterministic validation gates (what each checks and what correction it returns), the domain-knowledge store (pinned vs retrieved), the bounded repair loop, and the regression eval — then list which failure modes each layer catches and which it cannot."

## Reliability Notes

> [!warning] Caveats
> - **Practitioner retrospective, self-reported metrics.** Architecture and failure modes are credible and specific (0.85+); the quantitative claims (~67%→80% pass rate, single-digit re-query rate, blocker ranking) are unaudited 13-site CBT figures with no model or test set disclosed (~0.6).
> - **Incomplete by design.** The author is honest that silent semantic errors can't be gated, so this is a strong-but-partial safety story.
> - **Stack-bound.** Tightly coupled to PostgreSQL + pgvector and a maintained warehouse catalog; portability of specifics is unproven.
> - **Confidence:** 0.82 overall — high on the transferable patterns, lower on the metrics and on generality.

## Backfill Status

- Newly written 2026-06-26 from a full web_fetch capture; all sections populated. Raise coverage/confidence later with: confirmed gate ordering and repair-cap semantics, post-deploy silent-error detection method, the `query_knowledge_base` schema and embedding model, and any GA-scale metrics superseding the 13-site CBT figures.
