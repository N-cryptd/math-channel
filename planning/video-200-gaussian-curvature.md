# Video 200: Gaussian Curvature

**Playlist:** Differential Geometry (Video 7 of 13)
**Level:** Graduate (Differential Geometry)
**Class:** Video200_GaussianCurvature
**Script:** scripts/graduate/video-200-gaussian-curvature.py

## Prerequisites
- Video 198: First Fundamental Form (metric tensor, E, F, G)
- Video 199: Second Fundamental Form (shape operator, principal curvatures, e, f, g)
- Linear Algebra: Determinants, eigenvalues, self-adjoint operators
- Calculus III: Partial derivatives, chain rule

## Learning Objectives
1. Define Gaussian curvature K = k₁·k₂ = (eg - f²)/(EG - F²)
2. Compute Gaussian curvature for classical surfaces (sphere, cylinder, saddle, plane)
3. Understand the Theorema Egregium: K is an isometric invariant
4. Derive K entirely from the first fundamental form (Brioschi formula sketch)
5. State Gauss's Theorema Egregium and its profound implications
6. Introduce surfaces of constant curvature and their classification

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — The Most Surprising Theorem (~45s)
- "Gauss discovered something astonishing: the Gaussian curvature of a surface can be computed using only the first fundamental form. That means K depends only on measurements made on the surface itself — not on how the surface sits in space. A flat sheet of paper and a cylinder have the same Gaussian curvature: zero. You can bend paper into a cylinder without stretching it. But you cannot bend it into a sphere. This is the Theorema Egregium — the Remarkable Theorem."

### Scene 2: Intro + Section Divider (~20s)
- play_intro("Gaussian Curvature", "Differential Geometry")
- Section divider: "1 — Definition and Examples"

### Scene 3: Definition and Examples (~90s)
- K = k₁ · k₂ = (eg - f²) / (EG - F²)
- Plane: K = 0 (both principal curvatures zero)
- Sphere (radius R): K = 1/R² (positive everywhere)
- Cylinder (radius R): K = 0 (one principal curvature zero)
- Saddle: K < 0 (principal curvatures opposite signs)
- "Gaussian curvature classifies points on a surface. K greater than zero means the surface looks like a bowl. K less than zero means it looks like a saddle. K equals zero means it is flat in at least one direction."

### Scene 4: Gauss's Equation and the Theorema Egregium (~90s)
- The Theorema Egregium: Gaussian curvature is invariant under isometries
- An isometry preserves the first fundamental form (lengths, angles, areas)
- Therefore K, being expressible in terms of E, F, G and their derivatives alone, is preserved
- This means: if you can bend a surface without stretching, K stays the same
- "Gauss proved that the Gaussian curvature depends only on the first fundamental form and its derivatives. Two surfaces with the same first fundamental form have the same Gaussian curvature. Bending without stretching preserves K."

### Scene 5: Isometric Bending and Non-Bending (~80s)
- Cylinder ↔ plane: isometric (K = 0 for both). Paper can be rolled into a cylinder.
- Sphere ↔ anything flat: NOT isometric (K = 1/R² ≠ 0). Paper cannot be wrapped on a sphere without wrinkling/stretching.
- Cone ↔ plane (minus vertex): isometric (K = 0 away from vertex)
- Practical implication: you cannot make an accurate flat map of the Earth without distortion (because Earth has K > 0 and a flat map has K = 0)

### Scene 6: Computing K from the First Form (~80s)
- Show that K depends on E, F, G and their partial derivatives (up to second order)
- Sketch the Brioschi formula (state it, don't derive in full)
- The fact that eg - f²/EG - F² can be rewritten in terms of only E, F, G is the computational heart of the Theorema Egregium
- "The explicit formula for K in terms of the first fundamental form is long but remarkable. It involves only E, F, G and their first and second partial derivatives."

### Scene 7: Surfaces of Constant Curvature (~80s)
- K = constant everywhere: special class of surfaces
- K = 0: developable surfaces (planes, cylinders, cones, tangent surfaces of curves)
- K > 0 constant: spheres (only surface with constant positive curvature)
- K < 0 constant: pseudosphere (tractrix of revolution), hyperbolic plane models
- Connection to non-Euclidean geometry: surfaces of constant negative curvature realize hyperbolic geometry

### Scene 8: Summary and Outro (~70s)
- Key results:
  1. K = k₁·k₂ = (eg-f²)/(EG-F²) classifies local shape
  2. Theorema Egregium: K is an isometric invariant
  3. K depends only on the first fundamental form
  4. Isometric bending: cylinder ≈ plane (K=0), sphere ≠ plane (K≠0)
  5. Constant K surfaces connect to non-Euclidean geometry
- Preview: Video 201 — Geodesics
- play_outro

## Competitive Analysis Reference
Per channel-analysis/improvements.md: Green-field topic.
- 3B1B: "Gauss's Remarkable Theorem" (most popular DG video on YouTube)
- Dr. Trefor Bazett: Gaussian curvature whiteboard lecture
- Mathologer: "The Gauss-Bonnet theorem" (advanced audience)
- Faculty of Khan: Theorema Egregium proof sketch

Our approach: First animated Theorema Egregium in a complete DG playlist. Visual isometric bending demonstrations. Follow 3B1B's emphasis on the "you can't flatten a sphere" insight.
