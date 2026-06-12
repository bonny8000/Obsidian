# Source Capture: Randomized Block Analysis

URL: https://conjointly.com/kb/randomized-block-analysis/

Retrieved: 2026-06-08

Source collection: Conjointly Research Methods Knowledge Base

TOC title: Randomized Block Analysis

TOC order: 115

TOC depth: 2

Author/site: William M.K. Trochim / Conjointly

Published: Not stated

Word count: 330

---

I’ve decided to present the statistical model for the [Randomized Block Design](https://conjointly.com/kb/randomized-block-designs/) in regression analysis notation. Here is the model for a case where there are four blocks or homogeneous subgroups.

*Where:*

- `y<sub>i</sub>` = outcome score for the `i` <sup>th</sup> unit
- `β<sub>0</sub>` = coefficient for the *intercept*
- `β<sub>1</sub>` = mean difference for treatment
- `β<sub>2</sub>` = blocking coefficient for block 2
- `β<sub>3</sub>` = blocking coefficient for block 3
- `β<sub>4</sub>` = blocking coefficient for block 4
- `Z<sub>1i</sub>` = dummy variable for treatment (`0` =control, `1` =treatment)
- `Z<sub>2i</sub>` = `1` if block 2, `0` otherwise
- `Z<sub>3i</sub>` = `1` if block 3, `0` otherwise
- `Z<sub>4i</sub>` = `1` if block 4, `0` otherwise
- `e<sub>i</sub>` = residual for the `i` <sup>th</sup> unit

Notice that we use a number of [dummy variables](https://conjointly.com/kb/dummy-variables/) in specifying this model. We use the dummy variable `Z1` to represent the treatment group. We use the dummy variables `Z<sub>2</sub>`, `Z<sub>3</sub>` and `Z<sub>4</sub>` to indicate blocks 2, 3 and 4 respectively. Analogously, the beta values (`b` ’s) reflect the treatment and blocks 2, 3 and 4. What happened to Block 1 in this model? To see what the equation for the Block 1 comparison group is, fill in your dummy variables and multiply through. In this case, all four `Zs` are equal to 0 and you should see that the intercept (`β<sub>0</sub>`) is the estimate for the Block 1 control group. For the Block 1 treatment group, `Z<sub>1</sub>` = 1 and the estimate is equal to `β<sub>0</sub>` + `β<sub>1</sub>`. By substituting the appropriate dummy variable “switches” you should be able to figure out the equation for any block or treatment group.

The data matrix that is entered into this analysis would consist of five columns and as many rows as you have participants: the posttest data, and one column of 0’s or 1’s for each of the four dummy variables.
