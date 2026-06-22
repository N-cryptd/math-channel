# Video 81: Sets and Operations
## Discrete Mathematics — Video 3 of 12

**Predecessor:** Video 80 (Predicate Logic)
**Next:** Video 82 (Relations and Functions)

### Competitive Analysis

Based on analysis in channel-analysis/improvements.md (2026-06-21):
- **MAJOR GAP:** No high-quality Manim-animated video covers all set theory basics in one place
- Competitors split across 4-6 videos: TrevTutor (2.79M views, pen-on-paper), Dr. Trefor Bazett (338K, semi-animated), Organic Chemistry Tutor (2.93M on union/intersection, 1.35M on set builder notation)
- De Morgan's laws for sets have NO animated/visual treatment on YouTube
- No competitor animates the 2^n power set growth or Cartesian product grid formation
- Following TrevTutor's proven demand (2.79M views) and Trefor Bazett's structured approach

### Key Differentiators
1. Venn diagram animations: color-coded fill operations for union, intersection, difference, complement
2. Animated set builder notation → roster notation transformation
3. Power set as branching tree showing 2^n growth
4. Cartesian product as animated grid forming from two axes
5. Visual proof of De Morgan's laws via Venn diagram shading
6. Bridge from predicate logic: predicates define sets (connects to Video 80)

### Color Coding
| Concept | Color | Hex |
|---------|-------|-----|
| Set A | PRIMARY | #5BC0EB |
| Set B | SECONDARY | #7BC950 |
| Universal set U | ACCENT | #FFD166 |
| Empty set / special | RED | #EF476F |
| Element labels | WHITE | #FFFFFF |
| Intersection region | ACCENT | #FFD166 |
| Complement region | DIM | #6B6B8D |

### Structure (12 minutes, 10 scenes)

**Scene 1 — Hook: What is a Set? (0:45)**
- Recall from predicate logic: P(x) picks out elements — those elements form a set
- A set is a well-defined collection of distinct objects
- Examples: {1, 2, 3}, {a, b, c}, {red, blue, green}
- Everything in mathematics is built from sets — they are the foundation
- Content budget: 2 examples + motivation statement

**Scene 2 — Set Notation and Roster Method (1:00)**
- Section divider
- Curly braces {}: the universal set notation
- Element of: x ∈ A (x belongs to A)
- Not element of: x ∉ A
- Roster method: listing all elements explicitly
- Examples: A = {1, 2, 3, 4, 5}, B = {a, e, i, o, u}
- Order doesn't matter: {1, 2, 3} = {3, 1, 2}
- No duplicates: {1, 1, 2} = {1, 2}
- Visual: animate elements appearing inside curly braces
- Content budget: definition + 2 examples + key properties

**Scene 3 — Set Builder Notation (1:15)**
- Section divider
- Sometimes listing all elements is impossible (infinite sets!)
- Set builder notation: {x ∈ U | P(x)} — "the set of all x in U such that P(x)"
- The vertical bar | reads as "such that" or "where"
- Bridge to predicate logic: the predicate P(x) from Video 80 defines the set
- Examples:
  - E = {x ∈ Z | x is even}
  - P = {x ∈ N | x is prime}
  - S = {x ∈ R | 0 < x < 1}
- Animated conversion: roster {2, 4, 6, 8, ...} → builder notation
- Content budget: definition + 3 examples + animated conversion

**Scene 4 — Special Sets (0:45)**
- Section divider
- Empty set: ∅ = {} — contains nothing
- Universal set: U — the set of all elements under consideration
- Subset: A ⊆ B — every element of A is in B
- Proper subset: A ⊂ B — subset but not equal
- Visual: show A as a circle inside B's circle
- Content budget: 4 definitions with visual

**Scene 5 — Union and Intersection (1:30)**
- Section divider
- Venn diagram with two overlapping circles (A in blue, B in green)
- Union: A ∪ B = {x | x ∈ A or x ∈ B} — everything in A or B or both
  - Visual: shade both circles entirely
- Intersection: A ∩ B = {x | x ∈ A and x ∈ B} — elements in BOTH
  - Visual: shade only the overlap
- Disjoint sets: A ∩ B = ∅ (no overlap)
- Example: A = {1, 2, 3, 4}, B = {3, 4, 5, 6}
  - A ∪ B = {1, 2, 3, 4, 5, 6}
  - A ∩ B = {3, 4}
- Content budget: 2 operations + example with Venn

**Scene 6 — Difference and Complement (1:15)**
- Section divider
- Set difference: A \ B = {x | x ∈ A and x ∉ B} — in A but NOT in B
  - Visual: shade A minus the overlap
- Complement: A^c = U \ A = {x | x ∈ U and x ∉ A} — everything NOT in A
  - Visual: shade the entire rectangle except A's circle
- Example: U = {1, 2, 3, 4, 5}, A = {1, 2}
  - A^c = {3, 4, 5}
- Connection to logic: complement is like negation, intersection is like AND, union is like OR
- Content budget: 2 operations + example + logic connection

**Scene 7 — Power Set (1:15)**
- Section divider
- The power set P(A) is the set of ALL subsets of A
- Example: A = {1, 2}
  - P(A) = {∅, {1}, {2}, {1, 2}}
  - |P(A)| = 4 = 2^2
- Example: A = {1, 2, 3}
  - |P(A)| = 8 = 2^3
- General formula: |P(A)| = 2^|A|
- Visual: binary tree showing each element either included or excluded (0/1 branches)
- "Aha moment": the power set grows EXPONENTIALLY — adding one element doubles the power set
- Content budget: 2 examples + formula + tree visual

**Scene 8 — Cartesian Product (1:15)**
- Section divider
- Ordered pair: (a, b) — order matters! (1, 2) ≠ (2, 1)
- Cartesian product: A × B = {(a, b) | a ∈ A, b ∈ B}
- Example: A = {1, 2}, B = {x, y}
  - A × B = {(1,x), (1,y), (2,x), (2,y)}
- |A × B| = |A| × |B|
- Visual: animate a grid/table forming from two axes
- Connection: the xy-plane in geometry IS the Cartesian product R × R
- Content budget: definition + example + grid visual + connection to geometry

**Scene 9 — De Morgan's Laws for Sets (1:15)**
- Section divider
- (A ∪ B)^c = A^c ∩ B^c — "complement of union = intersection of complements"
- (A ∩ B)^c = A^c ∪ B^c — "complement of intersection = union of complements"
- These mirror the De Morgan's laws from propositional logic (Video 79)!
- Visual proof with Venn diagrams:
  - Shade (A ∪ B)^c: everything outside both circles
  - Shade A^c ∩ B^c: outside A AND outside B — same region!
- Real-world: "Not (A or B)" = "Not A AND Not B" — same pattern as logic
- Content budget: 2 laws + animated Venn proof + logic connection

**Scene 10 — Summary + Outro (0:30)**
- Recap: sets are collections → notation (roster + builder) → special sets → 4 operations → power set → Cartesian product → De Morgan's laws
- "Sets are the foundation of all mathematics"
- Next: Relations and Functions — built on sets!
- Content budget: 3 summary items
