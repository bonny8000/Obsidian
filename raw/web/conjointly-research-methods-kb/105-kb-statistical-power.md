# Source Capture: Statistical Power

URL: https://conjointly.com/kb/statistical-power/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Statistical Power

TOC order: 105

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 1511

---

There are four interrelated components that influence the conclusions you might reach from a statistical test in a research project. The logic of statistical inference with respect to these components is often difficult to understand and explain. This paper attempts to clarify the four components and describe their interrelationships.

The four components are:

- **sample size** is the number of units (e.g. people) accessible to the study;
- **effect size** is the salience of the treatment relative to the noise in measurement;
- **alpha level** (`α`, or significance level) is the odds that the observed result is due to chance;
- **statistical power** (`1−β`) is the odds that you will observe a treatment effect when it occurs.

Given values for any three of these components, it is possible to compute the value of the fourth. For instance, you might want to determine what a reasonable sample size would be for a study. If you could make reasonable estimates of the effect size, alpha level and power, it would be simple to compute (or, more likely, look up in a table) the sample size.

Some of these components will be more manipulable than others depending on the circumstances of the project. For example, if the project is an evaluation of an educational program or counseling program with a specific number of available consumers, the sample size is set or predetermined. Or, if the drug dosage in a program has to be small due to its potential negative side effects, the effect size may consequently be small. The goal is to achieve a balance of the four components that allows the maximum level of power to detect an effect if one exists, given programmatic, logistical or financial constraints on the other components.

[The Statistical Inference Decision Matrix](#the-statistical-inference-decision-matrix) shows the basic decision matrix involved in a statistical conclusion. All statistical conclusions involve constructing [two mutually exclusive hypotheses](https://conjointly.com/kb/hypotheses-explained/), termed the null (labeled H <sub>0</sub>) and alternative (labeled H <sub>1</sub>) hypothesis. Together, the hypotheses describe all possible outcomes with respect to the inference. The central decision involves determining which hypothesis to accept and which to reject. For instance, in the typical case, the null hypothesis might be:

> **H <sub>0</sub>:** Program Effect = 0

while the alternative might be

> **H <sub>1</sub>:** Program Effect ≠ 0

The null hypothesis is so termed because it usually refers to the “no difference” or “no effect” case. Usually in social research we expect that our treatments and programs will make a difference. So, typically, our theory is described in the alternative hypothesis.

The [table below](#the-statistical-inference-decision-matrix) is a complex figure that you should take some time studying. First, look at the header row (the shaded area). This row depicts reality – whether there really is a program effect, difference, or gain. Of course, the problem is that you never know for sure what is really happening (unless you’re God). Nevertheless, because we have set up mutually exclusive hypotheses, one must be right and one must be wrong. Therefore, consider this the view from God’s position, knowing which hypothesis is correct. The first column of the 2×2 table shows the case where our program does not have an effect; the second column shows where it does have an effect or make a difference.

The left header column describes the world we mortals live in. Regardless of what’s true, we have to make decisions about which of our hypotheses is correct. This header column describes the two decisions we can reach – that our program had no effect (the first row of the 2×2 table) or that it did have an effect (the second row).

Now, let’s examine the cells of the 2×2 table. Each cell shows the Greek symbol for that cell. Notice that the columns sum to `1` (i.e. `α + (1-α) = 1` and `β + (1-β) = 1`). Why can we sum down the columns, but not across the rows? Because if one column is true, the other is irrelevant – if the program has a real effect (the right column) it can’t at the same time not have one. Therefore, the odds or probabilities have to sum to `1` for each column because the two rows in each column describe the only possible decisions (accept or reject the null/alternative) for each possible reality.

Below the Greek symbol is a typical value for that cell. You should especially note the values in the bottom two cells. The value of `α` is typically set at `.05` in the social sciences. A newer, but growing, tradition is to try to achieve a statistical power of at least `.80`. Below the typical values is the name typically given for that cell (in caps). If you haven’t already, you should note that two of the cells describe errors – you reach the wrong conclusion – and in the other two you reach the correct conclusion. Sometimes it’s hard to remember which error is Type I and which is Type II. If you keep in mind that Type I is the same as the a or significance level, it might help you to remember that it is the odds of finding a difference or effect by chance alone. People are more likely to be susceptible to a Type I error, because they almost always want to conclude that their program works. If they find a statistical effect, they tend to advertise it loudly. On the other hand, people probably check more thoroughly for Type II errors because when you find that the program was not demonstrably effective, you immediately start looking for why (in this case, you might hope to show that you had low power and high `β` – that the odds of saying there was no treatment effect even when there was were too high). Following the capitalized common name are several different ways of describing the value of each cell, one in terms of outcomes and one in terms of theory-testing. In italics, we give an example of how to express the numerical value in words.

To better understand the strange relationships between the two columns, think about what happens if you want to increase your power in a study. As you increase power, you increase the chances that you are going to find an effect if it’s there (wind up in the bottom row). But, if you increase the chances that you wind up in the bottom row, you must at the same time be increasing the chances of making a Type I error! Although we can’t sum to `1` across rows, there is clearly a relationship. Since we usually want high power *and* low Type I Error, you should be able to appreciate that we have a built-in tension here.

## The Statistical Inference Decision Matrix

![Statistical Inference Decision Matrix](https://conjointly.com/img/statistical-inference-decision-matrix.svg)

Statistical Inference Decision Matrix

We often talk about alpha (`α`) and beta (`β`) using the language of “higher” and “lower.” For instance, we might talk about the advantages of a higher or lower α-level in a study. You have to be careful about interpreting the meaning of these terms. When we talk about *higher* α-levels, we mean that we are *increasing* the chance of a Type I Error. Therefore, a *lower* α-level actually means that you are conducting a *more rigorous* test. With all of this in mind, let’s consider a few common associations evident in the table. You should convince yourself of the following:

- the lower the `α`, the lower the power; the higher the α, the higher the power.
- the lower the `α`, the less likely it is that you will make a Type I Error (i.e. reject the null when it’s true).
- the lower the `α`, the more “rigorous” the test.
- an `α` of `.01` (compared with `.05` or `.10`) means the researcher is being relatively careful, s/he is only willing to risk being wrong 1 in a 100 times in rejecting the null when it’s true (i.e. saying there’s an effect when there really isn’t).
- an `α` of `.01` (compared with `.05` or `.10`) limits one’s chances of ending up in the bottom row, of concluding that the program has an effect. This means that both your statistical power and the chances of making a Type I Error are lower.
- an `α` of `.01` means you have a `99%` chance of saying there is no difference when there in fact is no difference (being in the upper left box).
- increasing `α` (e.g. from `.01` to `.05` or `.10`) increases the chances of making a Type I Error (i.e. saying there is a difference when there is not), decreases the chances of making a Type II Error (i.e. saying there is no difference when there is) and decreases the rigor of the test.
- increasing `α` (e.g. from `.01` to `.05` or `.10`) increases power because one will be rejecting the null more often (i.e. accepting the alternative) and, consequently, when the alternative is true, there is a greater chance of accepting it (i.e. power).
