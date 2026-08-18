# Video 217: Group Actions — Advanced Abstract Algebra

## Overview
A group G *acts* on a set X when each element g ∈ G permutes X in a way compatible with the group operation. This seemingly simple idea unifies and powers: symmetry groups in geometry, Galois theory (Video 223+), conjugation classes, permutation representations, and the orbit-stabilizer theorem — the bridge between group theory and combinatorics.

## Competitive Analysis (2026-08-18)

**Market Gap:** Group actions sit at the heart of modern algebra, yet YouTube coverage is almost exclusively whiteboard lectures (Michael Penn ~5-15K views per video, The Math Sorcerer ~1-3K, Dr. Peyam ~2-5K). No Manim-animated video provides visual intuition for orbits, stabilizers, and the orbit-stabilizer theorem. The closest competitor is Socratica's Abstract Algebra series (pivoted to coding 2024+), which had clean Manim animations but never covered group actions.

**Competitors found: **
- Michael Penn: No dedicated group actions video found (covers individual problems, not systematic treatment)
- Mathologer: Covers symmetry/geometry adjacent to group actions but not the formal theory
- The Bright Side of Mathematics: Abstract Algebra playlist exists but lecture-style tablet writing
- All competitors: definition-first, no animation of orbits as moving points, no visual orbit-stabilizer connection

**Our approach (distinct):**
1. Visual-first: animate an orbit as colored dots being permuted by group elements
2. Orbit-stabilizer theorem with a visual partition proof (|G| = |Orb(x)| · |Stab(x)|)
3. Concrete running example: D_4 acting on the vertices of a square
4. Bridge to counting: Burnside's lemma as teaser for next content
5. Connection back to Abstract Algebra I (Video 113: Permutation Groups)

## Scenes (target: 12-15 min)

### Scene 1: Hook — Symmetry in Action (30s)
- **Content:** Rotations/reflections of a square permute 4 vertices. That's a group acting on a set.
- **Budget:** play_intro + 3 text items
- **Narration:** ~30 words / 12s

### Scene 2: Formal Definition (45s)
- **Content:** G × X → X with two axioms: e·x = x, g·(h·x) = (gh)·x
- **Budget:** section_divider + title + formula + 2 text items
- **Narration:** ~50 words / 20s

### Scene 3: Running Example — D_4 on Vertices (60s)
- **Content:** Label vertices 1,2,3,4. Show r (rotation) and s (reflection) acting. Show orbit of vertex 1 = {1,2,3,4}
- **Budget:** title + MathTex for permutation + 2 text items
- **Narration:** ~60 words / 24s

### Scene 4: Orbits (45s)
- **Content:** Orbit(x) = {g·x : g ∈ G}. Orbits partition X. Equivalence relation: x ~ y iff y = g·x
- **Budget:** section_divider + title + formula + 2 text items
- **Narration:** ~50 words / 20s

### Scene 5: Stabilizers (45s)
- **Content:** Stab(x) = {g ∈ G : g·x = x}. Subgroup of G. Example: Stab(vertex 1) in D_4 = {e, s_diag}
- **Budget:** section_divider + title + formula + 2 items
- **Narration:** ~50 words / 20s

### Scene 6: Orbit-Stabilizer Theorem (60s)
- **Content:** |Orb(x)| · |Stab(x)| = |G| for finite G. Key bijection proof sketch: G/Stab(x) ↔ Orb(x)
- **Budget:** section_divider + title + boxed formula + 2 text items
- **Narration:** ~60 words / 24s

### Scene 7: Visual Proof of Orbit-Stabilizer (60s)
- **Content:** Map G → Orb(x) by g ↦ g·x. Each fiber has |Stab(x)| elements. Total = |Orb(x)| × |Stab(x)|
- **Budget:** title + MathTex map + 2 text items
- **Narration:** ~60 words / 24s

### Scene 8: Conjugation Action (45s)
- **Content:** G acts on itself by conjugation: g·x = gxg^{-1}. Orbits = conjugacy classes. Stabilizer = centralizer.
- **Budget:** section_divider + title + formula + 2 text items
- **Narration:** ~50 words / 20s

### Scene 9: Examples of Conjugation in S_3 (45s)
- **Content:** S_3 conjugacy classes: {e}, {(12),(13),(23)}, {(123),(132)}. Class equation.
- **Budget:** title + MathTex + 2 text items
- **Narration:** ~50 words / 20s

### Scene 10: The Class Equation (45s)
- **Content:** |G| = |Z(G)| + Σ |Cl(x_i)|. Teaser for Sylow theorems.
- **Budget:** section_divider + title + boxed formula + 2 text items
- **Narration:** ~50 words / 20s

### Scene 11: Left Coset Action (45s)
- **Content:** G acts on G/H by g·(aH) = (ga)H. Transitive action. Kernel ⊲ G.
- **Budget:** title + formula + 2 text items
- **Narration:** ~45 words / 18s

### Scene 12: Summary + Outro (30s)
- **Content:** Key takeaways. Play outro.
- **Budget:** section_divider + title + 4 text items + play_outro
- **Narration:** ~60 words / 24s

## Key Formulas
- g · (h · x) = (gh) · x, e · x = x
- Orb(x) = {g·x : g ∈ G}
- Stab(x) = {g ∈ G : g·x = x}
- |G| = |Orb(x)| · |Stab(x)|
- |G| = |Z(G)| + Σ [G : C_G(x_i)]  (class equation)
