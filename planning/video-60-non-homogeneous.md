# Video 60: Non-Homogeneous Second-Order Equations

## Overview
- **Playlist:** Ordinary Differential Equations
- **Duration target:** 10-12 minutes
- **Class name:** `Video60_NonHomogeneous`
- **Script file:** `scripts/undergraduate/video-60-non-homogeneous.py`

## Competitive Analysis Reference
No dedicated competitive analysis was run. General observations from Trefor Bazett,
3Blue1Brown (DE chapter), and Khan Academy:
- Frame the method of undetermined coefficients as a "guessing game" with rules
- Start by recalling the homogeneous solution (complementary function)
- Introduce the particular solution as the "new ingredient"
- Show the superposition structure: y = y_c + y_p
- Work through two clear examples: polynomial forcing, exponential forcing
- Color-code: complementary (y_c) in PRIMARY, particular (y_p) in ACCENT, forcing f(x) in RED

## Scene Plan

### Scene 1: Hook — When the Right Side Is Not Zero (~1.5 min)
**Content budget (max 5 items):** Title, recall homogeneous, forcing function, equation
- Start with play_intro()
- "So far, the right side has always been zero. But in physics, forces act on systems."
- "A forced spring: ay'' + by' + cy = F(t) — the right side is the external force"
- "We need a new technique: the particular solution"
- "The key insight: general solution = complementary + particular"

### Scene 2: Structure of the Solution (~1.5 min)
**Content budget:** Section divider, structure formula, definitions, superposition
- Section divider "1 — Complementary + Particular"
- y = y_c + y_p, where y_c is the homogeneous solution, y_p is any particular solution
- "y_c already has two arbitrary constants — that is all we need"
- "y_p just needs to satisfy the equation with the forcing term"
- "This decomposition works because the equation is linear"

### Scene 3: Method of Undetermined Coefficients (~2.5 min)
**Content budget:** Section divider, method overview, guess table, modification rule
- Section divider "2 — Method of Undetermined Coefficients"
- "The idea: if f(x) is a polynomial, exponential, sine, or cosine — guess a similar form for y_p"
- Guess rules:
  - f(x) = polynomial → guess polynomial of same degree
  - f(x) = e^{kx} → guess A·e^{kx}
  - f(x) = sin(kx) or cos(kx) → guess A·sin(kx) + B·cos(kx)
- **Caution**: if your guess overlaps with y_c, multiply by x (or x² for double overlap)
- "This is not magic — it is an educated guess with systematic rules"

### Scene 4: Example 1 — Polynomial Forcing (~2 min)
**Content budget:** Section divider, equation, y_c, guess y_p, solve, full solution
- Section divider "3 — Example: Polynomial Forcing"
- y'' - 3y' + 2y = 4x²
- y_c = C1·e^x + C2·e^{2x} (from characteristic equation r²-3r+2=0)
- Guess: y_p = Ax² + Bx + C (same degree as RHS)
- y_p' = 2Ax + B, y_p'' = 2A
- Substitute: 2A - 3(2Ax+B) + 2(Ax²+Bx+C) = 4x²
- Match coefficients: 2A=4 → A=2, -6A+2B=0 → B=6, 2A-3B+2C=0 → C=8
- y_p = 2x² + 6x + 8
- Full solution: y = C1·e^x + C2·e^{2x} + 2x² + 6x + 8

### Scene 5: Example 2 — Exponential Forcing (~2 min)
**Content budget:** Section divider, equation, y_c, guess y_p, solve, full solution
- Section divider "4 — Example: Exponential Forcing"
- y'' + y' - 2y = 3e^{3x}
- y_c = C1·e^x + C2·e^{-2x} (characteristic: r²+r-2=0 → r=1,-2)
- Guess: y_p = A·e^{3x}
- y_p' = 3A·e^{3x}, y_p'' = 9A·e^{3x}
- Substitute: 9A + 3A - 2A = 3 → 10A = 3 → A = 3/10
- y_p = (3/10)·e^{3x}
- Full solution: y = C1·e^x + C2·e^{-2x} + (3/10)e^{3x}

### Scene 6: Summary + Preview (~1 min)
**Content budget:** Summary items, formula recap, next video teaser, outro
- Non-homogeneous equation: ay'' + by' + cy = f(x)
- Solution structure: y = y_c + y_p
- Method: guess y_p based on f(x), substitute, match coefficients
- Watch for overlap with y_c — multiply by x if needed
- "Next: variation of parameters — a more general method that works for any f(x)"
- play_outro() — tease "Variation of Parameters"

## Key Formulas
- ay'' + by' + cy = f(x)
- y = y_c + y_p
- Example 1: y = C1·e^x + C2·e^{2x} + 2x² + 6x + 8
- Example 2: y = C1·e^x + C2·e^{-2x} + (3/10)e^{3x}
- Polynomial forcing → polynomial guess (same degree)
- Exponential forcing → exponential guess (same base)
