# Video 91: Direct Proof (Introduction to Proof-Based Mathematics)

## Overview
- **Video Number:** 91
- **Playlist:** Introduction to Proofs (L4 — Proof-Based Mathematics)
- **Estimated Duration:** 12 min
- **Prerequisites:** Video 90 (Why Proofs?), basic logic (implication, universal quantifier)

## Learning Objectives
1. Understand the structure of a direct proof: assume P, derive Q
2. Learn the standard template: "Let ... Suppose ... Then ... Therefore ..."
3. Apply direct proof to number-theoretic statements (even/odd, divisibility)
4. Recognize and avoid common mistakes (circular reasoning, assuming conclusion)
5. See how to choose the right starting point (rewriting definitions)

## Scene Breakdown

### Scene 1: Hook — What Does "Direct" Mean? (0:00–1:30)
- **Content:** Contrast direct proof with other strategies. "You know WHERE you're going, and you walk straight there." 
- **Visual:** Diagram showing P → arrow → Q with a straight path, vs. indirect paths (contradiction, contrapositive) branching off
- **Budget:** Title + diagram (3 blocks + 2 arrows) = 5 items max
- **Narration:** ~30 words, ~12s

### Scene 2: The Direct Proof Template (1:30–3:30)
- **Content:** Introduce the standard structure. "To prove P → Q: 1. Assume P is true. 2. Use definitions and known facts. 3. Chain deductions to reach Q."
- **Visual:** Template text appearing line by line: Assume → Expand → Deduce → Conclude
- **Budget:** 4 template steps + title = 5 items
- **Narration:** ~50 words, ~20s

### Scene 3: Example 1 — Sum of Even Numbers (3:30–6:00)
- **Content:** Prove: "If m and n are even integers, then m + n is even." Full step-by-step proof with justification for each line.
- **Visual:** Statement → Let (definitions) → Algebra → Conclusion. Each line reveals with color coding: hypothesis=PRIMARY, algebra=SECONDARY, conclusion=ACCENT
- **Budget:** Statement + current proof line + justification label = 3 items
- **Narration:** ~80 words, ~33s

### Scene 4: Example 2 — Product of Odd Numbers (6:00–8:30)
- **Content:** Prove: "If a and b are odd integers, then a · b is odd." Show how to apply the same template to a new domain.
- **Visual:** Same template structure but with multiplication. a = 2k+1, b = 2m+1 → expand → factor out the 2.
- **Budget:** Statement + current proof line + justification = 3 items
- **Narration:** ~80 words, ~33s

### Scene 5: Example 3 — Divisibility (8:30–10:30)
- **Content:** Prove: "If n is an integer, then 3n² + n + 2 is even." Requires more algebraic manipulation. Shows that direct proof works for more complex statements too.
- **Visual:** Statement → algebraic expansion step by step → factorization → conclusion
- **Budget:** Statement + current line + justification = 3 items
- **Narration:** ~70 words, ~29s

### Scene 6: Common Mistakes — What NOT to Do (10:30–11:30)
- **Content:** Show two common errors: (1) Circular reasoning — using what you're trying to prove. (2) Forgetting to use the hypothesis.
- **Visual:** Two side-by-side "bad proof" examples with red X marks, then the fix for each.
- **Budget:** 2 bad examples (one at a time) + red X + fix = 4 items
- **Narration:** ~40 words, ~16s

### Scene 7: Recap + Outro (11:30–12:00)
- **Content:** Summary of the direct proof template + preview of next video (Proof by Contrapositive).
- **Visual:** Recap bullets + "Next: Proof by Contrapositive" card
- **Budget:** 3-4 recap items + next card = 4-5 items
- **Narration:** ~30 words, ~12s

## Key Formulas
- Even: n = 2k for integer k
- Odd: n = 2k + 1 for integer k
- Sum of evens: 2k + 2m = 2(k + m)
- Product of odds: (2k+1)(2m+1) = 4km + 2k + 2m + 1 = 2(2km + k + m) + 1
- Parity of 3n² + n + 2: = 3n² + n + 2 = n(3n + 1) + 2; cases: if n even → even + even = even; if n odd → odd · even + even = even

## Competitive Analysis Reference
- See improvements.md [2026-06-30] Direct Proof entry
- Key differentiator: animated step-by-step proof reveals with color-coded justification
- Competitors: mostly whiteboard/university lecture style — no Manim-animated proof tutorials exist for this topic
