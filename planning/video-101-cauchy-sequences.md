# Video 101: Cauchy Sequences

**Playlist:** Real Analysis I (Video 3 of 12)
**Level:** Undergraduate (Real Analysis)
**Class:** Video101_CauchySequences
**Script:** scripts/undergraduate/video-101-cauchy-sequences.py

## Prerequisites
- Video 99: The Real Numbers (Completeness)
- Video 100: Sequences and Convergence (epsilon-N definition)
- Videos 90-98: Introduction to Proofs (complete)
- Understanding of the completeness axiom and suprema

## Learning Objectives
1. Understand intuitively what it means for terms to "get closer to each other"
2. State the formal definition of a Cauchy sequence
3. Prove that every convergent sequence is Cauchy (using triangle inequality)
4. State the Cauchy criterion: in R, Cauchy iff convergent (depends on completeness)
5. Understand why Cauchy sequences may fail to converge in Q (connect to completeness)

## Competitive Analysis References
- Analysis: channel-analysis/improvements.md (2026-07-04 entry for Video 101)
- Michael Penn (349K subs): Whiteboard lecture, systematic, proof-heavy. Structure 8/10, Visuals 4/10. Avoid: dense lecture format without visual intuition.
- Bright Side of Mathematics: Manim animations, systematic. Structure 8/10, Visuals 7/10. Adopt: systematic approach to definition.
- BriTheMathGuy: Fast-paced Manim. Structure 8/10, Pacing 9/10, Visuals 8/10. Adopt: fast-paced efficiency for proof that convergent implies Cauchy.
- Key gap: NO competitor visualizes the "terms getting closer to each other" vs "terms getting closer to L" distinction.
- Our unique edges:
  - Two-panel comparison: convergence (all terms near L) vs Cauchy (any two terms near each other)
  - The sequence 1, 1.4, 1.41, 1.414, ... shown as Cauchy in Q but not convergent in Q
  - Color-coded proof: convergent => Cauchy (forward) and Cauchy => convergent (uses completeness)

## Scene Plan (9 scenes, ~12 min target)

### Scene 1: Hook -- The Mystery Limit (~60s)
**Visual:** Number line with dots appearing, clustering tighter and tighter, but no L marked.
- Start with: "Last time we proved convergence using the epsilon-N definition. But there is a problem: that definition requires you to KNOW the limit L in advance. What if you do not know L? What if you cannot even guess it?"
- Show dots on a number line clustering: 1, 1.4, 1.41, 1.414, 1.4142, ... getting closer to each other
- Question: "These terms are clearly getting closer to each other. But can we prove they converge -- without knowing what they converge to?"
- Transition to intro.
**Elements:** Number line, sequence dots (progressive reveal), question text
**Content budget:** 4 elements max

### Scene 2: Intro + Section Divider (~20s)
**Visual:** Channel intro animation, then section divider.
- play_intro("Cauchy Sequences", "Real Analysis I")
- Section divider: "1 -- The Idea"

### Scene 3: Convergence vs Cauchy Intuition (~100s)
**Visual:** Two-panel comparison: left shows convergence (terms near L), right shows Cauchy (distance between any two terms shrinks).
- Left panel: "Convergence" -- all terms near L, arrow pointing to L
- Right panel: "Cauchy" -- two highlighted terms a_m and a_n, the distance between them shrinking
- Key distinction: "Convergence measures each term's distance from L. Cauchy measures the distance between any two terms."
- "If the terms are getting closer to each other, they must be getting closer to SOMETHING. In R, completeness guarantees that something exists."
- Show the epsilon-band concept: for Cauchy, the band is between any two terms, not between a term and L.
**Content:** "Here is the key distinction. In convergence, we measure the distance from each term to the limit L. Every term must eventually be within epsilon of L. But in a Cauchy sequence, we measure the distance between any two terms. If you pick any two terms far enough along the sequence, their distance is less than epsilon. Think of it like this: convergence means the terms are all approaching the same destination. Cauchy means the terms are all approaching each other. If the terms are squeezing together, they must be squeezing toward something. In the real numbers, completeness guarantees that something exists."
**Elements:** Two labeled panels (left/right), distance arrows, epsilon band visual
**Content budget:** Progressive reveal, max 5

### Scene 4: Section Divider -- Formal Definition (~5s)
**Visual:** Section divider "2 -- The Definition"

### Scene 5: The Formal Definition (~120s)
**Visual:** Number line showing the "any two terms" concept, then the formal definition in a formula box.
- Start with visual: number line, two points a_m and a_n highlighted, double-headed arrow showing |a_m - a_n|
- Animate: as m,n increase, the arrow shrinks to nearly zero
- Reveal formal definition step by step:
  - "A sequence (a_n) is Cauchy if..."
  - "for every epsilon > 0, there exists N in N..."
  - "such that for all m, n > N: |a_m - a_n| < epsilon"
- Show in formula box (accent color border)
- Explain each part:
  - epsilon: how close we demand any two terms to be
  - N: how far along the sequence we need to go
  - m, n > N: BOTH terms must be past this point
  - |a_m - a_n| < epsilon: the distance between them is tiny
- Emphasize: "Notice -- the limit L does NOT appear anywhere in this definition!"
**Content:** "Now the formal definition. A sequence a sub n is Cauchy if for every epsilon greater than zero, there exists a natural number N such that for all m and n greater than N, the absolute value of a sub m minus a sub n is less than epsilon. Unpack this. Epsilon is how close we demand any two late terms to be. N tells us how far along we need to go. And the condition says: once both indices m and n are past N, the two terms are within epsilon of each other. Notice something crucial. The limit L does not appear anywhere in this definition. That is the power of Cauchy sequences. We can test convergence without knowing what the limit is."
**Elements:** Number line, a_m and a_n dots, distance arrow (animated), definition box, part explanations
**Content budget:** Progressive reveal, fade old elements

### Scene 6: Section Divider -- Proof (~5s)
**Visual:** Section divider "3 -- Convergent Implies Cauchy"

### Scene 7: Proof -- Every Convergent Sequence is Cauchy (~120s)
**Visual:** Step-by-step proof with color-coded key terms.
- Claim: If a_n -> L, then (a_n) is Cauchy
- Proof:
  - "Let epsilon > 0."
  - "Since a_n -> L, there exists N such that for all n > N: |a_n - L| < epsilon/2"
  - "Let m, n > N. Then: |a_m - a_n| = |(a_m - L) - (a_n - L)|"
  - "By triangle inequality: <= |a_m - L| + |a_n - L| < epsilon/2 + epsilon/2 = epsilon"
  - "Therefore (a_n) is Cauchy. QED."
- Key insight box: "The trick is to use epsilon/2 -- each term gets half the budget!"
- Visual: number line showing L in center, a_m and a_n each within epsilon/2 of L, so they are within epsilon of each other.
**Content:** "The first direction is straightforward. If a sequence converges, it must be Cauchy. Here is the proof. Let epsilon be positive. Since a sub n converges to L, there exists N such that for all n greater than N, the absolute value of a sub n minus L is less than epsilon over two. Now let m and n both be greater than N. We want to bound the distance between a sub m and a sub n. Write a sub m minus a sub n as a sub m minus L minus a sub n plus L, which equals a sub m minus L minus a sub n minus L. By the triangle inequality, this is at most a sub m minus L plus a sub n minus L. Each of these is less than epsilon over two, so the sum is less than epsilon. The proof is complete. The trick was using epsilon over two: each term gets half the error budget, so together they stay within epsilon."
**Elements:** Claim, proof steps (progressive), key insight box, number line visual
**Content budget:** Progressive reveal, max 5 lines at a time

### Scene 8: Section Divider -- Completeness (~5s)
**Visual:** Section divider "4 -- Cauchy and Completeness"

### Scene 9: Cauchy Implies Convergent in R + The Q Example (~120s)
**Visual:** Two-part scene. First: the theorem statement. Second: the Q counterexample.
- Part 1: Theorem statement
  - "Theorem: Every Cauchy sequence in R converges."
  - "This is EQUIVALENT to the completeness axiom!"
  - Brief proof sketch: (a_n) is bounded (Cauchy), so by Bolzano-Weierstrass has a convergent subsequence, and the whole sequence converges to the same limit.
  - Or: define L = sup{a_n : n > N}, show a_n -> L using Cauchy property.
  - Keep it as a statement + intuition, not a full proof (save full proof for later).
- Part 2: The Q counterexample
  - Show: 1, 1.4, 1.41, 1.414, 1.4142, ... (decimal approximations of sqrt(2))
  - "In R, this converges to sqrt(2). But sqrt(2) is NOT in Q."
  - "So in Q, this is Cauchy but NOT convergent."
  - Color: terms in Q in PRIMARY, the "missing limit" in RED
  - "Completeness fills the holes. R has no gaps, so Cauchy always converges."
**Content:** "Here is the deep result. In the real numbers, every Cauchy sequence converges. This theorem is actually equivalent to the completeness axiom. It means that in R, the two notions of convergence and being Cauchy are the same thing. But this fails in the rational numbers. Consider the sequence: one, one point four, one point four one, one point four one four, and so on. These are the decimal approximations of the square root of two. In the reals, this converges to root two. But root two is not a rational number. So in Q, this sequence is Cauchy, the terms get arbitrarily close to each other, but it does not converge because its limit is missing from Q. Completeness is what fills the gaps. The real numbers have no holes, so every Cauchy sequence finds its limit."
**Elements:** Theorem statement (formula box), Q example on number line (dots + missing limit marker), "Completeness fills the holes" label
**Content budget:** Progressive reveal, max 5

### Scene 10: Summary + Outro (~60s)
**Visual:** Key takeaways as progressive reveal, then outro.
- Key takeaways:
  - A Cauchy sequence is one where terms get closer to each other
  - The definition does not reference the limit L
  - Every convergent sequence is Cauchy (easy direction)
  - In R, Cauchy iff convergent (requires completeness!)
  - Completeness fills the "holes" that Q has
- Outro with play_outro(), teasing next video "Limits of Functions"
**Content:** "Five things to remember. A Cauchy sequence is one where any two terms far enough along are arbitrarily close. The definition does not mention the limit at all, which is its power. Every convergent sequence is Cauchy, and we proved this using the triangle inequality with the epsilon over two trick. In the real numbers, Cauchy and convergent are the same thing, and this equivalence depends on completeness. And completeness is what distinguishes R from Q, filling the holes that make Cauchy sequences fail to converge. Next time, we move from sequences to functions and study limits of functions."
**Elements:** Takeaways (progressive reveal, 3-5 items), outro
**Content budget:** Progressive reveal
