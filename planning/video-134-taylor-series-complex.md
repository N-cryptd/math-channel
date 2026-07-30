# Video 134: Taylor Series in the Complex Plane

**Playlist:** Complex Analysis (Video 11 of 13)
**Class:** Video134_TaylorSeriesComplex
**Script:** scripts/undergraduate/video-134-taylor-series-complex.py
**Est. Duration:** 12 min
**Status:** PLAN

## Competitive Analysis Summary

[Analysis based on known competitor content.]

- **3Blue1Brown:** Has NOT produced a dedicated video on complex Taylor series. His "Taylor series" chapter (Calc II) is the closest analog — showing how polynomials approximate functions. The visual language of successive approximations directly informs our approach.
- **Faculty of Khan:** Has a video on Taylor/Laurent series in complex analysis. Whiteboard style, covers the derivation from CIF and convergence properties but lacks animated visualization of the disk of convergence.
- **Michael Penn:** Multiple Taylor series computation videos. Rapid-fire algebra, shows how to find Taylor coefficients but doesn't visualize the convergence disk.
- **Dr. Peyam:** Lecture-style video on complex Taylor series. Traditional theorem-proof format.
- **BriTheMathGuy:** Manim-based but fast-paced, focuses on the formula rather than the beautiful geometric picture of disk convergence.
- **The Bright Side of Mathematics:** Complex Analysis series likely covers this with clean Manim style.

**Market gap:** No video visually explains WHY Taylor series converge in perfect disks in the complex plane — and how the radius of convergence is determined by the nearest singularity. This is one of the most striking differences between real and complex analysis, and it's almost never animated.

**Techniques to adopt:**
- Animate successive Taylor polynomial approximations on the complex plane
- Visualize the disk of convergence growing until it hits the nearest singularity
- Show the contrast: real Taylor series have mysterious convergence behavior, complex ones have clean disk convergence
- Color-code the coefficients: c_n = f^(n)(a)/n! from CIF

**Techniques to avoid:**
- Stating the formula without showing where it comes from (CIF connection)
- Skipping the key insight about the radius of convergence and nearest singularity
- Not showing the contrast with real Taylor series (this is what makes complex Taylor series beautiful)
- Dense coefficient computation without geometric context

## Scene Plan

### Scene 1: Hook — "Series That Always Converge in Circles" (~50s)
- Recap from Video 133: CIF gives us derivatives, and derivatives give us power series
- "In real analysis, Taylor series are mysterious — some converge, some don't, and the reasons are subtle"
- "In complex analysis, Taylor series ALWAYS converge in perfect disks. And the radius is determined by something beautiful: the distance to the nearest singularity"
- Visual: a point with concentric circles expanding outward, each labeled as the disk of convergence
- Bridge: "This is one of the most striking differences between real and complex analysis"

### Scene 2: The Taylor Series Formula (~55s)
- Every analytic function has a Taylor series: f(z) = Σ (z-a)^n / n! * f^(n)(a)
- The coefficients come from CIF: c_n = f^(n)(a)/n! = 1/(2πi) ∮ f(z)/(z-a)^{n+1} dz
- Visual: formula box, then the coefficient formula with CIF connection
- "Every analytic function is equal to its Taylor series — not just nearby, but within the entire disk of convergence"

### Scene 3: The Radius of Convergence (~60s)
- Key theorem: the Taylor series converges for |z-a| < R, where R is the distance from a to the nearest singularity of f
- Visual: point a, nearest singularity at distance R, disk of convergence, boundary of disk touches the singularity
- Example: 1/(1-z) expanded around z=0: nearest singularity at z=1, R=1, series is Σ z^n
- Example: 1/(1+z) expanded around z=2: nearest singularity at z=-1, R=3, series converges in disk of radius 3
- "The singularities are the roadblocks — the series can't see past them"

### Scene 4: Visualizing Convergence (~55s)
- Visual: animate Taylor polynomials approximating a function (e.g., e^z or 1/(1-z))
- Show: T_1, T_3, T_5, T_10 — each one fills in more of the function
- Outside the disk: the polynomials diverge
- Color gradient: inside disk (green/accurate) → boundary (yellow) → outside (red/divergent)
- "Inside the disk: the polynomial approximations converge uniformly"

### Scene 5: Contrast with Real Analysis (~50s)
- Real: ln(1+x) = x - x²/2 + x³/3 - ... converges only for -1 < x ≤ 1
- The reason in real analysis: mysterious, hard to explain
- Complex: the SAME series converges for |z| < 1, and the reason is clear: the singularity at z = -1
- Visual: real number line with convergence interval, next to complex plane with convergence disk
- "The complex picture explains what the real picture cannot"

### Scene 6: Summary and Preview (~45s)
- Recap: analytic functions = Taylor series within disk of convergence
- Radius = distance to nearest singularity
- Complex Taylor series are simpler and more beautiful than real ones
- Teaser: "Next time, we'll explore what happens when a function has a singularity INSIDE the region — Laurent series"
- Outro

## Color Coding
- PRIMARY (#5BC0EB): convergence disks, boundaries, geometric objects
- SECONDARY (#7BC950): analytic functions, Taylor polynomials, convergence regions
- ACCENT (#FFD166): theorem statements, key formulas, highlights
- RED (#EF476F): singularities, divergence regions, boundaries of convergence
- DIM (#6B6B8D): computation steps, labels, secondary information
