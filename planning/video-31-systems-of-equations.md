# Video 31: Systems of Equations (Matrix Form)

**Playlist:** Linear Algebra (Video 7 of 16)
**Duration target:** 10-12 minutes
**Status:** PLAN COMPLETE

## Competitive Analysis Reference
Analysis attempted — youtubei.js returned minimal data due to innerTube API changes. Proceeding with known competitor approaches:

Key insights from prior analysis of 3B1B, Khan Academy, Dr. Trefor Bazett:
- **3B1B** (Essence of LA): Geometric first — shows intersecting lines/planes, then connects to matrix notation. Visual intuition: each equation = a plane; solution = intersection point(s).
- **Khan Academy**: Systematic approach — Ax=b, augmented matrix, classification (unique/infinite/none). Strong on worked examples.
- **Dr. Trefor Bazett**: Clean bridge from traditional algebra to matrix form. Good on existence/uniqueness theorem.

Our approach: **Geometric motivation → Matrix notation → Classification → Connection to column space → Worked example → Summary.** We'll emphasize the visual intuition (3B1B style) while maintaining systematic rigor (Khan style), and explicitly connect to column space and invertibility from Video 30.

## Scene Breakdown

### Scene 1: Hook + Intro (30s)
- **Content budget:** intro animation + motivation question
- **Narration:** "Every system of linear equations hides a geometric secret. Lines intersecting, planes colliding, dimensions collapsing. Today we learn how matrices reveal what your equations are really doing."
- Play channel intro
- Show two lines intersecting → ask "what does this have to do with matrices?"
- **Items:** intersecting lines visual, question text (2 items)

### Scene 2: From Equations to Matrices (2 min)
- **Content budget:** system of equations, matrix A, vector x, vector b (4 items)
- **Narration:** "Consider a simple system: 2x plus y equals 5, and x minus 3y equals 1. We can write this as a matrix equation A times x equals b, where A holds the coefficients, x holds the variables, and b holds the constants."
- Show a 2×2 system of equations
- Animate the transformation into Ax=b form
- Color-code: A (PRIMARY), x (SECONDARY), b (ACCENT)
- **Items:** equations text, A matrix, x vector, b vector (4 items)

### Scene 3: What Does Ax=b Really Mean? (2 min)
- **Content budget:** grid, transformed grid, b vector, equation label (4 items)
- **Narration:** "Think about what A times x equals b is really saying. The matrix A transforms the vector x into the vector b. So solving this system means finding which vector, when transformed by A, lands exactly on b."
- Show the column picture: columns of A scaled by x₁ and x₂
- Show the row picture: each equation defines a line, solution is intersection
- Connect: "Column picture — A times x is a linear combination of columns of A"
- **Items:** columns visualization, b point, equation text (3-4 items)

### Scene 4: Classification — Unique, Infinite, or None (2.5 min)
- **Content budget:** 3 small diagrams side by side with labels (4 items)
- **Narration:** "Not every system has a solution. There are three possibilities. One unique solution — the lines intersect at exactly one point. Infinitely many solutions — the lines are the same, every point works. No solution — the lines are parallel, they never meet."
- Show three cases with geometric visuals:
  1. Unique: two lines crossing (det(A) ≠ 0)
  2. Infinite: two lines overlapping
  3. None: two parallel lines
- Connect to determinant: unique solution ⟺ det(A) ≠ 0
- **Items:** 3 case visuals, classification label (4 items)

### Scene 5: Connection to Column Space (2 min)
- **Content budget:** grid with column vectors, b point, column space label, verdict (4 items)
- **Narration:** "Here is a powerful insight. A times x equals b has a solution if and only if b lives in the column space of A. The column space is the set of all possible outputs of the transformation A."
- Show column space as a shaded region
- b inside column space → solution exists
- b outside column space → no solution
- Connect to invertibility: square + det ≠ 0 → column space = all of R² → always solvable
- **Items:** column space visualization, b vector, verdict label (3-4 items)

### Scene 6: Worked Example (2 min)
- **Content budget:** system, matrix form, solution computation, verification (4 items)
- **Narration:** "Let's solve a concrete system. Take 3x plus 2y equals 8, and x minus y equals 1. The coefficient matrix is A equals [[3, 2], [1, -1]]. Since det A is negative 5, which is nonzero, a unique solution exists."
- Step-by-step solution using matrix inverse: x = A⁻¹b
- Verify: plug solution back into original equations
- **Items:** system, matrix, solution steps, verification (4 items)

### Scene 7: Summary + Outro (1 min)
- **Content budget:** key takeaways list, next video preview (4 items)
- **Narration:** "To summarize. Every linear system can be written as A x equals b. This means: find x such that A transforms x into b. A solution exists if b is in the column space. For square matrices, det nonzero guarantees exactly one solution. Next time, we'll learn how to systematically solve any system using row reduction."
- Key formulas: Ax = b, x = A⁻¹b (when invertible), classification
- Play outro
- **Items:** summary bullets, next video teaser (3-4 items)
