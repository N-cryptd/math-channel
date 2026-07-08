# Video 105: The Derivative (Rigorous)

**Playlist:** Real Analysis I (Video 7 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video105_DerivativeRigorous
**Script:** scripts/undergraduate/video-105-derivative-rigorous.py

## Prerequisites
- Video 102: Limits of Functions (epsilon-delta definition)
- Video 103: Continuity (epsilon-delta, sequential criterion, types of discontinuity)
- Video 104: Uniform Continuity (Heine-Cantor, Lipschitz hierarchy)
- Videos 99-101: Real Numbers, Sequences, Cauchy Sequences
- Videos 90-98: Introduction to Proofs (complete)

## Learning Objectives
1. Rigorous definition of the derivative as a limit of difference quotients
2. Prove that differentiability implies continuity (and the converse fails via |x| at 0)
3. Derive standard derivative rules from the limit definition (linearity, product rule)
4. Discuss differentiability on intervals and one-sided derivatives
5. Connect to Lipschitz condition: differentiable on [a,b] with bounded derivative => Lipschitz => uniformly continuous

## Competitive Analysis References
- **3Blue1Brown (8.46M subs):** "The paradox of the derivative" (4.38M views). Gold standard secant-to-tangent animation, speedometer metaphor. Rating: 10/10 across all dimensions. BUT: calculus-level, no rigor, no proofs. We adopt the secant-to-tangent visual and build rigor on top.
- **Michael Penn (350K subs):** "Real Analysis | Introduction to differentiability" (31.7K views, 11:46). Whiteboard, defines differentiability, example (x^2), non-example (|x| at 0), proves diff=>cont. Rating: Structure 8, Pacing 6, Visuals 3, Narration 7, Hooks 4. Adopt: proof rigor, example/non-example structure. Avoid: starting with algebra without geometric intuition.
- **Michael Penn (350K subs):** "Real Analysis | Derivative Rules" (15.6K views, 14:24). Derives product, quotient, chain rules from limit definition. Rating: Structure 8, Pacing 5, Visuals 3, Narration 7, Hooks 4. Adopt: systematic rule derivations. Avoid: dense algebra walls without breathing room.
- **The Bright Side of Mathematics (233K subs):** "Real Analysis 34 | Differentiability" (22.8K views, 10:50). Tablet writing, builds from slope/secant/tangent to formal definition. Rating: Structure 8, Pacing 7, Visuals 5, Narration 7, Hooks 5. Adopt: progressive intuition-to-rigor build.

**Key gap:** No competitor animates the rigorous real analysis treatment of derivatives with Manim. The secant-to-tangent animation, diff=>cont proof, and Lipschitz cascade are all highly visual yet remain stuck on whiteboards.

## Scene Plan (11 scenes, ~14 min target)

### Scene 1: Hook — From Secant to Tangent (~60s)
**Visual:** Animated secant line on a curve, sliding closer to a fixed point, converging to the tangent line. The difference quotient displayed and updating live.
- Start with a curve (e.g., x^2) and two points: (a, f(a)) and (a+h, f(a+h))
- Draw the secant line through both points
- Animate h shrinking -> secant rotates toward tangent
- Display the difference quotient: [f(a+h) - f(a)] / h
- "In calculus, you learned that the derivative is the slope of the tangent line."
- "Today we make this rigorous: the derivative as a limit of difference quotients."
**Elements:** Graph with animated secant/tangent, difference quotient formula
**Content budget:** 3 elements max (graph + formula + title)

### Scene 2: Intro + Section Divider (~15s)
**Visual:** Channel intro, then section divider.
- play_intro("The Derivative (Rigorous)", "Real Analysis I")
- Section divider: "1 — The Formal Definition"

### Scene 3: Formal Definition (~90s)
**Visual:** Progressive reveal of the formal definition with geometric motivation.
- Recall: slope of secant = [f(a+h) - f(a)] / h
- "The derivative is the limit of this slope as h approaches 0."
- Formal definition:
  - f is differentiable at a if the limit as h -> 0 of [f(a+h) - f(a)] / h exists and is finite
  - Denote this limit as f'(a)
- Equivalent form: limit as x -> a of [f(x) - f(a)] / (x - a)
- "Key: the limit must exist and be finite. Both the left-hand and right-hand limits must agree."
- Color-code: f(a+h) in PRIMARY, f(a) in SECONDARY, h in ACCENT
**Elements:** Definition box (progressive reveal), equivalent form note
**Content budget:** 4 elements max

### Scene 4: Section Divider (~5s)
**Visual:** Section divider "2 — Differentiable Implies Continuous"

### Scene 5: Theorem + Proof Sketch (~120s)
**Visual:** Two-part scene. Part 1: geometric motivation. Part 2: algebraic proof.
- Part 1: Geometric
  - "Theorem: If f is differentiable at a, then f is continuous at a."
  - Animated: show the secant on f, as h -> 0, not only does the slope approach f'(a), but f(a+h) -> f(a)
  - "If the tangent line exists, the function can't have a jump."
- Part 2: Algebraic proof
  - Need to show: limit as x -> a of f(x) = f(a)
  - Strategy: write f(x) - f(a) = [f(x) - f(a)] / (x - a) * (x - a)
  - = [difference quotient] * (x - a)
  - As x -> a: first factor -> f'(a) (exists by hypothesis), second factor -> 0
  - Product -> f'(a) * 0 = 0
  - Therefore f(x) -> f(a). QED.
- "The proof is elegant: we factor the continuity check into a product of two things we know."
**Elements:** Theorem box, animated secant/tangent, proof steps (progressive)
**Content budget:** Progressive reveal, max 5

### Scene 6: Section Divider (~5s)
**Visual:** Section divider "3 — The Converse Fails"

### Scene 7: Counterexample — |x| at x=0 (~100s)
**Visual:** Graph of |x| with animated left/right secants approaching different slopes.
- "The converse is false. Continuous does NOT imply differentiable."
- "The classic counterexample: f(x) = |x| at x = 0."
- Show the graph: V-shape
- Animate right secant (h > 0): slope approaches +1
- Animate left secant (h < 0): slope approaches -1
- "The left and right limits disagree: +1 vs -1. The derivative does not exist."
- "Visually: the graph has a corner. No unique tangent line."
- "Continuity holds: limit as x -> 0 of |x| = 0 = f(0). But differentiability fails."
- Mention: other examples (Weierstrass function is continuous everywhere but differentiable nowhere, but that's beyond our scope)
**Elements:** |x| graph, animated secants, slope values, conclusion text
**Content budget:** 4 elements max

### Scene 8: Section Divider (~5s)
**Visual:** Section divider "4 — Derivative Rules from the Definition"

### Scene 9: Linearity and Product Rule (~120s)
**Visual:** Animated derivations of key rules from the limit definition.
- "All the derivative rules you know from calculus can be PROVED from the limit definition."
- **Linearity** (sum/difference rule):
  - (f + g)'(a) = lim [f(a+h) + g(a+h) - f(a) - g(a)] / h
  - = lim [f(a+h) - f(a)] / h + lim [g(a+h) - g(a)] / h  (limit laws!)
  - = f'(a) + g'(a)
  - "The sum rule is just the limit law for sums applied to difference quotients."
- **Scalar multiple:** (cf)'(a) = c * f'(a) (same idea)
- **Product Rule** (sketch):
  - (fg)'(a) = lim [f(a+h)g(a+h) - f(a)g(a)] / h
  - Add and subtract f(a+h)g(a):
  - = lim [f(a+h)g(a+h) - f(a+h)g(a) + f(a+h)g(a) - f(a)g(a)] / h
  - = lim f(a+h) * [g(a+h) - g(a)] / h + lim [f(a+h) - f(a)] / h * g(a)
  - = f(a) * g'(a) + f'(a) * g(a)
  - "The product rule: the derivative of the product is NOT the product of derivatives."
- Color-code each step to show the algebraic manipulation clearly
**Elements:** Rule derivations with progressive reveal, color-coded terms
**Content budget:** Progressive reveal, max 5

### Scene 10: Section Divider + Differentiability on Intervals (~90s)
**Visual:** Section divider "5 — Differentiability on Intervals and the Lipschitz Connection"
- Define: f is differentiable on (a,b) if f is differentiable at every point in (a,b)
- Define: f is differentiable on [a,b] if the one-sided derivatives exist at the endpoints
  - f'_+(a) = lim as h->0+ of [f(a+h) - f(a)] / h
  - f'_-(b) = lim as h->0- of [f(b+h) - f(b)] / h
- **Lipschitz Connection** (key result, connecting to Video 104):
  - "Theorem: If f is differentiable on [a,b] and |f'(x)| <= M for all x, then f is Lipschitz on [a,b]."
  - Sketch: By the Mean Value Theorem (preview), for any x, y in [a,b]:
    - |f(x) - f(y)| = |f'(c)| * |x - y| <= M * |x - y|  for some c between x and y
  - "Lipschitz with constant M means the function can't change faster than rate M."
  - **Cascade:** Differentiable (bounded derivative) -> Lipschitz -> Uniformly Continuous -> Continuous
  - This is exactly the hierarchy from Video 104, now with differentiability at the top!
  - Animate the cascade diagram building from Video 104's hierarchy
**Elements:** Interval definitions, one-sided derivative notation, Lipschitz theorem, cascade diagram
**Content budget:** Progressive reveal, max 5

### Scene 11: Summary + Outro (~50s)
**Visual:** Key takeaways as progressive reveal, then outro.
- Key takeaways:
  1. Derivative = limit of difference quotients [f(a+h) - f(a)] / h as h -> 0
  2. Differentiable at a point => continuous at that point (converse fails: |x| at 0)
  3. All derivative rules follow from the limit definition using limit laws
  4. On a closed interval, bounded derivative => Lipschitz => uniformly continuous
  5. Next: the Mean Value Theorem and its consequences
- play_outro("The Mean Value Theorem", "Real Analysis I")
**Elements:** 5 takeaway items, outro
**Content budget:** 5 items max

## Visual Design Notes
- Secant-to-tangent animation: the centerpiece visual. Use PRIMARY color for secant, SECONDARY for tangent, show convergence with a smooth animation
- |x| counterexample: LEFT slope in RED, RIGHT slope in PRIMARY, corner highlighted with ACCENT
- Product rule derivation: color-code the "add and subtract" trick so viewers can track the algebra
- Hierarchy cascade: build from Video 104's Lipschitz -> Uniform -> Continuous, add Differentiable on top
- Graphs: use axes with light gridlines, consistent with Videos 102-104 style
