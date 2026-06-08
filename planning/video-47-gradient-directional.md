# Video 47: Gradient and Directional Derivatives

**Playlist:** Calculus III — Multivariable
**Video #7 of 14 in playlist**
**Estimated Duration:** 12 minutes
**Class:** `Video47_GradientDirectional`

## Learning Objectives
1. Define the gradient vector as the vector of all partial derivatives
2. Understand the directional derivative as the rate of change in any direction
3. Derive the connection: D_u f = grad(f) · u (dot product formula)
4. Geometric meaning: gradient points in direction of steepest ascent, magnitude = max rate of change
5. Gradient is perpendicular to level curves/contour lines
6. Worked example computing gradient and directional derivative

## Scene Plan

### Scene 1: Hook — The Mountain Problem (30s)
**Content budget:**
- Channel intro animation
- Motivation: "You're standing on a hill. Which direction should you walk to go uphill the fastest?"
- Teaser: the answer involves a special vector called the gradient

**Competitive insight:** Based on Trefor Bazett's mountain metaphor (9/10 visuals). This is more intuitive than starting with formulas.

**Narration:** "Imagine you're standing on a hillside. You want to climb as fast as possible. Which direction do you walk? In this video, we'll discover a vector that points the way — the gradient."

### Scene 2: Defining the Gradient (60s)
**Content budget:**
- Section divider: "The Gradient Vector"
- Definition: grad(f) = [df/dx, df/dy] — vector of partial derivatives
- Notation: nabla f, grad f, vector form
- Example: for f(x,y) = x²y + y³, compute the gradient
- Color: PRIMARY for the gradient vector

**Narration:** "The gradient of a scalar function f is a vector whose components are the partial derivatives. It collects all the directional rate-of-change information into a single vector."

### Scene 3: Directional Derivative — Definition (90s)
**Content budget:**
- Section divider: "Directional Derivatives"
- Motivation: partial derivatives give slope in x and y only — what about any direction?
- Formal definition: D_u f = lim [f(x+hu1, y+hu2) - f(x,y)] / h
- Unit vector u = (u1, u2) specifies the direction
- Important: u MUST be a unit vector
- Color: SECONDARY for directional derivative concepts

**Narration:** "A directional derivative extends partial derivatives to any direction. We move along a unit vector u and measure the rate of change. The key requirement: u must be a unit vector."

### Scene 4: The Gradient Shortcut (90s)
**Content budget:**
- Section divider: "The Gradient Formula"
- Key theorem: D_u f = grad(f) · u
- Derivation sketch: from limit definition, recognize the dot product pattern
- This is the "shortcut" — compute gradient once, then dot with any direction
- Formula box highlighted in ACCENT
- The geometric implication: since D_u f = |grad f| |u| cos(theta), maximum when theta=0

**Competitive insight:** Following Trefor's approach of deriving the formula from the limit, then showing the elegant shortcut. Unlike Organic Chemistry Tutor who just gives the formula.

**Narration:** "Here's the beautiful shortcut. The directional derivative in the direction u equals the dot product of the gradient with u. This means once you compute the gradient, you can find the rate of change in any direction with a single dot product."

### Scene 5: Geometric Meaning (120s)
**Content budget:**
- Section divider: "What Does the Gradient Mean?"
- From D_u f = |grad f| cos(theta):
  - Maximum rate of change = |grad f| (when theta = 0)
  - Direction of steepest ascent = direction of grad f
  - Zero rate of change = perpendicular to grad f
- Gradient is perpendicular to level curves (contour lines)
- Visual: show contour map with gradient arrows perpendicular to contour lines
- 3D surface visualization with gradient arrow pointing uphill

**Competitive insight:** Following Trefor's excellent geometric interpretation with contour maps (9/10 visuals). We'll create our own contour visualization rather than using a topographic photo.

**Narration:** "The gradient has three beautiful geometric properties. First, its magnitude equals the maximum rate of change. Second, it points in the direction of steepest ascent. Third, it's perpendicular to the level curves — the lines of constant height."

### Scene 6: Worked Example (90s)
**Content budget:**
- Section divider: "Worked Example"
- Function: f(x,y) = x² + y²
- Compute gradient: grad f = (2x, 2y)
- Evaluate at point (1,2): grad f = (2, 4)
- Compute directional derivative in direction u = (1/sqrt(2), 1/sqrt(2)):
  D_u f = (2)(1/sqrt(2)) + (4)(1/sqrt(2)) = 6/sqrt(2) = 3*sqrt(2)
- Color-code: PRIMARY for gradient, SECONDARY for computation, ACCENT for final answer

**Narration:** "Let's work through an example. For f(x,y) = x squared plus y squared, the gradient is (2x, 2y). At the point (1,2), the gradient is (2,4). To find the directional derivative at 45 degrees..."

### Scene 7: Summary + Outro (60s)
**Content budget:**
- Summary of key formulas: gradient definition, D_u f = grad·u
- Three geometric properties of the gradient
- Key takeaways (bullet points)
- Channel outro with next video card (Lagrange Multipliers)

**Narration:** "To summarize: the gradient packages all partial derivatives into a vector. The directional derivative in any direction equals the gradient dot product with that direction. The gradient points in the direction of steepest ascent and is perpendicular to level curves."

## Visual Design
- **Gradient vector:** Drawn as PRIMARY arrow on surface/contour map
- **Directional vectors:** SECONDARY arrows showing different directions
- **Contour map:** 2D contour lines with gradient arrows perpendicular
- **3D surface:** Optional paraboloid with gradient arrow pointing uphill
- **Formula boxes:** ACCENT-highlighted for key results (grad f definition, D_u f = grad·u)
- **Unit vector warning:** RED highlight when u is not normalized

## References
- Competitive analysis: channel-analysis/improvements.md (2026-06-05 entry)
- Previous video: Video 46 (Partial Derivatives)
- Next video: Video 48 (Lagrange Multipliers)
