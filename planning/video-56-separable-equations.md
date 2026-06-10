# Video 56: First-Order Separable Equations

## Overview
- **Playlist:** Ordinary Differential Equations
- **Duration target:** 10-12 minutes
- **Class name:** `Video56_SeparableEquations`
- **Script file:** `scripts/undergraduate/video-56-separable-equations.py`

## Competitive Analysis Reference
See `channel-analysis/improvements.md` entry for 2026-06-09 (Video 56).
Key decisions:
- Hook with solving dy/dx = rN from Video 55 (adopting Trefor Bazett's "now we solve it" framing)
- Animated algebraic manipulation of variable separation (our innovation — going beyond Khan's static whiteboard)
- Progressive examples: simple (exponential) → applied (cooling) → tricky (xy product)
- Section divider pattern for clear structure

## Scene Plan

### Scene 1: Hook — We Can Actually Solve This (~2 min)
**Content budget (max 5 items):** Title, recall DE from Video 55, separation visualization, solution reveal
- Start with play_intro()
- "Remember from the last video? We had dN/dt = rN, the population growth equation."
- Show the equation dy/dx = ky (general form)
- "What if I told you there's a trick to solve equations like this?"
- Separate: dy/y = k dx → integrate → ln|y| = kx + C → y = Ce^(kx)
- Key reveal: the solution is an exponential function!

### Scene 2: Definition — What Makes an Equation Separable? (~2 min)
**Content budget:** Section divider, definition text, separable form, recognition examples
- Section divider "1 — Definition"
- A first-order ODE is separable if it can be written as: dy/dx = g(x) · h(y)
- The key: the x stuff and y stuff are MULTIPLIED, not mixed
- Non-examples: dy/dx = x + y (NOT separable — can't separate), dy/dx = sin(xy) (NOT separable)
- Test: can you algebraically move all y terms to one side and all x terms to the other?
- Progressive reveal of separable vs non-separable examples

### Scene 3: The Separation Technique (~2.5 min)
**Content budget:** Section divider, step-by-step procedure, animated manipulation
- Section divider "2 — The Technique"
- Step 1: Write in form dy/dx = g(x)h(y)
- Step 2: "Separate" the variables: move all y terms (including dy) to the left, all x terms (including dx) to the right
  - Visually: dy/h(y) = g(x)dx
- Step 3: Integrate both sides: ∫ dy/h(y) = ∫ g(x)dx
- Step 4: Solve for y (if possible)
- Animated: show the terms physically "sliding" to their respective sides
- This is the central teaching moment of the video

### Scene 4: Example 1 — Exponential Growth/Decay (~2 min)
**Content budget:** Section divider, equation setup, step-by-step solution, answer highlight
- Section divider "3 — Example: Exponential Growth"
- dy/dx = -0.1y (decay with rate 0.1)
- Step 1: Already in separable form: g(x) = -0.1, h(y) = y
- Step 2: dy/y = -0.1 dx
- Step 3: ∫ dy/y = ∫ -0.1 dx → ln|y| = -0.1x + C
- Step 4: y = Ce^(-0.1x) — exponential decay!
- Connect back: "This is the same form we saw in the hook!"
- Show the decaying curve (optional simple graph)
- Physical interpretation: half-life

### Scene 5: Example 2 — Newton's Law of Cooling (~2 min)
**Content budget:** Section divider, problem statement, equation setup, solution, interpretation
- Section divider "4 — Example: Newton's Cooling"
- Problem: A cup of coffee at 90°C in a room at 20°C
- dT/dt = -k(T - 20) where k > 0 is the cooling constant
- Step 1: Let u = T - 20, then du/dt = -ku (substitution trick)
- Step 2: du/u = -k dt
- Step 3: ln|u| = -kt + C → u = Ce^(-kt)
- Step 4: T = 20 + Ce^(-kt)
- Apply initial condition T(0) = 90 → C = 70
- Final: T(t) = 20 + 70e^(-kt)
- Physical interpretation: coffee approaches room temperature exponentially

### Scene 6: Summary + Preview (~1.5 min)
**Content budget:** Summary text, key takeaways, next video teaser, outro
- Separable equations: dy/dx = g(x)h(y) → separate → integrate → solve
- Key idea: algebraically separate the variables, then integrate both sides
- "Not every first-order ODE is separable — next time we'll learn about first-order LINEAR equations"
- play_outro()

## Key Formulas
- dy/dx = g(x)h(y) (separable form)
- dy/h(y) = g(x)dx (separated form)
- ∫ dy/h(y) = ∫ g(x)dx + C (integrated form)
- y = Ce^(kx) (exponential solution)
- T(t) = T_s + Ce^(-kt) (Newton's cooling)

## Animation Notes
- The "sliding variables" animation in Scene 3 is the signature visual — animate terms moving between sides of the equation
- Color-code: y-terms in PRIMARY, x-terms in SECONDARY, constants in ACCENT
- For the cooling example, show a temperature curve decaying toward the room temperature asymptote
- Keep the exponential decay graph simple (no complex axes, just the curve and labels)
- Each example follows the same 4-step structure — use consistent visual layout so students see the pattern
