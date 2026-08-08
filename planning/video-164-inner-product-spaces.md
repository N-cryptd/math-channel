# Video 164: Inner Product Spaces

**Playlist:** Functional Analysis (Video 3 of 12)
**Class:** Video164_InnerProductSpaces
**File:** scripts/graduate/video-164-inner-product-spaces.py
**Estimated duration:** ~600s (10 min)
**Status:** plan_written

## Topics
1. Opening hook: what does a norm NOT give you? (angles, orthogonality, projection)
2. The inner product adds geometric structure to a normed space
3. Formal definition: inner product axioms (symmetry/linearity/positive-definiteness)
4. How the inner product induces a norm: ||x|| = sqrt(<x,x>)
5. Examples: R^n with dot product, L^2[a,b] function space, sequence space l^2
6. Cauchy-Schwarz inequality (visual proof via projection)
7. Orthogonality: perpendicular vectors, orthogonal complements
8. Orthogonal projection: best approximation theorem
9. Gram-Schmidt in function spaces: Legendre polynomials as example
10. Teaser: completeness + inner product = Hilbert space (next video)
11. Summary + what's next

## Prerequisites
- Video 162 (Normed Spaces) — complete
- Video 163 (Banach Spaces) — complete
- Linear Algebra Videos 37-38 (Inner Product Spaces, Orthogonality & Gram-Schmidt) — complete
- Measure Theory Video 158 (L^p Spaces) — complete

## Competitive Analysis
Full analysis in channel-analysis/improvements.md [2026-08-07] Inner Product Spaces entry.
Detailed analysis: channel-analysis/analysis-164-inner-product.md

Key takeaways:
- **Market gap:** No high-quality animated video covers inner product spaces at graduate level.
- **Technique to adopt:** Application-driven opening (Steve Brunton's data science framing). Show what inner product ADDS beyond a norm.
- **Technique to adopt:** Visual proof of Cauchy-Schwarz via projection geometry (3B1B style).
- **Technique to avoid:** Definition-first without motivation. Chalkboard aesthetic.
- **Key differentiator:** Function inner products as the graduate leap beyond LA video 37.

## Scene Plan

### Scene 1: Hook — What a Norm Misses (45s)
**Content budget:** Intro + title + 2-3 text items
- Play intro: "Inner Product Spaces", "Functional Analysis"
- "A norm tells you the LENGTH of a vector"
- "But what about the ANGLE between two vectors?"
- "What does it mean for two functions to be PERPENDICULAR?"
- "Inner product spaces give us angles, orthogonality, and projection"
- Reference: the "ladder" from Video 162 (inner product → normed → metric)

### Scene 2: Formal Definition (55s)
**Content budget:** Title + definition box + 3 axioms (progressive)
- Definition: an inner product on V is a map <.,.> : V x V → R (or C) satisfying:
  1. Symmetry / Conjugate symmetry: <x,y> = <y,x> (or conj)
  2. Linearity in first argument: <ax + by, z> = a<x,z> + b<y,z>
  3. Positive-definiteness: <x,x> >= 0, equality iff x = 0
- Color-code each axiom (PRIMARY, SECONDARY, ACCENT)

### Scene 3: Inner Product Induces a Norm (50s)
**Content budget:** Title + formula + 2 items
- Key formula: ||x|| = sqrt(<x,x>)
- Verify the norm axioms from inner product properties
- Not every norm comes from an inner product! (L1 and L-infinity don't)
- Visual: show ||x||^2 = <x,x> as the bridge concept

### Scene 4: Examples (65s)
**Content budget:** Title + 3 examples (progressive reveal)
- Example 1: R^n with dot product <x,y> = sum(x_i * y_i) — familiar from LA
- Example 2: L^2[a,b] with <f,g> = integral_a^b f(x)g(x) dx — the graduate leap
- Example 3: l^2 (square-summable sequences) <a,b> = sum(a_n * b_n) — bridge between finite/infinite
- For each: show the norm it induces

### Scene 5: Cauchy-Schwarz Inequality (70s)
**Content budget:** Title + formula + visual proof
- Statement: |<x,y>| <= ||x|| ||y||
- Visual proof: project y onto x, the projection component <= ||y||
- The angle formula: cos(theta) = <x,y> / (||x|| ||y||) — only when the norm comes from an inner product!
- Show equality case: x and y are parallel

### Scene 6: Orthogonality and Complements (55s)
**Content budget:** Title + 2-3 items
- Definition: x ⊥ y iff <x,y> = 0
- Orthogonal complement: M⊥ = {x : <x,m> = 0 for all m in M}
- Pythagorean theorem: if x ⊥ y, then ||x+y||^2 = ||x||^2 + ||y||^2
- Visual: right triangle with perpendicular vectors

### Scene 7: Orthogonal Projection (55s)
**Content budget:** Title + formula + 2 items
- Formula: proj_M(x) = sum(<x,e_i> e_i) for orthonormal basis {e_i}
- Best approximation: ||x - proj_M(x)|| <= ||x - m|| for all m in M
- Connection to least squares, Fourier series, PCA (brief application teaser)

### Scene 8: Gram-Schmidt in Function Spaces (60s)
**Content budget:** Title + process steps + example
- Brief recap: Gram-Schmidt builds an orthonormal basis from any basis
- NEW content: apply Gram-Schmidt to {1, x, x^2, ...} in L^2[-1,1]
- Result: Legendre polynomials P_0(x)=1, P_1(x)=x, P_2(x)=(3x^2-1)/2, ...
- Visual: show first 3 Legendre polynomials as curves

### Scene 9: Summary + Outro (40s)
**Content budget:** Summary items + outro
- Recap: inner product gives angles, orthogonality, projection
- Cauchy-Schwarz is the foundational inequality
- Not every norm comes from an inner product
- Function spaces like L^2 are inner product spaces
- Preview: Hilbert Spaces = complete inner product spaces (Video 165)

## Visual Design Notes
- Use the "ladder" visualization from Video 162: inner product sits ABOVE normed
- Color-code axioms consistently (PRIMARY for symmetry, SECONDARY for linearity, ACCENT for positive-definiteness)
- Function inner product: show integral symbol prominently, then animate it "collapsing" to the dot product formula for R^n (finite case)
- Cauchy-Schwarz: geometric projection diagram with colored vectors
- Legendre polynomials: plot as smooth curves with color coding matching the palette
