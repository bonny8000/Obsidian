---
source_url: https://www.langchain.com/blog/two-different-types-of-agent-authorization
captured: 2026-06-22
title: Two different types of agent authorization
authors: [Harrison Chase]
published: 2026-03-23
publisher: LangChain Blog
---

# Two different types of agent authorization
**Author:** Harrison Chase ("Harrison's In the Loop") — **Published:** 2026-03-23 — LangChain Blog (Deployment / Agent Architecture)

> Immutable capture. AI-written summary, key points, short quoted excerpts, and diagram-content notes only — no full article text. See the source URL for the complete article. Reading time: ~4 min.

## Summary

A short post (tied to the LangSmith Fleet launch) that names a distinction many agent builders blur: **agent authorization** — what an agent is authorized to do and, concretely, *who it authenticates as* when it calls a tool (e.g. when an agent calls a Slack tool, whose data does it pull?). The post identifies **two different types**:

1. **On-behalf-of** — the agent operates with the **end user's own credentials**. This was "the standard way that most people thought of agents until recently." Example: an onboarding agent with access to Notion and Rippling — when Alice uses it, it sees only Alice's Rippling records and Alice's Notion pages; when Bob uses it, only Bob's. Implementing this requires (a) knowing *who* is using the agent (Alice vs Bob) and (b) mapping those user IDs to auth credentials passed into tools at runtime.
2. **Own fixed credentials** — popularized by "OpenClaw." Here the creator (Alice) builds an agent and exposes it to others (via text, email, Twitter, etc.); when others interact with it, it does **not** use the end user's credentials — it uses the authorization **Alice gave it**. Using Alice's own credentials is possible but usually undesirable (the agent could then surface Alice's private docs to anyone who asks), so people create **dedicated service accounts** (a dedicated Notion/Rippling account for the agent) to control its access. Everyone interacting then effectively shares one set of credentials.

**LangSmith Fleet** ships both as two agent types: **Assistants** (act "on-behalf-of" their end user) and **Claws** (have their own fixed credentials). Fleet also adds **channels** (Slack, Gmail, Outlook, Teams to start) and **agent sharing**. Because Assistants act per-user, sharing one requires mapping a channel user (e.g. a Slack user ID) to a LangSmith ID, so Assistants are initially available only in the subset of channels where that mapping exists. The post stresses that fixed-credential agents exposed on open channels especially **need human-in-the-loop** guardrails for dangerous/sensitive actions, since they can be invoked in many ways. It closes by pointing at WorkOS's "agents need authorization, not just authentication" piece for future directions, and flags upcoming **per-user / granular memory permissions** (an Assistant shouldn't remember sensitive things about Alice and reuse them in a chat with Bob).

## Key Points

- **Agent authorization = what the agent is authorized to do**; the crisp operational question is *who does the agent authenticate as* when it calls a tool. This is **authorization**, distinct from authentication (the post links WorkOS's "agents need authorization, not just authentication").
- **Two types:**
  - **On-behalf-of / Assistants** — uses the **end user's** credentials; per-user scoping (Alice sees only Alice's data, Bob only Bob's). Requires identifying the current user and mapping user IDs → credentials injected into tools at runtime.
  - **Own-credentials / Claws** — uses a **fixed** credential set the creator granted; same credentials for everyone who interacts. Often implemented via a **dedicated service account** rather than the creator's personal credentials (to avoid leaking the creator's private data).
- **History:** on-behalf-of was the default mental model "until OpenClaw came around," which popularized creator-owned agents exposed to others through arbitrary channels.
- **Fleet specifics:** Assistants vs Claws map 1:1 onto the two authorization types; **channels** (Slack, Gmail, Outlook, Teams) and **sharing** are new; Assistants need a channel-user → LangSmith-ID mapping to be shared, so they launch on fewer channels than Claws.
- **HITL is coupled to authorization type:** a fixed-credential agent exposed on a channel is "opened up to be used in a variety of ways," so sensitive/dangerous actions should be gated behind human-in-the-loop guardrails.
- **Memory is the next frontier:** memory should be handled differently per type; today managed via access permissions (when you share an agent you choose whether others can edit it/its memory); **user-specific memory** is planned so an Assistant won't reuse Alice's sensitive memories in Bob's session.

## Short Quoted Excerpts

- "Agent authorization refers to what the agent is authorized to do. When an agent calls a Slack tool - who does it *authenticate* as before pulling the data?"
- "The standard way that most people thought of agents until recently is that they operate 'on-behalf-of' a user."
- "When others interacted with that agent, it didn't use the credentials of the end user - it used the authorization that Alice had given it."
- "Assistants: act 'on-behalf-of' their end user" / "Claws: have their own fixed credentials"

## Worked Examples (the three real Fleet agents)

- **Onboarding Agent — Assistant.** Access to Slack and Notion, exposed in Slack; uses the **end user's** Slack and Notion credentials.
- **Email Agent — Claw.** Responds to incoming email; regardless of who emails, it reads **the creator's** calendar for availability and replies on the creator's behalf. Sending emails / calendar invites is **gated behind a HITL guardrail**.
- **Product agent — Claw.** Monitors competitors, answers product/roadmap questions; has its **own Notion account** and is exposed via a custom Slack bot.

## Diagrams (content captured from text/captions)

The post has a hero banner (`agent-identity-banner.png`, decorative) and **one explanatory diagram** captioned **"Agent identity"** (`Fleet-agent-identity.png`). web_fetch returned the hero as bare `![]()` and the explanatory image with only the alt text "Agent identity" — no internal labels were recoverable as text.

- *"Agent identity" diagram* — from the surrounding prose, it depicts the two-way split of Fleet agent authorization: **Assistants** authenticating as the **end user** (per-user credentials, on-behalf-of) vs **Claws** authenticating with the agent's **own fixed credentials** (e.g. a dedicated service account, shared across all users), layered over the new **channels** (Slack/Gmail/Outlook/Teams) and sharing model. The precise box/arrow labels are not text-recoverable from the capture.

## Provenance Notes
- Primary source: LangChain engineering blog (vendor), "Harrison's In the Loop." Author Harrison Chase. Published 2026-03-23. ~4 min.
- Vendor lens: frames the distinction around **LangSmith Fleet** (Assistants/Claws, channels, sharing) — the conceptual taxonomy (on-behalf-of vs own-credentials) is product-agnostic but the implementation and naming are LangChain's.
- External pointer: links a WorkOS blog ("Agents need authorization, not just authentication") for future directions; cites "OpenClaw" as the trend that popularized creator-owned, externally-exposed agents.
