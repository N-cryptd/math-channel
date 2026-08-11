# Video 182: Applications — Heat Equation

**Playlist:** Fourier Analysis (Videos 174-183)
**Level:** Graduate (L5)
**Estimated Duration:** 14 min
**Class:** Video182_HeatEquation
**Script:** scripts/graduate/video-182-heat-equation.py

---

## Scene Plan (8 scenes)

### Scene 1: Hook — PDEs Become Algebra (70s)
- Partial differential equations are the language of physics
- Fourier transform converts PDEs into ODEs (one less dimension!)
- The heat equation is the perfect first example
- "Where calculus fails, algebra succeeds"

### Scene 2: The Heat Equation (100s)
- u_t = α u_xx (heat equation on the real line)
- Initial condition: u(x, 0) = f(x)
- Physical meaning: rate of change proportional to curvature
- In Fourier space: û_t = -αω² û → û(ω, t) = û(ω, 0) e^{-αω²t}
- Solution by inverse transform!

### Scene 3: The Heat Kernel (Fundamental Solution) (120s)
- Start with delta initial condition: u(x, 0) = δ(x)
- û(ω, 0) = 1/√(2π)
- Solution: û(ω, t) = (1/√(2π)) e^{-αω²t}
- Inverse transform: u(x, t) = (1/√(4παt)) e^{-x²/(4αt)}
- This is a GAUSSIAN! Heat equation diffuses via Gaussian spreading
- As t→0: approaches delta. As t→∞: spreads out to zero.

### Scene 4: General Solution via Convolution (100s)
- For general f(x, 0) = f(x):
  u(x, t) = ∫ G(x - y, t) f(y) dy where G is heat kernel
- This is CONVOLUTION: u = G(·, t) * f
- The heat kernel is the Green's function for the heat equation
- Connection: convolution theorem explains why Fourier works so well

### Scene 5: Smoothing and Regularization (100s)
- The heat equation SMOOTHS functions
- Discontinuities are instantly smoothed out
- High-frequency components decay faster (e^{-αω²t})
- This is the Laplace operator as a low-pass filter!
- Applications: image denoising, anisotropic diffusion

### Scene 6: Fourier Method for PDEs (100s)
- General recipe:
  1. Transform the PDE (derivatives become multiplication)
  2. Solve the resulting ODE for û(ω, t)
  3. Inverse transform to get u(x, t)
- Works for: heat equation, wave equation, Laplace equation, Schrödinger
- Limitation: only for linear PDEs with constant coefficients (on R or T^n)

### Scene 7: Connection to Previous Topics (80s)
- Heat kernel is a Gaussian → connects to Video 177 (eigenfunction)
- Solution is convolution → connects to Video 179 (convolution theorem)
- Smoothing connects to Video 176 (integration = low-pass)
- Energy decay connects to Video 180 (Parseval)
- All Fourier analysis concepts converge here

### Scene 8: Summary and Preview (60s)
- 1. Heat equation in Fourier space: û_t = -αω²û
- 2. Heat kernel: Gaussian (1/√(4παt)) e^{-x²/(4αt)}
- 3. General solution: convolution with heat kernel
- 4. Heat equation smooths (high freq decay exponentially)
- 5. Fourier method: PDEs → ODEs → inverse transform
- Preview: Fourier Analysis Summary
- Outro
