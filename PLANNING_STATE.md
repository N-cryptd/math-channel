# Math Channel — Planning State

## Production Progress
| # | Video | Status | Script | Rendered (480p) | Narrated |
|---|-------|--------|--------|-----------------|----------|
| 01-16 | Calculus I | DONE | YES | YES | YES |
| 17 | Sequences | DONE | YES | YES | YES (rendered/) |
| 18 | Series | DONE | YES | YES | YES (rendered/) |
| 19 | Convergence Tests | DONE | YES | YES | YES (rendered/) |
| 20 | Power Series | DONE | YES | YES | YES (rendered/) |
| 21 | Taylor/Maclaurin | DONE | YES | YES | YES (rendered/) |
| 22 | Parametric | DONE | YES | YES | YES (rendered/) |
| 23 | Polar | DONE | YES | YES | YES (rendered/) |
| 24 | Calc II Review | DONE | YES | YES | YES (rendered/) |

## Next Up: Linear Algebra (undergraduate/)
| # | Video | Status | Plan | Script | Rendered | Narrated |
|---|-------|--------|------|--------|----------|----------|
| 25 | What is a Vector? | DONE | YES | YES | YES |
| 26 | Linear Combinations and Span | DONE | YES | YES | YES |
| 27 | Matrices as Transformations | DONE | YES | YES | YES |
| 28 | Matrix Multiplication | DONE | YES | YES | YES |
| 29 | Determinants | DONE | YES | YES | YES |
| 30 | Inverse Matrices | DONE | YES | YES | YES | YES |
| 31 | Systems of Equations (Matrix) | DONE | YES | YES | YES | YES |
| 32 | Row Reduction / Echelon Form | DONE | YES | YES | YES | YES |
| 33 | Null Space and Column Space | DONE | YES | YES | YES | YES |
| 34 | Rank and Nullity | DONE | YES | YES | YES | YES |
| 35 | Eigenvalues and Eigenvectors | DONE | YES | YES | YES | YES |
| 36 | Diagonalization | DONE | YES | YES | YES | YES |
| 37 | Inner Product Spaces | DONE | YES | YES | YES | YES |
| 38 | Orthogonality and Gram-Schmidt | DONE | YES | YES | YES | YES |
| 39 | Linear Transformations (Abstract) | DONE | YES | YES | YES | YES |
| 40 | Singular Value Decomposition | DONE | YES | YES | YES | YES |

## Pipeline Steps Per Video
1. Write plan → planning/video-NN-topic.md
2. Write script → scripts/undergraduate/video-NN-topic.py
3. Compile check → python3 -c "import py_compile; ..."
4. Render → bash templates/produce.sh VideoNN_ClassName ql
5. Verify output → check *_narrated.mp4 exists
6. Update this file → change BACKLOG to DONE

## Calculus III — Multivariable (undergraduate/)
| # | Video | Status | Plan | Script | Rendered | Narrated |
|---|-------|--------|------|--------|----------|----------|
| 41 | Vectors in 3D Space | DONE | YES | YES | YES | YES |
| 42 | Dot Product in 3D | DONE | YES | YES | YES | YES |
| 43 | Cross Product in 3D | DONE | YES | YES | YES | YES |
| 44 | Lines and Planes in 3D | DONE | YES | YES | YES | YES |
| 45 | Vector-Valued Functions | DONE | YES | YES | YES | YES |
| 46 | Partial Derivatives | DONE | YES | YES | YES | YES |
| 47 | Gradient and Directional Derivatives | DONE | YES | YES | YES | YES |
| 48 | Lagrange Multipliers | DONE | YES | YES | YES | YES |
| 49 | Double Integrals | DONE | YES | YES | YES | YES |
| 50 | Triple Integrals | DONE | YES | YES | YES | YES |
| 51 | Line Integrals | DONE | YES | YES | YES | YES |
| 52 | Green's Theorem | DONE | YES | YES | YES | YES |
| 53 | Stokes' Theorem | DONE | YES | YES | YES | YES |
| 54 | Divergence Theorem (FINAL) | DONE | YES | YES | YES | YES |

## Differential Equations (undergraduate/)
| # | Video | Status | Plan | Script | Rendered | Narrated |
|---|-------|--------|------|--------|----------|----------|
| 55 | What is a Differential Equation? | DONE | YES | YES | YES | YES |

## Last Updated
2026-06-09 (Video 54 — Divergence Theorem produced: plan, script, render, narrate. CALCULUS III COMPLETE — all 54 videos done.)

## Ordinary Differential Equations (undergraduate/)
| # | Video | Status | Plan | Script | Rendered | Narrated |
|---|-------|--------|------|--------|----------|----------|
| 55 | What is a Differential Equation? | DONE | YES | YES | YES | YES |
| 56 | Separable Equations | DONE | YES | YES | YES | YES |
| 57 | First-Order Linear Equations | DONE | YES | YES | YES | YES |
| 58 | Second-Order Linear Equations (Intro) | DONE | YES | YES | YES | YES |

## Last Updated
2026-06-11 (Video 57 — First-Order Linear Equations rendered+narrated at 480p15. Video 58 — Second-Order Linear Equations Intro rendered+narrated at 480p15.)