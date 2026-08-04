# Video 155: Lebesgue Measurable Functions

**Playlist:** Measure Theory (Video 5 of 12)
**Class:** Video155_LebesgueMeasurableFunctions
**Script:** scripts/graduate/video-155-lebesgue-measurable-functions.py
**Est. Duration:** 15 min (~500s)
**Status:** PLAN

## Competitive Analysis Summary

Competitive analysis based on landscape knowledge — consistent with prior Measure Theory videos (151-154) where web search was unavailable. No major Manim-animated channel has a dedicated video on measurable functions specifically. The topic is always bundled into broader Lebesgue integral lectures.

**Market Landscape:**
- **Abide By Reason** (652K views on Lebesgue integral) covers the integral concept but never formally defines measurable functions or simple function approximation
- **vcubingx** (386K views) shows horizontal slicing but doesn't cover measurability conditions
- **Faculty of Khan** has lecture-style videos on Lebesgue integration that mention measurable functions but without animation
- **Dr. Peyam** covers measurable functions in lecture format with proofs on whiteboard
- **Michael Penn** has a video on the Lebesgue integral that touches on measurability
- No channel has a systematic animated treatment of measurable functions, simple functions, or Egorov's theorem

**Our approach:** Visual-first. Open with the core question: "what functions can we integrate with Lebesgue measure?" Show the preimage condition visually — a function is measurable iff the preimage of every Borel set is measurable. Animate simple functions as step functions building up to approximate any measurable function. Visual staircase approximation converging to a curve. Egorov's theorem gets a visual treatment showing uniform convergence except on a small set.

## Scene Plan

### Scene 1: Hook — "Which Functions Can We Measure?" (~55s)
- "Four videos ago we started building measure theory. We have measurable sets, sigma-algebras, and the Lebesgue measure. Now the question: what functions can we actually integrate?"
- Visual: a function graph, then the real line below colored to show measurable/non-measurable sets
- "The answer is surprisingly generous — almost every function you've ever encountered is Lebesgue measurable."
- Progressive reveal: the question, the function graph visual, the surprising answer
- Transition: "To define the Lebesgue integral, we first need a rigorous notion of measurability for functions."

### Scene 2: Formal Definition — Measurable Functions (~90s)
- "Let (X, Sigma) be a measurable space. A function f: X -> R is measurable if for every open set U in R, the preimage f^{-1}(U) is in Sigma."
- Definition box with the formal statement, color-coded:
  - f: X -> R — PRIMARY
  - f^{-1}(U) in Sigma for all open U — ACCENT
  - "equivalently, for all a in R: {x : f(x) > a} is in Sigma" — SECONDARY
- Visual: number line with f, arrows showing preimages of intervals mapping back to measurable sets
- Key equivalences (progressive reveal):
  1. f^{-1}(open) measurable — the definition
  2. f^{-1}((a, inf)) measurable — equivalent
  3. f^{-1}((a, b)) measurable — equivalent
  4. All of these are equivalent characterizations
- "Notice: we're checking preimages of sets in the codomain, not the domain. The function doesn't need to be continuous or even nice — it just needs to send measurable sets back to measurable sets."

### Scene 3: Key Examples — Measurable vs Non-Measurable (~80s)
- Examples of measurable functions (progressive reveal):
  1. Every continuous function f: R -> R is measurable (preimage of open is open)
  2. The indicator function 1_E is measurable iff E is measurable
  3. The Dirichlet function (1 on Q, 0 on R\Q) is measurable! (Q has measure zero)
  4. Monotone functions are measurable
- "The Dirichlet function is the star example — it's nowhere continuous and not Riemann integrable, but it IS Lebesgue measurable."
- Visual: indicator function on [0,1] showing 1_E for measurable E
- Visual: Dirichlet function graph with rationals highlighted in red

### Scene 4: Simple Functions (~80s)
- "Simple functions are the building blocks of Lebesgue integration."
- Definition: a function s: X -> R is simple if it takes only finitely many values
- Standard form: s(x) = sum_{i=1}^{n} a_i * 1_{A_i}(x) where {A_i} partition X
- Visual: step function diagram — horizontal bars at levels a_1, a_2, ..., a_n over sets A_1, A_2, ..., A_n
- "Every simple function is measurable if and only if each A_i is measurable."
- Progressive reveal: definition, standard form formula, visual step function, measurability condition
- "Simple functions play the role that rectangles play in Riemann integration — they're our basic approximating objects."

### Scene 5: Approximation Theorem (~90s)
- "One of the most important theorems in measure theory:"
- Theorem (Simple Function Approximation): For every measurable function f >= 0, there exists a sequence of simple functions s_n >= 0 such that s_n converges pointwise to f, and s_1 <= s_2 <= ... <= f (monotone increasing).
- Visual: staircase function converging upward to a smooth curve
- Explicit construction (progressive reveal):
  - Divide the range [0, n] into 2^{2n} intervals of length 1/2^{2n}
  - Define s_n(x) = k/2^{2n} when k/2^{2n} <= f(x) < (k+1)/2^{2n}, and s_n(x) = n when f(x) >= n
- "The construction is beautifully explicit — we're approximating f by rounding down to finer and finer grids."
- Visual: coarse grid -> fine grid -> finer grid approximation
- "This theorem tells us: if you understand simple functions, you understand ALL non-negative measurable functions."

### Scene 6: Properties of Measurable Functions (~70s)
- "Measurable functions behave wonderfully under algebraic operations:"
- Progressive reveal of properties:
  1. If f and g are measurable, then f+g is measurable
  2. If f and g are measurable, then f*g is measurable
  3. If f is measurable, then |f| is measurable
  4. If f_n is a sequence of measurable functions converging pointwise to f, then f is measurable
  5. max(f, g) and min(f, g) are measurable when f, g are measurable
- "The pointwise limit property (4) is especially powerful — it says measurability is preserved under limits. This is NOT true for continuity."
- Visual: sequence of functions converging, all highlighted as measurable
- Color-code: algebraic operations in PRIMARY, limit property in RED (important)

### Scene 7: Egorov's Theorem — Statement (~80s)
- "We close with a stunning result about sequences of measurable functions."
- Egorov's Theorem: Let (X, Sigma, mu) be a finite measure space, and let f_n -> f pointwise. Then for every epsilon > 0, there exists a measurable set E with mu(X \ E) < epsilon such that f_n -> f UNIFORMLY on E.
- "Pointwise convergence almost everywhere can be upgraded to uniform convergence, except on a set of arbitrarily small measure."
- Visual: a function sequence converging pointwise but with some bad spots, then highlight the set E where convergence is uniform
- Key conditions highlighted:
  1. Finite measure space (mu(X) < inf) — ACCENT
  2. Pointwise convergence (or a.e. convergence) — PRIMARY
  3. Conclusion: uniform convergence off a small set — RED
- "Egorov's theorem is the bridge between pointwise and uniform convergence in measure theory. It fails without the finite measure assumption."
- Example where it fails: f_n(x) = 1_{[n, n+1]} on R — converges to 0 pointwise, but not uniformly on any set of finite complement
- "Egorov is a preview of the convergence theorems (Dominated Convergence, Monotone Convergence) that will power the Lebesgue integral."

### Scene 8: Summary & Outro (~45s)
- Recap key ideas:
  - Measurable function: preimages of open sets are measurable
  - Equivalences: > a, >= a, < a conditions
  - Continuous, indicator, and Dirichlet functions are all measurable
  - Simple functions: finite-valued, the building blocks
  - Approximation theorem: every non-negative measurable function is a limit of simple functions
  - Measurable functions form an algebra closed under limits
  - Egorov's theorem: pointwise -> uniform on finite measure spaces (off a small set)
- "Next time we'll define the Lebesgue integral itself — the integral that finally fixes everything Riemann couldn't handle."
- play_outro(next="The Lebesgue Integral", next_playlist="Measure Theory")
