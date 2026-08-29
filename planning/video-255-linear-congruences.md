# Video 255: Linear Congruences

## Playlist: Number Theory (Videos 251-265)
## Duration Target: 10-15 minutes
## Prerequisites: Video 251 (Euclidean Algorithm), Video 254 (Modular Arithmetic)

---

## Scene Plan

### Scene 1: Hook -- Solving Equations Mod n (45s)
**Content budget:** title + 3 items
- What is x if 3x = 7 (mod 11)?
- We need the modular inverse of 3
- The Euclidean algorithm finds it

### Scene 2: Definition and Existence (75s)
- Section divider: "1. Linear Congruences"
- ax = b (mod n)
- Solvable iff gcd(a, n) | b
- If gcd(a, n) = 1: unique solution x = a^(-1) * b (mod n)
- If gcd(a, n) = d > 1 and d | b: d solutions

### Scene 3: Finding Modular Inverses (75s)
- Section divider: "2. Modular Inverse"
- Extended Euclidean algorithm: find x, y such that ax + ny = gcd(a,n)
- If gcd(a,n) = 1, then x is the inverse of a (mod n)
- Example: inverse of 3 (mod 11) = 4 (since 3*4 = 12 = 1 mod 11)

### Scene 4: Systems and Motivation for CRT (60s)
- Section divider: "3. Systems of Congruences"
- Example: solve x = 2 (mod 3) and x = 3 (mod 5)
- Brute force: check numbers = 2 mod 3: 2, 5, 8, 11, 14, 17, 20, 23...
- 8 = 3 (mod 5)? No. 8 = 3 (mod 5)? Yes!
- This is tedious. We need a systematic method.
- Teaser: Chinese Remainder Theorem (next video)

### Scene 5: Summary & Outro (45s)
- Key takeaways + play_outro

---
## Technical Notes
- Script file: scripts/graduate/video-255-linear-congruences.py
- Class name: Video255_LinearCongruences
