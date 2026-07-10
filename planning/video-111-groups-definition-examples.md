# Video 111: Groups — Definition and Examples

**Playlist:** Abstract Algebra I (Video 1 of 12) — SERIES PREMIERE
**Level:** Undergraduate (Abstract Algebra)
**Class:** Video111_GroupsDefinitionExamples
**Script:** scripts/undergraduate/video-111-groups-definition-examples.py

## Competitive Analysis Reference

Analysis completed 2026-07-08. See `channel-analysis/improvements.md` — section "Groups: Definition and Examples (Video 111)".

Key competitor insights incorporated:
- 3Blue1Brown: Symmetry-of-triangle hook, concrete-to-abstract arc, color-coded transformations
- Socratica: Definition → examples → non-examples structure, series positioning
- Dr. Trefor Bazett: "What makes something a group?" question-first framing, Rubik's cube example
- Bright Side of Mathematics: Verifying examples against each axiom, Manim theorem-proof format

Our unique advantage: Animated systematic curriculum — this is Video 1 of 12 covering the full abstract algebra sequence. We combine 3B1B's visual intuition with Socratica's rigor, using progressive disclosure and color-coded axiom visualization that no competitor offers.

## Prerequisites
- Video 98: Proof Writing Style (proof techniques)
- Video 83: Equivalence Relations (from Discrete Math — useful but not required)
- General familiarity with sets, functions, and basic proof techniques

## Learning Objectives
1. Understand what a group is through intuitive examples (symmetries, integers, modular arithmetic)
2. State and explain the four group axioms: closure, associativity, identity, inverse
3. Verify that familiar structures (Z under +, Z_n under +, symmetries of a triangle) satisfy all axioms
4. Identify non-examples and explain which axiom fails
5. Define abelian groups and distinguish commutative from non-commutative groups
6. Appreciate why the group concept unifies seemingly different mathematical structures

## Scene Plan (9 scenes, ~15 min)

### Scene 1: Hook — The Symmetry of a Triangle (~80s)
- play_intro("Groups — Definition and Examples", "Abstract Algebra I")
- Animated: regular triangle with color-coded rotations (0°, 120°, 240°) and reflections (3 axes)
- "Look at this triangle. If you rotate it 120 degrees, it looks the same. These symmetries form a group."
- "Throughout mathematics, the same pattern shows up: integers under addition, matrices under multiplication, Rubik's cube moves, even the symmetries of a snowflake."
- "Today we define this pattern precisely — and discover the power of abstraction."
- Preview: pattern → axioms → examples → non-examples → abelian groups

### Scene 2: What Pattern Do We See? (~70s)
- Section: "1 — The Common Pattern"
- Show 3 examples side by side (progressive reveal):
  1. Integers under +: combine any two, get another; 0 does nothing; negatives undo
  2. Z_6 under +: same idea, but we wrap around (clock arithmetic); 0 is still identity
  3. Symmetries of a triangle: compose two symmetries, get a third; "do nothing" is the identity; each symmetry has an inverse
- "In every case: we have a SET of things and a WAY TO COMBINE them, and three special properties hold."
- Build anticipation: "Let's name these properties precisely."

### Scene 3: The Four Axioms (~90s)
- Section: "2 — Definition of a Group"
- Formal definition with color-coded axiom cards:
  - Closure (PRIMARY): For all a, b in G, a * b is in G
  - Associativity (SECONDARY): For all a, b, c in G, (a * b) * c = a * (b * c)
  - Identity (ACCENT): There exists e in G such that e * a = a * e = a
  - Inverse (RED): For every a in G, there exists a^{-1} such that a * a^{-1} = e
- "Notice: commutativity is NOT on this list. That's not an accident — we'll see why soon."
- Each axiom appears as a colored card with MathTex formula, building up one at a time

### Scene 4: Example 1 — The Integers Under Addition (~70s)
- Section: "3 — Example: (Z, +)"
- Verify each axiom for Z under addition:
  - Closure: sum of two integers is an integer (check)
  - Associativity: (a+b)+c = a+(b+c) (check)
  - Identity: e = 0 (check)
  - Inverse: a^{-1} = -a (check)
- "So (Z, +) is a group. This is our first verified example."
- Brief: "Notice the star (*) is just a symbol for the operation. Here, star means addition."

### Scene 5: Example 2 — Modular Arithmetic (~70s)
- Section: "4 — Example: (Z_n, +)"
- Z_6 under addition mod 6: {0, 1, 2, 3, 4, 5}
- Verify briefly: closure (sum mod 6 stays in Z_6), identity (0), inverse (6-n)
- Visual: a clock face with arithmetic operations
- "This is the same pattern as Z, but we've wrapped it around. The group structure is identical in spirit."
- "These are called CYCLIC groups — and we'll dedicate a whole video to them later."

### Scene 6: Non-Examples (~80s)
- Section: "5 — What's NOT a Group?"
- Non-example 1: Integers under multiplication (Z, *)
  - Closure: yes. Associativity: yes. Identity: e=1, yes.
  - Inverse: 2^{-1} = 1/2 not an integer. FAILS.
  - "Almost a group — but one axiom fails. That's enough to disqualify it."
- Non-example 2: Integers under subtraction (Z, -)
  - Associativity: (5-3)-2 = 0, but 5-(3-2) = 4. FAILS.
  - "A single counterexample destroys the axiom."
- Visual: each non-example shown with the failing axiom highlighted in RED

### Scene 7: Abelian Groups — The Twist (~70s)
- Section: "6 — Abelian Groups"
- "Here's the surprise: in the group axioms, we never required a * b = b * a."
- Definition: A group is ABELIAN (commutative) if a * b = b * a for all a, b.
- Example: (Z, +) is abelian — obviously, addition commutes.
- Non-example: Symmetries of a triangle — rotate then reflect is NOT the same as reflect then rotate.
- Visual: animate the two compositions on a triangle to show they give different results
- "Non-abelian groups are everywhere — matrix multiplication, symmetries, permutations. The Rubik's cube group is non-abelian: doing move A then move B is generally different from B then A."
- Named after Niels Henrik Abel (1802–1829) — brief historical note

### Scene 8: The Big Picture (~50s)
- Section: "7 — Why Groups Matter"
- Connect: groups unify integers, symmetries, matrices, permutations, polynomials under one framework
- "When you prove a theorem about groups, it applies to ALL of these at once."
- "This is the power of abstraction: study the structure, and the applications follow."
- Preview upcoming: "Next — Subgroups. What subsets of a group are themselves groups?"
- Brief roadmap: "Subgroups → Cyclic Groups → Permutations → Cosets → Homomorphisms → Quotient Groups → Rings & Fields"

### Scene 9: Summary + Outro (~60s)
- Key takeaways (4 items, one at a time):
  1. A group is a set with an operation satisfying closure, associativity, identity, inverse
  2. Familiar examples: (Z, +), (Z_n, +), symmetries, invertible matrices
  3. Non-examples fail at least one axiom
  4. Abelian = commutative; non-abelian groups are common and important
- "You now know what a group is — the foundational object of abstract algebra."
- play_outro("Groups: Definition and Examples", "Abstract Algebra I")
