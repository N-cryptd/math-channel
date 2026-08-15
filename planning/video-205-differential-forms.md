# Video 205: Differential Forms

**Playlist:** Differential Geometry (Video 12 of 13)
**Level:** Graduate (Differential Geometry)
**Class:** Video205_DifferentialForms
**Script:** scripts/graduate/video-205-differential-forms.py

## Prerequisites
- Video 204: Tangent Spaces and Vector Fields (tangent space, derivations, pushforward)
- Linear Algebra: Dual spaces, alternating multilinear maps, determinant, wedge product
- Calculus: Line integrals, surface integrals, exterior derivative

## Learning Objectives
1. Define differential 1-forms as dual to vector fields (linear functionals on T_p M)
2. Understand differential k-forms as alternating k-linear maps on T_p M
3. Compute the exterior derivative d: Ω^k(M) → Ω^{k+1}(M)
4. Apply the wedge product ∧ to combine differential forms
5. Understand closed (dω = 0) and exact (ω = dη) forms
6. Connect differential forms to integration: Stokes' theorem preview

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — The Language of Integration (~60s)
- "Every integral you've ever computed — line integrals, surface integrals, flux integrals — is really the integral of a differential form. Differential forms are the natural language for integration on manifolds."
- Content budget: 2 items + title

### Scene 2: Differential 1-Forms (~90s)
- Definition: A 1-form ω at p is a linear map ω_p: T_p M → R
- The cotangent space T*_p M is the dual of T_p M
- In coordinates: ω = a_i(x) dx^i (Einstein summation)
- dx^i is the dual basis: dx^i(∂/∂x^j) = δ^i_j
- Content budget: 4 items

### Scene 3: Differential k-Forms (~90s)
- A k-form at p is an alternating k-linear map (T_p M)^k → R
- Ω^k(M) = smooth sections of ∧^k T*M
- 0-forms: smooth functions f
- 1-forms: df = (∂f/∂x^i) dx^i (exterior derivative of a function)
- 2-forms: dx^i ∧ dx^j (area elements)
- Content budget: 4 items

### Scene 4: Wedge Product (~80s)
- The wedge product ∧ combines forms: if ω ∈ Ω^k, η ∈ Ω^l, then ω ∧ η ∈ Ω^{k+l}
- Anticommutative: α ∧ β = -β ∧ α
- Example: dx ∧ dy is the area element in 2D
- Content budget: 3 items

### Scene 5: Exterior Derivative (~90s)
- d: Ω^k(M) → Ω^{k+1}(M) generalizes gradient, curl, divergence
- 0-forms → 1-forms: df = (∂f/∂x^i) dx^i (gradient)
- 1-forms → 2-forms: d(ω_i dx^i) = (∂ω_j/∂x^i - ∂ω_i/∂x^j) dx^i ∧ dx^j (curl)
- Key property: d∘d = 0 (Poincaré lemma: dd = 0)
- Content budget: 4 items

### Scene 6: Closed and Exact Forms (~80s)
- Closed: dω = 0
- Exact: ω = dη for some η
- Every exact form is closed (since dd = 0)
- The converse depends on topology (de Rham cohomology)
- Content budget: 3 items

### Scene 7: Integration of Forms (~80s)
- k-forms are the objects that can be integrated over k-dimensional submanifolds
- ∫_S ω where S is k-dimensional, ω is a k-form
- Change of variables works naturally with forms
- Preview: Stokes' theorem says ∫_∂Ω ω = ∫_Ω dω
- Content budget: 4 items

### Scene 8: Summary and Outlook (~70s)
- 1-forms: dual to vector fields
- k-forms: alternating multilinear maps
- Exterior derivative: d, with dd = 0
- Stokes: ∫_∂Ω ω = ∫_Ω dω
- Preview next: "Video 206 brings it all together with Stokes' theorem on manifolds."
- Play outro

## Key Formulas
1. 1-form: ω = a_i dx^i
2. k-form: ω = Σ a_{i₁...iₖ} dx^{i₁} ∧ ... ∧ dx^{iₖ}
3. Wedge: dx^i ∧ dx^j = -dx^j ∧ dx^i
4. Exterior derivative: d(ω_i dx^i) = (∂ω_j/∂x^i - ∂ω_i/∂x^j) dx^i ∧ dx^j
5. d² = 0
6. Stokes' theorem: ∫_∂Ω ω = ∫_Ω dω
