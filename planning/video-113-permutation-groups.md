# Video 113: Permutation Groups
**Playlist:** Abstract Algebra I (Video 3 of 12)
**Est. Duration:** 15 minutes
**Class:** Video113_PermutationGroups

## Topics Covered
1. Symmetric groups S_n — definition and examples
2. Two-line notation and cycle notation
3. Composition of permutations (right-to-left convention)
4. Transpositions — definition and decomposition
5. Parity — even and odd permutations
6. Alternating group A_n

## Scene Plan

### Scene 1: Hook — "The Shuffling Problem" (~1.5 min)
**Content budget:** title + 4 colored dots + labels
- Open with 4 colored dots in a row (red, blue, green, yellow)
- Animate them being rearranged (shuffled)
- Ask: "How many ways can we rearrange 4 objects? What structure do these rearrangements have?"
- Bridge: "These rearrangements form a group — a permutation group."

### Scene 2: Definition of S_n (~2 min)
**Content budget:** title + definition + example
- Define S_n = set of all bijections {1, 2, ..., n} → {1, 2, ..., n}
- Operation: function composition
- Show |S_n| = n! (brief explanation)
- Verify group axioms: closure, associativity, identity, inverse
- S_3 has 6 elements — preview of what's coming

### Scene 3: Two-Line Notation (~2 min)
**Content budget:** title + notation display + example
- Show two-line notation: sigma = [1 2 3 4 / 2 4 1 3]
- Animate: each column shows where an element goes
- Identity in two-line notation
- Brief — this is a stepping stone to cycle notation

### Scene 4: Cycle Notation (~2.5 min)
**Content budget:** title + cycle display + dot diagram + labels
- Introduce cycle notation as the standard: (1 2 4)(3)
- Show how to read cycles: "1 goes to 2, 2 goes to 4, 4 goes to 1, 3 stays"
- Show a permutation diagram with colored dots and arrows
- Disjoint cycles: (1 2)(3 4) — elements in different cycles don't interact
- Convention: omit 1-cycles, write identity as (1)(2)...(n) or just e

### Scene 5: Composition of Permutations (~2 min)
**Content budget:** title + 2 permutations + result + tracking diagram
- Define composition: sigma ∘ tau means "apply tau first, then sigma"
- Right-to-left convention — emphasize this is the FUNCTION composition convention
- Work through example: (1 2 3) ∘ (1 3) step by step
- Use color tracking: follow one element at a time
- Note: permutations are generally NOT commutative

### Scene 6: Transpositions (~2 min)
**Content budget:** title + transposition def + cycle decomposition + example
- A transposition swaps exactly two elements: (i j)
- Key theorem: every cycle can be decomposed into transpositions
- Show: (1 2 3 4) = (1 4)(1 3)(1 2) — animate the splitting
- Disjoint cycles → product of transpositions for each cycle
- Note: decomposition is NOT unique (different orderings possible)

### Scene 7: Parity — Even and Odd Permutations (~2 min)
**Content budget:** title + definition + visual + examples
- Key result: the NUMBER of transpositions in any decomposition of a permutation always has the same parity
- Even permutation: decomposes into an even number of transpositions
- Odd permutation: decomposes into an odd number of transpositions
- Sign function: sgn(sigma) = (-1)^k where k = number of transpositions
- Visual: inversion count diagram — crossing lines in a permutation diagram
- S_3: even = {e, (1 2 3), (1 3 2)}, odd = {(1 2), (1 3), (2 3)}

### Scene 8: Alternating Group A_n and Summary (~1.5 min)
**Content budget:** title + definition + summary points
- A_n = set of even permutations in S_n
- A_n is a subgroup of S_n (closed under composition)
- |A_n| = n! / 2 (half the elements of S_n)
- Summary: 4 key takeaways
- Preview: "Next time — Cosets and Lagrange's Theorem"

## Competitive Analysis References
- Mathologer's "shuffling" metaphor used for Scene 1 hook
- Socratica's two-line notation bridge used for Scene 3
- Mathologer's color-coded element tracking used for Scene 5 composition
- Trefor Bazet's logical progression (def → cycles → transpositions → parity) used for overall structure
- Inversion-count visual for parity (not from any specific competitor, but more intuitive than algebraic proof)

## Style Notes
- Use colored dots (PRIMARY=blue, SECONDARY=green, ACCENT=yellow, RED=red) to represent elements 1-4
- Animate permutations as dot movements — this is the key visual for this video
- Keep formal definitions brief; maximize visual element tracking
- Right-to-left composition is a common student stumbling point — emphasize visually
