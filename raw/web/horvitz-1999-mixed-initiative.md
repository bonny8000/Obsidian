# Raw Capture: Horvitz (1999) Principles of Mixed-Initiative User Interfaces

- Captured: 2026-06-12
- Capture type: structured notes from ACM DL abstract page and secondary literature (full PDF behind ACM paywall)
- URL: https://dl.acm.org/doi/10.1145/302979.303030
- DOI: 10.1145/302979.303030
- Citation: Horvitz, E. (1999). Principles of Mixed-Initiative User Interfaces. CHI '99, 159-166.

## Capture Notes (paraphrased, not verbatim)

Positioned against the late-90s debate between direct manipulation (Shneiderman) and autonomous interface agents (Maes): argues the productive path is coupling automated services with direct manipulation rather than choosing one. Demonstrated through the Lookout system for calendar/scheduling from email.

Principles as described in the paper and secondary literature (paraphrased):
- Provide automated service only when it adds genuine value over the user acting directly.
- Reason about uncertainty in the user's goals before acting; act under a decision-theoretic expected-utility frame that weighs the cost of action, inaction, and interruption.
- Consider the user's attention as a cost: timing of agent initiative should account for the status of the user's focus.
- Support dialog to resolve uncertainty instead of guessing when confidence is low; degrade gracefully toward asking or doing nothing.
- Allow efficient invocation and termination of the automated service; keep the user able to take direct control at any time.
- Support an ongoing memory of recent interactions and learn from the user over time.
- Make agent behavior socially appropriate and its intentions legible.

Key transferable idea: agent initiative is a decision-theoretic problem — expected value of action vs. cost of interruption — not a binary autonomy setting. Heavily cited in current proactive-agent work (e.g., arXiv 2501.00383 Proactive Conversational Agents).
