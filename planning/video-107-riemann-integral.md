# Video 107: The Riemann Integral

**Playlist:** Real Analysis I (Video 9 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video107_RiemannIntegral
**Script:** scripts/undergraduate/video-107-riemann-integral.py

## Prerequisites
- Video 99: The Real Numbers (Completeness, sup/inf)
- Video 100: Sequences and Convergence
- Video 101: Cauchy Sequences
- Video 102: Limits of Functions (epsilon-delta)
- Video 103: Continuity (epsilon-delta, Extreme Value Theorem)
- Video 104: Uniform Continuity (Heine-Cantor, Lipschitz)
- Video 105: The Derivative (Rigorous)
- Video 106: Mean Value Theorem (Proof)
- Videos 90-98: Introduction to Proofs (complete)

## Learning Objectives
1. Understand partitions of an interval and mesh size
2. Define upper and lower Darboux sums L(f,P) and U(f,P)
3. Understand refinement of partitions and how sums behave under refinement
4. Define the upper and lower integrals (inf of upper sums, sup of lower sums)
5. State the Darboux criterion for integrability: f integrable iff L* = U*
6. Prove that continuous functions on [a,b] are Riemann integrable (using uniform continuity)
7. Show the Dirichlet function is NOT integrable as a counterexample
8. State that monotone functions are integrable (without full proof)

## Competitive Analysis References
Analysis completed 2026-07-08 in channel-analysis/improvements.md (appended to end of file). Key findings:

**Competitors analyzed:** EpsilonDelta (122K views), Michael Penn (42K views), Bright Side of Mathematics (74K views), Dr. Peyam (31K views), 3B1B reference (11.4M views for essence of calculus).

**Market gap:** NO competitor provides a Manim-animated formal Riemann integral with Darboux criterion proof. Bright Side uses tablet (not Manim), EpsilonDelta uses custom animation, Michael Penn and Dr. Peyam use whiteboard only.

**Key techniques to adopt:**
- EpsilonDelta's "story arc" approach: Riemann sums motivation → formal definition → Darboux criterion
- Animated partition refinement showing upper/lower sums converging
- Animated Dirichlet function with color-coded rational/irrational points
- EpsilonDelta's curiosity hook about "what we learn vs Riemann's original"

**Our unique contribution:**
- Animated Darboux criterion proof (no competitor does this)
- Visual partition refinement animation
- Animated Dirichlet function showing non-integrability
- Continuous => integrable proof with animated uniform continuity application

## Scene Plan (9 scenes, ~12 min target)

### Scene 1: Hook — Area Under a Curve (~60s)
**Visual:** Classic area-under-curve animation inspired by 3B1B's essence of calculus. Start with a smooth curve on [a,b], show rectangle approximations getting finer.
- "In calculus, you learned that the integral gives the area under a curve."
- "You drew rectangles, made them thinner, and the area got more accurate."
- Show 4 rectangles, then 8, then 16 → area converges
- "But what exactly does 'more accurate' mean? And when does this limit actually exist?"
- "Today we define the Riemann integral — rigorously."
- Color-code: curve in PRIMARY, rectangles in SECONDARY (lower) and ACCENT (upper)
**Elements:** Curve graph, partition rectangles (max 4 visible at once)
**Content budget:** 4 elements max

### Scene 2: Intro + Section Divider (~15s)
**Visual:** Channel intro, then section divider.
- play_intro("The Riemann Integral", "Real Analysis I")
- Section divider: "1 — Partitions and Sums"

### Scene 3: Partitions and Darboux Sums (~120s)
**Visual:** Formal definition building progressively.
- Section divider: "1 — Partitions and Sums"
- "A partition P of [a,b] is a finite set of points..."
- Show interval [a,b] with partition points marked: a = x_0 < x_1 < ... < x_n = b
- "The mesh of P is the width of the widest subinterval: ||P|| = max(x_i - x_{i-1})"
- "For a bounded function f on [a,b], on each subinterval [x_{i-1}, x_i]..."
- "The supremum M_i and infimum m_i of f exist by completeness"
- "Upper sum: U(f,P) = sum of M_i * (x_i - x_{i-1})"
- "Lower sum: L(f,P) = sum of m_i * (x_i - x_{i-1})"
- Animate: show function with rectangles reaching up to M_i (upper, in ACCENT) and up to m_i (lower, in SECONDARY)
- "Always: L(f,P) <= U(f,P) for every partition P"
**Elements:** Number line with partition, function graph, upper rectangles, lower rectangles, formulas (progressive reveal, max 5)
**Content budget:** 5 elements max

### Scene 4: Refinement and Upper/Lower Integrals (~120s)
**Visual:** Show partition getting finer, behavior of sums.
- "A partition Q refines P if Q contains all points of P, plus more."
- Animate: start with 3-point partition, add points to get 6-point partition
- "Key fact: refinement squeezes the gap."
- "L(f,P) <= L(f,Q) <= U(f,Q) <= U(f,P)" (animated inequality chain)
- "The lower integral L* = sup over all partitions P of L(f,P)"
- "The upper integral U* = inf over all partitions P of U(f,P)"
- "We always have L* <= U*"
- Animate: show a number line with L(f,P) values approaching L* from below, U(f,P) values approaching U* from above
**Elements:** Partition refinement animation, inequality chain, number line with L*/U* (max 5)
**Content budget:** 5 elements max

### Scene 5: Darboux Criterion — The Definition (~90s)
**Visual:** The central definition, presented as a formula box.
- Section divider: "2 — Integrability"
- "Definition: f is Riemann integrable on [a,b] if L* = U*."
- "The common value is called the Riemann integral: integral from a to b of f(x) dx"
- "Equivalently (Darboux criterion): for every epsilon > 0, there exists a partition P such that U(f,P) - L(f,P) < epsilon"
- Show formula box with the epsilon-definition, highlighted in ACCENT
- "This says: we can make the gap between upper and lower sums arbitrarily small."
- Animate: show U - L gap shrinking as partition gets finer
**Elements:** Definition box, epsilon-formula, gap animation (max 4)
**Content budget:** 4 elements max

### Scene 6: Non-Integrable Function — The Dirichlet Function (~120s)
**Visual:** The dramatic counterexample showing not every bounded function is integrable.
- Section divider: "3 — When Integration Fails"
- "Consider the Dirichlet function: d(x) = 1 if x is rational, 0 if x is irrational"
- Animate: on [0,1], color rational points in PRIMARY, irrational points in SECONDARY — both dense!
- "Every subinterval contains both rational and irrational points"
- "So M_i = 1 and m_i = 0 for EVERY subinterval"
- "Therefore U(f,P) = 1 and L(f,P) = 0 for EVERY partition P"
- "The gap U(f,P) - L(f,P) = 1 never shrinks — no matter how fine the partition"
- "The Dirichlet function is NOT Riemann integrable"
- "Integrability requires more than boundedness — it requires the function to not oscillate too wildly"
**Elements:** Dirichlet function graph, color-coded points, partition rectangles, conclusion (max 5)
**Content budget:** 5 elements max

### Scene 7: Continuous Functions Are Integrable (~150s)
**Visual:** The positive theorem — the main proof.
- Section divider: "4 — Continuous => Integrable"
- "Theorem: If f is continuous on [a,b], then f is Riemann integrable."
- "Proof strategy: Use uniform continuity from Video 104."
- "Since f is continuous on the closed interval [a,b], by Heine-Cantor (Video 104), f is uniformly continuous."
- "So for every epsilon > 0, exists delta > 0 such that |x - y| < delta implies |f(x) - f(y)| < epsilon / (b - a)"
- Animate: show the uniform continuity epsilon-delta on the graph
- "Choose a partition P with mesh ||P|| < delta"
- "On each subinterval [x_{i-1}, x_i]: M_i - m_i < epsilon / (b - a)"
- "So: U(f,P) - L(f,P) = sum of (M_i - m_i)(x_i - x_{i-1})"
- "< sum of [epsilon / (b-a)] * (x_i - x_{i-1})"
- "= [epsilon / (b-a)] * sum of (x_i - x_{i-1})"
- "= [epsilon / (b-a)] * (b - a) = epsilon"
- "By the Darboux criterion, f is integrable!"
- Animate: show the algebraic chain collapsing to epsilon, with a satisfying highlight
**Elements:** Theorem statement, uniform continuity graph, partition, algebra chain (progressive reveal, max 5)
**Content budget:** 5 elements max

### Scene 8: More Integrable Functions (~60s)
**Visual:** Quick catalog of other integrable function classes.
- "Two more important classes of integrable functions:"
- "1. Monotone functions on [a,b] are integrable"
- "Proof sketch: at discontinuity points, the jump can be made arbitrarily small with a fine partition"
- "2. Functions with finitely many discontinuities on [a,b] are integrable"
- "This covers most functions encountered in practice"
- "The only way integrability fails is if the function oscillates infinitely often"
**Elements:** Two statements with brief justification (max 4)
**Content budget:** 4 elements max

### Scene 9: Summary + Outro (~45s)
**Visual:** Key takeaways with animated summary.
- "Key takeaways:"
- Progressive reveal of bullet points:
  - "A partition divides [a,b] into subintervals"
  - "Upper and lower Darboux sums bound the integral"
  - "f is integrable iff upper and lower integrals coincide (Darboux criterion)"
  - "Continuous functions are always integrable"
  - "The Dirichlet function shows boundedness alone is not enough"
- "In the next video, we prove the Fundamental Theorem of Calculus — the bridge between derivatives and integrals."
- play_outro()
**Elements:** Summary bullet points, outro (max 5)
**Content budget:** 5 elements max

## Visual Metaphors and Color Coding
- PRIMARY (#5BC0EB): function curves, rational points, lower sums
- SECONDARY (#7BC950): lower rectangles, irrational points, safe bounds
- ACCENT (#FFD166): upper rectangles, key definitions, highlighted results
- RED (#EF476F): non-integrable examples, the Dirichlet function danger
- DIM: partition lines, supporting notation
- WHITE: main text, key labels

## Animation Notes
- Scene 3: The partition animation should show points appearing one by one on the number line, then rectangles growing up from the x-axis
- Scene 4: Refinement animation — new partition points slide in, rectangles split, lower area goes up, upper area goes down
- Scene 6: Dirichlet function — scatter plot animation with two colors (PRIMARY for rational, SECONDARY for irrational) filling in simultaneously
- Scene 7: The algebra chain should use Transform animations to morph each inequality into the next
