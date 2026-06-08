# Video 50: Triple Integrals
## Calculus III — Multivariable Playlist — Video 10 of 14

### Topic
Triple integrals: extending integration to three variables, iterated triple integrals,
changing order of integration in 3D, applications (volume, mass, center of mass,
moments of inertia).

### Prerequisites
- Video 49: Double Integrals
- Single-variable and double integration techniques
- Basic 3D geometry (Video 41-44)

### Duration Target
12–15 minutes

### Competitive Analysis Insights
Based on channel-analysis/improvements.md Video 49 analysis:
- We lead with geometry before formulas
- Progressive disclosure: one formula per scene
- Color-coded integration orders (PRIMARY for first order, SECONDARY for second)
- Worked examples before formal definitions
- Classic "impossible in one order, easy in another" as the aha moment

### Scene Plan

**Scene 1: Hook — From 2D to 3D (0:00–1:30)**
- Content budget: title (1) + 2D reminder (1) + 3D extension (1) + question (1) = 4 items
- Narration: "We've integrated over flat regions. Now we stack layers vertically.
What if the density of a solid object varies throughout its volume?"
- Visuals: 2D integral → 3D solid concept

**Scene 2: The Triple Integral Definition (1:30–3:00)**
- Content budget: title (1) + definition steps (1-3) = 4 items
- Partition a 3D region E into small boxes, sum f(x,y,z) ΔV, take the limit
- Key formula: ∫∫∫_E f(x,y,z) dV

**Scene 3: Iterated Triple Integrals — Fubini Extension (3:00–5:00)**
- Content budget: title (1) + formula (1) + bounds explanation (1) = 3 items
- ∫∫∫ f dV = ∫_a^b ∫_{g1(x)}^{g2(x)} ∫_{h1(x,y)}^{h2(x,y)} f dz dy dx
- Order: innermost (z) first, then y, then x

**Scene 4: Worked Example — Volume of a Tetrahedron (5:00–7:30)**
- Content budget: title (1) + setup (1) + steps (1-2) = 4 items
- Region: bounded by x=0, y=0, z=0, x+y+z=1
- Compute volume = ∫₀¹ ∫₀^{1-x} ∫₀^{1-x-y} 1 dz dy dx = 1/6

**Scene 5: Changing Order in 3D (7:30–10:00)**
- Content budget: title (1) + original (1) + swapped (1) = 3 items
- 6 possible orders (dzdydx, dydzdx, dxdydz, etc.)
- Quick example of swapping to simplify bounds

**Scene 6: Applications — Mass and Center of Mass (10:00–12:00)**
- Content budget: title (1) + mass formula (1) + center of mass formulas (1) = 3 items
- Mass = ∫∫∫ δ(x,y,z) dV
- x̄ = (1/M) ∫∫∫ x·δ dV (and similarly for ȳ, z̄)

**Scene 7: Moments of Inertia (12:00–13:00)**
- Content budget: title (1) + formula (1) = 2 items
- I_x = ∫∫∫ (y²+z²)·δ dV

**Scene 8: Summary (13:00–14:30)**
- Content budget: title (1) + 4 takeaways (1-4) = 5 items
- Triple integral extends double integral
- 6 possible orders of integration
- Applications: volume, mass, center of mass, moments of inertia
- Outro

### Key Formulas
1. ∫∫∫_E f dV = lim ∑ f(x*,y*,z*) ΔV
2. ∫∫∫ f dz dy dx with appropriate bounds
3. Mass = ∫∫∫ δ dV
4. x̄ = (1/M) ∫∫∫ x·δ dV
5. I_x = ∫∫∫ (y²+z²)·δ dV
