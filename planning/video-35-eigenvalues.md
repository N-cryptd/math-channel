# Video 35: Eigenvalues and Eigenvectors

**Playlist:** Linear Algebra (Undergraduate)
**Video #11 of 16 in playlist, #35 overall**
**Target Duration:** 12-15 min
**Status:** Script

## Competitive Analysis Notes
- youtubei.js non-functional; analysis based on domain knowledge.
- **3B1B:** Iconic video "Eigenvalues and Eigenvectors, visually explained" — uses the linear transformation visual where eigenvectors stay on their span. Color-codes invariant directions. Shows eigenvectors as the "natural axes" of a transformation.
- **Khan Academy:** Computational approach — characteristic polynomial, solve for eigenvalues, then find eigenvectors by solving (A - λI)x = 0.
- **Dr. Trefor Bazett:** Bridges both — starts with geometric intuition, then shows computation.
- **Our approach:** Start with the geometric question "which vectors don't change direction?", define formally, show the characteristic polynomial method, work a 2×2 example, and end with the geometric interpretation.

## Scene Plan

### Scene 1: Hook + Channel Intro (~15s)
- **Narration:** "Some transformations stretch space along certain directions while leaving those directions unchanged. Today we find those special directions — the eigenvectors — and measure how much they stretch — the eigenvalues."
- **Content:** Channel intro.
- **Budget:** Intro mobjects only.

### Scene 2: The Geometric Idea (~45s)
- **Narration:** "Imagine applying a transformation to a vector. Most vectors change direction. But some special vectors only get scaled — they stay on the same line. These are eigenvectors."
- **Content:**
  - Title: "The Core Idea"
  - Before/After: vector v → Av (same direction, different length)
  - Text: "Av = λv — same direction, scaled by λ"
- **Budget:** 3 items.

### Scene 3: Formal Definition (~45s)
- **Narration:** "Formally: a nonzero vector v is an eigenvector of A if Av equals lambda v for some scalar lambda. The scalar lambda is the eigenvalue."
- **Content:**
  - Title: "Definition"
  - MathTex: Av = λv, v ≠ 0
  - Text: "λ (lambda) = eigenvalue (scaling factor)"
  - Text: "v = eigenvector (invariant direction)"
- **Budget:** 4 items.

### Scene 4: Finding Eigenvalues — Characteristic Polynomial (~60s)
- **Narration:** "How do we find eigenvalues? We rearrange: Av minus lambda v equals zero. Factor out v: (A minus lambda I) v equals zero. For a nonzero solution v, the matrix A minus lambda I must be singular. So its determinant is zero."
- **Content:**
  - Step 1: Av = λv
  - Step 2: Av - λv = 0 → (A - λI)v = 0
  - Step 3: det(A - λI) = 0
  - Text: "This is the characteristic equation"
- **Budget:** 4 items.

### Scene 5: Worked Example — 2×2 Matrix (~90s)
- **Narration:** "Let us find the eigenvalues of a 2×2 matrix. We compute the determinant of A minus lambda I and set it to zero. This gives us a quadratic equation in lambda."
- **Content:**
  - Matrix A = [[2, 1], [1, 2]]
  - A - λI = [[2-λ, 1], [1, 2-λ]]
  - det = (2-λ)² - 1 = λ² - 4λ + 3 = 0
  - Solutions: λ₁ = 3, λ₂ = 1
- **Budget:** 4 items (progressive reveal of computation steps).

### Scene 6: Finding Eigenvectors (~60s)
- **Narration:** "For each eigenvalue, we find eigenvectors by solving (A minus lambda I) v equals zero. For lambda equals 3, we get x plus y equals 0, so eigenvectors are multiples of (1, -1). For lambda equals 1, we get x minus y equals 0, so eigenvectors are multiples of (1, 1)."
- **Content:**
  - λ₁ = 3: eigenvector (1, -1)
  - λ₂ = 1: eigenvector (1, 1)
  - Summary table
- **Budget:** 4 items.

### Scene 7: Geometric Interpretation (~45s)
- **Narration:** "Geometrically, our transformation stretches by a factor of 3 along the direction (1, -1) and leaves the direction (1, 1) unchanged. These are the natural axes of the transformation."
- **Content:**
  - Visual: two eigenvector directions shown
  - λ₁ = 3: stretches by 3
  - λ₂ = 1: leaves unchanged
  - Text: "Eigenvectors = natural coordinate system"
- **Budget:** 4 items.

### Scene 8: Key Properties (~45s)
- **Narration:** "Some important facts. The sum of eigenvalues equals the trace of the matrix. The product of eigenvalues equals the determinant. And an n by n matrix has at most n eigenvalues."
- **Content:**
  - λ₁ + λ₂ + ... + λₙ = tr(A)
  - λ₁ · λ₂ · ... · λₙ = det(A)
  - Text: "At most n distinct eigenvalues for n×n matrix"
- **Budget:** 4 items.

### Scene 9: Summary + Outro (~20s)
- **Narration:** "To summarize: eigenvectors are invariant directions, eigenvalues measure scaling, and we find them via the characteristic polynomial. Next time we use them to diagonalize matrices."
- **Content:**
  - Summary bullets
  - Outro
- **Budget:** Intro mobjects.

## Key Formulas
1. Av = λv, v ≠ 0
2. det(A - λI) = 0 (characteristic equation)
3. Σλᵢ = tr(A), Πλᵢ = det(A)

## Example Matrix
A = [[2, 1], [1, 2]]
- Characteristic polynomial: (2-λ)² - 1 = λ² - 4λ + 3 = (λ-3)(λ-1)
- λ₁ = 3, eigenvector (1, -1)
- λ₂ = 1, eigenvector (1, 1)

## Style Notes
- Use PRIMARY for eigenvectors, ACCENT for eigenvalues
- Geometric interpretation scene should feel intuitive — use color-coded arrows/lines
- The worked example is the heart of the video — spend the most time here
