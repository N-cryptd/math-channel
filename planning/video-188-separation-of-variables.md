# Video 188: Separation of Variables

**Playlist:** Partial Differential Equations (Videos 184-193)
**Class:** Video188_SeparationOfVariables
**Target Duration:** 12-15 minutes
**Level:** Graduate (builds on Videos 185-187, unifies the method)

## Relationship to Prior Videos
Videos 185-187 each used separation of variables in a specific context:
- Video 185: Heat equation - separation leading to exponential decay
- Video 186: Wave equation - separation leading to oscillation
- Video 187: Laplace's equation - separation on rectangles

This video steps back and presents the GENERAL method as a unified framework, connecting all three.

## Competitive Analysis
- See channel-analysis/improvements.md - PDE playlist analysis
- 3B1B DE3: "Solving the heat equation" (1.66M views) - touches separation conceptually but doesn't complete the derivation, no unified framework
- commutant PDE 13: Wave equation separation (342K views, blackboard, 2012) - rigorous but no animation
- Faculty of Khan: Heat PDE by Separation of Variables (151K views, whiteboard) - detailed derivation, no animation
- Steve Brunton: "PDE 101: Separation of Variables" (112K views, slides) - good breadth, no animation
- NO competitor covers separation as a unified framework across heat/wave/Laplace with animations

Our approach: Present the general recipe, show WHY it works, connect eigenvalue problems to Fourier series, demonstrate the superposition principle, and unify all three equations.

## Prerequisites
- Videos 185-187 (heat, wave, Laplace equations)
- Fourier Series (Videos 174-176)
- Linear Algebra (eigenvalues, eigenvectors)
- ODEs ( Videos 55-66)

## Scene Plan

### Scene 1: Hook - One Method, Three Equations (60s)
**Content budget:** 4 items
- Intro (play_intro)
- Title: "One Method to Solve Them All"
- We've seen separation of variables three times - now let's understand WHY it works
- Preview: the general recipe, when it applies, and what eigenvalues have to do with PDEs

### Scene 2: The General Idea (120s)
**Content budget:** 5 items
- Title: "The Separation Ansatz"
- Assume u(x_1, x_2, ...) = X_1(x_1) * X_2(x_2) * ...
- Substitute into PDE, divide by product to separate variables
- Each side must equal a constant (the separation constant)
- This reduces a PDE to a system of ODEs

### Scene 3: The Eigenvalue Problem (120s)
**Content budget:** 5 items
- Title: "The Eigenvalue Problem"
- Boundary conditions constrain the separation constant
- Only special values (eigenvalues) are allowed
- Each eigenvalue gives an eigenfunction (basis function)
- This is why we get DISCRETE solutions: Fourier sine series, cosine series, etc.

### Scene 4: Fourier Series Expansion (120s)
**Content budget:** 5 items
- Title: "Expanding in Eigenfunctions"
- The initial condition determines coefficients via inner products
- b_n = (2/L) integral f(x) sin(n*pi*x/L) dx
- This is a projection: decomposing the initial data into eigenfunction components
- Higher modes = higher frequency content

### Scene 5: The Superposition Principle (120s)
**Content budget:** 5 items
- Title: "Linearity and Superposition"
- PDEs are linear: if u_1 and u_2 solve it, so does a*u_1 + b*u_2
- Each eigenfunction * its temporal part = one solution mode
- The general solution = infinite sum of all modes
- This is why we can match ANY initial condition

### Scene 6: Heat vs Wave vs Laplace - The Same Framework (120s)
**Content budget:** 5 items
- Title: "Three Equations, One Structure"
- Table: Heat (decay: exp(-lambda*t)), Wave (oscillation: cos+sin), Laplace (no time)
- Same spatial problem: X'' + lambda X = 0
- Same eigenvalues: lambda_n = (n*pi/L)^2
- Only the temporal equation differs - the spatial structure is universal

### Scene 7: When Does Separation Work? (90s)
**Content budget:** 5 items
- Title: "When Can We Separate?"
- Works for: linear, homogeneous PDEs with separable boundary conditions
- Needs: geometry that matches coordinates (rectangles, disks, spheres)
- Fails for: nonlinear PDEs, irregular domains, mixed boundary conditions
- The Sturm-Liouville theory generalizes this (preview of next video)

### Scene 8: Summary and Outro (60s)
**Content budget:** 5 items
- Title: "Key Takeaways"
- Separation of variables: product ansatz -> system of ODEs
- Boundary conditions create eigenvalue problems
- Fourier series expands initial conditions in eigenfunctions
- Superposition builds general solutions from individual modes
- Next: Sturm-Liouville Theory

## Visual Design Notes
- Color: PRIMARY (blue) for the general method, SECONDARY (green) for heat, PRIMARY for wave, ACCENT (yellow) for Laplace
- Use a consistent color-coded table in Scene 6
- Show the eigenfunctions as animated basis functions
- Animate the eigenvalue spectrum as discrete points on a number line
- Show superposition: overlay individual modes building up the full solution
