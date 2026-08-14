# Video 199: Second Fundamental Form

**Playlist:** Differential Geometry (Video 6 of 13)
**Level:** Graduate (Differential Geometry)
**Class:** Video199_SecondFundamentalForm
**Script:** scripts/graduate/video-199-second-fundamental-form.py

## Prerequisites
- Video 197: Surfaces in R³ (parametrizations, tangent plane, normal vector)
- Video 198: First Fundamental Form (coefficients E, F, G, metric tensor)
- Video 196: Frenet-Serret Frame (curvature of curves)
- Linear Algebra: Self-adjoint operators, eigenvalues, quadratic forms

## Learning Objectives
1. Define the shape operator (Weingarten map) as the differential of the Gauss map
2. Define the second fundamental form coefficients e, f, g (or ℓ, m, n)
3. Compute principal curvatures as eigenvalues of the shape operator
4. Define mean curvature H and Gaussian curvature K in terms of the second fundamental form
5. Understand the geometric meaning: how the surface bends in space (extrinsic)

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — Intrinsic vs Extrinsic (~45s)
- "The first fundamental form tells you how to measure things on the surface — distances, angles, areas. But it says nothing about how the surface sits in space. Two surfaces can have the same first fundamental form but look completely different. The second fundamental form captures this missing information: how the surface curves, bends, and twists in three-dimensional space."

### Scene 2: Intro + Section Divider (~20s)
- play_intro("Second Fundamental Form", "Differential Geometry")
- Section divider: "1 — The Gauss Map"

### Scene 3: The Gauss Map and Shape Operator (~90s)
- The Gauss map N: S → S² sends each point to its unit normal
- The shape operator S_p: T_p S → T_p S is defined as S_p(v) = -D N_p(v)
  (the negative differential of the Gauss map)
- S is self-adjoint: I(S(v), w) = I(v, S(w)) for all tangent vectors
- "The Gauss map sends each point on the surface to its unit normal vector on the unit sphere. The shape operator is the negative derivative of this map. It is a linear map from the tangent plane to itself, and it is self-adjoint with respect to the first fundamental form."

### Scene 4: Second Fundamental Form Coefficients (~80s)
- The second fundamental form: II(v, w) = I(S(v), w) = ⟨N, d²σ⟩
- Coefficients: e = σ_uu · N, f = σ_uv · N, g = σ_vv · N
- Matrix: II = [[e, f], [f, g]]
- Alternative formula: II(v, w) = -⟨dN(v), w⟩ (since N is unit)
- "The second fundamental form is a quadratic form on the tangent plane defined by the shape operator. The three coefficients e, f, and g measure the normal components of the second partial derivatives."

### Scene 5: Principal Curvatures (~90s)
- The shape operator has real eigenvalues (self-adjoint + spectral theorem)
- The eigenvalues k₁, k₂ are the principal curvatures
- The eigenvectors are the principal directions
- Geometric meaning: the principal curvatures are the maximum and minimum normal curvatures
- Normal curvature in direction v: k_n(v) = II(v, v) / I(v, v)
- Euler's formula: k_n(theta) = k₁ cos²θ + k₂ sin²θ

### Scene 6: Mean and Gaussian Curvature (~80s)
- Mean curvature: H = (k₁ + k₂) / 2 = (eG - 2fF + gE) / (2(EG - F²))
- Gaussian curvature: K = k₁ · k₂ = (eg - f²) / (EG - F²)
- H = 0: minimal surface (soap films)
- K = 0: one principal curvature is zero (cylinder, cone)
- K > 0: both curvatures same sign (sphere, ellipsoid)
- K < 0: curvatures opposite sign (saddle, hyperboloid)

### Scene 7: Example — Sphere and Cylinder (~80s)
- Sphere: e = -R, f = 0, g = -R sin²φ... wait, for outward normal N = sigma/R:
  e = sigma_uu · N = -R sin²φ · (1/R) · R = ... actually e = -R sin²φ·cos(something)...
  Simplify: For sphere with outward N, k₁ = k₂ = 1/R, H = 1/R, K = 1/R²
- Cylinder: k₁ = 1/R (circular cross-section), k₂ = 0 (along axis)
  H = 1/(2R), K = 0

### Scene 8: Summary and Outro (~60s)
- Key results:
  1. Gauss map N: S → S², shape operator S = -DN
  2. II = [[e, f], [f, g]] where e = σ_uu · N, etc.
  3. Principal curvatures: eigenvalues of S
  4. Mean curvature H = (k₁+k₂)/2, Gaussian K = k₁·k₂
  5. Extrinsic: measures how surface sits in space
- Preview: Video 200 — Gaussian Curvature (Theorema Egregium!)
- play_outro

## Competitive Analysis Reference
Per channel-analysis/improvements.md: Green-field topic.
- Dr. Trefor Bazett: "Second Fundamental Form" whiteboard lecture
- Faculty of Khan: Shape operator derivation
- 3B1B: "Gauss's Remarkable Theorem" (intuitive, not formula-heavy)

Our approach: Progressive derivation of the second fundamental form, emphasizing the contrast with the intrinsic first form. Use the sphere/cylinder comparison to show how extrinsic geometry differs.
