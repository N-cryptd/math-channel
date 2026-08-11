# Video 176: Fourier Series Properties

**Playlist:** Fourier Analysis (Videos 174-183)
**Level:** Graduate (L5)
**Estimated Duration:** 15 min
**Class:** Video176_FourierSeriesProperties
**Script:** scripts/graduate/video-176-fourier-series-properties.py

---

## Competitive Analysis Summary

Key competitor videos:
- Engineering Funda "Properties of Fourier Series Explained" (dP10vLm3hNM, 7.8K views, Feb 2025) — Covers linearity, time/frequency shifting, scaling, symmetry. Slide-based signal processing perspective. Engineering-focused, not rigorous math. No animations.
- FEMA ACADEMY "Linearity Property of Continuous Time Fourier Series" (bJZyNaRF8g0, 2K views, 2017) — Very narrow: only linearity, low production quality.
- 3B1B Fourier Transform (12.3M views) — Visual masterpiece but focuses on the transform, not series properties. Does not cover linearity of series, differentiation, or Parseval.
- Dr. Peyam Fourier series content (~10-30K views each) — Whiteboard theorem-proof style, covers individual properties across multiple videos but no unified animated treatment.
- Michael Penn Fourier content (~20-50K views) — Chalkboard style, computation-focused. Covers Parseval's theorem separately.

**Market gap:** No animated Manim video provides a unified, visually-driven treatment of Fourier series properties at the graduate level. Existing content either (a) treats properties individually in whiteboard format, or (b) takes an engineering/signal-processing approach without mathematical rigor. Nobody combines all four major properties — linearity, differentiation/integration, even/odd extensions, and Parseval's identity — into one cohesive, animated video with the Hilbert space perspective.

**Our unique angle:** This video is the natural follow-up to Videos 174-175. Having established Fourier series as an orthogonal decomposition in L2 and studied convergence, we now explore the algebraic and analytic structure of this decomposition. We use the Hilbert space framework from Functional Analysis to give unified proofs — linearity follows from linearity of the inner product, Parseval from completeness of the orthonormal basis. Differentiation and integration become "coefficient-level" operations with geometric meaning.

**What to AVOID:**
- Don't just list properties as formulas without motivation — show WHY each property matters
- Don't treat differentiation of series as a mere "differentiate term by term" without addressing convergence conditions
- Don't skip the even/odd extension motivation — this is how we apply Fourier series to functions defined on half-intervals, critical for PDE boundary value problems
- Don't prove Parseval's identity abstractly — connect it to the Pythagorean theorem in infinite dimensions

---

## Scene Plan (8 scenes)

### Scene 1: Hook — The Rules of the Game (75s)
**Content budget:** Title + 3 "rules" preview + connection to previous videos
- Recall: Video 174 built Fourier series from orthogonal projections; Video 175 studied convergence
- Now we ask: "What can we DO with a Fourier series? What algebraic rules does it follow?"
- Preview the four properties we'll cover:
  1. Linearity — series of a sum is the sum of the series
  2. Differentiation & Integration — series of derivatives, term by term
  3. Even & Odd Extensions — extending functions to full periods
  4. Parseval's Identity — energy conservation in the frequency domain
- Color-code each property: Linearity=PRIMARY, Diff/Int=SECONDARY, Extensions=ACCENT, Parseval=RED
- Connect to big picture: these properties are what make Fourier series a powerful computational tool, not just a theoretical decomposition

### Scene 2: Linearity — The Easiest Property (150s)
**Content budget:** Title + 2 function definitions + proof sketch + formula
- Statement: If f and g have Fourier series, then (af + bg) has Fourier series with coefficients (a * coeff_f + b * coeff_g)
- Show with formulas:
  - f(x) has coefficients {a_n^f, b_n^f}
  - g(x) has coefficients {a_n^g, b_n^g}
  - (af+bg)(x) has coefficients {a*a_n^f + b*a_n^g, a*b_n^f + b*b_n^g}
- PROOF (animated): The Fourier coefficient formula involves an integral, and integration is linear
  - a_n^{af+bg} = (1/pi) * integral[(af+bg) cos(nx)] dx
  - = a * (1/pi) * integral[f cos(nx)] dx + b * (1/pi) * integral[g cos(nx)] dx
  - = a * a_n^f + b * a_n^g
- Color-code: the sum in PRIMARY, the coefficients in ACCENT
- Emphasize: this follows directly from linearity of the integral — and in Hilbert space language, from linearity of the inner product
- This property is what allows us to decompose complex signals into simpler parts, solve for each part separately, then recombine

### Scene 3: Differentiation of Fourier Series (150s)
**Content budget:** Title + derivative formula + convergence condition + visual
- Statement: If f is continuous AND f' is piecewise smooth, then we can differentiate the Fourier series term by term
- Formula: f'(x) = sum_{n=1}^{inf} (-n * a_n * sin(nx) + n * b_n * cos(nx))
- Show how the coefficients transform: multiplying by n swaps cos<->sin and scales
- KEY WARNING: This only works when f' itself has a valid Fourier series (sufficient smoothness)
- Counterexample: the square wave — differentiating gives delta functions at the jumps, the differentiated series diverges at those points
- Visual: show the derivative coefficient relationship as a transformation diagram:
  - Original: a_n cos(nx) + b_n sin(nx)
  - Derivative: -n*a_n sin(nx) + n*b_n cos(nx)
  - The factor n amplifies high frequencies — differentiation is a high-pass filter!
- Connect to signal processing: this is why differentiation amplifies noise

### Scene 4: Integration of Fourier Series (120s)
**Content budget:** Title + integral formula + constant term + contrast with differentiation
- Statement: We can ALWAYS integrate a Fourier series term by term — no extra smoothness needed!
- Formula: integral of f(x) dx = a_0*x/2 + sum_{n=1}^{inf} (a_n * sin(nx)/n - b_n * cos(nx)/n + C)
- Key insight: dividing by n instead of multiplying — integration is a low-pass filter
- This is the opposite of differentiation: integration always converges (smooths things out)
- The constant of integration C is the only subtlety — it's determined by boundary conditions
- Visual: contrast differentiation (multiply by n, amplifies high freq) vs integration (divide by n, attenuates high freq) side by side
- Connect to PDEs: the heat equation uses integration (smoothing), the wave equation uses both

### Scene 5: Section Divider — From Algebra to Extensions (30s)
**Content budget:** Section divider "Part 2: Extensions & Energy"
- Brief transition: "Now that we understand how to manipulate Fourier series algebraically, let's see how to apply them to functions that aren't naturally periodic."

### Scene 6: Even and Odd Extensions (180s)
**Content budget:** Title + 2 extension visuals + half-range formulas
- Motivation: We often need Fourier series on [0, L] only (half interval), e.g., boundary value problems
- Two choices: extend the function to [-L, L] as even or as odd
- EVEN extension: f_even(x) = f(|x|) on [-L, L]
  - Only cosine terms survive (all b_n = 0)
  - Called the "Fourier cosine series" or "half-range cosine expansion"
  - Formula: a_n = (2/L) * integral_0^L f(x) cos(n*pi*x/L) dx
- ODD extension: f_odd(x) = sign(x) * f(|x|) on [-L, L]
  - Only sine terms survive (all a_n = 0, including a_0)
  - Called the "Fourier sine series" or "half-range sine expansion"
  - Formula: b_n = (2/L) * integral_0^L f(x) sin(n*pi*x/L) dx
- Visual: show a function on [0, L] being mirrored — one side as cosine (smooth), other as sine (odd/antisymmetric)
- Color-code: even extension = SECONDARY (smooth, green), odd extension = ACCENT (sharp, yellow)
- KEY APPLICATION: PDE boundary conditions — Dirichlet conditions use sine series (zero at boundaries), Neumann conditions use cosine series (zero derivative at boundaries)
- Emphasize: the SAME function can have different Fourier expansions depending on how we extend it — the series converges to different functions on (-L, 0)

### Scene 7: Parseval's Identity — Energy Conservation (150s)
**Content budget:** Title + Parseval formula + energy interpretation + connection to Pythagorean theorem
- Statement: The L2 norm of f equals the L2 norm of its Fourier coefficients
- Formula: (1/pi) * integral_{-pi}^{pi} |f(x)|^2 dx = (a_0^2)/2 + sum_{n=1}^{inf} (a_n^2 + b_n^2)
- Or equivalently: ||f||_2^2 = sum of squared coefficients
- CONNECTION to Video 165 (Hilbert Spaces): This IS the Pythagorean theorem for infinite-dimensional spaces!
  - In R^n: ||v||^2 = sum of (v . e_i)^2 for any orthonormal basis {e_i}
  - In L2: ||f||^2 = sum of |<f, e_n>|^2 for the trigonometric basis
  - The Fourier coefficients squared are the "energy" in each frequency
- Visual: animated bar chart showing energy in each harmonic — the bars add up to the total energy
- Applications:
  - Signal processing: total signal power = sum of power in each frequency component
  - Physics: total energy of a wave = sum of energy in each mode
  - Numerical analysis: how many terms to keep — truncate when residual energy is small
- Emphasize: Parseval tells us the Fourier series doesn't lose or gain energy — it's a perfect isometry

### Scene 8: Summary and Preview (60s)
**Content budget:** 4 key takeaways + outro
- Key takeaways:
  1. Fourier series are linear — sums and scalar multiples work component-by-component
  2. Differentiation multiplies coefficients by n (high-pass), integration divides by n (low-pass)
  3. Even/odd extensions let us use Fourier series on half intervals — critical for PDE boundary conditions
  4. Parseval's identity is the Pythagorean theorem in infinite dimensions — energy is conserved in the frequency domain
- Preview next video: "The Fourier Transform — extending Fourier series from periodic functions to all functions"
- Channel outro

---

## Visual Design Notes
- **Color coding throughout:**
  - PRIMARY (#5BC0EB) = Linearity, basis functions, formulas
  - SECONDARY (#7BC950) = Integration, even extensions, smooth operations
  - ACCENT (#FFD166) = Differentiation, odd extensions, transformation effects
  - RED (#EF476F) = Parseval's identity, energy, convergence failures
  - DIM (#6B6B8D) = Supporting text, warnings, conditions
- **Signature visual:** Side-by-side differentiation vs integration — showing how coefficients transform (multiply by n vs divide by n) with animated bar charts
- **Even/odd extension visual:** A function on [0, pi] being mirrored leftward — smooth cosine extension on one side, antisymmetric sine extension on the other
- **Parseval energy bars:** Animated bar chart showing squared coefficients adding up to total L2 norm, color-coded by frequency
- **Transformation diagram:** Arrows showing how differentiation/integration transforms (a_n, b_n) pairs

## Dependencies
- Prerequisites: Video 174 (Introduction to Fourier Series), Video 175 (Convergence of Fourier Series), Video 165 (Hilbert Spaces)
- Next video: Video 177 — The Fourier Transform
