# Video 36: Diagonalization

**Playlist:** Linear Algebra (Undergraduate)
**Video #12 of 16 in playlist, #36 overall**
**Target Duration:** 12-15 min
**Status:** Script

## Competitive Analysis Notes
- youtubei.js non-functional; analysis based on domain knowledge.
- **3B1B:** Shows diagonalization as "changing to the eigenbasis" where the matrix becomes a simple scaling matrix. Emphasizes the geometric interpretation.
- **Khan Academy:** Computational approach — build P from eigenvectors, D from eigenvalues, verify A = PDP^{-1}.
- **Our approach:** Start with motivation (why diagonalize?), show the PDP^{-1} decomposition, work a 2x2 example, discuss when it fails, and show a power application.

## Scene Plan

### Scene 1: Hook + Channel Intro (~15s)
- Motivation: computing A^100 seems impossible, but diagonalization makes it easy.
- Content: Channel intro.

### Scene 2: Why Diagonalize? (~40s)
- A diagonal matrix is easy: powers, exponentials, determinants.
- If we can write A = PDP^{-1}, then A^n = PD^nP^{-1}.
- Content: motivation with formula preview.

### Scene 3: The Decomposition (~50s)
- A = PDP^{-1} where P has eigenvectors as columns, D has eigenvalues on diagonal.
- Content: formula, meaning of each matrix.

### Scene 4: Worked Example (~90s)
- Use same 2x2 matrix from Video 35: A = [[2,1],[1,2]]
- Eigenvalues: 3, 1. Eigenvectors: (1,-1), (1,1).
- Build P, D, verify the decomposition.

### Scene 5: Computing Powers (~45s)
- A^n = PD^nP^{-1}
- Show A^10 for our example.
- Content: formula + numeric result.

### Scene 6: When Does It Fail? (~40s)
- Need n linearly independent eigenvectors.
- Defective matrices (repeated eigenvalue, not enough eigenvectors).
- Example: [[1,1],[0,1]] has eigenvalue 1 with multiplicity 2 but only one eigenvector.

### Scene 7: Summary + Outro (~20s)
- Summary bullets, outro.

## Key Formulas
1. A = PDP^{-1}
2. A^n = PD^nP^{-1}
3. Diagonalizable iff n independent eigenvectors

## Style Notes
- Use same PRIMARY/SECONDARY color scheme as Video 35 for consistency
- The worked example reuses the matrix from Video 35 for continuity
