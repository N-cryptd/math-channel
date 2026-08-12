# Video 192: Numerical Methods for PDEs

**Playlist:** Partial Differential Equations (Video 9 of 10)
**Level:** Graduate (Partial Differential Equations)
**Class:** Video192_NumericalMethodsPDEs
**Script:** scripts/graduate/video-192-numerical-methods-pdes.py

## Prerequisites
- Videos 184-191: PDE intro through Distributions & Weak Solutions
- Basic calculus: derivatives, integrals, Taylor series
- Linear algebra: matrix operations, eigenvalues

## Learning Objectives
1. Understand why most PDEs require numerical solutions
2. Learn the finite difference method: discretize derivatives on a grid
3. Understand stability (CFL condition) and convergence
4. See the finite element method: piecewise solutions on meshes
5. Compare methods: FDM for simple grids, FEM for complex geometry

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — Why Numerical? (~60s)
**Visual:** A beautiful analytical solution formula that suddenly shatters into a grid.
- Start with: "In this playlist, we have solved PDEs analytically. Separation of variables, Green's functions, Fourier transforms. These are elegant and powerful. But the vast majority of PDEs in engineering and science have no closed-form solution."
- Show the Laplace equation on an irregular domain — cannot solve analytically.
- Key message: Numerical methods turn PDEs into algebra problems a computer can solve.
- Transition to intro.
**Content:** "Every PDE we have studied so far had a clean analytical solution. We found eigenfunctions, computed Fourier coefficients, wrote closed-form expressions. But this is the exception, not the rule. In practice, PDEs live on complicated domains with complicated coefficients and complicated boundary conditions. The real world is not a rectangle. Numerical methods let us approximate solutions that we cannot compute exactly, and for most problems, they are the only option."
**Elements:** Analytical formula (beautiful), irregular domain shape, grid overlay, "No closed-form solution" label
**Content budget:** 4 elements max

### Scene 2: Intro + Section Divider (~20s)
**Visual:** Channel intro animation, then section divider.
- play_intro("Numerical Methods for PDEs", "Partial Differential Equations")
- Section divider: "1 — Finite Difference Method"
**Elements:** Intro animation, section divider
**Content budget:** Animated sequence

### Scene 3: Finite Differences — The Core Idea (~90s)
**Visual:** A function curve on a grid, showing how derivatives become differences.
- The central idea: replace derivatives with differences on a discrete grid.
- Show Taylor expansion: u(x+h) ≈ u(x) + h·u'(x) + (h²/2)·u''(x) + ...
- From this: u'(x) ≈ [u(x+h) - u(x-h)] / (2h) — the central difference formula.
- For second derivatives: u''(x) ≈ [u(x+h) - 2u(x) + u(x-h)] / h²
- Visualize: three grid points connected, the parabola they approximate.
**Content:** "The finite difference method is the most intuitive numerical approach. We lay down a uniform grid of points and replace every derivative with a difference between neighboring values. From Taylor's theorem, the first derivative at a point is approximately the difference of its neighbors divided by the grid spacing, using the central difference formula. The second derivative becomes a three-point stencil: the value at a point minus twice the center plus the value on the other side, all divided by h squared. This turns every PDE into a system of algebraic equations."
**Elements:** Grid visualization, Taylor expansion formula, central difference formula, second derivative stencil, grid points with connections
**Content budget:** Progressive reveal, max 5

### Scene 4: FDM Applied to the Heat Equation (~90s)
**Visual:** 1D heat equation discretized on a grid, showing the stencil marching in time.
- Start with u_t = α u_{xx}.
- Discretize in space: x_i = i·h, in time: t_n = n·k.
- Time derivative: forward difference: [u_i^{n+1} - u_i^n] / k.
- Space derivative: central difference: [u_{i-1}^n - 2u_i^n + u_{i+1}^n] / h².
- Combined: u_i^{n+1} = u_i^n + (αk/h²)(u_{i-1}^n - 2u_i^n + u_{i+1}^n).
- This is the FTCS scheme (Forward Time, Central Space).
- Visual: grid with time marching upward, stencil highlighting 3 spatial points.
**Content:** "Let us apply this to the heat equation. We discretize space with spacing h and time with spacing k. Using forward difference in time and central difference in space, we get the FTCS scheme. Each new time step is computed from three values at the current time step. This is explicit: you can compute each new value directly from old values. The parameter alpha times k over h squared is the key dimensionless number. If it is too large, the scheme blows up."
**Elements:** Heat equation, discretized grid, FTCS formula, stencil visual, stability note
**Content budget:** Progressive reveal, max 5

### Scene 5: Stability and the CFL Condition (~80s)
**Visual:** Stable vs unstable numerical solutions side by side.
- The FTCS scheme is conditionally stable.
- Stability condition: αk/h² ≤ 1/2 (the CFL condition).
- Show what happens when violated: oscillations grow exponentially.
- Show stable case: smooth convergence to true solution.
- Key insight: there is a fundamental trade-off between accuracy and computational cost.
**Content:** "Not every finite difference scheme works. The FTCS scheme for the heat equation is only stable when alpha k over h squared is at most one half. If you violate this, the numerical solution oscillates wildly and grows without bound — complete garbage. This is the CFL condition, named after Courant, Friedrichs, and Lewy. It tells you the relationship between your time step and space step. Smaller time steps are more stable but more expensive. There is always a trade-off."
**Elements:** CFL condition formula, stable solution visual, unstable solution visual, trade-off label
**Content budget:** 4 elements, two-column layout

### Scene 6: Section Divider — Finite Element Method (~5s)
**Visual:** Section divider "2 — Finite Element Method"
- Section divider animation
**Elements:** Section divider
**Content budget:** Animated sequence

### Scene 7: The Finite Element Method — Overview (~90s)
**Visual:** A complex domain divided into triangular elements.
- FEM: divide the domain into elements (triangles, quadrilaterals).
- Approximate the solution as a sum of basis functions, one per node.
- u(x) ≈ Σ u_j · φ_j(x), where φ_j are piecewise polynomial "hat functions".
- Multiply the PDE by a test function and integrate — the weak form (connects to Video 191!).
- This produces a linear system Ku = f, where K is the stiffness matrix.
- Key advantage: handles complex geometry naturally.
**Content:** "The finite element method takes a different approach. Instead of a regular grid, you divide the domain into elements: triangles and quadrilaterals that conform to any shape. The solution is approximated as a weighted sum of basis functions — the famous hat functions that are piecewise linear and peak at one node. This connects directly to the weak solutions we studied in the last video. You multiply the PDE by a test function, integrate over the domain, and obtain a linear system. The matrix is called the stiffness matrix. FEM handles complex geometry, mixed boundary conditions, and material heterogeneity naturally."
**Elements:** Mesh of triangles, hat function visual, weak form connection, Ku=f equation, geometry advantage label
**Content budget:** Progressive reveal, max 5

### Scene 8: Summary and Outro (~60s)
**Visual:** Side-by-side comparison of FDM vs FEM, then outro.
- Compare FDM and FEM:
  - FDM: simple, regular grids, easy to implement
  - FEM: flexible geometry, rigorous mathematical framework
  - Both: turn PDEs into linear algebra problems
- Key takeaways:
  1. Most PDEs require numerical methods
  2. Finite differences: derivatives become differences on a grid
  3. Stability matters: CFL condition for explicit schemes
  4. Finite elements: weak form + piecewise approximation
  5. Both reduce PDEs to systems of equations
- Point to Video 193: the PDE summary tying everything together.
**Content:** "Finite differences and finite elements are the two pillars of numerical PDE solving. Finite differences are simpler and faster to implement on regular grids. Finite elements are more flexible and mathematically rigorous, handling any geometry. Both methods turn calculus into algebra: the computer solves a matrix equation. The key lesson is that numerical methods make PDEs practical for real-world problems. In the next video, we summarize the entire PDE playlist and chart the path forward."
**Elements:** FDM vs FEM comparison, 5 takeaway items, next video teaser
**Content budget:** Progressive reveal, max 5
