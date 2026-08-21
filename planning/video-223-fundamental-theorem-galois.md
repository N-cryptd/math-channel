# Video 223: Fundamental Theorem of Galois Theory — Plan

## Metadata
- **Number:** 223
- **Topic:** Fundamental Theorem of Galois Theory (FTGT)
- **Level:** Graduate (Advanced Abstract Algebra)
- **Class:** Video223_FundamentalTheoremGalois
- **Script:** scripts/graduate/video-223-fundamental-theorem-galois.py
- **Builds on:** Video 222 (Galois Theory — Aut(E/F), fixed fields, correspondence teaser)
- **Leads to:** Video 224 (Applications of Galois Theory — solvability by radicals)
- **Estimated duration:** 10-14 minutes

## Competitive Analysis

See channel-analysis/improvements.md [2026-08-20] entry for full analysis.

**5 competitors analyzed:** Aleph 0 (314K, animated lattice, skips formal parts), Richard Borcherds (33K, full proof, whiteboard), Dr. Peyam (120K, thorough, dry), Michael Penn (80-150K, computational, whiteboard), Mathemaniac (from 222 analysis, dial metaphor, no full FTGT).

**Key market gap:** NO competitor covers the FTGT with BOTH (a) animated lattice visuals AND (b) full formal statement including normal subgroups and the degree formula.

**Our positioning:** The definitive animated FTGT video. Aleph 0 has the visuals but skips the definitions. Borcherds/Dr. Peyam have the rigor but no animation. We do both.

**Running example:** Q(sqrt2, sqrt3)/Q — degree 4 extension, Galois group V4 (Klein four). Rich enough to show subgroups, intermediate fields, normal subgroups, and the degree formula.

**Techniques to adopt:**
- Aleph 0's animated lattice visualization (subgroup field correspondence)
- Aleph 0's storytelling: state theorem early as big picture, then prove each part
- Michael Penn's computational examples (but animated)
- Use Q(sqrt2, sqrt3)/Q as a running example throughout (richer than Q(sqrt2)/Q)

**Techniques to avoid:**
- Skipping the Galois extension definition (Aleph 0 does this; we define it)
- 25-minute single-video approach (too long; 222 already covered Galois groups)
- Proving every part in full detail (prove main ideas, state the rest)
- Borcherds/Dr. Peyam's wall-of-formalism with no visual relief

## Scene Plan (8 scenes)

### Scene 1: Hook — The Perfect Correspondence (50s)
**Content budget:** intro animation + title + 3 progressive items
**Narration (~30s):** "Last time we defined Galois groups and fixed fields, and we saw a tantalizing preview: subgroups of the Galois group seem to correspond to intermediate fields. Today we make this precise. The Fundamental Theorem of Galois Theory is one of the most beautiful results in all of algebra. It says that for a Galois extension, the lattice of subgroups and the lattice of intermediate fields are perfect mirrors of each other — with inclusion reversed."

- play_intro("Fundamental Theorem of Galois Theory", "Advanced Abstract Algebra")
- Title: "The Perfect Correspondence"
- 3 progressive items:
  1. "Last time: Galois groups and fixed fields"
  2. "Subgroups of Gal(E/F) seem to correspond to intermediate fields"
  3. "Today: the Fundamental Theorem makes this precise"

### Scene 2: Galois Extensions — The Definition (65s)
**Content budget:** section divider + title + definition box + 3 conditions
**Narration (~30s):** "Before stating the theorem, we need one crucial definition. A field extension E over F is called a Galois extension if it satisfies two equivalent conditions. First: E is the splitting field of a separable polynomial over F. Second, and more useful for us: the fixed field of the full Galois group is exactly the base field. That is, the fixed field of Gal(E/F) equals F itself. This means the Galois group is large enough to capture all the structure."

- Section divider: "1 — Galois Extensions"
- Title: "Galois Extensions"
- Definition box (formula_box): E/F is Galois if E^{Gal(E/F)} = F
- Equivalent: E is the splitting field of a separable polynomial over F
- Key insight: "The Galois group is large enough — no extra symmetries are missing"

### Scene 3: The Theorem Statement — Big Picture (80s)
**Content budget:** section divider + title + theorem box + 4 parts listed progressively
**Narration (~35s):** "Here is the Fundamental Theorem. Let E over F be a finite Galois extension. Then there is an inclusion-reversing bijection between subgroups of Gal(E/F) and intermediate fields between F and E. The maps are: from a subgroup H, take the fixed field E to the H. And from an intermediate field K, take Gal(E/K). Furthermore, the degree of the extension E over K equals the order of H, and K over F equals the index of H in Gal(E/F). Finally, H is a normal subgroup if and only if K is a Galois extension of F."

- Section divider: "2 — The Fundamental Theorem"
- Title: "The Fundamental Theorem of Galois Theory"
- Theorem box with main statement
- 4 parts revealed progressively:
  1. Inclusion-reversing bijection
  2. Maps: H -> E^H and K -> Gal(E/K)
  3. Degree formula: [E:K] = |H|, [K:F] = [G:H]
  4. Normal subgroups <-> Galois subextensions

### Scene 4: Running Example — Gal(Q(sqrt2, sqrt3)/Q) (80s)
**Content budget:** section divider + title + field tower + Galois group elements
**Narration (~35s):** "Let's see this in action with our running example. Consider Q of square root of 2, square root of 3 over Q. This has degree 4, and it's the splitting field of the polynomial x squared minus 2 times x squared minus 3, which is separable, so it's a Galois extension. The Galois group has four elements. There's the identity, the map that sends sqrt2 to minus sqrt2, the map that sends sqrt3 to minus sqrt3, and the composition that flips both. This is the Klein four group V4."

- Section divider: "3 — Running Example"
- Title: "Gal(Q(sqrt2, sqrt3)/Q)"
- Show: degree 4, splitting field of (x^2-2)(x^2-3)
- Show 4 automorphisms: id, sigma_2, sigma_3, sigma_2*sigma_3
- Result: Galois group = V4 (Klein four)

### Scene 5: The Lattice — Subgroups and Intermediate Fields (90s)
**Content budget:** section divider + title + two-column lattice diagram
**Narration (~40s):** "Now the magic. V4 has five subgroups: the whole group, the trivial subgroup, and three subgroups of order 2. On the field side, the intermediate fields are: Q, the whole extension, and three quadratic extensions. Let me show you the lattice. On the left, subgroups ordered by inclusion. On the right, intermediate fields. Watch how the maps work. The subgroup generated by sigma_2 fixes Q of sqrt3. The subgroup generated by sigma_3 fixes Q of sqrt2. And the subgroup generated by sigma_2 sigma_3 fixes Q of sqrt 6. The correspondence is perfect and inclusion-reversing."

- Section divider: "4 — The Lattice"
- Title: "Subgroup-Field Correspondence"
- Two-column lattice: subgroups (left) and intermediate fields (right)
- Animate the correspondence arrows connecting them
- Show 3 intermediate fields: Q(sqrt3), Q(sqrt2), Q(sqrt6)
- Highlight inclusion-reversing property

### Scene 6: Normal Subgroups and Galois Subextensions (75s)
**Content budget:** title + definition + example + visual highlight on lattice
**Narration (~30s):** "The deepest part of the theorem connects normal subgroups to Galois extensions. A subgroup H of Gal(E/F) is normal if and only if its fixed field K is a Galois extension of F. In our example, all three order-2 subgroups of V4 are normal, because V4 is abelian. And indeed, all three intermediate fields Q of sqrt2, Q of sqrt3, and Q of sqrt6 are Galois over Q — they're all splitting fields of separable polynomials. In general, when H is not normal, K over F fails to be Galois."

- Section divider: "5 — Normal Subgroups"
- Title: "Normal Subgroups and Galois Extensions"
- Statement: H normal in G iff E^H/F is Galois
- Visual: highlight the lattice connections that are normal
- Example: all subgroups of V4 are normal (V4 is abelian)
- All intermediate fields are Galois over Q

### Scene 7: The Degree Formula (65s)
**Content budget:** title + formula box + worked example
**Narration (~30s):** "Finally, the degree formula ties the group theory and field theory together. If H is a subgroup with fixed field K, then the degree of E over K equals the order of H, and the degree of K over F equals the index of H in G. In our example, each order-2 subgroup has fixed field of degree 2 over Q. And 2 times 2 equals 4, the degree of the full extension. The degree formula is what makes the correspondence not just a set bijection, but a structural isomorphism of lattices."

- Section divider: "6 — The Degree Formula"
- Title: "Degrees and Group Orders"
- Formula box: [E : E^H] = |H|, [E^H : F] = [G : H]
- Worked example: |<sigma_2>| = 2, [Q(sqrt2,sqrt3) : Q(sqrt3)] = 2
- Key: 2 x 2 = 4 = [Q(sqrt2,sqrt3) : Q]

### Scene 8: Summary and Outro (45s)
**Content budget:** title + 5 takeaway items + outro
**Narration (~25s):** "Let's recap. A Galois extension is one where the fixed field of the full Galois group is exactly the base field. The Fundamental Theorem gives an inclusion-reversing bijection between subgroups and intermediate fields. The degree formula connects extension degrees to group orders and indices. Normal subgroups correspond to Galois subextensions. And in our example, Q of sqrt2, sqrt3 over Q, the Klein four group and the three quadratic intermediate fields perfectly illustrate all parts of the theorem."

- Section divider: "7 — Summary"
- Title: "Key Takeaways"
- 5 progressive items:
  1. "E/F Galois: E^{Gal(E/F)} = F"
  2. "Inclusion-reversing bijection: subgroups <-> intermediate fields"
  3. "Maps: H -> E^H and K -> Gal(E/K)"
  4. "Normal subgroups <-> Galois subextensions"
  5. "Degree formula: [E:E^H] = |H|"
- play_outro("Applications of Galois Theory", "Advanced Abstract Algebra")

## Visual Design Notes
- The lattice diagram (Scene 5) is the visual CLIMAX — invest the most time here
- Subgroups on left in PRIMARY, intermediate fields on right in SECONDARY, correspondence arrows in ACCENT
- Normal subgroup connections get a special glow (SECONDARY border)
- The degree formula scene uses a formula_box highlight in ACCENT
- Running example Q(sqrt2, sqrt3)/Q should appear consistently across scenes 4-7
- Show the Klein four group as a visual element (4 dots connected, like a diamond)
- Animate automorphisms as permutations: show sqrt2 -> +-sqrt2 and sqrt3 -> +-sqrt3

## Thumbnail Concept
Dark BG (#1A1832) with the subgroup lattice (left) and field lattice (right) connected by glowing ACCENT arrows. The V4 group at top-left, Q(sqrt2, sqrt3) at top-right. Text: "The Fundamental Theorem of Galois Theory" in ACCENT. A single glowing connection arrow in the center.
