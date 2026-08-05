# Video 157: Convergence Theorems (MCT, DCT)

**Playlist:** Measure Theory (Video 8 of 12)
**Class:** Video157_ConvergenceTheorems
**Script:** scripts/graduate/video-157-convergence-theorems.py
**Est. Duration:** 15 min (~600s)
**Status:** PLAN

## Competitive Analysis Summary

Competitive analysis based on landscape knowledge — consistent with prior Measure Theory videos. The convergence theorems (MCT, DCT, Fatou's Lemma) are among the most-wanted topics in measure theory.

**Market Landscape:**
- **Abide By Reason** covers MCT intuition but without animated proofs or Fatou's Lemma
- **Faculty of Khan** covers DCT in lecture style with a whiteboard — proofs on screen but static
- **Dr. Peyam** has separate videos for MCT and DCT, whiteboard style, good rigor but no visuals
- **vcubingx** does not have dedicated MCT/DCT content
- **Michael Penn** covers MCT with a proof but lecture-style, no animation
- **3Blue1Brown** does not cover measure theory convergence theorems directly
- **No channel** provides a systematic animated treatment covering all three: Fatou's Lemma -> MCT -> DCT with visual proof sketches and worked examples

**Our approach:** We cover all three convergence theorems in logical dependency order:
1. Fatou's Lemma first (the foundation — it's the inequality that motivates both MCT and DCT)
2. Monotone Convergence Theorem (from Fatou's Lemma — when the liminf IS the limit)
3. Dominated Convergence Theorem (from Fatou's Lemma — the most powerful and widely used)
4. Worked examples showing where Riemann fails but Lebesgue succeeds via DCT
5. Comparison of hypotheses: MCT requires monotonicity, DCT requires a dominating function

## Scene Plan

### Scene 1: Hook — "Swapping Limits and Integrals" (~60s)
- "In calculus, we often want to swap a limit and an integral. lim of integral of f_n equals integral of lim of f_n."
- "With the Riemann integral, this swap can fail even under very strong assumptions. Today we see three theorems that guarantee this swap under the Lebesgue integral."
- Visual: Text showing lim(integral(f_n)) vs integral(lim(f_n)), question mark between them
- "The Monotone Convergence Theorem, Fatou's Lemma, and the Dominated Convergence Theorem — collectively called the convergence theorems — are the crown jewels of Lebesgue integration."
- Progressive reveal: the problem statement, the question mark, the three theorem names
- play_intro() with "Convergence Theorems (MCT, DCT)" title

### Scene 2: Fatou's Lemma (~80s)
- "We begin with Fatou's Lemma, sometimes called the Fatou-Lebesgue theorem. It gives a one-sided inequality."
- Setup: {f_n} is a sequence of non-negative measurable functions on (X, Sigma, mu)
- Statement: integral(liminf f_n) <= liminf integral(f_n)
- "In words: the integral of the liminf is at most the liminf of the integrals."
- "This is a one-sided inequality — equality can fail. The integrals might overshoot."
- Visual: formula box for the inequality, with liminf highlighted
- "Fatou's Lemma is the foundation. Both MCT and DCT are proved using it."
- The intuitive reason: liminf picks the worst terms, so the integral of the liminf is the smallest possible. The integrals don't cooperate, so their liminf can be larger.

### Scene 3: Monotone Convergence Theorem (~90s)
- "The Monotone Convergence Theorem, or MCT, says that for increasing sequences of non-negative functions, Fatou's inequality becomes an equality."
- Hypotheses:
  1. 0 <= f_1 <= f_2 <= ... (monotone increasing)
  2. f_n -> f pointwise
  3. All f_n are measurable
- Conclusion: lim integral(f_n) = integral(f)
- "Equivalently: we can swap the limit and the integral."
- Visual: staircase functions increasing to a smooth curve, areas under each shown
- "Proof sketch from Fatou's Lemma: Since f_n is increasing, liminf integral(f_n) = lim integral(f_n). And liminf f_n = f. Fatou gives integral(f) <= lim integral(f_n). But f_n <= f implies integral(f_n) <= integral(f), so lim integral(f_n) <= integral(f). Equality!"
- Progressive reveal: hypothesis, conclusion, proof idea
- section_divider(1, "Monotone Convergence Theorem")

### Scene 4: MCT Application — Geometric Series (~70s)
- "The MCT is not just theory. Here's a concrete application."
- Example: On [0,1] with Lebesgue measure, f_n(x) = (1 - x)^n * e^x
- "As n increases, (1-x)^n converges pointwise to 0 for x in (0,1] and equals 1 at x=0."
- "The pointwise limit is the zero function (almost everywhere)."
- "By MCT: lim integral_0^1 (1-x)^n e^x dx = integral_0^1 0 dx = 0"
- "This tells us the integrals converge to zero — which we can verify by explicit computation using integration by parts."
- Visual: functions (1-x)^n * e^x on [0,1] as n increases, getting more concentrated near x=0
- "Notice: we didn't need to evaluate the integrals explicitly. MCT gave us the limit for free."

### Scene 5: Dominated Convergence Theorem (~90s)
- "The MCT is powerful but requires monotonicity. The Dominated Convergence Theorem, or DCT, removes this restriction at the cost of one extra hypothesis."
- Hypotheses:
  1. f_n -> f pointwise
  2. |f_n| <= g for all n, where g is integrable (integral(|g|) < infinity)
  3. All functions are measurable
- Conclusion: lim integral(f_n) = integral(f), and also integral(|f_n - f|) -> 0
- "The function g is called the dominating function, or the integrable majorant."
- "The DCT is the most-used theorem in measure theory. It justifies swapping limits and integrals, differentiating under the integral sign, and interchanging infinite sums and integrals."
- Visual: f_n functions bouncing up and down but bounded by a g curve from above and -g from below
- "Proof sketch: Apply Fatou's Lemma to g + f_n and g - f_n separately. This gives two inequalities that sandwich lim integral(f_n) = integral(f)."
- section_divider(2, "Dominated Convergence Theorem")

### Scene 6: DCT Application — Exponential Limit (~70s)
- "A classic DCT application: evaluate lim integral of f_n."
- Example: On [0,1], f_n(x) = n * x * e^{-n*x^2}
- "As n -> infinity, f_n(x) -> 0 for every x > 0, and f_n(0) = 0. So f -> 0 pointwise."
- "But can we swap limit and integral? Need a dominating function."
- "Claim: |f_n(x)| <= e^{-1/2} / (2 * x) for x > 0, and |f_n(0)| = 0. But this isn't integrable near 0!"
- Better approach: "By calculus, max of n*x*exp(-n*x^2) over x >= 0 is sqrt(n/2)*exp(-1/2). So |f_n(x)| <= sqrt(n/e) for all x."
- "This isn't uniform in n. Let's use a cleaner example."
- Cleaner example: f_n(x) = x^n on [0,1]. Then f_n -> 0 pointwise, and |x^n| <= 1 (integrable on [0,1]).
- "By DCT: lim integral_0^1 x^n dx = integral_0^1 0 dx = 0"
- "Indeed, integral_0^1 x^n dx = 1/(n+1) -> 0. DCT gives us this for free without evaluating."
- Visual: x^n curves approaching the zero function, with g(x)=1 as the bound

### Scene 7: Comparison — Where Riemann Fails (~70s)
- "Why can't the Riemann integral do this? Consider f_n = n * 1_{[0, 1/n]} on [0,1]."
- "Each f_n is a step function (Riemann integrable): integral = n * (1/n) = 1."
- "The pointwise limit: for x > 0, eventually n > 1/x so f_n(x) = 0. For x = 0, f_n(0) = n -> infinity. So f_n -> 0 pointwise on (0,1]."
- "With Riemann: each integral = 1, but the limit function has integral 0. lim integral(f_n) = 1 != 0 = integral(lim f_n)."
- "The Riemann integral cannot swap limit and integral here. The functions converge to zero but their integrals remain at 1."
- "With Lebesgue: f_n -> 0 a.e. and |f_n| <= g? No single integrable g dominates all f_n (they form a spike growing taller and thinner)."
- "So neither MCT nor DCT applies directly — but that's the point: the hypotheses fail, and the theorem correctly tells us not to swap."
- "The convergence theorems are both powerful and precise: they give conditions that are both necessary and sufficient in practice."

### Scene 8: Summary & Outro (~50s)
- Summary points:
  1. Fatou's Lemma: integral(liminf f_n) <= liminf integral(f_n) (one-sided inequality)
  2. MCT: for increasing non-negative sequences, lim integral(f_n) = integral(lim f_n)
  3. DCT: for dominated sequences, lim integral(f_n) = integral(lim f_n) (most general)
  4. Applications: evaluating limits of integrals without explicit computation
  5. Riemann comparison: no analogous theorems exist for Riemann integration
  6. These three theorems are the primary reason the Lebesgue integral is preferred in modern analysis
- play_outro(next="L^p Spaces", next_playlist="Measure Theory")
