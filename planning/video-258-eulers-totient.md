# Video 258: Euler's Totient Function

## Playlist: Number Theory (Videos 251-265)
## Duration Target: 10-15 minutes
## Prerequisites: Video 252 (Primes), Video 254 (Modular Arithmetic), Video 257 (Fermat's Little Theorem)

---

## Scene Plan

### Scene 1: Hook -- From Primes to Composites (45s)
- Fermat's Little Theorem: a^(p-1) = 1 (mod p) -- works only for primes
- Question: what about composite moduli like 15 or 12?
- Tease: Euler found the answer, and the key is a counting function

### Scene 2: Definition and First Examples (75s)
- phi(n) = number of integers 1 <= k <= n with gcd(k, n) = 1
- Visual: animate numbers 1..10, highlight coprimes (1,3,7,9), phi(10) = 4
- Second example: phi(12) = 4 (1,5,7,11)
- Note: phi(1) = 1 by convention

### Scene 3: Table of Values and Patterns (60s)
- Build table: n=1..12, phi(n) values
- Notice: phi(p) = p-1 for primes (7, 5, 11, 3, 2 all confirm)
- Notice: phi(2p) = phi(p) for odd prime p
- Notice: phi(8) = 4 = phi(4), phi(9) = 6

### Scene 4: Prime Powers (75s)
- For prime p: phi(p) = p - 1 (all numbers except p are coprime)
- For p^k: count total p^k numbers, subtract multiples of p (p, 2p, ..., p^k)
- Formula: phi(p^k) = p^k - p^(k-1) = p^(k-1)(p - 1)
- Example: phi(27) = 27 - 9 = 18, phi(16) = 16 - 8 = 8

### Scene 5: Multiplicative Property (90s)
- Key theorem: if gcd(m, n) = 1 then phi(mn) = phi(m) * phi(n)
- Intuition via Chinese Remainder Theorem (reference Video 256)
- Each coprime residue mod m pairs with each coprime residue mod n
- Example: phi(15) = phi(3)*phi(5) = 2*4 = 8. Verify: {1,2,4,7,8,11,13,14}

### Scene 6: The Product Formula (75s)
- If n = p1^a1 * p2^a2 * ... * pk^ak then:
- phi(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pk)
- Worked example: phi(60) = 60 * (1-1/2) * (1-1/3) * (1-1/5) = 60 * 1/2 * 2/3 * 4/5 = 16
- Second example: phi(72) = 72 * 1/2 * 2/3 = 24

### Scene 7: Euler's Theorem (60s)
- Theorem: if gcd(a, n) = 1 then a^phi(n) = 1 (mod n)
- This generalizes Fermat's Little Theorem!
- When n = p (prime): phi(p) = p-1, so a^(p-1) = 1 (mod p) -- Fermat!
- Example: 3^8 = 6561. 6561 mod 15 = 1. And phi(15) = 8. Confirmed!

### Scene 8: Summary and RSA Teaser (45s)
- phi(n) counts coprimes up to n
- Formula via prime factorization
- Euler's theorem generalizes Fermat's Little Theorem
- phi(n) is the key to RSA encryption -- next video

---
## Technical Notes
- Coprime counting animation: number line with highlighted elements
- Table: progressive reveal, 2-3 rows at a time to respect 5-item rule
- Product formula: step-by-step substitution animation
- Euler's theorem: formula box in ACCENT color
- Script: scripts/graduate/video-258-eulers-totient.py
- Class: Video258_EulersTotient
- Competitive analysis: Neso Academy (411K views), Khan Academy (206K views), Mu Prime Math (37K views) -- none cover multiplicative property or product formula
