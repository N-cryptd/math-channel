# Video 133: Consequences of CIF

**Playlist:** Complex Analysis (Video 10 of 13)
**Class:** Video133_ConsequencesOfCIF
**Script:** scripts/undergraduate/video-133-consequences-of-cif.py
**Est. Duration:** 12 min
**Status:** PLAN

## Competitive Analysis Summary

[Analysis based on known competitor content.]

- **3Blue1Brown:** Has NOT produced dedicated videos on the Maximum Modulus Principle, Liouville's Theorem, or FTA proof via complex analysis. His "Taylor series" and "divergence/curl" visualizations provide the philosophical precedent: showing that constraints on local behavior have powerful global consequences.
- **Faculty of Khan:** Has videos on Liouville's theorem and FTA via complex analysis. Whiteboard style, covers the proof structure but lacks geometric visualization of WHY bounded entire functions must be constant.
- **Michael Penn:** Has a video proving FTA using Liouville's theorem. Rapid algebra, no visual animation of the key steps.
- **Dr. Peyam:** Lecture-style videos covering these topics. Traditional theorem-proof format.
- **BriTheMathGuy:** Manim-based but fast-paced, focuses on computation rather than the beautiful conceptual chain: CIF → Cauchy estimates → Liouville → FTA.
- **The Bright Side of Mathematics:** Complex Analysis series likely covers these topics with clean Manim style.

**Market gap:** No video visually traces the chain from CIF to its most famous corollaries. The conceptual arc — CIF gives bounds → bounded entire functions are constant (Liouville) → every polynomial has a root (FTA) — is beautiful but almost never animated as a connected story.

**Techniques to adopt:**
- Tell the story as a chain: CIF → Cauchy Estimates → Liouville → FTA, each flowing naturally from the last
- Visualize the Maximum Modulus Principle: show a function's modulus on a disk and demonstrate the maximum occurs on the boundary
- Animate the proof of Liouville: start with f entire + bounded, use Cauchy estimates to show f' ≡ 0
- Visualize the FTA proof: assume p(z) has no root, construct 1/p(z), show it's bounded, contradiction with Liouville

**Techniques to avoid:**
- Treating each theorem as isolated — the beauty is in the chain of implications
- Dense algebra without geometric context
- Skipping Cauchy Estimates (the bridge between CIF and Liouville)
- Not showing the FTA proof — it's the crowning achievement of this chain

## Scene Plan

### Scene 1: Hook — "From One Formula to Three Theorems" (~50s)
- Recap from Video 132: Cauchy's Integral Formula gives f(z0) from boundary data
- "But CIF is more than a computation tool — it's an engine that drives three of the most important results in all of mathematics"
- Visual: CIF formula in center, with three arrows branching out to: Maximum Modulus, Liouville, FTA
- Bridge: "Each of these follows from CIF, and each reveals something profound about analytic functions"

### Scene 2: The Cauchy Estimates (~55s)
- Theorem: If f is analytic on and inside a circle of radius R centered at z0, then |f^(n)(z0)| ≤ M * n! / R^n, where M = max |f(z)| on the circle
- Derivation from CIF: |f^(n)(z0)| = n!/(2π) * |∮ f(z)/(z-z0)^{n+1} dz| ≤ n!/(2π) * M/(R^{n+1}) * 2πR = n! * M / R^n
- Visual: formula box, then the inequality chain with color coding
- Emphasize: "This bounds derivatives in terms of the function's maximum on the boundary"

### Scene 3: Maximum Modulus Principle (~55s)
- Theorem: If f is analytic on a domain D and continuous on its closure, then |f| achieves its maximum on the boundary of D (not in the interior)
- Visual: a disk with |f(z)| displayed as color intensity — darkest at the boundary
- Proof idea: if |f| had a local maximum at an interior point, use Cauchy estimates to show f is constant
- Contrast with real-valued functions: sin(x) has interior max, but no non-constant analytic function can
- "Analytic functions don't have local extrema of |f| in the interior"

### Scene 4: Liouville's Theorem (~60s)
- Theorem: Every bounded entire function is constant
- Proof: Use Cauchy estimates. Let f be entire with |f(z)| ≤ M for all z. For any point z0 and any radius R: |f'(z0)| ≤ M/R. Since R can be arbitrarily large, f'(z0) = 0. This holds for all z0, so f is constant.
- Visual: a bounded function (stays within a horizontal band), then show R → ∞ making the bound → 0
- "The more room you give an entire function, the more constrained its derivative becomes"
- Key insight: "An entire function that doesn't grow must be flat"

### Scene 5: The Fundamental Theorem of Algebra (~65s)
- Theorem: Every non-constant polynomial with complex coefficients has at least one complex root
- Proof by contradiction: Suppose p(z) has no root. Then 1/p(z) is entire. Show 1/p(z) → 0 as |z| → ∞, so it's bounded. By Liouville, 1/p(z) is constant, so p(z) is constant — contradiction!
- Visual: the chain of logic as a flow diagram
- Key step: why 1/p(z) is bounded: p(z) ~ z^n for large |z|, so 1/p(z) ~ 1/z^n → 0
- "One of the oldest problems in mathematics, proved in three lines using complex analysis"

### Scene 6: The Big Picture (~50s)
- Visual: the full chain of implications: CIF → Cauchy Estimates → Maximum Modulus / Liouville → FTA
- Each step colored differently, arrows connecting them
- "This is the power of complex analysis: a single formula about integrals leads to the Fundamental Theorem of Algebra"
- Teaser: "Next time, we'll explore Taylor series in the complex plane — and discover they converge in perfect disks, unlike the real case"
- Outro

## Color Coding
- PRIMARY (#5BC0EB): contours, boundaries, geometric objects
- SECONDARY (#7BC950): analytic functions, function values, key results
- ACCENT (#FFD166): theorem statements, CIF formula, highlights
- RED (#EF476F): contradictions, vanishing terms, things that break
- DIM (#6B6B8D): computation steps, labels, secondary information
