# Video 131: Cauchy's Theorem

**Playlist:** Complex Analysis (Video 8 of 13)
**Class:** Video131_CauchysTheorem
**Script:** scripts/undergraduate/video-131-cauchys-theorem.py
**Est. Duration:** 12 min
**Status:** PLAN + SCRIPT

## Competitive Analysis Summary

No high-production Manim-animated video exists specifically explaining Cauchy's Theorem with visual geometric intuition.

- **3Blue1Brown:** Has NOT produced a dedicated Cauchy's Theorem video. His "Green's Theorem" visualization (Chapter 14 of Multivariable Calc) is the closest visual analog — showing that circulation vanishes for curl-free vector fields. This is the real-line version of Cauchy's theorem and informs our geometric approach.
- **Faculty of Khan:** "Cauchy's Theorem (Complex Analysis)" — whiteboard-style (~150K views). Covers the theorem statement, uses the Green's Theorem connection for the proof sketch. No animations of contours or regions.
- **Michael Penn:** Multiple contour integral computation videos that use Cauchy's theorem. Rapid-fire algebra, no geometric visualization of the simply-connected domain or the vanishing integral.
- **Dr. Peyam:** Lecture-style video on Cauchy's theorem. Traditional theorem-proof-example format on blackboard.
- **BriTheMathGuy:** Has a "Complex Analysis" playlist with a Cauchy's theorem section. Manim-based but fast-paced and computation-heavy, less time on the geometric intuition.
- **The Bright Side of Mathematics:** Has a complex analysis series including Cauchy's integral theorem. Clean Manim style, theorem-statement-first approach.

**Market gap:** No video visually explains WHY the integral of an analytic function around a closed loop vanishes. The connection to Green's theorem and the Cauchy-Riemann equations making the integrand exact is almost never animated. The simply-connectedness condition is stated but rarely visualized with domain topology.

**Techniques to adopt:**
- Following 3B1B's Green's Theorem intuition: show the curl-free / divergence-free decomposition that the C-R equations create
- Animate a contour shrinking to a point, showing the integral stays zero at every scale
- Visual: simply-connected domain (filled region) vs. multiply-connected domain (hole in the middle)
- Color-code the integrand's real and imaginary parts using u, v and show they cancel via C-R

**Techniques to avoid:**
- Stating the theorem formally before any geometric motivation
- Skipping the simply-connected condition (it's the #1 student mistake)
- Going straight to the proof without showing what the theorem MEANS visually
- Dense algebra in the proof — keep the visual geometric intuition primary

## Scene Plan

### Scene 1: Hook — "The Most Surprising Result in Complex Analysis" (~50s)
- Open with the result from Video 130: polynomial integrals around closed paths vanish
- "What if we told you this isn't just true for polynomials, but for EVERY analytic function?"
- This is Cauchy's Theorem: the integral of f(z) around any closed contour is zero
- Visual: a closed contour in the complex plane with the integral = 0 appearing
- Bridge: "We already know from Video 130 that f(z) = z and f(z) = z^2 integrate to zero around closed paths. Cauchy's theorem says this holds for all analytic functions."

### Scene 2: Simply-Connected Domains (~55s)
- Define simply-connected: a domain D in C where every closed curve can be continuously shrunk to a point without leaving D
- Visual: a simply-connected region (filled circle/ellipse) with a contour inside it shrinking to a point
- Contrast with a multiply-connected domain: a region with a hole (like an annulus)
- "A contour around the hole cannot be shrunk past it" — visual of the contour getting stuck on the hole
- This condition is ESSENTIAL — Cauchy's theorem fails without it

### Scene 3: The Theorem Statement (~50s)
- Theorem (Cauchy-Goursat): If f is analytic on a simply-connected domain D, then for every closed contour gamma in D, the integral of f(z) dz = 0
- Visual: theorem statement in a formula box with ACCENT border
- Highlight three key ingredients: (1) f is analytic, (2) D is simply-connected, (3) gamma is closed
- Each ingredient gets a color-coded label
- "Let's understand why this is true."

### Scene 4: The Intuition via Green's Theorem (~65s)
- Recap: integral_gamma f(z) dz = integral_gamma (u dx - v dy) + i integral_gamma (v dx + u dy)
- Green's Theorem says: integral_gamma P dx + Q dy = double integral_D (dQ/dx - dP/dy) dA
- Apply to both real and imaginary parts using the Cauchy-Riemann equations
- Real part: dQ/dx - dP/dy = d(-v)/dx - du/dy = -(dv/dx + du/dy)... wait, that's wrong
- Correct: P = u, Q = -v for real part: dQ/dx - dP/dy = -dv/dx - du/dy
- Using C-R: du/dx = dv/dy and du/dy = -dv/dx
- So -dv/dx - du/dy = du/dy - du/dy = 0
- Visual: show the cancellation step by step with color coding
- Same cancellation for the imaginary part

### Scene 5: The Geometric Picture (~55s)
- The C-R equations say f' exists — the function's real and imaginary parts are tightly coupled
- This coupling makes the integrand an exact differential: f(z) dz = dF for some F
- Exact differentials always integrate to zero around closed loops
- Visual: a flow field where the circulation around any closed loop vanishes
- "Analytic functions are the 'conservative' functions of the complex plane"
- This is the deep reason: analyticity implies path-independence

### Scene 6: Example — f(z) = 1/z and the Hole (~60s)
- Now show what happens WITHOUT simply-connectedness
- f(z) = 1/z is analytic on C \ {0}, which is NOT simply-connected
- Contour: unit circle gamma(t) = e^{it}, 0 <= t <= 2*pi
- Compute: integral = integral_0^{2pi} (1/e^{it}) * i e^{it} dt = integral_0^{2pi} i dt = 2*pi*i
- The integral is NOT zero! Because the domain has a hole at z = 0
- Visual: the unit circle contour, the hole at the origin highlighted in RED
- "The singularity at z = 0 creates a hole, and the integral 'detects' this hole"

### Scene 7: Consequences and Preview (~50s)
- Cauchy's theorem has enormous consequences:
  1. Path independence: if two paths share endpoints, the integrals are equal
  2. Antiderivatives exist for analytic functions on simply-connected domains
  3. This leads directly to Cauchy's Integral Formula (next video)
- Visual: two paths from z1 to z2, showing the closed loop integral is zero, hence the path integrals are equal
- Teaser: "Next time, we'll see that Cauchy's theorem gives us something even more powerful: Cauchy's Integral Formula, which lets us compute function values from boundary data alone."

### Scene 8: Summary (~40s)
- Recap the three key ideas:
  1. Cauchy's theorem: analytic + simply-connected + closed contour => integral = 0
   2. The proof relies on Green's Theorem + Cauchy-Riemann equations
   3. Simply-connectedness is not optional — 1/z shows what happens without it
- Visual: three bullet points fading in one by one
- Outro

## Color Coding
- PRIMARY (#5BC0EB): contours, paths, domain boundaries
- SECONDARY (#7BC950): analytic functions, u(x,y) component
- ACCENT (#FFD166): theorem statements, key results, highlights
- RED (#EF476F): warnings, singularities, holes, things that go wrong
- DIM (#6B6B8D): contextual information, labels
