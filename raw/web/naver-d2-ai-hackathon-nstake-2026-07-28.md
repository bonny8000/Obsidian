---
source_url: https://d2.naver.com/helloworld/4821538
captured: 2026-07-28
title: "[AI 해커톤 후기] AI 해커톤 1위 팀이 AI에게 맡기지 않은 것"
authors: [장동원, 유석모, 서정은, 남궁은경]
published: 2026-07-24
publisher: NAVER D2 (Hello World)
language: ko
tags: [ENGINEERING_DAY]
---

# What the Winning AI Hackathon Team Did *Not* Delegate to AI — NAVER D2

**Original title (ko):** 「[AI 해커톤 후기] AI 해커톤 1위 팀이 AI에게 맡기지 않은 것」
**Authors:** 장동원 (NAVER Cloud IT Service), 유석모 (NAVER 네이버앱 서비스), 서정은 (NAVER Creative&Experience), 남궁은경 (NAVER 콘텐츠 서비스)
**Published:** 2026-07-24 · **Captured:** 2026-07-28
**Capture note:** Full Korean article text was retrieved and read end-to-end via the D2 content API. This file is an AI-written English summary; the original text is not reproduced.

## Summary

A retrospective from the team that won NAVER's internal "모두의 Engineering Day AI 해커톤." In ~6 hours (10:00–16:00) a four-person cross-functional team built **NStake**, replacing spreadsheet-based equity/shareholding management with an LLM + MCP investment portfolio platform. The article's thesis is in its title: the decisive choices were about **what they refused to hand to AI**.

## Hackathon format

- Problems came from real internal work. Staff experiencing a problem joined as **problem holders (출제자)**; participants as **solvers**.
- Teams of four mixed development, planning, design, finance, and operations.
- **Pair prompting:** two dev environments per team; multiple people wrote prompts and reviewed results together rather than one person accepting AI output alone.
- Judging: LLM first-pass evaluation (from code + docs) → problem holder evaluation → participant final evaluation.

## The problem chosen

Convert manual Excel-based equity/investment-status management into an LLM/MCP platform. The team was unfamiliar with finance terms (발행 주식 수, 지분율, 유상증자, 구주 양수도, RCPS, 감자). They picked it as first choice anyway, because impact was clear:

- **17 staff** each maintained their own Excel file for NAVER-and-affiliate investee changes.
- Monthly, someone contacted each owner, collected files, and re-consolidated.
- Multi-country, multi-currency, multi-tier ownership structures made transaction history hard to manage.
- These numbers can feed **external disclosures** (business reports), so a single wrong figure is not a small matter.

## The reframing: the problem was not Excel

The obvious solution — web form instead of Excel, one database, dashboard, natural-language Q&A, AI-generated monthly report — turned out to solve the wrong problem. Collecting values in one place does not make them trustworthy: a stored "30% ownership" does not explain *why* it is 30%. That requires knowing the order of new investments, share sales, capital increases, and reductions, and how each affected issued and held share counts. Discrepancies against the internal finance ledger or external disclosures could be a different as-of date, an unreflected recent transaction, or a different definition — so neither side can be declared wrong automatically.

Restated problem: **it is hard to explain what transactions produced the current number, and on what basis it can be trusted.**

Goal shifted from "an input screen that replaces Excel" to "a system of record that manages *how the number was produced* alongside *its verification result*."

| Before | NStake |
|---|---|
| Each owner writes Excel | Owner enters transactions |
| Request change notices | Current state computed from transaction history |
| Consolidate many files | Validated against internal rules + external sources |
| Human compares/checks | Discrepancies reviewed and dispositioned |
| Report & disclose | Equity status and report generated |

## Designing what to delegate

The team fixed the **standards that keep work moving end to end** before adding features: work flow, validation criteria, report rules, safeguards.

**Where the work actually ends.** Demo-friendly features (natural-language query, dashboard, auto report) do not finish the owner's job. They mapped: 입력 → 값 검증 → 불일치 발견 → 담당자 확인/처리 → 현재 상태 반영 → 보고. If a saved value can't be checked, the owner reopens Excel. If a mismatch is surfaced but can't be corrected or marked "no issue," it just creates another to-do list. If a report figure can't be traced to its transactions, it can't be used officially. Their yardstick moved **from feature count to workflow completeness**.

**AI as evaluator and verifier, not just code generator.** Roles split into: evaluator (structuring the problem and success criteria), design partner (comparing design options), implementation assistant, and verifier (finding doc↔code mismatches). Loop for each large feature: short design doc → implement → collect test evidence (screenshots, logs) → reflect into deck and README → re-verify that docs match actual execution flow. Recurring review questions became a checklist — "is the feature described in the presentation actually in the code?", "is there any security-risky behavior?", "is a partial implementation being described as complete?" The key difference: they defined success first, then used AI to keep checking results against it.

**Transaction history, not current value.** Instead of editing current issued/held share counts and ownership percentage directly, NStake records the transactions that produced them in time order (capital payment, new investment, paid/free capital increase, share transfer and disposal, capital reduction, stock split, liquidation) and computes current state from them. A divergence between computed and stored state becomes a check item in itself.

**Validation split three ways (Rule / Statistical / eXternal):**

| Class | Meaning |
|---|---|
| **Rule** | Decidable by explicit rule — ownership totals, missing exchange rate, new transaction after liquidation |
| **Statistical** | Signals that narrow what a human looks at first without asserting error — unusually large amounts, abrupt share-count changes |
| **eXternal** | Internal vs. external-disclosure differences where the system must *not* decide right/wrong; a human confirms |

Not everything can be called an "error." Separating system-decidable problems, suspicious values, and human-judgment differences was, in the authors' view, important to overall trustworthiness.

## Design prototype re-judged in user context

The conventional plan → design → dev → QA order was effectively inverted: each discipline pre-planned its own area, and because AI could produce prototypes immediately, implementing first and fixing together beat waiting for a finished spec.

One hour in, three developers had generated the entire NStake UI around a cute steak character in browns and beiges — including on the loading screen. Fast, but likely to unsettle a finance team. For an equity-management system the design goal was not charm: it was information that is no less convenient than Excel and that gives the impression the numbers can be trusted. In the finance team's Excel, **cell colors carried meaning** — yellow, gray, pale blue indicated information state and purpose, not decoration. These users needed familiarity, trust, a formal impression, and professionalism.

So the team dropped the character concept and applied the **NAVER design system** — neutral base with NAVER green as accent, a calm ERP style — and produced app icon, favicon, and logo. With principles written into `design.md`, AI produced overall tone and drafts fast, but reaching the intended level took repeated "that's not it / change to this style" iterations, and some elements had to be redrawn or hand-tuned. **Design became a development bottleneck** while the whole team waited on PNGs. Conclusion: AI accelerated exploration and drafting but was not the final judge; usability had to be re-judged against the finance team's working practices.

## The month-end report was un-generated

Initially transaction history was passed to a model to write the monthly report. Fast to build, good in demo — but wording varied on identical data, sentences drifted from company reporting format, and a model-connection problem would affect official report generation itself. More importantly, transaction classification and totals in an official report are not a wording problem: **the same transaction data must always yield the same result.** So classification into investment / disposal / change and the total calculations became explicit rules, shared by screen and Excel report. **AI was removed from deciding official numbers**, and kept for natural-language Q&A about investment status, turning a user's free-text transaction description into an input draft, and explaining complex discrepancies legibly.

Their resulting delegation table:

| Work characteristic | Applied approach |
|---|---|
| Same input must always give same result | Explicit rules and code |
| Officially computing amounts, quantities, ratios | Deterministic calculation |
| Used directly for financial/legal judgment | Rule-based processing + human approval |
| Multiple phrasings acceptable | Generative AI |
| User can re-review the result | AI-assisted draft generation |
| Narrowing what to check matters more than being right | AI or statistical model |

## Guardrails start at the request, not the response

Guardrails for financial data are usually imagined as filters on dangerous questions or inappropriate answers. In NStake the core was **authorization boundaries**, not response filters. The real questions: who can see which company's data, under whose authority the AI queries it, and how explaining a query result differs from changing data. Letting the AI read everything and then masking part of the final answer was judged unsafe — from the start it must receive only the entities the logged-in user may see and only the tools they may run.

| Boundary | Principle applied |
|---|---|
| Authentication | After internal SSO, issue a separate short-lived token for AI/MCP carrying minimal identity |
| Data authorization | Don't trust the token or the model's judgment — re-check the user's role and assigned entity scope in the DB **on every request** |
| Tool authorization | Separate policies for read, LLM query, write, and admin functions |
| Change approval | State-changing operations (create/update/delete) require explicit user confirmation before execution |
| Information protection | Sensitive-data masking, input length limits, no credentials in logs or error messages |
| Traceability | Append-only audit log of who read/created/updated/deleted what, when |

Their formulation: a safety policy does not end with writing "don't show unauthorized data" in the prompt. Rather than hoping the model follows rules, the authentication/authorization layer and the tool executor **outside** the model must structurally block disallowed actions.

## Limits hit while using AI

### Authorization and execution control

The biggest problem was not a wrong number. Initialization code written to wipe **local** test data ran while connected to the **shared development database**. A recovery script restored the data, but the same execution repeated until the dangerous reset code was fully removed, and final recovery took **over 20 minutes** — not short in a 6-hour hackathon.

This was not simply "AI generated dangerous code." AI wrote the code assuming a local environment; the DB connection target later changed to shared dev. The execution environment changed. Contributing causes: the AI tooling had more privilege than needed, local and shared dev were not sufficiently separated, and the target environment and recovery procedure were not checked before deletion.

Principles adopted afterwards:

- Don't give AI tooling admin privileges by default.
- Clearly separate local / dev / production environments.
- Re-confirm the target environment before deletion or large-scale change.
- Require explicit user approval for destructive operations.
- Confirm backup and recoverability before feature development.
- Verify AI-generated code by actual execution results, not by its explanation.

Conclusion: where AI can access real systems and generate and run code, **privilege and execution control can be a more direct risk than hallucination**.

### "The feature exists" vs. "it works in the job"

Functions and files existed and AI reported features complete, but some were never wired into the flow where a user presses a button and sees a result. Afterwards, completion was not judged by the existence of a file or function — the user had to be able to finish: 로그인 → 담당 회사 확인 → 거래 입력 → 저장 → 검증 → 불일치 확인 → 문제 처리 → 현재 상태·보고서 반영.

The expectation that supplying more material makes AI understand the work also had to be revised. As documents accumulated, differing terms and as-of dates mixed, which file was authoritative became ambiguous, and existing screens conflicted with actual business rules. What was needed was **judgment criteria, not volume**: which document is authoritative, what wins when values differ, which as-of date determines the latest value, who decides exceptions, what is auto-applied versus human-checked. That judgment cannot be delegated to AI — the standards for the work must be set by people.

## Results and open questions

NStake placed **first in the LLM first-pass evaluation**, was chosen for the problem holder's **SUPER (슈퍼패스)**, and placed **first in the final evaluation**. Re-run five more times under the same conditions after the event, it placed first **four** times. Score gaps among top teams were small.

Evaluation noted that NStake did not stop at equity-status entry but connected the workflow through reference-data reconciliation and discrepancy handling. The authors attribute this not to any single AI feature, nor to having built web, mobile app, backend and AI features, but to **all features sharing one workflow**: 입력 → 검증 → 판단 → 처리 → 결과 생성. They are explicit that theirs was not the only correct approach and that small score gaps mean no single feature or document decided the win.

**Not production-ready.** Partial DART reconciliation and audit logging made it into the prototype, but remaining work includes automated reconciliation including the internal finance ledger, production-grade MCP authentication, dev/prod separation, transaction guarantees, audit-log retention and monitoring, and automated tests.

Three questions the authors pose for the next step:

- How far can AI output be trusted, and who does the final check?
- How far should the data AI can see and the actions it can execute be allowed?
- How does a working PoC become a safe, measurable production system?

## Closing claim

Enterprise AX was not adding one more AI feature to existing work: it was redesigning **which judgments are left as rules, which are left to people, and what role AI plays in between**. Their conclusion, paraphrased: a good AI system is not one where AI does many things — it is one where important work does not wobble when AI is wrong or stops. The operative question is what to delegate and what never to delegate.
