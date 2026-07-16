# Video 120: Sylow Theorems — Plan

**Playlist:** Advanced Abstract Algebra (Video 2 of 12)
**Duration target:** 15 min
**Prerequisites:** Video 119 (Group Actions), Lagrange's Theorem, Cauchy's Theorem
**Script:** `scripts/undergraduate/video-120-sylow-theorems.py`
**Class:** `Video120_SylowTheorems`

## Competitive Analysis Summary

No high-production Manim-animated Sylow Theorems video exists on YouTube. Major market gap.

**Competitors analyzed:**
1. **Prof. Macauley** (60K views, 49 min) — Cayley diagrams, slides-based, too long. Structure 9, Visuals 8.
2. **Richard E Borcherds** (15K views, 20 min) — Chalkboard, ideal length, weak visuals. Structure 7, Visuals 3.
3. **VisualMath** (1.9K views, 16 min) — Slide animation, intuition-first but vague. Structure 6, Visuals 6.
4. **Mohamed Omar** (27K views, 12 min) — Best pacing, intuition→rigor, chalkboard. Structure 7, Pacing 8.

**Key adoption from competitors:**
- From Macauley: Use Cayley diagram visual for showing conjugacy of Sylow p-subgroups
- From Omar: Intuition-before-rigor approach, start with Cauchy's theorem motivation
- From all: Emphasize applications (groups of order pq) as concrete payoff

**Our differentiation:**
- Full Manim animation (none of the competitors use this)
- Compact 15-min single video covering all three theorems
- Visual metaphor: "prime power lenses" — zooming into the p-part of |G|

## Scene Plan (8 scenes)

### Scene 1: Hook — "The Mystery of the p-Part" (~40s narration)
- **Content budget:** Title + 3 items + 1 formula = 5 elements
- Visual: "What subgroups MUST every finite group of order 60 have?"
- Motivate with A5 (order 60) — what can we guarantee?
- Tease the three theorems
- Show key formula: |G| = p^k · m where p ∤ m

### Scene 2: Sylow p-Subgroups — Definition (~50s)
- **Content budget:** Title + 4 items
- Define: p-group, Sylow p-subgroup (order p^k where p^k || |G|)
- Lagrange's theorem as warm-up: order of subgroup divides |G|
- Cauchy's theorem as motivation: if p | |G| then G has an element of order p
- The Sylow p-subgroup generalization: not just one element, but a whole subgroup of order p^k

### Scene 3: First Sylow Theorem — Existence (~55s)
- **Content budget:** Title + 3 items + 1 formula
- Statement: For every prime p dividing |G|, Sylow p-subgroups exist
- Proof sketch via group action on subsets (action on size-p^k subsets by left multiplication)
- Show counting argument visually
- Key insight: existence guarantees we can always "find the p-part"

### Scene 4: Second Sylow Theorem — Conjugacy (~50s)
- **Content budget:** Title + 4 items
- Statement: All Sylow p-subgroups are conjugate to each other
- If P and Q are Sylow p-subgroups, then P = gQg^{-1} for some g in G
- Proof via double coset counting (brief sketch)
- Visual: Cayley diagram showing conjugation as "viewing the same structure from different angles"

### Scene 5: Third Sylow Theorem — Counting (~60s)
- **Content budget:** Title + 4 items + 1 boxed formula
- Statement: n_p ≡ 1 (mod p) and n_p | m
- The number of Sylow p-subgroups is tightly constrained
- Boxed formula: n_p ≡ 1 (mod p) and n_p | (|G| / p^k)
- Proof sketch using group action of G on the set of Sylow p-subgroups by conjugation
- Visual: Show constraint narrowing possibilities for concrete group orders

### Scene 6: Application — Groups of Order pq (~55s)
- **Content budget:** Title + 4 items + 1 formula
- Example: Groups of order 6 = 2 × 3 (or pq in general)
- Use Sylow theorems to determine structure
- n_3 ≡ 1 (mod 3) and n_3 | 2 → n_3 = 1 (unique Sylow 3-subgroup)
- n_2 ≡ 1 (mod 2) and n_2 | 3 → n_2 = 1 or 3
- Result: classify all groups of order pq where p ∤ (q-1)

### Scene 7: Application — Groups of Order 30 (~50s)
- **Content budget:** Title + 4 items
- Example: |G| = 30 = 2 · 3 · 5
- n_5 ≡ 1 (mod 5) and n_5 | 6 → n_5 = 1 or 6
- n_3 ≡ 1 (mod 3) and n_3 | 10 → n_3 = 1 or 10
- Show how constraints lead to normal Sylow subgroups
- Conclusion: G ≅ C_3 × D_5 or C_5 × D_3 (up to isomorphism)

### Scene 8: Summary (~30s)
- **Content budget:** Title + 3 items
- Three theorems recap: Existence, Conjugacy, Counting
- Connection to classification of finite groups
- Preview of next video: Solvable and Nilpotent Groups
- Outro
