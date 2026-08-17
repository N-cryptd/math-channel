# Video 211: Simplicial Homology — Plan

**Playlist:** Algebraic Topology (Videos 207–216)
**Prerequisites:** Video 210 (Simplicial Complexes)

## Video Outline (~10 min)

### Scene 1: Hook — Counting Holes Algebraically (18s)
- Motivation: fundamental group uses loops; homology uses chains of simplices
- Content budget: intro + 3 key ideas

### Scene 2: Chains — Formal Sums of Simplices (24s)
- Oriented simplices, formal sums with integer coefficients
- Chain groups C_n(K) — free abelian groups on n-simplices
- Content budget: definition + 2 formulas + examples

### Scene 3: Boundary Maps (25s)
- The boundary operator ∂_n: C_n → C_{n-1}
- Boundary of a simplex: alternating sum of its faces
- Key property: ∂ ∘ ∂ = 0
- Content budget: formula + visual + property

### Scene 4: Cycles and Boundaries (25s)
- Z_n = ker(∂_n) — cycles (chains with zero boundary)
- B_n = im(∂_{n+1}) — boundaries (chains that are boundaries of something)
- B_n ⊂ Z_n (because ∂²=0)
- Content budget: 2 definitions + inclusion + visual

### Scene 5: Homology Groups (25s)
- H_n(K) = Z_n / B_n — cycles modulo boundaries
- Rank of H_n counts "n-dimensional holes"
- H_0 counts connected components
- H_1 captures the same info as abelianization of π_1
- Content budget: definition + 3 interpretations

### Scene 6: Computing H_n (30s)
- Example: homology of the circle
- H_0(S^1) = Z, H_1(S^1) = Z, H_n = 0 for n ≥ 2
- Example: homology of the sphere
- H_0(S^2) = Z, H_1(S^2) = 0, H_2(S^2) = Z
- Content budget: worked examples + formulas

### Scene 7: Summary & Outro (20s)
- Homology as a systematic hole-counting tool
- Advantages over fundamental group: abelian, computable
- Next video: Singular Homology

## Key Formulas
- ∂[v_0, ..., v_n] = Σ(-1)^i [v_0, ..., v̂_i, ..., v_n]
- ∂² = 0
- H_n = Z_n / B_n = ker(∂_n) / im(∂_{n+1})
- H_0(S^1) = Z, H_1(S^1) = Z
- H_1(S^2) = 0, H_2(S^2) = Z
