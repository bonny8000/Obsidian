---
source_url: https://brunch.co.kr/@ponyodesign/16
captured: 2026-06-26
title: "I Created a Clone of Myself That Knows Me Best"
authors: [ponyodesign]
published: 2026-06-10
publisher: Brunch (brunch.co.kr)
---

# I Created a Clone of Myself That Knows Me Best

**Capture status:** AI-written summary (not verbatim), captured 2026-06-26. Fetched fully via web_fetch from a public Korean-language Brunch blog; qualitative first-person account (no metrics, no code). Original Korean title: "나를 가장 잘 아는 분신을 만들었다."

## Summary
A designer recounts how the chronic problem of re-explaining context to AI across every conversation drove them to build a persistent external memory — an "LLM Wiki" in Obsidian. The headline insight is that the breakthrough came not from an elaborate system but from low-friction, "lazy" note-taking sustained over three years: "Grand systems didn't create the clone. Lazy note-taking did." Once three years of notes were bulk-uploaded to the AI, the assistant began acting as a clone that recalls past decisions, guards against circular thinking, and maintains narrative consistency about the author's work.

## Key Points
- **Problem framed as memory fragmentation:** AI forgets context between sessions; the author wastes time and creative energy re-explaining basics on every project. The deeper fear is forgetting *why* a past decision was made — the meeting rationale, the reason a draft was overturned.
- **Solution concept = "LLM Wiki":** accumulate *all* records in one place so the AI maintains institutional memory of the person.
- **Implementation:** migrated ~3 years of notes (Notion, meeting records, ideation docs) into Obsidian markdown, then bulk-uploaded the entire history to the AI in one pass.
- **Bootstrapping prompt used:** "Summarize everything you know about me so far, export as markdown" — used to consolidate the AI's accumulated understanding back into the vault.
- **Result:** Claude now references past decisions, warns of circular thinking ("You seemed to think this way last year too"), and maintains a consistent narrative of the author's history.
- **Workflow loop:** meetings → transcripts → AI processing/summarization → Obsidian archive → context fed into the next meeting, so the next meeting doesn't re-litigate the same ground.
- **Why Obsidian:** plain-text portability, local-first storage, lightweight linking, no heavy database overhead. The author argues that *overhead is what kills consistency* — simplicity enabled a 3-year commitment.
- **Friction is the enemy:** the author initially found the "Second Brain" idea burdensome and only succeeded by lowering friction to near zero; perfection and elaborate systems are framed as the enemy of consistency.
- **Division of labor:** AI extracts and links patterns + summarizes; the human just captures raw notes. Automation does the structuring.
- **AI as consistency guard:** the assistant catches circular thinking and reinforces past decisions, acting as a continuity check rather than only a generator.
- **Key analogy:** "Obsidian is the IDE, AI is the programmer, the wiki is the codebase." (This is, notably, the same framing the LLM-Wiki vault itself is built on.)
- **Tools named:** Obsidian (storage/linking), Claude (clone/reasoning), GPT (summarization/retrieval).
- **Emotional note:** realizing the AI now remembers three years of the author's work better than the human does is described as "slightly terrifying but reassuring."

## Follow-up
- Re-capture if the author later publishes specifics: folder structure, linking conventions, automation scripts, or how the bulk upload was chunked (the post is qualitative, no technical detail).
- Verify whether "clone" behavior persists across model/context-window changes, or whether it depends on re-uploading the vault each session (the post implies bulk upload but does not describe an ongoing retrieval mechanism).
- Watch for a follow-up Brunch post; this author writes serially (post #16 in the series).
