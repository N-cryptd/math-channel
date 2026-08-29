# Video 253: The Fundamental Theorem of Arithmetic

## Playlist: Number Theory (Videos 251–265)
## Duration Target: 10–15 minutes
## Prerequisites: Video 251 (Divisibility), Video 252 (Primes)

---

## Scene Plan

### Scene 1: Hook — Unique Fingerprint (45s)
**Content budget:** title + 3 items
- Every integer has a unique prime factorization
- 12 = 2^2 * 3, no other way
- This is so natural we assume it, but it requires proof

### Scene 2: Statement of the Theorem (60s)
**Content budget:** title + formula + 2 items
- Section divider: "1. The Theorem"
- Theorem: Every integer n > 1 can be written uniquely as p1^a1 * p2^a2 * ... * pk^ak
- Where p1 < p2 < ... < pk are primes and ai >= 1
- Text: "Existence + Uniqueness — we prove both"

### Scene 3: Existence — Why Factorization Always Works (75s)
**Content budget:** title + 3 items
- Section divider: "2. Existence"
- If n is prime, done
- If n is composite, n = ab where 1 < a, b < n
- Apply to a and b by induction (strong induction on n)
- Must terminate because factors are strictly smaller

### Scene 4: Uniqueness — The Hard Part (90s)
**Content budget:** title + 3 items
- Section divider: "3. Uniqueness"
- Key tool: Euclid's Lemma (p | ab => p | a or p | b)
- If n = p1*...*pk = q1*...*qm, then p1 divides some qj
- Since qj is prime, p1 = qj. Cancel and induct.

### Scene 5: Examples and Applications (60s)
**Content budget:** title + 4 items
- Section divider: "4. Using the FTA"
- GCD via prime factorization
- LCM via prime factorization
- gcd(a,b) * lcm(a,b) = a * b

### Scene 6: Summary & Outro (45s)
- Four takeaways + play_outro

---

## Technical Notes
- Uniqueness proof: use color to show p1 = qj matching
- GCD/LCM: MathTex with side-by-side comparison
- Script file: scripts/graduate/video-253-fundamental-theorem-arithmetic.py
- Class name: Video253_FundamentalTheoremArithmetic
