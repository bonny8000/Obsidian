---
source_url: https://theaxlabs.com/blog/claude-code-interview-first
captured: 2026-07-24
title: "PRD를 쓰지 마세요. Claude Code가 당신을 인터뷰하게 하세요"
authors: [AX LABS]
published: 2026-07-23
publisher: AX LABS Blog
language: ko
---

# Don't Write a PRD — Let Claude Code Interview You (AX LABS)

**Original title (ko):** 「PRD를 쓰지 마세요. Claude Code가 당신을 인터뷰하게 하세요」
**Published:** 2026-07-23 · **Captured:** 2026-07-24
**Capture note:** AI-written summary of a Korean-language practical guide. Full text not reproduced.

## Summary

Instead of authoring a long PRD for Claude Code, invert the direction: have the agent **interview you** to extract requirements one question at a time. The economic argument is that the expensive failure is not a long prompt but **code generated in the wrong direction** — so decisions should be settled in cheap conversational turns before any code is produced.

## Key Points

- **The real cost is misdirection.** "The real cost isn't long prompts but code running in the wrong direction." Regenerating wrong output costs far more than the input ever did.
- **Three mechanisms make interviews cheaper:**
  1. Short Q&A turns replace long, expensive code-generation turns.
  2. The user is spared the labor of writing the document.
  3. A good interview surfaces decisions the user had not consciously made.
- **Decision-first principle:** "Finish decisions through inexpensive conversation before code generation."

### The 10 interview prompts, by phase

**Pre-launch — requirements extraction**
- Open with "interview me, don't code," asking one question at a time.
- Offer trade-off options rather than making unilateral choices.
- Read the codebase first and identify conflicts with what exists.
- Probe edge cases systematically.
- Formalize the interview into a PRD with goals / non-goals / requirements / edge cases / completion criteria.

**Execution — holding direction**
- Require approval of the implementation plan before coding starts.
- Ask rather than assume when uncertain.
- Record code preferences in `CLAUDE.md`.

**Post-completion — debugging and iteration**
- Interview before fixing bugs: diagnose first.
- Run retrospective interviews and convert the lessons into `CLAUDE.md` rules.

### Named concepts

- **Happy path vs. edge cases** — separating the basic scenario from failure modes during elicitation.
- **Non-goals** — explicitly stating what will *not* be done, to anchor direction.
- **`CLAUDE.md`** — the project file carrying code preferences and learned patterns between sessions.

## Stated Caveats

**None stated by the author.** The piece assumes access to Claude Code and presents the method as universally applicable — the absence of stated limits is itself worth noting when weighing the advice.

## Practical Recommendations

1. Start every new feature with 「바로 짜지 마. 나를 인터뷰해」 — *don't code yet; interview me.*
2. Embed the principles in `CLAUDE.md` so they persist across sessions.
3. Create slash commands (e.g. `/interview`) for the prompts you reuse.
4. Institutionalize the interview step to scale it across an organization.
