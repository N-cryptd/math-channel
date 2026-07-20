# Video 128: Limits and Continuity in C

**Playlist:** Complex Analysis (Video 3 of 13)
**Class:** Video128_LimitsContinuityComplex
**Script:** scripts/undergraduate/video-128-limits-continuity-complex.py
**Est. Duration:** 12 min
**Status:** PLAN → SCRIPT

## Competitive Analysis Summary

No dedicated animated/video competitor content found for "Limits and Continuity in Complex Analysis" as a standalone topic. The topic is typically covered:
- **Dr. Peyam / Michael Penn:** As a 5-minute chalkboard segment within larger complex analysis lectures — no visual animations, purely symbolic epsilon-delta proofs.
- **Textbooks:** Ahlfors, Churchill & Brown — formal definition-first approach, no animations.
- **3Blue1Brown:** Has not covered complex limits/continuity explicitly; his complex exponentials video touches on continuity of e^z intuitively but never states the definition.

**Market gap:** No high-production Manim-animated video exists explaining complex limits and continuity with visual intuition. This is a pedagogically critical topic because:
1. The epsilon-delta definition extends naturally from R^2 → C (since C ≅ R^2), but most students don't realize this connection
2. Continuity in C is STRONGER than real continuity — the function must "work" from all directions in the plane, not just left/right
3. This sets up the key insight that differentiability in C is MUCH stronger than in R — the Cauchy-Riemann equations require specific behavior

**Techniques to adopt:**
- Animated epsilon-delta disk shrinking around a point (3B1B-style visual)
- Show approach paths: from real axis, imaginary axis, and diagonally — all must agree
- Contrast with real limits (only 2 directions: left and right)
- Use the u(x,y) + iv(x,y) decomposition to show how complex continuity = real continuity of both component functions
- Animated approach along different paths converging to same limit

**Techniques to avoid:**
- Starting with the formal epsilon-delta definition before geometric intuition
- Dense proof-heavy approach without visuals
- Not emphasizing the key difference: C ≅ R^2 means limits require convergence from ALL 2D directions, not just 2 (left/right)

## Scene Plan

### Scene 1: Hook — "What Does 'Close' Mean in the Complex Plane?" (~40s)
- Open with the real limit concept: lim(x→a) f(x) = L means x approaching a from left AND right
- Ask: "But in the complex plane, there are infinitely many directions to approach a point!"
- Visual: convergence paths on a 2D plane radiating toward a central point
- Bridge from Video 127 (complex functions) to limits
- Intro

### Scene 2: Complex Limits — Definition (~55s)
- Define lim(z→z₀) f(z) = L in epsilon-delta language adapted to C
- Key: |z - z₀| < δ implies |f(z) - L| < ε
- Visual: epsilon disk in the w-plane, delta disk in the z-plane
- f maps the delta disk INTO the epsilon disk
- Emphasize: the definition looks identical to R^2, and it IS — because C ≅ R^2 topologically

### Scene 3: Approach Paths — Why Complex Limits Are Harder (~55s)
- In R: only 2 directions (left, right) to check
- In C: infinitely many paths — straight lines from any angle, spirals, zigzags
- If the limit exists, ALL paths must agree
- Visual: show 3-4 different colored paths converging to z₀, all mapping to points near L
- Counter-example teaser: if two paths give different values, the limit does NOT exist

### Scene 4: Limit Does Not Exist — A Counter-Example (~50s)
- Classic example: f(z) = z̄ / z (conjugate over z) as z → 0
- Along real axis (y=0): z = x, z̄/z = x/x = 1
- Along imaginary axis (x=0): z = iy, z̄/z = (-iy)/(iy) = -1
- Different paths give different limits → limit does not exist
- Visual: show the two paths with different result values, Red X mark

### Scene 5: Continuity in C (~50s)
- Definition: f is continuous at z₀ if lim(z→z₀) f(z) = f(z₀)
- Three equivalent perspectives:
  1. Epsilon-delta definition (direct)
  2. Sequential: z_n → z₀ implies f(z_n) → f(z₀)
  3. Component-wise: u and v are both continuous (as real functions of x,y)
- Visual: smooth function with no "jumps" in the complex plane
- Key insight: continuity in C = continuity of both u(x,y) and v(x,y)

### Scene 6: Examples of Continuous Functions (~50s)
- Polynomials: always continuous everywhere (sum of continuous functions)
- e^z: continuous everywhere (series converges uniformly)
- Rational functions: continuous everywhere EXCEPT at poles
- Visual: show continuity domain for 1/z (punctured plane)
- Contrast: f(z) = z̄/z is discontinuous at z=0

### Scene 7: Sequences and Series — Complex Version (~45s)
- Definition of convergence: z_n → z₀ means |z_n - z₀| → 0
- Same as convergence in R^2
- Power series converge in complex disks (not just intervals!)
- Teaser: radius of convergence is a DISK in C, not just an interval in R
- This is the geometric insight that complex analysis provides

### Scene 8: Summary and Road Ahead (~35s)
- Key takeaways: complex limits require ALL-path agreement, continuity = u,v continuous, polynomials/exponentials are everywhere continuous
- Teaser for next video: complex differentiation — the Cauchy-Riemann equations
- Outro

## Content Budget per Scene

| Scene | Elements on Screen | Notes |
|-------|-------------------|-------|
| 1 | Max 4 | Real limit diagram, question, complex plane with paths |
| 2 | Max 4 | Epsilon-delta formula, delta disk, epsilon disk, mapping arrow |
| 3 | Max 5 | Complex plane, 3-4 approach paths, z₀ label |
| 4 | Max 4 | Two paths with different limits, formulas, Red X |
| 5 | Max 4 | Continuity definition, smooth function visual, u/v decomposition |
| 6 | Max 4 | Polynomial example, punctured plane, continuity domain |
| 7 | Max 4 | Sequence convergence, disk vs interval comparison |
| 8 | Max 3 | Summary list, teaser text, channel outro |

## Color Coding
- PRIMARY (#5BC0EB): Axes, real parts, approach paths from real direction
- SECONDARY (#7BC950): Imaginary parts, approach paths from imaginary direction
- ACCENT (#FFD166): Key formulas (epsilon-delta definition, continuity definition)
- RED (#EF476F): Counter-examples, "limit does not exist", discontinuity markers
- DIM (#6B6B8D): Secondary information, sequence terms
