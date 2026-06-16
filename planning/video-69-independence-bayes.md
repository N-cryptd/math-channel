# Video 69: Independence and Bayes' Theorem

**Playlist:** Probability & Statistics (Video 3 of 12)
**Duration target:** 12-14 minutes
**Script file:** `scripts/undergraduate/video-69-independence-bayes.py`
**Class name:** `Video69_IndependenceBayes`
**Status:** PLANNING -> SCRIPTING

## Competitive Analysis Reference
- See `channel-analysis/improvements.md` sections on 3B1B Bayes (HZGCoVF3YvM), conditional probability (Video 68 analysis)
- Key competitors analyzed:
  - **3Blue1Brown** "Bayes theorem, the geometry of changing beliefs" (5.76M views) -- area/rectangle model, medical test motivation, stunning visuals, 10/10 across all dimensions
  - **StatQuest** "Bayes' Theorem, Clearly Explained" (2.1M views) -- spam filter example, Bayesian vs Frequentist framing, punchy style
  - **Dr. Trefor Bazett** "Bayes' Theorem" (800K views) -- clean pedagogical style, covers independence as prerequisite
  - **Khan Academy** "Bayes' Theorem and Conditional Probability" (1.5M views) -- thorough but visually plain
  - **Organic Chemistry Tutor** "Independent Events Probability" (1.8M views) -- whiteboard, covers mutual independence briefly

### Competitive Gap
- No existing video covers BOTH independence AND Bayes' theorem in one place
- Independence videos are visually plain (whiteboard) while Bayes videos are visually rich -- Manim animations for independence would be distinctive
- Mutual independence is almost never covered on YouTube
- The connection between independence and Bayes is never explicitly made

## Scene Plan

### Scene 1: Hook -- The Coin Paradox (0:00-1:30, ~60s)
**Narration:** ~120 words, 60s
- "Flip a fair coin twice. You already know the first flip is heads. What's the probability the second flip is also heads? Most people say: it depends, or they think it's affected. But it's not -- it's still 1/2."
- "This is the simplest example of independence: knowing one event tells you nothing about the other."
- "But now imagine instead: flip two coins, and I tell you at least one is heads. What's the probability BOTH are heads? Most people say 1/2. The answer is actually 1/3."
- The contrast between the two questions is the hook -- independence vs. conditional reasoning
- **Content budget:** Title + question 1 + answer + question 2 + "the answer might surprise you" teaser
- **Animation:** Write title, two questions shown sequentially, answers revealed with Transform
- **Connects to:** Video 68's conditional probability definition

### Scene 2: Formal Definition of Independence (1:30-3:30, ~120s)
**Narration:** ~240 words, 120s
- Section divider: "Independence"
- "Two events A and B are independent if knowing whether B occurred tells us nothing about whether A occurred."
- Formal definition: P(A ∩ B) = P(A) * P(B)
- Equivalently: P(A|B) = P(A) -- "conditioning on B doesn't change A"
- Visual: Venn diagram with Omega rectangle, two overlapping events A and B
- Show area model: if A and B are independent, the overlap region has area = P(A) * P(B)
- Show how this derives from P(A|B) = P(A ∩ B)/P(B) = P(A), so P(A ∩ B) = P(A)*P(B)
- **Content budget:** section divider + definition box + Venn diagram + equivalence formula + intuition text (5 items max)
- **Animation:** Section divider, Venn diagram builds up, formula box with highlight, equivalence shown by Transform

### Scene 3: Independence Examples and Counterexamples (3:30-5:30, ~120s)
**Narration:** ~240 words, 120s
- Example 1: Two fair coin flips -- P(H₁) = 1/2, P(H₂) = 1/2, P(H₁ ∩ H₂) = 1/4 = (1/2)(1/2). Independent!
  - Visual: Two coins side by side, each landing H or T
- Example 2: Roll a die. A = "even number", B = "at least 4". Check: P(A) = 1/2, P(B) = 1/2, P(A ∩ B) = P({4,6}) = 1/3 ≠ 1/4. NOT independent!
  - Visual: Die face grid, highlight sets A, B, and A ∩ B
- Key insight: "Independence is NOT the same as 'mutually exclusive'. In fact, mutually exclusive events with positive probability are NEVER independent (because P(A ∩ B) = 0 ≠ P(A)*P(B))."
- Show the Venn diagram for the "not independent" case with unequal overlap
- **Content budget:** Two examples shown sequentially, each with max 4 items on screen, then key insight
- **Animation:** Coin example builds up, die example replaces it, key insight with RED highlight

### Scene 4: Pairwise vs. Mutual Independence (5:30-7:00, ~90s)
**Narration:** ~180 words, 90s
- Section divider: "Mutual Independence"
- "What about three events? We might think pairwise independence is enough."
- Definition: A, B, C are mutually independent if ALL of these hold:
  - P(A ∩ B) = P(A)*P(B)
  - P(A ∩ C) = P(A)*P(C)
  - P(B ∩ C) = P(B)*P(C)
  - P(A ∩ B ∩ C) = P(A)*P(B)*P(C)
- Warning (RED): Pairwise independence does NOT imply mutual independence!
- Counterexample: Two coin flips, define:
  - A = "first flip is heads"
  - B = "second flip is heads"
  - C = "both flips are the same" (HH or TT)
  - A and B independent? Yes. A and C? Yes (1/2 * 1/2 = 1/4). B and C? Yes.
  - But A ∩ B ∩ C = {HH}, P = 1/4 ≠ (1/2)^3 = 1/8. Not mutually independent!
- "This subtlety trips up students AND professionals. In this course, 'independent' means mutually independent unless we say otherwise."
- **Content budget:** definition box (3 formulas stacked) + warning text + counterexample shown step by step (5 items max on screen at a time)
- **Animation:** Definition builds up progressively, warning with RED flash, counterexample shown as a small grid

### Scene 5: Bayes' Theorem -- The Medical Test Revisited (7:00-9:30, ~150s)
**Narration:** ~300 words, 150s
- Section divider: "Bayes' Theorem"
- "Remember the medical test from last video? A test is 99% accurate. You test positive. What's the probability you actually have the disease?"
- "The answer depends on how rare the disease is. If only 1 in 1000 people have it, the answer is shocking: only about 9%."
- Derive Bayes' theorem from the conditional probability definition:
  - P(A|B) = P(A ∩ B) / P(B) ... (1)
  - P(B|A) = P(B ∩ A) / P(A) ... (2)
  - Since A ∩ B = B ∩ A: P(A ∩ B) = P(B|A) * P(A)
  - Substitute into (1): P(A|B) = P(B|A) * P(A) / P(B)
  - And by the law of total probability: P(B) = P(B|A)*P(A) + P(B|A^c)*P(A^c)
- Show the full formula in a formula_box with ACCENT highlight
- "Prior: P(A) -- what you believed before seeing evidence"
- "Likelihood: P(B|A) -- how likely the evidence is if A is true"
- "Posterior: P(A|B) -- what you believe AFTER seeing evidence"
- "Bayes' theorem tells you how to UPDATE your beliefs given new evidence."
- **Content budget:** Derivation shown step by step (max 4 items), then formula box, then prior/likelihood/posterior labels (progressive reveal)
- **Animation:** Step-by-step derivation with Transform from one line to next, formula box with flash, labels appear one at a time

### Scene 6: Worked Example -- The Medical Test (9:30-11:30, ~120s)
**Narration:** ~240 words, 120s
- Setup: Disease affects 1 in 1000 people (prevalence = 0.001)
  - Test sensitivity: P(+|D) = 0.99 (detects disease 99% of the time)
  - Test specificity: P(-|no D) = 0.99 (correct negative 99% of the time)
  - Therefore P(+|no D) = 0.01 (false positive rate)
- Question: P(D|+) = ?
- Apply Bayes:
  - P(D|+) = P(+|D)*P(D) / [P(+|D)*P(D) + P(+|D^c)*P(D^c)]
  - = (0.99 * 0.001) / [(0.99 * 0.001) + (0.01 * 0.999)]
  - = 0.00099 / [0.00099 + 0.00999]
  - = 0.00099 / 0.01098
  - ≈ 0.0902 ≈ 9%
- Visual: Area/rectangle model inspired by 3B1B
  - Omega as a tall rectangle split into "disease" (thin strip, 0.1%) and "no disease" (wide, 99.9%)
  - Color the test-positive portions: most positives are actually false positives!
  - Show the area model animating to reveal the 9% result
- "Even though the test is 99% accurate, if the disease is rare, most positive results are wrong."
- **Content budget:** Setup parameters (3-4 items), then formula application (4-5 items), then area model visual, then answer
- **Animation:** Parameters FadeIn, formula applied step by step, area model builds up, answer with flash

### Scene 7: Independence and Bayes (11:30-12:30, ~60s)
**Narration:** ~120 words, 60s
- Section divider: "Putting It Together"
- "What happens if A and B are independent? Then P(A|B) = P(A), so Bayes gives:"
  - P(A|B) = P(B|A)*P(A)/P(B) = P(A)*P(A)/P(A) = P(A)
  - "No new information! Independence means evidence doesn't change beliefs."
- "Bayes' theorem is interesting precisely when events are NOT independent -- when evidence actually tells you something."
- "This is why independence is a prerequisite for understanding Bayes: independence is the boring baseline, and Bayes is the exciting generalization."
- **Content budget:** formula simplification + key insight text + connection statement (3 items)
- **Animation:** Formula with Transform simplification steps, insight with ACCENT highlight

### Scene 8: Summary and Outro (12:30-13:30, ~60s)
**Narration:** ~120 words, 60s
- Recap with progressive_reveal:
  1. Independence: P(A ∩ B) = P(A) * P(B) -- knowledge of one event tells you nothing about the other
  2. Pairwise ≠ mutual independence -- need ALL intersection probabilities
  3. Bayes' theorem: P(A|B) = P(B|A)*P(A) / P(B) -- update beliefs with evidence
  4. Prior → Likelihood → Posterior: the Bayesian framework
  5. Independence makes Bayes trivial; dependence makes it powerful
- Tease: "Next time -- Random Variables: turning events into numbers"
- play_outro()
- **Content budget:** 5 recap items + outro card
- **Animation:** Progressive reveal of takeaways, then play_outro

## Color Coding
- PRIMARY (#5BC0EB): Events, sets, conditional probability notation
- SECONDARY (#7BC950): Sample space Omega, favorable outcomes, prior probabilities
- ACCENT (#FFD166): Key formulas (independence definition, Bayes' theorem), posterior
- RED (#EF476F): Warnings, common mistakes, counterexamples
- DIM (#6B6B8D): Intermediate steps, "boring" terms, labels

## Formulas to Render
1. P(A ∩ B) = P(A) * P(B) (independence)
2. P(A|B) = P(A) (equivalent form)
3. P(A ∩ B ∩ C) = P(A)*P(B)*P(C) (mutual independence)
4. P(A|B) = P(B|A)*P(A) / P(B) (Bayes' theorem)
5. P(A|B) = P(B|A)*P(A) / [P(B|A)*P(A) + P(B|A^c)*P(A^c)] (Bayes with total probability)
6. Numerical computation: 0.00099/0.01098 ≈ 9%

## Technical Notes
- Venn diagrams: Use Circle objects with fill_opacity for overlapping regions
- Area/rectangle model for Bayes: Use Rectangle objects with different fill_opacity colors to show proportions
- Dice grid: 6 squares for die faces, highlight subsets
- Coin flip visuals: Text("H") and Text("T") in small rounded rectangles
- Counterexample for mutual independence: Show 2x2 grid of coin outcomes with event memberships highlighted
- Use single backslashes in raw strings for LaTeX
- Keep formulas clean — use ly.formula_box() for key results
