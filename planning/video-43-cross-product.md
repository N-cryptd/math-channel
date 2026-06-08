# Video 43: Cross Product in 3D

## Overview
**Playlist:** Calculus III — Multivariable (Video 3 of 14)
**Topic:** The cross product of two 3D vectors
**Estimated duration:** 12 minutes

## Competitive Analysis
Skipped — youtubei.js search API unavailable from this environment. Proceeding with standard approach based on the successful pattern from Video 42 (Dot Product).

## Scene Breakdown

### Scene 1: Hook + Intro (15s)
- **Narration:** "The dot product measures how much two vectors agree. But what if we want a vector that's perpendicular to both? That's the cross product — and it's everywhere in physics."
- **Content budget:** Bridge text + play_intro
- **Elements:** bridge Text (1 item)

### Scene 2: Algebraic Definition — Determinant Form (30s)
- **Narration:** "The cross product takes two vectors and produces a new vector perpendicular to both. We compute it as the determinant of a 3x3 matrix with the unit vectors i, j, k in the first row, the components of a in the second row, and the components of b in the third row."
- **Content budget:** Section divider, title, determinant formula, note (5 items max)
- **Elements:** determinant formula (MathTex), note about resulting vector

### Scene 3: The Component Formula (25s)
- **Narration:** "Expanding the determinant gives us the component formula. The x-component is a2*b3 minus a3*b2. The y-component is a3*b1 minus a1*b3. And the z-component is a1*b2 minus a2*b1."
- **Content budget:** title, component formula, note (3 items)
- **Elements:** MathTex with full component expansion

### Scene 4: Geometric Meaning — Right-Hand Rule (35s)
- **Narration:** "The cross product vector points in a direction given by the right-hand rule. Point your index finger along a, curl your fingers toward b, and your thumb points in the direction of a cross b. The magnitude equals the area of the parallelogram spanned by the two vectors."
- **Content budget:** title, right-hand rule description, magnitude formula, area interpretation (4 items)
- **Elements:** MathTex for magnitude formula |a × b| = |a||b|sinθ, text for area interpretation

### Scene 5: Properties (35s)
- **Narration:** "The cross product is anti-commutative: a cross b equals negative b cross a. It distributes over addition. It's not associative. And the cross product of a vector with itself is the zero vector. Two parallel vectors have a zero cross product since sin of zero is zero."
- **Content budget:** title + 4 properties with labels (5 items using VGroup pairs)
- **Elements:** anti-commutative, distributive, self-cross = 0, parallel vectors → 0

### Scene 6: Worked Example — Torque (30s)
- **Narration:** "A classic application is torque in physics. If a force of two, three, zero acts at a position vector one, zero, zero from the pivot, the torque is the cross product of r and F. Computing: r cross F gives zero, zero, negative three. The magnitude of torque is three Newton-meters."
- **Content budget:** title, setup, formula, calculation, result (5 items)
- **Elements:** torque formula τ = r × F, example vectors, computation, answer

### Scene 7: Summary + Outro (20s)
- **Narration:** "To summarize: the cross product takes two vectors and returns a perpendicular vector. Its magnitude is the area of the parallelogram, and its direction follows the right-hand rule. Unlike the dot product, it's anti-commutative. In physics, it gives us torque and angular momentum. Next time, we'll use cross products to define lines and planes in 3D space."
- **Content budget:** title + 5 takeaways (progressive reveal), then play_outro
- **Elements:** 5 summary Text items

## Key Formulas
1. **Determinant form:** a × b = det([i j k; a1 a2 a3; b1 b2 b3])
2. **Component form:** ⟨a2b3-a3b2, a3b1-a1b3, a1b2-a2b1⟩
3. **Magnitude:** |a × b| = |a||b|sinθ
4. **Anti-commutative:** a × b = -(b × a)

## References
- Builds on: Video 41 (Vectors in 3D), Video 42 (Dot Product)
- Precedes: Video 44 (Lines and Planes in 3D)
