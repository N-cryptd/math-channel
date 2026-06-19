# Video 76: Estimation and Confidence Intervals
## Probability & Statistics — Video 10 of 12

**Predecessor:** Video 75 (Central Limit Theorem)
**Next:** Video 77 (Hypothesis Testing)

### Competitive Analysis
youtubei.js search API returned empty results for "confidence intervals" queries
(possible API regression June 2026). Proceeding with general knowledge of
competitor landscape:
- StatQuest: Has CI videos (~500K-1M views), whiteboard style, practical framing
- Khan Academy: CI videos in stats playlist, traditional lecture style
- 3B1B: No dedicated CI video — major gap/opportunity
- Dr. Trefor Bazett: CI content in statistics playlist
- **GAP 1: No 15-min Manim-animated CI video with visual interval construction**
- **GAP 2: No video connects CLT directly to CI formula derivation visually**
- **GAP 3: No CI video shows animated repeated sampling to build intuition about "95% confident"**
- **GAP 4: No CI video combines derivation + examples + t-distribution in single 15-min video**

### Key Differentiators
1. CLT → CI bridge as a direct continuation (Video 75 → 76)
2. Animated repeated sampling: show 100 confidence intervals, ~95 contain mu
3. Visual construction of the CI formula from CLT step by step
4. Color coding: sample statistics = PRIMARY, population params = ACCENT, interval = SECONDARY
5. Coverage probability visual: animated bars sliding, some missing mu
6. t-distribution introduction for small samples
7. Preview of Video 77 (hypothesis testing)

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Sample Statistics (x-bar, s) | PRIMARY | #5BC0EB |
| Population Parameters (mu, sigma) | ACCENT | #FFD166 |
| Confidence Interval Range | SECONDARY | #7BC950 |
| Warning / Caveat | RED | #EF476F |
| Critical Value (z, t) | PRIMARY | #5BC0EB |

### Structure (15 minutes)

**Scene 1 — Hook + CLT Recap (1:30)**
- Quick recap: CLT says sample mean is approximately normal
- Key formula from Video 75: X-bar ~ N(mu, sigma^2/n)
- Motivation: "We know the distribution — now how do we use it?"
- Tease: "If we observe x-bar = 3.2, what can we say about mu?"
- Content budget: 3 recap items + motivation question

**Scene 2 — Point Estimation (1:30)**
- Natural estimator of mu: x-bar (the sample mean)
- Properties: unbiased (E[x-bar] = mu), consistent (variance → 0)
- But: a single number gives no sense of uncertainty!
- Motivation for intervals: "Wouldn't it be better to give a range?"
- Content budget: 3 items + interval motivation

**Scene 3 — Deriving the Confidence Interval (3:00)**
- Start from CLT: P(-z < (x-bar - mu)/(sigma/sqrt(n)) < z) = 0.95
- Rearrange algebraically to isolate mu:
  P(x-bar - z*sigma/sqrt(n) < mu < x-bar + z*sigma/sqrt(n)) = 0.95
- Identify: margin of error = z * sigma / sqrt(n)
- CI formula: (x-bar - z*sigma/sqrt(n), x-bar + z*sigma/sqrt(n))
- Step-by-step algebraic rearrangement (3 formula transformations)
- Content budget: 3 formula stages + final formula box

**Scene 4 — What Does "95% Confident" Mean? (2:30)**
- Common misconception: NOT "95% probability mu is in this interval"
- Correct interpretation: "95% of intervals constructed this way contain mu"
- Visual: 100 simulated CIs, ~95 green (contain mu) and ~5 red (miss)
- mu is fixed — it's the intervals that vary across samples
- Content budget: misconception text + correct interpretation + simulated intervals visual

**Scene 5 — Choosing the Confidence Level (1:30)**
- 90%, 95%, 99% — trade-off: wider interval = more confidence
- z* values: 1.645 (90%), 1.96 (95%), 2.576 (99%)
- Visual: three intervals side by side, widths increasing
- Content budget: 3 levels with z* values + visual comparison

**Scene 6 — Worked Example (2:00)**
- Problem: Sample of n=50, x-bar=24.8, known sigma=6.2. Find 95% CI.
- Step by step: z* = 1.96, ME = 1.96 * 6.2/sqrt(50) = 1.72
- CI: (24.8 - 1.72, 24.8 + 1.72) = (23.08, 26.52)
- Interpretation sentence: "We are 95% confident that mu is between 23.08 and 26.52"
- Content budget: 4 calculation steps + final interval + interpretation

**Scene 7 — The t-Distribution (2:00)**
- When sigma is unknown (almost always!), use s instead
- Introduce t-distribution: wider tails than normal for small n
- t_{n-1} distribution: depends on degrees of freedom (n-1)
- As n → ∞, t → normal (CLT again!)
- CI formula with t: (x-bar ± t* * s / sqrt(n))
- Visual: normal vs t-distribution overlay
- Content budget: motivation + t-formula + normal-vs-t visual

**Scene 8 — Summary + Preview of Hypothesis Testing (1:30)**
- Key ideas recap: point estimates → intervals → confidence level
- CI formula (z and t versions)
- Common z* values reference
- "Next: we'll test whether a specific value of mu is plausible — hypothesis testing!"
- Content budget: 3 recap items + next video tease
