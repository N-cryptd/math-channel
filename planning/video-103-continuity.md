# Video 103: Continuity (Epsilon-Delta Definition)

**Playlist:** Real Analysis I (Video 5 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video103_Continuity
**Script:** scripts/undergraduate/video-103-continuity.py

## Prerequisites
- Video 99: The Real Numbers (Completeness)
- Video 100: Sequences and Convergence (epsilon-N definition)
- Video 101: Cauchy Sequences
- Video 102: Limits of Functions (epsilon-delta definition)
- Videos 90-98: Introduction to Proofs (complete)

## Learning Objectives
1. Understand intuitively what it means for a function to be continuous at a point
2. State the formal epsilon-delta definition of continuity
3. Understand how continuity relates to the limit of a function: lim f(x) = f(a)
4. Prove continuity of basic functions (polynomials, |x|, etc.) using epsilon-delta
5. Understand the sequential criterion for continuity
6. Identify types of discontinuities: removable, jump, infinite, oscillation

## Competitive Analysis References
- Web search was unavailable for this cycle. Analysis is based on prior competitor knowledge.
- **Dr. Trefor Bazett (606K subs):** Covers continuity at calculus level with Manim-like animations. Strong hooks and visual intuition (9/10 engagement). Typically focuses on geometric intuition over rigorous proofs.
- **Michael Penn (349K subs):** Whiteboard, systematic proof-based approach (8/10 structure). Covers continuity proofs rigorously but lacks animation.
- **Wrath of Math (241K+ views):** Lecture with annotated slides. Covers epsilon-delta continuity proofs (7/10 structure, 4/10 visuals).
- **Key gap:** NO competitor fully animates the epsilon-delta definition of continuity on a function graph with the "tube" shrinking dynamically while showing the definition text simultaneously.
- **Our unique edges:**
  - Animated epsilon-delta "tube" on a continuous function, showing that the tube always maps inside the epsilon-band
  - Contrast with discontinuous function where the tube "breaks" at the discontinuity
  - Sequential criterion connecting back to Videos 100-101
  - Classification of discontinuities with visual examples for each type

## Scene Plan (10 scenes, ~14 min target)

### Scene 1: Hook — The Graph You Can Draw Without Lifting Your Pen (~60s)
**Visual:** Two function graphs — one smooth, one with a jump.
- Show f(x) = x^2 (smooth, continuous) alongside g(x) = sign(x) (jump at x=0)
- "In calculus, your teacher said: a function is continuous if you can draw its graph without lifting your pen."
- "That intuition is useful. But can we make it rigorous?"
- "What exactly does it mean for a function to have no 'breaks' at a point?"
- Transition to intro.
**Elements:** Two function graphs, question text
**Content budget:** 4 elements max

### Scene 2: Intro + Section Divider (~20s)
**Visual:** Channel intro animation, then section divider.
- play_intro("Continuity", "Real Analysis I")
- Section divider: "1 — From Limits to Continuity"

### Scene 3: The Key Idea — Continuity = Limit Equals Value (~90s)
**Visual:** Function graph with animated limit approaching f(a).
- "From our last video, we know how to define the limit of f(x) as x approaches a."
- "Continuity is beautifully simple: f is continuous at a if the limit equals the function value."
- Definition: "We say f is continuous at a if the limit as x approaches a of f(x) equals f(a)."
- Animate: show the limit value approaching f(a) on the y-axis, then show they coincide.
- Key insight: "The limit captures the PREDICTED value. Continuity says the prediction is correct."
- Three equivalent conditions (progressive reveal):
  1. lim_{x->a} f(x) = f(a)
  2. For every epsilon > 0, there exists delta > 0 such that |x - a| < delta implies |f(x) - f(a)| < epsilon
  3. For every sequence x_n -> a, we have f(x_n) -> f(a)
**Elements:** Graph, limit animation, definition box, key insight
**Content budget:** Progressive reveal, max 5

### Scene 4: Section Divider — Epsilon-Delta Definition (~5s)
**Visual:** Section divider "2 — The Formal Definition"

### Scene 5: Epsilon-Delta Definition — Animated (~120s)
**Visual:** Function graph with animated delta-tube and epsilon-band shrinking.
- Start with f(x) = x^2 at x = a = 2 (so f(a) = 4)
- "The formal definition: f is continuous at a if for every epsilon greater than zero, there exists a delta greater than zero, such that whenever the absolute value of x minus a is less than delta, the absolute value of f(x) minus f(a) is less than epsilon."
- Key difference from the limit definition: we use |x - a| < delta (includes x = a!) not 0 < |x - a| < delta
- "Notice: we removed the zero less than part! The limit excludes the point itself. Continuity INCLUDES it."
- Animate: show delta-tube (vertical band around x = a), show epsilon-band (horizontal band around f(a))
- Shrink epsilon, watch delta shrink. The tube always maps inside the band.
- Contrast: now show g(x) = |x|/x at x = 0. The tube can't map into any small epsilon-band.
- "This is what discontinuity LOOKS like: no matter how small delta is, the tube contains values far from the 'predicted' output."
**Elements:** Graph with delta-tube and epsilon-band, definition box, contrast with discontinuous function
**Content budget:** Progressive reveal, max 5

### Scene 6: Section Divider — Proof Example (~5s)
**Visual:** Section divider "3 — Proving Continuity"

### Scene 7: Proof — f(x) = x^2 is continuous at x = 2 (~120s)
**Visual:** Step-by-step proof with progressive reveal.
- Claim: "The function f(x) = x^2 is continuous at a = 2."
- Proof structure:
  - "Let epsilon greater than 0."
  - "Choose delta = min(1, epsilon / 5)."
  - "Suppose |x - 2| < delta."
  - "Then |f(x) - f(2)| = |x^2 - 4| = |x + 2| times |x - 2|"
  - "Since |x - 2| < delta <= 1, we have 1 < x < 3, so |x + 2| < 5."
  - "Therefore |f(x) - f(2)| < 5 times delta <= 5 times (epsilon / 5) = epsilon."
  - "Therefore |f(x) - f(2)| < epsilon. QED."
- Key insight box: "The min(1, epsilon/5) trick: we bound one factor by a constant, then use delta to control the other."
**Elements:** Claim, proof steps (progressive reveal), key insight box
**Content budget:** Progressive reveal, max 5 lines

### Scene 8: Section Divider — Sequential Criterion (~5s)
**Visual:** Section divider "4 — Sequences and Continuity"

### Scene 9: Sequential Criterion + Types of Discontinuity (~120s)
**Visual:** Two-part scene. Part 1: theorem. Part 2: classification.
- Part 1: Theorem
  - "Theorem: f is continuous at a if and only if for every sequence x_n converging to a, the sequence f(x_n) converges to f(a)."
  - "This follows directly from our limit sequential criterion and the definition of continuity."
- Part 2: Types of discontinuity (visual classification)
  - Removable: f(x) = (x^2 - 4)/(x - 2) at x = 2 — limit exists but f(a) is undefined
  - Jump: f(x) = |x|/x at x = 0 — left and right limits exist but differ
  - Infinite: f(x) = 1/x at x = 0 — limit is infinite
  - Oscillation: f(x) = sin(1/x) at x = 0 — no limit exists
- "In each case, the epsilon-delta definition FAILS. The tube doesn't map inside any epsilon-band."
**Elements:** Theorem, 4 mini-graphs showing each type (progressive reveal)
**Content budget:** Progressive reveal, max 5 at a time

### Scene 10: Summary + Outro (~60s)
**Visual:** Key takeaways as progressive reveal, then outro.
- Key takeaways:
  - Continuity means the limit equals the function value: lim f(x) = f(a)
  - The epsilon-delta definition includes x = a (unlike the limit definition)
  - The sequential criterion: f(x_n) -> f(a) whenever x_n -> a
  - There are four types of discontinuities: removable, jump, infinite, oscillation
  - Continuity is a LOCAL property — at each point individually
- Outro with play_outro(), teasing next video "Uniform Continuity"
**Narration:** "Five things to remember. Continuity means the limit of f of x as x approaches a equals f of a. The function's predicted value at a matches its actual value. In the epsilon-delta definition, we include x equals a, unlike the limit definition which excludes it. The sequential criterion says f is continuous at a if and only if for every sequence converging to a, f of x sub n converges to f of a. There are four types of discontinuities: removable, where the limit exists but the function value doesn't match; jump, where left and right limits differ; infinite, where the function blows up; and oscillation, where the function oscillates wildly. And continuity is a local property, defined point by point. Next time, we explore uniform continuity, where continuity is global."
**Elements:** Takeaways (progressive reveal, max 5), outro
**Content budget:** Progressive reveal
