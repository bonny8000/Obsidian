---
source_url: https://guanjie.li/Thinking-out-louder/2026/06/18/what-LLM-can-and-cannot-find.html
captured: 2026-06-22 (verbatim body added 2026-07-20 from fuller capture)
title: "Lost in Translation: What LLM Can and Cannot Find for Product Teams in User Interview Transcripts"
authors: [Guanjie Li]
published: 2026-06-18
publisher: Thinking Out Louder (personal blog)
---

# Lost in Translation: What LLM Can and Cannot Find for Product Teams in User Interview Transcripts

## Which questions work, and why

The figure plots all 23 questions on two axes. The horizontal axis is well-posedness (inverted so that higher means more stable), represented by hue (red dots = unstable criterion, blue dots = stable). The vertical axis is human prior-reading pass rate, represented by lightness (light dots = proxy’s responses diverge from researcher’s reading, dark dots = proxy’s responses aligns). The dots clustering toward the upper right side that appear dark blue are questions the proxy handles well on both counts. Questions that appear red or pale are ones to approach with caution for different reasons.

### What works

The questions that land in the upper right share a common structure. They ask about observable behavior, explicit stance, or factual experience, not what participants felt or should have felt. These are questions with a relatively clear evidentiary standard. Note that a subset of the dark blue cluster (Q13 privacy concerns, Q16 role shift to oversight, Q12 social stigma) have very low base rates: fewer than a quarter of participants from this sample addressed them at all. The proxy handles these generally well by abstaining when the signal isn’t there.

### What doesn’t work, and why it differs

Questions not in the upper right fall short for distinct reasons. A red or purple dot means the grader flip-flops on whether the question is answerable at all, usually because it contains a boundary the rubric can’t resolve without product context. A pale dot means the criterion is stable but the proxy’s content diverges from what my prior reading finds useful. Some questions are both purple and pale: the criterion is unstable, and when an answer does come through, the content diverges too.

*Emotional and affective questions* are hard to transmit to an LLM. Q08 (positive emotions) appears blue but pale: while user satisfaction sounds straightforward and intuitive, what counts as a meaningful, product-relevant expression of it is use-dependent. Finding a value proposition requires knowing when affect crosses into something strong enough to matter; assessing long-term satisfaction might only need cognitive appraisal. Without specifying which, the question is well-posed for the LLM but may not surface what a product team is actually looking for. Q10 (frustration with AI) appears lilac: whether a participant’s negative mentions count as frustration has no stable answer until a threshold is defined. Q09 (performance concerns) took considerable revision to distinguish from adjacent questions, and the proxy had little difficulty surfacing concerns literally present in the transcript. Yet what I was looking for was a real gap between user expectation and LLM capability, at a level of detail that would inform a product decision. The proxy doesn’t have that lens, and its responses diverge from my prior readings accordingly.

*Fine-grained behavioral and process questions* (Q22 follow-up prompting behavior, Q23 post-AI workflow handoff, Q24 communication style preference) range from pale indigo to mauve. The signal for micro-behaviors in Q22 and Q23 is sparse and fragmented in interview text. Q24 compounds the problem: what counts as a “communication style” spans text prompts, file uploads, structured templates, and more. Whether a participant’s offhand mention of any of these counts as a meaningful pattern depends on what kind of friction you’re trying to understand, and different teams would draw that line differently. These questions are often the most valuable to designers precisely because they are hard to ask directly, and for the same reason, they are hard for an LLM to extract reliably from interview text.

*Normative questions* (Q15 tasks humans should do regardless of AI capability, Q18 broader societal concerns) sit on the paler side. They ask what participants believe ought to be the case, and whether a given statement rises to the level of a considered position depends on reading tone and intent. A product team asking these questions may be trying to set guardrails and identify directions to deprioritize, a judgment that requires product context the proxy doesn’t have access to.

Q01 (AI tools used) deserves a separate note because it looks different from the others: the dot is red but not pale. The proxy reads the content and captures what the human prior reading recognizes as AI tools, but there is instability in the criterion itself: Does someone mentioning “an AI assistant” counts as specifying their tool? How about “AI features in Adobe”? Rewording or sharpening the rubric would help, but only up to a point. Any definition of “specific enough” will lag behind what users are actually doing, since the tool landscape changes faster than any rubric can track.

---

## The bottleneck is communication, not LLM capability

Looking across the questions that fall short, a pattern emerges. The questions that work are those where a product team member can transmit their intent to the LLM completely enough. The questions a proxy struggles with tend to be ones where the criterion itself resists articulation: what counts as a meaningful expression of frustration, whether a workflow detail rises to the level of a stated preference.

A user proxy is, at its core, a communication channel: a product team member specifies what they want to know, the proxy extracts it from the transcript, and an LLM or human evaluator checks whether the extraction was faithful. Every step in that chain requires a shared understanding of what counts. Human colleagues build that understanding implicitly from accumulated product exposure, from seeing which signals matter for which decisions, from a shared sense of what an insight looks like before it can be written down. The rubric is the only interface between a human and an LLM, and some things don’t fit through it, because the understanding itself was never fully linguistic to begin with.

This is also why qualitative research can’t be replaced by running interview transcripts through an LLM, regardless of how capable the model becomes. The bottleneck isn’t the model’s ability to read or reason, but the cost of communicating what you are looking for precisely enough that the model can find it. That cost is highest exactly where the research value is highest: in the findings a product team didn’t know to look for until they saw them. A tighter rubric makes the proxy more reliable at finding what you specified; it also makes it less likely to surface what you didn’t. The most valuable qualitative insights tend to be the ones that reframe the question, and those can’t be written into a rubric in advance.

---

## What this means in practice

If you have used an LLM to process user interview transcripts and found the results uneven (useful in some places, frustratingly sloppy in others), the pattern above suggests why. It is not a capability problem. It is a question design problem, and more specifically, a communication problem: the LLM may have found what the question asked for; the question just didn’t ask for what you needed. There are three levers to improve.

The first is **question selection**. The results here reflect one question set, one dataset, and one proxy architecture. Your questions and your product context will shift the picture. But the underlying pattern is likely to hold: observable, factual, explicit questions travel better through the rubric interface. If you are starting out, these are where a proxy will be most consistent and most aligned with what you are looking for. Emotional reactions, process micro-behaviors, and normative positions require substantially more effort to capture reliably, and may not be worth that effort for every research goal.

The second is **question refinement**. If a question is ill-posed but the construct is in principle articulable, sharpening the wording or the rubric boundary will help. Though if the boundary depends on product context, no amount of rewording will fully close the gap. There is also a deeper tradeoff: the tighter the rubric, the more reliably the proxy finds what you specified, and the less likely it is to surface what you didn’t. For questions where unexpected findings are the point, over-specifying the criterion can be counterproductive.

The third is **context provision**: giving the LLM your role, the decisions you are trying to make, what you already know and what kind of signal you are looking for. This is the highest-effort lever and the one with the highest ceiling. It can make questions usable that would otherwise be ill-posed. The catch is that it requires externalizing tribal knowledge you may not realize you have. Much of what makes a product team member’s reading of a transcript valuable is accumulated and implicit; knowing which details matter, for which decisions, is something that develops over time and doesn’t always survive translation into a prompt.

For those building user proxy systems, this reframes where the real work lies. Getting the proxy to extract information from a transcript is the easier half of the problem. The harder half is on the human side: helping product team members communicate what they are looking for clearly enough that the rubric can carry it. That means designing question sets iteratively, stress-testing rubric boundaries against real proxy responses, and building in ways for users to specify context. The proxy is only as good as the question it is answering, and the question is only as good as the intent behind it can be made explicit.

---

## Appendix 1: Why well-posedness is measured through the grader

You might wonder: why not measure answerability directly from the user proxy? Why use the transcript-grounded grader infrastructure, which was designed for a different task?

**Answerability is not a property of the proxy alone.** “Can this question be answered?” only has meaning once you define what counts as an answer. For clear-cut cases (a participant explicitly mentions an observable behavior), answerability is a fact about the transcript and the rubric agrees instantly. For boundary cases (does mentioning “AI features in Adobe” count as specifying AI tools used, or is it too vague?), answerability depends on a normative choice about where to draw the line. That choice lives in the rubric, not in the proxy. Q01 is the clearest example: the proxy consistently reads the transcript in a way aligned with human prior readings; the instability is in whether the rubric classifies that response as addressing the question. No amount of inspecting the proxy would reveal this.

**There is no grader-free shortcut.** One might propose re-running the proxy and comparing responses: if the proxy answers consistently, the question must be answerable. But a proxy can rephrase across runs and still be expressing the same meaning. Determining whether two responses agree on answerability despite differences in wording would itself require applying the rubric, which is exactly what the grader does.

If there is so much struggle with rubric definition, why not have a human judge and rely on an internalized rubric? A human judge faces the same instability the LLM-powered grader does. With genuinely ambiguous boundary cases, a human reading the same transcript twice will not always land the same way. The difference is that the grader’s drift is measurable and human drift is not: there is no practical way to have a human judge the same item multiple times with no memory of prior judgments. The grader is not a substitute for human judgment, but the only instrument that can make the instability visible and quantifiable.

---

## Appendix 2: The well-posedness formula

For each question and interview transcript pair, the grader runs $r$ times and produces a binary judgment on each run: answerable or not. Let $p_b$ be the fraction of runs that called the question answerable for the transcript of participant $b$. The within-participant variance for that question-participant pair is $p_b(1 - p_b)$, which equals zero when the grader is fully consistent and reaches its maximum of 0.25 when the grader is evenly split.

Well-posedness is defined as:

$$
\text{well-posedness} = 1 - \frac{1}{0.25} \cdot \frac{1}{N} \sum_{b=1}^{N} p_b(1 - p_b)
$$

Here, $N = 50$ participants and $r = 9$ times. The denominator 0.25 is the theoretical maximum of a Bernoulli variance (achieved when $p = 0.5$), making the score interpretable as a fraction: 1.0 means the grader was never uncertain about answerability for any participant; 0 means it was at 50/50 for every participant on every run.

### Three caveats

**This is within-participant variance, not total variance.** The formula averages $p_b(1-p_b)$ across participants (the grader’s uncertainty for a given participant’s transcript). It does not use the variance of the mean $p$ across participants, which would mix in between-participant heterogeneity: some participants’ transcripts address a topic, others’ don’t. That between-participant spread reflects base rate, not fuzziness. Q13 (privacy concerns) and Q16 (role shift to oversight) have near-zero well-posedness variance but low base rates, as the grader is perfectly consistent that most transcripts don’t address these topics.

**The raw (uncorrected) variance is used for normalization.** An unbiased variance estimator would multiply by $\frac{r}{r-1}$, but individual values can then exceed 0.25, breaking the $\[0, 1\]$ bound. Since the formula is used for interpretation rather than variance estimation, the raw mean is the right choice. The two versions differ by less than 12% in practice and do not change the ranking.

**Use Figure 1 for direction, not precision.** Each dot represents a question’s mean well-posedness score, and hovering reveals a 90% confidence interval derived from a bootstrap over the 50 interview transcripts. For many questions in the middle of the range, those intervals overlap. Q01 sits clearly at the left (0.64) and a handful of questions sit clearly at the right (1.0), but the questions in between are harder to rank with confidence. Narrowing the confidence intervals would require a larger sample, which is beyond the scope of this post. The figure is a guide to broad groupings, not a precise scorecard.