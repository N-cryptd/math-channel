# Video 185: The Heat Equation

**Playlist:** Partial Differential Equations (Videos 184–193)
**Class:** Video185_HeatEquation
**Target Duration:** 12–15 minutes
**Level:** Undergraduate (follows Video 184, connects to Fourier Analysis Video 182)

## Relationship to Video 182
Video 182 covered the heat equation from the Fourier transform perspective:
- Heat kernel on the whole real line R
- Gaussian spreading and convolution
- Fourier transform converts PDE to ODE

Video 185 covers the classical PDE approach:
- Derivation from Fourier's law of heat conduction
- Finite interval [0, L] with boundary conditions
- Separation of variables → Fourier sine series
- Specific solutions with different initial conditions

These are complementary — Video 182 is the transform approach, Video 185 is the series approach.

## Competitive Analysis References
- See channel-analysis/improvements.md — PDE playlist analysis
- 3B1B DE2 covers heat equation intuition (3.2M views) — visual, non-rigorous
- commutant "Heat equation: intuition" (234K views) — blackboard, physical reasoning
- Faculty of Khan covers separation of variables rigorously (whiteboard)
- The Bright Side of Mathematics covers heat equation via FT (PDE series)
- Our approach: combine physical intuition with rigorous separation of variables, animated

## Prerequisites
- Video 184 (What is a PDE?)
- Calculus III (partial derivatives, gradients)
- Fourier Series (Videos 174-176) — for the solution series

## Scene Plan

### Scene 1: Hook — From Coffee to Metals (60s)
**Content budget:** 4 items
- Intro (play_intro)
- Title: "The Equation of Heat"
- Physical motivation: why does your coffee cool down?
- Preview: we'll derive the PDE from basic physics
**Narration:** ~30 words (12s)

### Scene 2: Derivation from Physical Reasoning (120s)
**Content budget:** 5 items
- Title: "Deriving the Heat Equation"
- Fourier's law: heat flux ∝ negative temperature gradient
- Conservation of energy in a thin slice
- Balance equation: rate of change = flux in - flux out
- The 1D heat equation: ∂u/∂t = α ∂²u/∂x²
**Narration:** ~60 words (24s)

### Scene 3: Physical Interpretation (60s)
**Content budget:** 4 items
- Title: "What Does It Mean?"
- Curvature interpretation: heat flows away from peaks
- α is the thermal diffusivity (how fast heat spreads)
- Higher curvature → faster change
**Narration:** ~30 words (12s)

### Scene 4: Initial and Boundary Conditions (90s)
**Content budget:** 5 items
- Title: "Setting Up the Problem"
- Initial condition: u(x, 0) = f(x) — starting temperature
- Dirichlet BC: u(0,t) = u(L,t) = 0 (fixed temperature at ends)
- Neumann BC: ∂u/∂x(0,t) = 0 (insulated end)
- We'll focus on Dirichlet with fixed zero endpoints
**Narration:** ~45 words (18s)

### Scene 5: Separation of Variables — Setup (120s)
**Content budget:** 5 items
- Section divider: "Solving by Separation of Variables"
- Assume u(x,t) = X(x)T(t)
- Substitute into the heat equation
- Divide by XT to separate: T'/T = α X''/X
- Each side must equal a constant (say, -λ)
**Narration:** ~55 words (22s)

### Scene 6: The Spatial Problem — Eigenvalues (120s)
**Content budget:** 5 items
- Title: "The Spatial Equation"
- X'' + λX = 0 with X(0) = X(L) = 0
- Solutions: X_n(x) = sin(nπx/L) for λ_n = (nπ/L)²
- Only certain λ values work (eigenvalues!)
- Connection to Fourier sine series
**Narration:** ~55 words (22s)

### Scene 7: The Temporal Problem (90s)
**Content budget:** 5 items
- Title: "The Time Equation"
- T' + αλT = 0
- Exponential decay: T_n(t) = exp(-α(nπ/L)²t)
- Higher modes decay faster (smoothing effect)
- The complete solution: sum of all modes
**Narration:** ~45 words (18s)

### Scene 8: Complete Solution (90s)
**Content budget:** 5 items
- Title: "The Full Solution"
- u(x,t) = Σ b_n sin(nπx/L) exp(-α(nπ/L)²t)
- Fourier sine coefficients: b_n = (2/L)∫f(x)sin(nπx/L)dx
- Initial condition determines all coefficients
- As t→∞, u→0 (equilibrium)
**Narration:** ~50 words (20s)

### Scene 9: Visual Example (90s)
**Content budget:** 5 items
- Title: "Example: Triangular Initial Temperature"
- Initial: f(x) = triangular spike in the middle
- Show first few Fourier modes
- Show how they decay differently
- Result: smoothing toward equilibrium
**Narration:** ~45 words (18s)

### Scene 10: Summary and Outro (60s)
**Content budget:** 5 items
- Title: "Key Takeaways"
- Key points:
  - Heat equation derived from conservation + Fourier's law
  - Separation of variables: product solution u=XT
  - Boundary conditions → eigenvalues → discrete spectrum
  - Higher modes decay exponentially faster → smoothing
- Outro (next: Wave Equation)
**Narration:** ~30 words (12s)

## Visual Design Notes
- Color code consistently with Video 184: SECONDARY (green) for heat equation
- Animate the separation process: show u(x,t) splitting into X(x) and T(t)
- Show Fourier modes as animated sine waves with decay
- Temperature profile visualization: color gradient from hot to cold
- Show the eigenvalues appearing as a discrete spectrum

## Estimated Total Duration: ~12 minutes
