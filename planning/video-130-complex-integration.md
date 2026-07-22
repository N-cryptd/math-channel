# Video 130: Complex Integration (Contour Integrals)

**Playlist:** Complex Analysis (Video 7 of 13)
**Class:** Video130_ComplexIntegration
**Script:** scripts/undergraduate/video-130-complex-integration.py
**Est. Duration:** 15 min
**Status:** PLAN → SCRIPT

## Competitive Analysis Summary

No dedicated animated competitor content found for "Contour Integrals" or "Complex Line Integrals" as standalone topics with visual animation.

- **Faculty of Khan:** Has a contour integral video (~200K views) with whiteboard-style derivation. Covers parameterization of gamma and the integral formula, but no animations of paths in the complex plane.
- **Michael Penn:** Has multiple contour integral computation videos. Dense example-driven approach with rapid algebra, no visuals.
- **Dr. Peyam:** Lecture-style C-R and contour integral videos. Traditional theorem-proof format.
- **3Blue1Brown:** Has NOT produced a dedicated contour integral video. His "Divergence and Curl" and "Green's Theorem" videos show related line integral visuals that could inspire our approach — particularly his path animation and flux/flow color coding.
- **Mathologer:** No contour integral content found.

**Market gap:** No high-production Manim-animated video exists explaining contour integrals with visual path animation. The key pedagogical opportunity:

1. The integral of f(z) dz generalizes real line integrals to curves in the complex plane — this can be VISUALIZED by animating a path gamma(t) through the complex plane while showing the integrand's value along it
2. Parameterization is the bridge between geometry and computation — show how gamma(t) = x(t) + iy(t) translates a curve into integrable components
3. The fact that dz = gamma'(t) dt decomposes naturally into dx + i dy — this decomposition is visually intuitive when shown alongside the curve
4. Polynomials integrated along any closed path give zero — this is a concrete preview of Cauchy's theorem without requiring its full machinery

**Techniques to adopt:**
- Animated path tracing through the complex plane (gamma curve drawn in real-time)
- Color-coded decomposition: gamma(t) = x(t) + iy(t) with PRIMARY for real part, SECONDARY for imaginary part
- Split-screen: geometric curve on the left, algebraic parameterization on the right
- Connect to Video 129: "Since we now know polynomials are holomorphic, their integrals around closed paths vanish"
- Use concrete worked examples with f(z) = z (trivial) and f(z) = z^2 (shows the pattern)

**Techniques to avoid:**
- Starting with the most general form without motivating the definition
- Dense algebra without showing the geometric path alongside it
- Not connecting back to real line integrals (students learned those in Calculus III)

## Scene Plan

### Scene 1: Hook — "From the Real Line to the Complex Plane" (~45s)
- Recap: real line integrals integrate a function along a curve in R^2
- "What if f is a complex-valued function and the curve lives in the complex plane?"
- Visual: real plane curve fading into complex plane curve (color shift)
- Bridge from Video 129's differentiation to integration: "We have complex derivatives. Now we need complex integrals."
- Intro

### Scene 2: Contours and Parameterization (~55s)
- Define: a contour (or path) gamma is a piecewise smooth curve in C
- Parameterize: gamma(t) for a <= t <= b, where gamma(t) = x(t) + i y(t)
- Visual: show a specific curve (e.g., semicircle) being traced out as t goes from a to b
- Show the real and imaginary components: x(t) and y(t) side by side
- Key: gamma'(t) = x'(t) + i y'(t) gives the tangent direction at each point

### Scene 3: The Contour Integral Definition (~60s)
- Definition: integral_C f(z) dz = integral_a^b f(gamma(t)) * gamma'(t) dt
- This is the complex analogue of the real line integral
- Expand: if f(z) = u(x,y) + i v(x,y), then:
  integral_C f(z) dz = integral_C (u dx - v dy) + i integral_C (v dx + u dy)
- Visual: show the definition boxed in accent color, then expand with color-coded u/v components
- Two real integrals in one complex integral

### Scene 4: Computing dz Along a Contour (~50s)
- Practical formula: dz = gamma'(t) dt = (x'(t) + i y'(t)) dt
- So the integral becomes a standard calculus integral from a to b
- Key steps: (1) parameterize the contour, (2) substitute z = gamma(t) and dz = gamma'(t) dt, (3) integrate from t=a to t=b
- Visual: three-step algorithm as a numbered list

### Scene 5: Example 1 — f(z) = z along a straight line (~60s)
- Contour: straight line from z=0 to z=1+i (gamma(t) = t(1+i), 0 <= t <= 1)
- gamma'(t) = 1 + i
- f(gamma(t)) = t(1+i)
- f(gamma(t)) * gamma'(t) dt = t(1+i)(1+i) dt = t(2i) dt
- Integral = integral_0^1 2it dt = 2i * [t^2/2]_0^1 = i
- Visual: trace the line segment while computing the integral step by step
- This is path-dependent! If we chose a different curve from 0 to 1+i, we'd get a different answer

### Scene 6: Example 2 — f(z) = z^2 along the unit semicircle (~65s)
- Contour: upper unit semicircle from z=1 to z=-1 (gamma(t) = e^{it}, 0 <= t <= pi)
- gamma'(t) = i e^{it}
- f(gamma(t)) = e^{2it}
- f(gamma(t)) * gamma'(t) dt = e^{2it} * i e^{it} dt = i e^{3it} dt
- Integral = i * integral_0^pi e^{3it} dt = i * [e^{3it}/(3i)]_0^pi = (1/3)(e^{3ipi} - 1) = (1/3)(-1 - 1) = -2/3
- Visual: trace the semicircle while computing

### Scene 7: Closed Contours and a Preview of Cauchy (~55s)
- A contour is closed if gamma(a) = gamma(b)
- Notation: integral with a circle (contour integral notation)
- Key fact preview: if f is holomorphic on and inside gamma, the closed contour integral is ZERO
- Example: integral over any closed contour of z dz = 0 (since z is entire)
- Visual: closed curve with the integral = 0 result highlighted in accent
- "This is a shadow of Cauchy's theorem — the deep result we'll prove in the next videos"

### Scene 8: Summary and Road Ahead (~40s)
- Key takeaways: contour integrals generalize line integrals to C; parameterization converts them to real integrals; the integral depends on both the function and the path; holomorphic functions integrate to zero around closed contours
- Teaser: Cauchy's Theorem and Cauchy's Integral Formula
- Outro

## Content Budget per Scene

| Scene | Elements on Screen | Notes |
|-------|-------------------|-------|
| 1 | Max 4 | Real line integral, complex plane curve, transition visual |
| 2 | Max 5 | Contour curve, parameterization formula, gamma(t) components, tangent vector |
| 3 | Max 4 | Definition box, u/v decomposition, two real integrals |
| 4 | Max 4 | dz formula, three-step algorithm |
| 5 | Max 5 | Line segment, parameterization, substitution steps, final answer |
| 6 | Max 5 | Semicircle, parameterization, computation steps, final answer |
| 7 | Max 4 | Closed contour, integral=0 notation, holomorphic property |
| 8 | Max 3 | Summary list, teaser text, channel outro |

## Color Coding
- PRIMARY (#5BC0EB): Real parts, x(t), Re(f), real-axis components
- SECONDARY (#7BC950): Imaginary parts, y(t), Im(f), imaginary-axis components
- ACCENT (#FFD166): Key formulas (integral definition, theorem statements, final answers)
- RED (#EF476F): Warnings, non-zero results when zero expected
- DIM (#6B6B8D): Secondary information, labels, step numbers
