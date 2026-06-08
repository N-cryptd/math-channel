# Video 28: Matrix Multiplication
**Playlist:** Linear Algebra (Video 4 of 16)
**Est. Duration:** 12-15 minutes
**Status:** PLANNING

## Competitive Analysis References
- **3B1B Chapter 4** (XkY2nUCgJcQ, ~6M views) — "Matrix multiplication as composition". 10/10 across dimensions. Key insight: frames matrix multiplication as composition of transformations rather than a mechanical process. Shows "apply transformation A, then transformation B" as the core concept. Animate the grid through two successive transformations.
- **Khan Academy** — Matrix multiplication as the standard "rows × columns" dot-product algorithm. More mechanical but thorough for computation. Good for teaching the algorithm but weaker on intuition.
- **Dr. Trefor Bazett** — Balances formal computation with visual interpretation. Uses the "column view" of multiplication to build intuition before showing the standard algorithm.

## Approach (synthesized from competitors)
Following 3B1B's intuition-first philosophy but adding more formal content than he provides:
1. Start with the **composition of transformations** idea (3B1B approach)
2. Show how applying transformation A then B leads to a single combined transformation
3. Derive the matrix multiplication formula FROM this geometric insight
4. THEN teach the standard algorithm (rows × columns) as the mechanical shortcut
5. Include a worked example with actual numbers
6. Show that matrix multiplication is NOT commutative (A·B ≠ B·A) with a visual demo

This ordering (intuition → derivation → algorithm) is our unique contribution — 3B1B stops too early on the algorithm, and KA starts too early with the algorithm.

## Scenes

### Scene 1: Hook + ChannelIntro (duration ~15s)
- ChannelIntro: "Matrix Multiplication" / "Linear Algebra"
- Teaser: "What happens when you apply two transformations, one after another?"

### Scene 2: Composition of Transformations (duration ~90s)
- Review: a matrix represents a transformation of space
- Key question: if we apply transformation A, then transformation B, what is the combined effect?
- Visual: start with a grid, apply first transformation (e.g., rotation), then apply second (e.g., shear)
- The result is a SINGLE transformation that does both at once
- This is what matrix multiplication means: composing transformations

### Scene 3: Tracking the Basis Vectors (duration ~90s)
- To find the combined matrix, track where i-hat and j-hat go through BOTH transformations
- After transformation A: i-hat → A's first column, j-hat → A's second column
- Then transformation B is applied to those results
- The result gives us the columns of the combined matrix B·A
- Visual: animate basis vectors through two successive transformations step by step

### Scene 4: Deriving the Formula (duration ~90s)
- Let A = [[a, b], [c, d]], B = [[e, f], [g, h]]
- B·A's first column = B × (first column of A) = B × [a, c]
  = [a·e + c·g, a·f + c·h]
- B·A's second column = B × (second column of A) = B × [b, d]
  = [b·e + d·g, b·f + d·h]
- Key insight: each column of the result is a linear combination of B's columns, weighted by A's corresponding column
- Show the full matrix multiplication formula emerging from this

### Scene 5: The Standard Algorithm (duration ~90s)
- Now present the familiar "row × column" algorithm
- (B·A)_{ij} = row i of B · column j of A
- Visual: highlight a row and a column, show their dot product filling in one entry
- Connect back: this IS the same as the composition we derived — just organized differently
- Note: we read LEFT to RIGHT (B first, then A) because B is applied SECOND

### Scene 6: Worked Example (duration ~120s)
- Concrete example:
  - A = [[1, 2], [3, 4]] (a specific transformation)
  - B = [[0, -1], [1, 0]] (90° rotation)
  - Compute B·A step by step
  - B·A = [[-3, -4], [1, 2]]
- Show the geometric interpretation: first apply A, then rotate by 90°
- Visual: grid → transformation A → rotation → final result

### Scene 7: Non-Commutativity (duration ~90s)
- A·B ≠ B·A in general!
- Compute A·B with the same matrices: A·B = [[2, -1], [4, -3]]
- Compare B·A = [[-3, -4], [1, 2]] with A·B = [[2, -1], [4, -3]]
- Visual: show two different grids (B·A vs A·B) to demonstrate they produce different transformations
- Intuition: order matters — rotating THEN shearing ≠ shearing THEN rotating
- This is because function composition is not commutative

### Scene 8: Properties Summary (duration ~60s)
- Matrix multiplication is associative: (A·B)·C = A·(B·C)
- NOT commutative: A·B ≠ B·A in general
- Identity matrix: A·I = I·A = A
- Dimensions: (m×n) · (n×p) = (m×p) — the inner dimensions must match
- Brief teaser: these properties will be crucial when we study determinants and inverses

### Scene 9: Summary + Outro (duration ~30s)
- Key takeaways:
  1. Matrix multiplication = composition of transformations
  2. The formula comes from tracking basis vectors through both transformations
  3. The standard algorithm (row × column) is the mechanical way to compute it
  4. Order matters! Matrix multiplication is NOT commutative
- Teaser: "Next time, we will learn about determinants — a single number that tells you how a transformation changes area."
- ChannelOutro with next video: "Determinants" / "Linear Algebra"

## Key Visual Elements
- 2D NumberPlane with two successive grid transformations (animated step by step)
- Color-coded basis vectors: PRIMARY for i-hat, SECONDARY for j-hat
- Animated dot-product computation (highlighting row and column)
- Side-by-side comparison grid for A·B vs B·A
- Matrix multiplication formula building up progressively

## Mathematical Content
- Composition of linear transformations: T_B ∘ T_A
- Matrix multiplication formula: (BA)_{ij} = Σ_k b_{ik} · a_{kj}
- Column interpretation: each column of BA is B applied to the corresponding column of A
- Row-column algorithm for computation
- Non-commutativity with counterexample
- Associativity and identity properties
- Dimension compatibility: (m×n)·(n×p) → (m×p)

## Prerequisites from Earlier Videos
- Video 25: Vectors (basis vectors, components)
- Video 26: Linear combinations and span
- Video 27: Matrices as transformations (matrix-vector multiplication)
