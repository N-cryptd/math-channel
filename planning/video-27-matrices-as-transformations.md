# Video 27: Matrices as Transformations
**Playlist:** Linear Algebra (Video 3 of 16)
**Est. Duration:** 12-15 minutes
**Status:** PLANNING

## Competitive Analysis References
- 3B1B Chapter 3 (10/10 across all dimensions) — grid morphing visual, basis-vector-tracking framework
- Khan Academy linear transformations — formal linearity conditions, multi-dimensional cases
- Dr. Trefor Bazett — unit square visualization, balance of formal and visual

## Scenes

### Scene 1: Hook + ChannelIntro (duration ~15s)
- ChannelIntro: "Matrices as Transformations" / "Linear Algebra"
- Teaser question: "What does a matrix actually DO?"

### Scene 2: What is a Transformation? (duration ~90s)
- A transformation is a function from R² to R²: takes every point, moves it somewhere new
- Visual: show a grid of dots, then animate them all shifting simultaneously
- Key insight: we think of it as moving the entire space, not just individual points
- Subcaption: "A transformation is a function that takes every point in space and moves it somewhere new."

### Scene 3: Linear vs Non-Linear (duration ~60s)
- Show a LINEAR transformation: grid lines stay straight, evenly spaced, origin stays fixed
- Show a NON-LINEAR transformation: grid warps, curves, origin may move
- The two rules of linearity:
  1. Grid lines remain straight and evenly spaced
  2. The origin stays in place
- Subcaption: "Linear transformations have two rules: they keep grid lines straight and evenly spaced, and they keep the origin fixed."

### Scene 4: Following the Basis Vectors (duration ~90s)
- THE key visual: animate i-hat and j-hat moving under a transformation
- i-hat (PRIMARY) lands at new position, j-hat (SECONDARY) lands at new position
- Show that knowing where i-hat and j-hat go determines EVERYTHING
- Any vector v = a·i-hat + b·j-hat transforms to a·T(i-hat) + b·T(j-hat)
- This is because the transformation is LINEAR (preserves addition and scaling)
- Subcaption: "Because the transformation is linear, knowing where i-hat and j-hat land tells us where EVERY vector goes."

### Scene 5: The Matrix Encodes the Transformation (duration ~90s)
- If i-hat lands at (a, c) and j-hat lands at (b, d), the matrix is:
  ```
  | a  b |
  | c  d |
  ```
- The FIRST column is where i-hat goes, the SECOND column is where j-hat goes
- Visual: show the matrix filling in as i-hat and j-hat move to their new positions
- Subcaption: "The matrix is just a record: the first column says where i-hat goes, the second column says where j-hat goes."

### Scene 6: Example — Rotation (duration ~120s)
- Rotation by 90°: i-hat goes from (1,0) to (0,1), j-hat goes from (0,1) to (-1,0)
- Matrix: | 0  -1 |
           | 1   0 |
- Visual: animate the entire grid rotating 90° with smooth morph
- Show several vectors (not just basis) landing correctly
- Verify: apply matrix to vector (2, 1) → (−1, 2). Show geometrically that this is correct.
- Subcaption: "A 90-degree rotation sends i-hat to j-hat and j-hat to negative i-hat. So our matrix has those as its columns."

### Scene 7: Example — Shear (duration ~90s)
- Shear transformation: i-hat stays at (1,0), j-hat goes to (1,1)
- Matrix: | 1  1 |
           | 0  1 |
- Visual: animate the grid shearing — x-axis stays, everything else slides right proportional to y
- Show unit square → parallelogram
- Subcaption: "A shear pushes everything horizontally by an amount proportional to its height. I-hat stays put, but j-hat shifts one unit to the right."

### Scene 8: Matrix-Vector Multiplication = Applying the Transformation (duration ~90s)
- THE climactic reveal: when you multiply a matrix by a vector, you are applying the transformation to that vector
- A·v = a₁·(column 1) + a₂·(column 2)
- Visual: decompose vector into components, scale each matrix column, add them up
- Connect back to linear combinations from Video 26!
- Subcaption: "Matrix-vector multiplication is really just: scale the first column by the vector's x-component, scale the second column by the y-component, and add them. You're computing where that vector lands under the transformation."

### Scene 9: Formal Properties (duration ~60s)
- T(u + v) = T(u) + T(v) — preserves addition
- T(c·v) = c·T(v) — preserves scaling
- These are what make the basis-vector tracking work
- Brief mention: matrices can be any size, not just 2×2 (teaser for higher dimensions)
- Subcaption: "These two properties, preserving addition and scaling, are what guarantee that the basis vectors determine everything."

### Scene 10: Summary + Outro (duration ~30s)
- Key takeaways:
  1. A matrix represents a linear transformation of space
  2. Column 1 = where i-hat goes, Column 2 = where j-hat goes
  3. Matrix-vector multiplication = applying the transformation
  4. Linear transformations preserve lines and the origin
- Teaser: "What happens when we apply two transformations in a row? That's matrix multiplication — coming up next."
- ChannelOutro with next video: "Matrix Multiplication" / "Linear Algebra"

## Key Visual Elements
- 2D NumberPlane with animated grid morphing (using Manim's `apply_matrix` or manual animation)
- Color-coded basis vectors: PRIMARY (#58C4DD) for i-hat, SECONDARY (#83C167) for j-hat
- Unit square → parallelogram transformation visual
- Smooth continuous grid transformation animation

## Mathematical Content
- Function notation: T: R² → R²
- Matrix notation: 2×2 matrix with column interpretation
- Matrix-vector multiplication as linear combination of columns
- Linearity conditions: T(u+v) = T(u) + T(v), T(cv) = cT(v)
- Examples: 90° rotation, shear transformation

## Prerequisites from Earlier Videos
- Video 25: What is a Vector? (basis vectors, components)
- Video 26: Linear Combinations and Span (linear combinations, scaling, adding)
