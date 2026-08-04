---
source_url: https://global.toyota/en/mobility/frontier-research/44665908.html
captured: 2026-08-04
title: "Research on Voice Interaction with Humanoid Robots"
authors: [Kazuya Yamamoto]
published: 2026-07-31
publisher: Toyota Motor Corporation — Frontier Research Center
language: en
format: first-party research interview (corporate publication)
---

# Research on Voice Interaction with Humanoid Robots — Toyota Frontier Research Center

**Author / interviewee:** Kazuya Yamamoto, Social Robotics Group, R-Frontier Department, Frontier Research Center, Toyota Motor Corporation.
**Published:** 2026-07-31 (Frontier Research → Publications) · **Captured:** 2026-08-04
**Contact given:** frc_pr@mail.toyota.co.jp

AI-written extraction, interview format. No full-text reproduction; short quoted phrases only.

---

## Subjects

Two mascot robots, each approximately **90 cm** tall, modelled on real, named people:

- **Tommy** — modelled on **Yuta Tomikawa**, an announcer for Toyota's owned media *Toyota Times*.
- **AI Morizo** — modelled on **Chairman Akio Toyoda**.

Prior generation of mascot robots had **no voice dialogue at all**; communication was emotional expression through full-body movement, driven by remote control plus image recognition. LLMs are given as the reason that changed.

## Pipeline

Speech recognition → response generation via LLM → speech synthesis. Layered on top: camera-based image recognition for situational understanding, and motion output synchronised to speech. The stated goal is *"multifaceted communication that is unique to physical robots."*

## The three named challenges

1. Reproducing the person's likeness.
2. Achieving response quality **and** response speed simultaneously.
3. Non-verbal communication — situational understanding and emotional expression.

---

## Challenge 1 — person-likeness

Likeness is carried in three places: physical appearance, synthesised voice timbre, and the knowledge and thinking process behind responses.

**Voice:** a speech-synthesis model trained on the real person's voice data. Mr. Tomikawa personally recorded training data.

**The key design decision** — Toyota explicitly rejected the obvious approach:

> "While there is a method of training the model extensively on the person's past remarks so it answers identically, our goal is to enable responses that convey the person's distinct character for any question or topic."

Instead: *"we limited the input knowledge to basic profiles, placing emphasis on extracting the underlying philosophies and thought processes from their past remarks to feed into the LLM."*

So: **transcripts are mined for reasoning patterns, not memorised as answers.** The stated reason is coverage — imitating past remarks cannot answer novel questions in character. Yamamoto names the hard part as *"determining what data to input and to what extent."*

## Challenge 2 — the latency budget

**The stated target:** *"for human-like voice dialogue, it is desirable for the response to begin within approximately one second."*

**The stated tension:** every technique that improves response quality increases delay. Named quality techniques and their cost: RAG (defined in-text as retrieving knowledge from a prepared database), web search for current information, and running the LLM multiple times to refine content. *"There is a trade-off where utilizing these methods increases the delay until the final response."*

### Measure 1 — parallel speculative execution

Routing decision: simple greetings answer immediately with no retrieval; current-events questions wait for a web search. But running judgment → search → generation sequentially would itself be too slow. So all three stages **start in parallel** and *"discarding what becomes unnecessary."* Compute is spent to buy latency.

### Measure 2 — prioritised fillers and clarifications

Three response types, ranked:

1. **Main response** (highest priority)
2. **Clarification** — e.g. *"Are you asking about…?"*, generated immediately after speech recognition
3. **Filler** — e.g. *"Um"*, *"Well"*, generated pre-emptively when delay is anticipated

Lower-priority output is emitted **only when the higher-priority response cannot be generated in time.** Yamamoto states the reason for the ranking explicitly: a fixed output order *"becomes monotonous and unnatural."* Because the priority resolution depends on the routing judgment and on LLM latency jitter, the observable output pattern varies naturally — the variation is a by-product of the mechanism, not scripted.

### Measure 3 — "think while listening" (AI Morizo only, newly adopted)

Response generation begins **before the user finishes speaking**. When speech recognition completes, the partially-informed candidate responses are compared against the final recognised text to check whether any would introduce a content discrepancy. Among those with no discrepancy, the system adopts **the one whose generation started earliest**. Anticipatory generation is therefore used as-is where it is still valid.

> "This method can shorten response times without compromising quality."

Savings depend on the input sentence's structure.

**The honest negative result:**

> "Even with these measures, we still cannot get them to consistently respond within one second, and continuous improvement is required."

## Challenge 3 — non-verbal behaviour

Both robots carry cameras. The stack:

- A machine-learning image-recognition model decides *"the person the robot should pay attention to now."*
- A **high-speed VLM** (Vision-Language Model) then analyses that person's appearance and actions for a flexible read of their situation.
- Movements and expressions are selected at high frequency from the combination of image analysis and dialogue content, with fast LLMs doing the selection.

**Stated remaining problems:** accurately deciding who to attend to, what they are doing, and how to map that onto expression and movement. And the expressive vocabulary itself is *"still insufficient"* — the system currently **selects from a few fixed patterns**. The stated ambition is to *generate* movements and expressions rather than select them.

## Deployment history

| When | Where |
| --- | --- |
| From Nov 2024 | Tommy on permanent display at the **Toyota Kaikan Museum**, Toyota City, Aichi — facility information plus open Q&A from visitors |
| Jul 2025 | Tommy, updated to speak English, at **Expo 2025 Osaka, Kansai, Japan** |
| Dec 2025 | Tommy at **World Robot Summit 2025 AICHI** |
| 2025 | AI Morizo at Toyota stakeholder event **"WORLD ARIGATO FEST. 2025"** |

Chairman Akio Toyoda's own reported verdict on AI Morizo: **"The answers sound exactly like me."**

Yamamoto's stated view of public demonstration: having an environment where customers test dialogue and give direct feedback is *"extremely valuable"* — both as team motivation and because the demonstrations are how the remaining challenges were recognised.

## Evidence quality

- **No quantitative results of any kind.** No measured latency figures, no success rates, no user-study data, no comparison against a baseline or an alternative design.
- The only evaluative statements are the one-second target (stated as desirable, and stated as not consistently met) and one named individual's subjective impression.
- First-party corporate publication with no external review.

## Referenced companion articles (by footnote)

1. Interaction research with the partner robot "Keparan" at the National Museum of Emerging Science and Innovation (Miraikan)
2. "Taking Over for Yuta Tomikawa? Tommy Is Growing Fast with AI Technology"
3. "Tommy Shows Off Flawless English! People & Robots Co-exist at Osaka Expo"
4. Frontier Research Center at Expo 2025 Osaka, Kansai — exhibition summary
5. Frontier Research Center's exhibition at World Robot Summit 2025 AICHI
6. "Exclusive: Global Guests Gather in Japan for a Rare Event Showcasing Toyota's Future"

## Figures referenced in the article (captions only)

- Tommy (left) and AI Morizo (right), approx. 90 cm
- AI Morizo engaged in voice dialogue
- Mr. Tomikawa assisting with voice-data recording
- Delay factors in voice dialogue
- Parallel execution pattern for response judgment, search, and response generation
- Generation of fillers, clarifications, and main responses
- "Think while listening" response generation method
- Expressions and movements according to the situation judged by LLMs
