# Video 158: L^p Spaces — Plan

**Playlist:** Measure Theory (Video 9 of 12)
**Script:** `scripts/graduate/video-158-lp-spaces.py`
**Class:** `Video158_LpSpaces`
**Est. Duration:** 12-15 minutes

## Competitive Analysis Summary

### Key Competitors
1. **The Bright Side of Mathematics** — "Multidimensional Integration 16 | Lᵖ-Spaces" (580 views, Jul 30 2026)
   - Lecture-style with proofs; solid yellow/dark backgrounds; covers Lᵖ definition, Hölder, Minkowski
   - Structure: 7/10, Pacing: 6/10 (definition-heavy), Visuals: 5/10 (static graphs), Narration: 7/10, Hooks: 5/10
   - Thumbnail: Black BG, yellow title, mathematical notation in white/orange — clear but lecture-style

2. **Problemathic** — "Integrating any function and defining L1 spaces | Properties" (649 views)
   - Focus on L¹ space specifically, chalk-aesthetic, proof-oriented
   - Structure: 6/10, Pacing: 5/10 (dense), Visuals: 6/10, Narration: 6/10, Hooks: 4/10

3. **3Blue1Brown** — Style reference (no Lᵖ video)
   - Benchmark for intuition-first, visual storytelling approach

### Market Gap
No high-production Manim-animated video exists that visually explains Lᵖ spaces with intuition-first approach. All competitors use lecture-style formats. We can differentiate by:
- Animating the p-norm as a "distance" concept with geometric intuition
- Visualizing how different p values change the "shape" of the unit ball
- Progressive build-up from L¹ → L² → Lᵖ with color-coded examples
- Interactive-feeling progressive disclosure of Hölder/Minkowski proofs

### Techniques to Adopt
1. **From TBSOM:** Comprehensive coverage of definition, Hölder's inequality, Minkowski's inequality, completeness
2. **From 3B1B:** Start with geometric motivation (unit circles in different Lᵖ norms), high-contrast visuals
3. **From Problemathic:** Connect Lᵖ to integration (our advantage — we just covered Lebesgue integral in videos 151-157)

### Techniques to Avoid
1. Definition-first without motivation (TBSOM's approach)
2. Static visuals without animation
3. Treating Lᵖ spaces in isolation — we should connect to everything learned so far

## Scenes

### Scene 1: Hook — Measuring "Size" (45s)
**Content budget (≤5 items):**
- Title: "How do we measure the 'size' of a function?"
- Three text items: L¹ = "area under curve", L² = "energy", Lᵖ = "generalization"
- Hook question: "What makes a function 'small enough' to integrate?"

**Narration:** In calculus, we measure a function's size by its integral. But what if the integral diverges? We need a way to classify functions by how fast they grow. Lᵖ spaces give us precisely this framework.

### Scene 2: From L¹ to L² — Building Intuition (60s)
**Content budget (≤5 items):**
- Section divider: "2 | From L¹ to L²"
- L¹ formula: ‖f‖₁ = ∫|f|
- L² formula: ‖f‖₂ = (∫|f|²)^{1/2}
- Interpretation: "L¹ measures area, L² measures energy"
- Bridge question: "Can we generalize to any p?"

**Narration:** We already know L¹ — it's the Lebesgue integral. L² appears everywhere in physics and signal processing. Both are special cases of Lᵖ spaces.

### Scene 3: The Lᵖ Norm — Definition (60s)
**Content budget (≤5 items):**
- Section divider: "3 | The Lᵖ Norm"
- Definition box: ‖f‖_p = (∫|f|^p dμ)^{1/p} for 1 ≤ p < ∞
- Three conditions: f measurable, ∫|f|^p < ∞, 1 ≤ p ≤ ∞
- L^∞ case: ‖f‖_∞ = ess sup|f|

**Narration:** For a measurable function f and a parameter p between 1 and infinity, we define the Lᵖ norm. The function f belongs to Lᵖ if this norm is finite.

### Scene 4: Key Examples (75s)
**Content budget (≤5 items):**
- Section divider: "4 | Examples"
- Example 1: f(x) = x^{-1/3} on (0,1) — in L¹? L²? Lᵖ for p < 3?
- Example 2: f(x) = e^{-x} on [0,∞) — in all Lᵖ
- Visualization: power function graph showing where integral converges

**Narration:** Let's see concrete examples. A function like x to the minus one-third lives in Lᵖ only when p is less than three. This shows how different Lᵖ spaces capture different decay properties.

### Scene 5: Hölder's Inequality (75s)
**Content budget (≤5 items):**
- Section divider: "5 | Hölder's Inequality"
- Statement: ‖fg‖₁ ≤ ‖f‖_p · ‖g‖_q where 1/p + 1/q = 1
- Visual: two functions multiplying, areas
- Special case: p=q=2 → Cauchy-Schwarz

**Narration:** Hölder's inequality is the engine behind Lᵖ spaces. It says the product of an Lᵖ function and an Lᵠ function is always integrable, when p and q are conjugate.

### Scene 6: Minkowski's Inequality (60s)
**Content budget (≤5 items):**
- Section divider: "6 | Minkowski's Inequality"
- Statement: ‖f+g‖_p ≤ ‖f‖_p + ‖g‖_p (triangle inequality)
- Connection: Minkowski proves Lᵖ is a normed space
- Key insight: relies on Hölder's inequality

**Narration:** Minkowski's inequality is the triangle inequality for Lᵖ. This is what makes Lᵖ a genuine normed space — a result that depends crucially on Hölder's inequality.

### Scene 7: Lᵖ is Complete (Riesz-Fischer) (60s)
**Content budget (≤5 items):**
- Section divider: "7 | Completeness: Riesz-Fischer"
- Statement: Every Cauchy sequence in Lᵖ converges
- Consequence: Lᵖ is a Banach space
- Special highlight: L² is a Hilbert space (inner product!)

**Narration:** A deep result: Lᵖ spaces are complete. Every Cauchy sequence converges to a function still in Lᵖ. This means Lᵖ is a Banach space, and L² — with its inner product — is a Hilbert space.

### Scene 8: The Big Picture + Outro (45s)
**Content budget (≤5 items):**
- Summary diagram: L¹ ⊂ L² ⊂ ... nesting (for finite measure)
- Key takeaways: 3 bullet points
- Connection to convergence theorems (Video 157)
- Outro with next video: Radon-Nikodym Theorem

**Narration:** On finite measure spaces, Lᵖ spaces nest: L^q sits inside L^p when p is larger. Combined with the convergence theorems from our last video, Lᵖ spaces become the natural home for analysis.

## Content Flow
```
Scene 1 (Hook) → Scene 2 (L¹/L² intuition) → Scene 3 (Lᵖ definition)
→ Scene 4 (Examples) → Scene 5 (Hölder) → Scene 6 (Minkowski)
→ Scene 7 (Riesz-Fischer) → Scene 8 (Summary + Outro)
```

## Key Formulas
- ‖f‖_p = (∫|f|^p dμ)^{1/p}
- ‖f‖_∞ = ess sup |f|
- Hölder: ‖fg‖₁ ≤ ‖f‖_p · ‖g‖_q, 1/p + 1/q = 1
- Minkowski: ‖f+g‖_p ≤ ‖f‖_p + ‖g‖_p
