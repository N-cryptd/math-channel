# Video 49: Double Integrals
## Calculus III — Multivariable Playlist — Video 9 of 14

### Topic
Double integrals over rectangular and general regions: Riemann sum intuition in 2D,
iterated integrals, Fubini's theorem, changing order of integration, double integrals
over non-rectangular regions, and applications (volume, area, average value).

### Prerequisites
- Video 46: Partial Derivatives
- Video 47: Gradient and Directional Derivatives
- Video 48: Lagrange Multipliers
- Single-variable integration (Calculus I/II)

### Duration Target
12–15 minutes

### Competitive Analysis Insights
Based on the competitive landscape:
- **3B1B approach**: Builds 2D integration from 1D by extending the Riemann sum to rectangles in the plane. Uses color-coded volumes under surfaces.
- **Standard textbook approach**: Starts with rectangular regions, defines Riemann sums, then extends to general regions via Type I/II.
- **Our approach**: We'll lead with a geometric hook (volume under a surface), formalize via Riemann sums, then show the practical power of iterated integrals. We avoid the dry textbook progression by using a concrete example early.

### Scene Plan

**Scene 1: Hook — Volume Under a Surface (0:00–1:30)**
- Content budget: title (1) + 3D surface sketch (1) + volume highlight (1) + question (1) = 4 items
- Narration: "What's the volume under a surface? In single-variable calculus, we found the area under a curve. Now we extend that idea to three dimensions."
- Visuals: z = f(x,y) surface, shaded region beneath, question text
- Animation: Surface appears, region highlights, question fades in

**Scene 2: From 1D to 2D — The Riemann Sum Extension (1:30–3:30)**
- Content budget: title (1) + 1D integral reminder (1) + grid on xy-plane (1) + Riemann sum bars (1) + label (1) = 5 items
- Narration: "Recall: a single integral divides the x-axis into strips. For two variables, we divide the xy-plane into rectangles, erect columns, and sum their volumes."
- Key formula: limit of sum f(x_i*, y_j*) ΔA → ∫∫_R f(x,y) dA

**Scene 3: Iterated Integrals — Fubini's Theorem (3:30–5:30)**
- Content budget: title (1) + iterated integral formula (1) + rectangle label (1) + note text (1) = 4 items
- Narration: "Fubini's theorem tells us we can evaluate a double integral as two nested single integrals. The order of integration doesn't matter for continuous functions on rectangles."
- Key formulas: ∫∫_R f(x,y) dA = ∫_a^b ∫_c^d f(x,y) dy dx = ∫_c^d ∫_a^b f(x,y) dx dy

**Scene 4: Worked Example — Volume Under a Plane (5:30–8:00)**
- Content budget: title (1) + problem statement (1) + iterated integral setup (1) + step 1 result (1) + final answer (1) = 5 items
- Example: Find the volume under f(x,y) = 6 - 2x - 3y over [0,1] × [0,2]
- Step by step: set up outer/inner integral, evaluate inner, then outer
- Narration walks through computation with pauses for readability

**Scene 5: General Regions — Type I and Type II (8:00–10:00)**
- Content budget: title (1) + Type I formula (1) + Type II formula (1) + region labels (1) = 4 items
- Narration: "Not all regions are rectangles. Type I regions have fixed x-bounds with y varying between two curves. Type II flips the roles."
- Key formulas: Type I: ∫_a^b ∫_{g1(x)}^{g2(x)} f(x,y) dy dx; Type II: ∫_c^d ∫_{h1(y)}^{h2(y)} f(x,y) dx dy

**Scene 6: Changing Order of Integration (10:00–12:00)**
- Content budget: title (1) + original integral (1) + region sketch description (1) + swapped integral (1) = 4 items
- Example: Switch ∫_0^1 ∫_x^1 e^{y^2} dy dx → evaluate as ∫_0^1 ∫_0^y e^{y^2} dx dy
- Narration: "Sometimes one order is impossible to evaluate analytically. Switching the order makes it tractable."

**Scene 7: Applications — Area and Average Value (12:00–13:30)**
- Content budget: title (1) + area formula (1) + average value formula (1) = 3 items
- Area = ∫∫_R 1 dA; Average value = (1/Area(R)) ∫∫_R f(x,y) dA
- Quick numeric example for area of a region

**Scene 8: Summary and Recap (13:30–15:00)**
- Content budget: summary title (1) + 3 key takeaways (1-3) = 4 items
- Recap: double integral = volume/signed volume, iterated integrals via Fubini, order matters for non-rectangular regions, applications
- Outro with play_outro()

### Key Formulas to Render
1. ∫∫_R f(x,y) dA = lim_{m,n→∞} Σ_i Σ_j f(x_i*, y_j*) ΔA
2. ∫∫_R f(x,y) dA = ∫_a^b [∫_c^d f(x,y) dy] dx (iterated)
3. Type I: ∫_a^b ∫_{g₁(x)}^{g₂(x)} f(x,y) dy dx
4. Type II: ∫_c^d ∫_{h₁(y)}^{h₂(y)} f(x,y) dx dy
5. Area = ∫∫_R dA; Avg = (1/A) ∫∫_R f dA
