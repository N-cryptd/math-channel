# Video 204: Tangent Spaces and Vector Fields

**Playlist:** Differential Geometry (Video 11 of 13)
**Level:** Graduate (Differential Geometry)
**Class:** Video204_TangentSpacesVectorFields
**Script:** scripts/graduate/video-204-tangent-spaces-vector-fields.py

## Prerequisites
- Video 203: Manifolds Introduction (charts, atlases, smooth structure)
- Linear Algebra: Vector spaces, dual spaces, tangent spaces of R^n
- Calculus: Partial derivatives, directional derivatives, Jacobian matrices

## Learning Objectives
1. Define the tangent space T_p M at a point p on a manifold
2. Understand tangent vectors as derivations (directional derivatives on functions)
3. Construct the tangent space via coordinate charts (pushforward of coordinate vectors)
4. Define vector fields as smooth assignments of tangent vectors
5. Compute pushforwards and understand coordinate vector fields ∂/∂x^i
6. Introduce the tangent bundle TM and its role in differential geometry

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — Vectors Without an Ambient Space (~60s)
- "In R^3, a tangent vector to a surface is easy: it's a vector in R^3 that's tangent to the surface. But on an abstract manifold, there's no surrounding space. How do we define tangent vectors? This is one of the most subtle constructions in differential geometry."
- Content budget: 2 items + title

### Scene 2: Tangent Vectors as Curves (~90s)
- Approach 1: Equivalence classes of curves through p
- Two curves γ₁, γ₂ through p define the same tangent vector if d(φ∘γ₁)/dt|_0 = d(φ∘γ₂)/dt|_0 in some (any) chart
- This gives a coordinate-invariant notion
- Content budget: 3 items

### Scene 3: Tangent Vectors as Derivations (~90s)
- Approach 2: A tangent vector v at p is a linear map v: C^∞(M) → R satisfying the Leibniz rule: v(fg) = v(f)·g(p) + f(p)·v(g)
- Example: ∂f/∂x^i at p is a derivation
- These two approaches are equivalent (theorem)
- Content budget: 4 items

### Scene 4: The Tangent Space (~80s)
- The tangent space T_p M is the set of all tangent vectors at p
- It's an n-dimensional real vector space
- Given a chart (U, φ) with coordinates (x¹, ..., xⁿ), a basis for T_p M is {∂/∂x¹, ..., ∂/∂xⁿ}
- "This is the most important vector space in differential geometry"
- Content budget: 3 items

### Scene 5: Vector Fields (~90s)
- A vector field X assigns a tangent vector X_p ∈ T_p M to each point p
- In coordinates: X = X^i(x) ∂/∂x^i (Einstein summation)
- Smooth vector fields: the component functions X^i are C^∞
- Examples: gradient vector field, coordinate vector fields
- Content budget: 4 items

### Scene 6: Pushforward (~80s)
- Given a smooth map F: M → N, the pushforward F_* maps tangent vectors: F_*: T_p M → T_{F(p)} N
- In coordinates: (F_* v)(f) = v(f ∘ F)
- The Jacobian matrix of F is the matrix representation of F_*
- Content budget: 3 items

### Scene 7: The Tangent Bundle (~80s)
- The tangent bundle TM = ⋃_{p∈M} T_p M
- It's a 2n-dimensional manifold (if M is n-dimensional)
- Sections of the tangent bundle are precisely vector fields
- "The tangent bundle is where the geometry lives"
- Content budget: 3 items

### Scene 8: Summary and Outlook (~70s)
- Three equivalent pictures: curves, derivations, coordinate vectors
- Tangent space: n-dimensional vector space at each point
- Vector fields: smooth assignments, coordinate expressions
- Preview next: "Video 205 introduces differential forms — the dual objects to vector fields."
- Play outro
- Content budget: 3 items + outro

## Key Formulas
1. Leibniz rule: v(fg) = v(f)g(p) + f(p)v(g)
2. Coordinate basis: {∂/∂x¹, ..., ∂/∂xⁿ} for T_p M
3. Vector field: X = X^i(x) ∂/∂x^i
4. Pushforward: (F_* v)(f) = v(f ∘ F)
5. Tangent bundle: TM = ⋃_{p∈M} T_p M
