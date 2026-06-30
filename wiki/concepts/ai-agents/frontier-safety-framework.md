---
type: concept
status: active
created: 2026-06-26
updated: 2026-06-26
tags: [frontier-safety-framework, ai-safety, google-deepmind, agentic-ai, guardrails]
sources:
  - sources/gemini-3-5-launch
  - sources/google-io-2026-agentic-gemini
confidence: 0.5
---

# Frontier Safety Framework

## Summary

The **Frontier Safety Framework (FSF)** is Google DeepMind's governance framework for operating frontier / agentic models within cybersecurity and ethical guardrails. In this vault it appears as the safety layer paired with [[concepts/ai-agents/gemini-3-5|Gemini 3.5]] — the controls meant to keep highly autonomous agents inside acceptable bounds as they execute long-horizon, multi-step tasks.

## Why It Matters

As models shift from answering questions to autonomously *acting* (the [[concepts/ai-agents/agentic-ai|agentic AI]] turn), the risk surface moves from "wrong answer" to "wrong action at scale." A safety framework is what lets a vendor ship autonomy commercially — the production counterpart, on the model-provider side, to project-level [[concepts/ai-agents/zero-trust-agent-development|zero-trust]] practices.

## Key Claims

- FSF is cited as the safety/guardrail layer accompanying Gemini 3.5's "actionability" and long-horizon agent workflows (cybersecurity + ethical operation).
- It is positioned as a precondition for deploying highly autonomous agents at enterprise scale.

## Related Concepts

- [[concepts/ai-agents/gemini-3-5|Gemini 3.5]]
- [[concepts/ai-agents/agentic-ai|Agentic AI]]
- [[concepts/ai-agents/agent-security-architecture|Agent Security Architecture]]
- [[concepts/ai-agents/zero-trust-agent-development|Zero-Trust Agent Development]]
- [[concepts/infrastructure-dev/eu-ai-act-compliance|EU AI Act Compliance]]

## Conflicts & Caveats

> [!warning] Thin grounding
> Created during a 2026-06-26 lint pass to resolve dangling links from the Gemini sources. Both anchor sources are `coverage: partial` / `llm_ready: false` Google company-blog notes that only *mention* the FSF; its actual mechanisms (risk tiers, evaluations, mitigations) are not captured here. Confidence 0.5 — expand from a primary DeepMind FSF source on the next relevant ingest.

## Sources

- [[sources/gemini-3-5-launch|Introducing Gemini 3.5: Cutting-Edge Intelligence with Action]]
- [[sources/google-io-2026-agentic-gemini|Google I/O 2026: The Beginning of the Agentic Gemini Era]]

## Open Questions

- What are the FSF's concrete risk tiers, evaluations, and mitigation gates?
- How does it compare to other frontier labs' safety/preparedness frameworks?
