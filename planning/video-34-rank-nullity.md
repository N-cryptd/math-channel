# Video 34: Rank and Nullity

**Playlist:** Linear Algebra (Undergraduate)
**Video #10 of 16 in playlist, #34 overall**
**Target Duration:** 12–15 min
**Status:** Script

## Competitive Analysis Notes
- youtubei.js non-functional; analysis based on domain knowledge.
- **3B1B style:** Connects rank to dimension of the output space — how much "information" survives the transformation. Visual metaphors of collapsing dimensions.
- **Khan Academy:** Systematic approach — defines rank as number of pivots, proves row rank = column rank, works through examples.
- **Trefor Bazett:** Emphasizes the rank-nullity theorem as the "accounting equation" of linear algebra — everything is either in the null space or contributes to the column space.
- **Our approach:** Define rank computationally (pivot count), then geometrically (dimension of column space), prove row rank = column rank via RREF, deep-dive into rank-nullity with examples, discuss rank of special matrices.

## Scene Plan

### Scene 1: Hook + Channel Intro (~15s)
- **Narration:** "We just met the null space and column space. Today we go deeper into their dimensions and uncover a surprising fact: the row rank always equals the column rank."
- **Content:** Channel intro. Brief recap.
- **Budget:** Intro mobjects only.

### Scene 2: What is Rank? (~45s)
- **Narration:** "The rank of a matrix is the number of pivot columns in its row echelon form. It counts how many columns are truly independent."
- **Content:**
  - Title: "Rank"
  - Definition: rank(A) = number of pivots in REF
  - Example: 3×4 matrix with 2 pivots → rank = 2
  - Text: "Also equals dim(Col A)"
- **Budget:** 4 items.

### Scene 3: Rank by Example (~60s)
- **Narration:** "Consider this matrix. After row reduction, we find two pivot positions. So the rank is 2. The nullity — the dimension of the null space — is 4 minus 2 equals 2."
- **Content:**
  - Matrix (3×4)
  - REF with pivots highlighted
  - rank = 2, nullity = n - rank = 4 - 2 = 2
  - Text: "Two free variables"
- **Budget:** 4 items.

### Scene 4: Nullity (~30s)
- **Narration:** "Nullity is simply the dimension of the null space. It tells us how many dimensions get collapsed to zero."
- **Content:**
  - Title: "Nullity"
  - Formula: nullity(A) = dim(Nul A)
  - Formula: nullity(A) = n - rank(A)
  - Text: "Number of free variables in RREF"
- **Budget:** 4 items.

### Scene 5: Row Rank = Column Rank (~60s)
- **Narration:** "Here is a remarkable fact: the number of independent rows always equals the number of independent columns. Why? Because row operations preserve the row space, and RREF has the same number of nonzero rows as pivot columns."
- **Content:**
  - Title: "Row Rank = Column Rank"
  - Text: "Number of independent rows = number of independent columns"
  - Text: "Both equal the number of pivots in RREF"
  - Brief illustration
- **Budget:** 4 items.

### Scene 6: Rank-Nullity Deep Dive (~60s)
- **Narration:** "The rank-nullity theorem says: rank plus nullity equals the number of columns. Think of it as an accounting equation. Every column is either a pivot column contributing to the rank, or a free column contributing to the nullity."
- **Content:**
  - Formula: rank(A) + nullity(A) = n
  - Visual: pivot columns (counted by rank) + free columns (counted by nullity) = all columns
  - Example verification
- **Budget:** 4 items.

### Scene 7: Rank of Special Matrices (~45s)
- **Narration:** "Some special cases. The identity matrix has full rank. A matrix of all zeros has rank zero. A square invertible matrix has full rank and nullity zero."
- **Content:**
  - I_n: rank = n, nullity = 0
  - Zero matrix: rank = 0, nullity = n
  - Invertible: rank = n, nullity = 0
- **Budget:** 3 items (show one at a time via progressive reveal).

### Scene 8: Summary + Outro (~20s)
- **Narration:** "To summarize: rank counts independent columns, nullity counts what gets collapsed, and together they account for every column. Next time we meet eigenvalues and eigenvectors."
- **Content:**
  - Summary bullets
  - Outro with channel branding
- **Budget:** Intro mobjects.

## Key Formulas
1. rank(A) = number of pivots in REF(A) = dim(Col A) = dim(Row A)
2. nullity(A) = dim(Nul A) = n - rank(A)
3. rank(A) + nullity(A) = n

## Style Notes
- Use PRIMARY for rank, SECONDARY for nullity throughout
- Emphasize the "accounting" metaphor for rank-nullity
- Keep scenes shorter to avoid narration timing issues
