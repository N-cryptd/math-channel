# Video 132: Cauchy's Integral Formula

**Playlist:** Complex Analysis (Video 9 of 13)
**Class:** Video132_CauchysIntegralFormula
**Script:** scripts/undergraduate/video-132-cauchys-integral-formula.py
**Est. Duration:** 12 min
**Status:** PLAN + SCRIPT

## Competitive Analysis Summary

[Analysis completed 2026-07-30. YouTube search tool unavailable (youtubei.js v17 ESM-only breakage). Analysis based on known competitor content.]

- **3Blue1Brown:** Has NOT produced a dedicated Cauchy's Integral Formula video. His "Divergence and Curl" and "Green's Theorem" visualizations (Calc III) are the closest analogs — showing how boundary integrals encode interior information. This visual language directly informs our approach: show that CIF is the complex analog of "measuring the interior from the boundary."
- **Faculty of Khan:** "Cauchy's Integral Formula" — whiteboard style (~150K views). Covers the formula statement, proof using Cauchy's theorem, and computation examples (evaluating integrals of f(z)/(z-a)). Clean theorem-proof-example structure but NO visual geometric intuition of why the formula works.
- **Michael Penn:** Multiple CIF computation videos — rapid-fire algebra, shows how to use the formula to evaluate real integrals. Computation-heavy, no visualization of the keyhole contour or the geometric meaning.
- **Dr. Peyam:** Lecture-style video on CIF. Traditional theorem-proof-example format on blackboard. Good for seeing the algebra but no visual intuition.
- **BriTheMathGuy:** Has a "Complex Analysis" playlist with CIF coverage. Manim-based but fast-paced and computation-focused, less time on the beautiful geometric meaning.
- **The Bright Side of Mathematics:** Complex Analysis series includes CIF. Clean Manim style, theorem-statement-first approach. Covers the formula and its immediate corollaries.

**Market gap:** No video visually explains WHY Cauchy's Integral Formula works — why the values of an analytic function inside a disk are completely determined by its values on the boundary. The connection between the 1/(z-a) kernel and the "probe" interpretation is almost never animated. The geometric picture of shrinking a contour around a point to isolate the value at that point is powerful but rarely shown.

**Techniques to adopt:**
- Following 3B1B's boundary-encodes-interior philosophy: animate how integrating around a boundary "reads out" the function's value at interior points
- Visualize the key deformation: start with a large contour, then show it shrinking down to a tiny circle around z=a
- Show 1/(z-a) as a "probe kernel" — it detects the value f(a)
- Color-code the integrand decomposition: f(z)/(z-a) = f(a)/(z-a) + [f(z)-f(a)]/(z-a)
- Animate the second term vanishing as the circle shrinks (since f is analytic, the numerator is O(|z-a|))

**Techniques to avoid:**
- Stating the formal theorem before motivating WHY it's remarkable
- Dense algebra in the proof without geometric context
- Going straight to computation examples without first showing what the formula means
- Skipping the connection to Cauchy's theorem (this is the key bridge from Video 131)
- Not visualizing the contour deformation (key geometric insight)

## Scene Plan

### Scene 1: Hook — "Values from the Boundary" (~50s)
- Recap from Video 131: Cauchy's theorem says closed contour integrals of analytic functions vanish
- "But what if the function has a singularity inside the contour? The integral is no longer zero — and it encodes something beautiful"
- "Cauchy's Integral Formula says: the value of an analytic function at ANY interior point is completely determined by its values on the boundary"
- Visual: a contour in the complex plane with a point z0 inside it. An arrow from the boundary "reads" the value f(z0)
- Bridge: "We already know from Video 131 that if the domain is simply connected, the integral vanishes. But 1/(z - z0) has a singularity at z0, and its integral around z0 is 2*pi*i. Cauchy's formula combines these two facts into something extraordinary."

### Scene 2: The Theorem Statement (~55s)
- Theorem (Cauchy's Integral Formula): If f is analytic on and inside a simple closed contour gamma, and z0 is a point inside gamma, then f(z0) = (1/(2*pi*i)) * integral_gamma f(z)/(z - z0) dz
- Visual: theorem statement in a formula box with ACCENT border
- Highlight the three key parts: (1) f is analytic, (2) gamma is a simple closed contour, (3) z0 is inside gamma
- "The left side is just a function value. The right side is an integral over the boundary. This is remarkable: boundary data determines interior values"
- Emphasize: "For analytic functions, knowing the values on a circle tells you everything inside"

### Scene 3: The Key Ingredient — 1/(z - z0) (~60s)
- Recall from Video 131: integral_gamma 1/(z - z0) dz = 2*pi*i when z0 is inside gamma
- Visual: small circle around z0, parameterized as z0 + r*e^{it}
- Compute: integral = integral_0^{2pi} (1/(r*e^{it})) * i*r*e^{it} dt = 2*pi*i
- "The answer doesn't depend on r! Any circle around z0 gives 2*pi*i"
- Visual: animate the circle shrinking and growing — the integral stays constant
- "This is the kernel of Cauchy's formula — 1/(z-z0) is the probe that detects values"

### Scene 4: The Geometric Proof via Deformation (~65s)
- Start with: f(z0) = (1/(2*pi*i)) * integral_gamma f(z)/(z-z0) dz
- Key trick: write f(z)/(z-z0) = f(z0)/(z-z0) + [f(z)-f(z0)]/(z-z0)
- The first integral gives: f(z0) * (1/(2*pi*i)) * integral_gamma 1/(z-z0) dz = f(z0) * 1 = f(z0) ✓
- For the second integral: need to show it vanishes
- Visual: deform gamma into a tiny circle of radius epsilon around z0
- On this tiny circle: |f(z)-f(z0)| ≤ M*epsilon (since f is differentiable, the difference is bounded by epsilon)
- The integral ≤ M*epsilon * 2*pi*epsilon / epsilon = 2*pi*M*epsilon → 0 as epsilon → 0
- Visual: animate the contour shrinking — the second integral's contribution shrinks to zero
- Color-code: first term (SECONDARY), second term (RED) vanishing

### Scene 5: Computing with CIF — Example 1 (~60s)
- Evaluate integral_gamma z^2/(z-1) dz where gamma is |z| = 2
- f(z) = z^2, z0 = 1, which is inside |z| = 2
- By CIF: integral = 2*pi*i * f(1) = 2*pi*i * 1 = 2*pi*i
- Visual: show the circle |z| = 2, the point z0=1 inside it, the answer appearing
- "Notice how easy this is — no parameterization needed, no messy trigonometric integrals"
- Contrast: "In Video 130 we computed similar integrals by parameterization. CIF gives us the answer instantly"

### Scene 6: Higher Derivatives — The General Formula (~60s)
- "CIF doesn't just give the function value — it gives ALL derivatives"
- Theorem: f^(n)(z0) = (n!/(2*pi*i)) * integral_gamma f(z)/(z-z0)^{n+1} dz
- Visual: formula box for the general case
- "Differentiate both sides of the basic formula with respect to z0 — the derivative passes under the integral"
- "This is extraordinary: if f is analytic once, it is analytic infinitely many times"
- Visual: cascade of derivatives flowing from one formula — f, f', f'', f''' all determined by the boundary
- "In real analysis, differentiability once does NOT imply twice. But in complex analysis, once = infinitely many times"

### Scene 7: Computing Derivatives — Example 2 (~50s)
- Evaluate integral_gamma e^z/(z-1)^3 dz where gamma is |z| = 2
- This is the n=2 case: f(z) = e^z, z0 = 1
- By generalized CIF: integral = (2!/(2*pi*i))^{-1} ... wait
- Correct: integral = 2*pi*i * f''(z0)/2! = 2*pi*i * e^1/2 = pi*i*e
- Visual: show the computation steps with color coding
- "We extracted the second derivative of e^z at z=1, just from a boundary integral"
- Emphasize the power: "You don't even need to know the function explicitly — just that it's analytic"

### Scene 8: Summary and Preview (~45s)
- Recap the key ideas:
  1. CIF: f(z0) = (1/(2*pi*i)) * integral_gamma f(z)/(z-z0) dz
  2. The proof uses contour deformation and the key fact about 1/(z-z0)
  3. Generalized formula gives all derivatives from boundary data
  4. Analytic once → analytic infinitely many times
- Visual: four bullet points fading in one by one
- Teaser: "Next time, we'll use CIF to prove powerful consequences — the Maximum Modulus Principle, Liouville's Theorem, and the Fundamental Theorem of Algebra. CIF is the engine that drives all of complex analysis."
- Outro

## Color Coding
- PRIMARY (#5BC0EB): contours, paths, domain boundaries
- SECONDARY (#7BC950): analytic functions, f(z), function values
- ACCENT (#FFD166): theorem statements, key results, highlights, 2*pi*i
- RED (#EF476F): singularities, vanishing terms, things to be careful about
- DIM (#6B6B8D): contextual information, labels, computation steps
