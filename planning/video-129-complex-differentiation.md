# Video 129: Complex Differentiation

**Playlist:** Complex Analysis (Video 4 of 13)
**Class:** Video129_ComplexDifferentiation
**Script:** scripts/undergraduate/video-129-complex-differentiation.py
**Est. Duration:** 14 min
**Status:** PLAN → SCRIPT

## Competitive Analysis Summary

No dedicated animated/video competitor content found for "Complex Differentiation" or "Cauchy-Riemann Equations" as standalone topics with visual animation.

- **Faculty of Khan, Michael Penn, Dr. Peyam, MathTheBeautiful:** All cover C-R equations in lecture-style (chalkboard/computer screen) format. Faculty of Khan's video (~300K views) derives C-R by equating real-axis and imaginary-axis limits. Michael Penn does example-heavy computation. Dr. Peyam gives the full rigorous proof. None use animations.
- **3Blue1Brown:** Has NOT produced a dedicated complex differentiation / C-R video. His Fourier Transform video (12M views, spUNpyF58BY) is the gold standard for animated complex analysis visuals but covers a different topic. His complex exponentials content touches on holomorphic behavior intuitively but never states the C-R equations.
- **Reducible:** No complex analysis content.
- **Mathologer:** Covers complex analysis topics visually but not specifically differentiation/C-R.

**Market gap:** No high-production Manim-animated video exists explaining complex differentiation with visual intuition. This is the most critical topic in a complex analysis course — the moment where students learn why complex differentiability is so much stronger than real differentiability. The pedagogical opportunity is enormous:

1. The derivative definition looks identical to the real case — but the consequences are dramatically different because the limit must exist from ALL 2D directions
2. The C-R equations can be VISUALIZED: show how the derivative limit along x and along iy gives two different interpretations that must agree, leading to the equations
3. The "conformal mapping" consequence of holomorphicity can be shown visually — holomorphic functions preserve angles, which is a geometric property with no real-variable analogue
4. f(z) = z-bar is NOT differentiable — this was our counter-example from Video 128 and now gets its WHY explanation via C-R

**Techniques to adopt:**
- Animated limit visualization: show the difference quotient h approaching 0 from different angles in the complex plane, with the value of (f(z+h) - f(z))/h converging to the same number regardless of direction for holomorphic f
- Split-screen: real axis approach vs imaginary axis approach, equating them to derive C-R
- Color-coded u(x,y) and v(x,y) decomposition with partial derivatives highlighted
- Visual: show grid mapping under f(z) = z^2 (holomorphic — preserves angles) vs f(z) = z-bar (non-holomorphic — flips orientation)
- Connect to Video 128: "Remember how f(z) = z-bar/z had no limit at 0? The same function z-bar fails the C-R equations everywhere"

**Techniques to avoid:**
- Starting with the formal C-R theorem statement before geometric motivation
- Dense algebra without visual intuition for WHY the equations work
- Not connecting back to the approach-paths idea from Video 128

## Scene Plan

### Scene 1: Hook — "Same Formula, Different World" (~45s)
- Open with the real derivative formula: f'(x) = lim(h→0) [f(x+h) - f(x)] / h
- "What if we just replace x with z? f'(z) = lim(h→0) [f(z+h) - f(z)] / h"
- The formula looks IDENTICAL — but h is now a complex number approaching 0 from ALL directions
- Visual: real number line (h approaches from left and right) vs complex plane (h approaches from infinitely many directions)
- Bridge from Video 128's "all paths must agree" idea
- Intro

### Scene 2: Complex Derivative — Definition (~55s)
- Formal definition: f'(z₀) = lim(h→0) [f(z₀ + h) - f(z₀)] / h, h ∈ C
- Key insight: h can approach 0 along the real axis, imaginary axis, or any angle
- If the limit exists (all paths agree), f is differentiable at z₀
- Visual: show h approaching 0 as a shrinking vector from different angles, all giving same derivative value
- Emphasize: "Same limit structure, infinitely more demanding"
- Compare to real case: only 2 one-sided limits to check

### Scene 3: Why Complex Differentiability Is STRONGER (~50s)
- In R: f'(x) exists ⟺ left limit = right limit (2 conditions)
- In C: f'(z) exists ⟺ ALL directional limits agree (∞ conditions!)
- This is why complex differentiable functions are incredibly well-behaved
- Teaser: "A function that's complex differentiable is automatically infinitely differentiable — you can't say that in real analysis!"
- Visual: contrast "2 checks" (real) with "infinite checks" (complex) — the convergence requirement is vastly stronger

### Scene 4: Deriving the Cauchy-Riemann Equations (~65s)
- Write f(z) = f(x + iy) = u(x,y) + i·v(x,y)
- Approach 1: h → 0 along the real axis (h = Δx, real)
  - f'(z₀) = ∂u/∂x + i·∂v/∂x
- Approach 2: h → 0 along the imaginary axis (h = iΔy, imaginary)
  - f'(z₀) = ∂v/∂y - i·∂u/∂y
- Equate both expressions (they must be equal!):
  - ∂u/∂x = ∂v/∂y  and  ∂u/∂y = -∂v/∂x
- Visual: split-screen showing both approaches side by side, with color-coded u and v partials
- These are the CAUCHY-RIEMANN EQUATIONS — the necessary condition for differentiability

### Scene 5: The Cauchy-Riemann Equations — Statement and Meaning (~50s)
- Formal statement box: If f = u + iv is differentiable at z₀, then the C-R equations hold
- Converse: If u, v have continuous partial derivatives satisfying C-R at z₀, then f is differentiable there
- The C-R equations encode the constraint that the "stretch" of f is the same in all directions
- Visual: Jacobian matrix of f as a 2x2 real matrix, showing how C-R forces it to be a rotation + scaling (conformal)
- Key geometric insight: "C-R = the Jacobian is a similarity transformation"

### Scene 6: Example — f(z) = z² (Holomorphic) (~55s)
- f(z) = z² = (x² - y²) + i(2xy)
- So u = x² - y², v = 2xy
- Check C-R: ∂u/∂x = 2x = ∂v/∂y ✓, ∂u/∂y = -2y = -∂v/∂x ✓
- Therefore f'(z) = 2z (same formula as real!)
- Visual: show the u and v partial derivatives matching up, with checkmarks
- f(z) = z² is holomorphic everywhere — an "entire" function
- Quick mention: ALL polynomials are entire (holomorphic everywhere)

### Scene 7: Counter-Example — f(z) = z̄ (NOT Differentiable) (~50s)
- Connect to Video 128: "We saw f(z) = z-bar/z fails at z=0. What about just f(z) = z-bar?"
- f(z) = z̄ = x - iy, so u = x, v = -y
- Check C-R: ∂u/∂x = 1, ∂v/∂y = -1 → 1 ≠ -1 ✗
- C-R equations FAIL → z̄ is NOWHERE differentiable!
- Visual: show the C-R check with Red X on the failing equations
- Even though z̄ is continuous everywhere, it's differentiable NOWHERE
- "In real analysis, |x| is continuous but not differentiable at one point. In complex analysis, z-bar is continuous everywhere but differentiable NOWHERE — that's how strong the requirement is"

### Scene 8: Holomorphic and Entire Functions (~45s)
- Definition: f is holomorphic on an open set Ω if it's differentiable at every point of Ω
- "Entire" = holomorphic on all of C
- Examples of entire functions: polynomials, e^z, sin(z), cos(z)
- Key property teaser: "If f is holomorphic, then f is infinitely differentiable, f is analytic (equals its Taylor series), and f satisfies Cauchy's integral formula — this is the miracle of complex analysis"
- Visual: hierarchy diagram showing continuous ⊃ differentiable ⊃ holomorphic

### Scene 9: Summary and Road Ahead (~40s)
- Key takeaways: complex derivative = same formula, vastly stronger requirement; C-R equations are the test; polynomials and e^z are holomorphic everywhere; z-bar is nowhere differentiable
- Teaser for next video: complex integration and Cauchy's theorem
- Outro

## Content Budget per Scene

| Scene | Elements on Screen | Notes |
|-------|-------------------|-------|
| 1 | Max 4 | Real derivative formula, complex derivative formula, real line vs complex plane |
| 2 | Max 4 | Definition formula, shrinking h vectors, convergence indicator |
| 3 | Max 4 | "2 checks" vs "∞ checks", comparison diagram |
| 4 | Max 5 | f = u+iv decomposition, two approach paths with partials, C-R equations |
| 5 | Max 4 | C-R theorem box, Jacobian matrix, geometric interpretation |
| 6 | Max 4 | z² decomposition, partial derivative computation, checkmarks |
| 7 | Max 4 | z̄ decomposition, C-R check with X marks, comparison to |x| |
| 8 | Max 4 | Hierarchy diagram, entire function examples, key property |
| 9 | Max 3 | Summary list, teaser text, channel outro |

## Color Coding
- PRIMARY (#5BC0EB): Real parts, real axis approach, u(x,y)
- SECONDARY (#7BC950): Imaginary parts, imaginary axis approach, v(x,y)
- ACCENT (#FFD166): Key formulas (derivative definition, C-R equations, theorem statements)
- RED (#EF476F): Counter-examples, "does not hold", non-differentiability markers
- DIM (#6B6B8D): Secondary information, labels, hierarchy diagram
