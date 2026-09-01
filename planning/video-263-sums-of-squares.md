# Video 263: Sums of Two Squares — Number Theory

## Overview
Which integers can be written as a sum of two squares? Fermat gave a beautiful
characterization for primes: p = x^2 + y^2 if and only if p = 2 or p = 1 (mod 4).
This video explores the identity that makes this work (Brahmagupta), classifies
primes, and shows how the full classification of integers follows.

## Scenes (8 scenes, ~10 min)

### Scene 1: Hook (~1.5 min)
Content budget: intro animation + 2 text items
- Channel intro
- Title: "Sums of Two Squares"
- Pose the question: 5 = 1^2 + 2^2, 13 = 2^2 + 3^2, but can 7 be written this way?
- Tease: the answer depends only on whether p = 1 (mod 4)

### Scene 2: Which Primes Are Sums of Two Squares? (~1.5 min)
Content budget: title + 4 text/formula items
- Section divider: "The Question"
- Small primes table: 2=1+1, 3=NO, 5=1+4, 7=NO, 11=NO, 13=4+9, 17=1+16
- Pattern: p = 2 or p = 1 (mod 4) works; p = 3 (mod 4) does not
- Fermat's Theorem statement

### Scene 3: Brahmagupta-Fibonacci Identity (~2 min)
Content budget: title + formula box + 2 text items
- Section divider: "The Key Identity"
- State identity: (a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2
- Formula box with the identity
- Interpret: product of two sums-of-squares IS a sum-of-squares
- Example: 5 * 13 = 65 = 1+64 = 8^2 + 1^2

### Scene 4: Proof Idea — Descent (~2 min)
Content budget: title + 3 text items
- Section divider: "Why It's True"
- Key insight: if p | (a^2 + b^2) and p = 1 (mod 4), then p itself is a sum of squares
- Thue's lemma: if p | (a^2 + 1), exists x,y with x^2 + y^2 = kp for small k
- Descent: use Brahmagupta identity to reduce k step by step until k=1
- Note: full proof is deep (uses Wilson's theorem); we show the structure

### Scene 5: The Negative Case (~1 min)
Content budget: title + 2 text items
- Section divider: "Why p = 3 (mod 4) Fails"
- Mod 4 argument: squares are 0 or 1 mod 4, so x^2 + y^2 is 0, 1, or 2 mod 4
- So x^2 + y^2 = p with p = 3 (mod 4) is impossible

### Scene 6: Full Classification of Integers (~1.5 min)
Content budget: title + 3 text items
- Section divider: "Which Integers?"
- Theorem: n = x^2 + y^2 iff every prime q = 3 (mod 4) appears with EVEN exponent in n's factorization
- Examples: 45 = 9*5 = 3^2 * 5 -> 45 = 6^2 + 3^2 (3 appears squared, OK)
- Counter-example: 21 = 3*7 -> 3 and 7 both 3 mod 4 with exponent 1 -> NO

### Scene 7: Worked Examples (~1.5 min)
Content budget: title + 3 text/formula items
- Section divider: "Worked Examples"
- Example 1: Write 65 = 5*13 as sum of two squares using Brahmagupta
  - (1^2+2^2)(2^2+3^2) = (1*2-2*3)^2 + (1*3+2*2)^2 = (-4)^2 + 7^2 = 16+49 = 65
- Example 2: 10 = 2*5 = (1^2+1^2)(1^2+2^2) = (-1)^2+3^2 = 10

### Scene 8: Summary + Outro (~0.5 min)
Content budget: title + 3 text items
- Section divider: "Summary"
- Key takeaways
- Channel outro

## Competitive Analysis
Skipped: web search unavailable during this run. Topics well-covered in standard
number theory curricula (Dummit & Foote, Hardy & Wright). Style follows
established channel patterns from videos 251-262.

## Production Notes
- Use visual proof for the mod-4 impossibility (color-coded squares)
- Brahmagupta identity should be in a formula box with ACCENT color
- The descent proof idea is sketched, not fully formal
- Connect back to quadratic reciprocity (video 262) — -1 is a QR mod p iff p = 1 mod 4
