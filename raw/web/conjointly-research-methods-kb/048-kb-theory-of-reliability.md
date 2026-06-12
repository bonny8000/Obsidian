# Source Capture: Theory of Reliability

URL: https://conjointly.com/kb/theory-of-reliability/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Theory of Reliability

TOC order: 48

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 1602

---

What is **reliability**? We hear the term used a lot in research contexts, but what does it really mean? If you think about how we use the word “reliable” in everyday language, you might get a hint. For instance, we often speak about a machine as reliable: “I have a reliable car.” Or, news people talk about a “usually reliable source”. In both cases, the word reliable usually means “dependable” or “trustworthy.” In research, the term “reliable” also means dependable in a general sense, but that’s not a precise enough definition. What does it mean to have a dependable measure or observation in a research context? The reason “dependable” is not a good enough description is that it can be confused too easily with the idea of a valid measure (see [Measurement Validity](https://conjointly.com/kb/measurement-validity-types/)). Certainly, when we speak of a dependable measure, we mean one that is both reliable and valid. So we have to be a little more precise when we try to define reliability.

In research, the term reliability means “repeatability” or “consistency”. A measure is considered reliable if it would give us the same result over and over again (assuming that what we are measuring isn’t changing!).

Let’s explore in more detail what it means to say that a measure is “repeatable” or “consistent”. We’ll begin by defining a measure that we’ll arbitrarily label `X`. It might be a person’s score on a math achievement test or a measure of severity of illness. It is the value (numerical or otherwise) that we observe in our study. Now, to see how repeatable or consistent an observation is, we can measure it twice. We’ll use subscripts to indicate the first and second observation of the same measure. If we assume that what we’re measuring doesn’t change between the time of our first and second observation, we can begin to understand how we get at reliability. While we observe a score for what we’re measuring, we usually think of that score as consisting of two parts, the ’true’ score or actual level for the person on that measure, and the ’error’ in measuring it (see [True Score Theory](https://conjointly.com/kb/true-score-theory/)).

![Observed scores with differing error score values](https://conjointly.com/img/kb/Assets/images/reltrue.png)

Observed scores with differing error score values

It’s important to keep in mind that we observe the `X` score – we never actually see the true (`T`) or error (`e`) scores. For instance, a student may get a score of `85` on a math achievement test. That’s the score we observe, an `X` of `85`. But the reality might be that the student is actually better at math than that score indicates. Let’s say the student’s true math ability is `89` (i.e. `T=89`). That means that the error for that student is `-4`. What does this mean? Well, while the student’s true math ability may be `89`, he/she may have had a bad day, may not have had breakfast, may have had an argument, or may have been distracted while taking the test. Factors like these can contribute to errors in measurement that make the student’s observed ability appear lower than their true or actual ability.

OK, back to reliability. If our measure, `X`, is reliable, we should find that if we measure or observe it twice on the same persons that the scores are pretty much the same. But why would they be the same? If you look at the figure you should see that the only thing that the two observations have in common is their true scores, `T`. How do you know that? Because the error scores (`e<sub>1</sub>` and `e<sub>2</sub>`) have different subscripts indicating that they are different values. But the true score symbol `T` is the same for both observations. What does this mean? That the two observed scores, `X<sub>1</sub>` and `X<sub>2</sub>` are related only to the degree that the observations share true score. You should remember that the error score is assumed to be random. Sometimes errors will lead you to perform better on a test than your true ability (e.g. you had a good day guessing!) while other times it will lead you to score worse. But the true score – your true ability on that measure – would be the same on both observations (assuming, of course, that your true ability didn’t change between the two measurement occasions).

With this in mind, we can now define reliability more precisely. Reliability is a **ratio** or fraction. In layperson terms we might define this ratio as:

You might think of reliability as the proportion of “truth” in your measure. Now, we don’t speak of the reliability of a measure for an individual – reliability is a characteristic of a measure that’s taken across individuals. So, to get closer to a more formal definition, let’s restate the definition above in terms of a set of observations. The easiest way to do this is to speak of the variance of the scores. Remember that the variance is a measure of the spread or distribution of a *set* of scores. So, we can now state the definition as:

We might put this into slightly more technical terms by using the abbreviated name for the variance and our variable names:

We’re getting to the critical part now. If you look at the equation above, you should recognize that we can easily determine or calculate the bottom part of the reliability ratio – it’s just the variance of the set of scores we observed (You remember how to calculate the variance, don’t you? It’s just the sum of the squared deviations of the scores from their mean, divided by the number of scores). But how do we calculate the variance of the true scores. We can’t see the true scores (we only see `X`)! Only God knows the true score for a specific observation. And, if we can’t calculate the variance of the true scores, we can’t compute our ratio, which means ***we can’t compute reliability***! Everybody got that? The bottom line is… **we can’t compute reliability because we can’t calculate the variance of the true scores.**

Great. So where does that leave us? If we can’t compute reliability, perhaps the best we can do is to *estimate* it. Maybe we can get an estimate of the variability of the true scores. How do we do that? Remember our two observations, `X<sub>1</sub>` and `X<sub>2</sub>`? We assume (using [true score theory](https://conjointly.com/kb/true-score-theory/)) that these two observations would be related to each other to the degree that they share true scores. So, let’s calculate the correlation between `X<sub>1</sub>` and `X<sub>2</sub>`. Here’s a simple formula for the correlation:

where the `sd` stands for the standard deviation (which is the square root of the variance). If we look carefully at this equation, we can see that the covariance, which simply measures the “shared” variance between measures must be an indicator of the variability of the true scores because the true scores in `X<sub>1</sub>` and `X<sub>2</sub>` are the only thing the two observations share! So, the top part is essentially an estimate of `var(T)` in this context. And, since the bottom part of the equation multiplies the standard deviation of one observation with the standard deviation of the same measure at another time, we would expect that these two values would be the same (it is the same measure we’re taking) and that this is essentially the same thing as squaring the standard deviation for either observation. But, the square of the standard deviation is the same thing as the variance of the measure. So, the bottom part of the equation becomes the variance of the measure (or `var(X)`). If you read this paragraph carefully, you should see that the correlation between two observations of the same measure is an estimate of reliability.

It’s time to reach some conclusions. We know from this discussion that we cannot calculate reliability because we cannot measure the true score component of an observation. But we also know that we can *estimate* the true score component as the covariance between two observations of the same measure. With that in mind, we can estimate the reliability as the correlation between two observations of the same measure. It turns out that there are several ways we can estimate this reliability correlation. These are discussed in [Types of Reliability](https://conjointly.com/kb/types-of-reliability/).

There’s only one other issue I want to address here. How big is an estimate of reliability? To figure this out, let’s go back to the equation given earlier:

and remember that because `X = T + e`, we can substitute in the bottom of the ratio:

With this slight change, we can easily determine the range of a reliability estimate. If a measure is perfectly reliable, there is no error in measurement – everything we observe is true score. Therefore, for a perfectly reliable measure, the equation would reduce to:

Now, if we have a perfectly unreliable measure, there is no true score – the measure is entirely error. In this case, the equation would reduce to:

From this we know that reliability will always range between `0` and `1`. The value of a reliability estimate tells us the proportion of variability in the measure attributable to the true score. A reliability of `.5` means that about half of the variance of the observed score is attributable to truth and half is attributable to error. A reliability of `.8` means the variability is about 80% true ability and 20% error. And so on.
