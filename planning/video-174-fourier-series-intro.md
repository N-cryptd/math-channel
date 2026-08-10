# Video 174: Introduction to Fourier Series

**Playlist:** Fourier Analysis (Videos 174-183)
**Level:** Graduate (L5)
**Estimated Duration:** 15 min
**Class:** Video174_FourierSeriesIntro
**Script:** scripts/graduate/video-174-fourier-series-intro.py

---

## Competitive Analysis Summary

Key competitor videos:
- 3B1B "But what is the Fourier Transform?" (12.3M views) — winding machine metaphor
- Reducible "The FFT" (2.2M views) — algorithm-focused, discovery narrative
- Steve Brunton Fourier content (20-100K each) — whiteboard, application-driven
- Mathologer "Fourier transforms... the movie!" (800K) — Euler formula connection

**Market gap:** No animated Fourier Analysis playlist (series) exists. 3B1B has one brilliant standalone video, Brunton has lectures, but nobody does a systematic animated series.

**Our unique angle:** Connect Fourier Series to Hilbert space theory from our Functional Analysis playlist. Fourier series = orthogonal decomposition in L². This is genuinely different from every competitor.

**What to AVOID:** The winding machine metaphor (too associated with 3B1B). Instead, use projection onto orthogonal basis functions.

---

## Scene Plan (8 scenes)

### Scene 1: Hook — From Hilbert Spaces to Sound (90s)
**Content budget:** Title + 3 bullet points
- Start with channel intro/outro branding
- Motivation: "You learned about Hilbert spaces and orthonormal bases. What if the most important orthonormal basis in all of mathematics is made of sine and cosine functions?"
- Three key ideas teased:
  1. Any function can be decomposed into sines and cosines
  2. The coefficients come from inner products (projections)
  3. This connects to heat flow, signal processing, quantum mechanics

### Scene 2: The Square Wave Challenge (90s)
**Content budget:** Title + visual square wave + question
- Show a square wave (periodic function)
- Ask: "Can we build this from smooth sine waves?"
- Show first few terms: sin(x) approximation
- Demonstrate partial sum visually — already looks close!
- This is the hook that 3B1B and most channels use too — we keep it brief

### Scene 3: The Formal Setup (120s)
**Content budget:** Title + definition + period/frequency labels
- Periodic functions: f(x + T) = f(x), fundamental period T
- Define the interval [-L, L] where L = T/2
- The question: find coefficients a₀, aₙ, bₙ such that:
  f(x) = a₀/2 + sum of [aₙ cos(nπx/L) + bₙ sin(nπx/L)]
- Color-code: aₙ terms in PRIMARY (blue), bₙ terms in SECONDARY (green), a₀ in ACCENT (yellow)

### Scene 4: Orthogonal Projections — The Key Insight (120s)
**Content budget:** Title + inner product formula + projection interpretation
- THIS IS OUR UNIQUE CONTRIBUTION vs competitors
- In R²: projecting onto basis vectors gives dot product components
- In L²(-L,L): the inner product is the integral
- <f, g> = integral from -L to L of f(x)g(x) dx
- The sine and cosine functions form an ORTHONORMAL basis for L²
- Each coefficient IS an orthogonal projection:
  aₙ = (1/L) * integral f(x)cos(nπx/L) dx
  bₙ = (1/L) * integral f(x)sin(nπx/L) dx
- Visual: show the projection formula, highlight the parallel to R²

### Scene 5: Computing a Fourier Series — Worked Example (150s)
**Content budget:** Title + square wave + computed coefficients + partial sums
- Work through the square wave example:
  f(x) = {1 for 0 < x < L, -1 for -L < x < 0}
- Compute bₙ = (2/nπ)(1 - cos(nπ)) — only odd terms survive!
- Show: f(x) ≈ (4/π)[sin(x) + sin(3x)/3 + sin(5x)/5 + ...]
- Visual: animate partial sums converging to square wave
- Label terms with colors matching the formula

### Scene 6: Convergence — What Does "Equals" Mean? (120s)
**Content budget:** Title + convergence types list + key theorem
- Three levels of convergence:
  1. Pointwise convergence (works at most points)
  2. Uniform convergence (works everywhere, for smooth enough f)
  3. L² convergence (works for ALL square-integrable f)
- Key theorem: For f in L²(-L,L), the Fourier series converges in L²
- Preview: convergence will be a whole video (Video 175)
- Mention: Parseval's theorem — energy in function = energy in coefficients

### Scene 7: Why Fourier? Applications (90s)
**Content budget:** Title + 3-4 application bullets
- Heat equation: Fourier's original motivation (1810s)
- Signal processing: decomposing signals into frequency components
- Quantum mechanics: momentum representation via Fourier transform
- Image compression (JPEG uses DCT — discrete cosine transform)
- Each gets one line, color-coded

### Scene 8: Summary and Preview (60s)
**Content budget:** Title + 4 key takeaways + outro
- Key takeaways:
  1. Fourier series = orthogonal decomposition in L²
  2. Coefficients come from inner product projections
  3. Convergence depends on which topology you use
  4. Applications span physics, engineering, and pure math
- Preview next video: "Convergence of Fourier Series — pointwise, uniform, L²"
- Channel outro

---

## Visual Design Notes
- **Color coding throughout:**
  - PRIMARY (#5BC0EB) = cosine terms, aₙ coefficients
  - SECONDARY (#7BC950) = sine terms, bₙ coefficients
  - ACCENT (#FFD166) = the constant term a₀
  - RED (#EF476F) = convergence issues, Gibbs phenomenon
- **Signature visual:** Animated partial sums building up to approximate a function, showing the orthogonal projection metaphor
- **No epicycle/winding machine** — our differentiator is the Hilbert space connection

## Dependencies
- Prerequisites: Functional Analysis playlist (especially Video 164 — Inner Product Spaces, Video 165 — Hilbert Spaces)
- Next video: Video 175 — Convergence of Fourier Series
