# Source Capture: Factorial Design Analysis

URL: https://conjointly.com/kb/factorial-design-analysis/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Factorial Design Analysis

TOC order: 114

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 326

---

Here is the regression model statement for a simple [2 x 2 Factorial Design](https://conjointly.com/kb/factorial-designs/). In this design, we have one factor for time in instruction (1 hour/week versus 4 hours/week) and one factor for setting (in-class or pull-out). The model uses a [dummy variable](https://conjointly.com/kb/dummy-variables/) (represented by a `Z`) for each factor. In two-way factorial designs like this, we have two main effects and one interaction. In this model, the main effects are the statistics associated with the beta values that are adjacent to the `Z` -variables. The interaction effect is the statistic associated with `b3` (i.e. the `t` -value for this coefficient) because it is adjacent in the formula to the multiplication of (i.e. interaction of) the dummy-coded `Z` variables for the two factors. Because there are two dummy-coded variables, each having two values, you can write out 2 x 2 = 4 separate equations from this one general model. You might want to see if you can write out the equations for the four cells. Then, look at some of the differences between the groups. You can also write out two equations for each `Z` variable. These equations represent the main effect equations. To see the difference between levels of a factor, subtract the equations from each other. If you’re confused about how to manipulate these equations, check the section on [how dummy variables work](https://conjointly.com/kb/dummy-variables/).

*where:*

- `y<sub>i</sub>` is the outcome of the i <sup>th</sup> unit
- `β<sub>0</sub>` is the coefficient for the *intercept*
- `β<sub>1</sub>` is the mean difference on factor 1
- `β<sub>2</sub>` is the mean difference on factor 2
- `β<sub>3</sub>` is the interaction of factor 1 and factor 2
- `Z<sub>1i</sub>` is the dummy variable for factor 1 (`0` = 1 hour per week, `1` = 4 hours per week)
- `Z<sub>2i</sub>` is the dummy variable for factor 2 (`0` = in class, `1` = pull-out)
- `e<sub>i</sub>` is the residual for the `i` <sup>th</sup> unit
