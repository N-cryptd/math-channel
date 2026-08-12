# Video 186: The Wave Equation

**Playlist:** Partial Differential Equations (Videos 184–193)
**Class:** Video186_WaveEquation
**Target Duration:** 12–15 minutes
**Level:** Undergraduate

## Competitive Analysis References
- See channel-analysis/improvements.md — PDE playlist analysis
- 3B1B covers wave equation visually (DE series)
- commutant: wave equation separation (342K views, 2011, blackboard)
- Faculty of Khan covers d'Alembert solution (whiteboard)
- Our approach: animated derivation + d'Alembert + separation of variables

## Prerequisites
- Video 184 (What is a PDE?), Video 185 (Heat Equation)
- Calculus III, Fourier Series (174-176)

## Scene Plan

### Scene 1: Hook — Vibrations Everywhere (60s)
**Content budget:** 4 items
- Intro (play_intro)
- Title: "The Mathematics of Vibration"
- Guitar strings, drum heads, electromagnetic waves, sound
- All governed by the same equation

### Scene 2: Derivation from a Vibrating String (120s)
**Content budget:** 5 items
- Title: "Deriving the Wave Equation"
- Consider a taut string under tension T
- Small segment: net vertical force = T(u_xx dx)
- Newton's 2nd law: mass * acceleration = net force
- Result: u_tt = c^2 u_xx where c = sqrt(T/rho)

### Scene 3: Physical Interpretation (60s)
**Content budget:** 4 items
- Title: "What Does It Mean?"
- Acceleration (2nd time derivative) proportional to curvature
- Wave speed c depends on tension and density
- Unlike heat equation: second order in time → oscillations, not decay

### Scene 4: Initial Conditions (60s)
**Content budget:** 5 items
- Title: "Two Initial Conditions"
- u(x, 0) = f(x) — initial displacement
- u_t(x, 0) = g(x) — initial velocity
- Need TWO conditions (second order in time, unlike heat equation's one)
- Boundary conditions same as heat: Dirichlet or Neumann

### Scene 5: d'Alembert's Solution on the Real Line (120s)
**Content budget:** 5 items
- Section divider: "d'Alembert's Solution"
- No boundaries (infinite string)
- Factor the operator: (d/dt - c d/dx)(d/dt + c d/dx)u = 0
- General solution: u(x,t) = F(x - ct) + G(x + ct)
- Right-moving wave F(x-ct) and left-moving wave G(x+ct)
- Specific form with initial conditions

### Scene 6: Separation of Variables (120s)
**Content budget:** 5 items
- Title: "Separation of Variables on [0, L]"
- Same ansatz: u(x,t) = X(x)T(t)
- Spatial: X'' + lambda X = 0, same eigenvalues as heat equation
- Temporal: T'' + lambda c^2 T = 0 (oscillation, not decay!)
- T_n(t) = A_n cos(n pi c t / L) + B_n sin(n pi c t / L)

### Scene 7: Complete Solution — Standing Waves (90s)
**Content budget:** 5 items
- Title: "Standing Waves"
- u(x,t) = sum [A_n cos + B_n sin] sin(n pi x / L)
- Each mode is a standing wave at a specific frequency
- Frequencies: f_n = nc/(2L) — the harmonic series
- Overtones in music are exactly these frequencies

### Scene 8: Summary and Outro (60s)
**Content budget:** 5 items
- Title: "Key Takeaways"
- Wave equation: second order in time → oscillations
- d'Alembert: superposition of left/right traveling waves
- Separation: standing waves at discrete frequencies
- Next: Laplace's Equation

## Visual Design Notes
- Color: PRIMARY (blue) for wave equation consistently
- Animate a traveling wave: F(x - ct) moving right
- Show standing waves as animated sine curves oscillating in place
- Show the harmonic series frequencies as a spectrum
