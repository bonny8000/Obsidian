# Source Capture: Dummy Variables

URL: https://conjointly.com/kb/dummy-variables/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Dummy Variables

TOC order: 111

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 1544

---

A dummy variable is a numerical variable used in regression analysis to represent subgroups of the sample in your study. In research design, a dummy variable is often used to distinguish different treatment groups. In the simplest case, we would use a `0,1` dummy variable where a person is given a value of `0` if they are in the control group or a `1` if they are in the treated group. Dummy variables are useful because they enable us to use a single regression equation to represent multiple groups. This means that we don’t need to write out separate equation models for each subgroup. The dummy variables act like **‘switches’** that turn various parameters on and off in an equation. Another advantage of a `0,1` dummy-coded variable is that even though it is a nominal-level variable you can treat it statistically like an interval-level variable (if this made no sense to you, you probably should refresh your memory on [levels of measurement](https://conjointly.com/kb/levels-of-measurement/)). For instance, if you take an average of a `0,1` variable, the result is the proportion of `1` s in the distribution.

*where:*

- `y<sub>i</sub>` is outcome score of `i` <sup>th</sup> unit,
- `β<sub>0</sub>` is coefficient for the *intercept*,
- `β<sub>1</sub>` is coefficient for the *slope*,
- `Z<sub>i</sub>` is:
	- `1` if the `i` <sup>th</sup> unit is in the treatment group;
		- `0` if the `i` <sup>th</sup> unit is in the control group;
- `e<sub>i</sub>` is residual for the `i` <sup>th</sup> unit.

To illustrate dummy variables, consider the simple regression model for a posttest-only two-group randomized experiment. This model is essentially the same as [conducting a t-test on the posttest means for two groups or conducting a one-way Analysis of Variance (ANOVA)](https://conjointly.com/kb/posttest-only-analysis/). The key term in the model is `β<sub>1</sub>`, the estimate of the difference between the groups. To see how dummy variables work, we’ll use this simple model to show you how to use them to pull out the separate sub-equations for each subgroup. Then we’ll show how you estimate the difference between the subgroups by subtracting their respective equations. You’ll see that we can pack an enormous amount of information into a single equation using dummy variables. All I want to show you here is that `β<sub>1</sub>` is the difference between the treatment and control groups.

To see this, the first step is to compute what the equation would be for each of our two groups separately. For the control group, `Z = 0`. When we substitute that into the equation, and recognize that by assumption the error term averages to `0`, we find that the predicted value for the control group is `β<sub>0</sub>`, the intercept. Now, to figure out the treatment group line, we substitute the value of `1` for `Z`, again recognizing that by assumption the error term averages to `0`. The equation for the treatment group indicates that the treatment group value is the sum of the two beta values.

![](https://conjointly.com/img/kb/Assets/images/statsim6.gif)

Now, we’re ready to move on to the second step – computing the difference between the groups. How do we determine that? Well, the difference must be the difference between the equations for the two groups that we worked out above. In other word, to find the difference between the groups we just find the difference between the equations for the two groups! It should be obvious from the figure that the difference is `β<sub>1</sub>`. Think about what this means. The difference between the groups is `β<sub>1</sub>`. OK, one more time just for the sheer heck of it. The difference between the groups in this model is `β<sub>1</sub>`!

![](https://conjointly.com/img/kb/Assets/images/statsim7.gif)

Whenever you have a regression model with dummy variables, you can always see how the variables are being used to represent multiple subgroup equations by following the two steps described above:

- create separate equations for each subgroup by substituting the dummy values
- find the difference between groups by finding the difference between their equations

## Coding Dummy Variables for Categorical Variables

> [!primary] Primary
> This subsection was authored by the Conjointly team.

The two-group example above is the simplest dummy variable case, but the same logic generalises to categorical variables with any number of levels. Suppose your treatment factor has `k` levels rather than just two. For example, imagine an experiment with four conditions: a control group and three different treatment groups (call them A, B, and C). How do we represent this in a single regression equation?

The rule is straightforward: **a categorical variable with `k` categories requires `k − 1` dummy variables**. One category is left out and serves as the *reference* (or *baseline*) category. Each of the remaining `k − 1` dummies is a `0,1` indicator that “switches on” only for observations belonging to its own category.

For our four-group example, we pick one group as the reference (let’s choose the control group) and create three dummy variables:

- `Z₁` = `1` if the unit is in treatment A, `0` otherwise
- `Z₂` = `1` if the unit is in treatment B, `0` otherwise
- `Z₃` = `1` if the unit is in treatment C, `0` otherwise

A unit in the control group has `Z₁ = Z₂ = Z₃ = 0`. The regression model becomes:

$$ y\_i = \\beta\_0 + \\beta\_1 Z\_{1i} + \\beta\_2 Z\_{2i} + \\beta\_3 Z\_{3i} + e\_i $$

Following the same two-step procedure from above, we can read off the predicted value for each group by substituting the appropriate dummy values and recognising that the error term averages to `0`:

- **Control** (`Z₁ = Z₂ = Z₃ = 0`): predicted value is `β₀`
- **Treatment A** (`Z₁ = 1`, others `0`): predicted value is `β₀ + β₁`
- **Treatment B** (`Z₂ = 1`, others `0`): predicted value is `β₀ + β₂`
- **Treatment C** (`Z₃ = 1`, others `0`): predicted value is `β₀ + β₃`

So the intercept `β₀` is the predicted value for the reference (control) group, and each slope coefficient `β₁`, `β₂`, `β₃` is the *difference* between the corresponding treatment group and the reference. The difference between any two non-reference groups is found the same way as before, by subtracting their equations: the difference between Treatment A and Treatment B, for instance, is `β₁ − β₂`. This is exactly the same interpretation we had in the two-group case, just extended.

### Why we omit the reference dummy

A natural question is: why not include a dummy for every category, including the control group? It would seem more symmetric to give every group its own indicator. The answer is that doing so breaks the regression.

If we created four dummies, `Z₀, Z₁, Z₂, Z₃`, one for each group, then for every observation in the dataset:

$$ Z\_{0i} + Z\_{1i} + Z\_{2i} + Z\_{3i} = 1 $$

Every unit belongs to exactly one group, so the four dummies always sum to one. But the intercept term in the regression is already a column of ones in the design matrix. This means the four dummy columns add up to the intercept column, so one of them is a perfect linear combination of the others. This problem is known as the **dummy variable trap**, a special case of *perfect multicollinearity*.

When perfect multicollinearity is present, the design matrix `X` is *singular*, the matrix `X'X` cannot be inverted, and the ordinary least squares formula for the coefficients has no unique solution. Statistical software will either refuse to fit the model, drop one of the redundant dummies automatically, or return a warning about rank deficiency. Conceptually, the issue is that the model has no way to tell where the “baseline” ends and the “group effects” begin: you could add any constant to `β₀` and subtract that same constant from each `βⱼ` and get identical predictions, so the coefficients are not uniquely defined.

Omitting one dummy fixes the problem. The omitted category becomes the reference, its mean is captured by the intercept, and every other coefficient is interpreted as a difference relative to it.

A few practical points follow from this:

- **The choice of reference category is arbitrary in terms of model fit.** Predicted values, residuals, and overall `R²` are unaffected by which category you drop. Only the interpretation of the coefficients changes.
- **Choose a reference that aids interpretation.** Common choices include the control group in an experiment, the most common category in observational data, or a meaningful baseline (for example, “no formal education” when modelling education levels).
- **You can include all `k` dummies if you drop the intercept.** This is sometimes called the *cell means* parameterisation. Each coefficient then represents a group mean directly rather than a difference from a reference. The model fit is identical, but the hypotheses tested by the individual `t` -statistics change.

The same `k − 1` rule applies to every categorical predictor you add to the model. If you have two categorical variables, one with three levels and one with four, you would include `2 + 3 = 5` dummies in total, each set with its own reference. Interactions between categorical variables are formed from products of dummies, but the underlying logic of choosing a reference and avoiding the dummy trap stays the same.
