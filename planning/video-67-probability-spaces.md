# Video 67: Probability Spaces

**Playlist:** Probability & Statistics (Video 1 of 12)
**Estimated duration:** 11 min
**Script file:** `scripts/undergraduate/video-67-probability-spaces.py`
**Class name:** `Video67_ProbabilitySpaces`
**Status:** PLANNING → SCRIPTING

## Competitive Analysis Insights

### 3Blue1Brown — Bayes theorem, the geometry of changing beliefs
- **Approach:** Uses geometric area model — probabilities as areas of rectangles. Not about probability spaces directly, but his visual philosophy is the gold standard.
- **Key insight to adopt:** Represent probabilities as areas/regions. Omega as a unit square, events as shaded regions. This geometric intuition makes the axioms feel natural, not arbitrary.

### Dr. Trefor Bazett — Introduction to probability
- **Approach:** Clean structure: sample space → events → probability formula → examples → independence. Introduces the (Omega, F, P) triple. Colored Venn diagrams.
- **Key insight to adopt:** The formal triple as a "framework" concept. Clean transition from informal "chance of" language to formal notation.

### Organic Chemistry Tutor — Intro to Probability, Sample Space, Tree Diagrams
- **Approach:** Whiteboard-only, 17 min, 3.8M views. Massive demand, low production quality. Covers many examples but no animations.
- **Key insight to adopt:** Equally-likely outcomes as a bridge from counting to probability. Simple examples (coins, dice) build quick intuition.

### MIT OCW — L01.4 Probability Axioms
- **Approach:** Formal lecture (Tsitsiklis), covers Kolmogorov axioms rigorously, derives consequences. Low visual appeal.
- **Key insight to adopt:** Derive consequences (P(empty)=0, complement rule) from axioms to show their power. Present axioms as "foundation rules."

### Khan Academy — Probability explained
- **Approach:** Real-world motivation first, simple visuals, modular format. Accessible but never reaches formalism.
- **Key insight to adopt:** "Why do we care?" before definitions. Simple clear language for new terminology.

### Our Approach (Synthesis)
- **Structure:** Opening puzzle → Sample spaces (Omega) → Events as subsets → Kolmogorov axioms → Consequences → Worked example → Summary
- **Visual metaphors:** (1) Omega as a unit rectangle divided into colored regions (3B1B-style area model), (2) Events as shaded subsets within Omega, (3) Axioms as "building blocks" that animate into place
- **Color scheme:** PRIMARY (#5BC0EB) for Omega/sample space, SECONDARY (#7BC950) for events, ACCENT (#FFD166) for axioms/key results, RED (#EF476F) for complement/warnings

## Scene Breakdown

### Scene 1: Hook — The Coin Puzzle (50s)
**Narration:** "Flip a fair coin ten times. What is the probability of getting at least one head? Most people try to count the favorable outcomes. But there's a much easier way."
- Content budget: 4 items
- play_intro("Probability Spaces", "Probability & Statistics")
- Title: "The Coin Puzzle"
- Visual: 10 coin icons arranged in a row, some H some T
- Question: MathTex for P(at least one H in 10 flips)
- Key insight: "It's easier to find the probability of NO heads, then subtract from 1"
- Result: 1 - (1/2)^10 ≈ 0.999 — almost certain!
- Transition: "To understand why this works, we need a proper framework"
- ly.clear()

### Scene 2: Sample Spaces (90s)
**Narration:** "Every probability question starts with a sample space. The sample space Omega is the set of all possible outcomes of an experiment."
- Content budget: 5 items
- ly.section_divider(1, "Sample Spaces")
- Definition: Omega = set of all outcomes
- Example 1: Coin flip → Omega = {H, T}
- Example 2: Die roll → Omega = {1, 2, 3, 4, 5, 6}
- Visual: Two sample spaces shown side by side (Venn-style circles with elements)
- Key idea: "The sample space depends on how we define the experiment"
- ly.clear()

### Scene 3: Events (90s)
**Narration:** "An event is a subset of the sample space. Any collection of outcomes we care about is an event."
- Content budget: 5 items
- ly.section_divider(2, "Events")
- Definition: Event A ⊆ Omega
- Visual: Omega rectangle with shaded region labeled A
- Examples:
  - "Rolling an even number" = {2, 4, 6} ⊆ {1,2,3,4,5,6}
  - "Rolling a 7" = ∅ (impossible event)
  - "Rolling at least 1" = Omega (certain event)
- Special events: Omega itself (certain), ∅ (impossible)
- Complement: A^c = Omega \ A — show as the unshaded region
- ly.clear()

### Scene 4: The Probability Function (60s)
**Narration:** "A probability function P assigns a number between 0 and 1 to every event. P(A) = 1 means A is certain, P(A) = 0 means A is impossible."
- Content budget: 5 items
- ly.section_divider(3, "The Probability Function")
- The triple (Omega, F, P) displayed prominently with formula_box
- P: events → [0, 1]
- Visual: Omega rectangle with event A shaded; label shows P(A) = area of A / area of Omega
- For equally-likely outcomes: P(A) = |A| / |Omega| (count outcomes)
- "This is why probability connects to counting"
- ly.clear()

### Scene 5: Kolmogorov Axioms (120s)
**Narration:** "In 1933, Andrey Kolmogorov established three axioms that define probability. Every probability rule you've ever used follows from these three."
- Content budget: 5 items
- ly.section_divider(4, "Kolmogorov Axioms")
- Axiom 1: P(A) >= 0 for all events A (non-negativity)
- Axiom 2: P(Omega) = 1 (normalization)
- Axiom 3: If A ∩ B = ∅, then P(A ∪ B) = P(A) + P(B) (additivity)
- Each axiom animates in with an ACCENT-colored box
- Visual: Show Axiom 3 with two non-overlapping shaded regions in Omega
- Note: "These three rules are the entire foundation of probability theory"
- ly.clear()

### Scene 6: Consequences from the Axioms (90s)
**Narration:** "From just three axioms, we can derive powerful results. Let's prove the complement rule."
- Content budget: 5 items
- ly.section_divider(5, "Consequences")
- Consequence 1: P(∅) = 0
  - Proof sketch: A ∪ ∅ = A, so P(A) = P(A) + P(∅), therefore P(∅) = 0
- Consequence 2: P(A^c) = 1 - P(A)
  - Proof: A ∪ A^c = Omega, A ∩ A^c = ∅
  - P(A) + P(A^c) = P(Omega) = 1
  - Show with Venn diagram: A shaded + A^c shaded = whole Omega
- "This is exactly what we used in the coin puzzle!"
- Connect back to hook: 1 - P(no heads) = 1 - (1/2)^10
- ly.clear()

### Scene 7: Worked Example — Rolling Dice (90s)
**Narration:** "Let's put it all together with a concrete example. Roll two six-sided dice and find the probability that the sum is 7."
- Content budget: 5 items
- ly.section_divider(6, "Worked Example")
- Sample space: 36 equally likely outcomes (6x6 grid shown)
- Event A: sum = 7 → {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)} — 6 outcomes
- P(A) = 6/36 = 1/6
- Visual: 6x6 grid with the 6 winning cells highlighted in SECONDARY
- Bonus: Complement — P(sum != 7) = 1 - 1/6 = 5/6
- ly.clear()

### Scene 8: Summary and Outro (45s)
**Narration recap:** "Probability spaces give us a rigorous framework for reasoning about uncertainty."
- Key takeaways (progressive_reveal):
  1. Sample space Omega = all possible outcomes
  2. Events = subsets of Omega
  3. Probability function P maps events to [0, 1]
  4. Three axioms: non-negativity, normalization, additivity
  5. Everything else (complement rule, inclusion-exclusion) follows from the axioms
- play_outro() — tease "Next: Conditional Probability"
- ly.clear()

## Technical Notes
- Omega rectangle: use a RoundedRectangle or Rectangle as the visual "sample space" container
- Shaded regions: use VMobject with fill_opacity for events within Omega
- 6x6 dice grid: arrange 36 small squares in a grid, highlight winning cells
- Complement visualization: animate the "flip" of shaded ↔ unshaded regions
- Axiom boxes: use ly.formula_box() with ACCENT color for each axiom
- Keep formulas clean — single backslashes in raw strings
- Coin icons: can use Text("H") and Text("T") in small rounded rectangles
