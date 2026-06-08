# Video 51: Line Integrals
## Calculus III — Multivariable Playlist — Video 11 of 14

### Topic
Line integrals: scalar line integrals (mass of a wire, arc length), vector line integrals
(work by a force field), the Fundamental Theorem for Line Integrals, path independence,
conservative vector fields, potential functions.

### Prerequisites
- Video 49: Double Integrals
- Video 45: Vector-Valued Functions (parametric curves)
- Gradient (Video 47)

### Duration Target
12–15 minutes

### Scene Plan

**Scene 1: Hook — Integrating Along a Curve (0:00–1:30)**
- Narration: "Instead of integrating over a flat region or a solid, what if we integrate
along a curve? Imagine measuring the total mass of a thin wire whose density varies."
- Visuals: curve C in 2D, density label, question

**Scene 2: Scalar Line Integral — Mass of a Wire (1:30–4:00)**
- Formula: ∫_C f(x,y) ds = ∫_a^b f(r(t)) |r'(t)| dt
- ds = |r'(t)| dt converts arc length element to parameter
- Example: mass of wire with density δ(x,y) = x+y on unit circle

**Scene 3: Vector Line Integral — Work (4:00–6:30)**
- Formula: ∫_C F · dr = ∫_a^b F(r(t)) · r'(t) dt
- Physical meaning: work = force · displacement (dot product)
- Sign convention: positive if force has component along motion

**Scene 4: Conservative Fields (6:30–9:00)**
- Definition: F = ∇f for some scalar potential f
- Key theorem: ∫_C ∇f · dr = f(B) - f(A) (only depends on endpoints!)
- Theorem name: Fundamental Theorem for Line Integrals

**Scene 5: Path Independence (9:00–11:00)**
- Equivalent conditions: path independence ⟺ conservative ⟺ curl F = 0 ⟺ exact
- Example: work is same along any path from A to B in a conservative field

**Scene 6: Worked Example (11:00–13:00)**
- F(x,y) = (2xy, x²+y²), find ∫_C F·dr from (0,0) to (1,1)
- Check: curl F = 0, find potential f = x²y + y³/3, compute f(1,1)-f(0,0) = 4/3

**Scene 7: Summary (13:00–15:00)**
- Scalar line integral: integrate a function along a curve
- Vector line integral: work done by a vector field
- Conservative fields: path-independent, curl = 0
- Fundamental Theorem: ∫ ∇f · dr = f(B) - f(A)
- Outro
