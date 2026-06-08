# Video 40: Singular Value Decomposition

**Playlist:** Linear Algebra (Undergraduate)
**Video #16 of 16 in playlist, #40 overall**
**Target Duration:** 12-15 min
**Status:** Plan

## Competitive Analysis Notes
- Analysis based on domain knowledge (web search deferred).
- **3B1B (Essence of Linear Algebra Ch.7):** Introduces SVD via the idea that every linear transformation can be decomposed into: rotation → scaling → rotation. Uses the "stretching directions" (singular vectors) and "stretching amounts" (singular values) as the core intuition. Beautiful visualization of ellipsoids.
- **Reducible:** Focuses on SVD for data compression (low-rank approximation). Shows how keeping top-k singular values gives best rank-k approximation (Eckart-Young theorem).
- **Our approach:** Connect SVD back to everything we've learned: eigenvalues, diagonalization, orthogonal matrices, and projections. Start with the motivation (why SVD exists when diagonalization fails), show the geometric picture, give the formula, and end with a data compression teaser.

## Scene Plan

### Scene 1: Hook + Channel Intro (~15s)
- Motivation: "Diagonalization only works for nice matrices. SVD works for EVERY matrix."
- Content: Channel intro.

### Scene 2: Why Do We Need SVD? (~45s)
- Diagonalization requires n independent eigenvectors — not all matrices have them.
- Non-square matrices can't be diagonalized at all.
- SVD works for ANY m×n matrix.
- Content: motivation contrast diagonalization vs SVD.

### Scene 3: The Geometric Picture (~60s)
- Every linear transformation T: Rⁿ → Rᵐ can be decomposed as:
  - Rotate in the domain (Vᵀ)
  - Scale along orthogonal axes (Σ)
  - Rotate in the codomain (U)
- Unit circle → ellipse under any matrix.
- The axes of the ellipse are the singular vectors.
- Content: visual with rotation-scale-rotation breakdown.

### Scene 4: The SVD Formula (~60s)
- A = UΣVᵀ
- U: m×m orthogonal matrix (left singular vectors)
- Σ: m×n diagonal matrix (singular values σ₁ ≥ σ₂ ≥ ... ≥ 0)
- Vᵀ: n×n orthogonal matrix (right singular vectors)
- Content: formula, dimensions, meaning of each component.

### Scene 5: Computing the SVD (~60s)
- Step 1: Compute AᵀA — this is symmetric positive semi-definite.
- Step 2: Find eigenvalues λᵢ and eigenvectors vᵢ of AᵀA.
- Step 3: σᵢ = √λᵢ (singular values).
- Step 4: uᵢ = Avᵢ / σᵢ (left singular vectors).
- Content: step-by-step algorithm with formulas.

### Scene 6: Connection to Other Concepts (~50s)
- Singular values of A = √(eigenvalues of AᵀA)
- If A is symmetric: SVD = eigenvalue decomposition
- Rank(A) = number of nonzero singular values
- The best rank-k approximation uses top k singular values
- Content: formula connections.

### Scene 7: Low-Rank Approximation (~45s)
- Keep only the top k singular values: A ≈ U_k Σ_k V_kᵀ
- This is the BEST rank-k approximation (Eckart-Young theorem)
- Applications: image compression, noise reduction, recommendation systems
- Content: formula + application list.

### Scene 8: Summary + Outro (~20s)
- SVD works for every matrix, reveals hidden structure
- Recap of full Linear Algebra playlist
- Channel outro with "What's Next?" card.
- Content: summary, playlist recap, outro.

## Key Formulas
1. A = UΣVᵀ
2. σᵢ = √λᵢ(AᵀA)
3. uᵢ = Avᵢ/σᵢ
4. Rank(A) = # nonzero σᵢ
5. A_k = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ (best rank-k approximation)
