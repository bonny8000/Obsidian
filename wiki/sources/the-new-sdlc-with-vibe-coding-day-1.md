---
type: source
status: active
created: 2026-06-16
updated: 2026-06-16
tags: [vibe-coding, agentic-engineering, sdlc, context-engineering, generative-ai]
source_path: raw/The-New-SDLC-With-Vibe-Coding-Day-1.pdf
authors: [Addy Osmani, Shubham Saboo, Sokratis Kartakis]
---

# The New SDLC With Vibe Coding: From ad-hoc prompting to Agentic Engineering

**Authors:** Addy Osmani, Shubham Saboo, and Sokratis Kartakis
**Date:** May 2026

## Executive Summary
This paper explores the transition from "vibe coding" (casual, natural language prompting) to "agentic engineering" (disciplined implementation using AI agents within human-designed systems). It introduces several key frameworks:
- **The Spectrum from Vibe Coding to Agentic Engineering:** Differentiating by verification, structure, and risk profile.
- **Context Engineering:** The practice of providing AI agents with rich, structured information (Instructions, Knowledge, Memory, Examples, Tools, Guardrails).
- **Static vs. Dynamic Context:** Balancing always-loaded rules (like `AGENTS.md`) with on-demand skill retrieval.
- **The Factory Model:** Shifting the developer's role from writing code to designing the system (the "factory") that produces code.
- **Harness Engineering:** The scaffolding around the AI model (prompts, tools, sandboxes, orchestration) that enables reliable output.
- **Conductors vs. Orchestrators:** Two modes of working—real-time pair programming (Conductor) vs. high-level goal delegation (Orchestrator).

## Key Concepts

### Vibe Coding vs. Agentic Engineering
- **Vibe Coding:** Casual prompts, "does it seem to work?" verification, minimal codebase understanding, high risk for production.
- **Agentic Engineering:** Formal specs, automated test suites, comprehensive review, low risk through systematic verification.

### Context Engineering (The Six Pillars)
1. **Instructions:** Core role and goals.
2. **Knowledge:** RAG, architectural diagrams.
3. **Memory:** Session logs and long-term state.
4. **Examples:** Few-shot patterns.
5. **Tools:** API definitions and scripts.
6. **Guardrails:** Hard constraints and safety rules.

### The Agent Equation
`Agent = Model + Harness`
The harness (scaffolding) is what makes a raw model an effective agent.

---

## Full Content (OCR Transcript)

### Introduction
The most profound shift in software engineering isn't a new language, framework, or cloud service. It's the transition from writing code to expressing intent, and trusting intelligent systems to translate that intent into working software.

For most of computing history, programming has been an act of translation: understand the problem in human terms, design a solution in abstract terms, then render it in syntax a machine can execute. Each step introduces friction. That friction is now collapsing.

As of early 2026, 85% of professional developers regularly use AI Coding Agents, 51% use them daily, and an estimated 41% of all new code is AI-generated.

### The Spectrum: Vibe Coding to Agentic Engineering
The spectrum ranges from casual "vibe coding," where a developer prompts an AI and accepts whatever comes back, to disciplined "agentic engineering," where AI acts as a powerful implementation engine within carefully designed systems of constraints, tests, and feedback loops.

### Context Engineering: The Real Skill
The quality of AI-generated code depends less on the cleverness of your prompts and more on the quality of the context provided.
- **Static Context:** Always loaded (rule files like `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`).
- **Dynamic Context:** Loaded on demand (Agent Skills, RAG).

### The New Software Development Life Cycle
AI compresses the SDLC dramatically, but unevenly. Implementation is hours; requirements and architecture remain human-paced. The developer's role shifts from primary implementor to system designer and quality arbiter.

### The Factory Model
The developer's primary output is not code - it's the system that produces code.
1. Specifications and context
2. Agents
3. Tests and quality gates
4. Feedback loops
5. Guardrails

### Harness Engineering
A raw model is not an agent. It becomes one once a harness gives it state, tool execution, feedback loops, and enforceable constraints. 

### Developer Roles: Conductors and Orchestrators
- **Conductor:** Real-time, synchronous, in-IDE pair programming. Fine-grained control.
- **Orchestrator:** Asynchronous, high-level, multi-agent delegation. Goal-level control.

### The 80% Problem
AI agents generate ~80% of code rapidly, but the remaining 20% (edge cases, error handling) demands deep contextual knowledge that models often lack.

### The Economics of AI Development
- **Vibe Coding:** Low CapEx (minimal investment), High OpEx (Token Burn Rate, Maintenance Tax, Security Remediation).
- **Agentic Engineering:** High CapEx (upfront platform design), Low OpEx (sustainable scale, low marginal cost).

### Conclusion
"Generation is solved. Verification, judgment, and direction are the new craft."
