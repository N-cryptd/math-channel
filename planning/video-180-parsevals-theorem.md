# Video 180: Parseval's Theorem

**Playlist:** Fourier Analysis (Videos 174-183)
**Level:** Graduate (L5)
**Estimated Duration:** 14 min
**Class:** Video180_ParsevalsTheorem
**Script:** scripts/graduate/video-180-parsevals-theorem.py

---

## Competitive Analysis Summary

Key competitor videos:
- Dr. Trefor Bazett "Parseval's Identity, Fourier Series, and Solving this Classic Pi Formula" (WPeU34jndSw, 92.6K views, 611K subs) — Undergraduate-level, focuses on Fourier series Parseval identity to solve Basel problem (sum 1/n^2 = pi^2/6). Blackboard thumbnail with summation. Good narrative arc (Pi Day special), connects Parseval to a famous result. But limited to Fourier series, no FT extension, no autocorrelation, no applications.
- Steve Brunton "Parseval's Theorem" (ML0eYMyhqOs, 87.3K views, 546K subs) — Signal processing context, data-driven science focus. Dark blue thumbnail with Fourier series/transform equations. Covers energy conservation in truncated Fourier series. Practical but lecture-style, no animations.
- Mike, the Mathematician "The Plancherel Theorem" (pIpuHVJC2vc, 1.4K views, 25.7K subs) — Graduate-level, most rigorous competitor. Proves Plancherel as consequence of convolution theorem. Whiteboard-style. Low views but closest in content depth to what we need.
- Iain Explains "What is Power Spectral Density (PSD)?" (DoSLMEEo1Y0, 124.7K views, 96.5K subs) — Engineering-focused, explains PSD from intuitive and mathematical perspectives. Red thumbnail with speaker and graphs. Good Wiener-Khinchin connection but no animation, pure slides.

**Market gap:** No video provides a unified, animated, graduate-level treatment of Parseval's theorem that connects Plancherel → generalized Parseval → autocorrelation → Wiener-Khinchin → quantum mechanics. Every competitor covers one piece (series Parseval, or signal energy, or PSD) but nobody connects the full chain with Manim-quality visuals. Nobody animates the Fourier uncertainty principle derivation from Parseval. Nobody bridges signal processing and quantum mechanics in a single video through this theorem.

**Our unique angle:** Our video is the energy conservation payoff of the entire Fourier Analysis playlist. Building from Video 177 (Fourier Transform definition), Video 178 (Properties), and Video 179 (Convolution Theorem), we now show that Parseval is the deep unifying principle: the FT is unitary, so it preserves ALL geometric structure (norms, inner products, angles). We are the only channel showing: (1) the full Plancherel → Parseval → autocorrelation → Wiener-Khinchin chain with animations, (2) the uncertainty principle as a Parseval consequence, (3) quantum probability conservation as a direct application, (4) the connection between engineering PSD and mathematical correlation theory.

**What to AVOID:**
- Don't focus only on Fourier series version (following Trefor's approach) — we're at the FT level now
- Don't do only the statement without proof intuition (following Brunton)
- Don't be purely theoretical without applications (following Mike)
- Don't separate PSD from its mathematical foundation (following Iain)
- Don't skip the generalized Parseval — it's the key to everything

**Thumbnail analysis:**
- Trefor: Blackboard style, white/pink text, summation formula. Clean but academic. Rating: 6/10.
- Brunton: Dark blue swirl, chalkboard equations, clear title. Professional. Rating: 7/10.
- Iain: Red background, speaker photo, density graphs. Engaging but busy. Rating: 6/10.
- Our thumbnail should: Dark background (our BG=#1A1832), show the Plancherel formula large and centered in ACCENT, time-domain curve (left) and frequency-domain curve (right) connected by = sign, clean PRIMARY text "Parseval's Theorem" at top.

---

## Scene Plan (8 scenes)

### Scene 1: Hook — Energy in Two Domains (70s)
**Content budget:** Title + 3 preview items + theorem teaser
- Energy conservation is the deepest theme in Fourier analysis
- Parseval's theorem = precise statement of energy conservation
- "What you gain in localization you lose in smoothness, but total energy stays the same"
- Preview the journey: Plancherel → Parseval → correlation → Wiener-Khinchin → quantum
- Color-code: energy concepts in PRIMARY, applications in ACCENT

### Scene 2: Plancherel Theorem (120s)
**Content budget:** Title + formula box + 2 explanation items
- Statement: ||f||_2 = ||F-hat||_2
- Integral form: integral |f(x)|^2 dx = integral |F-hat(omega)|^2 domega
- Follows from unitarity of the Fourier transform
- "Time domain energy = frequency domain energy — they are exactly the same"
- Connect to Video 178's unitary operator discussion
- Following Brunton's practical framing but with our animated formula reveal
- Visual: formula in a PRIMARY-colored box, then items below

### Scene 3: Generalized Parseval Identity (120s)
**Content budget:** Section divider + title + formula box + 3 insight items
- For two functions: integral f(x) g-bar(x) dx = integral F-hat(omega) G-hat-bar(omega) domega
- Inner product preserved by unitary transform
- Special case g=f gives Plancherel
- This is the Parseval-Plancherel theorem
- "Analogy: rotation preserves dot products in R^n — the FT does the same in L^2"
- Color-code: formula in SECONDARY box, items in PRIMARY/SECONDARY/ACCENT

### Scene 4: Cross-Correlation and Autocorrelation (120s)
**Content budget:** Title + formula box + 3 insight items
- Cross-correlation: (f star g)(x) = integral f-bar(t) g(t+x) dt
- Related to convolution: f star g = f-bar * (-g)
- Fourier transform: F{f star g} = sqrt(2pi) F-hat-bar(omega) G-hat(omega)
- Autocorrelation: f star f — measures self-similarity at different lags
- Autocorrelation theorem: F{f star f} = sqrt(2pi) |F-hat(omega)|^2
- Following Brunton's signal processing framing with our animation style
- Color-code: cross-correlation in PRIMARY, autocorrelation in SECONDARY, power spectrum in ACCENT

### Scene 5: Wiener-Khinchin Theorem (100s)
**Content budget:** Section divider + title + 3 items
- For a wide-sense stationary random process, the power spectral density
  is the Fourier transform of the autocorrelation function
- S(omega) = integral R(tau) e^{-i omega tau} dtau where R(tau) = E[X(t) X-bar(t+tau)]
- This connects time-domain statistics to frequency-domain energy
- "Foundation of spectral analysis — every spectrum analyzer uses this theorem"
- Applications: signal analysis, noise characterization, filter design
- Bridging Iain's PSD explanation with rigorous mathematical foundation
- Color-code: S(omega) in PRIMARY, R(tau) in SECONDARY, applications in ACCENT

### Scene 6: Bandwidth and Duration (100s)
**Content budget:** Title + uncertainty formula box + 2 items
- Parseval connects bandwidth and duration through energy
- Essential bandwidth: range of frequencies containing X% of total energy
- RMS bandwidth and RMS duration: sigma_t * sigma_omega >= 1/2 (uncertainty)
- "The Gaussian achieves equality — it's the minimally uncertain function"
- Applications in communication theory (Shannon, Nyquist)
- Color-code: uncertainty formula in ACCENT box, items in PRIMARY/SECONDARY

### Scene 7: Quantum Mechanics Application (80s)
**Content budget:** Title + 3 items
- Position and momentum wave functions are Fourier pairs
- |psi(x)|^2 dx = probability in position, |psi-hat(p)|^2 dp = probability in momentum
- Parseval guarantees total probability = 1 in both representations
- "Heisenberg uncertainty follows from Fourier uncertainty — it's the same principle"
- Color-code: position in PRIMARY, momentum in SECONDARY, conservation in ACCENT

### Scene 8: Summary (60s)
**Content budget:** Title + 5 takeaway items + outro
- 1. Plancherel: L2 norm preserved
- 2. Parseval: inner product preserved
- 3. Cross-correlation <-> product of conjugate transforms
- 4. Wiener-Khinchin: power spectrum = transform of autocorrelation
- 5. Quantum: probability preserved between position and momentum
- Preview: Applications in Signal Processing
- Channel outro

---

## Visual Design Notes
- **Color coding throughout:**
  - PRIMARY (#5BC0EB) = Time domain, definitions, first function f
  - SECONDARY (#7BC950) = Frequency domain, results, second function g
  - ACCENT (#FFD166) = Key formulas, theorems, insights, uncertainty
  - RED (#EF476F) = Quantum mechanics application (deepest application)
  - DIM (#6B6B8D) = Supporting formulas, conditions, references to prior videos
- **Signature visual:** The dual-domain energy bar chart — show |f(x)|^2 as a filled curve on the left (time) and |F-hat(omega)|^2 as a filled curve on the right (frequency), with equal areas highlighted. This visual recurs throughout.
- **Plancherel visual:** The integral equation in a PRIMARY box, with "TIME" label on left integral and "FREQUENCY" label on right integral
- **Autocorrelation visual:** A signal sliding past itself with the product/integral shown
- **Uncertainty visual:** sigma_t * sigma_omega inequality with the >= sign pulsing
- **Quantum visual:** Two probability density curves (position and momentum) with "total = 1" beneath each

## Dependencies
- Prerequisites: Video 177 (The Fourier Transform), Video 178 (FT Properties), Video 179 (Convolution Theorem), Video 165 (Hilbert Spaces)
- Next video: Video 181 — Applications: Signal Processing
