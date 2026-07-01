# Video 92: Proof by Contrapositive (Introduction to Proof-Based Mathematics)

## Overview
- **Video Number:** 92
- **Playlist:** Introduction to Proofs (L4 — Proof-Based Mathematics)
- **Estimated Duration:** 12 min
- **Prerequisites:** Video 90 (Why Proofs?), Video 91 (Direct Proof), basic logic (implication, negation)

## Learning Objectives
1. Understand what the contrapositive is: P → Q is equivalent to ¬Q → ¬P
2. See WHY they're equivalent (truth table + visual diagram)
3. Learn when contrapositive is easier than direct proof (negated conclusions are simpler)
4. Apply the contrapositive technique to concrete number theory examples
5. Distinguish contrapositive from contradiction (common student confusion)

## Scene Breakdown

### Scene 1: Hook — The "Back Door" (0:00–1:30)
- **Content:** Open with the idea that sometimes the direct path is blocked, but the back door is wide open. Introduce contrapositive as the "back door proof."
- **Visual:** P → Q shown as a locked door; ¬Q → ¬P shown as the key/alternate entrance. Animated transition between the two.
- **Budget:** P→Q diagram + locked door icon + ¬Q→¬P diagram + key icon = 4 items max
- **Narration:** ~30 words, ~12s

### Scene 2: Definition — What IS the Contrapositive? (1:30–3:30)
- **Content:** Formal definition: "The contrapositive of P → Q is ¬Q → ¬P." Show truth table proving equivalence (T/F/T, F/T/T, T/F/T, T/T/T — both have F only when P=T, Q=F).
- **Visual:** Two-column truth table animated row by row. Highlight matching rows in PRIMARY/SECONDARY.
- **Budget:** Table header + 4 rows = 5 items (progressively revealed)
- **Narration:** ~50 words, ~20s

### Scene 3: When to Use It — Strategy Selection (3:30–5:00)
- **Content:** "Choose contrapositive when: (1) The conclusion's negation is simpler to work with. (2) The hypothesis's negation gives you more to work with. (3) Direct proof hits a wall."
- **Visual:** Decision flowchart or comparison: Direct path (block) vs Contrapositive (open). Example: "If n² is even → n is even" — direct proof is awkward; contrapositive (if n is odd → n² is odd) is natural.
- **Budget:** 3 criteria items + title = 4 items
- **Narration:** ~45 words, ~18s

### Scene 4: Example 1 — If n² is Even, Then n is Even (5:00–7:30)
- **Content:** Statement: "If n² is even, then n is even." Show why direct is awkward (what do you do with n²?). Then contrapositive: "If n is odd, then n² is odd." Proof: Let n = 2k+1 → n² = (2k+1)² = 4k²+4k+1 = 2(2k²+2k)+1 = odd. QED.
- **Visual:** Statement → contrapositive transformation (color-coded: P→Q becomes ¬Q→¬P) → proof steps with progressive reveal
- **Budget:** Statement + contrapositive form + current proof step = 3 items
- **Narration:** ~80 words, ~33s

### Scene 5: Example 2 — Product of Rationals is Rational (7:30–9:30)
- **Content:** Statement: "If xy is irrational, then at least one of x or y is irrational." Direct proof from "irrational" is hard. Contrapositive: "If both x and y are rational, then xy is rational." Proof: x = a/b, y = c/d → xy = ac/bd ∈ Q. Clean algebra.
- **Visual:** Statement → contrapositive → proof. Color-code rational/irrational.
- **Budget:** Statement + contrapositive + current step = 3 items
- **Narration:** ~70 words, ~29s

### Scene 6: Contrapositive vs Contradiction (9:30–11:00)
- **Content:** Common confusion. Contrapositive: prove ¬Q → ¬P (you assume ¬Q and directly derive ¬P). Contradiction: assume P ∧ ¬Q and derive a contradiction (anything false). They're different strategies, even though both are indirect.
- **Visual:** Side-by-side comparison: Contrapositive (linear: ¬Q → ¬P) vs Contradiction (two assumptions collide → explosion). Use different colors for each.
- **Budget:** 2 strategy diagrams + labels = 4 items
- **Narration:** ~50 words, ~20s

### Scene 7: Recap + Outro (11:00–12:00)
- **Content:** Summary: Contrapositive = ¬Q → ¬P, logically equivalent, use when negations simplify the work. Preview of next video (Proof by Contradiction).
- **Visual:** Recap bullets + "Next: Proof by Contradiction" card
- **Budget:** 3-4 recap items + next card = 4-5 items
- **Narration:** ~30 words, ~12s

## Key Formulas
- Contrapositive: P → Q ≡ ¬Q → ¬P
- Truth table: (T,T,T), (T,F,F), (F,T,T), (F,F,T)
- Odd definition: n = 2k+1 for integer k
- (2k+1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1
- Rational definition: x = a/b where a,b ∈ Z, b ≠ 0
- Product of rationals: (a/b)(c/d) = ac/bd ∈ Q

## Competitive Analysis Reference
- See improvements.md [2026-07-01] Proof by Contrapositive entry
- Key differentiator: Animated truth table proof + visual "locked door/key" metaphor
- Zero Manim-animated contrapositive proof videos exist — major gap
- Our advantage: visual explanation of WHY contrapositive works, not just HOW
