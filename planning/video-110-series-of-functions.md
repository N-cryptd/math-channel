# Video 110: Series of Functions

**Playlist:** Real Analysis I (Video 12 of 12) — FINAL VIDEO
**Level:** Undergraduate (Real Analysis)
**Class:** Video110_SeriesOfFunctions
**Script:** scripts/undergraduate/video-110-series-of-functions.py

## Competitive Analysis Reference

Analysis completed 2026-07-08. See `channel-analysis/improvements.md` — section "Series of Functions (Video 110)".

Key competitor insights incorporated:
- Bright Side of Mathematics: incremental definition building, systematic structure
- Michael Penn: M-test examples connecting to specific power series
- Dr. Trefor Bazett: "power series are the payoff" framing, Taylor series connection
- BriTheMathGuy: "when can you swap sum and integral?" hook question

Our unique advantage: Animated partial sums convergence, M-test envelope visualization, unified narrative showing how uniform convergence of series enables term-by-term differentiation/integration, culminating in the proof that power series are infinitely differentiable.

## Prerequisites
- Video 100: Sequences and Convergence
- Video 109: Pointwise vs Uniform Convergence (direct prerequisite)
- Calculus II: Infinite Series, Power Series, Taylor Series (informal familiarity)

## Learning Objectives
1. Define convergence of a series of functions via partial sums
2. Define uniform convergence of a series of functions
3. State and apply the Weierstrass M-test for uniform convergence
4. Understand term-by-term integration: uniform convergence allows swapping sum and integral
5. Understand term-by-term differentiation: uniform convergence of derivatives allows swapping sum and derivative
6. Apply all results to power series: uniform convergence on compact subsets of the interval of convergence
7. Conclude that power series are infinitely differentiable within their radius of convergence

## Scene Plan (8 scenes, ~12 min)

### Scene 1: Hook (~60s)
- play_intro
- "When can you swap a sum and an integral? When can you differentiate term by term? The answer: when the series converges UNIFORMLY."
- Animated: partial sums S_1, S_2, S_3 of a series approaching the limit function
- Preview: "Today we go from sequences of functions to SERIES of functions, and unlock the operations that make power series so powerful."

### Scene 2: Convergence of Series of Functions (~90s)
- Section: "1 — Series of Functions"
- Definition: sum f_n converges at x if the sequence of partial sums S_N(x) = sum_{n=1}^{N} f_n(x) converges
- The series converges pointwise if S_N → f pointwise
- The series converges uniformly if S_N → f uniformly
- "Everything from the previous video applies — just replace f_n with partial sums S_N"
- Show partial sums building up visually

### Scene 3: Weierstrass M-Test (~90s)
- Section: "2 — The Weierstrass M-Test"
- Statement: if |f_n(x)| ≤ M_n for all x in E, and sum M_n converges, then sum f_n converges uniformly on E
- "Find constants M_n that bound each |f_n(x)| from above"
- Example: sum x^n/n! on [0,1] — M_n = 1/n!, sum converges
- Visual: show |f_n| bounded by M_n envelope

### Scene 4: Term-by-Term Integration (~80s)
- Section: "3 — Term-by-Term Integration"
- Theorem: if sum f_n converges uniformly on [a,b], then integral of sum = sum of integrals
- "Uniform convergence lets you pull the integral inside the sum"
- Proof sketch: |∫S_N - ∫f| ≤ ∫|S_N - f| ≤ (b-a) sup|S_N - f| → 0
- "This is the swap theorem for integrals!"

### Scene 5: Term-by-Term Differentiation (~80s)
- Section: "4 — Term-by-Term Differentiation"
- Theorem: if sum f_n converges pointwise, each f_n' is continuous, and sum f_n' converges uniformly, then (sum f_n)' = sum f_n'
- "Differentiation requires MORE — uniform convergence of the DERIVATIVES, not the original series"
- Why: differentiation amplifies small differences (think: derivative of x^n is n*x^{n-1})
- Key contrast: integration smooths out errors; differentiation magnifies them

### Scene 6: Power Series — Everything Comes Together (~90s)
- Section: "5 — Power Series"
- Definition: sum a_n * x^n centered at 0 (or more generally sum a_n (x-c)^n)
- Radius of convergence R (from ratio test or root test)
- Key result: a power series converges uniformly on any compact subset of (-R, R)
- Proof idea: use M-test with M_n = |a_n| * r^n where r < R
- "Inside the radius, you can differentiate and integrate term by term — infinitely many times!"

### Scene 7: The Big Picture (~50s)
- Connect all results: M-test → uniform convergence → swap theorems → power series properties
- "Uniform convergence is the key that unlocks all the operations"
- This completes the arc: sequences → convergence → uniform convergence → series → power series

### Scene 8: Summary + Outro + Celebration (~60s)
- Key takeaways recap
- Celebrate completing Real Analysis I (12 videos!)
- "Next up: Abstract Algebra I or Complex Analysis — stay tuned!"
- play_outro("Real Analysis I Complete!", "Real Analysis I")
