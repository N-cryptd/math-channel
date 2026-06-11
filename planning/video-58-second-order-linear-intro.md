# Video 58: Second-Order Linear Equations — Introduction

## Overview
- **Playlist:** Ordinary Differential Equations
- **Duration target:** 10-12 minutes
- **Class name:** `Video58_SecondOrderLinearIntro`
- **Script file:** `scripts/undergraduate/video-58-second-order-linear-intro.py`

## Competitive Analysis Reference
No dedicated competitive analysis was run for this video. The plan draws on general
observations from ODE playlists by Trefor Bazett, 3Blue1Brown (DE chapter),
and Khan Academy. Key decisions:
- Start by contrasting first-order vs second-order — keep the transition natural from Video 57
- Introduce the characteristic equation as the central tool (not just "memorize")
- Show the physical motivation: springs and pendulums (following Trefor Bazett's applied approach)
- Derive the general solution structure: complementary + particular
- Color-code: homogeneous solutions in PRIMARY/SECONDARY, particular in ACCENT, forcing term in RED
- Keep it focused on constant-coefficient homogeneous — save variation of parameters for a later video

## Scene Plan

### Scene 1: Hook — Beyond First Order (~1.5 min)
**Content budget (max 5 items):** Title, recall first-order, spring example, second-order reveal
- Start with play_intro()
- "We've solved first-order equations — one derivative, one initial condition. Clean."
- "But the real world isn't always that simple. Think of a mass on a spring..."
- "Newton's second law gives us F = ma, which means d²y/dt² — a SECOND derivative."
- "These are second-order equations, and they're everywhere: springs, circuits, pendulums."
- Reveal: d²y/dx² + P(x) dy/dx + Q(x) y = R(x) — the general second-order linear ODE

### Scene 2: What Does Second-Order Mean? (~1.5 min)
**Content budget:** Section divider, definition, key terms, examples
- Section divider "1 — Anatomy of a Second-Order ODE"
- Standard form: ay'' + by' + cy = f(x), where a ≠ 0
- a, b, c are coefficients; f(x) is the forcing function
- Homogeneous: f(x) = 0 → ay'' + by' + cy = 0
- Non-homogeneous: f(x) ≠ 0
- "We'll start with the homogeneous case — it's the foundation"
- Key property: superposition! If y1 and y2 are solutions, then c1·y1 + c2·y2 is also a solution

### Scene 3: The Characteristic Equation (~2.5 min)
**Content budget:** Section divider, ansatz, derivation, three cases
- Section divider "2 — The Characteristic Equation"
- "The key insight: try y = e^{rx} as a trial solution"
- If y = e^{rx}, then y' = r·e^{rx}, y'' = r²·e^{rx}
- Substitute into ay'' + by' + cy = 0:
  a·r²·e^{rx} + b·r·e^{rx} + c·e^{rx} = 0
- Factor out e^{rx} (never zero): ar² + br + c = 0 — the characteristic equation!
- "The solutions to this QUADRATIC tell us everything about the ODE"
- Three cases based on the discriminant D = b² - 4ac:
  1. D > 0: two distinct real roots r1, r2 → y = C1·e^{r1x} + C2·e^{r2x}
  2. D = 0: one repeated root r → y = C1·e^{rx} + C2·x·e^{rx}
  3. D < 0: complex roots α ± βi → y = e^{αx}(C1·cos(βx) + C2·sin(βx))

### Scene 4: Example 1 — Distinct Real Roots (~1.5 min)
**Content budget:** Section divider, equation, characteristic eq, roots, solution
- Section divider "3 — Example: Two Distinct Roots"
- y'' - 5y' + 6y = 0
- Characteristic equation: r² - 5r + 6 = 0 → (r-2)(r-3) = 0 → r = 2, 3
- General solution: y = C1·e^{2x} + C2·e^{3x}
- "Two exponential solutions combined with arbitrary constants"
- Physical interpretation: the solution grows without bound (both roots positive)

### Scene 5: Example 2 — Repeated Roots (~1.5 min)
**Content budget:** Section divider, equation, characteristic eq, repeated root, solution
- Section divider "4 — Example: Repeated Root"
- y'' - 4y' + 4y = 0
- Characteristic equation: r² - 4r + 4 = 0 → (r-2)² = 0 → r = 2 (repeated)
- General solution: y = C1·e^{2x} + C2·x·e^{2x}
- "When the root repeats, we need a second solution — x·e^{rx} does the trick"
- Show that both e^{2x} and x·e^{2x} satisfy the ODE (verification)

### Scene 6: Example 3 — Complex Roots (~1.5 min)
**Content budget:** Section divider, equation, characteristic eq, complex roots, solution
- Section divider "5 — Example: Complex Roots"
- y'' + 2y' + 5y = 0
- Characteristic equation: r² + 2r + 5 = 0 → r = (-2 ± √(-16))/2 = -1 ± 2i
- α = -1, β = 2
- General solution: y = e^{-x}(C1·cos(2x) + C2·sin(2x))
- "Complex roots always give oscillating solutions — waves, vibrations, resonance"

### Scene 7: Summary + Preview (~1 min)
**Content budget:** Summary items, formula recap, next video teaser, outro
- Second-order linear ODE: ay'' + by' + cy = f(x)
- Characteristic equation: ar² + br + c = 0
- Three cases: real distinct, repeated, complex
- Superposition principle: linear combinations of solutions are solutions
- "Next time: initial value problems — how do we find C1 and C2?"
- play_outro() — tease "Initial Value Problems for Second-Order ODEs"

## Key Formulas
- Standard form: ay'' + by' + cy = f(x)
- Trial solution: y = e^{rx}
- Characteristic equation: ar² + br + c = 0
- Discriminant: D = b² - 4ac
- Case 1 (D > 0): y = C1·e^{r1x} + C2·e^{r2x}
- Case 2 (D = 0): y = C1·e^{rx} + C2·x·e^{rx}
- Case 3 (D < 0): y = e^{αx}(C1·cos(βx) + C2·sin(βx))
- Example 1: y = C1·e^{2x} + C2·e^{3x}
- Example 2: y = C1·e^{2x} + C2·x·e^{2x}
- Example 3: y = e^{-x}(C1·cos(2x) + C2·sin(2x))

## Animation Notes
- Scene 3 derivation is the signature moment — animate the trial solution substitution step by step
- Color-code consistently: r1 in PRIMARY, r2 in SECONDARY, repeated root in ACCENT, complex parts in PRIMARY/SECONDARY
- For the three cases, use consistent layout: show characteristic equation → discriminant → roots → solution
- The physical spring/mass motivation could use a simple NumberLine oscillation, but keep it minimal
- Transition from Video 57's first-order focus to this video's second-order should feel like a natural deepening
