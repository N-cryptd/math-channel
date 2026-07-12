# Video 114: Cosets and Lagrange's Theorem

**Playlist:** Abstract Algebra I (Video 5 of 12)
**Level:** Undergraduate (Abstract Algebra)
**Class:** Video114_CosetsAndLagrangesTheorem
**Script:** scripts/undergraduate/video-114-cosets-and-lagranges-theorem.py

## Prerequisites
- Video 111: Groups — Definition and Examples
- Video 112: Subgroups and Cyclic Groups
- Video 113: Permutation Groups

## Learning Objectives
1. Define left and right cosets of a subgroup H in G
2. Understand cosets partition the group into equal-size blocks
3. Visualize cosets with concrete examples (Z_6, S_3)
4. State Lagrange's Theorem: |H| divides |G|
5. Apply Lagrange's Theorem: element order divides |G|, prime-order groups are cyclic

## Scene Plan (9 scenes, ~12 min)

### Scene 1: Hook — Partitioning a Group (~70s)
- play_intro("Cosets and Lagrange's Theorem", "Abstract Algebra I")
- Visual: Z_6 elements on a circle, subgroup {0, 3} highlighted, then offset copies {1, 4} and {2, 5} shown in different colors
- "If you have a subgroup H inside a group G, what happens if you 'shift' every element of H by some fixed element g?"
- "You get another block the same size as H. These blocks partition G perfectly."
- "This simple observation leads to one of the most powerful theorems in all of group theory."

### Scene 2: Definition of Cosets (~80s)
- Section: "1 — Left Cosets"
- Formal definition: gH = {gh : h in H}
- Right cosets: Hg = {hg : h in G}
- "gH is called the LEFT coset of H by g. It's everything you get by taking each element of H and multiplying by g on the LEFT."
- Visual: Show H = {0, 3} in Z_6, then compute 1+H = {1, 4}, 2+H = {2, 5}
- Color-coded blocks for each coset
- Note: "g is called the REPRESENTATIVE of the coset gH."

### Scene 3: Example — Cosets in Z_6 (~70s)
- Section: "2 — Example: Z_6"
- Full walkthrough: G = Z_6 = {0,1,2,3,4,5}, H = {0, 3} = <3>
- Compute all left cosets:
  - 0+H = {0, 3} (H itself)
  - 1+H = {1, 4}
  - 2+H = {2, 5}
  - 3+H = {3, 0} = H (duplicate!)
  - 4+H = {4, 1} = 1+H (duplicate!)
  - 5+H = {5, 2} = 2+H (duplicate!)
- Visual: color-coded table or circles showing the three distinct cosets
- "We only get THREE distinct cosets, each of size TWO."
- "This is no accident — it's Lagrange's Theorem in action."

### Scene 4: Properties of Cosets (~70s)
- Section: "3 — Key Properties"
- Property 1: g is in gH (because g = g·e and e is in H)
- Property 2: If gH = kH then g and k differ by an element of H
  - gH = kH iff g^(-1)k is in H
- Property 3: Either gH = kH or gH ∩ kH = ∅ (cosets are either equal or disjoint)
- Property 4: |gH| = |H| for all cosets (the map h -> gh is a bijection)
- Visual: each property displayed as a colored card, one at a time

### Scene 5: Example — Cosets in S_3 (~70s)
- Section: "4 — Example: S_3"
- G = S_3 = {e, (12), (13), (23), (123), (132)}, H = A_3 = {e, (123), (132)}
- Compute left cosets:
  - eH = H = {e, (123), (132)}
  - (12)H = {(12), (12)(123), (12)(132)} = {(12), (13), (23)}
- "Only TWO distinct cosets, each of size THREE."
- "Two cosets, three elements each, and 2 times 3 equals 6, which is |S_3|."
- Visual: colored partition of S_3 elements

### Scene 6: Lagrange's Theorem Statement (~60s)
- Section: "5 — Lagrange's Theorem"
- Formal statement (boxed): If H is a subgroup of G, then |H| divides |G|
- Define the INDEX: [G : H] = number of distinct cosets of H in G
- Then |G| = [G:H] · |H|
- "This is one of the most-used theorems in group theory."
- Visual: the equation |G| = [G:H] · |H| displayed prominently
- Historical note: Joseph-Louis Lagrange (1736–1813)

### Scene 7: Proof Sketch of Lagrange's Theorem (~80s)
- Section: "6 — Proof"
- Step 1: Cosets partition G (by Property 3: disjoint or equal)
- Step 2: All cosets have the same size as H (by Property 4: bijection)
- Step 3: Count: if there are [G:H] distinct cosets, each of size |H|...
- Then |G| = [G:H] · |H|
- Visual: animated partition of G into equal-sized blocks
- "The proof is remarkably short — three observations, and we're done."

### Scene 8: Applications (~70s)
- Section: "7 — Applications"
- Application 1: Order of an element divides |G|
  - For any g in G, |<g>| = order(g) divides |G|
  - Proof: <g> is a subgroup, apply Lagrange
- Application 2: Groups of prime order are cyclic
  - If |G| = p (prime), then for any non-identity g, order(g) divides p and is > 1
  - So order(g) = p, meaning <g> = G
  - "There is essentially only one group of prime order — the cyclic group."
- Application 3: Fermat's Little Theorem teaser
  - "Lagrange's Theorem gives us a clean proof that a^(p-1) ≡ 1 (mod p)"
  - "We'll see this connection when we study group homomorphisms."

### Scene 9: Summary + Outro (~60s)
- Key takeaways:
  1. A left coset gH shifts subgroup H by g
  2. Cosets partition G into equal-size blocks
  3. Lagrange's Theorem: |H| divides |G|
  4. The index [G:H] = |G|/|H| counts the cosets
  5. Order of any element divides |G|
- Preview: "Next — Group Homomorphisms: structure-preserving maps between groups."
- play_outro("Cosets and Lagrange's Theorem", "Abstract Algebra I")
