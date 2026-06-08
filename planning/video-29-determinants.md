# Video 29: Determinants

**Playlist:** Linear Algebra (Video 5 of 16)
**Duration target:** 12-15 minutes
**Status:** PLAN COMPLETE

## Competitive Analysis Reference
Based on analysis of 3B1B Chapter 6 (4.76M views), Khan Academy, and Mathologer.
See `channel-analysis/improvements.md` — Video 29 section.

Key insight from 3B1B: determinant measures area/volume scaling of a transformation.
Our approach: geometric intuition first → formula derivation → worked example → properties.

## Scene Breakdown

### Scene 1: Hook + Intro (30s)
- **Content budget:** intro animation + question
- **Narration:** "Every matrix transformation stretches, squishes, or flips space. The determinant tells you exactly HOW MUCH."
- Play channel intro
- Show a grid being transformed (area changes visibly) → ask "by what factor?"
- **Items:** transformed grid visual, question text (2 items)

### Scene 2: Area Scaling — The Geometric Meaning (2 min)
- **Content budget:** plane, unit square, transformed parallelogram, area labels (4 items)
- **Narration:** "Let's start with a simple question. Take the unit square, and apply a matrix transformation. The unit square becomes a parallelogram. The area of this parallelogram, divided by the area of the original unit square (which is 1), is the determinant."
- Show 2D grid with unit square highlighted
- Apply a specific transformation (e.g., [[3, 1], [0, 2]])
- Show the parallelogram with area computed
- Key formula: det(A) = area(after) / area(before)
- **Items:** plane, unit square, arrow, area value (4 items)

### Scene 3: The 2x2 Formula (2 min)
- **Content budget:** matrix, column vectors, parallelogram, formula (4 items)
- **Narration:** "The area of a parallelogram formed by two vectors is the magnitude of their cross product. For vectors (a,c) and (b,d), this gives |ad - bc|."
- Show columns of matrix as two vectors
- Show the parallelogram they form
- Derive: det = ad - bc
- Highlight the formula prominently
- **Items:** matrix, two column vectors, parallelogram, formula box (4 items)

### Scene 4: Signed Area — Orientation Matters (2 min)
- **Content budget:** before/after grids, det values, orientation indicator (4 items)
- **Narration:** "The determinant isn't just area — it's SIGNED area. Positive means orientation is preserved. Negative means it gets flipped."
- Show det > 0 case (stretching, area grows, orientation same)
- Show det < 0 case (reflection, area same but orientation flipped)
- Visual: show i-hat and j-hat swapping positions (reflection across y=x)
- det < 0 means "mirror image" — orientation reversed
- **Items:** two grids side by side, det values (3-4 items)

### Scene 5: det = 0 — The Crucial Case (2 min)
- **Content budget:** plane, squished grid, det label, insight text (4 items)
- **Narration:** "When the determinant is zero, something dramatic happens. The transformation squishes all of 2D space into a line, or even a single point. Everything collapses."
- Show a transformation with det = 0 (e.g., [[1, 2], [2, 4]])
- Animate the entire 2D grid collapsing onto a line
- This means: det = 0 ⟹ non-invertible (preview of inverse matrices video)
- Connect to systems of equations: det = 0 ⟹ no unique solution
- **Items:** plane, squished transformation, "det = 0" label, "non-invertible" text (4 items)

### Scene 6: Worked Example (2 min)
- **Content budget:** matrix, formula, computation steps, result (4 items)
- **Narration:** "Let's compute a determinant. Take the matrix with entries 2, 1, 5, 3. The determinant is 2 times 3 minus 1 times 5, equals 6 minus 5, equals 1. So this transformation preserves area."
- Compute det([[2,1],[5,3]]) = 2(3) - 1(5) = 1
- Visual: show the matrix, highlight the diagonal products, compute
- Second quick example: det([[1,2],[3,6]]) = 1(6) - 2(3) = 0
- **Items:** matrix, computation steps (3-4 items)

### Scene 7: Key Properties (2 min)
- **Content budget:** property list items revealed progressively (3-5 items)
- **Narration:** "The determinant has some beautiful properties. det of the identity is 1, because the identity doesn't change area. det of AB equals det(A) times det(B) — the area scaling factors multiply. det of A transpose equals det(A)."
- Properties:
  1. det(I) = 1
  2. det(AB) = det(A) · det(B) (geometric: scaling factors compose)
  3. det(A^T) = det(A)
  4. det(cA) = c^n det(A) for n×n matrix
  5. Swapping rows/columns flips the sign
- **Items:** progressive reveal of property cards (5 items max)

### Scene 8: Summary + Outro (1 min)
- **Content budget:** summary list, next video tease, outro (4 items)
- **Narration:** "To recap: the determinant measures how much a matrix transformation scales area. It's positive when orientation is preserved, negative when flipped, and zero when space collapses. And the formula for a 2x2 matrix is ad minus bc."
- Summary key points
- Tease next video: "Next time — inverse matrices, and why det = 0 means no inverse."
- Play channel outro
- **Items:** summary text, next video card, outro elements (4 items)

## Key Formulas
- det([[a,b],[c,d]]) = ad - bc
- det(A) = 0 ⟹ A is not invertible
- det(AB) = det(A) · det(B)
- det(I) = 1

## Visual Plan
- Use NumberPlane throughout (from video-28 helpers)
- Unit square → parallelogram animation is THE key visual
- Color: PRIMARY for i-hat/x-components, SECONDARY for j-hat/y-components, RED for det < 0 cases, ACCENT for formula highlights
- Grid transformation animations: reuse apply_to_plane() helper from video-28
