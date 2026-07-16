# Video 119: Group Actions

**Playlist:** Abstract Algebra I (Video 9 of 12)
**Duration target:** 10-12 minutes
**Class:** Video119_GroupActions
**Script:** scripts/undergraduate/video-119-group-actions.py

## Competitive Analysis Summary
- Mathemaniac Ch7 (42K views, 10:51): group action = homomorphism to Sym(S), Cayley's theorem
- Mathemaniac Ch2 (86K views, 12:27): counting-based orbit-stabilizer motivation, polygon examples
- 3B1B Monster (3.7M views, 22:00): action-first intuition, groups as symmetries
- Prof. Macauley (27K views, 32:35): "switchboard" metaphor, left/right actions
- MathDoctorBob (47K views, 20:19): whiteboard, orbits as equivalence classes

## Scene Plan

### Scene 1: Hook (0:00-0:35)
**Content budget: 4 items max**
- Following 3B1B's action-first approach: show a regular pentagon and ask "how many rotations send vertex 1 to vertex 3?"
- Teaser: "Groups don't just exist in isolation -- they ACT on things"
- Connect to previous videos: we defined groups, homomorphisms, quotients -- now groups in action

### Scene 2: Definition of Group Action (0:35-2:20)
**Content budget: 5 items max**
- Formal definition: G acts on X if there is a map G x X -> X satisfying identity and compatibility
- Following Prof. Macauley: "switchboard" metaphor -- each group element permutes elements of X
- Connect to homomorphism viewpoint (Mathemaniac): action = homomorphism phi: G -> Sym(X)
- Brief notation: g.x or phi(g)(x)

### Scene 3: Example -- Dihedral Group Acting on Polygon (2:20-4:00)
**Content budget: 5 items max**
- D_5 (dihedral group of order 10) acts on vertices {1,2,3,4,5} of a pentagon
- Visual: show rotation r_72 sending each vertex to the next
- Show reflection as another group element
- Connect back: this is the SAME D_5 we've seen before, but now we see it acting

### Scene 4: Orbits (4:00-5:40)
**Content budget: 5 items max**
- Definition: orbit of x = {g.x : g in G}
- Visual: show orbit of vertex 1 under D_5 = all 5 vertices (transitive)
- Orbit partition: show that orbits partition X (color-code different orbits)
- Example: S_3 acting on {1,2,3,4,5,6} -- {1,2,3} is one orbit, {4,5,6} is another
- Orbits are equivalence classes under x ~ y iff y = g.x for some g

### Scene 5: Stabilizers (5:40-7:10)
**Content budget: 5 items max**
- Definition: stabilizer of x = {g in G : g.x = x}
- Stabilizer is always a subgroup (prove briefly)
- Visual on pentagon: stabilizer of vertex 1 in D_5 = {e} (only identity fixes it)
- Contrast: D_5 acting on diagonals -- some stabilizers are larger
- Connect: stabilizer measures "how much doesn't move x"

### Scene 6: Orbit-Stabilizer Theorem (7:10-9:00)
**Content budget: 5 items max**
- Following Mathemaniac's counting argument: |G| = |Orb(x)| * |Stab(x)|
- Proof sketch: each element of the orbit is "hit" exactly |Stab(x)| times
- Visual: show the fibration / bijection between G/Stab(x) and Orb(x)
- Formula box with theorem statement
- Apply to D_5 example: |Orb(v1)| = 5, |Stab(v1)| = 2, |D_5| = 10 = 5*2

### Scene 7: Example -- Permutation Action and Cayley's Theorem (9:00-10:40)
**Content budget: 5 items max**
- Every group acts on itself by left multiplication: g.x = gx
- Orbits: the whole group (transitive). Stabilizers: trivial {e}
- Orbit-stabilizer gives: |G| = |G| * 1 (trivial but connects concepts)
- Cayley's theorem: every group is isomorphic to a subgroup of a symmetric group
- This is the PAYOFF -- connects group actions to the fundamental question "what are all the groups?"

### Scene 8: Summary (10:40-11:30)
**Content budget: 5 items max**
- Recap: group action definition, orbits, stabilizers, orbit-stabilizer theorem
- Key formula: |G| = |Orb(x)| * |Stab(x)|
- Tease: "Next time -- the Sylow theorems, which use group actions to count subgroups of prime power order"
- End card

## Visual Design Notes
- Use polygon (pentagon) as the central visual metaphor throughout
- Color-code: PRIMARY for orbits, SECONDARY for stabilizers, ACCENT for the orbit-stabilizer formula
- Show group elements as arrows/transforms on the polygon
- Orbit-stabilizer theorem gets a formula box with surrounding glow

## Narration Notes
- ~180 words per minute target
- Total narration ~1200-1400 words
- Connect frequently to previous videos (Video 116: homomorphisms, Video 113: permutations)
