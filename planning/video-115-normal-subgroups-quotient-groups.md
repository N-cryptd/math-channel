# Video 115: Normal Subgroups and Quotient Groups

**Playlist:** Abstract Algebra I (Video 5 of 12)
**Level:** Undergraduate (Abstract Algebra)
**Class:** Video115_NormalSubgroupsQuotientGroups
**Script:** scripts/undergraduate/video-115-normal-subgroups-quotient-groups.py

## Prerequisites
- Video 111: Groups — Definition and Examples
- Video 112: Subgroups and Cyclic Groups
- Video 113: Permutation Groups
- Video 114: Cosets and Lagrange's Theorem

## Competitive Analysis Summary
- **Socratica** (460K views): Motivates via congruences (Z/nZ). Covers normal subgroups → quotient groups sequentially. Uses colored coset partitions. Focus on definition-check-example pattern.
- **Mathemaniac** (39K views): "Conjugation as change of perspective" — visual metaphor of rotating the view. Focuses on why normal subgroups matter for simple groups.
- **Our approach:** Start with the motivating question "When do cosets form a group?" → Z/nZ as prototype → formal definition → equivalent characterizations → S_3/A_3 example → why "normal" matters for building new groups from old.

## Learning Objectives
1. Understand when left and right cosets coincide: gH = Hg
2. Define normal subgroup formally (gHg⁻¹ ⊆ H)
3. Recognize Z/nZ as the motivating example of a quotient group
4. Define the quotient group G/H with its operation
5. Work through S_3/A_3 as the canonical non-abelian example

## Scene Plan (8 scenes, ~12 min)

### Scene 1: Hook — When Do Cosets Form a Group? (~70s)
- play_intro("Normal Subgroups and Quotient Groups", "Abstract Algebra I")
- Recall: cosets partition G into equal-size blocks
- Key question: "Can we make these blocks into a GROUP themselves?"
- "If we could multiply blocks together, we'd get a NEW group built from pieces of G."
- "But this doesn't always work — it requires something special about H."

### Scene 2: The Prototype — Z/nZ (~80s)
- Section: "1 — The Prototype"
- Review modular arithmetic: Z under addition, subgroup nZ
- Cosets of nZ: [0] = {..., -6, -3, 0, 3, 6, ...}, [1] = {..., -5, -2, 1, 4, 7, ...}, ...
- These cosets form Z/nZ — and they're a group under [a] + [b] = [a+b]
- "Notice: the result doesn't depend on which representatives you pick. [1]+[3] = [4] = [7] = [1]+[10]."
- "This well-definedness is everything. It's what makes the quotient group work."

### Scene 3: What Can Go Wrong? (~70s)
- Section: "2 — When Things Break"
- Consider S_3 with H = {e, (12)}. Compute left cosets:
  - eH = {e, (12)}, (13)H = {(13), (132)}, (23)H = {(23), (123)}
- Now compute right cosets:
  - He = {e, (12)}, H(13) = {(13), (123)}, H(23) = {(23), (132)}
- "The left and right cosets are DIFFERENT! (13)H ≠ H(13)."
- "If we tried to define coset multiplication, the result would depend on our choice of representative."
- "The group operation would be ILL-DEFINED."

### Scene 4: Definition of Normal Subgroup (~80s)
- Section: "3 — Normal Subgroups"
- Definition (boxed): H is normal in G (H ◁ G) if gH = Hg for all g in G
- Equivalently: gHg⁻¹ ⊆ H for all g (conjugate of any element of H stays in H)
- "A normal subgroup is one where left and right cosets always agree."
- "This means multiplication of cosets is well-defined."
- Visual: gH and Hg as two sets, highlighted to show they're equal

### Scene 5: Equivalent Conditions (~70s)
- Section: "4 — Equivalent Conditions"
- Four equivalent ways to say H ◁ G:
  1. gH = Hg for all g in G (left cosets = right cosets)
  2. gHg⁻¹ ⊆ H for all g in G (closed under conjugation)
  3. gHg⁻¹ = H for all g in G (stronger: conjugation preserves H exactly)
  4. Every left coset is also a right coset
- "Conditions 2 and 3 are equivalent because |gHg⁻¹| = |H|, so if it's contained in H, it must equal H."
- Key fact: "In abelian groups, EVERY subgroup is normal." (gh = hg, so gH = Hg)

### Scene 6: The Quotient Group G/H (~80s)
- Section: "5 — The Quotient Group"
- Definition (boxed): G/H = {gH : g in G} with operation (aH)(bH) = (ab)H
- "G/H is a group IF AND ONLY IF H is normal in G."
- Verify group axioms:
  - Closure: (aH)(bH) = (ab)H is a coset ✓
  - Identity: eH = H ✓
  - Inverse: (aH)⁻¹ = a⁻¹H ✓
  - Associativity: inherited from G ✓
- "The KEY is well-definedness — why (aH)(bH) = (ab)H doesn't depend on representatives."
- |G/H| = [G:H] = |G|/|H| (by Lagrange)

### Scene 7: Example — S_3 / A_3 (~80s)
- Section: "6 — Example: S_3 / A_3"
- G = S_3, H = A_3 = {e, (123), (132)} (the even permutations)
- A_3 is normal in S_3 (it has index 2)
- Cosets: A_3 (even perms) and (12)A_3 (odd perms)
- Quotient group S_3/A_3 ≅ Z/2Z (just two elements: even and odd)
- Multiplication table:
  - A_3 · A_3 = A_3 (even + even = even)
  - A_3 · (12)A_3 = (12)A_3 (even + odd = odd)
  - (12)A_3 · (12)A_3 = A_3 (odd + odd = even)
- Visual: two-element group table
- "This captures the 'parity' structure of S_3 — quotient groups extract structural features."

### Scene 8: Summary + Outro (~60s)
- Key takeaways:
  1. A normal subgroup has gH = Hg for all g
  2. Normality is needed for well-defined coset multiplication
  3. The quotient group G/H has cosets as elements
  4. Z/nZ is the motivating prototype
  5. Every subgroup of an abelian group is normal
- Preview: "Next — Group Homomorphisms: structure-preserving maps between groups."
- play_outro("Normal Subgroups and Quotient Groups", "Abstract Algebra I")
