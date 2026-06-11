# Video 59: Initial Value Problems for Second-Order ODEs

## Overview
- **Playlist:** Ordinary Differential Equations
- **Duration target:** 10-12 minutes
- **Class name:** `Video59_SecondOrderIVP`
- **Script file:** `scripts/undergraduate/video-59-second-order-ivp.py`

## Competitive Analysis Reference
No dedicated competitive analysis was run for this video. The plan draws on general
observations from ODE playlists by Trefor Bazett, 3Blue1Brown (DE chapter),
and Khan Academy. Key decisions:
- Connect directly from Video 58's general solutions (with C1, C2) to IVPs
- Show that second-order IVPs need TWO initial conditions (unlike first-order's one)
- Physical motivation: specify both position AND velocity at time zero
- Work through 3 examples: one for each root type (real, repeated, complex)
- Color-code: ICs in RED, solution parts in PRIMARY/SECONDARY, computed values in ACCENT
- Keep it practical and mechanical — the theory is done, now apply it

## Scene Plan

### Scene 1: Hook — Finding C1 and C2 (~1.5 min)
**Content budget (max 5 items):** Title, recall general solution, problem statement, two ICs
- Start with play_intro()
- "Last time we found general solutions with C1 and C2. But which solution is THE solution?"
- "In the real world, we know the state at one moment. For a spring: position AND velocity."
- "An initial value problem gives us a specific ODE plus initial conditions to pin down C1 and C2."
- "A second-order IVP needs TWO initial conditions — that is new."

### Scene 2: Setting Up an IVP (~1.5 min)
**Content budget:** Section divider, general form, physical meaning, example setup
- Section divider "1 — What Is an IVP?"
- General form: ay'' + by' + cy = 0, with y(0) = y₀, y'(0) = v₀
- "The first condition fixes the starting value. The second fixes the starting rate of change."
- Physical analogy: throwing a ball — you need both position and velocity to predict the path
- "The process: find the general solution, then plug in the ICs to solve for C1 and C2."

### Scene 3: Example 1 — Distinct Real Roots (~2 min)
**Content budget:** Section divider, equation, general solution, two equations, solve, answer
- Section divider "2 — Example: Distinct Real Roots"
- y'' - 3y' + 2y = 0, with y(0) = 1, y'(0) = 0
- From Video 58: characteristic equation r² - 3r + 2 = 0 → r = 1, 2
- General solution: y = C1·e^x + C2·e^{2x}
- IC 1: y(0) = C1 + C2 = 1
- IC 2: y'(0) = C1 + 2C2 = 0
- System: C1 + C2 = 1, C1 + 2C2 = 0 → C2 = -1, C1 = 2
- Particular solution: y = 2e^x - e^{2x}

### Scene 4: Example 2 — Repeated Root (~2 min)
**Content budget:** Section divider, equation, general solution, two ICs, solve, answer
- Section divider "3 — Example: Repeated Root"
- y'' - 4y' + 4y = 0, with y(0) = 3, y'(0) = 5
- Characteristic equation: r² - 4r + 4 = 0 → r = 2 (repeated)
- General solution: y = C1·e^{2x} + C2·x·e^{2x}
- IC 1: y(0) = C1 = 3
- IC 2: y'(0) = 2C1 + C2 = 5 → C2 = -1
- Particular solution: y = 3e^{2x} - x·e^{2x}
- "Notice: the repeated root makes y' a bit more involved because of the chain rule on x·e^{2x}"

### Scene 5: Example 3 — Complex Roots (~2 min)
**Content budget:** Section divider, equation, general solution, two ICs, solve, answer
- Section divider "4 — Example: Complex Roots"
- y'' + 2y' + 5y = 0, with y(0) = 0, y'(0) = 1
- From Video 58: α = -1, β = 2
- General solution: y = e^{-x}(C1·cos(2x) + C2·sin(2x))
- IC 1: y(0) = e^0(C1·1 + C2·0) = C1 = 0
- IC 2: y'(x) needs chain rule: -e^{-x}(C1·cos2x + C2·sin2x) + e^{-x}(-2C1·sin2x + 2C2·cos2x)
- y'(0) = -C1 + 2C2 = 1 → since C1 = 0: C2 = 1/2
- Particular solution: y = (1/2)e^{-x}·sin(2x)
- "A pure oscillation with exponential decay — starts at zero with velocity 1"

### Scene 6: The System Method (~1.5 min)
**Content budget:** Section divider, general method, matrix form, summary
- Section divider "5 — The General Method"
- Step 1: Find the general solution (characteristic equation + roots + formula)
- Step 2: Compute y'(x) from the general solution
- Step 3: Plug x=0 into both y(x) and y'(x)
- Step 4: Solve the 2×2 system for C1 and C2
- "You always get a 2×2 linear system. Easy to solve by elimination or substitution."

### Scene 7: Summary + Preview (~1 min)
**Content budget:** Summary items, next video teaser, outro
- Second-order IVP: ay'' + by' + cy = 0, y(0) = y₀, y'(0) = v₀
- Two initial conditions → 2×2 system for C1, C2
- Method works for all three root types
- "Next: what happens when f(x) ≠ 0? Non-homogeneous equations and particular solutions."
- play_outro() — tease "Non-Homogeneous Second-Order Equations"

## Key Formulas
- General form: ay'' + by' + cy = 0
- ICs: y(0) = y₀, y'(0) = v₀
- Example 1: y = 2e^x - e^{2x}
- Example 2: y = 3e^{2x} - x·e^{2x}
- Example 3: y = (1/2)e^{-x}·sin(2x)
- Chain rule for y': y = C1·e^{rx} + C2·x·e^{rx} → y' = r·C1·e^{rx} + C2·e^{rx} + r·C2·x·e^{rx}
- Chain rule for complex: y = e^{αx}(C1·cos βx + C2·sin βx) → more involved

## Animation Notes
- Scene 3-5 examples follow the same 4-step visual pattern for consistency
- The 2×2 system appearing is the "aha" moment — show both equations side by side
- For complex root example (Scene 5), the chain rule on y' is the tricky part — animate step by step
- Color-code consistently: ICs in RED, general solution parts in PRIMARY/SECONDARY, computed C values in ACCENT
