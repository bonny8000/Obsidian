# The fallacy of depth at scale
### What AI-moderated interviews can and cannot support

**Source:** [saeidehbakhshi.substack.com](https://saeidehbakhshi.substack.com/p/the-fallacy-of-depth-at-scale?triedRedirect=true)
**Date Added:** 2026-06-01

Research methods do not become interchangeable just because AI makes them scalable.

The pitch around AI-moderated research keeps getting louder: qualitative depth at survey scale, interviews by the thousand, thematic synthesis in hours instead of weeks. The argument gets made from both sides, as the future of research or as something to debunk. My position is less dramatic than either. These tools are a new affordance. They do not replace surveys or interviews, because they answer a different part of the problem.

The mistake underneath the discourse is treating methods as points on one line from cheap-and-shallow to rich-and-expensive, with AI moderation as the thing that finally bends the line. Methods are not on one line. Each is built around a different primitive, and that primitive decides which part of a research problem the method can address. Faster, cheaper, and more scalable does not mean better for every question.

## **An Example: The four questions inside “why are users not coming back”**

Lets consider an example product problem. Return rates are softening and the team wants to know why. That reads as one question but depending on what you ask it will call for a different method:

*   **Prevalence:** how many, for which reasons? What share of users cite price, a competitor, poor onboarding, and how does that vary by cohort, tenure, or plan? A counting question. It needs a denominator, so only a survey can answer this well.
*   **Mechanism:** what happened, in what order, and how did it feel? What was the user doing before they stopped, where did it break, when did it stop feeling worth opening? This needs depth, sequence, and observation. This is something you can answer by a human moderated observed interview.
*   **Hypothesis generation:** what reasons did we not think to ask about? Across thousands of people, in their own words, what shows up that was not in the team’s mental model? Open text in a survey answers it, at the level of what users write in one pass.
*   **Discovery at scale:** what sits underneath a stated reason, across many people? A thousand users say “not worth it anymore,” and a moderator asks what changed. AI-moderated interviews answer this partially: follow-up on volunteered language, reaching the verbally accessible part of the mechanism, still missing behavior and the unsaid.

## **The problem with “depth at scale”**

“Depth at scale” sounds plausible because it collapses several properties into one word. Break down what people call richness and it is at least three separate things:

*   **Depth per data point:** how far below the surface reason the method reaches, from a forced choice to a probed exchange to a fully adaptive conversation.
*   **Modality:** which channels it captures, from a checkbox to text to the fuller signal of someone showing you their screen or struggling through a task.
*   **Adaptivity:** whether the instrument changes in response to the person or stays fixed.

Those are the properties the hype talks about. Three more decide whether the output can actually be used as evidence, and the richness framing ignores them:

*   **Structured validity:** whether the output can be read as a measurement, which depends on a fixed instrument applied to a defined sample.
*   **Sample inclusiveness:** who ends up in the data, governed by fluency, cognitive access, motivation, and reachability.
*   **Interpretation control:** where meaning gets made, from a respondent ticking a box to a human coding transcripts to a model summarizing a model, and how auditable that step is.

Separating these is what exposes the substitution problem. AI moderation can raise depth and adaptivity over open text without touching validity, inclusiveness, or interpretation control. More probing produces more language, not a denominator.

## **The four primitives**

Each method is built around a different primitive, and the primitive has pros and cons and affordances. The structure of what each method was built to actually do:

*   **Survey:** a fixed instrument and a denominator. Everyone answers the same items the same way, so counts read as proportions of a known population.
*   **Depth interview:** a human adapting in real time. The instrument changes inside the session, and what the person does is data alongside what they say.
*   **Open text:** volunteered language. Users supply their own words, at a volume large enough to surface reasons no one anticipated.
*   **AI-moderated interview:** probed language at machine scale. Follow-up added to the free-text response, run many times.

### **Survey at scale**

A survey’s job is to count the reasons you already know how to name, not to discover new ones.

*   **Can answer:** prevalence and comparisons. What share cite price, a competitor, or low usage, and how that differs by cohort, plan, and tenure. When the question is how much and among whom, it is the right method, not a cheap stand-in.
*   **Biases:** social desirability, acquiescence, question-order and response-order effects, and recall bias, which flattens the intermittent friction behind gradual disengagement. Upstream of all of these is nonresponse bias: only reachable, willing lapsed users answer, which over-weights the articulate and the aggrieved.
*   **Cannot answer:** mechanism, unanticipated reasons, or anyone who did not respond.

### **Depth interviews**

A depth interview can reconstruct the sequence behind the problem, but cannot size it.

Fifteen lapsed users, an hour each. A good interviewer does not log “too expensive” and move on; they ask what changed, when the product last felt worth opening, what the person was doing the week they stopped. A structure appears that no survey would produce: the price objection surfaced only after a redesign broke a workflow, and the decision to leave was made weeks before the cancellation.

*   **Can answer:** mechanism, sequence, felt experience, and counterfactuals grounded in real episodes.
*   **Biases:** interviewer effects and demand characteristics steer which thread becomes data; articulation bias over-weights people who narrate well; confabulation is real, since people have limited introspective access to the causes of their own behavior, so “why did you stop” can produce a plausible reason rather than the true one.
*   **Cannot answer:** prevalence. Fifteen interviews cannot tell you how large the broken-workflow effect is, and three of fifteen is not a valid measurement of anything.

### **Open text at scale**

Open text can surface reasons you did not think to ask about, but only at the level of what people write in one pass.

Reviews, tickets, feature requests, typed churn reasons. It captures language no survey would have prompted, in users’ own words, across thousands of responses, which a survey cannot do and an interview cannot reach at that scale.

*   **Can answer:** limited discovery. Which reasons exist in users’ own language, including unanticipated ones.
*   **Biases:** item nonresponse on open-ended fields is high and nonrandom, driven by verbal fluency, cognitive access, and motivation, so the corpus over-represents the articulate and engaged. Affect skew compounds it, since people write at emotional extremes and stay quiet when mildly disengaged. At the analysis stage, low intercoder reliability on short fragments makes coding interpretive, and model-based coding does not remove that subjectivity. The interpretive choices move from per-response judgments into the prompt wording and category definitions, where they are applied consistently but are harder to inspect, and the model’s training influences how ambiguous responses get classified.
*   **Cannot answer:** what sits beneath a stated reason, what share of users holds it, or anything from silently disengaged users. Recurrence in the corpus is not prevalence, because the denominator is whoever chose to write and whatever they remembered to mention, not mentioning a reason doesn’t mean that reason was not true for the person.

### **AI-moderated interviews**

AI-moderated interviews are open text (or voice) plus follow-up, which is a real new capability. Where open text or voice response gives one response, the moderator can ask what changed, when it last felt worth it, what the person switched to. That is discovery plus disambiguation on a far larger sample than a human interview study.

But the follow-up is only as good as the participant’s first verbalization, the model’s interpretation of that verbalization, and the probe policy. If the user gives a thin answer, the system has less to work with. If the model interprets the answer too literally, it may follow the wrong thread. If the probing logic rewards fluency, articulate participants get more depth while terse participants produce thinner data. The method adds adaptivity, but the adaptivity is still bounded by language.

It inherits open text’s self-selection and fluency skew, because participants still opt in and answer in language, and the added follow-up introduces failures of its own.

*   **Can answer:** probed stated reasons at scale, deeper than open text, sometimes with higher self-disclosure than a human-facing setting.
*   **Biases:** response-contingent probing, where probe quality depends on what the respondent already gave, so the articulate get sharper follow-ups and the terse get shallow ones or none. A comparison with trained interviewers in a child interview study found the model mostly stopped probing reluctant respondents while professionals continued. There is also verbosity bias, the documented tendency of LLMs to engage more with longer, fluent input, which compounds the fluency skew. The absence of social and physical cues matters too, since the moderator cannot read hesitation or the gap between what a user says and does. Repeated probing can also produce confabulation, where laddering on an introspectively inaccessible reason creates a more fluent invented account rather than the true one. And then there is model-on-model synthesis, where a model summarizes transcripts a model collected, so both stages share a pull toward fluent, central-tendency output with no human reading the raw material.
*   **Cannot answer:** observed behavior, introspectively inaccessible reasons, fair prevalence, or anyone outside the recruitable and articulate population.

## **Why the errors do not average out**

The biases fall into two families:

**Who produces the data:** nonresponse, fluency, cognitive access, motivation, self-selection, reachability. Sample problems.

**What happens to the data:** response bias, interviewer effects, confabulation, coding subjectivity, response-contingent probing, verbosity, model-on-model synthesis. Instrument and interpretation problems.

Volume fixes neither. Sample bias is in the source, so more responses give you more of the same skew. Instrument bias is in how the method treats what it receives, so it holds at any size. Their errors are structural, not statistical, which means you cannot pick a method and count on scale to cover what it misses. A thousand AI-moderated interviews do not create a denominator or make behavior visible; they reproduce the same blind spots at a larger scale.

## **The takeaway**

Running all four methods on every question is not realistic, and chasing one method that does everything is the mistake this whole post is about. The practical move is to pick the method that answers the question you actually care about, and to be clear-eyed about what it cannot tell you.

So start from the question, not the method:

*   If you need to know **how many and among whom**, use a survey, and accept that it will miss the reasons you did not think to ask about.
*   If you need to know **what happened and why**, use depth interviews, and accept that they cannot tell you how common it is.
*   If you need to **discover reasons you have not thought of**, use open text, and accept that it skews toward whoever bothered to write.
*   If you want **probed discovery at scale**, use AI-moderated interviews, and accept that they still miss behavior, the unsaid, and should not be used as measurement.

AI-moderated interviews add one real thing: follow-up to volunteered language, at scale. That is worth having. But it is not a valid way to measure prevalence, not observation, and not a substitute for a person who notices what the participant did not say.
