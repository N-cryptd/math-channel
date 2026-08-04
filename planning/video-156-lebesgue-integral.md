# Video 156: The Lebesgue Integral

**Playlist:** Measure Theory (Video 7 of 12)
**Class:** Video156_LebesgueIntegral
**Script:** scripts/graduate/video-156-lebesgue-integral.py
**Est. Duration:** 15 min (~600s)
**Status:** PLAN

## Competitive Analysis Summary

Competitive analysis based on landscape knowledge — consistent with prior Measure Theory videos. Several channels cover the Lebesgue integral conceptually but few give a systematic animated treatment.

**Market Landscape:**
- **Abide By Reason** (652K views on Lebesgue integral) covers the horizontal slicing intuition beautifully but skips the formal definition via simple functions
- **vcubingx** (386K views) has the classic horizontal slicing animation showing Lebesgue vs Riemann
- **Faculty of Khan** covers Lebesgue integration lecture-style with proofs on screen
- **Dr. Peyam** does Lebesgue integral with measure theory rigor, whiteboard style
- **Michael Penn** has a video on the Lebesgue integral touching on integration of simple functions
- **3Blue1Brown** does not have a dedicated Lebesgue integral video (but his Riemann integral content sets expectations)
- No channel systematically builds the Lebesgue integral from simple functions through the approximation theorem in animated form

**Our approach:** We build the Lebesgue integral systematically:
1. Start with simple function integration (the foundation)
2. Use the approximation theorem from Video 155 to define the general integral
3. Show Lebesgue vs Riemann visually (vertical vs horizontal slicing)
4. Key properties: linearity, monotonicity, Chebyshev's inequality
5. The Dirichlet function as the star example — Lebesgue integrates it, Riemann can't

## Scene Plan

### Scene 1: Hook — "The Riemann Integral's Fatal Flaw" (~60s)
- "In Video 107 we studied the Riemann integral. It works beautifully for continuous functions. But it has a fatal flaw: it can't integrate the Dirichlet function."
- Visual: Dirichlet function graph (1 on Q, 0 on R\Q) with upper/lower Riemann sums always 1 and 0
- "The upper sum is always 1, the lower sum is always 0 — the Riemann integral doesn't exist. But intuitively, the rationals are negligible. We should get integral = 0."
- "The Lebesgue integral fixes this by slicing horizontally instead of vertically."
- Progressive reveal: Riemann problem statement, Dirichlet function, the horizontal slicing idea

### Scene 2: Simple Function Integration (~90s)
- "We defined simple functions in Video 155. Now we define their integral."
- Definition: If s = sum a_i * 1_{A_i} is a simple function (a_i >= 0, A_i measurable partition of X), then:
  integral(s) = sum a_i * mu(A_i)
- Visual: step function with horizontal bars at levels a_1, a_2, ..., a_n, with mu(A_i) as widths
- "Think of it as the area of the horizontal bars — level times the measure of the set at that level."
- "This is well-defined even though the representation isn't unique."
- Key properties of the simple integral:
  1. Linearity: integral(s + t) = integral(s) + integral(t)
  2. Monotonicity: s <= t implies integral(s) <= integral(t)
  3. integral(s) >= 0 when s >= 0

### Scene 3: Definition of the Lebesgue Integral (~90s)
- "For a general non-negative measurable function f, we use the approximation theorem from Video 155."
- Recall: s_n -> f pointwise with 0 <= s_1 <= s_2 <= ... <= f
- Definition: integral(f) = sup_n integral(s_n) = lim_{n->inf} integral(s_n)
- "This is the supremum of all simple function integrals that lie below f."
- Visual: staircase functions approaching a smooth curve from below, with their areas highlighted
- "The limit always exists (possibly infinity) because the integral(s_n) is an increasing sequence."
- Formula box: integral(f) d_mu = lim_{n->inf} integral(s_n) d_mu
- "This is defined for every non-negative measurable function f."

### Scene 4: General Functions (Signed & Extended) (~80s)
- "What about functions that take both positive and negative values?"
- Decompose: f = f^+ - f^- where f^+ = max(f, 0) and f^- = max(-f, 0)
- "Both f^+ and f^- are non-negative measurable functions."
- Definition: integral(f) = integral(f^+) - integral(f^-)
- "We say f is integrable if both integral(f^+) and integral(f^-) are finite."
- Visual: function split into positive part (above x-axis) and negative part (below x-axis)
- "The notation: L^1(X, mu) = { f : integral(|f|) < inf } — the space of integrable functions"
- Formula: integral(f) = integral(f^+) - integral(f^-)

### Scene 5: Lebesgue vs Riemann — The Star Example (~80s)
- "Let's see the Lebesgue integral in action on the function that broke Riemann."
- Dirichlet function: D(x) = 1 if x in Q, 0 if x in R\Q, on [0, 1]
- "D is measurable because Q is countable (measure zero)."
- Simple function approximation: s_n = D itself (it's already simple!)
- integral(D) = 1 * m(Q ∩ [0,1]) + 0 * m([0,1] \ Q) = 1 * 0 + 0 * 1 = 0
- "The Lebesgue integral of the Dirichlet function is 0 — exactly what our intuition demands."
- Visual: Riemann fails (upper=1, lower=0) vs Lebesgue succeeds (=0)
- "The Riemann integral partitions the domain. The Lebesgue integral partitions the RANGE."
- Visual: vertical slices (Riemann) vs horizontal slices (Lebesgue)

### Scene 6: Key Properties of the Lebesgue Integral (~80s)
- Progressive reveal of properties:
  1. Linearity: integral(af + bg) = a * integral(f) + b * integral(g)
  2. Monotonicity: f <= g implies integral(f) <= integral(g)
  3. integral(f) = 0 doesn't imply f = 0 (counterexample: f = 1_Q on [0,1])
  4. Markov's inequality: mu({|f| >= c}) <= integral(|f|) / c
- "Markov's inequality says: if the integral is small, the set where f is large must be small."
- Visual: number line with a large set marked where |f| >= c, bounded by integral/c
- "Property 3 is important: the Lebesgue integral can't distinguish a function from one that differs on a null set."

### Scene 7: Preview — Convergence Theorems (~60s)
- "The real power of the Lebesgue integral reveals itself in the convergence theorems."
- "The Monotone Convergence Theorem (MCT): if 0 <= f_1 <= f_2 <= ... and f_n -> f pointwise, then integral(f_n) -> integral(f)"
- "The Dominated Convergence Theorem (DCT): if f_n -> f pointwise and |f_n| <= g for integrable g, then integral(f_n) -> integral(f)"
- "These are the crown jewels — they're why the Lebesgue integral is so powerful."
- "With Riemann integration, even if f_n -> f uniformly, you might not be able to swap integral and limit. With Lebesgue, under mild conditions, you always can."
- Visual: function sequence converging, with areas under curves approaching the area under the limit
- "These theorems are the subject of the next video."

### Scene 8: Summary & Outro (~50s)
- Summary points:
  1. Simple function integral: sum a_i * mu(A_i)
  2. Lebesgue integral for f >= 0: sup of simple function integrals
  3. General case: integral(f^+) - integral(f^-)
  4. Dirichlet function: Lebesgue integrates it (value 0), Riemann can't
  5. Properties: linearity, monotonicity, Markov's inequality
  6. Preview: MCT and DCT — the convergence theorems
- play_outro(next="Convergence Theorems (MCT, DCT)", next_playlist="Measure Theory")
