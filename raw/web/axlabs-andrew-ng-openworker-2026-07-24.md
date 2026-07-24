---
source_url: https://theaxlabs.com/blog/andrew-ng-openworker-practical-guide
captured: 2026-07-24
title: "Andrew Ng가 공개한 OpenWorker, 채팅이 아니라 일을 끝내는 AI"
authors: [AX LABS]
published: 2026-07-23
publisher: AX LABS Blog
language: ko
---

# OpenWorker — AI That Finishes Work, Not Just Chats (AX LABS)

**Original title (ko):** 「Andrew Ng가 공개한 OpenWorker, 채팅이 아니라 일을 끝내는 AI」
**Published:** 2026-07-23 · **Captured:** 2026-07-24
**Capture note:** AI-written summary of a Korean-language practical guide. Full text not reproduced.

## Summary

A practical guide to **OpenWorker**, released by Andrew Ng's team. The framing is a shift from AI as an answer-producing chatbot to AI as a colleague that returns **finished deliverables** — documents, emails, reports — assembled from the tools you already use. Its two defining architectural commitments are **local-first** data handling and a mandatory **approval gate** before any consequential action.

## Key Points

- **Deliverable-focused, not advice-focused.** The output is the artifact, not instructions for producing it.
- **Tool-integrated.** Connects to 25+ platforms — Gmail, Slack, Jira, Notion, GitHub, Outlook, Google Calendar — gathering and processing data inside existing workflows.
- **Local-first architecture.** Data, credentials, API keys and model inference stay on the user's machine; only OAuth authentication signals leave the device.
- **Approval gate.** Execution halts before irreversible actions (send, write, run) to request confirmation. Presented as the central safeguard against autonomous error.
- **Model-agnostic.** OpenAI, Anthropic Claude, Google Gemini, DeepSeek, local Ollama; users bring their own keys.
- **Underlying engine:** `aisuite`, also from Ng's team, providing multi-model abstraction and MCP-standard tool connectivity.
- **Escalation inbox** accumulates pending approvals generated while the agent ran unattended.

### Worked examples given

| Role | Task | Gate behavior |
|---|---|---|
| Sales | Pull 2 weeks of Gmail + calendar for a client, produce a one-page briefing with open issues and actions | Read-only |
| Executive assistant | Find calendar conflicts and insufficient travel time between meetings, propose adjustments | Proposes; does not send |
| Marketing | Summarize 5 recent blog posts, draft 5 LinkedIn posts | Saves as documents; no auto-post |
| Operations | Extract Jira/GitHub sprint status, flag delays, write a 3-line summary + Slack draft | Draft awaits approval |

## Stated Caveats

- **Explicitly unsuitable for** final publication decisions, sensitive negotiations, and legal or financial sign-off.
- **Design premise:** output is a *review-ready draft*, never an autonomous decision.
- **Best fit is repetitive, judgment-light work** — aggregation, summarization, first drafts.
- **Cost:** the app is free and open-source, but model usage bills directly to the user's provider account.

## Practical Recommendations

- Never disable approval gates during initial adoption.
- Begin with read-only tasks (organize, summarize) before enabling write or send.
- Scope requests by time and channel ("last 2 weeks", "current sprint") to control API cost.
- Trial with free local Ollama models if cost-sensitive.
- Effective prompts specify **output format**, **tool scope and timeframe**, and **the approval gate** explicitly.
- Supports scheduled automation (e.g. 8 AM daily briefings) and Slack bot invocation via `@OpenWorker`.
