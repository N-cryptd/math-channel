# Video 194: Curves in R^n — Differential Geometry Playlist

**Playlist:** Differential Geometry (Videos 194–206)
**Level:** Graduate (L5)
**Estimated Duration:** 12 minutes
**Prerequisites:** Calculus III (Videos 41–54), Linear Algebra (Videos 25–40)

## Topic Overview
This video introduces the Differential Geometry playlist by establishing the foundational object: parametrized curves in R^n. We define smooth curves, tangent vectors, velocity and speed, reparametrization, and regular curves. The key insight is that a curve is more than its image — the parametrization carries essential geometric information.

## Competitive Analysis Notes
- **Market gap:** No Manim-animated systematic differential geometry playlist exists on YouTube. 3B1B has not covered this topic. Mathologer has topology videos but no diff geom series. Faculty of Khan covers some topics but whiteboard-only.
- **Trefor Bazett** has some geometry content but not a complete playlist.
- **Key insight:** This is a green-field topic with no dominant animated competitor. We can define the space.
- **Approach:** Build from calculus III vectors → rigorous parameterization → set up for arc length and curvature (next video).

## Scene Plan

### Scene 1: Hook (45s)
- Channel intro
- Motivation: Why study curves? Roller coasters, planetary orbits, DNA, particle physics
- Title: "Curves in R^n"
- Content budget: intro animation + title + 3 bullet points max

### Scene 2: What is a Curve? (90s)
- Section divider: "1 — Parametrized Curves"
- Definition: A curve is a smooth map γ: [a,b] → R^n
- Show 2D example: γ(t) = (cos t, sin t) — animated circle trace
- Show 3D example: γ(t) = (cos t, sin t, t) — animated helix trace
- Emphasize: the map (parametrization) ≠ the image (set of points)
- Content budget: definition formula + 2 animated curves

### Scene 3: Tangent Vectors and Velocity (90s)
- Section divider: "2 — Tangent Vectors"
- Definition: γ'(t) = velocity vector at parameter t
- Speed: |γ'(t)| — magnitude of velocity
- Visual: tangent vector drawn at a point on the helix
- Key: tangent vector is always tangent to the curve at that point
- Content budget: formula + helix with tangent arrow

### Scene 4: Regular Curves (60s)
- Section divider: "3 — Regular Curves"
- Definition: γ is regular if γ'(t) ≠ 0 for all t
- Why it matters: regular curves have well-defined tangent lines everywhere
- Example: γ(t) = (t^3, t^2) has a cusp at t=0 — not regular there
- Content budget: definition + cusp example visual

### Scene 5: Reparametrization (90s)
- Section divider: "4 — Reparametrization"
- Given γ(t), define α(s) = γ(φ(s)) where φ is smooth and φ'(s) > 0
- Same geometric curve, different speed along it
- Visual: same helix traced at different speeds
- Arc-length parametrization preview: the "natural" parametrization
- Content budget: formula + comparison visual

### Scene 6: Examples Summary (60s)
- Two columns: "Regular curves" vs "Special cases"
- Left: line, circle, helix
- Right: cusp, self-intersections, reparametrizations
- Content budget: 2-column layout, 3 items each

### Scene 7: Outro (30s)
- What's next: arc length and curvature (Video 195)
- The Frenet-Serret frame (Video 196)
- Channel outro

## Key Formulas
- Curve: γ: [a,b] → R^n, γ(t) = (x₁(t), x₂(t), ..., xₙ(t))
- Velocity: γ'(t) = (x₁'(t), x₂'(t), ..., xₙ'(t))
- Speed: v(t) = |γ'(t)|
- Regular: γ'(t) ≠ 0 for all t
- Reparametrization: α(s) = γ(φ(s)), φ'(s) > 0
