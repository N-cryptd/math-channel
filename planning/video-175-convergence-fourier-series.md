# Video 175: Convergence of Fourier Series

**Playlist:** Fourier Analysis (Videos 174-183)
**Level:** Graduate (L5)
**Estimated Duration:** 16 min
**Class:** Video175_ConvergenceFourierSeries
**Script:** scripts/graduate/video-175-convergence-fourier-series.py

---

## Competitive Analysis Summary

Key competitor videos:
- 3B1B "But what is the Fourier Transform?" (12.3M views) — winding machine, briefly shows convergence visually but doesn't discuss convergence theorems
- Dr. Peyam "Fourier Series: Pointwise Convergence" (various, ~10-30K views) — whiteboard, theorem-proof style
- Michael Penn "Gibbs Phenomenon" (~20-50K views) — chalkboard, computation-focused
- Steve Brunton Fourier content (20-100K each) — whiteboard, application-driven, mentions convergence qualitatively
- TBSOM "Gibbs Phenomenon" (~35K views) — animated but superficial, doesn't prove Dirichlet conditions

**Market gap:** No animated Manim video covers the convergence theory of Fourier series at graduate level. Every competitor either (a) shows Gibbs visually without explaining the math, or (b) states Dirichlet conditions without visual proof. Nobody combines rigorous convergence theory with high-quality animation. This is a genuine gap — convergence theorems are the bridge between "Fourier series looks good" and "Fourier series IS good."

**Our unique angle:** Build from Video 174's Hilbert space foundation. Convergence is really about different topologies on L2. We show pointwise vs uniform vs L2 convergence as a hierarchy of "how well does S_N(x) approximate f(x)?" with visual demonstrations for each level. The Gibbs phenomenon gets a full deep-dive with the sine integral.

**What to AVOID:** 
- Don't just state theorems without visual motivation
- Don't skip the Dirichlet kernel derivation — it's the engine behind everything
- Don't treat Gibbs as a curiosity — show WHY it happens (sinc function overshoot)

---

## Scene Plan (9 scenes)

### Scene 1: Hook — When Does Approximation Become Reality? (90s)
**Content budget:** Title + 2 questions + answer preview
- Recall Video 174: we built partial sums S_N(x) and watched them approach f(x)
- Key question: "But does S_N(x) actually converge to f(x)? And what does 'converge' even mean for functions?"
- Three levels of convergence teased:
  1. Pointwise: S_N(x) -> f(x) at each x
  2. Uniform: S_N(x) -> f(x) everywhere, at the same rate
  3. L2: S_N -> f in the mean-square sense
- Answer preview: "The answer depends on which kind of convergence you demand, and it depends on properties of f"

### Scene 2: Pointwise Convergence — The Dirichlet Kernel (150s)
**Content budget:** Title + Dirichlet kernel formula + geometric interpretation
- Start from the partial sum: S_N(x) = a0/2 + sum of [a_n cos(nx) + b_n sin(nx)]
- Substitute the Fourier coefficient formulas (integral expressions)
- Algebraic manipulation yields: S_N(x) = (1/pi) * integral from -pi to pi of f(t) * D_N(x-t) dt
- Define the Dirichlet kernel: D_N(u) = 1/2 + sum_{k=1}^{N} cos(ku) = sin((N+1/2)u) / (2 sin(u/2))
- Show both forms — the sum form and the closed form
- Color-code: the sum form in PRIMARY, the closed form in ACCENT
- KEY INSIGHT: S_N(x) is a convolution of f with the Dirichlet kernel
- Visual: emphasize the kernel interpretation

### Scene 3: Dirichlet Conditions — When Pointwise Convergence Holds (150s)
**Content budget:** Title + 3 conditions + theorem statement
- Dirichlet's theorem: If f is:
  1. Piecewise continuous (finite number of jump discontinuities)
  2. Piecewise monotonic (finite number of local extrema per period)
  3. Periodic with period 2pi
- Then S_N(x) -> f(x) at every point of continuity
- At jump discontinuities: S_N(x) -> [f(x+) + f(x-)] / 2 (the midpoint of the jump)
- Color-code: condition 1 in PRIMARY, condition 2 in SECONDARY, condition 3 in ACCENT
- Emphasize: these are SUFFICIENT conditions, not necessary
- Most "nice" functions satisfy them — this covers the vast majority of applications

### Scene 4: Convergence at Discontinuities — The Midpoint Rule (120s)
**Content budget:** Title + visual of jump + midpoint formula
- Visual: show a function with a jump discontinuity
- Show the Fourier partial sums approaching the midpoint at the jump
- Formula: S_N(x_0) -> [f(x_0+) + f(x_0-)] / 2
- This is counterintuitive: the series doesn't converge to the function value at the jump
- It converges to the AVERAGE of the left and right limits
- Physical interpretation: the Fourier series "doesn't know" what value to assign at the jump, so it splits the difference
- Connect to L2 theory: changing f at a single point doesn't change its L2 norm, so L2 convergence doesn't care about point values

### Scene 5: Uniform Convergence — Stronger, Rarer (120s)
**Content budget:** Title + definition + theorem + contrast with pointwise
- Definition: sup_x |S_N(x) - f(x)| -> 0 as N -> infinity
- "Every x converges at the same rate" — the worst-case error goes to zero
- Theorem: S_N -> f uniformly if and only if f is continuous AND f' is piecewise continuous
- Show: this is MUCH stronger than Dirichlet conditions
- The key difference: uniform convergence FAILS at discontinuities
- Functions with jumps (like the square wave) converge pointwise but NOT uniformly
- Visual contrast: two panels — one where convergence is uniform (smooth function), one where it's not (square wave, Gibbs overshoot persists in sup norm)

### Scene 6: L2 Convergence — The Universal Guarantee (120s)
**Content budget:** Title + Parseval statement + theorem
- Definition: ||S_N - f||_2 = 0 (integral of |S_N - f|^2 goes to 0)
- This is convergence in the Hilbert space norm from Video 165
- THEOREM: For EVERY f in L2(-pi, pi), the Fourier partial sums converge to f in L2
- This requires NO smoothness conditions — just square-integrability
- Parseval's identity: ||f||_2^2 = a0^2/2 + sum of (a_n^2 + b_n^2)
- "Energy in the function = energy in the coefficients"
- L2 convergence is the weakest of the three — it allows Gibbs, it allows slow convergence at discontinuities
- But it's UNIVERSAL — it always works for L2 functions
- Connect to Hilbert space: this is the Riesz-Fischer theorem, the reason orthonormal bases work in infinite dimensions

### Scene 7: Gibbs Phenomenon — Deep Dive (180s)
**Content budget:** Title + 3 visual stages + sine integral formula + quantitative result
- Section divider: "The Gibbs Phenomenon"
- Recall the square wave overshoot from Video 174
- Why does it happen? The Dirichlet kernel D_N(u) has a main lobe and side lobes
- Near a jump, the integral picks up a contribution from the first side lobe
- This contribution approaches a definite limit — the Gibbs constant
- Gibbs constant: G = integral from 0 to pi of (sin t / t) dt - pi/2 ≈ 0.08949
- The overshoot as a fraction of the jump height: G * 2/pi ≈ 0.17898 / pi... 
  Actually: overshoot ≈ (2G/pi) * (jump height / 2) = G/pi * jump height
  More precisely: overshoot approaches (jump height)/2 * (Si(pi)/pi - 1/2) where Si is the sine integral
- The overshoot fraction: approximately 8.95% of the jump height on each side
- KEY: As N -> infinity, the overshoot HEIGHT stays constant, but the WIDTH shrinks to zero
- This is why pointwise convergence still holds (except AT the jump) but uniform convergence fails
- Visual: animated partial sums near the jump showing the overshoot narrowing but not shrinking

### Scene 8: Convergence Hierarchy — Putting It All Together (90s)
**Content budget:** Title + hierarchy diagram + comparison table
- Visual hierarchy:
  Uniform convergence (strongest) ⊂ Pointwise convergence ⊂ L2 convergence (weakest, universal)
- Summary table:
  | Type | Requires | Holds for square wave? | Converges at jumps? |
  | Uniform | f continuous, f' piecewise continuous | NO | — |
  | Pointwise | Dirichlet conditions | YES | To midpoint |
  | L2 | f in L2 | YES | N/A (not defined pointwise) |
- Color-code: Uniform in PRIMARY, Pointwise in SECONDARY, L2 in ACCENT
- Key message: "Choose the right convergence for your application"
  - Engineering: L2 convergence (energy), practical because it's always guaranteed
  - PDE theory: uniform convergence (error bounds everywhere)
  - Signal processing: pointwise convergence (reconstructing the signal)

### Scene 9: Summary and Preview (60s)
**Content budget:** 4 key takeaways + outro
- Key takeaways:
  1. Fourier partial sums are convolutions with the Dirichlet kernel
  2. Dirichlet conditions guarantee pointwise convergence (to midpoint at jumps)
  3. Uniform convergence requires smoothness; fails at discontinuities
  4. L2 convergence is universal for all square-integrable functions
  5. Gibbs phenomenon is a fundamental, quantifiable limitation at jumps
- Preview next video: "Fourier Transform — extending from periodic to all functions"
- Channel outro

---

## Visual Design Notes
- **Color coding throughout:**
  - PRIMARY (#5BC0EB) = Dirichlet kernel, pointwise convergence, uniform convergence
  - SECONDARY (#7BC950) = Dirichlet conditions, the function f(x)
  - ACCENT (#FFD166) = L2 convergence, Parseval's theorem, closed-form expressions
  - RED (#EF476F) = Gibbs phenomenon, convergence failures, discontinuities
- **Signature visual:** Three-panel convergence comparison — same function under pointwise, uniform, and L2 norms, with animated partial sums showing different behavior
- **Gibbs deep-dive visual:** Animated Dirichlet kernel showing the side lobes, with a highlighted region near the jump showing how the integral captures the overshoot
- **Hierarchy diagram:** Vertical stack with arrows showing Uniform → Pointwise → L2, color-coded

## Dependencies
- Prerequisites: Video 174 (Introduction to Fourier Series), Video 165 (Hilbert Spaces), Video 164 (Inner Product Spaces)
- Next video: Video 176 — Fourier Transform
