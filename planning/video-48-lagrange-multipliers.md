# Video 48: Lagrange Multipliers

**Playlist:** Calculus III — Multivariable
**Video #8 of 14 in playlist**
**Estimated Duration:** 12 minutes
**Class:** `Video48_LagrangeMultipliers`

## Learning Objectives
1. Understand the constrained optimization problem: maximize/minimize f(x,y) subject to g(x,y) = c
2. Derive the geometric intuition: at an optimum on the constraint curve, the gradient of f is parallel to the gradient of g
3. State the Lagrange multiplier method: solve nabla f = lambda nabla g together with g(x,y) = c
4. Define the Lagrangian function L(x,y,lambda) = f(x,y) - lambda(g(x,y) - c)
5. Worked examples: find extrema of f subject to a constraint (maximize and minimize)
6. Identify multiple candidate solutions and evaluate which are maxima vs minima

## Scene Plan

### Scene 1: Hook — The Fence Problem (45s)
**Content budget:**
- Channel intro animation
- Motivation: "You have 100m of fencing. How do you build a rectangular pen with maximum area?"
- Bridge from gradient video: "Last time we found the gradient points uphill. Now what if we can only walk along a trail?"
- The fence problem is the simplest constrained optimization — you can't change both x and y independently

**Competitive insight:** Open with concrete real-world problem (gap in market vs purely geometric or formulaic starts). Most competitors skip motivation entirely.

**Narration:** "Imagine you have 100 meters of fencing material and you need to build a rectangular pen. You want to maximize the area. But here's the catch: you can't just make the rectangle as big as you want. The perimeter must equal exactly 100 meters. This is a constrained optimization problem, and it's everywhere in engineering, economics, and physics."

### Scene 2: The Geometry of Constraints (120s)
**Content budget:**
- Section divider: "The Geometry of Constraints"
- 2D contour plot of f(x,y) with constraint curve g(x,y) = c
- Key insight: maximum occurs where contour of f is tangent to constraint curve
- Normals are parallel: nabla f is parallel to nabla g
- Show multiple contours of f as ellipses/hyperbolas intersecting the constraint line
- At the optimal point, the contour just touches (is tangent to) the constraint
- Since normals at a tangent point are parallel: nabla f || nabla g

**Competitive insight:** Following 3B1B's geometric-first approach — show the picture before any algebra. Progressive contour revelation: don't show all level curves at once, reveal them one by one as we "walk along" the constraint curve.

**Narration:** "Let's visualize this. Imagine contour lines of our function f on a 2D plane. Each contour represents a constant value of f. The constraint g(x,y) = c is a curve on this same plane. As we move along the constraint curve, f changes. The maximum occurs where a contour of f is tangent to the constraint. And at a point of tangency, the normals must be parallel — meaning the gradient of f is parallel to the gradient of g."

### Scene 3: The Lagrange Condition (90s)
**Content budget:**
- Section divider: "The Lagrange Condition"
- nabla f = lambda nabla g for some scalar lambda
- Three equations: df/dx = lambda dg/dx, df/dy = lambda dg/dy, g(x,y) = c
- lambda is called the Lagrange multiplier
- This gives us three equations and three unknowns (x, y, lambda)
- Solving this system gives candidate points

**Competitive insight:** Following Trefor Bazett's "motivate then formalize" arc. Derive from the geometric picture, then formalize. Most channels just state the condition without connecting back to the tangent/normal argument.

**Narration:** "Since the gradients are parallel at the optimum, we can write nabla f equals lambda times nabla g, where lambda is a scalar called the Lagrange multiplier. This gives us three equations in three unknowns: the partial derivatives of f with respect to x and y, the partial derivatives of g with respect to x and y, and the constraint itself."

### Scene 4: The Lagrangian Function (60s)
**Content budget:**
- Section divider: "The Lagrangian Function"
- L(x,y,lambda) = f(x,y) - lambda(g(x,y) - c)
- Taking partial derivatives of L with respect to x, y, and lambda recovers the Lagrange equations
- Setting dL/dx = 0 gives df/dx = lambda dg/dx
- Setting dL/dy = 0 gives df/dy = lambda dg/dy
- Setting dL/dlambda = 0 gives g(x,y) = c
- This is an elegant way to package the system into a single function

**Narration:** "There's an elegant way to package this system into a single function. We define the Lagrangian L equals f minus lambda times (g minus c). When we take the partial derivatives of L with respect to x, y, and lambda, and set each equal to zero, we recover exactly the Lagrange equations."

### Scene 5: Worked Example — Maximize (120s)
**Content budget:**
- Section divider: "Worked Example — The Fence Problem"
- f(x,y) = xy (area), constraint g(x,y) = 2x + 2y = 100
- Compute nabla f = (y, x) and nabla g = (2, 2)
- Lagrange equations: y = 2 lambda, x = 2 lambda, 2x + 2y = 100
- From the first two: x = y (so the rectangle is a square!)
- Substitute: 2x + 2x = 100, so x = 25
- Maximum area = 25 * 25 = 625
- Visual: show the rectangle becoming a square at the optimum

**Competitive insight:** Unlike OCT (pure algebra) or 3B1B (pure geometry), we do BOTH — show the algebra AND the geometric picture side by side. The "the answer is a square!" moment is the aha beat.

**Narration:** "Let's solve the fence problem. We want to maximize the area f equals x times y, subject to 2x plus 2y equals 100. The gradients are nabla f equals (y, x) and nabla g equals (2, 2). Setting nabla f equal to lambda nabla g gives y equals 2 lambda and x equals 2 lambda, which means x equals y. The optimal rectangle is a square! Plugging in: x equals 25, and the maximum area is 625."

### Scene 6: Multiple Candidates (90s)
**Content budget:**
- Section divider: "Multiple Candidates"
- New problem: minimize f(x,y) = x^2 + y^2 subject to x + y = 4
- This asks: what point on the line x + y = 4 is closest to the origin?
- Compute nabla f = (2x, 2y) and nabla g = (1, 1)
- Lagrange: 2x = lambda, 2y = lambda, so x = y
- Substitute into constraint: 2x = 4, x = y = 2
- Minimum value: 4 (distance squared = 4, distance = 2)
- Visual: line x + y = 4 with circle of radius 2 centered at origin, tangent at (2,2)

**Competitive insight:** Many competitors skip the fact that Lagrange multipliers can yield multiple candidate points (min, max, saddle) and you need to evaluate all of them. We explicitly show this is the minimum by evaluating f at the candidate.

**Narration:** "Now let's find the minimum. Minimize x squared plus y squared, subject to x plus y equals 4. Geometrically, we're finding the closest point on this line to the origin. The gradients are nabla f equals (2x, 2y) and nabla g equals (1, 1). Setting them parallel gives 2x equals lambda and 2y equals lambda, so x equals y. Substituting: x equals y equals 2. The minimum value of f is 4, which means the minimum distance is 2."

### Scene 7: Summary + Outro (75s)
**Content budget:**
- Section divider: "Key Takeaways"
- Summary of the method: set up nabla f = lambda nabla g with g(x,y) = c
- The Lagrangian function packages everything
- Key formulas recap
- Two examples solved: maximize area (square!) and minimize distance
- Lambda has meaning: rate of change of the optimum with respect to the constraint
- Channel outro with next video card

**Narration:** "To summarize: Lagrange multipliers solve constrained optimization. At the optimum, the gradient of f is parallel to the gradient of g. We write this as nabla f equals lambda nabla g, and solve it together with the constraint. The Lagrangian packages all three equations into one elegant function. In our examples, we found the square maximizes area and the closest point minimizes distance."

## Visual Design
- **Contour lines:** Concentric curves (ellipses for xy, circles for x^2+y^2) in varying muted colors
- **Constraint curve:** Bright SECONDARY line across the contour map
- **Gradient vectors:** PRIMARY arrows for nabla f, RED arrows for nabla g
- **Tangent moment:** At the optimal point, highlight that the contour touches the constraint (animate tangent lines coinciding)
- **Formula boxes:** ACCENT-highlighted for nabla f = lambda nabla g and the Lagrangian
- **Progressive contour revelation:** Reveal contour lines one by one, building up to the tangent point
- **Rectangle visual:** Show the rectangular pen morphing toward the optimal square shape

## References
- Competitive analysis: t_9cff985e comment thread (2026-06-06)
- Previous video: Video 47 (Gradient and Directional Derivatives)
- Next video: Video 49 (Extreme Values on Closed/Bounded Regions)
