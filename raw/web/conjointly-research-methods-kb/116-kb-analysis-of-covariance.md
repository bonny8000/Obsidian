# Source Capture: Analysis of Covariance

URL: https://conjointly.com/kb/analysis-of-covariance/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Analysis of Covariance

TOC order: 116

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 273

---

I’ve decided to present the statistical model for the [Analysis of Covariance design](https://conjointly.com/kb/covariance-designs/) in regression analysis notation. The model shown here is for a case where there is a single covariate and a treated and control group. We use a [dummy variables](https://conjointly.com/kb/dummy-variables/) in specifying this model. We use the dummy variable `Z<sub>i</sub>` to represent the treatment group. The beta values (`β` s) are the parameters we are estimating. The value `β<sub>0</sub>` represents the intercept. In this model, it is the predicted posttest value for the control group for a given `X` value (and, when `X=0`, it is the intercept for the control group regression line). Why? Because a control group case has a `Z=0` and since the `Z` variable is multiplied with `β<sub>2</sub>`, that whole term would drop out.

The data matrix that is entered into this analysis would consist of three columns and as many rows as you have participants: the posttest data, one column of `0` s or `1` s to indicate which treatment group the participant is in, and the covariate score.

This model assumes that the data in the two groups are well described by straight lines that have the same slope. If this does not appear to be the case, you have to modify the model appropriately.

*where:*

- `y<sub>i</sub>` is the outcome for the `i` <sup>th</sup> unit,
- `β<sub>0</sub>` is coefficient for the intercept,
- `β<sub>1</sub>` is the pretest coefficient,
- `β<sub>2</sub>` is the mean difference for treatment,
- `X<sub>i</sub>` is the covariate,
- `Z<sub>i</sub>` is the dummy variable for treatment:
- `e<sub>i</sub>` is the residual for the `i` <sup>th</sup> unit.
