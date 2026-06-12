# Source Capture: Regression Point Displacement

URL: https://conjointly.com/kb/regression-point-displacement-analysis/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Regression Point Displacement Analysis

TOC order: 119

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 358

---

## Regression Point Displacement Analysis

## Statistical Requirements

The notation for the [Regression Point Displacement (RPD) design](https://conjointly.com/kb/quasi-experimental-designs-other/#the-regression-point-displacement-rpd-design) shows that the statistical analysis requires:

- a posttest score
- a pretest score
- a variable to represent the treatment group (where `0` =comparison and `1` =program)
![](https://conjointly.com/img/kb/Assets/images/qoth9.gif)

These requirements are identical to the requirements for the [Analysis of Covariance](https://conjointly.com/kb/analysis-of-covariance/) model. The only difference is that the RPD design only has a single treated group score.

![](https://conjointly.com/img/kb/Assets/images/qoth10.gif)

The figure shows a bivariate (pre-post) distribution for a hypothetical RPD design of a community-based AIDS education program. The new AIDS education program is piloted in one particular county in a state, with the remaining counties acting as controls. The state routinely publishes annual HIV positive rates by county for the entire state. The `x` -values show the HIV-positive rates per 1000 people for the year preceding the program while the y-values show the rates for the year following it. Our goal is to estimate the size of the vertical displacement of the treated unit from the regression line of all of the control units, indicated on the graph by the dashed arrow. The model we’ll use is the Analysis of Covariance (ANCOVA) model stated in regression model form:

where:

- `y<sub>i</sub>` = outcome score for the i <sup>th</sup> unit
- `β<sub>0</sub>` = coefficient for the *intercept*
- `β<sub>1</sub>` = pretest coefficient
- `β<sub>2</sub>` = mean difference for treatment
- `x<sub>i</sub>` = covariate
- `Z<sub>i</sub>` = dummy variable for treatment (`0` = control, `1` = treatment \[`n` = `1`\])
- `e<sub>i</sub>` = residual for the i <sup>th</sup> unit

When we fit the model to our simulated data, we obtain the regression table shown below:

![](https://conjointly.com/img/kb/Assets/images/rpd2.gif)

The coefficient associated with the dichotomous treatment variable is the estimate of the vertical displacement from the line. In this example, the results show that the program lowers HIV positive rates by.019 and that this amount is statistically significant. This displacement is shown in the results graph:

![](https://conjointly.com/img/kb/Assets/images/rpd3.gif)

For more details on the statistical analysis of the RPD design, you can view an entire paper on the subject entitled, “ [The Regression Point Displacement Design for Evaluating Community-Based Pilot Programs and Demonstration Projects](https://billtrochim.net/research/RPD/RPD.pdf) ”.
