# Video 33: Null Space and Column Space

**Playlist:** Linear Algebra (Undergraduate)
**Video #9 of 16 in playlist, #33 overall**
**Target Duration:** 12–15 min
**Status:** Script

## Competitive Analysis Notes
- youtubei.js non-functional; analysis based on domain knowledge of 3B1B, Khan Academy, Dr. Trefor Bazett, and Professor Leonard approaches.
- **3B1B style:** Emphasizes geometric intuition — null space as the "squished" dimension, column space as the span of column vectors. Color-codes vectors heavily.
- **Trefor Bazett:** Walks through computational examples after definitions; uses matrix notation alongside geometric pictures.
- **Our approach:** Bridge the gap — start with geometric intuition (what gets mapped to zero? what can we reach?), then formal definitions with a computational example, then a visual summary.

## Scene Plan

### Scene 1: Hook + Channel Intro (~15s)
- **Narration:** "Last time we reduced matrices to row echelon form. But what does that reduction actually tell us about the matrix itself? Today we explore two fundamental subspaces hidden inside every matrix."
- **Content:** Channel intro animation. Brief recap of row reduction.
- **Budget:** Intro mobjects only.

### Scene 2: The Big Picture — What Gets Lost? (~30s)
- **Narration:** "Every matrix A defines a transformation from R^n to R^m. Two natural questions arise: (1) Which vectors get mapped to zero? And (2) Which vectors can we actually reach?"
- **Content:**
  - Text: "A maps R^n → R^m"
  - Text: "Question 1: What gets sent to zero?" (color: PRIMARY)
  - Text: "Question 2: What can we reach?" (color: SECONDARY)
- **Budget:** 3 items max.

### Scene 3: Null Space — Definition (~45s)
- **Narration:** "The null space of A, written Nul A, is the set of all vectors x such that Ax equals zero. These are the vectors that get completely annihilated by the transformation."
- **Content:**
  - Title: "Null Space (Kernel)"
  - Formula: Nul A = {x : Ax = 0}
  - Text: "All vectors mapped to the zero vector"
  - Text: "Subspace of R^n (the domain)"
- **Budget:** 4 items.

### Scene 4: Null Space — Finding It Computationally (~60s)
- **Narration:** "To find the null space, we solve Ax = 0 using row reduction. Consider this 3×3 matrix. After Gaussian elimination, we get this row echelon form. Setting the free variable z = t, we get x = t, y = -t, z = t. So the null space is all multiples of (1, -1, 1)."
- **Content:**
  - Matrix A (3×3)
  - RREF of A
  - Parametric solution: x = t(1, -1, 1)
  - Text: "Null space is a line through the origin"
- **Budget:** 4 items (show matrix, then replace with RREF, then show solution).

### Scene 5: Column Space — Definition (~45s)
- **Narration:** "The column space of A, written Col A, is the span of the column vectors of A. It is every vector b for which the system Ax = b has a solution."
- **Content:**
  - Title: "Column Space"
  - Formula: Col A = span{a₁, a₂, ..., aₙ}
  - Text: "All vectors we can reach via Ax = b"
  - Text: "Subspace of R^m (the codomain)"
- **Budget:** 4 items.

### Scene 6: Column Space — Finding It (~60s)
- **Narration:** "The column space is determined by the pivot columns of A. The pivot columns in the reduced matrix tell us which original columns form a basis. For our example, columns 1 and 2 are pivot columns."
- **Content:**
  - Original matrix A with column labels
  - RREF with pivots highlighted
  - Text: "Pivot columns 1 and 2 → basis of Col A"
  - Dimension: dim(Col A) = rank(A) = 2
- **Budget:** 4 items.

### Scene 7: Geometric Visualization (~60s)
- **Narration:** "Let us visualize both subspaces for our example. The null space is a line through the origin in R^3 — it is one-dimensional. The column space is a plane in R^3 — it is two-dimensional. Together, they reveal the structure of the transformation."
- **Content:**
  - 3D coordinate axes
  - Null space line (color: PRIMARY)
  - Column space plane (color: SECONDARY)
  - Labels for both subspaces
- **Budget:** 4 items (axes + line + plane + label).

### Scene 8: Key Relationships (~45s)
- **Narration:** "The null space and column space are connected by the Rank-Nullity Theorem: the dimension of the null space plus the dimension of the column space equals the number of columns. For our example: 1 plus 2 equals 3."
- **Content:**
  - Title: "Rank-Nullity Theorem"
  - Formula: dim(Nul A) + dim(Col A) = n
  - Example: 1 + 2 = 3 ✓
  - Text: "n = number of columns of A"
- **Budget:** 4 items.

### Scene 9: Summary + Outro (~20s)
- **Narration:** "To summarize: the null space captures what gets annihilated, the column space captures what we can reach, and together they satisfy the rank-nullity theorem. Next time we explore rank in depth."
- **Content:**
  - Summary bullets (progressive reveal)
  - Outro with channel branding
- **Budget:** Intro mobjects only.

## Key Formulas
1. Nul A = {x ∈ R^n : Ax = 0}
2. Col A = Span{a₁, a₂, ..., aₙ} where aᵢ are columns of A
3. Rank-Nullity Theorem: dim(Nul A) + dim(Col A) = n

## Example Matrix
A = [[1, 2, 1], [2, 4, 2], [1, 2, 3]]

RREF: [[1, 2, 0], [0, 0, 1], [0, 0, 0]]

Null space: x = t(-2, 1, 0) (setting free variable y = t, z = 0, then x = -2t)
Wait — let me recompute:
- Row 1: x + 2y = 0 → x = -2y
- Row 2: z = 0
- Free variable: y = t
- Null space: (-2t, t, 0) = t(-2, 1, 0)

Column space: pivot columns are 1 and 3 of A → basis is {(1,2,1), (1,2,3)}
dim(Nul A) = 1, dim(Col A) = 2, 1 + 2 = 3 = n ✓

## Style Notes
- Use PRIMARY (#5BC0EB) for null space, SECONDARY (#7BC950) for column space throughout
- In geometric visualization, use ThreeDScene for null space line and column space plane
- Keep narration concise — the previous videos had timing issues with too-long narration
