# Video 41: Vectors in 3D Space

**Playlist:** Calculus III — Multivariable  
**Video #1 of 14 in Calculus III**  
**Status:** SCRIPT → RENDER  
**Created:** 2026-05-30

## Competitive Analysis Notes
- Attempted youtubei.js metadata fetch — limited output from cloud IP (titles/metadata not returned).
- Known competitor approaches to 3D vectors:
  - 3B1B: Strong geometric intuition, emphasizes unit vectors and basis, color-coded axes
  - Khan Academy: Systematic component breakdown, concrete coordinate examples
  - Professor Leonard: Long-form lecture with hand-drawn style, very thorough

**Techniques to adopt:**
- Color-coded 3D axes (x=red, y=green, z=blue — standard convention)
- Visual demonstration of components projecting onto axes
- Emphasize magnitude formula connects to Pythagorean theorem

**Our unique angle:**
- Start from 2D → 3D bridge (students already know 2D vectors from LA)
- Focus on spatial intuition with clear Manim 3D scenes
- Connect 3D vectors to upcoming topics (dot/cross products, surfaces)

## Scene Plan

### Scene 1: Hook + Channel Intro (15s)
- **Content budget:** intro animation only
- Bridge from LA to Calc III: "We've mastered vectors in R^n. Now let's visualize them in three dimensions."
- play_intro("Vectors in 3D Space", "Calculus III — Multivariable")

### Scene 2: From 2D to 3D (60s)
- **Content budget:** title + 4 items
- Section divider: "The Third Dimension"
- Show 2D plane (x-y axes), then add z-axis emerging from origin
- Color code: x=RED, y=SECONDARY, z=PRIMARY
- Key formula: position in 3D as ordered triple (x, y, z)

### Scene 3: 3D Vector Components (60s)
- **Content budget:** title + 4 items
- Section divider: "Vector Components in 3D"
- Show vector v = <3, 4, 5> with projections onto each axis
- Component form: v = v_x * i + v_y * j + v_z * k
- Unit vectors i, j, k along each axis

### Scene 4: Magnitude in 3D (60s)
- **Content budget:** title + 3 items
- Section divider: "Magnitude (Length)"
- Formula: |v| = sqrt(v_x^2 + v_y^2 + v_z^2)
- Connect to 3D Pythagorean theorem
- Example: |<3,4,5>| = sqrt(9+16+25) = sqrt(50) = 5*sqrt(2)

### Scene 5: Direction and Unit Vectors (60s)
- **Content budget:** title + 3 items
- Section divider: "Direction in Space"
- Unit vector: u = v / |v|
- Example: normalize <3,4,5>
- Direction cosines concept (brief)

### Scene 6: Vector Operations (60s)
- **Content budget:** title + 4 items
- Section divider: "Operations in 3D"
- Addition: component-wise (parallelogram law still works)
- Scalar multiplication
- These work exactly like 2D — the rules generalize

### Scene 7: Summary + Outro (20s)
- **Content budget:** title + 5 items
- Key takeaways: 3 ordered triples, magnitude formula, unit vectors, operations generalize
- play_outro("Dot Product", "Calculus III — Multivariable")

## Total Estimated Duration: ~8-10 minutes

## Key Formulas
- v = <v_1, v_2, v_3> = v_1 i + v_2 j + v_3 k
- |v| = sqrt(v_1^2 + v_2^2 + v_3^2)
- u = v / |v|  (unit vector)
- v + w = <v_1+w_1, v_2+w_2, v_3+w_3>
