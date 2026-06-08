# Video 45: Vector-Valued Functions

## Metadata
- **Number:** 45
- **Playlist:** Calculus III — Multivariable
- **Position:** Video 5 of 14 in Calc III
- **Estimated Duration:** 12-15 minutes
- **Prerequisites:** Videos 41-44 (3D vectors, dot/cross product, lines/planes)
- **Class Name:** `Video45_VectorValuedFunctions`

## Overview
Introduce vector-valued functions as maps from real numbers to vectors, enabling us to describe curves in 2D and 3D space. Cover limits, derivatives, integrals, velocity/acceleration, and arc length.

## Scene Breakdown

### Scene 1: Hook + Intro (15s)
- Subcaption: "A vector-valued function maps a real number to a vector. As the parameter t changes, the tip of the vector traces out a curve in space."
- play_intro("Vector-Valued Functions", "Calculus III — Multivariable")
- Bridge text: "What if a function outputs not a number, but a vector?"
- Duration: ~15s

### Scene 2: Definition (20s)
- Section divider: "1 — What Is a Vector-Valued Function?"
- Title: "A Function That Outputs a Vector"
- Items:
  1. r(t) = <f(t), g(t), h(t)> — the general form (ACCENT, large)
  2. Each component f, g, h is a real-valued function of t
  3. 2D case: r(t) = <cos t, sin t> traces the unit circle
  4. 3D case: r(t) = <cos t, sin t, t> traces a helix
- Subcaption narration (~20s)

### Scene 3: Limits and Continuity (15s)
- Section divider: "2 — Limits and Continuity"
- Title: "Limits Component by Component"
- Items:
  1. lim r(t) = <lim f(t), lim g(t), lim h(t)>
  2. A vector-valued function is continuous if and only if each component is continuous
  3. Rules follow from scalar calculus (sum, product, etc.)
- Subcaption narration (~15s)

### Scene 4: Derivatives (20s)
- Section divider: "3 — Derivatives"
- Title: "Differentiate Each Component"
- Items:
  1. r'(t) = <f'(t), g'(t), h'(t)> (main formula, ACCENT)
  2. r'(t) is tangent to the curve at each point
  3. The derivative points in the direction of motion
  4. Sum, scalar product, dot product rules
- Subcaption narration (~20s)

### Scene 5: Velocity, Speed, Acceleration (25s)
- Section divider: "4 — Velocity and Acceleration"
- Title: "Physics Meets Calculus"
- Items:
  1. Position: r(t)
  2. Velocity: v(t) = r'(t) — tangent vector
  3. Speed: |v(t)| = |r'(t)| — scalar magnitude
  4. Acceleration: a(t) = v'(t) = r''(t)
- Example: r(t) = <t^2, t> → v(t) = <2t, 1> → a(t) = <2, 0>
- Subcaption narration (~25s)

### Scene 6: Integrals (15s)
- Section divider: "5 — Integrals of Vector Functions"
- Title: "Integrate Each Component"
- Items:
  1. ∫ r(t) dt = <∫ f(t) dt, ∫ g(t) dt, ∫ h(t) dt> + C
  2. Definite integrals follow similarly
  3. Use to recover position from velocity: r(t) = r(0) + ∫₀ᵗ v(s) ds
- Subcaption narration (~15s)

### Scene 7: Arc Length (20s)
- Section divider: "6 — Arc Length of a Space Curve"
- Title: "How Long Is the Curve?"
- Items:
  1. ds = |r'(t)| dt (infinitesimal arc length element)
  2. L = ∫ₐᵇ |r'(t)| dt (total arc length formula, ACCENT)
  3. Unit tangent vector: T(t) = r'(t) / |r'(t)|
- Worked example hint: helix arc length
- Subcaption narration (~20s)

### Scene 8: Summary + Outro (20s)
- Title: "Key Takeaways"
- 5 takeaways:
  1. r(t) maps t to a vector — traces curves in space
  2. Limits, derivatives, integrals all done component-by-component
  3. r'(t) is the velocity (tangent to the curve)
  4. Speed = |r'(t)|, acceleration = r''(t)
  5. Arc length = ∫ |r'(t)| dt
- play_outro("Partial Derivatives", "Calculus III — Multivariable")
- Duration: ~20s

## Visual Design Notes
- Use PRIMARY (blue) for velocity vectors
- Use SECONDARY (green) for acceleration vectors
- Use ACCENT (gold) for key formulas
- Show parametric curves using Manim's ParametricFunction where possible
- For the helix example, use ThreeDScene or 2D projection

## Competitive Analysis Notes
- 3B1B does not have a dedicated vector-valued functions video (his multivariable content focuses on partial derivatives and gradient)
- Khan Academy covers this with very dense formula dumps — we differentiate by progressive disclosure
- Professor Leonard has long-form lectures (45+ min) — we compress to 12-15 min with animations
- Our approach: Intuition-first (curves in space) → formulas → physics connections → arc length

## Estimated Total Duration
Sum of narration + animation: ~150s + intro/outro overhead ≈ 12-15 minutes
