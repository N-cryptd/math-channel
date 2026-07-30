# Video 136: The Residue Theorem

**Playlist:** Complex Analysis (Video 13 of 13 — FINALE)
**Class:** Video136_ResidueTheorem
**Script:** scripts/undergraduate/video-136-residue-theorem.py
**Est. Duration:** 12 min
**Status:** PLAN

## Competitive Analysis Summary

[Analysis based on known competitor content.]

- **3Blue1Brown:** Has NOT produced a dedicated Residue Theorem video. His approach to complex analysis through visual intuition would suggest: showing the theorem as a "counting theorem" — counting singularities and their strengths (residues) to evaluate integrals.
- **Faculty of Khan:** Has a video on the Residue Theorem. Whiteboard style, covers the statement, computing residues at simple poles and higher-order poles, and evaluating integrals. Clean but no animated visualization.
- **Michael Penn:** Many residue theorem computation videos. Shows how to evaluate complex and real integrals using residues. Very computation-focused.
- **Dr. Peyam:** Lecture-style video on the Residue Theorem. Traditional theorem-proof format.
- **BriTheMathGuy:** Manim-based but fast-paced, computation-heavy.
- **The Bright Side of Mathematics:** Complex Analysis series likely covers this.

**Market gap:** No video visually explains the Residue Theorem as a "counting theorem" — showing that the contour integral is the sum of contributions from each singularity inside, and that the residue measures the "strength" of each singularity. The connection to real integral evaluation (the payoff of the entire complex analysis playlist) is almost never shown as a visual story.

**Techniques to adopt:**
- Visualize the theorem: contour with multiple singularities inside, each contributing 2πi × residue
- Show residue computation methods for different pole orders
- Demonstrate evaluating a REAL integral using the Residue Theorem (the payoff!)
- Make this a satisfying finale to the Complex Analysis playlist

**Techniques to avoid:**
- Stating the theorem without geometric motivation
- Only showing simple examples — include a real integral application
- Not connecting back to the journey: CIF → estimates → Liouville → FTA → Laurent → Residues
- Ending without a playlist recap

## Scene Plan

### Scene 1: Hook — "The Most Practical Theorem" (~50s)
- "We've built an incredible machinery: Cauchy's Integral Formula, Laurent series, residues"
- "The Residue Theorem brings it all together into the most PRACTICAL tool in complex analysis"
- Visual: a contour with three singularities inside, each labeled with its residue
- "The integral = 2πi × (sum of all residues inside) — that's it!"
- Bridge: "This theorem lets us evaluate integrals that would be impossible otherwise"

### Scene 2: The Theorem Statement (~55s)
- Theorem (Residue Theorem): If f is analytic on and inside a simple closed contour γ, except for finitely many isolated singularities a₁, a₂, ..., aₙ inside γ, then ∮_γ f(z) dz = 2πi Σ Res(f, aₖ)
- Visual: formula box with color coding
- Key: we only need to know the residues at the singularities inside the contour
- "We don't need to parameterize anything. Just find the singularities inside, compute their residues, sum, multiply by 2πi"

### Scene 3: Computing Residues at Poles (~60s)
- Method 1: Simple pole at a. Res(f, a) = lim_{z→a} (z-a) f(z)
- Method 2: Pole of order k at a. Res(f, a) = 1/(k-1)! lim_{z→a} d^{k-1}/dz^{k-1} [(z-a)^k f(z)]
- Example: f(z) = e^z / (z-1)(z-2). Singularities at z=1 and z=2 (both simple poles).
  - Res(f, 1) = e^1/(1-2) = -e
  - Res(f, 2) = e^2/(2-1) = e^2
- Visual: computation steps color-coded

### Scene 4: Example — Evaluating a Contour Integral (~55s)
- Evaluate ∮_γ e^z / ((z-1)(z-2)) dz where γ is |z| = 3
- Both z=1 and z=2 are inside |z| = 3
- By Residue Theorem: integral = 2πi × (Res(f,1) + Res(f,2)) = 2πi × (-e + e^2) = 2πi(e^2 - e)
- Visual: circle with both singularities, residues labeled, sum computed
- "No parameterization, no messy trig integrals — just algebra!"

### Scene 5: Application to Real Integrals (~60s)
- THE PAYOFF: use complex analysis to evaluate real integrals
- Example: ∫_{-∞}^{∞} 1/(x²+1) dx = π
- Method: consider ∮_γ 1/(z²+1) dz where γ is the semicircle in the upper half-plane
- Singularities: z = i and z = -i. Only z = i is inside the contour.
- Res(1/(z²+1), i) = 1/(2i)
- By Residue Theorem: integral = 2πi × 1/(2i) = π
- Visual: semicircle contour, singularity at z=i, computation
- "An integral that normally requires arctangent substitution, solved by finding one residue!"

### Scene 6: Playlist Recap and Finale (~50s)
- Visual timeline of the entire Complex Analysis playlist:
  - Videos 126-128: Complex numbers, functions, limits
  - Video 129-130: Differentiation and integration
  - Video 131: Cauchy's Theorem (closed integrals vanish)
  - Video 132: CIF (boundary determines interior)
  - Video 133: Consequences (Liouville, FTA)
  - Video 134-135: Taylor and Laurent series
  - Video 136: Residue Theorem (the practical payoff)
- "From complex numbers to evaluating impossible integrals — that's the power of complex analysis"
- Outro with playlist complete marker

## Color Coding
- PRIMARY (#5BC0EB): contours, paths, geometric objects
- SECONDARY (#7BC950): analytic functions, function values
- ACCENT (#FFD166): theorem statements, the Residue Theorem, 2πi
- RED (#EF476F): singularities, residues, poles
- DIM (#6B6B8D): computation steps, labels, secondary information
