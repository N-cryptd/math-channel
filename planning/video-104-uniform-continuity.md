# Video 104: Uniform Continuity

**Playlist:** Real Analysis I (Video 6 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video104_UniformContinuity
**Script:** scripts/undergraduate/video-104-uniform-continuity.py

## Prerequisites
- Video 102: Limits of Functions (epsilon-delta definition)
- Video 103: Continuity (epsilon-delta, sequential criterion, types of discontinuity)
- Videos 99-101: Real Numbers, Sequences, Cauchy Sequences
- Videos 90-98: Introduction to Proofs (complete)

## Learning Objectives
1. Understand the key difference between pointwise and uniform continuity
2. State the formal definition: for every epsilon, ONE delta works for ALL x simultaneously
3. Prove that continuous on a closed interval implies uniform continuity (Heine-Cantor theorem sketch)
4. Show examples of continuous but not uniformly continuous functions (1/x on (0,1), x^2 on R)
5. Connect to Lipschitz continuity as a stronger condition

## Competitive Analysis References
- **Dr. Trefor Bazett (606K subs):** Uses Manim animations. Strong visual intuition for delta-epsilon, clear comparison of pointwise vs uniform. Typically ~10-12 min. Covers Heine-Cantor with a visual compactness argument. Rating: Structure 8/10, Pacing 7/10, Visuals 8/10, Narration 7/10, Hooks 6/10.
- **Michael Penn (349K subs):** Pen-and-paper whiteboard. Systematic, proof-heavy. Walks through formal proofs step by step. Less visual, more rigorous. Rating: Structure 9/10, Pacing 6/10, Visuals 3/10, Narration 7/10, Hooks 4/10.
- **Wrath of Math (241K+ views):** Lecture with annotated slides. Covers the 1/x counterexample well. Structured but static. Rating: Structure 7/10, Pacing 5/10, Visuals 4/10, Narration 6/10, Hooks 5/10.
- **Dr. Peyam (Active):** Enthusiastic style, thorough coverage. Often 20+ min. Very detailed proofs. Rating: Structure 7/10, Pacing 5/10, Visuals 3/10, Narration 8/10, Hooks 6/10.

**Key gap:** No competitor provides a compelling ANIMATED visualization of the key difference: in pointwise continuity, delta depends on BOTH epsilon and the point x=a. In uniform continuity, delta depends ONLY on epsilon. We will visually show multiple points on a curve each needing their own delta (pointwise) vs. ONE delta that works everywhere (uniform).

**Our unique edges:**
- Animated comparison: show 3 points on f(x)=x^2 each with their own shrinking delta tube (pointwise), then contrast with ONE tube that works everywhere (uniform)
- 1/x on (0,1): animate what happens as x approaches 0 — delta must shrink to zero — no single delta works for all points
- Heine-Cantor: visual proof sketch using finite subcover idea (compactness)
- Lipschitz connection: visual slope comparison showing Lipschitz implies uniform continuity

## Scene Plan (10 scenes, ~13 min target)

### Scene 1: Hook — Same Word, Different Meaning (~55s)
**Visual:** Show the epsilon-delta definition from Video 103, then highlight the key: "delta can depend on a."
- Display the continuity definition: for every epsilon > 0, there exists delta > 0 such that |x - a| < delta implies |f(x) - f(a)| < epsilon
- Highlight "delta" and "a" in different colors
- "Last time we defined continuity at a point. The delta we found depended on BOTH epsilon and the point a."
- "What if we need ONE delta that works for EVERY point simultaneously?"
- "That is uniform continuity — and it changes everything."
**Elements:** Definition box, highlighted labels, question text
**Content budget:** 4 elements max

### Scene 2: Intro + Section Divider (~15s)
**Visual:** Channel intro, then section divider.
- play_intro("Uniform Continuity", "Real Analysis I")
- Section divider: "1 — Pointwise vs Uniform"

### Scene 3: Visual Comparison — Pointwise Continuity (~90s)
**Visual:** f(x) = x^2 with three marked points, each needing their own delta.
- Show f(x) = x^2 with points at x=1, x=3, x=5
- At x=1 (gentle slope): large delta works
- At x=3 (steeper): smaller delta needed
- At x=5 (steepest): even smaller delta
- "For pointwise continuity: at each point, we find a delta that depends on BOTH the point and epsilon."
- "Near x=5, the function changes fast. Near x=1, it changes slowly."
- "Different points need different deltas. This is fine for pointwise continuity."
- Key visual: three delta tubes of different widths at the three points
**Elements:** Graph with 3 marked points, 3 delta tubes, labels
**Content budget:** Progressive reveal, max 5

### Scene 4: Section Divider (~5s)
**Visual:** Section divider "2 — The Definition"

### Scene 5: Formal Definition + Visual (~120s)
**Visual:** Side-by-side definitions, then animated uniform delta tube.
- Left column: Pointwise definition (epsilon depends on a)
- Right column: Uniform definition (delta depends on epsilon ONLY)
- Key change highlighted: "exists delta > 0" where delta works "for ALL x in the domain"
- Formal definition:
  - f is uniformly continuous on S if for every epsilon > 0, there exists delta > 0 such that for ALL x,y in S, |x - y| < delta implies |f(x) - f(y)| < epsilon
- Animated: show ONE delta tube that slides across the entire function — it always maps inside the epsilon-band
- "Notice: we use x and y (two arbitrary points), not x and a (a fixed point). Uniform continuity is about pairs of points."
**Elements:** Two-column definitions, animated sliding tube
**Content budget:** Progressive reveal, max 5

### Scene 6: Section Divider (~5s)
**Visual:** Section divider "3 — Continuous but Not Uniformly Continuous"

### Scene 7: Counterexample — f(x) = 1/x on (0,1) (~120s)
**Visual:** Graph of 1/x on (0,1), animated delta tubes shrinking near 0.
- "The classic counterexample: f(x) = 1/x on the open interval (0,1)."
- Show the graph: steep near 0, gentle near 1
- "This function IS continuous at every point in (0,1). But is it UNIFORMLY continuous?"
- Pick epsilon = 1. Show that near x = 0.01, we need delta < 0.0001
- "As x approaches 0, the required delta shrinks to zero. No single delta works for the entire interval."
- Animated: slide the delta tube rightward — it fits. Slide it leftward toward 0 — it breaks.
- "The problem: the open interval (0,1) is not closed. The function is unbounded near 0."
- Second example mention: f(x) = x^2 on ALL of R — also not uniformly continuous (same idea, slope grows without bound)
**Elements:** Graph of 1/x, animated tube, insight text
**Content budget:** Progressive reveal, max 5

### Scene 8: Section Divider (~5s)
**Visual:** Section divider "4 — Heine-Cantor Theorem"

### Scene 9: Heine-Cantor Theorem Sketch + Lipschitz (~120s)
**Visual:** Two-part scene. Part 1: theorem + proof sketch. Part 2: Lipschitz connection.
- Part 1: Heine-Cantor Theorem
  - "Theorem: If f is continuous on a CLOSED and BOUNDED interval [a,b], then f is uniformly continuous on [a,b]."
  - Proof sketch:
    - "By continuity, each point c in [a,b] has its own delta(c)."
    - "These delta-neighborhoods form an open cover of [a,b]."
    - "By the Heine-Borel theorem, a finite subcover exists: delta_1, delta_2, ..., delta_n."
    - "Take delta = the minimum of all these deltas. This ONE delta works everywhere."
  - Key insight: "Compactness guarantees that infinitely many local deltas reduce to a single global delta."
- Part 2: Lipschitz Continuity
  - "A stronger condition: f is Lipschitz on S if there exists a constant L such that |f(x) - f(y)| <= L times |x - y| for all x, y."
  - "Lipschitz implies uniformly continuous: just take delta = epsilon / L."
  - Visual: show a "slope comparison" — Lipschitz means the function never changes faster than rate L
  - Examples: |x| is Lipschitz (L=1), x^2 is not Lipschitz on R (slope grows), but IS Lipschitz on any bounded interval
  - Hierarchy: Lipschitz -> Uniformly Continuous -> Continuous
**Elements:** Theorem box, proof sketch (progressive), hierarchy diagram
**Content budget:** Progressive reveal, max 5

### Scene 10: Summary + Outro (~50s)
**Visual:** Key takeaways as progressive reveal, then outro.
- Key takeaways:
  - Pointwise continuity: delta depends on epsilon AND the point
  - Uniform continuity: ONE delta works for ALL points
  - 1/x on (0,1): continuous but NOT uniformly continuous
  - Heine-Cantor: continuous on [a,b] implies uniformly continuous
  - Hierarchy: Lipschitz -> Uniform -> Pointwise
- Outro with play_outro(), teasing next video "The Derivative (Rigorous)"
**Elements:** Takeaways (progressive reveal, max 5), outro
**Content budget:** Progressive reveal
