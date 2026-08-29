# Video 252: Prime Numbers

**Playlist:** Number Theory (Videos 251-265)
**Target duration:** 10-14 minutes
**Class:** Video252_PrimeNumbers
**File:** scripts/graduate/video-252-prime-numbers.py

## Competitive Analysis Reference

Based on the Aug 29 2026 analysis (appended to improvements.md):
- 3B1B prime spiral video: 7.5M views - cold-open visual mystery technique
- Numberphile Euclid proof: 878K views - address product+1 misconception explicitly
- Khan Academy sieve + PNT: 157K + 194K views with zero visual polish - huge Manim opportunity
- GAP: Nobody has made a cohesive Manim-animated intro to primes covering definition, sieve, Euclid proof, distribution, and PNT in one video
- Recommended: cold-open with mystery, visual sieve as centerpiece, Euclid proof with misconception callout, density visualization, close by circling back

## Content Outline (9 Scenes)

### Scene 1 - Hook (0:00-1:30)
**Goal:** Open with visual mystery, motivate primes as fundamental
- Intro animation
- Start with: "What do these numbers have in common?" showing 2,3,5,7,11,13
- Every integer is built from primes (Fundamental Theorem of Arithmetic teaser)\n- Applications: cryptography, pattern-seeking, deepest unsolved problems in math
- Content budget: intro + 3 bullet points

### Scene 2 - Definition of Primes (1:30-3:00)
**Goal:** Formal definition with visual intuition
- Section divider: "1 - What Are Primes?"
- Formal definition: p > 1, divisors are only 1 and p
- Not 1 (important convention) — show why 1 is excluded
- Examples: 2,3,5,7,11 are prime; 4,6,8,9 are not
- Visual: number line with primes highlighted in PRIMARY color
- Content budget: definition formula box -> 2-3 examples -> 1 is not prime note

### Scene 3 - Sieve of Eratosthenes (3:00-5:30)
**Goal:** Animated sieve as the centerpiece visual (the biggest animation opportunity)
- Section divider: "2 - Finding Primes"
- Grid of numbers 2-30 (or 2-50)
- Start: circle 2, cross out all multiples of 2 (even numbers flash RED)
- Next prime: circle 3, cross out multiples of 3
- Continue with 5 (multiples of 4 already crossed out)
- Primes remaining glow in PRIMARY
- Content budget: grid setup -> sieve animation with 2,3,5 -> remaining primes highlighted
- NOTE: This is the most animatable scene. Keep it visual-heavy with minimal text.

### Scene 4 - Infinitude of Primes - Setup (5:30-7:00)
**Goal:** Motivate Euclid's theorem
- Section divider: "3 - Are There Infinitely Many Primes?"
- Observation: primes seem to thin out (2,3,5,7,11,13,17,19,23,29...)
- Could they stop? What if 29 were the last prime?
- Euclid's insight (300 BCE): proof by contradiction
- Content budget: observation -> question -> proof strategy preview

### Scene 5 - Euclid's Proof (7:00-9:00)
**Goal:** Walk through the proof with visual clarity
- Assume finitely many: p1, p2, ..., pn
- Define N = p1 * p2 * ... * pn + 1
- Key question: is N prime or composite?
- N is not divisible by any pi (remainder is always 1)
- MISCONCEPTION CALLOUT: N itself might not be prime! It could have a new prime factor not in our list
- Either way: contradiction - there must be a prime not in our list
- Color coding: BLUE for assumption, RED for contradiction, GREEN for conclusion
- Content budget: assumption -> N construction -> key question -> contradiction -> conclusion

### Scene 6 - Fundamental Theorem of Arithmetic (9:00-10:00)
**Goal:** State unique factorization as the key property of primes
- Every integer n > 1 has a unique prime factorization (up to ordering)
- Visual: show 60 = 2^2 * 3 * 5 with color-coded factors
- Show 12 = 2^2 * 3, compare with 60 sharing factors
- Connection to the previous video (divisibility, gcd, Bezout)
- Content budget: theorem statement -> factorization example -> connection to Video 251

### Scene 7 - Distribution of Primes (10:00-11:30)
**Goal:** Visualize how primes thin out
- Section divider: "4 - The Distribution of Primes"
- Primes in intervals: [1,10] has 4, [1,100] has 25, [1,1000] has 168
- Density decreases: 40%, 25%, 16.8%
- Visual: bar chart showing prime count in intervals of increasing size
- Content budget: table of counts -> density trend -> bar chart

### Scene 8 - Prime Number Theorem Intuition (11:30-13:00)
**Goal:** State the PNT visually without proof
- Section divider: "5 - The Prime Number Theorem"
- pi(n) ~ n / ln(n) — the number of primes up to n is approximately n over ln(n)
- Visual: show pi(100) = 25 vs 100/ln(100) ≈ 21.7 (close!)
- Another check: pi(1000) = 168 vs 1000/ln(1000) ≈ 144.8 (getting closer relatively)
- The ln(n) grows slowly — so primes thin out, but never run out
- Connection to Euclid: infinite, but increasingly sparse
- Content budget: PNT formula box -> numerical checks -> intuition

### Scene 9 - Summary (13:00-14:00)
**Goal:** Recap and tease future topics
- Section divider: "Summary"
- Key takeaways (progressive reveal):
  1. Primes: p > 1 with only 1 and p as divisors
  2. Sieve of Eratosthenes finds all primes up to N
  3. There are infinitely many primes (Euclid, ~300 BCE)
  4. Every integer > 1 has a unique prime factorization
  5. pi(n) ~ n/ln(n) — primes thin out but never stop
- Outro with next video: "Prime Factorization and Modular Arithmetic"

## Visual Design Notes

### Sieve of Eratosthenes (Scene 3 - Centerpiece)
- Create a grid of numbers (2-50) as MathTex objects arranged in rows
- Each sieve step: circle the current prime in PRIMARY, flash-cross-out multiples in RED
- Use AnimationGroup for batch crossing out (all multiples of 2 at once, etc.)
- After sieving with 2,3,5,7: remaining numbers glow PRIMARY
- This is the visual highlight of the video — make it beautiful

### Euclid's Proof (Scene 5)
- Use color coding: assumption in PRIMARY, construction in WHITE, contradiction in RED, conclusion in SECONDARY
- Show N = product + 1 as a visual equation, not just text
- Explicitly show the misconception: give example like 2*3*5*7*11*13 + 1 = 30031 = 59 * 509 (composite!)

### Distribution (Scenes 7-8)
- Bar chart using Manim BarChart or custom rectangles
- Color bars with gradient from PRIMARY to SECONDARY
- Overlay the n/ln(n) curve as a dotted line

### General
- Avoid cramming — each scene has at most 5 visible elements
- 1 is NOT prime — address this explicitly (common student confusion)
- Product+1 misconception — address this explicitly (per Numberphile analysis)

## Narration Timing
- Scene 1: ~60s (intro + 3 bullets)
- Scene 2: ~70s
- Scene 3: ~120s (sieve animation needs time)
- Scene 4: ~60s
- Scene 5: ~100s
- Scene 6: ~50s
- Scene 7: ~70s
- Scene 8: ~80s
- Scene 9: ~50s
- Total: ~660s ≈ 11 minutes (within 8-15 min target)
