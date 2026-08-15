# Video 206: Stokes' Theorem on Manifolds

**Playlist:** Differential Geometry (Video 13 of 13 — FINALE)
**Level:** Graduate (Differential Geometry)
**Class:** Video206_StokesOnManifolds
**Script:** scripts/graduate/video-206-stokes-on-manifolds.py

## Prerequisites
- Video 205: Differential Forms (exterior derivative, wedge product, d²=0)
- Video 202: Gauss-Bonnet Theorem (as a special case of Stokes)
- Multivariable Calculus: Green's theorem, Stokes' theorem, divergence theorem
- All previous DG videos (194–205)

## Learning Objectives
1. State the general Stokes' theorem: ∫_∂Ω ω = ∫_Ω dω
2. Understand the orientation of ∂Ω induced by the orientation of Ω
3. Show how the general theorem specializes to: fundamental theorem of calculus, Green's theorem, classical Stokes' theorem, divergence theorem, Gauss-Bonnet
4. Appreciate Stokes' theorem as the ultimate generalization of the FTC
5. Connect the entire Differential Geometry playlist together

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — One Theorem to Rule Them All (~70s)
- "The fundamental theorem of calculus, Green's theorem, the classical Stokes' theorem, the divergence theorem, and even the Gauss-Bonnet theorem — they're ALL special cases of one single, beautiful result: the general Stokes' theorem on manifolds."
- Content budget: 2 items + title

### Scene 2: Statement of the General Stokes' Theorem (~90s)
- Section divider: "The General Stokes' Theorem"
- Let Ω be an oriented k-dimensional manifold with boundary ∂Ω
- Let ω be a (k-1)-form on Ω
- Then: ∫_∂Ω ω = ∫_Ω dω
- "The integral of ω over the boundary equals the integral of dω over the interior"
- Content budget: 3 items

### Scene 3: Orientation of the Boundary (~80s)
- The boundary ∂Ω inherits an orientation from Ω
- "Outward normal first" convention
- For a 2D region: boundary traversed counterclockwise
- For a 3D region: boundary oriented with outward normal
- This orientation is crucial — flipping it changes the sign
- Content budget: 4 items

### Scene 4: Special Case — Fundamental Theorem of Calculus (~80s)
- k=1, Ω = [a,b], ∂Ω = {b} - {a}
- ω = f (0-form)
- dω = df = f'(x) dx
- Stokes: f(b) - f(a) = ∫_a^b f'(x) dx
- "The theorem you learned in Calc I is the 1D case of Stokes!"
- Content budget: 3 items

### Scene 5: Special Case — Green's Theorem and Classical Stokes' (~90s)
- Green's theorem: k=2, Ω ⊂ R², ω = P dx + Q dy
- ∫_∂Ω (P dx + Q dy) = ∫∫_Ω (∂Q/∂x - ∂P/∂y) dx∧dy
- Classical Stokes': k=2, Ω is a surface in R³
- ∫_∂Ω F·dr = ∫∫_Ω (∇×F)·dS
- Content budget: 4 items

### Scene 6: Special Case — Divergence Theorem (~80s)
- k=3, Ω ⊂ R³, ω is a 2-form
- ∫_∂Ω F·dS = ∫∫∫_Ω (∇·F) dV
- The divergence theorem is Stokes' in 3D with a 2-form
- Content budget: 3 items

### Scene 7: Connection to Gauss-Bonnet (~90s)
- Gauss-Bonnet is ALSO a special case of Stokes
- The Euler class form integrates to the Euler characteristic
- ∫∫_S K dA = 2πχ(S) arises from integrating a curvature form
- This connects back to Video 202 — the circle is complete
- Content budget: 4 items

### Scene 8: Summary and Playlist Recap (~90s)
- Stokes' theorem: one theorem, many faces
- The entire DG playlist journey: curves → surfaces → curvature → geodesics → manifolds → forms → Stokes
- "Differential geometry gives us the language to describe curved spaces, from the earth's surface to the fabric of spacetime."
- Play outro (final video — no next video card)
- Content budget: 5 items + outro

## Key Formulas
1. General Stokes: ∫_∂Ω ω = ∫_Ω dω
2. FTC: f(b) - f(a) = ∫_a^b f'(x) dx
3. Green's: ∫_∂Ω (P dx + Q dy) = ∫∫_Ω (∂Q/∂x - ∂P/∂y) dA
4. Classical Stokes: ∫_∂S F·dr = ∫∫_S (∇×F)·dS
5. Divergence: ∫_∂V F·dS = ∫∫∫_V (∇·F) dV
6. Gauss-Bonnet: ∫∫_S K dA = 2πχ(S)
