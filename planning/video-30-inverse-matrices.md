# Video 30: Inverse Matrices

**Playlist:** Linear Algebra (Video 6 of 16)
**Duration target:** 12-15 minutes
**Status:** PLAN COMPLETE

## Competitive Analysis Reference
Based on analysis of 3B1B Chapter 7 (3.7M views), Khan Academy, and Dr. Trefor Bazett.
See `channel-analysis/improvements.md` — Video 30 section.

Key insight from 3B1B: inverse = transformation that undoes the original.
Our approach: geometric intuition first → invertibility conditions → 2×2 formula derivation → worked example → augmented matrix method → properties.

## Scene Breakdown

### Scene 1: Hook + Intro (30s)
- **Content budget:** intro animation + question
- **Narration:** "If every matrix is a transformation, can every transformation be undone? The answer is no — and understanding when you CAN undo a transformation is one of the most powerful ideas in linear algebra."
- Play channel intro
- Show a grid being transformed (e.g., a shear or rotation) → ask "can we reverse this?"
- **Items:** transformed grid visual, question text (2 items)

### Scene 2: The Inverse as "Undoing" (2 min)
- **Content budget:** plane, transformed plane, reversed plane, label (4 items)
- **Narration:** "The inverse of a matrix A, written A inverse, is the transformation that exactly reverses A. Apply A, then apply A inverse, and you get back to where you started."
- Show a 2D grid with a rotation transformation applied
- Then show the inverse (reverse rotation) bringing the grid back
- Key formula: A⁻¹ · A = I (and A · A⁻¹ = I)
- **Items:** plane, transformed plane, restored plane, identity formula (4 items)

### Scene 3: When Does the Inverse Exist? (2 min)
- **Content budget:** two grids side by side, labels, condition text (4 items)
- **Narration:** "So when does A inverse exist? The answer connects directly to the determinant. If det of A is zero, the transformation squishes space — and you cannot undo that. Information is lost."
- Show det ≠ 0 case: full-rank transformation, inverse exists
- Show det = 0 case: 2D collapses to a line, no inverse
- Key condition: det(A) ≠ 0 ⟺ A⁻¹ exists
- **Items:** two grids, condition labels (3-4 items)

### Scene 4: The 2×2 Formula Derivation (2.5 min)
- **Content budget:** matrix, system of equations, solved entries, formula box (4 items)
- **Narration:** "For a 2 by 2 matrix, we can derive A inverse explicitly. We want A times A inverse to equal the identity matrix. Let A inverse have unknown entries w, x, y, z. Multiplying out gives us four equations."
- Show A · A⁻¹ = I with unknown entries
- Solve the system step by step
- Arrive at the formula: A⁻¹ = (1/det) · [[d, -b], [-c, a]]
- Highlight that det appears in the denominator — confirming det ≠ 0 is required
- **Items:** matrix, equation system, solution, formula box (4 items)

### Scene 5: Worked Example (2 min)
- **Content budget:** matrix, computation steps, result, verification (4 items)
- **Narration:** "Let's find the inverse of a concrete matrix. Take A = [[2, 1], [5, 3]]. First, compute the determinant: 2 times 3 minus 1 times 5 equals 1. Since det is nonzero, the inverse exists."
- Compute det(A) = 1
- Apply formula: A⁻¹ = (1/1) · [[3, -1], [-5, 2]] = [[3, -1], [-5, 2]]
- Verify: A · A⁻¹ = I (quick check)
- **Items:** matrix, det computation, inverse matrix, identity verification (4 items)

### Scene 6: The Augmented Matrix Method (2 min)
- **Content budget:** augmented matrix, row operations, result (4 items)
- **Narration:** "For larger matrices, there's a systematic method. Write the matrix A next to the identity matrix, forming an augmented matrix. Apply row operations to turn the left side into I. The right side becomes A inverse."
- Show [A | I] → [I | A⁻¹]
- Brief demonstration with a simple example
- Mention this scales to 3×3 and larger matrices
- **Items:** augmented matrix, row operation arrows, result (3-4 items)

### Scene 7: Key Properties (1.5 min)
- **Content budget:** property list items revealed progressively (3-5 items)
- **Narration:** "Inverse matrices have elegant properties. The inverse of AB is B inverse times A inverse — note the order reversal. And the inverse of A transpose equals the transpose of A inverse."
- Properties:
  1. (A⁻¹)⁻¹ = A
  2. (AB)⁻¹ = B⁻¹A⁻¹ (order reversal!)
  3. (Aᵀ)⁻¹ = (A⁻¹)ᵀ
  4. det(A⁻¹) = 1/det(A)
- **Items:** progressive reveal of property cards (4-5 items max)

### Scene 8: Connection to Systems + Summary + Outro (1.5 min)
- **Content budget:** system equation, solution formula, summary list, outro (4 items)
- **Narration:** "Why do we care about inverses? Because they solve systems of equations. If A times x equals b, then x equals A inverse times b. This is the matrix form of 'divide both sides by A'."
- Show Ax = b → x = A⁻¹b
- Summary key points
- Tease next video: "Next time — systems of equations and the matrix approach."
- Play channel outro
- **Items:** equation, summary text, next video card, outro elements (4 items)

## Key Formulas
- A⁻¹ · A = A · A⁻¹ = I
- A⁻¹ = (1/det(A)) · [[d, -b], [-c, a]] for 2×2
- det(A) ≠ 0 ⟺ A is invertible
- Ax = b → x = A⁻¹b
- (AB)⁻¹ = B⁻¹A⁻¹

## Visual Plan
- Use NumberPlane throughout (reuse helpers from video-29)
- Key visual: grid → transformed grid → restored grid (A, then A⁻¹)
- Color: PRIMARY for A, ACCENT for A⁻¹, RED for non-invertible examples, SECONDARY for I
- The "undo" animation is THE signature visual for this video
- Reference 3B1B's approach but add our formula derivation and computational focus
