# Video 96: Proof by Cases

**Playlist:** Introduction to Proofs (Video 7 of 9)
**Level:** Undergraduate (Discrete Math / Proof-Based Mathematics)
**Class:** Video96_ProofByCases
**Script:** scripts/undergraduate/video-96-proof-by-cases.py

## Prerequisites
- Video 93: Direct Proof
- Video 94: Proof by Contrapositive
- Video 94/95: Proof by Induction / Strong Induction
- Basic familiarity with logical disjunction (OR) and implications

## Learning Objectives
1. Understand when proof by cases is applicable (hypothesis contains a disjunction)
2. State the formal logical basis: (P1 v P2 v ... v Pn) => R means prove Pi => R for each i
3. Recognize common case-split triggers: parity (even/odd), sign (positive/negative/zero), inequality thresholds
4. Apply proof by cases to prove a statement about integers (easy example)
5. Apply proof by cases to prove an inequality involving absolute values (medium example)
6. Apply proof by cases to prove a divisibility statement (challenging example)

## Competitive Analysis References
- Analysis: channel-analysis/improvements.md (2026-07-03 entry)
- Trefor Bazett's logical structure: adopt clean (P v Q) => R formal framing
- Kimberly Brehm's 3 progressive examples: compress into 10 min with better pacing
- Key gap: No competitor uses visual case-split trees or color-coded case tracking
- Our edge: Decision tree animation + color-coded cases + motivational puzzle hook

## Scene Plan (7 scenes, ~10 min target)

### Scene 1: Hook — The Mystery Envelope (~35s)
**Visual:** A sealed envelope with a question mark. Inside, a number. Challenge: prove something about it without knowing what it is — by splitting into cases.
Show two envelopes: "Could be even" and "Could be odd" — prove something true regardless.
**Content:** "Imagine someone hands you a sealed envelope with a number inside. They say: prove that n squared minus n is always even. You can't see the number — but you can still prove it, because there are only two possibilities: even or odd. That's proof by cases."
**Elements:** Envelope icon, two branch arrows, n^2 - n formula, "always even" badge
**Content budget:** 4 elements max

### Scene 2: The Logical Structure (~50s)
**Visual:** Formal logical structure with animated decision tree.
- Show: (P1 v P2 v ... v Pn) => R
- The tree: hypothesis node branches into n colored paths (P1, P2, ..., Pn), each converging to R
- Key requirements: (1) cases cover ALL possibilities, (2) cases are MUTUALLY EXCLUSIVE, (3) each case proves R
**Content:** "Proof by cases works when your hypothesis is a disjunction — an OR statement. If P1 OR P2 OR ... OR Pn, then R. You prove R under EACH case separately. For this to work, three things: your cases must cover every possibility, they must not overlap, and each case must independently lead to R."
**Elements:** Logical formula, decision tree, 3 requirement labels
**Content budget:** 5 elements (formula, tree, 3 labels progressively revealed)

### Scene 3: Common Case-Split Triggers (~40s)
**Visual:** Quick visual list with icons.
- Parity: even vs. odd (number line split at 0)
- Sign: positive, negative, zero (number line with 3 zones)
- Inequality thresholds: x < a, x = a, x > a
- Remainder classes: n mod 3 in {0, 1, 2}
- Conditional structure: if/else in code = case split in proofs
**Content:** "When do we reach for proof by cases? Whenever the universe naturally splits into categories. Parity — even or odd. Sign — positive, negative, or zero. Thresholds — less than, equal to, or greater than. Remainder classes. This is the same logic behind if/else statements in programming."
**Elements:** Category labels, number line visual, code snippet (if/else)
**Content budget:** 4-5 elements (categories appear progressively)

### Scene 4: Example 1 — n^2 - n is Always Even (Easy) (~80s)
**Visual:** Step-by-step proof with color-coded cases.
- Claim: For all integers n, n^2 - n is even
- Case 1 (PRIMARY color): n is even. Write n = 2k. Then n^2 - n = 4k^2 - 2k = 2(2k^2 - k). Even. Checkmark.
- Case 2 (SECONDARY color): n is odd. Write n = 2k + 1. Then n^2 - n = (2k+1)^2 - (2k+1) = 4k^2 + 2k = 2(2k^2 + k). Even. Checkmark.
- Conclusion: In both cases, n^2 - n is even. QED.
- Animated decision tree showing Case 1 (blue path) and Case 2 (green path) both leading to "Even"
**Content:** Walk through both cases step by step. Emphasize that the algebra in each case is different, but both reach the same conclusion. This is the power of proof by cases: you don't need one unified argument — you just need each case to work.
**Elements:** Claim, Case 1 derivation, Case 2 derivation, QED marker, mini tree
**Content budget:** Progressive reveal, max 5 at a time (remove Case 1 when showing Case 2, or show side by side with tree)

### Scene 5: Example 2 — Absolute Value Inequality (Medium) (~90s)
**Visual:** Proof with number line showing the case split at 0.
- Claim: For all real x, |2x - 1| >= 2x - 1
- Case 1: 2x - 1 >= 0 (i.e., x >= 1/2). Then |2x - 1| = 2x - 1 >= 2x - 1. Trivially true.
- Case 2: 2x - 1 < 0 (i.e., x < 1/2). Then |2x - 1| = -(2x - 1) = 1 - 2x. Since 2x - 1 < 0, we have 1 - 2x > 0 > 2x - 1. True.
- Animated number line: show the split point at x = 1/2, color the right side PRIMARY (positive) and left side SECONDARY (negative)
**Content:** "Now a classic case split involving absolute values. The absolute value always forces a case split at zero. When 2x minus 1 is non-negative, the absolute value does nothing — it's trivially true. When it's negative, the absolute value flips the sign, and the result is positive, which is always greater than a negative number."
**Elements:** Claim, number line with split, Case 1, Case 2, conclusion
**Content budget:** Progressive reveal, max 5 at a time

### Scene 6: Example 3 — Divisibility by 3 (Challenging) (~80s)
**Visual:** Proof with three colored cases on the number line.
- Claim: For all integers n, n^2 leaves remainder 0 or 1 when divided by 3
- Case 1 (PRIMARY): n = 3k. n^2 = 9k^2, remainder 0. Checkmark.
- Case 2 (SECONDARY): n = 3k + 1. n^2 = 9k^2 + 6k + 1, remainder 1. Checkmark.
- Case 3 (ACCENT): n = 3k + 2. n^2 = 9k^2 + 12k + 4, remainder 4 = 1. Checkmark.
- Conclusion: n^2 ≡ 0 or 1 (mod 3). QED.
- Number line showing residue classes mod 3 as three zones
**Content:** "A harder example with three cases. Every integer is congruent to 0, 1, or 2 modulo 3 — that's three exhaustive cases. In each case, we square and check the remainder. The key insight: 2 squared gives remainder 4, which is the same as remainder 1 mod 3. So we can refine: n squared is either 0 or 1 mod 3 — never 2."
**Elements:** Claim, Case 1, Case 2, Case 3, conclusion
**Content budget:** Progressive reveal, max 5 at a time

### Scene 7: Summary + Connection to Programming (~40s)
**Visual:** Summary checklist with side-by-side proof/code comparison.
- Proof by cases: split hypothesis into exhaustive, exclusive cases
- Each case independently proves the conclusion
- Same as: if/elif/else in programming
- Key: cases must be EXHAUSTIVE (cover everything) and EXCLUSIVE (no overlap)
- Teaser for next video: Existence and Uniqueness Proofs
**Content:** "Proof by cases is everywhere in mathematics and in code. Every if/else statement is a proof by cases in disguise. The keys: make sure your cases cover everything, don't overlap, and each one independently gets you to the conclusion."
**Elements:** Title, checklist, code comparison, key point, next video card
**Content budget:** 4-5 elements
