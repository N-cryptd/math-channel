# Video 72: Common Distributions (Discrete)
## Probability & Statistics — Video 6 of 12

**Predecessor:** Video 71 (Expectation and Variance)
**Next:** Video 73 (Common Distributions — Continuous)

### Competitive Analysis
Based on full analysis in `channel-analysis/improvements.md` (section "2026-06-17 — Video 72"):
- 3B1B: Only covers Binomial (2.58M views) — single distribution, 12+ min
- jbstatistics: Covers each individually (333-599K views each), whiteboard-only
- OCT: Lecture-style, 20-32 min each, no animations
- StatQuest: General overview only (608K views), no specific distributions
- **GAP: No Manim-animated video covers ALL common discrete distributions systematically**
- Combined demand: ~8.2M views across competitor videos

### Key Differentiators
1. Distribution "family tree" — relationships between all distributions (unique visual, NO competitor has this)
2. Animated PMF bar charts for each distribution
3. Color-coded distributions throughout
4. Consistent structure per distribution: scenario → PMF → E[X]/Var(X)

### Color Coding
| Distribution | Color | Hex |
|-------------|-------|-----|
| Bernoulli | PRIMARY | #5BC0EB |
| Binomial | SECONDARY | #7BC950 |
| Geometric | ACCENT | #FFD166 |
| Negative Binomial | RED | #EF476F |
| Hypergeometric | DIM | #6B6B8D |
| Poisson | ORANGE | #FF8C42 |

### Structure (12-15 minutes)

**Scene 1 — Hook (0:45)**
- "You know what random variables are, and how to compute expectation and variance. Now: which specific distributions do we actually USE?"
- Preview the 6 distributions as colored labels
- Content budget: intro animation + 6 distribution names

**Scene 2 — Bernoulli Distribution (1:30)**
- The simplest: one trial, success/failure
- X ∈ {0, 1}, P(X=1) = p
- PMF table: x=0 → (1-p), x=1 → p
- E[X] = p, Var(X) = p(1-p)
- Example: single coin flip
- Animated: a single bar chart (2 bars at x=0 and x=1)
- Color: PRIMARY

**Scene 3 — Binomial Distribution (2:30)**
- n independent Bernoulli trials
- PMF: C(n,k) · p^k · (1-p)^(n-k)
- Animate PMF bars for n=10, p=0.5 (bell shape)
- Show how shape changes with p (p=0.3 skewed, p=0.5 symmetric)
- E[X] = np, Var(X) = np(1-p)
- Example: 10 coin flips, P(exactly 7 heads)
- Color: SECONDARY

**Scene 4 — Geometric Distribution (1:30)**
- Number of trials until FIRST success
- PMF: (1-p)^(k-1) · p
- Exponential decay shape
- E[X] = 1/p, Var(X) = (1-p)/p²
- Example: rolling a die until you get a 6
- Memoryless property mention
- Color: ACCENT

**Scene 5 — Negative Binomial Distribution (1:30)**
- Generalization of Geometric: r successes
- PMF: C(k-1, r-1) · p^r · (1-p)^(k-r)
- E[X] = r/p
- When r=1, reduces to Geometric
- Color: RED

**Scene 6 — Hypergeometric Distribution (1:30)**
- Sampling WITHOUT replacement from finite population
- N total, K successes, n draws, k observed
- PMF: C(K,k) · C(N-K, n-k) / C(N,n)
- Compare to Binomial: with vs without replacement
- Example: drawing cards from a deck
- Color: DIM

**Scene 7 — Poisson Distribution (1:30)**
- Limit of Binomial as n→∞, p→0, λ=np fixed
- PMF: (λ^k · e^(-λ)) / k!
- E[X] = λ, Var(X) = λ (mean equals variance!)
- Approximation rule: n ≥ 20, np ≤ 5
- Example: emails per hour
- Color: ORANGE

**Scene 8 — Distribution Family Tree (1:30)**
- The KEY differentiator visual
- Animated tree diagram showing:
  - Bernoulli → Binomial (n trials)
  - Bernoulli → Geometric (wait for first)
  - Geometric → Negative Binomial (r successes)
  - Binomial → Poisson (n→∞ limit)
  - Binomial ≈ Hypergeometric (with vs without replacement)
- No competitor provides this unified view

**Scene 9 — Quick Reference Table (1:00)**
- Side-by-side table: Distribution | PMF | E[X] | Var(X)
- Builds row by row
- Summary of when to use each

**Scene 10 — Summary + Outro (0:45)**
- Recap: 6 distributions cover most practical discrete scenarios
- Bernoulli is the foundation; Binomial the workhorse; Poisson for rare events
- Tease Video 73: Continuous distributions (Normal, Exponential, Uniform)
