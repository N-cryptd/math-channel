# Video 64: Systems of ODEs

## Overview
- **Playlist:** Ordinary Differential Equations
- **Duration target:** 10-15 minutes
- **Class name:** `Video64_SystemsOfODEs`
- **Script file:** `scripts/undergraduate/video-64-systems-of-odes.py`

## Competitive Analysis Reference
Competitive analysis run 2026-06-13. Key findings from 4 competitor videos:

**3Blue1Brown — "But what is a differential equation?" and ODE series:**
- Owns the visual/intuition space with stunning phase plane animations
- Skips the actual eigenvalue solving method — viewers leave inspired but unable to solve
- Uses flow fields and vector field visualizations brilliantly

**Trefor Bazett — Systems of DEs playlist:**
- Best balance of computation and explanation
- Uses tablet-style writing (not Manim), less visually dynamic
- Covers decoupling, eigenvalue method thoroughly with worked examples

**Khan Academy — Systems of differential equations:**
- Exhaustive coverage but dated visuals and monotone delivery
- Nearly geometry-free — no phase portraits in the main lessons
- Good for completeness, poor for engagement

**BriTheMathGuy — Systems of ODEs:**
- Fast and punchy, good for review not first exposure
- Shallow on both intuition and rigor
- No animated visuals

**Our strategy — fill the upper-right quadrant:**
- High Manim-quality visuals (phase planes, vector fields) AND complete eigenvalue-method computation
- Physical motivation opening (coupled predator-prey or spring system)
- Single running example carried through the entire video
- Animated phase plane showing solution trajectories forming from eigenvectors
- End with "what if" teaser for follow-ups (complex eigenvalues, nonlinear systems)

## Scene Plan

### Scene 1: Hook — Why Systems? (~2 min)
**Content budget (max 5 items):** Title, physical scenario, coupled equations, matrix form reveal
- Start with play_intro()
- "So far every equation we have solved involved a single unknown function. But in the real world, quantities interact."
- Show a physical scenario: two tanks connected by pipes, or a spring-mass system
- "The amount of salt in tank A depends on tank B, and vice versa. We cannot solve them independently."
- Reveal the coupled system: x' = ax + by, y' = cx + dy
- "We need a method that handles both equations at once. The answer: write it as a matrix."

### Scene 2: From Equations to Matrices (~2 min)
**Content budget:** Section divider, coupled system, vector notation, matrix form
- Section divider "1 — Matrix Form"
- Start with the general coupled system:
  x' = ax + by
  y' = cx + dy
- Introduce vector notation: let x = [x, y]^T, then x' = Ax where A = [[a,b],[c,d]]
- "This compact form hides all the structure. To solve x' = Ax, we need to know how to exponentiate a matrix."
- Motivate eigenvalues: "If Av = lambda*v, then e^{At}*v = e^{lambda*t}*v"
- The key idea: eigenvectors give us special directions where the system simplifies

### Scene 3: The Eigenvalue Method (~3 min)
**Content budget:** Section divider, assumption, substitution, characteristic equation, eigenvectors
- Section divider "2 — The Eigenvalue Method"
- Assume solution of the form x(t) = e^{lambda*t} * v (vector)
- Substitute into x' = Ax: lambda * e^{lambda*t} * v = A * e^{lambda*t} * v
- Cancel e^{lambda*t}: Av = lambda*v — the eigenvalue equation!
- The characteristic equation: det(A - lambda*I) = 0
- "This gives us the eigenvalues. For each eigenvalue, find the eigenvector."
- Each eigenvalue-eigenvector pair gives one solution: e^{lambda*t} * v

### Scene 4: Worked Example — Two Tanks (~3 min)
**Content budget:** Section divider, system setup, matrix, characteristic eq, eigenvalues, eigenvectors, general solution
- Section divider "3 — Worked Example"
- Use a concrete 2x2 system:
  x' = -3x + y
  y' = 2x - 4y
- Matrix form: A = [[-3, 1], [2, -4]]
- Characteristic equation: (lambda + 3)(lambda + 4) - 2 = lambda^2 + 7lambda + 10 = 0
- Eigenvalues: lambda_1 = -2, lambda_2 = -5
- Eigenvector for lambda_1 = -2: v_1 = [1, 1]^T
- Eigenvector for lambda_2 = -5: v_2 = [1, -2]^T
- General solution: x(t) = c_1 * e^{-2t} * [1,1] + c_2 * e^{-5t} * [1,-2]
- "Both eigenvalues are negative, so every solution decays to zero."

### Scene 5: Phase Plane Basics (~3 min)
**Content budget:** Section divider, phase plane axes, eigenvector directions, trajectory animation, equilibrium
- Section divider "4 — The Phase Plane"
- "Instead of plotting x and y against time, plot them against each other."
- Show axes: horizontal = x, vertical = y
- Draw the eigenvector directions as straight lines through the origin
- "Along the eigenvector [1,1], the solution is pure exponential decay in that direction."
- "Along the eigenvector [1,-2], the solution decays even faster in that direction."
- Animate: trajectories curve toward the origin, pulled by both eigenvalue directions
- "Because both eigenvalues are negative, the origin is a stable node — all solutions spiral inward."
- "If one eigenvalue were positive, the origin would be a saddle — some solutions escape."
- Brief classification: stable node (both neg), unstable node (both pos), saddle (mixed), spiral (complex)

### Scene 6: Summary + Preview (~1.5 min)
**Content budget:** Summary items, formula recap, next video teaser, outro
- Coupled systems arise naturally when quantities interact
- Write x' = Ax in matrix form
- Eigenvalue method: det(A - lambda*I) = 0, find eigenvectors
- General solution: linear combination of e^{lambda_i * t} * v_i
- Phase plane visualizes solution behavior qualitatively
- "Next: Phase Portraits — classifying equilibrium points and drawing complete phase diagrams."
- play_outro() — tease "Phase Portraits"

## Key Formulas
- Coupled system: x' = ax + by, y' = cx + dy
- Matrix form: x' = Ax where x = [x, y]^T, A = [[a,b],[c,d]]
- Eigenvalue assumption: x(t) = e^{lambda*t} * v
- Eigenvalue equation: Av = lambda*v
- Characteristic equation: det(A - lambda*I) = 0
- General solution: x(t) = c_1 * e^{lambda_1*t} * v_1 + c_2 * e^{lambda_2*t} * v_2
- Example: lambda_1 = -2, v_1 = [1,1]; lambda_2 = -5, v_2 = [1,-2]

## Animation Notes
- Scene 1: Use a simple two-tank diagram with arrows to show coupling
- Scene 2: Animate the transition from component equations to matrix form step by step
- Scene 3: The eigenvalue derivation is the "aha moment" — animate the cancellation of e^{lambda*t} to reveal Av = lambda*v
- Scene 4: Color-code the two eigenvector solutions (PRIMARY for lambda_1, SECONDARY for lambda_2)
- Scene 5: The phase plane trajectory animation is the signature visual — animate curves forming from both eigenvector directions
- Scene 5: Keep the classification brief — just name the types and show one representative sketch for each; full classification comes in Video 65
- Use vector field arrows (numbered plane) in the phase plane for visual richness
