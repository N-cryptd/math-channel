# Video 137: Zeros and Poles

**Playlist:** Complex Analysis (Video 14 of 13 — extended)
**Class:** Video137_ZerosAndPoles
**Script:** scripts/undergraduate/video-137-zeros-and-poles.py
**Est. Duration:** 12 min
**Status:** PLAN

## Competitive Analysis Summary

[Analysis based on known competitor content.]

- **3Blue1Brown:** Has NOT produced dedicated videos on zeros/poles or the argument principle. His visual style would suggest: showing zeros as "sources" and poles as "sinks" in a flow field, with winding numbers counting how many times a curve wraps around.
- **Faculty of Khan:** Has videos on the argument principle and Rouché's theorem. Whiteboard style, covers the theorem statements and proof outlines but lacks geometric visualization of winding numbers.
- **Michael Penn:** Has computation videos using the argument principle to count zeros. Rapid-fire algebra.
- **Dr. Peyam:** Lecture-style videos on these topics.
- **BriTheMathGuy / The Bright Side of Mathematics:** Manim-based coverage, clean but fast-paced.

**Market gap:** No video visually explains the Argument Principle by animating the image of a curve under f(z) and showing how many times it winds around the origin — which counts the zeros inside. The connection between zeros of f and poles of 1/f is almost never animated.

**Techniques to adopt:**
- Visualize winding number: animate f(γ(t)) and count revolutions around 0
- Show zeros as "sources" and poles as "sinks" in a phase portrait
- Animate Rouché's theorem: deform one function into another on the boundary, same winding = same number of zeros
- Visual proof that N - P = (1/2πi) ∮ f'(z)/f(z) dz

**Techniques to avoid:**
- Stating the argument principle without showing the winding number intuition
- Dense proof without the geometric picture
- Not connecting zeros to poles (the duality)

## Scene Plan

### Scene 1: Hook — "Counting Zeros by Integrating" (~50s)
- "We know how to evaluate integrals using residues. But integrals can also COUNT things"
- "The Argument Principle lets us count the number of zeros and poles inside a contour — just by evaluating one integral"
- Visual: a contour with several zeros (dots) and a pole (X) inside
- Bridge: "This connects integration to the fundamental structure of analytic functions"

### Scene 2: Zeros of Analytic Functions (~50s)
- Zero of order m: f(z) = (z-a)^m g(z) where g(a) ≠ 0 and g is analytic
- Visual: zero of order 1, 2, 3 — each shown as labeled dots on the complex plane
- Key fact: zeros of a non-zero analytic function are isolated
- "Zeros don't accumulate — analytic functions can't have too many zeros in one place"

### Scene 3: The Argument Principle (~60s)
- Theorem: If f is meromorphic inside and on γ with zeros a₁,...,aₙ (multiplicities mₖ) and poles b₁,...,bₚ (orders nₗ), then:
  (1/2πi) ∮_γ f'(z)/f(z) dz = N - P (number of zeros minus poles, counting multiplicity)
- Key insight: f'(z)/f(z) has simple poles at zeros (residue = order of zero) and poles (residue = -order of pole)
- Visual: show f(γ) winding around origin N-P times
- "The integral of f'/f counts the net number of zeros minus poles"

### Scene 4: Rouché's Theorem (~55s)
- Theorem: If |f(z) - g(z)| < |f(z)| + |g(z)| on γ, then f and g have the same number of zeros inside γ
- Intuition: f never "swallows" g on the boundary, so their winding numbers match
- Example: prove that z⁵ + z + 1 has exactly one root in |z| < 1
  - Take f(z) = z⁵, g(z) = z⁵ + z + 1
  - On |z| = 1: |g(z) - f(z)| = |z + 1| ≤ 2, |f(z)| = 1
  - Better: take f(z) = 1, g(z) = z⁵ + z + 1, then |g - f| = |z⁵ + z| ≤ 2, |f| = 1
  - Actually use f(z) = z + 1, g(z) = z⁵ + z + 1: |g-f| = |z⁵| = 1, |f| = |z+1| ≥ ... need to be careful
  - Standard: f(z) = z + 1 has one zero at z = -1. On |z| = 1: |z⁵| = 1, |z + 1|: at z = -1, |z+1| = 0 — this doesn't work
  - Use instead: p(z) = z⁵ - 5z + 1 with |z| = 1, f(z) = -5z, g(z) = p(z). On |z| = 1: |g-f| = |z⁵ + 1| ≤ 2 < 5 = |f|. So same zeros as -5z, which has one zero (z=0) inside |z| = 1.
- Keep it simple with a clear example

### Scene 5: Application — Counting Zeros (~50s)
- Example: How many zeros does z⁴ - 3z² + 2 have in |z| < 2?
- Factor: (z²-1)(z²-2), zeros at ±1, ±√2 — all four inside |z| < 2
- Verify with Argument Principle: (1/2πi) ∮ f'(z)/f(z) dz = 4
- Visual: circle |z| = 2 with four zeros inside, all labeled

### Scene 6: Summary and Preview (~45s)
- Recap: zeros are isolated, Argument Principle counts N-P, Rouché's theorem compares
- The deep connection: integration → counting topological features
- Teaser: "Next time, we'll explore conformal mappings — transformations that preserve angles and shapes"
- Outro

## Color Coding
- PRIMARY (#5BC0EB): contours, boundaries, winding paths
- SECONDARY (#7BC950): zeros, analytic parts, positive quantities
- ACCENT (#FFD166): theorem statements, key results, N - P
- RED (#EF476F): poles, singularities, negative quantities
- DIM (#6B6B8D): computation steps, labels
