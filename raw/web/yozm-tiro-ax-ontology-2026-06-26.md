---
source_url: https://yozm.wishket.com/magazine/detail/3818/
captured: 2026-06-26
title: "Ontology Essential for AX: Starting with Meeting Records (feat. Tiro)"
authors: [Yozm IT, The Plato, Kim Sang-chul (CTO)]
published: 2026-06
publisher: Yozm IT / Wishket (branded content with The Plato)
---

# Ontology Essential for AX: Starting with Meeting Records (feat. Tiro)

**Capture status:** AI-written summary (not verbatim), captured 2026-06-26. Fetched fully via web_fetch from yozm.wishket.com. This is branded content (Yozm IT x The Plato) built around a CTO interview, so all product capability and efficacy claims are vendor-reported.

## Summary

A 10-person Korean team (The Plato, makers of the real-time meeting-transcription product Tiro) runs a ~300,000-user service by operating on a fleet of AI agents grounded in an *organizational ontology* derived from meeting records. The article's thesis: AX (AI transformation) maturity does not start with sophisticated agent technology but with systematically capturing and structuring an organization's own context — decision rationale, exceptions, human judgment — out of meeting transcripts into a "pre-ontology" wiki, so that agents make decisions aligned with the organization's values and knowledge. CTO Kim Sang-chul frames ontology as three layers (data, logic, action) forming an organizational digital twin, and reserves two responsibilities for humans: security and taste.

## Key Points

- **AI-native operations:** small teams scale through AI code generation. Cites Anthropic (80%+ of production code AI-written) and Y Combinator 2025 (4 of 16 batch teams at ~95% AI authorship); Tiro itself reports ~95% AI-generated code, with humans writing rules and aesthetic decisions.
- **Tiro's growth was zero-marketing**, riding an accuracy reputation: deaf users praised its precision; cited as the only tool to correctly transcribe a mixed Swedish-English video. Security creds: ISO 27001, SOC 2 Type II. (Named after Cicero's stenographer Tiro, 79 BCE, framed as the "world's first court reporter.")
- **Why meeting records:** agents need organizational *context* to make quality decisions — "agent quality hinges on what context and knowledge it carries into decision-making." Meeting discourse preserves decision rationale, exceptions, and human judgment that databases and code cannot.
- **Context-aware vs. naive agent example:** facing a customer's declining usage, a naive agent recommends an upsell; a context-aware agent recognizes the customer is in a security audit and offers compliance support instead.
- **Agent architecture = one "digital twin" agent per team member.** Stated goal "Macrohard" (a riff on Musk/xAI): hundreds of agents let the company self-operate without daily human intervention.
- **Named agents:** Mio (paired with teammate "Leo," mirrors his thinking/voice/judgment, converging over time via Slack); Barin (B2B sales; monitors 200+ customer accounts weekly, diagnoses churn risk, drafts contextual responses); Gyeoul (security; co-authors security-review reports with Barin); a Bug-Triage agent (diagnoses from logs, proposes fixes, summons an engineer for review).
- **Control mechanism:** agents validate decisions against a central *rule repository* (gating rules) before executing, and pull real-time org context from the meeting-derived wiki.
- **Ontology (Kim's formulation) = data + logic + action layers.** Data = concepts, names, locations, stakeholders. Logic = rules (e.g., "empty warehouse" means different things to different departments). Action = triggered responses ("if warehouse emptied / if fire breaks out, do X"). Ontology is consensus: "same word, same meaning across the organization."
- **Pre-ontology** = unvalidated concept extraction + relationships + source citations pulled from meeting records — drafting material *before* formal definition. Rationale: leaders mandated to define concepts often lack frontline operational context (a leader defining "warehouse" doesn't visit it daily). The final ontology is formally ratified by the org and added to the operational system.
- **Inspiration: Andrej Karpathy's "LLM Wiki"** — agents extract and index knowledge incrementally rather than re-reading raw sources on every query.
- **AI wiki mechanism (meeting records -> structured knowledge):** (1) transcription -> concept extraction; (2) de-duplication / alias merging ("Tiro"/"타로"/"tiro" into one page); (3) relationship mapping (membership, responsibility, relevance); (4) four-layer page structure: name+aliases / definition / source citation (transcript reference) / related concepts-people-projects; (5) continuous update — new meetings refresh existing pages instead of duplicating.
- **Irreducible human responsibilities:** (1) Security — humans give final approval on infrastructure/DB changes; all alterations logged and reversible; dev environment fully isolated from customer infra ("a flawed feature can be fixed after deploy, but a single infrastructure/DB mistake can be a death sentence"). (2) Taste & philosophy — competitive advantage is aesthetic/strategic judgment, not automation; culture rejects "Apple did X" reasoning and demands self-owned justification ("collision of taste" as brand-building).
- **Metrics/examples:** 10 people; 300,000 users; 200+ B2B deals handled by a single human + agent; ~95% AI-authored code. Sales flow: inquiry -> Barin retrieves 200-account context -> drafts contextual email -> human reviews & sends. Security flow: B2B question -> Gyeoul + Barin auto-generate report -> human review. Bug flow: report -> log analysis -> fix proposal -> engineer summoned -> human approval.
- **Compounding takeaway:** earlier ontology adoption means agents operate on deeper organizational history, widening a knowledge moat over time.

## Follow-up

- Verify the headline metrics (10 people / 300,000 users / ~95% AI code / 200+ B2B deals) against an independent (non-branded) source — these are vendor-reported in promotional content.
- Confirm the exact framing of Karpathy's "LLM Wiki" idea against his original statement, since the article paraphrases it.
- Re-capture if The Plato or Yozm publishes a deeper technical write-up of the pre-ontology -> ontology pipeline (the article is conceptual, not implementation-detailed).
