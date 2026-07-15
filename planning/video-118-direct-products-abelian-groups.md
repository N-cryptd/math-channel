# Video 118: Direct Products and Finite Abelian Groups

**Playlist:** Abstract Algebra I (Video 8 of 12)
**Class:** Video118_DirectProductsFiniteAbelian
**Estimated duration:** 12-15 minutes
**Date:** 2026-07-15

## Competitive Analysis Reference
Analysis completed 2026-07-15 in `channel-analysis/improvements.md` (section for Video 118).
Key sources: Michael Penn (16.7K views), Prof. Macauley (24.6K), EpsilonDelta (55.8K), Kimberly Brehm (8.4K+11.3K).

## Scene Plan

### Scene 1: Hook — "Building Groups from Simpler Ones" (1.5 min)
- Opening question: "How do we build complex groups from simple ones?"
- Chemistry analogy (from EpsilonDelta): groups = atoms, direct products = molecules
- Teaser: Z_2 × Z_3 = Z_6 (order 6 built from two order-2/3 groups)
- play_intro()

### Scene 2: External Direct Product — Definition (2 min)
- Definition: G × H = {(g,h) : g ∈ G, h ∈ H} with component-wise operation
- Example: Z_2 × Z_3 as ordered pairs with addition mod (2,3)
- Show the 6 elements explicitly
- Cayley table for Z_2 × Z_2 (Klein four-group) — 4 elements, multiplication table

### Scene 3: When is the Product Cyclic? (2.5 min)
- Key theorem: Z_m × Z_n ≅ Z_{mn} iff gcd(m,n) = 1
- Visual grid: Z_2 × Z_3 lattice (shows it's cyclic, generates full 6-cycle)
- Counterexample: Z_2 × Z_2 (Klein four, NOT cyclic — every element has order 1 or 2)
- Connection: this is the Chinese Remainder Theorem in group-theoretic language

### Scene 4: Properties of Direct Products (2 min)
- Order: |G × H| = |G| · |H|
- Subgroups: if A ≤ G and B ≤ H, then A × B ≤ G × H
- Abelian: G × H is abelian iff both G and H are abelian
- Component-wise structure: operations happen independently in each coordinate

### Scene 5: Internal Direct Products (1.5 min)
- When a group G "splits" as H × K internally
- Conditions: H ⊴ G, K ⊴ G, H ∩ K = {e}, HK = G
- Example: Z_6 = Z_2 × Z_3 internally via subgroups {0,3} and {0,2,4}

### Scene 6: Classification Theorem Statement (2 min)
- Fundamental Theorem of Finite Abelian Groups
- Every finite abelian group ≅ direct product of cyclic p-groups
- Two equivalent forms: invariant factor decomposition, elementary divisor decomposition
- Prime factorization analogy: "classifying abelian groups ≈ factoring integers"

### Scene 7: Classification Examples (2.5 min)
- All abelian groups of order 8: Z_8, Z_4 × Z_2, Z_2 × Z_2 × Z_2 (3 groups)
- All abelian groups of order 36: partitions of exponents → enumerate
- Algorithm: factor |G|, find partitions of prime-power exponents

### Scene 8: Summary + Outro (1 min)
- Key takeaways
- Direct products = building blocks
- Classification theorem gives the "periodic table" of finite abelian groups
- play_outro()

## Content Budget
- Scene 1: 3 items (title + 2 text items) + intro animation
- Scene 2: 4-5 items (definition, example, table)
- Scene 3: 3-4 items (theorem, visual, counterexample)
- Scene 4: 3-4 items (properties list)
- Scene 5: 3-4 items (conditions, example)
- Scene 6: 3-4 items (theorem statement, forms)
- Scene 7: 3-4 items (examples)
- Scene 8: 5 items (takeaways) + outro
