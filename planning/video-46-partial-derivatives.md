# Video 46: Partial Derivatives

**Playlist:** Calculus III — Multivariable
**Video #6 of 14 in playlist**
**Estimated Duration:** 15 minutes
**Class:** `Video46_PartialDerivatives`

## Learning Objectives
1. Understand what a partial derivative measures: rate of change in one direction while holding others constant
2. Geometric interpretation: slope of a curve obtained by slicing a surface
3. Compute partial derivatives using the limit definition and differentiation rules
4. Notation variants: ∂f/∂x, f_x, ∂²f/∂x², f_xy
5. Higher-order partial derivatives and Clairaut's theorem (equality of mixed partials)

## Scene Plan

### Scene 1: Hook (30s)
**Content budget:**
- Channel intro animation
- Bridge question about multi-input functions

**Narration:** "When a function depends on more than one variable, how do we differentiate it? A partial derivative measures the rate of change in just one direction, while holding everything else constant."

### Scene 2: Motivation — From 1D to 2D (90s)
**Content budget:**
- Title: "From One Variable to Two"
- Review: dy/dx for f(x)
- New: f(x,y) — two inputs, one output
- Key question: "What does 'derivative' mean here?"
- Answer preview: "Take derivative in one direction at a time"

**Narration connection:** Bridge from single-variable calculus. Students already know dy/dx. We extend to functions of two variables.

### Scene 3: Geometric Intuition — Slicing a Surface (120s)
**Content budget:**
- Section divider: "Geometric Intuition"
- 3D surface plot (f(x,y) = x² + y² paraboloid)
- Fix y = constant → slice through surface → get a 2D curve
- The partial derivative ∂f/∂x = slope of that curve
- Similarly for ∂f/∂y with x = constant
- Color coding: PRIMARY for x-slices, SECONDARY for y-slices

**Competitive insight:** Following 3B1B's approach — show the surface, slice it, and reveal the tangent slope. But compressed to fit our 15-min format.

### Scene 4: Formal Definition (90s)
**Content budget:**
- Section divider: "Formal Definition"
- Limit definition for ∂f/∂x
- Limit definition for ∂f/∂y
- Alternative notations: ∂f/∂x = f_x = ∂_x f

**Narration:** "The partial derivative with respect to x treats y as a constant and differentiates normally. Here's the limit definition — it looks just like the ordinary derivative, except the increment is only in x."

### Scene 5: Example 1 — Polynomial (120s)
**Content budget:**
- Section divider: "Examples"
- f(x,y) = 3x²y + 4xy³ + y
- ∂f/∂x computation (step by step)
- ∂f/∂y computation (step by step)
- Color-code: PRIMARY for ∂f/∂x steps, SECONDARY for ∂f/∂y steps

**Narration:** "Let's compute. For ∂f/∂x, treat every y as a constant. The derivative of 3x²y with respect to x is 6xy. For ∂f/∂y, now treat x as constant..."

### Scene 6: Example 2 — Exponential/Trig (90s)
**Content budget:**
- f(x,y) = e^(xy) sin(y)
- ∂f/∂x = ye^(xy) sin(y) (product rule)
- ∂f/∂y = xe^(xy) sin(y) + e^(xy) cos(y) (product rule)

**Narration:** "With exponentials and trig, the same principle applies. Treat the other variable as constant and use all your single-variable rules — chain rule, product rule, everything still works."

### Scene 7: Higher-Order Partial Derivatives (90s)
**Content budget:**
- Section divider: "Higher-Order Derivatives"
- f_xx = ∂²f/∂x² (second partial w.r.t. x)
- f_yy = ∂²f/∂y²
- f_xy = ∂²f/∂x∂y (mixed partial)
- f_yx = ∂²f/∂y∂x (other mixed partial)
- Clairaut's theorem: f_xy = f_yx (when continuous)

**Narration:** "Just like we can take second derivatives in single-variable calculus, we can take second partial derivatives. And a beautiful result: under mild conditions, the mixed partials are equal."

### Scene 8: Summary + Outro (60s)
**Content budget:**
- Summary formula box: key definitions
- Key takeaways (3 bullet points)
- Channel outro with next video card (Gradient and Directional Derivatives)

## Visual Design
- **3D surface:** Use `Surface` with color gradient for the paraboloid visualization
- **Slice planes:** Semi-transparent planes cutting through the surface (PRIMARY for y=const, SECONDARY for x=const)
- **Tangent lines:** Colored arrows showing the slope direction
- **Contour map:** Optional 2D contour plot as alternative geometric view
- **Formula boxes:** Highlighted with ACCENT color for key results

## References
- Competitive analysis: channel-analysis/improvements.md (2026-06-05 entry)
- Previous video: Video 45 (Vector-Valued Functions)
- Next video: Video 47 (Gradient and Directional Derivatives)
