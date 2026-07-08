# Video 108: Fundamental Theorem of Calculus (Proof)

**Playlist:** Real Analysis I (Video 10 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video108_FTCProof
**Script:** scripts/undergraduate/video-108-ftc-proof.py

## Prerequisites
- Video 99: The Real Numbers (Completeness, sup/inf)
- Video 100: Sequences and Convergence
- Video 101: Cauchy Sequences
- Video 102: Limits of Functions (epsilon-delta)
- Video 103: Continuity (epsilon-delta, Extreme Value Theorem)
- Video 104: Uniform Continuity (Heine-Cantor, Lipschitz)
- Video 105: The Derivative (Rigorous)
- Video 106: Mean Value Theorem (Proof)
- Video 107: The Riemann Integral (Darboux criterion, continuous => integrable)
- Videos 90-98: Introduction to Proofs (complete)

## Learning Objectives
1. Understand the accumulation function F(x) = integral from a to x of f(t) dt and its geometric meaning
2. State and prove FTC Part 1: if f is continuous on [a,b], then F is differentiable and F'(x) = f(x)
3. State and prove FTC Part 2: if F' = f and f is integrable, then integral from a to b of f = F(b) - F(a)
4. Use the MVT for integrals as the key lemma in both proofs
5. Apply FTC to evaluate definite integrals using antiderivatives
6. Understand FTC as the "bridge" connecting differentiation and integration

## Competitive Analysis References
Analysis completed 2026-07-08 in channel-analysis/improvements.md. Key findings:

**Competitors analyzed:** 3Blue1Brown (11.4M views, intuition-only, no proof), Dr. Trefor Bazett (250K views, semi-formal), Michael Penn (45K views, rigorous whiteboard), EpsilonDelta (120K views, animated semi-formal).

**Market gap:** NO competitor provides a Manim-animated RIGOROUS proof of both FTC parts with Riemann integral framework. This is our unique contribution.

**Key techniques to adopt:**
- 3B1B's accumulation function visualization (area growing with x) as the hook
- EpsilonDelta's "closes the loop" narrative framing
- Michael Penn's proof structure (MVT for integrals lemma, then both parts)
- Animated proof steps (our unique differentiator)

**Our unique contribution:**
- First Manim-animated rigorous proof of BOTH FTC parts
- Animated accumulation function + animated proof steps
- Connects directly to Video 107's Riemann integral framework
- MVT for integrals as a visual lemma

## Scene Plan (10 scenes, ~15 min target)

### Scene 1: Hook — The Bridge Between Calculus (~60s)
**Visual:** Inspired by 3B1B — show two pillars (differentiation and integration) with a bridge connecting them.
- "Everything in calculus revolves around two operations."
- "Differentiation: given a function, find its rate of change."
- "Integration: given a rate of change, find the total accumulation."
- "These seem like opposites. And they are — the Fundamental Theorem of Calculus proves it."
- "Today we prove BOTH parts of the FTC — rigorously, using the Riemann integral and the Mean Value Theorem."
- Show the two pillars in PRIMARY and ACCENT, bridge in SECONDARY
**Elements:** Pillar labels, bridge graphic, FTC label (max 4)
**Content budget:** 4 elements max

### Scene 2: Intro + Section Divider (~15s)
**Visual:** Channel intro, then section divider.
- play_intro("Fundamental Theorem of Calculus", "Real Analysis I")
- Section divider: "1 — The Accumulation Function"

### Scene 3: The Accumulation Function (~120s)
**Visual:** Animated area growing as x moves right — the key visual from 3B1B.
- "Let f be continuous on [a,b]. Fix a. Define the accumulation function:"
- F(x) = integral from a to x of f(t) dt
- Show: axes with f(t) drawn, x moving right from a to b, shaded area under curve growing
- "F(x) measures the signed area under f from a to x."
- "As x increases, F(x) accumulates more area."
- "What is the rate of change of this accumulation? In other words, what is F'(x)?"
- Animate: show F(x) as a curve being drawn alongside the shaded area
- "This question is FTC Part 1."
**Elements:** f(t) graph, shaded area growing, F(x) curve, formula (max 5)
**Content budget:** 5 elements max

### Scene 4: MVT for Integrals — The Key Lemma (~90s)
**Visual:** The lemma we need before the proof.
- Section divider: "2 — MVT for Integrals"
- "Lemma (MVT for Integrals): If f is continuous on [a,b], then there exists c in (a,b) such that:"
- integral from a to b of f(t) dt = f(c) * (b - a)
- "In other words: the average value of f on [a,b] is actually achieved at some point c."
- Visual: show f on [a,b], the rectangle f(c)*(b-a) shaded, with c marked
- "Proof: Since f is continuous on [a,b], it attains its min m and max M (by EVT, Video 103)."
- "So m(b-a) <= integral <= M(b-a)"
- "By IVT (Video 103), some c in (a,b) satisfies f(c) = integral/(b-a)"
- "This lemma is the engine that drives both proofs of the FTC."
**Elements:** Lemma statement, f graph with rectangle, c point, proof steps (progressive, max 5)
**Content budget:** 5 elements max

### Scene 5: FTC Part 1 — Statement and Proof (~150s)
**Visual:** The core proof of the first part.
- Section divider: "3 — FTC Part 1"
- "Theorem (FTC Part 1): If f is continuous on [a,b], and F(x) = integral from a to x of f(t) dt, then F is differentiable on (a,b) and F'(x) = f(x)."
- "Proof. Fix x in (a,b). For h small enough that x+h in [a,b]:"
- "F(x+h) - F(x) = integral from a to x+h of f(t)dt - integral from a to x of f(t)dt"
- "= integral from x to x+h of f(t) dt"
- Animate: show thin slice [x, x+h] under f, shaded
- "By the MVT for integrals: there exists c_h in (x, x+h) such that this equals f(c_h) * h"
- "So [F(x+h) - F(x)] / h = f(c_h)"
- "As h approaches 0, c_h is squeezed to x. Since f is continuous: f(c_h) approaches f(x)."
- "Therefore F'(x) = f(x). Done!"
- Animate: show c_h arrow pointing to x, then the limit
**Elements:** Theorem box, thin slice visual, MVT step, algebra chain, conclusion (progressive reveal, max 5)
**Content budget:** 5 elements max

### Scene 6: FTC Part 2 — Statement (~60s)
**Visual:** The second part, building on Part 1.
- Section divider: "4 — FTC Part 2"
- "Theorem (FTC Part 2): If f is integrable on [a,b] and F is an antiderivative of f (i.e., F' = f), then:"
- integral from a to b of f(x) dx = F(b) - F(a)
- "This is the computation theorem — it tells us how to evaluate integrals."
- "Instead of computing Riemann sums, just find any antiderivative F and plug in the endpoints."
- "The proof connects Riemann sums (Video 107) to antiderivatives (Video 105) via the MVT."
**Elements:** Theorem box, integral formula, brief explanation (max 4)
**Content budget:** 4 elements max

### Scene 7: FTC Part 2 — Proof (~150s)
**Visual:** The Riemann sum proof — our most ambitious animated proof.
- "Proof. Let P = {a = x_0 < x_1 < ... < x_n = b} be any partition of [a,b]."
- "By the Mean Value Theorem (Video 106), on each subinterval [x_{i-1}, x_i]:"
- "There exists c_i in (x_{i-1}, x_i) such that:"
- "F(x_i) - F(x_{i-1}) = F'(c_i) * (x_i - x_{i-1}) = f(c_i) * (x_i - x_{i-1})"
- Animate: show F(x) curve, partition points, tangent line at each c_i
- "Now sum over all subintervals:"
- "Sum of [F(x_i) - F(x_{i-1})] = Sum of f(c_i)(x_i - x_{i-1})"
- "The left side telescopes! All interior terms cancel:"
- "F(b) - F(a) = Sum of f(c_i)(x_i - x_{i-1})"
- Animate: show terms canceling, leaving only F(b) - F(a)
- "The right side is a Riemann sum for f with respect to partition P."
- "As the mesh ||P|| approaches 0, the Riemann sum approaches the integral:"
- "F(b) - F(a) = integral from a to b of f(x) dx. Done!"
**Elements:** Partition, MVT step, telescoping sum, Riemann sum, conclusion (progressive, max 5)
**Content budget:** 5 elements max

### Scene 8: Example — Evaluating an Integral with FTC (~90s)
**Visual:** A concrete example to cement understanding.
- Section divider: "5 — Example"
- "Evaluate: integral from 0 to 2 of x^2 dx"
- "Step 1: Find an antiderivative. F(x) = x^3/3 since F'(x) = x^2."
- "Step 2: Apply FTC Part 2:"
- "Integral = F(2) - F(0) = 8/3 - 0 = 8/3"
- Animate: show the graph of x^2 on [0,2], the shaded area, and the antiderivative
- "What took pages of Riemann sum computation in Video 107, FTC solves in two lines."
- "This is why the Fundamental Theorem is FUNDAMENTAL — it makes integration practical."
**Elements:** Problem statement, graph with shaded area, antiderivative, computation (max 5)
**Content budget:** 5 elements max

### Scene 9: Summary — The Bridge Complete (~60s)
**Visual:** Key takeaways with animated summary.
- "Key takeaways:"
- Progressive reveal:
  - "FTC Part 1: The integral function F(x) = integral of f is an antiderivative of f"
  - "FTC Part 2: integral of f from a to b = F(b) - F(a) for any antiderivative F"
  - "The MVT for integrals is the key lemma in both proofs"
  - "The Riemann integral and the derivative are genuinely inverse operations"
- "FTC closes the loop of calculus — differentiation and integration are two sides of the same coin."
- "In the next video, we explore pointwise and uniform convergence of function sequences."
- play_outro()
**Elements:** Summary bullet points, outro (max 5)
**Content budget:** 5 elements max

### Scene 10: Outro (~5s)
**Visual:** Standard outro.
- play_outro()
**Elements:** Outro only

## Visual Metaphors and Color Coding
- PRIMARY (#5BC0EB): the function f(t), the integrand
- ACCENT (#FFD166): the accumulation function F(x), antiderivative, key results
- SECONDARY (#7BC950): shaded areas, rectangles, geometric visualizations
- RED (#EF476F): the "bridge" graphic, important connections
- DIM: partition lines, supporting notation, proof scaffolding
- WHITE: main text, key labels

## Animation Notes
- Scene 3: The accumulation function animation is the visual centerpiece — area fills in as x sweeps right, F(x) curve grows alongside
- Scene 5: The thin slice [x,x+h] should animate with h shrinking, showing c_h getting squeezed to x
- Scene 7: The telescoping sum is the key visual moment — terms cancel one by one leaving F(b)-F(a)
- Scene 8: Keep the example fast and clean — this is the "aha" payoff moment
