# Video 251: Divisibility and the Euclidean Algorithm

**Playlist:** Number Theory (Videos 251–265)
**Target duration:** 10–12 minutes
**Class:** Video251_DivisibilityEuclidean
**File:** scripts/graduate/video-251-divisibility-euclidean.py

## Competitive Analysis Reference

- Aleph 0 has episodic number theory (twin primes, 181K views) — no systematic curriculum
- Mathologer does deep dives on specific results (not a full NT course)
- No animated, systematic Number Theory playlist exists on YouTube
- Our differentiator: structured curriculum from foundations up
- Per the Aug 2026 analysis sweep: strong demand signal, perfect post-Abstract-Algebra fit

## Content Outline (8 Scenes)

### Scene 1 — Hook (0:00–1:30)
**Goal:** Motivate divisibility as the bedrock of number theory
- Intro animation
- Every integer secretly encodes its divisors
- Cryptography, prime factorization, Diophantine equations all rest on divisibility
- Content budget: intro animation + 3 bullet points

### Scene 2 — Divisibility Definition (1:30–3:00)
**Goal:** Formal definition with intuitive examples
- Section divider: "1 — Divisibility"
- Definition: a | b iff exists integer k with b = a*k
- Notation: a divides b, a is a divisor/factor of b
- Examples: 3 | 12 (k=4), 5 does not divide 12
- Key properties: reflexive, transitive, antisymmetric-like (a|b and b|a implies a=±b)
- Content budget: definition formula box → 3 examples → 3 properties (progressive reveal, cull)

### Scene 3 — Division Algorithm (3:00–5:00)
**Goal:** The fundamental theorem connecting divisibility to remainders
- Section divider: "2 — Division Algorithm"
- Statement: for a>0, b integers, exists unique q,r with b = aq + r, 0 <= r < a
- Geometric intuition: number line with multiples of a, b falls between two
- Visual: number line showing multiples of a, b landing in an interval
- Uniqueness argument sketch
- Content budget: theorem box → number line visual → uniqueness note

### Scene 4 — GCD Definition (5:00–6:30)
**Goal:** Define greatest common divisor
- Section divider: "3 — Greatest Common Divisor"
- Definition: gcd(a,b) = largest d such that d|a and d|b
- Notation: gcd(a,b) or (a,b)
- Examples: gcd(12, 18) = 6, gcd(35, 14) = 7, gcd(8, 15) = 1 (coprime)
- Basic property: gcd(a, 0) = |a|
- Content budget: definition → 3 examples → coprime note

### Scene 5 — Euclidean Algorithm (6:30–8:30)
**Goal:** Walk through the algorithm with a concrete example
- Section divider: "4 — The Euclidean Algorithm"
- Key insight: gcd(a, b) = gcd(b, r) where r = a mod b
- Worked example: gcd(252, 105)
  - 252 = 2*105 + 42
  - 105 = 2*42 + 21
  - 42 = 2*21 + 0
  - Therefore gcd(252, 105) = 21
- Show the chain of equalities visually
- Efficiency note: terminates because remainders strictly decrease
- Content budget: key property → step-by-step example (progressive, 5 items max)

### Scene 6 — Why It Works (8:30–9:30)
**Goal:** Sketch correctness of the Euclidean algorithm
- Theorem: gcd(a, b) = gcd(b, a - bq) for any integer q
- Proof sketch: if d|a and d|b, then d|a - bq. Converse also holds.\n- Therefore gcd(a, b) = gcd(b, r) where r is the remainder
- The chain of gcds shrinks until remainder is 0
- Content budget: theorem → proof sketch → conclusion

### Scene 7 — Bezout's Identity (9:30–11:30)
**Goal:** State and illustrate Bezout's identity
- Section divider: "5 — Bezout's Identity"
- Statement: for integers a, b (not both zero), exists x, y with ax + by = gcd(a,b)
- Worked example: back-substitute gcd(252, 105) = 21
  - 21 = 105 - 2*42
  - 42 = 252 - 2*105
  - So 21 = 105 - 2*(252 - 2*105) = 5*105 - 2*252
  - Therefore x = -2, y = 5
- Corollary: a and b are coprime iff exists x, y with ax + by = 1
- Content budget: theorem box → back-substitution steps → corollary

### Scene 8 — Summary (11:30–12:30)
**Goal:** Recap key concepts
- Section divider: "Summary"
- 5 key takeaways (progressive reveal)
- Outro with next video: "Prime Numbers"

## Visual Design Notes
- Use number line visualization for Division Algorithm (Create animation for axis, FadeIn for points)
- Euclidean algorithm: show each step as a MathTex chain, progressive reveal
- Bezout back-substitution: color-code the substitution steps (PRIMARY for original, ACCENT for result)
- Avoid cramming — each scene has at most 5 visible elements
- Divisibility symbol | rendered in MathTex with proper spacing

## Narration Timing
- Scene 1: ~90s (22 words intro + 35 words bullets)
- Scene 2: ~90s
- Scene 3: ~120s
- Scene 4: ~90s
- Scene 5: ~120s
- Scene 6: ~60s
- Scene 7: ~120s
- Scene 8: ~60s
- Total: ~750s ≈ 12.5 minutes (within 8–15 min target)
