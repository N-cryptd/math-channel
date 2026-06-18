# Video 73: Common Distributions (Continuous)
## Probability & Statistics — Video 7 of 12

**Predecessor:** Video 72 (Common Distributions — Discrete)
**Next:** Video 74 (Joint Distributions)

### Competitive Analysis
Based on full analysis in `channel-analysis/improvements.md` (section "2026-06-17 — Video 73"):
- 3B1B: Only covers Normal via CLT (7M+ views) — single distribution, no formal PDF definition
- jbstatistics: Recent Normal video (~350K views, 3mo ago), slide-based, 30 min format
- StatQuest: Normal deep-dive (~600K views) + brief overview (~280K), hand-drawn tablet
- KA: Fragmented — each distribution gets separate ~10-15 min video, digital blackboard
- OCT: Separate whiteboard videos per distribution (200K-1M views), no animation
- **GAP: No Manim-animated video covers Normal + Exponential + Uniform systematically**
- **GAP: No family tree / relationships diagram for continuous distributions**

### Key Differentiators
1. Family tree continuity — bridge from Video 72's discrete family tree to continuous distributions
2. Animated smooth PDF curves (not bar charts) for each distribution
3. Color-coded distributions with consistent palette
4. Parameter intuition — show how mu/sigma/lambda reshape curves in real time
5. Side-by-side comparison: all three PDF curves overlaid
6. Real-world scenario for each distribution

### Color Coding
| Distribution | Color | Hex |
|-------------|-------|-----|
| Normal | PRIMARY | #5BC0EB |
| Exponential | SECONDARY | #7BC950 |
| Uniform | ACCENT | #FFD166 |

### Structure (12-15 minutes)

**Scene 1 — Hook (0:45)**
- Bridge from Video 72: "Last time we toured the discrete distributions. Now we move from PMFs to PDFs — continuous random variables."
- Preview the 3 distributions as colored labels with smooth curve icons
- Brief explanation: continuous = uncountable outcomes, PDF instead of PMF
- Content budget: intro animation + 3 distribution names

**Scene 2 — Uniform Distribution (2:00)**
- The simplest continuous distribution: equally likely over an interval [a, b]
- PDF: f(x) = 1/(b-a) for a ≤ x ≤ b, 0 otherwise
- E[X] = (a+b)/2, Var(X) = (b-a)²/12
- Animated: flat rectangle PDF that stretches with a and b
- Real-world: waiting for a bus that arrives uniformly over a 10-minute window
- Color: ACCENT (#FFD166)
- Compare to discrete Bernoulli (simplest discrete) — parallel to Video 72

**Scene 3 — Exponential Distribution (2:30)**
- Models waiting time between Poisson events
- PDF: f(x) = λe^(-λx) for x ≥ 0
- E[X] = 1/λ, Var(X) = 1/λ²
- Animated: decaying curve that stretches/compresses with lambda
- Real-world: time between radioactive decays, time between customer arrivals
- Memoryless property: P(X > s+t | X > s) = P(X > t)
- Color: SECONDARY (#7BC950)
- Bridge from Video 72's Poisson: "Poisson counts events in a fixed interval. Exponential measures the gap between events."

**Scene 4 — Normal Distribution (3:30)**
- The king of all distributions — CLT, natural phenomena
- PDF: f(x) = (1/(σ√(2π))) · e^(-(x-μ)²/(2σ²))
- E[X] = μ, Var(X) = σ²
- Animated: bell curve with mu controlling center, sigma controlling spread
- Show 68-95-99.7 rule visually
- Standardization: Z = (X-μ)/σ → Standard Normal N(0,1)
- Real-world: heights, measurement errors, stock returns
- Color: PRIMARY (#5BC0EB)
- Note: full CLT treatment in a later video, just mention it here

**Scene 5 — Continuous Family Tree (1:30)**
- The KEY differentiator — bridge from Video 72's discrete tree
- Animated diagram showing:
  - Poisson events → Exponential (gap between events)
  - Binomial (n→∞) → Normal (CLT connection)
  - Uniform → simplest continuous (like Bernoulli = simplest discrete)
  - Normal → special case of many distributions (preview)
- Use the same visual style as Video 72's family tree (arrows + labels)

**Scene 6 — Side-by-Side Comparison (1:30)**
- All three PDF curves plotted on the same axes, color-coded
- Highlight the visual differences: flat (Uniform), skewed decay (Exponential), symmetric bell (Normal)
- Quick comparison of support: finite [a,b] vs half-infinite [0,∞) vs infinite (-∞,∞)

**Scene 7 — Quick Reference Table (1:00)**
- Same format as Video 72: Distribution | PDF | E[X] | Var(X) | Support
- Builds row by row
- Summary of when to use each

**Scene 8 — Summary + Outro (0:45)**
- Recap: 3 distributions cover most practical continuous scenarios
- Uniform = simple flat, Exponential = waiting times, Normal = natural phenomena
- Tease next video: Joint distributions and independence in two variables
