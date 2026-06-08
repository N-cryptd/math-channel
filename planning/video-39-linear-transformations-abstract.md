# Video 39: Linear Transformations (Abstract)

**Playlist:** Linear Algebra (Undergraduate)
**Video #15 of 16 in playlist, #39 overall**
**Target Duration:** 10-13 min
**Status:** Plan

## Competitive Analysis Notes
- Analysis based on domain knowledge (web search deferred).
- **3B1B (Essence of Linear Algebra Ch.3):** Introduces linear transformations visually — "functions that preserve lines and the origin." Beautiful grid deformation animations. Key insight: a linear transformation is fully determined by where it sends the basis vectors.
- **Khan Academy:** More formal — defines T(v+w) = T(v) + T(w) and T(cv) = cT(v), then shows matrix representation. Proofs of linearity properties.
- **Our approach:** Start with the intuitive visual (functions that preserve grid lines), give the formal axioms, show the matrix connection (every matrix IS a linear transformation), then explore kernel and image (connecting back to null space and column space from Videos 33-34).

## Scene Plan

### Scene 1: Hook + Channel Intro (~15s)
- Motivation: "We've used matrices to transform vectors. But what IS a transformation, really?"
- Content: Channel intro.

### Scene 2: What is a Function? (~30s)
- Brief recap: a function maps inputs to outputs.
- But some functions are special — they preserve structure.
- Content: simple function diagram f: V → W.

### Scene 3: The Visual Intuition (~50s)
- Grid of points in R² — apply a transformation — grid lines stay lines, origin stays fixed.
- Contrast: non-linear transformations (curves, translations).
- Key rule: lines map to lines, origin maps to origin.
- Content: grid visual + rules.

### Scene 4: Formal Definition (~60s)
- T: V → W is linear if:
  1. T(u + v) = T(u) + T(v)  (additivity)
  2. T(cu) = cT(u)  (homogeneity)
- Combined: T(cu + dv) = cT(u) + dT(v)
- Content: formal definition with notation.

### Scene 5: Matrix Connection (~60s)
- Every m×n matrix A defines T(x) = Ax — this IS a linear transformation.
- Conversely, every linear transformation T: Rⁿ → Rᵐ can be written as T(x) = Ax for some matrix A.
- The columns of A are T(e₁), T(e₂), ..., T(eₙ).
- Content: matrix equation, column interpretation.

### Scene 6: Kernel and Image (~50s)
- Kernel: ker(T) = {v ∈ V : T(v) = 0} — same as null space!
- Image: im(T) = {T(v) : v ∈ V} — same as column space!
- Dimension theorem: dim(ker T) + dim(im T) = dim V — rank-nullity!
- Content: definitions + connection to earlier videos.

### Scene 7: Examples (~60s)
- Example 1: Projection onto x-axis (kernel is y-axis, image is x-axis).
- Example 2: Rotation by 90° (kernel is {0}, image is all of R²).
- Example 3: Zero transformation (kernel = all of R², image = {0}).
- Content: visual examples with kernel/image identified.

### Scene 8: Summary + Outro (~20s)
- Key takeaways, preview of SVD (Video 40).
- Content: summary bullets, outro with next video card.

## Key Formulas
1. T(u + v) = T(u) + T(v)
2. T(cu) = cT(u)
3. T(x) = Ax (matrix form)
4. ker(T) = Null(A), im(T) = Col(A)
5. dim(ker T) + dim(im T) = dim V
