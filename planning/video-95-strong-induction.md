# Video 95: Strong Induction

**Playlist:** Introduction to Proofs (Video 6 of 9)
**Level:** Undergraduate (Discrete Math / Proof-Based Mathematics)
**Class:** Video95_StrongInduction
**Script:** scripts/undergraduate/video-95-strong-induction.py

## Prerequisites
- Video 94: Proof by Mathematical Induction (weak induction)
- Basic familiarity with recurrence relations

## Learning Objectives
1. Understand the difference between weak and strong induction
2. State the Principle of Strong Induction formally
3. Recognize when strong induction is needed (multi-step dependencies)
4. Apply strong induction to prove a Fibonacci identity
5. Apply strong induction to prove every integer ≥ 2 is a product of primes

## Competitive Analysis References
- Analysis: channel-analysis/improvements.md (2026-07-03 entry)
- Trefor Bazett's recurrence relation example: adopt Fibonacci strong induction proof
- Numberphile's domino metaphor: adapt for staircase/bridge visual comparison
- Key gap: No competitor visualizes the hypothesis scope difference clearly

## Scene Plan (8 scenes, ~12 min target)

### Scene 1: Hook — The Staircase vs. The Bridge (~35s)
**Visual:** Two animations side by side.
Left: A staircase where each step rests only on the step directly below (weak induction).
Right: A bridge where each segment needs ALL previous segments to be anchored (strong induction).
The bridge collapses when only the last anchor is checked, but holds when all anchors are verified.
**Content:** "Regular induction is like climbing stairs — each step only needs the one below it. But what if your problem is more like building a bridge, where each piece depends on EVERYTHING before it? That's strong induction."
**Elements:** Two VGroup staircases, labels, title
**Content budget:** 4 elements max (staircase, bridge, 2 labels)

### Scene 2: Recap — Weak Induction (~30s)
**Visual:** Brief recap of weak induction formula with color-coded components.
P(1) true, P(k)→P(k+1), conclusion.
**Content:** Quick reminder of regular induction. The key assumption: we only assume P(k) to prove P(k+1). Just ONE previous case.
**Elements:** 3 formula boxes, highlight on P(k)
**Content budget:** 3 elements

### Scene 3: The Limit of Weak Induction — Fibonacci (~50s)
**Visual:** Fibonacci sequence growing: 1, 1, 2, 3, 5, 8, 13...
Each new number has TWO arrows pointing to it from the two previous numbers.
Show that to prove f_n ≥ n for n ≥ 5, assuming only f_k ≥ k is NOT ENOUGH because f_{k+1} = f_k + f_{k-1} needs TWO previous values.
**Content:** "Consider the Fibonacci sequence: each term is the sum of the TWO previous terms. If we try to prove f_n ≥ n using weak induction, we get stuck. We assume f_k ≥ k, but f_{k+1} = f_k + f_{k-1}. We need f_{k-1} too! Weak induction only gives us one step back."
**Elements:** Sequence display, arrows, failed proof attempt
**Content budget:** 4 elements

### Scene 4: The Principle of Strong Induction (~50s)
**Visual:** Formal statement with animated color-coding.
- Statement P(n) as a box
- Base case: P(1) true (green)
- Strong hypothesis: P(1) ∧ P(2) ∧ ... ∧ P(k) all true (orange/red, spanning full range)
- Inductive step: Using ALL of P(1)...P(k), prove P(k+1) (blue)
- Conclusion: P(n) true for all n ≥ 1 (yellow)
**Visual number line showing the range of the hypothesis as a growing highlighted bar.**
**Content:** The Principle: If P(1) is true, AND for every k ≥ 1, if ALL of P(1), P(2), ..., P(k) are true, then P(k+1) is true... THEN P(n) is true for all n ≥ 1.
**Elements:** Formal statement, number line with range highlight, labels
**Content budget:** 5 elements (statement, number line, 3 labels)

### Scene 5: Weak vs. Strong — Side by Side (~40s)
**Visual:** Two-column comparison.
Left column: Weak induction — hypothesis P(k), single blue dot on number line.
Right column: Strong induction — hypothesis P(1)∧...∧P(k), orange bar spanning from 1 to k.
Key insight highlighted: "Strong induction has a STRONGER hypothesis — it can assume more."
**Content:** "The only difference is what you assume. Weak: assume P(k). Strong: assume everything up to P(k). Everything else — base case, inductive step, conclusion — is the same. And since you can always ignore extra assumptions, strong induction is strictly more powerful."
**Elements:** Two columns, number line comparison, key insight label
**Content budget:** 5 elements

### Scene 6: Example 1 — Fibonacci Strong Induction Proof (~90s)
**Visual:** Step-by-step proof.
- Claim: f_n ≥ n for all n ≥ 5
- Base cases: f_5 = 5 ≥ 5 ✓, f_6 = 8 ≥ 6 ✓ (green highlight)
- Strong hypothesis: f_i ≥ i for all 5 ≤ i ≤ k (orange bar)
- Inductive step: f_{k+1} = f_k + f_{k-1} ≥ k + (k-1) = 2k - 1 ≥ k+1 (blue, with arrow showing f_k and f_{k-1} both available)
- QED marker
**Content:** Walk through the full proof. Show how the strong hypothesis gives us BOTH f_k and f_{k-1}, which is exactly what we need for the Fibonacci recurrence.
**Elements:** Claim, base cases, hypothesis, step derivation, conclusion
**Content budget:** Progressive reveal, max 5 at a time

### Scene 7: Example 2 — Every Integer ≥ 2 is a Product of Primes (~70s)
**Visual:** Quick second example showing the power of strong induction.
- Claim: Every integer n ≥ 2 is either prime or a product of primes
- Base: 2 is prime ✓
- Strong hypothesis: all integers from 2 to k satisfy the claim
- Step: If k+1 is prime, done. If composite, k+1 = ab where 2 ≤ a,b ≤ k. By strong hypothesis, both a and b are products of primes. So k+1 is a product of primes. ✓
**Content:** Second example adapted from Trefor Bazett's approach. Shows strong induction in a different context (number theory, not recurrence relations).
**Elements:** Claim, base case, two cases (prime/composite), conclusion
**Content budget:** Progressive reveal, max 5 at a time

### Scene 8: Summary — When to Use Strong Induction (~40s)
**Visual:** Summary checklist with examples.
- Use strong induction when your inductive step needs MORE than just P(k)
- Signals: recurrence relations, "every integer ≥ 2", divisibility chains
- Key point: strong induction is always valid — it's just sometimes unnecessary
- Teaser for next video: Proof by Cases
**Content:** Wrap up with clear guidance on when to choose strong induction over weak.
**Elements:** Title, checklist items, key point, next video card
**Content budget:** 4-5 elements
