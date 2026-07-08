# Video 109: Pointwise vs Uniform Convergence

**Playlist:** Real Analysis I (Video 11 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video109_PointwiseUniformConvergence
**Script:** scripts/undergraduate/video-109-pointwise-uniform-convergence.py

## Competitive Analysis Reference

Analysis completed 2026-07-08. See `channel-analysis/improvements.md` — section "Pointwise vs Uniform Convergence (Video 109)".

Key competitor insights incorporated:
- Bright Side of Mathematics: x^n canonical example, incremental definition building
- Socratica: epsilon/3 proof clarity
- BriTheMathGuy: "N depends on x" as key pedagogical distinction
- Michael Penn: Dini's theorem inclusion

Our unique advantage: Animated epsilon-tube and dynamic x^n convergence visualization that no competitor provides.

## Prerequisites
- Video 100: Sequences and Convergence
- Video 101: Cauchy Sequences
- Video 103: Continuity (epsilon-delta)
- Video 104: Uniform Continuity (concept of "uniform" — N independent of x)
- Video 105-108: Derivatives, MVT, Integral, FTC

## Learning Objectives
1. Define pointwise convergence of a sequence of functions
2. Define uniform convergence
3. Understand the crucial difference: for uniform, N works for ALL x simultaneously
4. Classic example: f_n(x) = x^n on [0,1] converges pointwise but NOT uniformly
5. Theorem: uniform limit of continuous functions is continuous
6. Theorem: uniform convergence allows interchange of limit and integral
7. Dini's theorem (bonus): monotone + continuous + compact => uniform

## Scene Plan (9 scenes, ~12 min)

### Scene 1: Hook (~60s)
- play_intro
- "A sequence of functions can converge. But HOW it converges matters."
- Animated: sequence of curves approaching a limit — one case smooth, one case with a spike

### Scene 2: Pointwise Convergence (~90s)
- Section: "1 — Pointwise Convergence"
- Definition: f_n → f pointwise if for each x, f_n(x) → f(x)
- "Fix x, then take n → ∞"
- Example: f_n(x) = x^n on [0,1], pointwise limit is 0 for x<1, 1 for x=1

### Scene 3: Uniform Convergence (~90s)
- Section: "2 — Uniform Convergence"
- Definition: f_n → f uniformly if sup|f_n(x) - f(x)| → 0
- Equivalently: for every ε>0, exists N such that for all n≥N and ALL x: |f_n(x)-f(x)|<ε
- "N works for EVERY x simultaneously"
- Key contrast: pointwise fixes x first; uniform controls all x at once

### Scene 4: The Key Example — x^n (~90s)
- Section: "3 — Why Pointwise ≠ Uniform"
- f_n(x) = x^n on [0,1]
- Pointwise limit: f(x) = 0 for x∈[0,1), f(1) = 1
- This limit is NOT continuous! But each f_n is continuous.
- sup|f_n - f| = sup near x=1 = approaches 1 ≠ 0
- So convergence is NOT uniform

### Scene 5: Uniform Limit of Continuous is Continuous (~80s)
- Section: "4 — Why Uniform Matters"
- Theorem: if f_n are continuous and f_n → f uniformly, then f is continuous
- Proof sketch: the "ε/3 argument"
- "Uniform convergence preserves continuity"

### Scene 6: Interchange of Limit and Integral (~70s)
- Section: "5 — Interchange with Integration"
- Theorem: if f_n → f uniformly on [a,b], then ∫f_n → ∫f
- "Uniform convergence lets you pull the limit inside the integral"
- Brief proof: |∫f_n - ∫f| ≤ ∫|f_n - f| ≤ (b-a)·sup|f_n-f| → 0

### Scene 7: Dini's Theorem (~60s)
- Section: "6 — Bonus: Dini's Theorem"
- If f_n continuous, f_n → f pointwise, f_n monotone (increasing or decreasing), and domain compact
- Then convergence is uniform
- "Monotone + continuous + compact upgrades pointwise to uniform"

### Scene 8: Visual Summary (~40s)
- Side-by-side comparison: pointwise (N depends on x) vs uniform (one N for all)

### Scene 9: Summary + Outro (~50s)
- Key takeaways
- play_outro("Series of Functions", "Real Analysis I")
