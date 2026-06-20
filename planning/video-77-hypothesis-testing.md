# Video 77: Hypothesis Testing
## Probability & Statistics — Video 11 of 12

**Predecessor:** Video 76 (Estimation and Confidence Intervals)
**Next:** Video 78 (Regression — playlist finale)

### Competitive Analysis

**Competitor landscape:**
- 3Blue1Brown: NO dedicated hypothesis testing video. Massive gap for polished animated coverage.
- jbstatistics: Multi-part whiteboard series (1M+ combined views), ~30 min each. Traditional ordering: H0/H1 -> test statistic -> rejection regions -> p-values -> Type I/II errors. Thorough but dry, no animation.
- StatQuest (~280K views): ~10 min, introduces p-values before rejection regions. Accessible but shallow on math, no sampling distribution visualization.
- Khan Academy / Dr. Nic: Basic 2D animations covering H0/H1 and p-values. Skip Type I/II errors entirely.

**Common structure:** All follow H0/H1 -> test statistic -> rejection/p-value -> Type I/II errors. Nobody connects back to confidence intervals or CLT visually.

**Key gaps to differentiate:**
1. Connect hypothesis testing to confidence intervals (natural bridge from Video 76)
2. Animate rejection regions forming on the sampling distribution under H0 (nobody does this visually)
3. Animated power curve (Type I/II errors are always static 2x2 tables)
4. Show WHY the test statistic takes its specific form (CLT from Video 75)
5. Philosophical motivation: why is H0 the default? (almost never addressed)

### Key Differentiators
1. CI -> hypothesis test bridge as direct continuation of Video 76
2. Animated rejection regions forming on sampling distribution under H0
3. Visual test statistic placement on the distribution
4. Animated p-value calculation (shaded area)
5. Type I/II error visual: power curve, not just 2x2 table
6. Connection between CI and hypothesis test (duality theorem)
7. Color coding: null hypothesis = PRIMARY, alternative = SECONDARY, rejection = RED, test statistic = ACCENT

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Null Hypothesis (H0) | PRIMARY | #5BC0EB |
| Alternative Hypothesis (H1) | SECONDARY | #7BC950 |
| Rejection Region / Error | RED | #EF476F |
| Test Statistic | ACCENT | #FFD166 |
| Population Parameters | ACCENT | #FFD166 |
| Sample Statistics | PRIMARY | #5BC0EB |

### Structure (15 minutes)

**Scene 1 — Hook + CI Recap (1:30)**
- Quick recap: CI gives a range of plausible values for mu
- Key formula: x-bar +/- z* * sigma/sqrt(n)
- Motivation: "What if someone claims mu = 20? How do we evaluate that claim?"
- Tease: "We learned how to estimate mu. Now we learn how to test claims about mu."
- Content budget: 3 recap items + motivation question

**Scene 2 — The Framework: H0 and H1 (1:30)**
- Null hypothesis H0: the default assumption (status quo)
- Alternative hypothesis H1: what we're trying to find evidence for
- Key insight: we assume H0 is true and look for evidence against it
- "The burden of proof is on the challenger"
- Notation: H0: mu = mu0 vs H1: mu != mu0 (two-sided)
- Also mention one-sided: H1: mu > mu0 or H1: mu < mu0
- Content budget: 4 items + example

**Scene 3 — The Test Statistic (2:00)**
- If H0 is true (mu = mu0), CLT tells us x-bar ~ N(mu0, sigma^2/n)
- Standardize: z = (x-bar - mu0) / (sigma/sqrt(n))
- Under H0, z ~ N(0, 1)
- The test statistic measures how many standard errors our sample is from the null value
- Connection to CLT (Video 75): this is just the CLT applied under H0
- Visual: sampling distribution under H0 with x-bar and test statistic marked
- Content budget: 3 items + formula + visual

**Scene 4 — Rejection Regions and Significance Level (2:00)**
- If H0 is true, z should be close to 0
- If z is very far from 0, that's evidence against H0
- Significance level alpha: probability of rejecting H0 when it's true
- Common choice: alpha = 0.05
- Rejection region: |z| > z* where z* = 1.96 for alpha = 0.05
- Visual: bell curve with rejection regions shaded in RED, acceptance region in SECONDARY
- Content budget: 3 items + alpha values + visual

**Scene 5 — The p-Value (2:00)**
- Definition: probability of observing a test statistic as extreme as ours, assuming H0
- p-value = P(|Z| >= |z_obs|) under H0
- Small p-value = strong evidence against H0
- Decision rule: reject H0 if p < alpha
- Visual: animated p-value calculation on the distribution
- Content budget: 3 items + visual + decision rule

**Scene 6 — Worked Example (2:00)**
- Problem: Factory claims light bulbs last 1000 hrs. Consumer group tests n=40, x-bar=985, sigma=50. At alpha=0.05, is the claim supported?
- Step by step: H0: mu=1000, H1: mu!=1000
- Test statistic: z = (985-1000)/(50/sqrt(40)) = -1.90
- Rejection: |z| = 1.90 < 1.96, so do NOT reject H0
- p-value: P(|Z| >= 1.90) = 0.057 > 0.05
- "Not enough evidence to reject the claim"
- Content budget: 4 calculation steps + conclusion

**Scene 7 — Type I and Type II Errors (1:30)**
- Two types of errors possible:
  - Type I: Reject H0 when it's true (false positive) — probability = alpha
  - Type II: Fail to reject H0 when it's false (false negative) — probability = beta
- Visual: 2x2 truth table animated
- Power = 1 - beta: probability of correctly rejecting a false H0
- Content budget: 4 items + table

**Scene 8 — CI and Hypothesis Tests: The Duality (1:00)**
- A 95% CI and a two-sided test at alpha=0.05 give the same conclusion
- If mu0 is INSIDE the CI, we do NOT reject H0
- If mu0 is OUTSIDE the CI, we DO reject H0
- Visual: CI bar with mu0 marked
- Content budget: 3 items + visual

**Scene 9 — Summary + Preview (1:30)**
- Key ideas recap: H0/H1 framework, test statistic, rejection/p-value, errors
- CI-test duality
- "Next: Regression — bringing it all together with data"
- Content budget: 3 recap items + next video tease
