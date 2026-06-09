# Video 55: What is a Differential Equation?

## Overview
- **Playlist:** Ordinary Differential Equations
- **Duration target:** 10-12 minutes
- **Class name:** `Video55_WhatIsADifferentialEquation`
- **Script file:** `scripts/undergraduate/video-55-what-is-a-differential-equation.py`

## Competitive Analysis Reference
See `channel-analysis/improvements.md` entry for 2026-06-09 (Video 55).
Key decisions:
- Hook with population growth example (adopting 3B1B's physical motivation + Zach Star's application-first framing)
- Slope field visualization as the central visual metaphor (3B1B's signature technique)
- Classification definitions after motivation, not before (avoiding Khan Academy's dry approach)

## Scene Plan

### Scene 1: Hook — Population Growth (~2 min)
**Content budget (max 5 items):** Title, population number text, growth equation, rate arrow, question text
- Start with play_intro()
- "Imagine you're tracking a population of bacteria..."
- Show N(t) = population at time t
- Key question: "What is dN/dt?" — the rate of change
- Introduce the idea: the rate depends on the current population
- dN/dt = rN — our first differential equation!

### Scene 2: Definition — What is a DE? (~1.5 min)
**Content budget:** Section divider, definition text, ODE vs PDE comparison, key notation
- Section divider "1 — Definition"
- Formal definition: equation involving derivatives of an unknown function
- ODE: derivatives with respect to ONE variable
- PDE: partial derivatives with respect to MULTIPLE variables (teaser only)
- Notation: y', dy/dx, y'' etc.
- The unknown is the FUNCTION y(x), not a number

### Scene 3: Classification — Order and Linearity (~2 min)
**Content budget:** Section divider, order definition, examples (1st/2nd order), linearity definition
- Section divider "2 — Classification"
- **Order:** highest derivative present
  - 1st order: dy/dx = f(x,y)
  - 2nd order: d²y/dx² = f(x,y,dy/dx)
  - Show concrete examples
- **Linearity:** coefficients of y and its derivatives are constants or functions of x only
  - Linear: d²y/dx² + 3 dy/dx + 2y = sin(x)
  - Nonlinear: dy/dx = y² (the y² makes it nonlinear)
- Progressive reveal of examples

### Scene 4: Visual — Slope Fields (~2.5 min)
**Content budget:** Section divider, slope field axes, slope segments, solution curve overlay, label text
- Section divider "3 — Slope Fields"
- A slope field is a visual representation of a 1st-order ODE
- At each point (x,y), draw a short line with slope = f(x,y)
- Show dy/dx = x (simple parabola example)
- Draw the slope field, then trace a solution curve through it
- Key insight: the DE defines a "terrain" — solutions are paths through that terrain
- Show that different starting points give different curves

### Scene 5: Physical Examples — Why DEs Matter (~2 min)
**Content budget:** Section divider, physics example 1 (falling), physics example 2 (spring), application text
- Section divider "4 — Real-World DEs"
- Falling object: d²y/dt² = -g (Newton's 2nd law)
- Spring-mass: m d²x/dt² + kx = 0 (Hooke's law)
- Population: dP/dt = rP(1 - P/K) (logistic growth)
- Brief: these are all ODEs — same concept, different applications

### Scene 6: Course Preview + Summary (~1.5 min)
**Content budget:** Summary text, course roadmap items, outro
- "In this course we'll learn:"
  - Separable equations (Video 56)
  - First-order linear (Video 57)
  - Second-order with constant coefficients (Video 59)
  - Laplace transforms (Video 60)
  - Systems and phase portraits (Video 61-62)
- Recap: DEs describe HOW things change, not just what they are
- play_outro()

## Key Formulas
- dN/dt = rN (exponential growth)
- dy/dx = f(x,y) (general 1st-order ODE)
- d²y/dx² + 3 dy/dx + 2y = sin(x) (linear 2nd-order)
- dy/dx = y² (nonlinear 1st-order)
- d²y/dt² = -g (free fall)
- m d²x/dt² + kx = 0 (spring)
- dP/dt = rP(1 - P/K) (logistic)

## Animation Notes
- Slope field is the star visual — use VMobject line segments, not Arrow objects
- Color-code: solution curves in PRIMARY, slope segments in DIM
- For the spring example, can optionally show a simple oscillation (but keep it brief)
- Population hook: use simple number text animations (500 → 1000 → 2000...)
