# Video 197: Surfaces in R³

**Playlist:** Differential Geometry (Video 4 of 13)
**Level:** Graduate (Differential Geometry)
**Class:** Video197_SurfacesR3
**Script:** scripts/graduate/video-197-surfaces-r3.py

## Prerequisites
- Video 194: Curves in R^n (parametrized curves, tangent vectors)
- Video 195: Arc Length & Curvature (arc-length parametrization, curvature)
- Video 196: Frenet-Serret Frame (TNB frame, curvature, torsion)
- Calculus III: Parametric surfaces, partial derivatives, cross products
- Linear Algebra: Bases, linear transformations

## Learning Objectives
1. Define a (regular) surface as a subset of R³ with smooth local parametrizations
2. Understand the role of coordinate charts and the concept of an atlas
3. Define regularity: the differential must be injective (Jacobian has rank 2)
4. Give examples: sphere, cylinder, torus, saddle surface (hyperbolic paraboloid)
5. Understand the tangent plane at a point as the span of the partial derivatives
6. Introduce the normal vector field via the cross product of partials
7. Understand coordinate transformations and why surfaces require multiple charts

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — From Curves to Surfaces (~45s)
**Visual:** A curve in 3D morphs into a surface by sweeping.
- "For three videos, we studied curves — one-dimensional objects in space. Now we make the jump to two dimensions. A surface is the natural next step: instead of a line sweeping through space, a surface is a sheet, a skin, a membrane. The sphere, the torus, the saddle — these are the objects differential geometry was built to study."
- Following 3B1B's pedagogical approach: always show the geometric object before defining it.
**Content:** Motivational transition from curves to surfaces.
**Elements:** "Curves: 1D" label → "Surfaces: 2D" label, surface images (sphere, torus), "How do we describe them mathematically?" question
**Content budget:** 3 elements max

### Scene 2: Intro + Section Divider (~20s)
**Visual:** Channel intro, then section divider.
- play_intro("Surfaces in R³", "Differential Geometry")
- Section divider: "1 — What is a Surface?"
**Elements:** Intro animation, section divider
**Content budget:** Animated sequence

### Scene 3: Intuitive Definition — Parametric Surfaces (~90s)
**Visual:** Build up from 1D curves to 2D surfaces via parametrizations.
- A curve: gamma(t) maps R to R³, one parameter, one output.
- A surface: sigma(u,v) maps R² to R³, two parameters, one output.
- The domain is a 2D region (rectangle, disk), the codomain is 3D space.
- Examples of the form sigma(u,v) = (x(u,v), y(u,v), z(u,v)):
  - Cylinder: sigma(u,v) = (cos u, sin u, v), u in [0, 2pi], v in R
  - Sphere: sigma(theta, phi) = (sin phi cos theta, sin phi sin theta, cos phi)
  - Hyperbolic paraboloid: sigma(u,v) = (u, v, u² - v²)
- "A surface parametrization is a smooth map from an open subset of R² into R³. Two real parameters control the output, and the image is a two-dimensional sheet in three-dimensional space. The cylinder is parameterized by an angle and a height. The sphere uses spherical coordinates. The saddle surface, or hyperbolic paraboloid, uses Cartesian coordinates with a quadratic z-component."
**Elements:** gamma(t) vs sigma(u,v) formulas, domain diagram, 2-3 example formulas
**Content budget:** Progressive reveal, max 5

### Scene 4: Regularity Condition (~80s)
**Visual:** Show what goes wrong without regularity, then define the condition.
- Problem: a parametrization can fail to be a valid surface description.
- Example of failure: sigma(u,v) = (cos u cos v, cos u sin v, u) has a singularity when u = pi/2 (cos u = 0, Jacobian rank drops).
- The partial derivatives: sigma_u = d(sigma)/du, sigma_v = d(sigma)/dv
- Regularity condition: sigma_u and sigma_v must be linearly independent (cross product nonzero) at every point.
- Equivalently: the Jacobian matrix D sigma = [sigma_u | sigma_v] must have rank 2.
- Geometric meaning: the surface has a well-defined tangent plane at every point.
- "A parametrization is regular if the partial derivatives sigma u and sigma v are linearly independent everywhere. This means their cross product is never the zero vector. Geometrically, regularity guarantees a well-defined tangent plane at every point. Without it, the surface could pinch, fold, or form cusps."
**Elements:** Jacobian matrix, rank 2 condition, cross product nonzero, tangent plane sketch
**Content budget:** Progressive reveal, max 5

### Scene 5: Tangent Plane and Normal Vector (~90s)
**Visual:** Show tangent plane at a point on a surface.
- At a point p = sigma(u₀, v₀), the tangent plane is spanned by sigma_u and sigma_v.
- Tangent vectors: sigma_u = partial derivative with respect to u, sigma_v = partial derivative with respect to v
- Unit normal: n = (sigma_u x sigma_v) / |sigma_u x sigma_v|
- The tangent plane consists of all tangent vectors to curves on the surface passing through p.
- "The tangent plane at a point on the surface is the two-dimensional plane that best approximates the surface at that point. It is spanned by the two partial derivatives of the parametrization. The unit normal vector is the cross product of the partials, normalized. This normal vector is perpendicular to every tangent direction."
**Elements:** T_p S = span{sigma_u, sigma_v} formula, normal vector formula, tangent plane diagram
**Content budget:** Progressive reveal, max 5

### Scene 6: Section Divider + Charts and Atlases (~80s)
**Visual:** Section divider, then explain the chart/transition map concept.
- Section divider: "2 — Coordinate Charts"
- One parametrization may not cover the entire surface.
- Example: Spherical coordinates have a singularity at the poles (phi = 0 and phi = pi).
- Solution: Use multiple overlapping parametrizations (coordinate charts).
- An atlas is a collection of charts whose images cover the entire surface.
- Transition maps: if two charts overlap on the surface, the change of parameters between them must be smooth.
- "No single parametrization can cover the entire sphere. Spherical coordinates break down at the north and south poles, where the Jacobian loses rank. The solution is to use multiple coordinate charts, each covering a part of the surface. An atlas is a collection of such charts. Where charts overlap, the transition from one set of coordinates to another must be smooth."
**Elements:** Atlas definition, transition map condition, "multiple charts needed" diagram
**Content budget:** Progressive reveal, max 5

### Scene 7: Examples Gallery (~80s)
**Visual:** Showcase 4 surfaces with their parametrizations.
- Sphere: sigma(theta, phi) = (R sin phi cos theta, R sin phi sin theta, R cos phi), regularity: |sigma_theta x sigma_phi| = R² sin phi ≠ 0
- Cylinder: sigma(u, v) = (R cos u, R sin u, v), |sigma_u x sigma_v| = R ≠ 0
- Torus: sigma(u, v) = ((R + r cos v) cos u, (R + r cos v) sin u, r sin v), regularity: (R + r cos v) · r ≠ 0 when R > r
- Saddle: sigma(u, v) = (u, v, u² - v²), |sigma_u x sigma_v| = sqrt(1 + 4u² + 4v²) > 0 always
- "The sphere, cylinder, torus, and saddle surface are all regular surfaces. Each has a simple parametrization, and the regularity condition is easy to verify. The saddle surface is particularly nice: its partial derivatives are never parallel, so a single chart covers the entire surface."
**Elements:** 4 surface parametrizations with regularity check
**Content budget:** Progressive reveal, max 5

### Scene 8: Summary and Outro (~60s)
**Visual:** Recap key results, then outro.
- Key results:
  1. A surface is locally described by smooth maps sigma(u,v): U ⊂ R² → R³
  2. Regularity: partial derivatives are linearly independent (rank 2 condition)
  3. Tangent plane: T_p S = span{sigma_u, sigma_v}
  4. Unit normal: n = (sigma_u x sigma_v) / |sigma_u x sigma_v|
  5. An atlas of coordinate charts covers the entire surface
- Preview: Next video (198) — The First Fundamental Form (metric on surfaces)
**Content:** "Today we defined surfaces as the two-dimensional objects of differential geometry. A surface is described locally by smooth parametrizations from R² into R³. Regularity ensures the tangent plane is well-defined. And an atlas of coordinate charts lets us cover surfaces that no single parametrization can describe completely. Next time, we introduce the first fundamental form — the tool that lets us measure lengths and angles on surfaces."
**Elements:** 5 key results, next video preview, outro animation
**Content budget:** Progressive reveal, max 5

## Competitive Analysis Reference
Per channel-analysis/improvements.md: Green-field topic — no comprehensive animated DG playlist exists on YouTube. Individual videos exist:
- Dr. Trefor Bazett: Whiteboard explanations of surface parametrizations (undergrad level)
- 3B1B: "Differential Geometry" playlist (visual but short, not comprehensive)
- Faculty of Khan: Graduate-level surface theory (whiteboard, formula-heavy)

Our approach: First comprehensive animated DG series. Use Manim for surface visualizations. Following the transition from curves→surfaces pedagogy (intuition before formalism, examples before abstraction).
