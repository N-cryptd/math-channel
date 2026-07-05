# Video 102: Limits of Functions

**Playlist:** Real Analysis I (Video 4 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video102_LimitsOfFunctions
**Script:** scripts/undergraduate/video-102-limits-of-functions.py

## Prerequisites
- Video 99: The Real Numbers (Completeness)
- Video 100: Sequences and Convergence (epsilon-N definition)
- Video 101: Cauchy Sequences (convergence vs Cauchy distinction)
- Videos 90-98: Introduction to Proofs (complete)
- Understanding of epsilon-N convergence for sequences

## Learning Objectives
1. Understand intuitively what it means for f(x) to approach L as x approaches a
2. State the formal epsilon-delta definition of a limit of a function
3. Understand each part of the definition (the quantifier order matters!)
4. Prove a simple limit using epsilon-delta (e.g., lim_{x->2} (3x-1) = 5)
5. Understand the sequential characterization: lim_{x->a} f(x) = L iff for all sequences x_n -> a, f(x_n) -> L
6. Use the sequential criterion to show a limit does NOT exist

## Competitive Analysis References
- Analysis: channel-analysis/improvements.md (2026-07-04 entry for Video 102)
- Michael Penn (349K subs): Whiteboard, systematic. Structure 8/10, Visuals 4/10. Avoid: dense lecture without visual intuition.
- Michael Penn second video: Sequential limits -- key connection to our Video 100. Adopt: the sequential characterization.
- Wrath of Math (241K+ views): Lecture with annotated slides. Structure 7/10. Covers epsilon-delta and sequence connection.
- Dr. Trefor Bazett (606K subs): Manim-like animations, "A Tale of Three Functions" hook. Structure 9/10, Visuals 8/10, Hooks 9/10. Adopt: the three-functions narrative hook.
- Key gap: NO competitor animates the delta-tube (vertical band around x=a) and epsilon-band (horizontal band around L) simultaneously on a function graph.
- Our unique edges:
  - Three-function animated hook inspired by Trefor Bazett but with rigorous treatment
  - Animated epsilon-delta box: simultaneous shrinking of delta-tube and epsilon-band on function graph
  - Sequential characterization connecting back to Video 100
  - Color-coded definition with animated proof

## Scene Plan (10 scenes, ~15 min target)

### Scene 1: Hook -- Three Functions, One Question (~60s)
**Visual:** Three animated function graphs side by side, all approaching x=2.
- Show three functions: f(x) = x^2, g(x) = sin(pi/x) near x=0, and a removable discontinuity (e.g., (x^2-4)/(x-2))
- Question: "All three functions are defined near x=2. But do they all approach the same value?"
- "More importantly: what does 'approach' even mean rigorously?"
- Transition to intro.
**Elements:** Three mini function graphs, question text
**Content budget:** 4 elements max

### Scene 2: Intro + Section Divider (~20s)
**Visual:** Channel intro animation, then section divider.
- play_intro("Limits of Functions", "Real Analysis I")
- Section divider: "1 -- The Intuition"

### Scene 3: What Does f(x) Approach? -- Intuition (~90s)
**Visual:** Animated function graph with a moving point approaching x=a from both sides.
- "In calculus, we said the limit of f(x) as x approaches a is L if f(x) gets close to L."
- Animate: a point on the x-axis approaching 'a', a corresponding point on the graph, and an arrow showing f(x) approaching L on the y-axis.
- "But 'close' is vague. How close? How do we prove it?"
- Show the removable discontinuity example: f(x) = (x^2-4)/(x-2). At x=2, the function is undefined, but the limit is 4.
- Key insight: "The limit does NOT depend on the value of f at a. It only depends on values NEAR a."
- "This is what makes limits powerful: we can talk about behavior near a point without ever evaluating at that point."
**Elements:** Graph, moving point, arrow, removable discontinuity annotation
**Content budget:** Progressive reveal, max 5

### Scene 4: Section Divider -- Formal Definition (~5s)
**Visual:** Section divider "2 -- The Definition"

### Scene 5: The Formal Definition -- Epsilon-Delta (~120s)
**Visual:** Function graph with animated epsilon-band (horizontal, around L) and delta-tube (vertical, around a).
- Start with the function graph of f(x) = 3x - 1, with the limit point at x=2, L=5.
- "We define: the limit of f of x as x approaches a equals L, if for every epsilon greater than zero, there exists a delta greater than zero, such that whenever zero is less than the absolute value of x minus a, and x minus a is less than delta, then the absolute value of f of x minus L is less than epsilon."
- Animate: 
  1. Show epsilon-band on y-axis (horizontal strip around L=5)
  2. Show delta-tube on x-axis (vertical strip around a=2, excluding a itself)
  3. The function passes through the intersection
  4. Shrink epsilon, watch delta shrink too
- Unpack each part:
  - "For every epsilon": you choose ANY tolerance on the output
  - "There exists delta": I can find a matching tolerance on the input
  - "0 < |x - a| < delta": x is close to a but NOT equal to a (the limit ignores the point itself!)
  - "|f(x) - L| < epsilon": the output is within the tolerance you chose
- "The key is the quantifier ORDER. For every epsilon, there exists delta. Epsilon comes first. You challenge me with any tolerance, and I must find a delta that works."
**Elements:** Graph with epsilon-band and delta-tube, definition box (MathTex), part explanations
**Content budget:** Progressive reveal, fade old elements, max 5 at a time

### Scene 6: Section Divider -- Proof (~5s)
**Visual:** Section divider "3 -- Proof Example"

### Scene 7: Proof -- lim_{x->2} (3x-1) = 5 (~120s)
**Visual:** Step-by-step proof with the animated delta-tube growing/shrinking.
- Claim: "The limit as x approaches 2 of 3x minus 1 equals 5."
- Proof structure:
  - "Let epsilon greater than 0."
  - "Choose delta = epsilon / 3."
  - "Suppose 0 < |x - 2| < delta."
  - "Then |f(x) - 5| = |3x - 1 - 5| = |3x - 6| = 3|x - 2|"
  - "And 3|x - 2| < 3 * delta = 3 * (epsilon/3) = epsilon."
  - "Therefore |f(x) - 5| < epsilon. QED."
- Key insight box: "We work backwards to find delta, then verify forwards."
- Show the animated verification: delta-tube maps into epsilon-band via the linear function
**Elements:** Claim, proof steps (progressive reveal), key insight box
**Content budget:** Progressive reveal, max 5 lines at a time

### Scene 8: Section Divider -- Sequential Characterization (~5s)
**Visual:** Section divider "4 -- Limits and Sequences"

### Scene 9: Sequential Characterization + Non-Existence (~120s)
**Visual:** Split scene. Part 1: theorem statement. Part 2: application showing limit does NOT exist.
- Part 1: Theorem
  - "Theorem: lim_{x->a} f(x) = L if and only if for every sequence (x_n) converging to a with x_n != a, the sequence f(x_n) converges to L."
  - Visual: animate x_n -> a on x-axis, then f(x_n) -> L on y-axis via the function graph
  - "This connects everything we learned about sequences to limits of functions."
- Part 2: Application -- showing a limit does NOT exist
  - "Consider f(x) = sin(pi/x) as x -> 0."
  - "If we pick x_n = 1/n, then f(x_n) = sin(n*pi) = 0 for all n."
  - "But if we pick y_n = 2/(2n+1), then f(y_n) = sin((2n+1)*pi/2) = +-1."
  - "Two sequences approaching 0 give different limits for f(x_n). Therefore the limit does NOT exist!"
  - Color: x_n sequence in PRIMARY, y_n sequence in RED
  - "This is the power of the sequential criterion. To prove no limit exists, just find two sequences with different outputs."
**Elements:** Theorem statement, animated sequence-to-limit visual, counterexample with two sequences
**Content budget:** Progressive reveal, max 5

### Scene 10: Summary + Outro (~60s)
**Visual:** Key takeaways as progressive reveal, then outro.
- Key takeaways:
  - The epsilon-delta definition makes "f(x) approaches L" precise
  - The quantifier order matters: for every epsilon, there EXISTS delta
  - The limit at a point does NOT depend on f(a) itself
  - The sequential criterion connects limits of functions to limits of sequences
  - To show no limit exists, find two sequences with different f(x_n) values
- Outro with play_outro(), teasing next video "Continuity"
**Content:** "Six things to remember. The epsilon-delta definition makes the idea of f of x approaching L mathematically precise. The quantifier order is crucial: for every epsilon, there exists a delta. Epsilon is given to you, and you must find the matching delta. The limit at a point does not depend on the function value at that point. The sequential characterization says a function limit exists if and only if every sequence converging to a gives f of x sub n converging to L. And to prove a limit does not exist, just find two sequences approaching a that give different outputs. Next time, we use limits to define continuity."
**Elements:** Takeaways (progressive reveal, max 5), outro
**Content budget:** Progressive reveal
