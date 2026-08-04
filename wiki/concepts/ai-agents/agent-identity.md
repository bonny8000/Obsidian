---
type: concept
status: active
created: 2026-05-18
updated: 2026-08-04
tags: [ai-agent, identity, governance, security]
sources:
  - sources/brunch-ghidesigner-472
  - sources/cloudflare-responsible-ai-bot-principles
confidence: 0.66
---

# Agent Identity

## Summary

Agent identity is the practice of giving an AI agent a distinct, auditable identity that can be granted permissions, tracked in logs, and governed separately from human users.

## Why It Matters

Agents that edit files, access tools, or retrieve sensitive information need accountability. A distinct identity helps organizations know what an agent did, under whose authorization, and with which permissions.

## Key Claims

- Agent identity supports traceability and permission management.
- Long-running design or research agents need scoped access rather than broad ambient access.
- Identity works with logging, review, and policy enforcement.

## Related Concepts

- [[concepts/infrastructure-dev/enterprise-ai-agent-platform|Enterprise AI Agent Platform]]
- [[concepts/infrastructure-dev/cloud-ai-governance|Cloud AI Governance]]
- [[concepts/ai-agents/managed-ai-agents|Managed AI Agents]]

## Sources

- [[sources/brunch-ghidesigner-472|Brunch: Google Gemini Enterprise for UXUI Design]]

## Open Questions

- [Answered → [[queries/2026-05-27-agent-attribution-shared-artifact|Query Page]]] How should agent actions be attributed when both human and agent contribute to the same artifact?
- **Has Web Bot Auth been adopted beyond OpenAI and Vercel?** The load-bearing question for internet-scale agent identity, and unchecked here as of 2026-08-04.

## Agent Identity on the Open Web

> [!important] Added 2026-08-04 — the first cryptographic answer in this vault
> This concept has treated identity as an intra-system concern (which agent acted, on whose authority, inside a product). [[wiki/sources/cloudflare-responsible-ai-bot-principles|Cloudflare (2025/2026)]] extends it to the wire.
>
> **The problem:** every crawler preference mechanism in existence — including all of `robots.txt` (RFC 9309) — is keyed to a **self-reported user-agent string**, which is trivially forgeable. So the web's whole consent layer runs on crawler honesty. *"Bots are increasingly vulnerable to being spoofed by bad actors."*
>
> **The proposed fix:** **Web Bot Auth**, an IETF draft layering bot identity over **RFC 9421 HTTP Message Signatures**, with a companion signatures-directory draft for key discovery. Deployed by OpenAI's ChatGPT agent and supported by Vercel; still a draft.
>
> **The identity claim is three-part:** who the bot is (user agent, IPs, cryptographic ID), who operates it (legal entity plus contact), and **what it is for** — one of search, AI-input, or training. Purpose is part of identity here, which is a genuine extension: OpenAI runs GPTBot and OAI-SearchBot as separate declared identities precisely so the purpose is verifiable per request.
>
> **The caveat that matters:** until the draft deploys, all of this is unverifiable self-reporting. See [[wiki/concepts/infrastructure-dev/ai-crawler-governance|AI Crawler Governance]] and [[wiki/analyses/2026-08-04-crawl-consent-vs-answer-surfaces|the 2026-08-04 memo]]. Cloudflare also sells the enforcement layer, which is worth holding in mind.

## Additional Sources

- [[wiki/sources/cloudflare-responsible-ai-bot-principles|Cloudflare (2025/2026): Responsible AI Bot Principles]] — Web Bot Auth, the disclosure requirements, and purpose-as-identity.

