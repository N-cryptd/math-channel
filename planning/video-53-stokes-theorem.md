# Video 53: Stokes' Theorem
## Calculus III — Multivariable Playlist -- Video 13 of 14

### Topic
Stokes' Theorem: the generalization of Green's Theorem to 3D surfaces. Relates the line integral
of a vector field around a closed curve C to the surface integral of the curl of the field over
any surface S bounded by C. Statement, proof idea, orientation conventions, worked example,
and the deep connection to Green's Theorem and the Fundamental Theorem of Calculus.

### Prerequisites
- Video 52: Green's Theorem
- Video 51: Line Integrals
- Video 47: Gradient and Directional Derivatives (curl concept)
- Video 43: Cross Product (surface normal)

### Duration Target
12–15 minutes

### Competitive Analysis Notes
- 3Blue1Brown covers curl extensively in "Divergence and Curl" (Essence of Calc chapter)
  but does not have a dedicated Stokes' Theorem video — this is a gap we fill.
- Khan Academy: Has Stokes' Theorem content with surface orientation focus — we take a
  more visual/intuitive approach, building from Green's Theorem analogy.
- Dr. Trefor Bazett: Covers Stokes' with good visual of twisted surfaces showing same
  boundary — we adopt the "many surfaces, one boundary" visual metaphor.
- Key insight from analysis: Most students struggle with orientation (right-hand rule for
  surface normal). We emphasize this with animated visuals.

### Scene Plan

**Scene 1: Hook — From Flat to Curved (0:00–1:30)**
- Narration: "Green's Theorem connects a line integral around a flat region to a double integral inside.
  But what if the boundary isn't flat? What if it wraps around a hemisphere, or a cone?
  Stokes' Theorem gives us the answer — and it's breathtakingly beautiful."
- Visuals: Flat disk → morphs into hemisphere with boundary circle unchanged
- Content budget: title + 2 bullet points + animation

**Scene 2: The Statement (1:30–4:00)**
- Formal statement: ∮_C F·dr = ∫∫_S (curl F)·n dS
- Define: C = closed boundary curve, S = surface with boundary C
- F = vector field, curl F = ∇×F, n = unit normal to S
- Orientation: right-hand rule — fingers follow C, thumb points in direction of n
- Content budget: formula + 3 labels + orientation diagram

**Scene 3: Green's Theorem as Special Case (4:00–6:00)**
- Show: when S is flat in the xy-plane, curl F · n dS = (∂Q/∂x - ∂P/∂y) dA
- This is exactly Green's Theorem!
- Stokes' = Green's in 3D — Green's is the flat special case
- Content budget: formula comparison + 2 explanatory lines

**Scene 4: The "Many Surfaces, One Boundary" Idea (6:00–8:00)**
- Key insight: The line integral only depends on C, NOT on which S you pick
- Visual: Same circle boundary, three different surfaces (disk, hemisphere, cone)
- All give the same line integral — this is profound!
- Content budget: 3 surfaces with same boundary + label

**Scene 5: Proof Idea (8:00–10:00)**
- Tile the surface S into tiny patches
- On each patch: circulation ≈ (curl F · n) × (area of patch)
- Interior edges cancel (adjacent patches traverse shared edges in opposite directions)
- Only boundary edges survive → line integral
- Content budget: tiling diagram + 3 explanation steps

**Scene 6: Worked Example (10:00–12:30)**
- F(x,y,z) = (y², -x², z²)
- C = circle x² + y² = 1 at z = 0 (unit circle, counterclockwise)
- S = hemisphere x² + y² + z² = 1, z ≥ 0
- Compute curl F = (0, 0, -2x - 2y)
- Normal to hemisphere: (x, y, z)/1 → curl·n = (-2x - 2y)z
- At z = √(1 - x² - y²): integral = ∫∫ (-2x - 2y)√(1-x²-y²) dA
- Switch to polar: = ∫₀²π ∫₀¹ (-2r cos θ - 2r sin θ)√(1-r²) r dr dθ
- The cos θ and sin θ integrals vanish → result = 0
- Check: Direct line integral gives same result
- Content budget: formula steps revealed progressively

**Scene 7: Summary and Outlook (12:30–14:00)**
- Stokes' Theorem: line integral = surface integral of curl
- Generalizes Green's Theorem to 3D
- Only the boundary matters — not the specific surface
- Preview of Divergence Theorem (Video 54)
- Outro
