# Video 135: Laurent Series

**Playlist:** Complex Analysis (Video 12 of 13)
**Class:** Video135_LaurentSeries
**Script:** scripts/undergraduate/video-135-laurent-series.py
**Est. Duration:** 12 min
**Status:** PLAN

## Competitive Analysis Summary

[Analysis based on known competitor content.]

- **3Blue1Brown:** Has NOT produced a dedicated Laurent series video. His Fourier series visualization (Chapter on "But what is a Fourier series?") is the closest analog — showing decomposition into frequency components. The idea of splitting a function into positive and negative frequency parts directly parallels the principal and analytic parts of a Laurent series.
- **Faculty of Khan:** Has a video on Laurent series. Whiteboard style, covers the formula, annulus of convergence, and classification of singularities. Clean but no animated visualization.
- **Michael Penn:** Has Laurent series computation videos. Rapid-fire algebra, finding principal parts and residues.
- **Dr. Peyam:** Lecture-style video on Laurent series. Traditional theorem-proof format.
- **BriTheMathGuy:** Manim-based but fast-paced.
- **The Bright Side of Mathematics:** Complex Analysis series includes Laurent series coverage.

**Market gap:** No video visually explains the geometric meaning of a Laurent series — splitting a function into a "nice" analytic part and a "singular" principal part, each converging in an annulus. The visualization of an annulus of convergence (two concentric circles with the function converging in between) is almost never animated.

**Techniques to adopt:**
- Visualize the annulus of convergence: inner circle from singularity, outer circle to next singularity
- Color-code the two parts: analytic part (positive powers) vs principal part (negative powers)
- Animate the classification: show how the principal part reveals the singularity type
- Show residue as the coefficient of 1/(z-a) — visually highlight it in the series

**Techniques to avoid:**
- Stating the formula without showing where it comes from
- Dense coefficient computation for every example
- Not clearly distinguishing the analytic and principal parts
- Skipping the connection to residues (preview of next video)

## Scene Plan

### Scene 1: Hook — "What About Singularities?" (~50s)
- Recap from Video 134: Taylor series converge in disks, up to the nearest singularity
- "But what if we want to represent a function NEAR a singularity? Taylor series fail here"
- "Laurent series generalize Taylor series by including negative powers — they converge in annuli, not disks"
- Visual: a disk with a hole in the middle (annulus) — the singularity is at the center
- Bridge: "Laurent series are the tool that unlocks residue theory"

### Scene 2: The Laurent Series Formula (~55s)
- Theorem: if f is analytic in the annulus r < |z-a| < R, then f(z) = Σ_{n=-∞}^{∞} c_n (z-a)^n
- Split: f(z) = Σ_{n=0}^{∞} c_n (z-a)^n + Σ_{n=1}^{∞} c_{-n} (z-a)^{-n}
- First sum: the "analytic part" (positive powers) — converges for |z-a| < R
- Second sum: the "principal part" (negative powers) — converges for |z-a| > r
- Visual: formula box with the two parts color-coded differently
- Coefficients from CIF: c_n = 1/(2πi) ∮ f(z)/(z-a)^{n+1} dz (same formula for all n, including negative!)

### Scene 3: The Annulus of Convergence (~55s)
- Visual: two concentric circles — inner radius r, outer radius R
- Inner boundary: determined by the singularity at a
- Outer boundary: determined by the next nearest singularity
- Example: f(z) = 1/((z-1)(z-2)) expanded about z=0 — singularity at z=1, next at z=2
- Annulus: 1 < |z| < 2
- Visual: plane with circles at |z|=1 and |z|=2, colored annulus between them

### Scene 4: Classification of Singularities (~60s)
- Three types based on the principal part:
  1. Removable: no negative powers → just extend f analytically (e.g., sin(z)/z at z=0)
  2. Pole: finitely many negative powers → highest is (z-a)^{-k}, order k pole (e.g., 1/z^3 at z=0)
  3. Essential: infinitely many negative powers → truly wild behavior (e.g., e^{1/z} at z=0)
- Visual: three examples, each showing the principal part
- "The principal part IS the singularity — it tells you exactly what kind you have"

### Scene 5: The Residue (~50s)
- The residue of f at z=a is c_{-1}, the coefficient of 1/(z-a)
- Visual: highlight c_{-1} in the Laurent series
- "Why c_{-1} matters: it's the only term that contributes a nonzero integral around a"
- Visual: ∮ (z-a)^n dz = 0 for all n except n=-1, where it equals 2πi
- Teaser: "Next time we'll use residues to evaluate real integrals — this is one of the most powerful applications of complex analysis"

### Scene 6: Summary and Preview (~45s)
- Recap: Laurent series = analytic part + principal part
- Converge in annuli, determined by singularity locations
- Classification: removable / pole / essential
- Residue = c_{-1}, preview of residue theorem
- Outro

## Color Coding
- PRIMARY (#5BC0EB): convergence boundaries, annuli, geometric objects
- SECONDARY (#7BC950): analytic parts, positive powers, removable singularities
- ACCENT (#FFD166): theorem statements, key results, residue c_{-1}
- RED (#EF476F): singularities, principal parts, negative powers, essential singularities
- DIM (#6B6B8D): computation steps, labels, secondary information
