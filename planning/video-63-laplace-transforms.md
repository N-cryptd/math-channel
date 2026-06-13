# Video 63: Laplace Transforms

**Playlist:** Ordinary Differential Equations
**Duration target:** 12–15 min
**Class name:** Video63_LaplaceTransforms

## Competitive Analysis References
- 3B1B "But what is a Laplace Transform?" (j0wJBEZdwLs, 1.69M views) — heavy theoretical, 34 min
- 3B1B "Why Laplace transforms are so useful" (FE-hM1kRK4Y, 748K views) — applied focus
- Dr. Trefor Bazett "Intro to the Laplace Transform" (KqokoYr_h1A, 1.34M views) — definition + 3 examples
- Steve Brunton "Generalized Fourier Transform" (7UvtU75NXTg, 366K views) — Fourier connection
- Full analysis in channel-analysis/improvements.md section "2026-06-13 — Laplace Transforms (Video 63)"

## Our Approach (different from competitors)
- **3B1B** spends 34 min on theory — we'll be practical: definition → properties → examples → solve ODE
- **Trefor** starts with definition then examples — we'll start with a **motivation problem** first (spring-mass), then definition
- **Brunton** frames as generalized Fourier — we won't assume Fourier background; we frame as ODE-solving tool
- **Key differentiator**: Progressive examples building from simplest (e^at) to step function, showing the transform's power

## Scene Breakdown

### Scene 1: Hook — When Algebra Beats Calculus (~45s)
**Motivation:** We've solved many ODEs, but there's a tool that turns calculus into algebra.
- Intro animation (play_intro)
- Title: "From Calculus to Algebra"
- Show: y'' + 3y' + 2y = f(t) — hard to solve directly
- Show: (s² + 3s + 2)Y = F(s) — algebra!
- Key question: "What if we could transform a differential equation into a polynomial equation?"
- Content budget: title + ODE + transformed ODE + question text = 4 items max

### Scene 2: The Definition (~90s)
- Title: "The Laplace Transform"
- Definition: L{f(t)} = ∫₀^∞ e^{-st} f(t) dt = F(s)
- Explain each part: f(t) is the "original", e^{-st} is the kernel, F(s) is the "transformed"
- Key insight: t → s domain (time to complex frequency)
- Color code: PRIMARY for t-domain, SECONDARY for s-domain
- Content budget: title + definition formula + "original" label + "transformed" label + insight text = 5

### Scene 3: Example 1 — The Simplest Transform (~60s)
- Title: "First Example: f(t) = e^{at}"
- Work through: L{e^{at}} = ∫₀^∞ e^{-(s-a)t} dt = 1/(s-a) for s > a
- Show the integral evaluation step by step
- Highlight the Region of Convergence condition (s > a)
- Content budget: title + original f(t) + integral step + result + ROC condition = 5

### Scene 4: Example 2 — Constants and Polynomials (~60s)
- Title: "Constants and Powers"
- f(t) = 1 → F(s) = 1/s (simplest!)
- f(t) = t → F(s) = 1/s² (integrate by parts or use the derivative property)
- Show the pattern: t^n → n!/s^{n+1}
- Brief mention: Gamma function connection (n! = Γ(n+1))
- Content budget: title + result for 1 + result for t + pattern formula = 4

### Scene 5: Key Property — Linearity and Derivatives (~90s)
- Section divider: "Key Properties"
- **Linearity**: L{af + bg} = aF(s) + bG(s) — just like integrals
- **The Magic Property**: L{f'(t)} = sF(s) - f(0)
- Show how this converts derivatives to multiplication by s
- **Second derivative**: L{f''(t)} = s²F(s) - sf(0) - f'(0)
- This is WHY Laplace transforms solve ODEs
- Content budget: 2 formulas visible at a time max, with title

### Scene 6: Solving an ODE with Laplace (~120s)
- Title: "Solving an ODE"
- Example: y' + 3y = 6, y(0) = 2
- Step 1: Transform both sides → sY - 2 + 3Y = 6/s
- Step 2: Solve algebraically → Y(s) = (2s + 6)/(s(s+3))
- Step 3: Partial fractions → Y(s) = 2/s
- Step 4: Invert → y(t) = 2
- Verify: y' + 3y = 0 + 6 = 6 ✓
- Content budget: progressive reveal, one step at a time, max 3 formulas visible

### Scene 7: The Heaviside Step Function (~60s)
- Title: "Piecewise Functions"
- Motivation: real systems have switches — circuits turn on, forces get applied
- Define H(t-a) = 0 for t < a, 1 for t ≥ a
- Key property: L{H(t-a)f(t-a)} = e^{-as}F(s)
- This is why Laplace handles piecewise forcing functions beautifully
- Content budget: title + definition graph + formula = 3

### Scene 8: Summary and Outlook (~45s)
- Title: "What We Learned"
- Summary points (progressive reveal):
  1. Laplace transform converts t-domain to s-domain
  2. Derivatives become multiplication by s
  3. ODEs become algebraic equations
  4. Partial fractions + table lookup for inversion
- Next video: Systems of ODEs with Laplace transforms
- Outro (play_outro)
- Content budget: title + 4 summary items (progressive reveal) = 5

## Pacing Notes
- Following competitive analysis: slow enough for intuition (unlike Brunton), but practical (unlike 3B1B's 34min)
- Each worked example gets ~60-90s with progressive formula reveals
- The ODE solving scene is the longest (~2 min) — this is the payoff scene
- Color scheme: PRIMARY=#5BC0EB for t-domain, SECONDARY=#7BC950 for s-domain, ACCENT=#FFD166 for key results
