# Video 187: Laplace's Equation

**Playlist:** Partial Differential Equations (Videos 184–193)
**Class:** Video187_LaplacesEquation
**Target Duration:** 12–15 minutes

## Competitive Analysis
- See channel-analysis/improvements.md — PDE playlist analysis
- 3B1B does NOT cover Laplace's equation
- commutant covers Laplace's equation (blackboard, 2011)
- Faculty of Khan covers Dirichlet problem (whiteboard)
- Our approach: harmonic functions, mean value property, max principle, animated

## Prerequisites
- Video 184 (What is a PDE?), Videos 185-186 (heat + wave)
- Calculus III (divergence, gradient)

## Scene Plan

### Scene 1: Hook — The Equation of Balance (60s)
- Intro (play_intro)
- Title: "The Equation of Equilibrium"
- No time evolution — steady state
- Temperature at equilibrium, electrostatic potential, fluid pressure

### Scene 2: What is Laplace's Equation? (60s)
- Title: "Definition"
- nabla^2 u = 0 (elliptic)
- No time dependence — everything is in balance
- Contrast: heat and wave equations both have time; Laplace is what remains

### Scene 3: Harmonic Functions (90s)
- Title: "Harmonic Functions"
- Definition: solutions to Laplace's equation
- Key properties: C-infinity (infinitely differentiable)
- Examples: u = x^2 - y^2, u = xy, u = ln(r), u = 1/r
- Any linear combination is also harmonic

### Scene 4: Mean Value Property (90s)
- Title: "The Mean Value Property"
- The value at any point equals the average over any circle/sphere
- u(x0) = (1/2pi) integral u(x0 + r cos(theta)) dtheta
- Physical meaning: no hot spots in equilibrium
- This is UNIQUE to harmonic functions

### Scene 5: Maximum Principle (90s)
- Title: "The Maximum Principle"
- A harmonic function has no interior maximum or minimum
- Max and min must be on the boundary
- Physical: in equilibrium, extreme values only at the edges
- Connection to heat equation: steady state has no interior peaks

### Scene 6: The Dirichlet Problem (120s)
- Title: "The Dirichlet Problem"
- Given boundary values, find u inside
- Well-posed: existence + uniqueness
- On a rectangle: separation of variables
- On a disk: Fourier series in polar coordinates

### Scene 7: Summary and Outro (60s)
- Key takeaways
- Laplace = equilibrium, harmonic functions
- Mean value property, maximum principle
- Dirichlet problem: boundary determines everything
- Next: Separation of Variables (general framework)
