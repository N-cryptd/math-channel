# Video 201: Geodesics

**Playlist:** Differential Geometry (Video 8 of 13)
**Level:** Graduate (Differential Geometry)
**Class:** Video201_Geodesics
**Script:** scripts/graduate/video-201-geodesics.py

## Prerequisites
- Video 198: First Fundamental Form (metric tensor, arc length)
- Video 199: Second Fundamental Form (shape operator, normal curvature)
- Video 200: Gaussian Curvature (intrinsic geometry)
- Calculus of Variations: Euler-Lagrange equation (helpful but not required)
- Linear Algebra: Christoffel symbols connection to metric derivatives

## Learning Objectives
1. Define geodesics as curves of zero geodesic curvature (parallel transport of tangent)
2. Understand geodesics as locally shortest paths (variational characterization)
3. State and interpret the geodesic equation: d²u^k/ds² + Γ^k_{ij} du^i/ds · du^j/ds = 0
4. Compute Christoffel symbols from the first fundamental form
5. Verify classic examples: great circles on sphere, straight lines on cylinder, meridians
6. Introduce the exponential map and geodesic completeness concept

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — What's the Shortest Path on a Sphere? (~50s)
- Open with the classic question: "If you fly from New York to Tokyo, why don't you fly in a straight line?"
- Show a sphere with two paths: a "straight line" (in the embedding space, actually non-geodesic) and a great circle (the actual shortest path, which appears to curve on a flat map)
- Key visual: Animated 3D sphere with two paths traced simultaneously
- "On a curved surface, the shortest path between two points is not what you'd expect. It's a geodesic — the generalization of a straight line to curved geometry. Today we'll discover what geodesics are, derive the equation that describes them, and compute them for real surfaces."

### Scene 2: Intro + Section Divider (~20s)
- play_intro("Geodesics", "Differential Geometry")
- Section divider: "1 — Geodesics as Straightest Curves"

### Scene 3: Definition — Zero Geodesic Curvature (~100s)
- Geodesic definition: a curve on a surface whose geodesic curvature is zero
- Geodesic curvature κ_g measures how much the curve bends within the surface (not perpendicular to it)
- κ_g = 0 means the tangent vector is parallel-transported along the curve
- Equivalently: the acceleration vector d²r/ds² is either zero (line) or purely normal to the surface (N)
- Geodesic equation preview: d²r/ds² is parallel to the surface normal N
- "A geodesic is the straightest possible curve on a surface. Its acceleration has no component tangent to the surface. The tangent vector simply glides along, staying as straight as it can."
- Visual: A curve on a surface with tangent vector T and normal vector N — show that dT/ds is parallel to N for a geodesic.

### Scene 4: Variational Characterization (~90s)
- Geodesics are also locally shortest paths (minimize arc length)
- Arc length functional: L[γ] = ∫ √(E u'² + 2F u'v' + G v'²) ds
- Euler-Lagrange equations give two equations in u and v
- These simplify (using energy functional E = ∫ g_ij du^i/ds · du^j/ds ds instead) to the geodesic equation
- "Geodesics minimize the distance between nearby points. We can find them by applying the calculus of variations to the arc length integral. The resulting equations are the geodesic equations."
- Show the energy functional simplification trick briefly (mention it, don't fully derive)

### Scene 5: The Geodesic Equation (~100s)
- Full geodesic equation in coordinate form:
  d²u^k/ds² + Γ^k_{ij} (du^i/ds)(du^j/ds) = 0
- Christoffel symbols Γ^k_{ij} defined from the metric tensor:
  Γ^k_{ij} = (1/2) g^{kl} (∂g_{li}/∂u^j + ∂g_{lj}/∂u^i - ∂g_{ij}/∂u^l)
- Connection to the metric: Christoffel symbols encode how the coordinate basis changes
- "The geodesic equation tells us that the second derivative of the coordinates plus a correction term from the Christoffel symbols equals zero. The Christoffel symbols are computed entirely from the first fundamental form — they are intrinsic."
- Key insight: The geodesic equation involves ONLY the first fundamental form (connection to Theorema Egregium from Video 200)

### Scene 6: Example — Sphere (Great Circles) (~90s)
- Parameterize sphere: x(u,v) = (R sin u cos v, R sin u sin v, R cos u)
- Compute E = R², F = 0, G = R² sin²u
- Key Christoffel symbols: Γ^1_{22} = -sin u cos u, Γ^2_{12} = Γ^2_{21} = cot u
- Geodesic equations for u(s), v(s)
- Show that great circles (where u = constant or v = as + b with appropriate constants) satisfy the equations
- "On a sphere, the geodesics are great circles — the largest possible circles you can draw. Meridians and the equator are geodesics. Every other geodesic is a rotated great circle."

### Scene 7: Example — Cylinder and Classification (~90s)
- Cylinder parameterization: x(u,v) = (R cos u, R sin u, v)
- E = R², F = 0, G = 1 → all Christoffel symbols are zero!
- Geodesic equations: u'' = 0, v'' = 0 → straight lines in (u,v) coordinates
- On the cylinder: geodesics are helices, straight lines (along axis), and circles (around circumference — but wait, are circles geodesics?)
- Meridians (v-lines): geodesics. Helices: geodesics. Circles (u-lines): NOT geodesics (they have nonzero geodesic curvature unless the cylinder is unrolled)
- Classification:
  - K > 0 (sphere): geodesics converge (great circles cross at antipodes)
  - K = 0 (plane/cylinder): geodesics are parallel (like Euclidean lines)
  - K < 0 (hyperbolic): geodesics diverge
- "On a cylinder, geodesics are helices. This is because the cylinder has zero Gaussian curvature — it is locally flat. When you unroll a cylinder into a plane, geodesics become ordinary straight lines."

### Scene 8: Summary, Exponential Map, and Outro (~80s)
- Key results:
  1. Geodesics: curves with zero geodesic curvature (parallel-transported tangent)
  2. Geodesics: locally shortest paths (variational characterization)
  3. Geodesic equation: d²u^k/ds² + Γ^k_{ij} u'^i u'^j = 0
  4. Christoffel symbols from metric: Γ^k_{ij} = (1/2) g^{kl}(...)
  5. Examples: great circles (sphere), helices/lines (cylinder)
- Exponential map preview: for each point p and tangent vector v, there is a unique geodesic γ(t) with γ(0)=p, γ'(0)=v
- This defines a map exp_p: T_pS → S — the exponential map
- Geodesic completeness: if exp_p is defined for all v and all t, the surface is geodesically complete
- Connection to Hopf-Rinow theorem: on a complete surface, any two points are joined by a (not necessarily unique) geodesic
- Preview: Video 202 — Parallel Transport
- play_outro

## Competitive Analysis Reference
Per channel-analysis/improvements.md (2026-08-14 entry):
- Eigenchris: Thorough but formula-first; we go geometry-first
- Dr. Trefor Bazett: Great "shortest path on Earth" hook — we adopt this
- Dialect: Beautiful animations, GR focus — we borrow the "free-fall = geodesic" idea but stay DG-focused
- Faculty of Khan: Rigorous derivation, no motivation — we reverse the order (intuition → equation)
- **Our unique contribution:** First Manim-animated geodesics video in a systematic DG playlist. 3D Manim surfaces with geodesic curves — no competitor has this.
