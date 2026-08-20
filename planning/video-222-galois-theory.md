# Video 222: Galois Theory — Plan

## Metadata
- **Number:** 222
- **Topic:** Galois Theory (Galois Groups, Aut(E/F), Fixed Fields, Correspondence)
- **Level:** Graduate (Advanced Abstract Algebra)
- **Class:** Video222_GaloisTheory
- **Script:** scripts/graduate/video-222-galois-theory.py
- **Builds on:** Video 219 (Field Extensions), Video 220 (Algebraic Extensions), Video 221 (Splitting Fields)
- **Leads to:** Video 223 (Fundamental Theorem of Galois Theory — full proof)
- **Estimated duration:** 10-14 minutes

## Competitive Analysis

See channel-analysis/improvements.md [2026-08-19] entry for full analysis.

**7 competitors analyzed:** Mathemaniac (549K, "dial" metaphor, skips definitions), Aleph 0 (314K, √2 hook, pink scheme, skips Aut/Fixed), Math Visualized (564K, "trousers" metaphor, very simplified), Michael Penn (computation-focused whiteboard), Socratica (historical motivation, light rigor), BriTheMathGuy (accessible but surface-level), Dr. Peyam (most thorough, 50-min lectures, dry).

**Key market gap:** All high-view-count competitors (Mathemaniac, Aleph 0, Math Visualized) SKIP the formal definitions. Michael Penn and Dr. Peyam have the definitions but no animations. NO competitor combines animation quality with computational depth for Aut(E/F) + fixed fields + correspondence.

**Our positioning:** The video that gives you the DEFINITIONS and EXAMPLES the popular videos assume. After watching Mathemaniac/Aleph 0, you understand the big idea. After watching our video, you can actually compute Galois groups.

**Techniques to adopt from competitors:**
- Mathemaniac's storytelling structure (each section raises a question the next answers)
- Aleph 0's concrete √2 hook
- Mathemaniac's "dial" metaphor for field automorphisms (adapted to concrete examples)
- Michael Penn's computational examples (but animated)
- Socratica's historical motivation (brief, in the hook)

**Techniques to avoid:**
- Skipping definitions (competitors do this; we must not)
- 45-minute epic length
- Math Visualized's non-standard "trousers" metaphor
- Pure whiteboard without visual intuition

## Scene Plan (7 scenes)

### Scene 1: Hook — The Mystery of Field Symmetries (45s)
**Content budget:** intro animation + 3 text items
**Narration (~25s):** "In the last few videos we built up the machinery of field extensions — algebraic elements, minimal polynomials, splitting fields. But there's a question we haven't asked yet: what are the SYMMETRIES of a field extension? If we adjoin √2 to Q, what maps does Q(√2) have that preserve the field structure? This question — and its stunning answer — is Galois theory."

- play_intro("Galois Theory", "Advanced Abstract Algebra")
- Title: "The Symmetries of Field Extensions"
- 3 progressive items:
  1. "Field extensions: Q ⊂ Q(√2) ⊂ Q(√2, i)"
  2. "Question: what maps preserve the algebraic structure?"
  3. "Galois groups encode these symmetries"

### Scene 2: Field Automorphisms — Definition (60s)
**Content budget:** title + definition box + 3 conditions
**Narration (~30s):** "A field automorphism is a bijective map from a field to itself that preserves addition and multiplication. For a field extension E over F, we're interested in automorphisms of E that fix every element of F. These form a group called Aut(E over F)."

- Section divider: "1 — Field Automorphisms"
- Title: "Field Automorphisms"
- Definition box: σ: E → E, bijective, σ(a+b) = σ(a) + σ(b), σ(ab) = σ(a)σ(b)
- Key point: Aut(E/F) = {σ ∈ Aut(E) : σ(c) = c for all c ∈ F}
- Note: Aut(E/F) forms a GROUP under composition

### Scene 3: Example — Gal(Q(√2)/Q) (75s)
**Content budget:** title + field elements + automorphism table + result
**Narration (~35s):** "Let's compute our first Galois group. Every element of Q(√2) can be written as a + b√2. An automorphism σ fixing Q must send √2 to another root of x²−2, so either √2 or −√2. This gives exactly two automorphisms: the identity and the map sending √2 to −√2. So Gal(Q(√2)/Q) is isomorphic to Z/2Z."

- Section divider: "2 — First Example"
- Title: "Gal(Q(√2)/Q)"
- Show: elements are a + b√2
- Show: σ(√2) must satisfy x²−2, so σ(√2) = ±√2
- Table: id: a+b√2 → a+b√2, σ: a+b√2 → a−b√2
- Result: Gal(Q(√2)/Q) ≅ Z/2Z
- Visual: two dots (±√2) on a number line with arrows showing identity and swap

### Scene 4: Example — Gal(Q(ζ₃)/Q) (75s)
**Content budget:** title + definition of ζ₃ + automorphisms + result
**Narration (~35s):** "Now a richer example. Let ζ₃ be a primitive cube root of unity, e to the 2πi/3. The minimal polynomial of ζ₃ over Q is x² + x + 1. An automorphism must send ζ₃ to another root, either ζ₃ itself or ζ₃ squared. This gives Gal(Q(ζ₃)/Q) ≅ Z/2Z as well — same group, different reason."

- Section divider: "3 — Second Example"
- Title: "Gal(Q(ζ₃)/Q)"
- Define ζ₃ = e^{2πi/3}, show ζ₃² + ζ₃ + 1 = 0
- Roots of x²+x+1: ζ₃ and ζ₃²
- Two automorphisms: id and σ(ζ₃) = ζ₃²
- Result: Gal(Q(ζ₃)/Q) ≅ Z/2Z
- Visual: two dots on the unit circle showing the swap

### Scene 5: Fixed Fields (70s)
**Content budget:** title + definition + diagram + example computation
**Narration (~30s):** "Given a group G of automorphisms of E, the fixed field of G is the set of all elements of E that every automorphism in G leaves unchanged. For a subgroup H of the Galois group, the fixed field E^H gives us a field between F and E. This is one half of the Galois correspondence."

- Section divider: "4 — Fixed Fields"
- Title: "Fixed Fields"
- Definition: E^H = {x ∈ E : σ(x) = x for all σ ∈ H}
- Example: For Gal(Q(√2)/Q) = {id, σ}, what is Q(√2)^{σ}?
  - σ(a+b√2) = a−b√2 = a+b√2 iff b=0, so fixed field = Q
- Diagram: Q ⊂ fixed field ⊂ E with Galois group above

### Scene 6: The Galois Correspondence — Teaser (70s)
**Content budget:** title + lattice diagram + key theorem statement
**Narration (~30s):** "Here's the remarkable theorem: for a Galois extension E over F, there is a perfect one-to-one correspondence between subgroups of the Galois group and intermediate fields. Reversing inclusion. Subgroups of order 2 correspond to extensions of degree 2. Normal subgroups correspond to Galois sub-extensions. This is the Fundamental Theorem of Galois Theory, and we'll prove it in the next video."

- Section divider: "5 — The Galois Correspondence"
- Title: "The Fundamental Theorem"
- Lattice diagram: subgroups on left, intermediate fields on right, with arrows connecting them (inclusion-reversing)
- Key statement: "Subgroups of Gal(E/F) ↔ Intermediate fields between F and E"
- Normal subgroups ↔ Galois subextensions
- Tease: "Full proof in the next video"

### Scene 7: Summary and Outro (40s)
**Content budget:** 4 takeaway items + outro
**Narration (~20s):** "Let's recap. Field automorphisms that fix the base field form the Galois group. We computed Gal(Q(√2)/Q) and Gal(Q(ζ₃)/Q), both isomorphic to Z/2Z. Fixed fields give us intermediate fields from subgroups. And the Galois correspondence — the Fundamental Theorem — links subgroups and intermediate fields in a perfect, inclusion-reversing pairing."

- Section divider: "6 — Summary"
- Title: "Key Takeaways"
- 4 progressive items:
  1. "Gal(E/F) = field automorphisms fixing F"
  2. "Gal(Q(√2)/Q) ≅ Z/2Z: identity + conjugation"
  3. "Fixed field E^H: elements unchanged by all σ ∈ H"
  4. "Galois correspondence: subgroups ↔ intermediate fields"
- play_outro("The Galois Correspondence", "Advanced Abstract Algebra")

## Visual Design Notes
- Color-code: automorphisms in PRIMARY, fixed fields in SECONDARY, the correspondence arrows in ACCENT
- The Galois correspondence lattice is the visual climax — animate subgroups on left, fields on right, with arrows connecting them
- Use Mathemaniac's "dial" idea subtly: show automorphisms as permutations of roots on a circle
- Nested field diagram: F ⊂ E with Gal(E/F) above, showing the connection
- For Gal(Q(√2)/Q): animate the two roots ±√2 on a number line, show the identity (no move) and the swap (arrow crossing)
- For Gal(Q(ζ₃)/Q): show ζ₃ and ζ₃² as points on the unit circle in the complex plane, show the swap as a rotation/reflection

## Thumbnail Concept
Dark BG (#1A1832) with a field tower Q ⊂ Q(√2) on the left, and the group Z/2Z on the right, connected by a glowing ACCENT (#FFD166) double arrow. Two dots (±√2) in PRIMARY with arrows between them showing the automorphism. Text: "Galois Theory: The Symmetries of Fields".
