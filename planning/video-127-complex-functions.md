# Video 127: Complex Functions

**Playlist:** Complex Analysis (Video 2 of 13)
**Class:** Video127_ComplexFunctions
**Script:** scripts/undergraduate/video-127-complex-functions.py
**Est. Duration:** 14 min
**Status:** PLAN -> SCRIPT

## Competitive Analysis Summary

Completed competitive analysis (see parent task t_6984d2ad). Key findings:
- **3Blue1Brown:** Winding/wrapping animations for complex exponentials are iconic; domain coloring via phase portraits is the gold standard for f:C->C visualization.
- **Mathologer:** Deep Euler's formula exploration with geometric narrative arc.
- **Michael Penn:** Traditional lecture-style proofs, lacking visual depth.
- **Dr. Peyam:** Graduate-level rigor, no animations.
- **Domain coloring creators:** Phase portrait visualizations rarely explained in intro videos.

**Techniques to adopt:**
- Grid transformation animations (conformal mapping visualization) — show how a grid in the domain warps under f(z)
- Winding/wrapping animation for e^z (inspired by 3B1B's Fourier transform approach)
- Decompose f(z) into Re(f(z)) and Im(f(z)) shown as colored surfaces
- Progressive disclosure: define each function class before visualizing it
- Domain coloring concept introduction (phase hue + brightness = magnitude)

**Techniques to avoid:**
- Dense definition-heavy approach without motivating visuals
- Showing a full domain coloring image without explaining what colors represent
- Skipping the connection between e^z and sin(z)/cos(z)

## Scene Plan

### Scene 1: Hook — "From Real to Complex" (~45s)
- Start with a familiar real function graph (e.g., f(x) = x^2 as a parabola on a 2D plane)
- Transition question: "But what happens when the input is complex?"
- Show that the output is also complex — we need a 4D picture (impossible to graph directly)
- Bridge from Video 126 (complex numbers) to functions between them
- Introduce the episode title

### Scene 2: Complex Functions — Definition and Notation (~50s)
- Define f: C -> C — a function from complex numbers to complex numbers
- Write f(z) = u(x,y) + iv(x,y) where z = x + iy
- Decompose into real and imaginary parts u and v
- Visual: input point z on the complex plane, output point w = f(z) on another copy of the complex plane
- Notation: w = f(z), mapping the z-plane to the w-plane

### Scene 3: Polynomials in C (~55s)
- Define polynomial p(z) = a_n z^n + ... + a_1 z + a_0 with complex coefficients
- Example: p(z) = z^2 + 1 — always has a root (z = i)
- Visual: map a few points through p(z) = z^2 and show output positions
- Key insight: Fundamental Theorem of Algebra — every non-constant polynomial has a root
- Visual: z^2 maps the complex plane by squaring the modulus and doubling the argument

### Scene 4: Rational Functions (~45s)
- Define R(z) = P(z)/Q(z) — ratio of two polynomials
- Zeros (where P(z) = 0) and poles (where Q(z) = 0)
- Example: R(z) = 1/z — the simplest non-trivial rational function
- Visual: show the inversion mapping (reciprocal) geometrically
- Key insight: rational functions are defined everywhere except at poles

### Scene 5: The Complex Exponential e^z (~65s)
- Define via power series: e^z = sum z^n/n! (same form as real exponential)
- Key property: e^(x+iy) = e^x * e^(iy) = e^x(cos y + i sin y)
- Decompose: Re(e^z) = e^x cos y, Im(e^z) = e^x sin y
- Visual: winding animation — as y increases, e^(iy) wraps around the unit circle; e^x scales the radius
- Show the periodicity in the imaginary direction: e^(z + 2πi) = e^z
- Visual: horizontal strips map to concentric annuli (or the whole plane minus origin)

### Scene 6: Trigonometric Functions in C (~55s)
- Define sin(z) and cos(z) via Euler's formula:
  - sin(z) = (e^(iz) - e^(-iz)) / (2i)
  - cos(z) = (e^(iz) + e^(-iz)) / 2
- These satisfy all the familiar identities: sin^2 + cos^2 = 1, angle addition, etc.
- But they are UNBOUNDED on C (unlike on R where |sin| <= 1)
- Visual: show sin(z) growing exponentially along the imaginary axis
- Key insight: cos(iy) = cosh(y) — hyperbolic cosine!

### Scene 7: Visualizing Complex Functions (~60s)
- The challenge: f: C -> C is a 4D map — how do we visualize it?
- Method 1: Domain coloring — color the input plane by arg(f(z)) (hue) and |f(z)| (brightness)
- Method 2: Grid transformation — show how a regular grid in the z-plane warps under f
- Method 3: Separate Re and Im as 3D surfaces
- Visual: simple grid transformation for f(z) = z^2 (wraps the plane twice)
- Visual: domain coloring concept for e^z (repeating hue bands)
- Teaser: conformal mapping is the beautiful property that preserves angles locally

### Scene 8: Summary and Road Ahead (~40s)
- Key takeaways: f(z) = u+iv decomposition, polynomials always have roots, e^z is periodic, sin/cos are unbounded in C, visualization via domain coloring
- Teaser for next video: Limits and Continuity in C
- Outro

## Content Budget per Scene

| Scene | Elements on Screen | Notes |
|-------|-------------------|-------|
| 1 | Max 4 | Real graph, question, complex plane, arrow |
| 2 | Max 4 | Definition, u+iv decomposition, z-plane and w-plane |
| 3 | Max 4 | Polynomial definition, z^2 mapping visual, FTA statement |
| 4 | Max 4 | Rational function definition, 1/z mapping, pole/zero labels |
| 5 | Max 5 | Power series, decomposition formula, winding animation, periodicity |
| 6 | Max 4 | Euler definitions, sin/cos identities, unboundedness visual |
| 7 | Max 5 | Domain coloring concept, grid transform, Re/Im surfaces |
| 8 | Max 3 | Summary list, teaser text, channel outro |

## Color Coding
- PRIMARY (#5BC0EB): Axes, real parts, polynomial terms
- SECONDARY (#7BC950): Imaginary parts, trigonometric functions
- ACCENT (#FFD166): Key formulas, exponential function highlights
- RED (#EF476F): Special values, poles, periodicity indicators
- DIM (#6B6B8D): Secondary information, labels, arrows
