# Video 94: Proof by Mathematical Induction

**Playlist:** Introduction to Proofs (Video 5 of 9)
**Level:** Undergraduate (Discrete Math / Proof-Based Mathematics)
**Class:** Video94_ProofByInduction
**Script:** scripts/undergraduate/video-94-proof-by-induction.py

## Prerequisites
- Videos 90-93: Why Proofs, Direct Proof, Contrapositive, Contradiction
- Basic familiarity with sums (sigma notation)

## Learning Objectives
1. Understand the intuition behind mathematical induction via the domino analogy
2. State the Principle of Mathematical Induction formally
3. Identify the three components: base case, inductive hypothesis, inductive step
4. Apply induction to prove the sum formula 1 + 2 + ... + n = n(n+1)/2
5. Apply induction to prove 2^n > n for all n ≥ 1
6. Understand the difference between weak and strong induction

## Competitive Analysis References
- Analysis: channel-analysis/improvements_induction.md
- Zach Star's domino animation: adopt animated domino chain as opening
- Trefor Bazett's learning objectives: adopt explicit objective framing
- Numberphile's set theory motivation: "you can't check infinitely many things"
- Grid visualization for sum formula: our unique visual contribution

## Scene Plan (9 scenes, ~13 min target)

### Scene 1: Hook — The Domino Effect (~30s)
**Visual:** Animated domino chain. Dominos stand upright in a row. The first domino falls, triggering the next, and so on. Camera follows the chain of falling dominoes.
**Content:** "If you push the first domino, and each domino knocks over the next one... they ALL fall. How do you KNOW? This is mathematical induction."
**Elements:** Domino rectangles (manim VMobjects), falling animation, title
**Content budget:** 4 elements max (dominos, label, arrow)

### Scene 2: Why We Need Induction (~40s)
**Visual:** Side-by-side: "Direct proof" (check n=1, n=2, n=3, ..., ???) with growing list that never ends vs. induction as a "shortcut."
**Content:** We have infinitely many statements to prove. We can't check each one individually. Induction lets us prove ALL of them with just two steps.
**Elements:** Two columns, growing list (left), two-step summary (right)
**Narration:** "You cannot check infinitely many cases. You need a method that handles infinity in finite steps."

### Scene 3: The Principle of Mathematical Induction (~50s)
**Visual:** Formal statement with animated color-coding.
- Statement P(n) shown as a box/function
- Base case: P(1) is true (highlighted in SECONDARY/green)
- Inductive step: P(k) → P(k+1) (highlighted in PRIMARY/blue and SECONDARY/green)
- Conclusion: P(n) true for all n ≥ 1 (highlighted in ACCENT/yellow)
**Content:** Formal principle: If P(1) is true, AND P(k) → P(k+1) for all k ≥ 1, THEN P(n) is true for all n ≥ 1.
**Elements:** Formal statement, 3 labeled components, visual flow arrows

### Scene 4: Anatomy of an Induction Proof (~35s)
**Visual:** Recipe/card format with three numbered steps.
**Content:**
1. **Base case:** Prove P(1) is true
2. **Inductive hypothesis:** Assume P(k) is true (for some k ≥ 1)
3. **Inductive step:** Using the hypothesis, prove P(k+1) is true
4. **Conclusion:** Therefore P(n) is true for all n ≥ 1
**Elements:** Recipe card with 4 numbered steps, color-coded

### Scene 5: Example 1 — Sum Formula with Grid Visual (~150s)
**Visual:** The classic 1 + 2 + ... + n = n(n+1)/2 proof.
- Part A (~40s): Show the statement P(n). Display grid visualization: growing right triangle of dots. For n=4, show 1+2+3+4 = 10 dots in a triangle. Duplicate, flip, form rectangle. Rectangle is n × (n+1), so triangle area = n(n+1)/2. (Visual intuition before algebra)
- Part B (~30s): Base case. n=1: 1 = 1(2)/2 = 1. Checkmark.
- Part C (~50s): Inductive hypothesis. Assume 1+2+...+k = k(k+1)/2 (highlighted PRIMARY). Then compute 1+2+...+k+(k+1) = k(k+1)/2 + (k+1) = (k+1)(k+2)/2. (Color-coded algebra)
- Part D (~30s): Conclusion. Therefore P(k+1) holds. Therefore P(n) holds for all n ≥ 1.
**Elements:** Grid dots, algebra steps (one at a time), color-coded substitution

### Scene 6: Example 2 — 2^n > n (~90s)
**Visual:** Prove 2^n > n for all n ≥ 1 using induction.
- Base case: n=1: 2^1 = 2 > 1. Check.
- Inductive hypothesis: Assume 2^k > k for some k ≥ 1.
- Inductive step: 2^(k+1) = 2 · 2^k > 2k ≥ k+1 (since k ≥ 1). Therefore 2^(k+1) > k+1.
- Note the key insight: we used 2k ≥ k+1 because k ≥ 1.
**Elements:** Power of 2 growth visual (optional bar chart), algebra steps

### Scene 7: When to Use Induction (~40s)
**Visual:** Signal words checklist, similar to Video 93's "When to Use Contradiction."
**Content:**
- "For all integers n ≥ ..." — statements indexed by natural numbers
- Sum and product formulas
- Recursive definitions (factorial, Fibonacci)
- Inequalities about sequences
- Divisibility claims
**Elements:** Bulleted list, one item at a time

### Scene 8: Strong Induction (~60s)
**Visual:** Comparison of weak vs. strong induction.
- Weak: "If P(k) then P(k+1)" — single rung support
- Strong: "If P(1), P(2), ..., P(k) then P(k+1)" — full foundation support
- Visual metaphor: single ladder rung vs. entire staircase foundation
- Mention: "Every proof by weak induction is also a proof by strong induction, but not vice versa."
- Brief example idea: the postage stamp problem (4-cent and 5-cent stamps can make any amount ≥ 12)
**Elements:** Side-by-side diagrams, visual metaphor

### Scene 9: Summary & Outro (~30s)
**Visual:** Key takeaways card + outro animation.
**Content:**
1. Induction: base case + inductive step → all cases
2. Domino metaphor: first falls + each triggers next → all fall
3. Two examples: sum formula, inequality
4. Strong induction: assume all previous, not just one
5. Next: Proof by Cases
**Elements:** 4 takeaway items, outro branding

## Technical Notes
- Domino animation: Use VGroup of rectangles with sequential rotation animation
- Grid visualization: Dot grid using MathTex dots or Dots mobject
- Color coding: P(k) = PRIMARY, P(k+1) = SECONDARY, substitution = ACCENT
- Follow AGENTS.md quality rules: max 5 elements, LayoutEngine, progressive disclosure
