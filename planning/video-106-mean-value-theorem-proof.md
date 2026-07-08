# Video 106: Mean Value Theorem (Proof)

**Playlist:** Real Analysis I (Video 8 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video106_MeanValueTheoremProof
**Script:** scripts/undergraduate/video-106-mean-value-theorem-proof.py

## Prerequisites
- Video 99: The Real Numbers (Completeness, sup/inf)
- Video 100: Sequences and Convergence
- Video 101: Cauchy Sequences
- Video 102: Limits of Functions (epsilon-delta)
- Video 103: Continuity (epsilon-delta, Extreme Value Theorem)
- Video 104: Uniform Continuity (Heine-Cantor, Lipschitz)
- Video 105: The Derivative (Rigorous) — differentiable => continuous, derivative rules
- Videos 90-98: Introduction to Proofs (complete)

## Learning Objectives
1. State and prove Fermat's Theorem (local extremum => f'(c) = 0)
2. State and prove Rolle's Theorem (equal endpoints => horizontal tangent)
3. State and prove the Mean Value Theorem via the auxiliary function h(x) = f(x) - L(x)
4. Understand WHY the auxiliary function works — geometric construction
5. Verify conditions are necessary with counterexamples
6. Apply MVT consequences: f'=0 => f constant, monotonicity, Lipschitz connection

## Competitive Analysis References
Analysis completed 2026-07-08 in channel-analysis/improvements.md (lines 1024-1332). Key findings:

**Market gap:** NO competitor provides a full Manim-animated proof of the MVT with visual geometric intuition. All use whiteboard/tablet.

**Key sources analyzed:** Michael Penn (25K views, whiteboard), Bright Side of Mathematics (21K views, tablet), Dr. Gajendra Purohit (839K views, chalkboard), Organic Chemistry Tutor (1.56M views, calculus-level, no proof), Dr. Trefor Bazett (35K views, counterexamples), bprp (17K views, MVT inequality applications), Bill Kinney (5K views, 34-min lecture).

**Techniques to adopt:**
- Trefor's counterexamples showing why conditions are necessary
- Bright Side's geometric-meaning-first approach
- bprp's inequality application (sqrt(1+x) < 1 + x/2)
- Bill Kinney's proof deconstruction strategy

**Our unique contribution:** Animated auxiliary function construction — no competitor visualizes h(x) = f(x) - L(x). We show the secant line being "subtracted" from f(x) to reveal h(x) with h(a)=h(b)=0, making Rolle's application visually obvious.

## Scene Plan (10 scenes, ~12 min target)

### Scene 1: Hook — The Driving Intuition (~45s)
**Visual:** Distance vs time graph with a car traveling from point A to point B. Secant line shows average speed. At some point, instantaneous speed equals average speed — the tangent equals the secant.
- "Imagine driving 120 miles in 2 hours. Average speed: 60 mph."
- "At some moment, your speedometer must have read exactly 60 mph."
- Show distance vs time curve, secant line (average speed), tangent line touching at one point with same slope
- "The Mean Value Theorem proves this is always true for nice functions."
- Color-code: curve in PRIMARY, secant in SECONDARY, tangent in ACCENT
**Elements:** Graph with car analogy, secant/tangent lines (max 4 visible)
**Content budget:** 4 elements max

### Scene 2: Intro + Section Divider (~15s)
**Visual:** Channel intro, then section divider.
- play_intro("Mean Value Theorem (Proof)", "Real Analysis I")
- Section divider: "1 — Fermat's Theorem"

### Scene 3: Fermat's Theorem — Statement + Proof (~90s)
**Visual:** Statement then animated proof sketch.
- "Before MVT, we need two building blocks. First: Fermat's Theorem."
- Statement: If f has a local extremum at c in (a,b) and f'(c) exists, then f'(c) = 0
- Graph: function with a local maximum at interior point c
- Proof sketch:
  - If f has local max at c: f(c+h) <= f(c) for small h
  - For h > 0: [f(c+h) - f(c)] / h <= 0, so limit as h->0+ <= 0
  - For h < 0: [f(c+h) - f(c)] / h >= 0, so limit as h->0- >= 0
  - Both one-sided limits equal f'(c), so f'(c) = 0
- Color-code: local max point in ACCENT, one-sided quotients in PRIMARY/RED
**Elements:** Theorem box, graph, proof steps (progressive reveal, max 5)
**Content budget:** 5 elements max

### Scene 4: Rolle's Theorem — Statement + Proof (~120s)
**Visual:** Statement with geometric motivation, then proof.
- Section divider: "2 — Rolle's Theorem"
- Statement: If f is continuous on [a,b], differentiable on (a,b), and f(a) = f(b), then exists c in (a,b) with f'(c) = 0
- Geometric picture: function starts and ends at same height — must have a horizontal tangent somewhere
- Animate: mark equal heights, show horizontal tangent point
- Proof:
  - By Extreme Value Theorem (Video 103): f attains max M and min m on [a,b]
  - Case 1: M = m => f is constant => f'(c) = 0 everywhere
  - Case 2: M > m => at least one extreme at interior point c in (a,b)
    - If f attains M at c in (a,b): f'(c) = 0 by Fermat's Theorem
    - If f attains m at c in (a,b): f'(c) = 0 by Fermat's Theorem
- Color-code: max in ACCENT, min in SECONDARY, Fermat reference in PRIMARY
**Elements:** Statement, graph, proof steps (progressive reveal, max 5)
**Content budget:** 5 elements max

### Scene 5: MVT Statement (~45s)
**Visual:** Formal statement with conditions highlighted.
- Section divider: "3 — The Mean Value Theorem"
- Theorem statement:
  - If f is continuous on [a,b] and differentiable on (a,b)
  - Then there exists c in (a,b) such that f'(c) = [f(b) - f(a)] / (b - a)
- Color-code conditions: "continuous" in PRIMARY, "differentiable" in SECONDARY, conclusion in ACCENT
- Visual: the secant line slope equals some tangent slope
**Elements:** Theorem box with highlighted conditions, graph showing secant line
**Content budget:** 3 elements max

### Scene 6: The Key Insight — Auxiliary Function (~120s)
**Visual:** Animated construction of h(x) = f(x) - L(x). This is our unique contribution.
- "The proof strategy: construct an auxiliary function that satisfies Rolle's conditions."
- Step 1: Show f(x) on graph with points (a, f(a)) and (b, f(b))
- Step 2: Draw the secant line L(x) = f(a) + [(f(b)-f(a))/(b-a)](x-a) through both endpoints
- Step 3: "Subtract the secant from f(x)" — animate L(x) moving down/away, revealing h(x) = f(x) - L(x)
- Step 4: Show h(a) = f(a) - L(a) = f(a) - f(a) = 0 and h(b) = f(b) - L(b) = f(b) - f(b) = 0
- "h(a) = h(b) = 0! Rolle's Theorem applies!"
- Color-code: f in PRIMARY, L(x) in SECONDARY, h(x) in ACCENT, zeros in RED
**Elements:** Graph with f, L, h animated step-by-step (max 4 at any time)
**Content budget:** 4 elements max per sub-step

### Scene 7: MVT Formal Proof (~90s)
**Visual:** Step-by-step algebraic proof.
- "Now the formal proof, connecting to the picture we just built."
- Define h(x) = f(x) - f(a) - [(f(b)-f(a))/(b-a)](x-a)
- Verify: h is continuous on [a,b] (difference of continuous functions)
- Verify: h is differentiable on (a,b) (difference of differentiable functions)
- Verify: h(a) = 0, h(b) = 0 (direct computation)
- Apply Rolle's Theorem: exists c in (a,b) with h'(c) = 0
- h'(x) = f'(x) - [(f(b)-f(a))/(b-a)]
- h'(c) = 0 => f'(c) = [f(b)-f(a)]/(b-a). QED.
- Color-code each step to match Scene 6's visual
**Elements:** Proof steps (progressive reveal, max 5)
**Content budget:** 5 elements max

### Scene 8: Why Conditions Matter — Counterexamples (~60s)
**Visual:** Two counterexample graphs (following Trefor's approach).
- "Both conditions are necessary. Without them, the theorem fails."
- Counterexample 1: f not continuous on [a,b] — jump discontinuity
  - Show broken graph with secant line, tangent lines never match secant slope
  - Mark the discontinuity point in RED
- Counterexample 2: f not differentiable at one point (e.g., |x|-like corner)
  - Show graph with corner, secant line, no tangent with matching slope at any point
  - Mark the non-differentiable point in RED
- "The MVT requires BOTH continuity and differentiability."
**Elements:** Two counterexample graphs with labels (max 3 per sub-step)
**Content budget:** 3 elements max per sub-step

### Scene 9: Consequences and Applications (~90s)
**Visual:** Three key consequences, revealed progressively.
- "The MVT has powerful consequences."
- Consequence 1: f'(x) = 0 for all x in interval => f is constant
  - Proof: For any a, b: f(b) - f(a) = f'(c)(b-a) = 0 * (b-a) = 0
  - "Derivative zero everywhere means the function never changes."
- Consequence 2: f'(x) > 0 => f is strictly increasing
  - Proof: For a < b: f(b) - f(a) = f'(c)(b-a) > 0
  - "Positive derivative means strictly increasing. Negative means strictly decreasing."
- Consequence 3: Lipschitz connection (connect to Video 104)
  - |f'(x)| <= M => |f(x) - f(y)| <= M|x-y| (from MVT)
  - "Bounded derivative implies Lipschitz — we previewed this in Video 105."
- Color-code: consequence 1 in PRIMARY, 2 in SECONDARY, 3 in ACCENT
**Elements:** Three consequence blocks (progressive reveal, max 5)
**Content budget:** 5 elements max

### Scene 10: Summary + Outro (~45s)
**Visual:** Key takeaways as progressive reveal, then outro.
- Proof dependency chain: Fermat's Theorem -> Rolle's Theorem -> Mean Value Theorem
- Key takeaways:
  1. MVT: exists c in (a,b) with f'(c) = [f(b)-f(a)]/(b-a]
  2. Proof via auxiliary function h(x) = f(x) - L(x) + Rolle's Theorem
  3. Both conditions (continuity + differentiability) are necessary
  4. f'=0 => f constant; f'>0 => f increasing; bounded f' => Lipschitz
  5. Next: The Riemann Integral
- play_outro("The Riemann Integral", "Real Analysis I")
**Elements:** Chain diagram + 4 takeaway items (progressive reveal)
**Content budget:** 5 items max

## Visual Design Notes
- **Secant-to-tangent animation (Scene 1):** Reuse the secant convergence technique from Video 105 but for the average speed interpretation. PRIMARY for curve, SECONDARY for secant, ACCENT for tangent.
- **Auxiliary function construction (Scene 6):** The centerpiece visual. Animate f(x), then overlay L(x), then "subtract" to show h(x). This is our unique competitive advantage — no one else animates this.
- **Proof chain diagram (Scene 10):** Arrow diagram: Fermat -> Rolle -> MVT, building left to right. PRIMARY arrows, ACCENT nodes.
- **Counterexamples (Scene 8):** Two-panel comparison or sequential reveal. Discontinuity/corner points highlighted with pulsing RED dots.
- **Color coding throughout:** Continuity = PRIMARY, Differentiability = SECONDARY, Conclusions = ACCENT, Warnings/Failures = RED.
