# Video 116: Group Homomorphisms

**Playlist:** Abstract Algebra I (Video 6 of 12)
**Level:** Undergraduate (Abstract Algebra)
**Class:** Video116_GroupHomomorphisms
**Script:** scripts/undergraduate/video-116-group-homomorphisms.py

## Prerequisites
- Video 111: Groups — Definition and Examples
- Video 112: Subgroups and Cyclic Groups
- Video 114: Cosets and Lagrange's Theorem
- Video 115: Normal Subgroups and Quotient Groups

## Competitive Analysis Summary
- **Socratica** (abstract algebra playlist, now pivoted to coding): Covered homomorphisms with definition → properties → kernel/image flow. Used Manim animations with colored element mapping diagrams. ~200K views total for the playlist.
- **The Math Sorcerer** (whiteboard style): Dense proof-heavy coverage. Works through proofs line by line on a blackboard. Good for rigor, poor for intuition-building.
- **Michael Penn** (whiteboard): Problem-focused approach — works through specific homomorphism verification exercises. Less conceptual, more computational.
- **Our approach:** Start with the intuition of "structure-preserving maps" using real-world analogies (functions that respect patterns). Then formal definition → key examples (determinant, sign, logarithm) → properties (identity, inverses, powers) → kernel and image → why kernel is always normal → tease the First Isomorphism Theorem. Distinctive visual: animated element-mapping diagrams showing how homomorphisms "collapse" group structure.

## Learning Objectives
1. Define a group homomorphism and verify that a map preserves the operation
2. Understand the key examples: determinant, sign map, logarithm, modular reduction
3. Prove that homomorphisms preserve identity, inverses, and powers
4. Define and work with the kernel of a homomorphism
5. Define and work with the image of a homomorphism
6. Prove that the kernel is always a normal subgroup
7. Understand why the First Isomorphism Theorem connects homomorphisms to quotient groups

## Scene Plan (8 scenes, ~12 min)

### Scene 1: Hook — Structure-Preserving Maps (~70s)
- play_intro("Group Homomorphisms", "Abstract Algebra I")
- Recall: functions between sets, but what about functions between GROUPS?
- "A homomorphism is a function that RESPECTS the group structure."
- "If a · b = c in G, then φ(a) · φ(b) = φ(c) in H."
- "The operation commutes with the function."
- Visual analogy: a map that sends patterns to patterns

### Scene 2: Formal Definition (~80s)
- Section: "1 — Definition"
- φ: G → H is a homomorphism if φ(ab) = φ(a)φ(b) for all a, b ∈ G
- Boxed definition with notation
- "The order of operations matters: we multiply in G first, then map. Or equivalently, map each element, then multiply in H. Same result."
- Notation convention: φ(1) or φ(e) for identity image

### Scene 3: Key Examples (~80s)
- Section: "2 — Examples"
- Example 1: det: GL(n,ℝ) → ℝ*
  - det(AB) = det(A)·det(B)
  - Captures "size/volume" of linear transformations
- Example 2: sign: S_n → {±1}
  - sign(σ·τ) = sign(σ)·sign(τ)
  - Even permutations → +1, odd → -1
- Example 3: log: (ℝ⁺, ×) → (ℝ, +)
  - log(ab) = log(a) + log(b)
  - Converts multiplication to addition

### Scene 4: Properties of Homomorphisms (~80s)
- Section: "3 — Properties"
- Property 1: φ(e_G) = e_H (identity maps to identity)
  - Proof: φ(e) = φ(e·e) = φ(e)φ(e), so e_H = φ(e)
- Property 2: φ(g⁻¹) = φ(g)⁻¹ (inverses map to inverses)
  - Proof: e_H = φ(e) = φ(g·g⁻¹) = φ(g)φ(g⁻¹)
- Property 3: φ(gⁿ) = φ(g)ⁿ (powers map to powers)
  - Proof by induction from φ(g·g) = φ(g)φ(g)

### Scene 5: Kernel (~80s)
- Section: "4 — The Kernel"
- Definition: ker(φ) = {g ∈ G : φ(g) = e_H}
- Visual: elements that map to the identity — they "collapse" to one point
- Key example: ker(det) = SL(n,ℝ) (matrices with determinant 1)
- Key example: ker(sign) = A_n (the alternating group — even permutations)
- Theorem: ker(φ) is always a subgroup of G

### Scene 6: Image (~70s)
- Section: "5 — The Image"
- Definition: im(φ) = {φ(g) : g ∈ G} ⊆ H
- Visual: everything in H that gets "hit" by φ
- Key example: im(det) = ℝ* (surjective onto non-zero reals)
- Theorem: im(φ) is always a subgroup of H
- Contrast: kernel lives in the DOMAIN, image lives in the CODOMAIN

### Scene 7: Kernel is Normal (~80s)
- Section: "6 — Why the Kernel is Special"
- Theorem: ker(φ) ◁ G (kernel is always a normal subgroup)
- Proof outline: if k ∈ ker(φ) and g ∈ G, then φ(gkg⁻¹) = φ(g)φ(k)φ(g)⁻¹ = φ(g)·e_H·φ(g)⁻¹ = e_H
- So gkg⁻¹ ∈ ker(φ), meaning ker(φ) is closed under conjugation
- "This is the deep connection between homomorphisms and normal subgroups."
- "Every normal subgroup arises as the kernel of some homomorphism."

### Scene 8: Summary + Teaser (~60s)
- Key takeaways:
  1. A homomorphism preserves the group operation: φ(ab) = φ(a)φ(b)
  2. Identity, inverses, and powers are all preserved
  3. The kernel = elements mapping to identity (always a normal subgroup)
  4. The image = elements in the codomain that get hit (always a subgroup)
  5. Normal subgroups and homomorphisms are two sides of the same coin
- Teaser: "Next — The Isomorphism Theorems, including the powerful result that G/ker(φ) ≅ im(φ)"
- play_outro("Group Homomorphisms", "Abstract Algebra I")
