---
type: source
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [organizational-ontology, agentic-automation, meeting-records, agent-digital-twin, llm-wiki, pre-ontology, human-in-the-loop, ai-native-team, vendor-reported]
source_path: raw/web/yozm-tiro-ax-ontology-2026-06-26.md
source_url: https://yozm.wishket.com/magazine/detail/3818/
authors: [Yozm IT, The Plato, Kim Sang-chul]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.75
---

# The Plato / Yozm IT (2026): Ontology Essential for AX — Starting with Meeting Records (feat. Tiro)

**Author:** Yozm IT with The Plato; interview with CTO Kim Sang-chul (김상철) — Yozm IT / Wishket (branded content), 2026-06.
**Raw capture:** [[raw/web/yozm-tiro-ax-ontology-2026-06-26|yozm-tiro-ax-ontology-2026-06-26]]
**URL:** [yozm.wishket.com/magazine/detail/3818](https://yozm.wishket.com/magazine/detail/3818/)

## Citation

Yozm IT & The Plato (2026, June). *Ontology essential for AX: Starting with meeting records (feat. Tiro)* [interview with CTO Kim Sang-chul]. Yozm IT (Wishket). Captured 2026-06-26 into raw/web/yozm-tiro-ax-ontology-2026-06-26.md.

## Summary

The Plato — a 10-person Korean team behind the real-time meeting-transcription product Tiro — argues that AX (AI transformation) does not begin with advanced agent technology but with **structuring an organization's own context out of its meeting records**. Decision rationale, exceptions, and human judgment live in meeting *discourse*, not in databases or code, so the team mines transcripts into a "pre-ontology" wiki and ratifies it into a formal **organizational ontology** of three layers — data, logic, action — that functions as an organizational digital twin. On top of this they run a fleet of per-person agents (one "digital twin" per team member) that pull real-time context from the wiki and validate every action against a central rule repository before executing. CTO Kim Sang-chul carves out two human-only responsibilities — **security** (final approval on infrastructure/DB changes) and **taste** (aesthetic and strategic judgment) — and frames earlier ontology adoption as a compounding moat. As branded content built on a vendor interview, its operational and efficacy claims are vendor-reported.

## Key Claims

- **AX starts with meeting records, not agent sophistication.** The scarce input is *organizational context*; "agent quality hinges on what context and knowledge it carries into decision-making," and that context lives in meeting discourse, not in databases or code.
- **Ontology = data + logic + action layers** forming an organizational digital twin. **Data** = concepts, names, locations, stakeholders; **logic** = department-specific rules (what "empty warehouse" means differs by team); **action** = triggered responses. Ontology is fundamentally **consensus**: "same word, same meaning across the organization."
- **Pre-ontology before formal ontology.** A **pre-ontology** is unvalidated concept extraction + relationships + transcript citations — drafting material that surfaces frontline language and edge cases *before* premature top-down definition. Rationale: leaders told to define concepts often lack the operational frontline context to do it well.
- **Per-person agent "digital twins."** One agent per team member; the stated end-state ("Macrohard") is hundreds of agents letting the company self-operate without daily human intervention.
- **Agents are gated, not autonomous.** Every agent validates decisions against a central **rule repository** and pulls live org context from the meeting-derived wiki before acting; humans approve high-stakes steps.
- **Two irreducible human responsibilities.** **Security** (final human approval on infra/DB changes; all changes logged and reversible; dev fully isolated from customer infra) and **taste/philosophy** (the real competitive moat; culture rejects "Apple did X" copying and demands self-owned justification).
- **Compounding knowledge moat.** Adopting the ontology earlier means agents reason over deeper organizational history, widening the advantage over time.
- **AI-native scaling.** Small teams scale via AI code generation; The Plato reports ~95% AI-authored code, with humans writing the rules and the aesthetic decisions.

## Useful Examples

- **Context-aware vs. naive agent:** a customer's usage declines; a naive agent recommends an upsell, while the context-aware agent recognizes the customer is mid security-audit and offers compliance support instead.
- **Named agents:** **Mio** (paired with teammate "Leo," mirrors his thinking/voice/judgment, converging over time via Slack); **Barin** (B2B sales; monitors 200+ customer accounts weekly, diagnoses churn risk, drafts contextual replies); **Gyeoul** (security; co-authors security-review reports with Barin); a **Bug-Triage agent** (diagnoses from logs, proposes a fix, then summons an engineer for review).
- **The AI-wiki pipeline:** transcription -> concept extraction -> alias de-duplication (merging "Tiro"/"타로"/"tiro" into one page) -> relationship mapping -> a four-layer page (name+aliases / definition / transcript citation / related concepts-people-projects) -> continuous refresh on each new meeting.
- **Operational metrics (vendor-reported):** 10 people; ~300,000 users; 200+ B2B deals handled by a single human + agent; ~95% AI-authored code. Tiro reportedly transcribed a mixed Swedish-English video correctly where others failed; holds ISO 27001 and SOC 2 Type II.
- **Lineage:** the AI-wiki idea is credited to Andrej Karpathy's "LLM Wiki" (agents incrementally extract/index knowledge instead of re-reading raw sources each query); the product name Tiro nods to Cicero's stenographer (79 BCE).

## Constraints / Caveats

- **Branded content + vendor CTO interview** (Yozm IT x The Plato). Treat all capability, efficacy, and headline metrics (10 people / 300k users / ~95% AI code / 200+ deals) as **vendor-reported and unverified**; no independent benchmark or audit is presented.
- **Conceptual, not implementation-grade.** The pre-ontology -> ontology pipeline and gating-rule mechanism are described at the level of narrative, not engineering detail; reproducing them would require information the article does not give.
- **Single source, single company.** One Korean startup's self-account; the generalizability of "start with meeting records" beyond a 10-person AI-native team is asserted, not demonstrated.
- **Coverage `substantial`, ingest `standard`** — well-captured but not exhaustively cross-verified; do not treat metrics as established fact.

## Design Implications

- **Treat organizational context as the primary agent substrate.** Before investing in agent autonomy, invest in capturing decision rationale and exceptions — meeting transcripts are a high-yield, under-exploited source for an [[concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]].
- **Build the wiki before the ontology.** The pre-ontology -> ratified-ontology path is a concrete instance of an [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]] and directly parallels Bonny's own [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]] practice (concept extraction, alias de-duplication, source citation, continuous refresh).
- **Gate agents on a rule repository and keep humans on the irreducible loop.** Agents that check a central rule store and require human sign-off on security/infra steps are a worked example of [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] applied to [[concepts/ai-agents/agentic-work-automation|Agentic Work Automation]].
- **Per-person "digital twin" agents** ([[concepts/ai-agents/agent-digital-twin|Agent Digital Twin]]) are a design pattern for [[concepts/ai-agents/harness-engineering|Harness Engineering]]: each agent is scoped to mirror one role's judgment and draws role-specific [[concepts/ai-agents/agent-memory|Agent Memory]] from the wiki.
- **The three-layer (data/logic/action) ontology** is a lighter-weight cousin of the [[concepts/infrastructure-dev/palantir-foundry-ontology|Palantir Foundry Ontology]] and of [[concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]] — useful as a vocabulary for structuring org knowledge that agents can act on.
- **Frame early adoption as [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]**, and read the 10-person/300k-user story as a data point for the [[concepts/product-management/10-person-unicorn|10-Person Unicorn]] thesis — while keeping the metrics flagged as vendor claims.
- **Reserve taste as the human moat** — [[concepts/product-management/product-taste|Product Taste]] as the differentiator that automation cannot supply.

## Tensions

- **Autonomy vs. control.** The "hundreds of agents, self-operating company" ambition sits against the gating rule-repository and mandatory human approval on security/infra — the article resolves this rhetorically more than mechanically.
- **Bottom-up pre-ontology vs. ratified consensus.** Surfacing frontline language contradicts the claim that ontology is org-wide consensus; reconciling messy transcript reality with a single ratified vocabulary is the hard, under-described step.
- **"Taste is the irreducible human moat" vs. ~95% AI-authored code.** If aesthetic/strategic judgment is the differentiator, it is in tension with how much production work is already delegated to agents; the boundary is asserted, not operationalized.
- **Vendor narrative vs. evidence.** The compounding-moat and efficiency claims are exactly what branded content is incentivized to overstate; the [[concepts/product-management/10-person-unicorn|10-Person Unicorn]] framing is inspiring but unaudited.

## Open Questions

- How exactly is a **pre-ontology promoted to a ratified ontology** — who arbitrates conflicting transcript definitions, and how are disputes logged?
- What is in the **rule repository**, how are gating rules authored and versioned, and how do agents fail safe when a decision has no matching rule?
- How is **alias de-duplication** validated (precision/recall) so that wrongly merged concepts don't corrupt downstream agent decisions?
- What independent evidence supports the **~95% AI-authored code** and **200+ B2B deals per human** figures?
- How transferable is "start with meeting records" to **non-AI-native or larger organizations** where meetings are noisier and trust is lower?

## Concepts Linked

- [[concepts/infrastructure-dev/organizational-ontology|Organizational Ontology]]
- [[concepts/ai-agents/agent-digital-twin|Agent Digital Twin]]
- [[concepts/infrastructure-dev/llm-wiki|LLM Wiki]]
- [[concepts/ai-agents/ai-maintained-wiki|AI-Maintained Wiki]]
- [[concepts/infrastructure-dev/palantir-foundry-ontology|Palantir Foundry Ontology]]
- [[concepts/infrastructure-dev/object-graph-mapping|Object-Graph Mapping]]
- [[concepts/ai-agents/agentic-work-automation|Agentic Work Automation]]
- [[concepts/ai-agents/harness-engineering|Harness Engineering]]
- [[concepts/ai-agents/agent-memory|Agent Memory]]
- [[concepts/product-management/compounding-knowledge|Compounding Knowledge]]
- [[concepts/product-management/10-person-unicorn|10-Person Unicorn]]
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]]
- [[concepts/product-management/product-taste|Product Taste]]

## LLM Use

- **Use for:** reasoning about how to bootstrap an organizational ontology from meeting records; the pre-ontology concept and the meeting-record -> structured-wiki pipeline; per-person "digital twin" agent design; framing the data/logic/action ontology layers; arguments for keeping security and taste as human responsibilities; the compounding-knowledge / small-AI-native-team thesis.
- **Do not use for:** citing the headline metrics (10 people / 300k users / ~95% AI code / 200+ deals) as verified fact; treating Tiro's accuracy or security claims as benchmarked; reconstructing implementation details of the ontology pipeline or rule repository (not provided).
- **Best prompt pattern:** "Using The Plato/Tiro's pre-ontology approach, outline how to extract an organizational ontology (data/logic/action layers) from our meeting transcripts: concept extraction, alias de-duplication, relationship mapping, transcript citations, and where to gate agents on a rule repository with human approval — and flag which efficacy claims are vendor-reported."

## Reliability Notes

> [!warning] Caveats
> - **Confidence 0.75.** The conceptual frame (meeting-records -> pre-ontology -> ratified ontology; data/logic/action layers; gating + human-only security/taste) is coherent, original, and directly useful. But this is **branded content built on a vendor CTO interview**, so every operational and efficacy claim — team size, user count, ~95% AI-authored code, 200+ deals per human, Tiro's transcription accuracy — is vendor-reported and unverified.
> - Treat the ideas as a strong design vocabulary, not the metrics as evidence; verify any number against an independent source before reuse.

## Backfill Status

- New 2026-06-26. All sections populated from a full-text web_fetch. Coverage would rise to `full` and confidence above 0.8 with: (1) an independent (non-branded) corroboration of the headline metrics; (2) a technical write-up of the pre-ontology -> ontology pipeline and rule repository; (3) confirmation of the Karpathy "LLM Wiki" framing against his original wording.
