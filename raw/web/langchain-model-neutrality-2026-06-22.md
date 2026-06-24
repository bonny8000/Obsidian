---
source_url: https://www.langchain.com/blog/model-neutrality
captured: 2026-06-22
title: Why Model Neutrality Matters More Than Cloud Neutrality
authors: [Neil Dahlke]
published: 2026-06-04
publisher: LangChain Blog
---
# Why Model Neutrality Matters More Than Cloud Neutrality
**Author:** Neil Dahlke **Published:** 2026-06-04 — LangChain Blog (Agent Architecture)

## Summary

An argument-driven LangChain post (by Neil Dahlke, ex-HashiCorp) that the agent era is repeating the cloud-lock-in story, and the right defense is a **neutral harness** — the equivalent of what Terraform was for cloud. The framing: every ~20 years software gets rebuilt (on-prem→cloud was the last shift; agents are the next), and each shift raises the same questions about vendor dependence, captive business logic, and exit cost. Enterprises answered late last time and paid for a decade in lock-in, unpredictable pricing, and failed migrations. We're about to repeat it with models.

The cloud-era lesson Dahlke draws: hyperscalers sold **commodities** (storage, network, compute — indistinguishable at the bytes-on-disk level), so the durable way to retain customers was lock-in at the **tooling layer** (CloudFormation/ARM/Vertex), which had no incentive to support competitors at parity. Terraform's reason to exist was a neutral abstraction one layer up — the right to switch and to mix providers without rewriting infra — and that argument won. Now the foundation labs are running the same play: tokens are an increasingly commoditizing commodity (closing frontier gaps, catching-up open weights, two-year price-per-token decline), so the labs' next move is to capture you at the **harness** — Claude Agent SDK, OpenAI Agents API, Vertex AI Agent Builder — because if they own the orchestration layer your business logic lives in, you keep buying their tokens even when a better/cheaper model exists. They have no incentive to make competitors' models first-class in their harness; harness lock-in is *harder* to unwind than model lock-in because that's where business logic lives.

Dahlke argues model neutrality matters *more* than cloud neutrality for three reasons (rate of change, selective commoditization, real open-weight options), adds that neutrality in the agent era is exercised *within a single run* (not just at contract renewal), and defines a neutral harness as three things: open source, multi-model out of the box, and profile-aware (not lowest-common-denominator). This is positioned as exactly what LangChain built with **Deep Agents**.

## Key Points

- **Generational shift framing:** software gets restructured every ~20 years; on-prem→cloud was last, agents are next — but this shift is happening in months, not years.
- **Cloud lesson:** hyperscalers sold commodities (storage/network/compute); the durable retention play was tooling-layer lock-in (CloudFormation, ARM templates, Vertex), with no incentive to support competitors at parity. Terraform won by being a neutral abstraction one layer up — the right to switch and to mix providers in one deployment without rewriting infra.
- **The labs are running the same play:** they sell **tokens** (an increasingly commoditizing commodity — closing frontier gaps, fast-catching open-weight models, a two-year downward price-per-million-tokens slope), so their next move is to **capture you at the harness**: Claude Agent SDK, OpenAI's Agents API, Vertex AI Agent Builder — "all the same shape."
- **Why the harness is the lock-in point:** if a lab owns the orchestration layer your business logic lives in, you keep consuming its tokens even when a better/cheaper/more-appropriate model exists. They have no commercial incentive to make competitors' models feel first-class. **Harness lock-in is harder to unwind than model lock-in** because the harness is where business logic lives.
- **Why model neutrality matters MORE than cloud neutrality — three reasons:**
  1. **Rate of change is different.** You move clouds maybe once every few years (renewal/outage); labs leapfrog each other every quarter or month. A locked-in team is locked out of the next leap every time.
  2. **Models are selectively commoditizing.** Easy dimensions (basic reasoning, generic Q&A, summarization) are eroding, but not everywhere: Anthropic currently leads coding (OpenAI closing), OpenAI leads multimodal; rankings shift every few months. The right production answer is often **multiple models in one workflow**, routing each task to whichever is best today — only possible with a side-neutral harness.
  3. **Open-weight models are a real option.** Llama, Mistral, DeepSeek, Qwen; self-hosting is credible in a way private cloud never was — so neutrality is offensive too (mix closed+open, route to cheapest/fastest/most-accurate, switch when a better one ships).
- **New layer vs cloud:** cloud neutrality was cashed in at renewal or during an outage; **model/agent neutrality is exercised within a single agent run** — Claude for a coding step, GPT for an image step, failover mid-execution on a rate limit, drop to a cheaper model where the expensive one isn't justified. "Cloud neutrality stopped at the contract. Agent neutrality has to follow the request."
- **A neutral harness is three things:**
  1. **Open source** — read every line; nothing hidden or captured. A closed-source agent framework shipped by a model lab is *not* neutral regardless of marketing.
  2. **Multi-model out of the box** — same harness, any backend (GPT, Claude, Gemini, Llama, Mistral, DeepSeek, Qwen, self-hosted behind your firewall); one agent definition, every provider first-class.
  3. **Profile-aware, not lowest-common-denominator** — neutrality is not pretending every model is interchangeable; expose **model profiles** so you can exploit each model's strengths/prompt patterns/tool-calling styles without being captive. "The right to switch. Not the requirement to flatten."
- **Positioning:** this is what LangChain built with **Deep Agents** — open, multi-model, profile-aware — "a harness designed to outlast any single model provider."
- **Closing stakes:** same pattern as cloud, but moving an order of magnitude faster, and the cost of getting it wrong compounds an order of magnitude faster too.

## Diagrams (content from text/captions)

The post's embedded images are the hero banner (`neutrality.png`), the author headshot, and related-post thumbnails. There are no explanatory architecture diagrams in the body — the argument is entirely prose, so there is no additional diagram content to recover.

## Short Quotes

- "We're about to do the exact same thing with models. We just lived through the last one. The lesson is right there."
- "Claude Agent SDK has no reason to make calling GPT, Gemini, or Llama feel first-class. From the lab's perspective, making competitors' models work well inside their harness costs revenue. They aren't going to."
- "The harness lock-in is going to be harder to unwind than the model lock-in itself, because the harness is where your business logic lives."
- "Cloud neutrality stopped at the contract. Agent neutrality has to follow the request."
- "The right to switch. Not the requirement to flatten."
