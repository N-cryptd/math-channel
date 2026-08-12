# Video 190: Green's Functions

**Playlist:** Partial Differential Equations (Videos 184-193)
**Class:** Video190_GreensFunctions
**Target Duration:** 15 minutes
**Level:** Graduate (builds on Videos 185-189, connects to Fourier Analysis)

## Relationship to Prior Videos
Video 189 (Sturm-Liouville Theory) showed that every PDE solved by separation of variables reduces to an eigenvalue problem with orthogonal eigenfunctions and completeness. But separation only works on specific domains with specific boundary conditions. Green's functions give us a more general and powerful approach: they solve the PDE for ANY source term (not just the initial condition), work on complex geometries via the method of images, and connect directly to Fourier analysis through convolution.

## Competitive Analysis
- See channel-analysis/improvements.md - Green's Functions analysis entry
- Mathemaniac: "Green's functions: the genius way to solve DEs" (755K views, 276K subs) -- best Green's functions video on YouTube, uses 3B1B-style visuals, starts from linear operators and Dirac delta, focuses on ODE context (harmonic oscillator). Strength: beautiful visual storytelling, "impulse response" motivation is excellent. Weakness: only covers ODEs, no PDE-specific content, no method of images, no heat kernel, no convolution formula. Thumbnail: black bg with white text and colored spheres with math symbols. Rating: 8/10.
- Faculty of Khan: "Introducing Green's Functions for PDEs" (156K views, 104K subs) -- whiteboard lecture, most comprehensive PDE coverage on YouTube. Covers the formal definition for Poisson's equation, derives properties, shows 1D example. Strength: rigorous treatment of PDE case, good for math students. Weakness: no animations, pure whiteboard, slow pace, no visual intuition for what Green's functions "look like." Thumbnail: blurred math equations with title text overlay. Rating: 7/10.
- Andrew Dotson: "Intuition for Green's Functions" (96K views, 249K subs) -- whiteboard, physics-focused (electrostatics motivation). Strength: physical intuition (point charge -> potential field) is excellent for building understanding. Weakness: whiteboard only, physics-specific, no connection to PDE theory or Fourier analysis. Thumbnail: Andrew writing on whiteboard with "Daily Physics Upload" text. Rating: 5/10.
- Prof. Dave Explains: "The Diffusion Equation Part 3: Green's Functions" (19K views, 4.38M subs) -- part of a series on diffusion equation. Strength: connects to heat equation specifically. Weakness: very recent, low views, no animations, surface-level treatment. Thumbnail: bell curve with colored time overlays.

Our approach: Start with the impulse response intuition (following Mathemaniac's excellent hook), define Green's function formally for PDEs, show the heat kernel as a concrete example with animated Gaussian spreading, demonstrate the convolution formula as the general solution, cover the method of images with animated reflections, and close with the Fourier connection. Nobody animates ALL of these for PDE Green's functions.

## Prerequisites
- Video 189 (Sturm-Liouville Theory)
- Video 185 (The Heat Equation)
- Videos 174-179 (Fourier Analysis: transform, convolution theorem)
- Video 170 (Inner Product Spaces / Functional Analysis basics)

## Scene Plan

### Scene 1: Hook - The Impulse Response (60s)
**Content budget:** 4 items
- Intro (play_intro)
- Title: "What If You Could Solve PDEs for ANY Source?"
- Physical analogy: tap a drum at one point (impulse), the resulting vibration pattern IS the Green's function
- Key insight: if you know the response to a point source, convolution with the actual source gives the full solution
- Green's function = the "DNA" of the PDE operator

### Scene 2: Formal Definition (120s)
**Content budget:** 5 items
- Title: "The Green's Function: Formal Definition"
- For a linear differential operator L, the Green's function G(x, xi) satisfies: L[G] = delta(x - xi)
- The delta function: infinite at xi, zero everywhere else, integrates to 1
- Think of delta as the "idealized point source"
- The Green's function encodes the response of L to a unit impulse at point xi
- Key properties: symmetry (for self-adjoint L), G -> 0 as |x| -> infinity

### Scene 3: The Heat Kernel (120s)
**Content budget:** 5 items
- Title: "The Heat Kernel: Green's Function for the Heat Equation"
- For the heat equation u_t = alpha * u_xx, the Green's function is the Gaussian: G(x,t) = 1/sqrt(4*pi*alpha*t) * exp(-x^2 / (4*alpha*t))
- Animated: a Gaussian that starts narrow (impulse) and spreads over time
- At t -> 0, this becomes a delta function (the point source)
- The heat kernel IS the fundamental solution: it solves the heat equation for a point source at x=0, t=0
- Connection: this is also called the "diffusion kernel" or "fundamental solution"

### Scene 4: Convolution Representation (120s)
**Content budget:** 5 items
- Title: "The Solution Formula: Convolution"
- General solution: u(x) = integral G(x, xi) * f(xi) d(xi)
- Physical meaning: sum up (integrate) the contributions from every source point
- Each source point xi contributes G(x, xi) to the field at point x
- For the heat equation with initial condition u(x,0) = f(x): u(x,t) = integral G(x-xi, t) * f(xi) d(xi)
- This is why Fourier analysis connects: convolution in physical space = multiplication in frequency space

### Scene 5: Method of Images (120s)
**Content budget:** 5 items
- Title: "Method of Images: Geometry Meets Green's Functions"
- Problem: what if we have a boundary condition (e.g., u = 0 at x = 0)?
- The free-space Green's function doesn't satisfy boundary conditions
- Method of images: place a "mirror image" source to cancel at the boundary
- For the half-line [0, infinity) with Dirichlet BC: G_D(x, xi) = G_free(x, xi) - G_free(x, -xi)
- Animated: show the positive source and negative mirror source, their sum cancels at x=0
- This trick works for heat, wave, and Laplace equations

### Scene 6: Connection to Fourier Analysis (120s)
**Content budget:** 5 items
- Title: "Green's Functions and the Fourier Transform"
- Take the PDE L[u] = f, apply Fourier transform: L_hat(u_hat) = f_hat
- The Green's function in Fourier space: G_hat(k) = 1 / L_hat(k)
- The Fourier representation: G(x) = integral e^{ikx} / L_hat(k) dk / (2*pi)
- This is often the EASIEST way to find Green's functions
- Example: for -u_xx = f, we get G_hat = 1/k^2, giving us the Green's function explicitly
- Connection to Video 179 (Convolution Theorem): convolution = multiplication under FT

### Scene 7: Summary and Outro (60s)
**Content budget:** 4 items
- Title: "Key Takeaways"
- Green's function = impulse response: solves L[G] = delta
- The general solution is convolution with G
- Heat kernel = Gaussian that spreads from a point source
- Method of images handles boundaries by mirror sources
- Fourier transform finds G in frequency space
- Next: Well-Posed Problems and PDE Theory (Video 191)

## Visual Design Notes
- Color: ACCENT (gold/yellow) as the primary scene color -- Green's functions are the "golden key" to solving PDEs
- Animate delta functions as tall narrow spikes that approach infinity
- Heat kernel: animated Gaussian spreading from a point, with color gradient from hot (red) to cool (blue)
- Method of images: show positive source (ACCENT) and negative mirror source (RED) with their combined field
- Convolution: animate as "sliding and integrating" -- show G moving across the source f
- Fourier connection: show dual domains (physical space <-> frequency space) side by side
