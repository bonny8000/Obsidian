---
type: source
status: active
created: 2026-06-22
updated: 2026-06-22
tags: [agent-authorization, agent-identity, on-behalf-of, delegated-permissions, confused-deputy, human-in-the-loop, agent-security, langchain, langsmith-fleet]
source_path: raw/web/langchain-agent-authorization-2026-06-22.md
source_url: https://www.langchain.com/blog/two-different-types-of-agent-authorization
authors: [Harrison Chase]
sources: []
ingest_level: standard
coverage: substantial
llm_ready: true
raw_preserved: true
confidence: 0.8
---
# Two Different Types of Agent Authorization (On-Behalf-Of vs Own-Credentials)
**Author:** Harrison Chase (LangChain) — **Published:** 2026-03-23 — LangChain Blog (Deployment / Agent Architecture)
**Raw capture:** [[raw/web/langchain-agent-authorization-2026-06-22|langchain-agent-authorization-2026-06-22]]
**URL:** [langchain.com/blog/two-different-types-of-agent-authorization](https://www.langchain.com/blog/two-different-types-of-agent-authorization)

## Citation

Chase, H. (2026, March 23). *Two different types of agent authorization.* LangChain Blog ("Harrison's In the Loop"). Captured 2026-06-22 into `raw/web/langchain-agent-authorization-2026-06-22.md`. Links a WorkOS post ("Agents need authorization, not just authentication") for future directions.

## Summary

A short, sharp post that names a distinction agent builders routinely blur: **agent authorization** — *who an agent authenticates as when it calls a tool*. When an agent calls Slack, does it pull data as the end user, or as itself? The post identifies **two types**:

- **On-behalf-of** — the agent uses the **end user's own credentials**, so access is scoped per-user (an onboarding agent sees only Alice's Notion/Rippling for Alice, only Bob's for Bob). Requires (a) identifying who is using the agent and (b) mapping that user ID to credentials injected into tools at runtime. This was the default mental model "until OpenClaw came around."
- **Own fixed credentials** — the agent uses authorization the **creator** granted it, identical for everyone who interacts. Using the creator's *personal* credentials is usually undesirable (it would surface their private docs to any user), so builders provision a **dedicated service account** to bound what the agent can reach.

LangSmith Fleet ships both as **Assistants** (on-behalf-of) and **Claws** (own credentials), plus **channels** (Slack/Gmail/Outlook/Teams) and **sharing**. A key consequence the post draws: fixed-credential agents exposed on open channels especially **need human-in-the-loop** guardrails, because they can be invoked in many uncontrolled ways. It flags **per-user memory** as the next problem (an Assistant must not reuse Alice's sensitive memories in Bob's session).

This is the LangChain-vendor, product-shaped statement of exactly the identity problem that [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4 — Vibe Coding Agent Security & Evaluation]] frames as a **security threat model**. The two map cleanly and should be read together: Day 4's *delegated identity* ≈ this post's **on-behalf-of / Assistants**, and Day 4's *distinct agentic identity* ≈ **own-credentials / Claws**. Day 4 supplies the *why it's dangerous* (Confused Deputy, ambient authority) and the *hardening* (JIT downscoping, deny-by-default); this post supplies the *clean two-option vocabulary* and the *when-to-use-which*.

## Key Claims

- **Agent authorization is the operative question, not authentication alone.** The crisp test is "who does the agent authenticate as before pulling the data?" The post explicitly nods to the WorkOS framing that agents need *authorization*, not just authentication.
- **Two types, named:**
  - **On-behalf-of / Assistants** — end-user credentials, per-user scoping; needs user-identification + a user-ID→credentials map at tool-call time.
  - **Own-credentials / Claws** — a fixed credential set the creator granted, shared across all users; typically a **dedicated service account** rather than the creator's personal creds (to avoid exposing the creator's private data).
- **History/driver:** on-behalf-of was the standard model until **OpenClaw** popularized creator-owned agents exposed to others over arbitrary channels (text/email/Twitter).
- **Fleet mapping:** Assistants ↔ on-behalf-of, Claws ↔ own-credentials; **channels** and **sharing** are new. Sharing an Assistant needs a channel-user→LangSmith-ID mapping, so Assistants launch on fewer channels than Claws.
- **HITL is coupled to authorization type:** exposing a fixed-credential agent on a channel "opens it up to be used in a variety of ways," so sensitive/dangerous actions should be gated behind human-in-the-loop guardrails.
- **Memory should differ by type:** today handled via share-time access/edit permissions; **user-specific memory** is planned so an Assistant won't leak Alice's memories to Bob.

## Useful Examples

- **The two-type taxonomy itself** — "on-behalf-of" vs "own fixed credentials" is a reusable, product-agnostic vocabulary for classifying any agent's identity model.
- **Onboarding agent (Assistant)** — Slack + Notion, exposed in Slack, uses the end user's own credentials → per-user data scoping.
- **Email agent (Claw)** — replies to anyone's email using *the creator's* calendar/identity; sending is gated behind a **HITL** guardrail. A concrete pairing of own-credentials + human approval for the dangerous action.
- **Product agent (Claw)** — has its **own Notion account** (the dedicated-service-account pattern in practice) and a custom Slack bot.
- **The dedicated-service-account move** — the standard mitigation when you *don't* want the agent inheriting the creator's full personal access.

## Constraints / Caveats

- **LangChain vendor post, product-framed.** The conceptual split is sound and general, but the implementation, naming (Assistants/Claws), and channel/sharing constraints are LangSmith Fleet's. ~4 min, opinion/announcement register, not a study.
- **Two-type framing is a simplification.** Real systems blend them (an agent acting partly on-behalf-of, partly with service-account scope for shared resources); the post doesn't cover hybrid/per-tool authorization granularity.
- **Authorization ≠ fine-grained authorization.** It establishes *whose* credentials, not *which scopes/permissions within* those credentials (it gestures at this via the WorkOS link and the "more granular memory permissions" follow-up, but doesn't specify a model).
- **Memory leakage across users is acknowledged but unsolved** at time of writing (handled only by coarse share-time permissions).

## Design Implications

- **Decide authorization type per agent, explicitly.** For any agent, answer "whose credentials does it act under?" up front: per-user (Assistant) when access must be scoped to the requester, fixed (Claw) when the agent is a shared service.
- **Prefer a dedicated, least-privileged service account for Claws** — never wire the creator's personal credentials into a shared agent; scope the account to exactly what the agent needs (the practical form of deny-by-default / [[concepts/ai-agents/agent-security-architecture|least-privilege identity]]).
- **Gate Claws' sensitive actions behind [[concepts/ux-research/human-in-the-loop|human-in-the-loop]].** A fixed-credential agent on an open channel is broadly reachable; require approval (or a diff/elicitation step) for dangerous tool calls.
- **For on-behalf-of, invest in the identity mapping** (channel user → platform user → tool credentials); it is the load-bearing piece and limits which channels you can safely expose.
- **Plan memory partitioning by authorization type** — user-specific memory for Assistants so cross-user leakage can't occur; reconcile with Day 4's *contextual associations* dimension of Effective Trust.
- **Reconcile with Day 4's hardening:** pick the identity type here, then apply Day 4's controls (distinct agentic identity, JIT-downscoped self-expiring tokens, deny-by-default file/tool allowlists) so the chosen identity can't be abused as a Confused Deputy.

## Tensions

- **On-behalf-of vs own-credentials = convenience/sharing vs per-user safety.** Claws are trivial to share and reason about (one identity) but concentrate access and broaden the blast radius; Assistants preserve per-user least privilege but need a robust identity-mapping layer and constrain which channels are safe.
- **Confused Deputy risk is *higher* for Claws** (a single over-scoped identity acting for many callers) — this post's "use HITL" is the lightweight mitigation; **[[sources/vibe-coding-agent-security-evaluation-day-4|Day 4]]** is the heavyweight one (zero ambient authority, JIT downscoping, deny-by-default). The two posts agree on the danger; Day 4 goes further on controls.
- **Delegated identity (on-behalf-of) vs distinct agentic identity (own-credentials).** Day 4 argues an over-privileged agent should get a *distinct* identity rather than the human's delegated creds; this post shows both are legitimate *depending on whether the agent is personal or shared* — reconciling: on-behalf-of is fine for a single user's personal agent, but a *shared/exposed* agent should use a distinct, least-privileged identity (a Claw on a dedicated account), which is precisely Day 4's recommendation.
- **Static fixed credentials vs Day 4's "static identity is a poor perimeter."** A Claw's fixed credentials are exactly the static identity Day 4 warns against; the reconciliation is to keep the identity fixed but **downscope and gate** it (JIT tokens + HITL), not to treat the credential as a trust boundary by itself.
- **Sharing/exposure vs control** — exposing agents on channels (the Fleet selling point) is what *creates* the authorization risk the post then has to mitigate with HITL.

## Open Questions

- What is the **fine-grained** authorization model *within* a chosen identity (per-tool, per-scope, time-bounded)? The post defers this to a linked WorkOS piece and a future memory-permissions feature.
- How is the **on-behalf-of identity mapping** (channel user → platform user → tool credentials) secured against spoofing/impersonation at the channel boundary?
- How will **user-specific memory** actually partition state for Assistants, and does it compose with Day 4's "contextual associations" trust dimension?
- For **Claws**, how is the dedicated service account itself governed (rotation, scope review, audit binding action→agent→human) — i.e. the Day 4 Governance pillar applied to a shared agent identity?
- (Image gap) The **"Agent identity" diagram** (`Fleet-agent-identity.png`) carried only the alt text "Agent identity"; its internal box/arrow labels were not text-recoverable. Content was reconstructed from prose (Assistants=end-user creds vs Claws=own fixed creds, over channels). The hero banner is decorative.

## Concepts Linked

- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]] — authorization-by-identity is the IAM pillar; least-privilege service accounts, deny-by-default, and "static identity is a poor perimeter" all bear directly on choosing/hardening an agent's identity type.
- [[concepts/ux-research/human-in-the-loop|Human-in-the-Loop]] — the post's primary mitigation for fixed-credential agents on open channels: gate sensitive actions behind human approval.
- [[concepts/ai-agents/managed-ai-agents|Managed AI Agents]] — LangSmith Fleet's Assistants/Claws + channels + sharing is a managed-agent platform model; authorization type is a first-class managed-agent setting.
- [[concepts/ai-agents/agentic-ai|Agentic AI]] — agents that call tools and take actions are exactly what needs an authorization model.
- [[concepts/agent-experience/agent-transparency|Agent Transparency]] — knowing *whose* credentials an agent acts under (and surfacing that to users it's shared with) is a transparency/trust concern.
- [[concepts/ai-agents/agent-authorization|Agent Authorization]] (new) — who an agent authenticates as when it acts (end user's delegated credentials "on-behalf-of" vs the agent's own fixed/service-account identity), and the per-user-scoping vs shared-blast-radius tradeoff between them. Strongly durable; unifies this post with Day 4's delegated-vs-agentic-identity and the Confused Deputy / zero-ambient-authority discussion.

## LLM Use

- **Use for:** giving teams the clean two-option vocabulary (on-behalf-of vs own-credentials) for an agent's identity; deciding which to use (per-user-scoped vs shared service); the dedicated-service-account pattern; coupling HITL to fixed-credential agents; reasoning about cross-user memory leakage. Pair with Day 4 for the threat model and hardening.
- **Do not use for:** a fine-grained authorization/permission-scope model (out of scope here); treating Assistants/Claws naming or Fleet channel constraints as general standards; assuming a fixed credential is itself a sufficient trust boundary (apply Day 4's downscoping/HITL).
- **Best prompt pattern:** "Classify this agent's authorization as on-behalf-of (Assistant) or own-credentials (Claw): does access need to be scoped to the requesting user, or is it a shared service? Then harden it with Day 4's controls — distinct least-privileged identity / dedicated service account, JIT-downscoped tokens, deny-by-default, and HITL gates on sensitive actions — and check for Confused-Deputy and cross-user memory-leak risks."

## Reliability Notes

> [!warning] Caveats
> - **LangChain vendor post** (announcement tied to LangSmith Fleet), "Harrison's In the Loop," 2026-03-23. Confidence **0.8** on the conceptual taxonomy (clear, general, and consistent with the security literature); apply a vendor lens — the implementation, naming (Assistants/Claws), and channel/sharing limits are LangChain product specifics, not standards.
> - Architecture diagrams not pixel-parsed; content captured from surrounding text/tables. The one explanatory image ("Agent identity") yielded only alt text; its labels were reconstructed from prose and may omit detail (flagged under Open Questions).
> - Short opinion/announcement register, not an evaluation or study; the deeper threat model and hardening live in [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4]], which should be read alongside it.

## Backfill Status

- Newly written 2026-06-22 from a full web capture (article read end-to-end; the three worked examples and both diagrams noted). All sections populated. `coverage: substantial` — the prose is fully captured; the one explanatory diagram's internal labels were not text-recoverable (see Open Questions / Reliability Notes). Part of the LangChain security/governance cluster; heavily cross-linked to [[sources/vibe-coding-agent-security-evaluation-day-4|Day 4]] (Confused Deputy / delegated-vs-agentic-identity / zero ambient authority) and adjacent to [[sources/bayer-prince-reliable-agentic-ai|Bayer PRINCE]] and [[sources/langchain-multi-agent-architecture|LangChain Multi-Agent Architecture]].
