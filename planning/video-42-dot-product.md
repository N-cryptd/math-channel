# Video 42: Dot Product in 3D

**Playlist:** Calculus III — Multivariable
**Video #2 of 14 in Calculus III**
**Status:** PLAN → SCRIPT → RENDER
**Created:** 2026-05-31

## Competitive Analysis Notes
- Attempted youtubei.js metadata fetch — limited output from cloud IP.
- Known competitor approaches to dot products:
  - 3B1B Chapter 9 (Dot products and duality): Emphasizes geometric intuition first (projection), connects to duality and linear transformations. Color-codes vectors, smooth projection animations.
  - Khan Academy: Systematic formula-first approach with concrete coordinate examples
  - Professor Leonard: Long-form lecture, covers formula + angle + projection applications
  - Professor Trefor Bazett: Clean geometric approach with projection emphasis

**Techniques to adopt:**
- Start with the geometric meaning (projection) BEFORE the formula — this is 3B1B's signature approach and it works
- Show projection visually: one vector "shadow" onto another
- Color-code the angle between vectors consistently (ACCENT for angle)
- Connect dot product to cosine formula — the "duality" insight
- Show both the algebraic and geometric perspectives

**Our unique angle:**
- Bridge from Video 41 (3D vectors) naturally
- Cover 4 key interpretations: algebraic formula, geometric (projection), angle formula, orthogonality test
- Practical examples: work done by a force, projection onto axis
- Tease cross product as the next video

## Scene Plan

### Scene 1: Hook + Channel Intro (15s)
- **Content budget:** intro animation only
- Bridge from Video 41: "Now that we have 3D vectors, how do we measure how much they point in the same direction?"
- play_intro("Dot Product in 3D", "Calculus III — Multivariable")

### Scene 2: The Algebraic Definition (60s)
- **Content budget:** title + 4 items
- Section divider: "The Dot Product Formula"
- Definition: a · b = a1*b1 + a2*b2 + a3*b3
- Key notation: center dot (not multiplication cross)
- Simple example: <1,2,3> · <4,5,6> = 4 + 10 + 18 = 32
- Result is a SCALAR (not a vector) — this is crucial

### Scene 3: What Does It Mean Geometrically? (70s)
- **Content budget:** title + 4 items
- Section divider: "Geometric Meaning"
- The dot product measures "how much two vectors agree in direction"
- Geometric formula: a · b = |a| |b| cos(θ)
- Connection: algebraic formula and geometric formula are the SAME thing (duality)
- When θ = 0: same direction → maximum positive dot product
- When θ = 90°: perpendicular → dot product is ZERO
- When θ = 180°: opposite direction → maximum negative dot product

### Scene 4: Projection Interpretation (70s)
- **Content budget:** title + 4 items
- Section divider: "Projection"
- The dot product gives the length of one vector's projection onto another
- Scalar projection: comp_a(b) = (a · b) / |a|
- Vector projection: proj_a(b) = (a · b / |a|²) * a
- Visual: show b casting a "shadow" onto a
- Practical example: how much of a force acts along a ramp

### Scene 5: Properties of the Dot Product (50s)
- **Content budget:** title + 4 items
- Section divider: "Key Properties"
- Commutative: a · b = b · a
- Distributive: a · (b + c) = a · b + a · c
- Scalar mult: (ka) · b = k(a · b)
- Self-dot: a · a = |a|²
- Orthogonality test: a · b = 0 ⟺ a ⊥ b

### Scene 6: Worked Example (60s)
- **Content budget:** title + 4 items
- Section divider: "Worked Example"
- Example: Force F = <3, 4, 0> on displacement d = <10, 0, 0>
- Work = F · d = 30 + 0 + 0 = 30 Joules
- Second example: F = <1, 1, 1>, d = <2, 0, 0> → Work = 2
- Physical meaning: only the component of force along displacement does work

### Scene 7: Summary + Outro (20s)
- **Content budget:** title + 5 items
- Key takeaways:
  1. Dot product: algebraic formula (sum of products)
  2. Geometric: a · b = |a| |b| cos(θ)
  3. Measures "agreement in direction"
  4. Projection formula for component along a vector
  5. Orthogonality: dot product = 0 means perpendicular
- play_outro("Cross Product", "Calculus III — Multivariable")

## Total Estimated Duration: ~10-12 minutes

## Key Formulas
- a · b = a₁b₁ + a₂b₂ + a₃b₃
- a · b = |a| |b| cos(θ)
- Scalar projection: comp_a(b) = (a · b) / |a|
- Vector projection: proj_a(b) = [(a · b) / (a · a)] a
- |a|² = a · a
- a ⊥ b ⟺ a · b = 0
- Work W = F · d
