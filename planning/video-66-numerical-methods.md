# Video 66: Numerical Methods (Euler, RK4)

**Playlist:** Differential Equations (Video 13 of 13)
**Estimated duration:** 12 min
**Script file:** `scripts/undergraduate/video-66-numerical-methods.py`
**Class name:** `Video66_NumericalMethods`
**Status:** PLANNING → SCRIPTING

## Competitive Analysis Insights

### 3Blue1Brown — ODE Series (Differential Equations chapter)
- **Approach:** Doesn't cover Euler/RK4 explicitly in the ODE playlist; focuses more on analytical methods. His "But what is a differential equation?" video touches on the idea of numerical stepping but doesn't go deep.
- **Visual technique:** Would likely use flowing curves with step-by-step construction
- **Gap opportunity:** This is a topic 3B1B hasn't deeply covered — our chance to own it

### Steve Brunton — Data-driven dynamics
- **Approach:** Covers Euler method and RK4 in applied dynamics context, connects to numerical simulation
- **Visual technique:** Shows stepping along curves, error accumulation visually
- **Pacing:** Moves quickly through the method, spends more time on applications
- **Key insight to adopt:** Show error visually — compare Euler approximation to true solution on the same plot

### Zach Star (legacy) — Engineering math
- **Approach:** Practical, code-oriented perspective on numerical methods
- **Pacing:** Fast, assumes strong calculus background
- **Weakness:** Less visual intuition, more formula-driven

### Our Approach (Synthesis)
- **Structure:** Why numerical? → Euler's method (geometric intuition) → Error analysis → Improved Euler (Heun's) → RK4 (the standard) → Summary
- **Visual metaphors:** (1) Euler stepping as walking along tangent lines, (2) Error as the growing gap between approximation and true curve, (3) RK4 as "looking ahead" with 4 evaluations per step
- **Color scheme:** PRIMARY (#5BC0EB) for true solutions, RED (#EF476F) for Euler approximation, ACCENT (#FFD166) for RK4, SECONDARY (#7BC950) for improved Euler

## Scene Breakdown

### Scene 1: Hook — Why Numerical Methods? (45s)
**Narration:** "Most differential equations cannot be solved analytically. The Laplace transform works for linear ODEs with constant coefficients, but real-world problems are often nonlinear. We need a different approach."
- Content budget: 4 items
- play_intro("Numerical Methods", "Ordinary Differential Equations")
- Motivating example: dy/dx = sin(x²) — no closed-form solution
- Key idea: "Instead of solving, we approximate step by step"
- ly.clear()

### Scene 2: Euler's Method — The Idea (90s)
**Narration:** "Euler's method is the simplest numerical approach. At each point, we follow the tangent line for a small step h."
- Content budget: 5 items
- Sub-scene 2a: The formula
  - MathTex: $y_{n+1} = y_n + h \cdot f(x_n, y_n)$
  - Explain each term: y_n is current value, h is step size, f gives the slope
- Sub-scene 2b: Geometric picture
  - Show a curve with tangent line at a point
  - Step along tangent: the approximation overshoots or undershoots
  - Next step: new tangent from the approximated point
- Sub-scene 2c: Visual stepping demo
  - Show 3-4 Euler steps on a curve, each step shown as a straight segment
- ly.clear()

### Scene 3: Error in Euler's Method (60s)
**Narration:** "Euler's method has a problem: each step introduces error, and the errors accumulate. The method is first-order accurate, meaning the error per step is proportional to h squared."
- Content budget: 5 items
- Show true curve vs Euler approximation on same axes
- Local error per step: O(h²)
- Global error over interval: O(h)
- Visual: gap between true and approximate curves grows
- Implication: halving step size halves the error — slow convergence
- ly.clear()

### Scene 4: Section Divider — Improved Methods (10s)
- ly.section_divider(3, "Better Methods")

### Scene 5: Improved Euler (Heun's Method) (90s)
**Narration:** "We can do better than Euler. The improved Euler method, also called Heun's method, uses the slope at the start AND the end of each step, then averages them."
- Content budget: 5 items
- Two-step process:
  1. Predictor: k₁ = f(xₙ, yₙ), predict y* = yₙ + h·k₁
  2. Corrector: k₂ = f(xₙ₊₁, y*), update yₙ₊₁ = yₙ + h/2 · (k₁ + k₂)
- Geometric intuition: "We look at the slope at the start, take a trial step, check the slope at the end, and average"
- Error: O(h³) per step, O(h²) globally — second-order accurate
- ly.clear()

### Scene 6: RK4 — The Gold Standard (120s)
**Narration:** "The Runge-Kutta fourth-order method, or RK4, takes this idea further. It evaluates the slope four times per step, at strategically chosen points, and combines them with carefully chosen weights."
- Content budget: 5 items
- Sub-scene 6a: The four slopes
  - k₁ = f(xₙ, yₙ)
  - k₂ = f(xₙ + h/2, yₙ + h·k₁/2)
  - k₃ = f(xₙ + h/2, yₙ + h·k₂/2)
  - k₄ = f(xₙ + h, yₙ + h·k₃)
- Sub-scene 6b: The formula
  - yₙ₊₁ = yₙ + h/6 · (k₁ + 2k₂ + 2k₃ + k₄)
- Sub-scene 6c: Why it works
  - "The weights (1, 2, 2, 1) over 6 match the coefficients of Simpson's rule"
  - Error: O(h⁵) per step, O(h⁴) globally — fourth-order!
  - "This is why RK4 is the workhorse of numerical ODE solving"
- ly.clear()

### Scene 7: Comparison (60s)
**Narration:** "Let's compare the three methods side by side."
- Content budget: 5 items
- Table/method comparison (progressive_reveal):
  1. Euler: O(h) global, 1 evaluation/step
  2. Improved Euler: O(h²) global, 2 evaluations/step
  3. RK4: O(h⁴) global, 4 evaluations/step
- Insight: "RK4 is 4x more work per step but much more accurate — you can use larger steps"
- ly.clear()

### Scene 8: Summary and Outro (45s)
**Narration recap:** "Numerical methods let us solve any ODE, even when no closed-form solution exists."
- Key takeaways (progressive_reveal):
  1. Euler: follow the tangent line, simple but inaccurate
  2. Error accumulates — Euler is only first-order
  3. Improved Euler averages slopes — second-order
  4. RK4 uses four evaluations — fourth-order, the standard
  5. In practice: use RK4 or adaptive methods (ode45)
- play_outro() — tease "Next up: Probability and Statistics"
- ly.clear()

## Technical Notes
- For Euler stepping visualization: draw tangent line segments on a pre-placed curve (use axes + VMobject curve + straight segments)
- Color code: true curve = PRIMARY, Euler = RED, RK4 = ACCENT, Improved Euler = SECONDARY
- Keep formulas readable — use multiple sub-scenes instead of cramming
- Step size h = 0.5 for visual clarity (not realistic, but visible on screen)
