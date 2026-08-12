# Video 184: What is a PDE?

**Playlist:** Partial Differential Equations (Videos 184–193)
**Class:** Video184_WhatIsAPDE
**Target Duration:** 10–14 minutes
**Level:** Undergraduate (follows Fourier Analysis, precedes Heat Equation)

## Competitive Analysis References
- See channel-analysis/improvements.md — PDE playlist analysis (Aug 2026)
- 3B1B DE2 covers heat equation intuition (3.2M views) but NO general PDE intro
- commutant has systematic PDE content (234K–342K views) but no animations (2011)
- Faculty of Khan covers PDE rigorously (whiteboard only)
- NO channel provides an animated intro to PDEs covering the general framework
- Our approach: physical motivation → general form → classification → canonical examples

## Prerequisites
- Calculus III (multivariable derivatives, gradients)
- Fourier Analysis (Videos 174–183) — especially the heat equation (Video 182)
- ODEs (Videos 55–66)

## Scene Plan

### Scene 1: Hook — The World is Governed by PDEs (90s)
**Content budget:** 5 items
- Intro animation (play_intro)
- Title: "The Equations That Describe Everything"
- Progressive reveal of real-world PDE examples:
  - Heat flows through a metal rod → heat equation
  - Ripples on a pond → wave equation
  - Gravitational potential around a planet → Laplace's equation
  - Quantum mechanics → Schrödinger equation
**Narration:** ~45 words (18s)

### Scene 2: What Makes It "Partial"? (60s)
**Content budget:** 4 items
- Title: "Ordinary vs Partial"
- ODE example: dy/dx = f(x,y) — one independent variable
- PDE example: ∂u/∂t = k ∂²u/∂x² — multiple independent variables
- Key distinction: multiple independent variables → partial derivatives
**Narration:** ~30 words (12s)

### Scene 3: The General Form (90s)
**Content budget:** 5 items
- Title: "General Form of a PDE"
- General PDE: F(x₁, ..., xₙ, u, ∂u/∂x₁, ..., ∂²u/∂x₁², ...) = 0
- Order: highest partial derivative present
- Linear vs nonlinear distinction
- Key examples with orders labeled
**Narration:** ~50 words (20s)

### Scene 4: The Three Canonical PDEs (120s)
**Content budget:** 5 items per sub-section (3 sub-sections)
- Section divider: "The Big Three"

#### 4a: Heat Equation
- ∂u/∂t = α ∇²u
- Physical meaning: rate of change ∝ curvature
- First-order in time, second-order in space

#### 4b: Wave Equation
- ∂²u/∂t² = c² ∇²u
- Physical meaning: acceleration ∝ curvature
- Second-order in both time and space

#### 4c: Laplace's Equation
- ∇²u = 0
- Equilibrium: no time dependence
- Solutions are "harmonic functions"
**Narration:** ~60 words (25s)

### Scene 5: Classification by Order and Linearity (90s)
**Content budget:** 5 items
- Title: "Classifying PDEs"
- Order: 1st, 2nd, 3rd...
- Linearity: linear (unknown appears to 1st power) vs nonlinear
- For 2nd-order linear PDEs: elliptic, parabolic, hyperbolic
- Connection to the big three: Laplace→elliptic, Heat→parabolic, Wave→hyperbolic
**Narration:** ~50 words (20s)

### Scene 6: Why Are PDEs Hard? (60s)
**Content budget:** 4 items
- Title: "The Challenge of PDEs"
- ODEs: one independent variable → well-understood theory
- PDEs: infinite-dimensional → much harder
- No general solution method (unlike ODEs)
- Each equation type needs its own toolkit
**Narration:** ~30 words (12s)

### Scene 7: Preview of the Playlist (60s)
**Content budget:** 5 items
- Title: "What's Coming Up"
- Roadmap items:
  - Heat equation → separation of variables
  - Wave equation → d'Alembert solution
  - Laplace's equation → boundary value problems
  - Advanced: Green's functions, distributions, numerical methods
**Narration:** ~30 words (12s)

### Scene 8: Summary and Outro (60s)
**Content budget:** 5 items
- Title: "Key Takeaways"
- Key points:
  - PDEs have multiple independent variables
  - Three canonical types: elliptic, parabolic, hyperbolic
  - Each needs specialized solution methods
- Outro (play_outro with next video: Heat Equation)
**Narration:** ~25 words (10s)

## Visual Design Notes
- Use ∂ symbol prominently (it's the signature of PDEs)
- Color code the three canonical equations consistently throughout playlist:
  - Heat equation → SECONDARY (green) — like warmth
  - Wave equation → PRIMARY (blue) — like water
  - Laplace's equation → ACCENT (gold) — like equilibrium
- Show the ∇² operator building from its definition
- For the hook scene, show animated icons (flame, wave, planet, atom) next to each equation

## Estimated Total Duration: ~10 minutes
