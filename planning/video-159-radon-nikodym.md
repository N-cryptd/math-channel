# Video 159: Radon-Nikodym Theorem

**Playlist:** Measure Theory (Video 10 of 12)
**Class:** Video159_RadonNikodym
**File:** scripts/graduate/video-159-radon-nikodym.py
**Estimated duration:** ~550s (9 min)

## Topics
1. Motivation: "derivative" of one measure w.r.t. another
2. Absolute continuity of measures (ν ≪ μ)
3. The Radon-Nikodym theorem (statement)
4. The RN derivative: properties and intuition
5. Concrete example: probability density = RN derivative
6. Lebesgue decomposition theorem (bridge)
7. Applications: change of measure, likelihood ratios
8. Summary and next steps

## Prerequisites
- Videos 151-158 (Measure Theory Intro through L^p Spaces)
- Key: sigma-algebras, measures, Lebesgue integral, convergence theorems

## Competitive Analysis Summary
See channel-analysis/improvements.md for 2026-08-05 entries.
- **Cofiber (10K views):** Motivation-first, density concept, covers RN + Lebesgue decomposition together
- **TBSOM (51K views):** Signed measures → Hahn → Lebesgue → RN pipeline (formal)
- **Our advantage:** Animated visuals for absolute continuity, progressive disclosure, color coding

## Scene Plan

### Scene 1: Hook — The "Derivative" of a Measure (~55s)
**Content budget:** title + 3 items + question
- Motivation: In calculus, df/dx tells us how f changes locally. What about measures?
- If ν(A) = ∫_A f dμ, then f = dν/dμ (the Radon-Nikodym derivative)
- Question: When does such an f always exist?
- Visual: animated equation ν(A) = ∫_A (dν/dμ) dμ

### Scene 2: Absolute Continuity (~65s)
**Content budget:** definition + visual + non-example
- Definition: ν ≪ μ means μ(A) = 0 ⟹ ν(A) = 0
- Intuition: ν "lives on" the same sets as μ; ν can't see sets μ ignores
- Visual metaphor: if μ assigns zero measure, ν must also assign zero
- Non-example warning: not the same as ν ≤ C·μ (that's bounded, different concept)

### Scene 3: The Radon-Nikodym Theorem (~70s)
**Content budget:** hypotheses + theorem statement + formula box
- Setup: (X, Σ, μ) σ-finite, ν ≪ μ, ν is a (signed/finite) measure
- Theorem: There exists a unique (a.e.) measurable f ≥ 0 such that ν(A) = ∫_A f dμ
- Write f = dν/dμ, the Radon-Nikodym derivative
- Uniqueness: if g also works, then f = g μ-a.e.
- Key condition: σ-finiteness is essential

### Scene 4: Properties of the RN Derivative (~60s)
**Content budget:** title + 4 properties
- Linearity: d(αμ + βν)/dλ = α·dμ/dλ + β·dν/dλ
- Chain rule: dρ/dμ = (dρ/dν)·(dν/dμ)
- Inverse: dμ/dν = 1/(dν/dμ)
- Integral: ∫ f dν = ∫ f·(dν/dμ) dμ (change of measure formula)

### Scene 5: Concrete Example — Probability Density (~65s)
**Content budget:** example setup + CDF + PDF connection
- On ℝ with Lebesgue measure λ: P(A) = ∫_A p(x) dx
- Here p = dP/dλ — the probability density is an RN derivative!
- CDF: F(x) = P((-∞, x]) = ∫_{-∞}^x p(t) dt
- This is what we've been using all along without knowing it!

### Scene 6: Lebesgue Decomposition (~55s)
**Content budget:** decomposition statement + 3 parts
- Any ν can be decomposed w.r.t. μ:
  - ν = ν_ac + ν_s (absolutely continuous + singular parts)
  - ν_ac ≪ μ (has RN derivative)
  - ν_s ⊥ μ (supported on μ-null set)
- This is the "big picture" — RN theorem handles the ν_ac part
- Visual: show the two orthogonal components

### Scene 7: Applications (~60s)
**Content budget:** 3 application areas
- Probability: Change of measure (dQ/dP), importance sampling, Girsanov's theorem
- Statistics: Likelihood ratio dP_θ/dP_θ0 = L(θ)/L(θ0)
- Information theory: KL divergence via RN derivative
- Connection: all of these are "RN derivatives in disguise"

### Scene 8: Summary + Outro (~60s)
**Content budget:** 4 takeaways + next video tease
- Key results: absolute continuity, RN theorem, Lebesgue decomposition
- The RN derivative generalizes density functions
- Applications span probability, statistics, information theory
- Next: Product Measures and Fubini's Theorem (Video 160)
- play_outro with next video tease

## Style Notes
- Dark background (BG=#1A1832), channel branding v2
- Progressive disclosure: max 5 elements on screen
- LayoutEngine for ALL positioning
- Formula boxes for main theorems
- Color coding: PRIMARY for definitions, SECONDARY for theorems, ACCENT for examples
- Section dividers between each scene
