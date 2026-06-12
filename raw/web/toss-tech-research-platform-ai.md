# Raw: Toss Tech — 휴리봇 이야기 #1

- **URL:** https://toss.tech/article/research-platform-ai
- **Title:** 휴리봇 이야기 #1: 토스는 AI 봇에게 사용자 인터뷰를 한다
- **Author:** Choi Jung-eun (최정은), UX Research Operation Manager, Toss
- **Published:** 2024-12-02
- **Publisher:** Toss Tech Blog
- **Captured:** 2026-05-27

---

## Summary

Toss developed "Huribot," an AI assistant trained on Toss user data to help designers conduct rapid usability checks without the overhead of traditional user testing (UT).

## Core Problem

Scaling user testing was hard. Toss had an established "User Mumul Day" program for on-demand remote testing, but designers faced significant barriers:
- Minimum one-hour preparation time per session
- Psychological hesitation to run small tests
- Inability to test small UI elements efficiently

## Solution: Huribot

Huribot enables designers to conduct quick usability checks by uploading screen images and asking questions — results in seconds, not hours.

## Development Process: Three-Phase Prompting Workflow

**Phase 1 — Pre-Prompting:**
- Narrow the problem (UT scalability)
- Define project goals clearly
- Build team consensus around AI's role as a "check" tool, not a verification tool

**Phase 2 — During Prompting:**
- Validate value early using a lightweight chatbot prototype with actual designers
- Collect feedback and iterate prompts based on real usage patterns

**Phase 3 — Post-Prompting:**
- Define minimum viable product (MVP) features for workflow integration
- Prioritize core functionality: image upload, question input, response generation

## Demonstrated Value

1. **Efficiency:** Designers verify usability with minimal resources
2. **Third-party perspective:** Helps designers gain objective distance from their own work

## Real-World Impact

Designers now use Huribot to detect issues like:
- Misleading graphics
- Dark patterns
- Unclear messaging

…during early design iteration, reserving formal user testing for deeper validation questions.

## Key Claims

- AI-assisted UT is positioned as a "check" tool supplementing, not replacing, formal research
- The three-phase prompting workflow (pre / during / post) is a reusable framework for building AI research tools
- Speed reduction from ~1 hour to seconds for lightweight usability checks
- Huribot was trained on Toss user data (proprietary)
