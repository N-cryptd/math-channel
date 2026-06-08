# Video 54: Divergence Theorem
## Calculus III — Multivariable Playlist -- Video 14 of 14 (FINAL)

### Topic
Divergence Theorem (Gauss's Theorem): Relates the flux of a vector field through a closed surface to the triple integral of the divergence over the enclosed volume. The capstone theorem of multivariable calculus — connecting surface integrals and volume integrals. Statement, physical intuition (flux = source minus sink), proof idea, worked example, applications (Gauss's law, fluid dynamics), and the grand unification of the Fundamental Theorem of Calculus.

### Prerequisites
- Video 53: Stokes' Theorem
- Video 52: Green's Theorem
- Video 49: Double Integrals
- Video 50: Triple Integrals
- Video 47: Gradient and Directional Derivatives (divergence concept)

### Duration Target
12-15 minutes

### Competitive Analysis Notes
- 3Blue1Brown covers divergence extensively in "Divergence and Curl" and flux in
  "Green's Theorem and 2D Divergence" but does not have a dedicated Divergence Theorem
  video — this is a major gap we fill.
- Khan Academy: Has a solid but dry Divergence Theorem lecture focusing on computation.
  We take a more visual/intuitive approach with physical analogies.
- Dr. Trefor Bazett: Covers Divergence Theorem with good geometric intuition on
  source/sink interpretation — we adopt this metaphor and enhance with animated visuals.
- MathTheBeautiful: Has a rigorous treatment — we balance rigor with intuition.
- Key insight from analysis: Students struggle to see WHY the theorem works (the
  divergence measures net flux density). We lead with the source/sink analogy.

### Scene Plan

**Scene 1: Hook — The Final Theorem (0:00–1:30)**
- Narration: "We've journeyed from tangent lines to surface integrals. Green's Theorem
  connected curves to areas. Stokes' Theorem connected curves to surfaces. Now, one
  final theorem connects surfaces to volumes — the Divergence Theorem. It's the
  grand finale of vector calculus."
- Visuals: Progression diagram: FTC → Green's → Stokes' → Divergence
- Content budget: title + progression diagram + motivation text

**Scene 2: Physical Intuition — Sources and Sinks (1:30–3:30)**
- Narration: Imagine a vector field representing fluid flow. The divergence at a
  point measures whether fluid is being created (source) or destroyed (sink) there.
- A positive divergence point acts as a source — fluid flows outward.
- A negative divergence point acts as a sink — fluid flows inward.
- The total flux through a closed surface = total "stuff" created inside minus
  the total "stuff" destroyed inside.
- Content budget: 4 bullet points with source/sink labels

**Scene 3: The Statement (3:30–5:30)**
- Formal statement: ∮∮_S F·n dS = ∭_V (div F) dV
- Define: S = closed surface, V = volume enclosed by S
- F = vector field, div F = ∇·F, n = outward unit normal
- Key: n always points OUTWARD for Divergence Theorem
- Content budget: formula + 4 definition labels + outward normal note

**Scene 4: Green's Theorem as 2D Special Case (5:30–7:00)**
- In 2D: Green's Theorem relates circulation around a closed curve to a double integral
- The 2D divergence theorem (flux form of Green's): ∮_C F·n ds = ∬_D (div F) dA
- When the volume shrinks to a flat region and the surface becomes its boundary curve,
  the Divergence Theorem reduces to the flux form of Green's Theorem
- Content budget: 2D formula + connection explanation + label

**Scene 5: The Big Picture — FTC Unification (7:00–9:00)**
- The Divergence Theorem is the 3D version of the Fundamental Theorem of Calculus
- FTC: integral of derivative = function values at boundary
- Green's: integral of curl over region = line integral on boundary
- Stokes': integral of curl over surface = line integral on boundary
- Divergence: integral of divergence over volume = flux through boundary
- ALL say: "integral of derivative over interior = something on the boundary"
- Content budget: 4 theorem comparisons in structured layout

**Scene 6: Proof Idea (9:00–10:30)**
- Decompose volume V into tiny boxes
- For each box: flux through its faces ≈ (div F) × (volume of box)
- Adjacent boxes share faces — internal face fluxes cancel
- Only flux through outer surface survives → the surface integral
- Sum → triple integral of divergence = surface integral of flux
- Content budget: 4 explanation steps revealed progressively

**Scene 7: Worked Example (10:30–13:00)**
- F(x,y,z) = (x, y, z) through the unit sphere x² + y² + z² = 1
- Method 1: Direct surface integral
  - Normal to sphere: n = (x, y, z), so F·n = x² + y² + z² = 1
  - Flux = ∮∮ 1 dS = surface area = 4π
- Method 2: Divergence Theorem
  - div F = ∂x/∂x + ∂y/∂y + ∂z/∂z = 3
  - Flux = ∭ 3 dV = 3 × (4π/3) = 4π
- Both give 4π ✓
- Content budget: formula steps revealed progressively, 2 methods shown

**Scene 8: Applications and Summary (13:00–15:00)**
- Gauss's Law in electromagnetism: electric flux = charge enclosed / ε₀
- Fluid dynamics: conservation of mass (incompressible fluid → div v = 0)
- Summary: The four great theorems of vector calculus form a unified framework
- Final message: Calculus III complete — from tangent lines to the Divergence Theorem
- Outro
- Content budget: 3 application bullets + summary + outro
