# Video 260: Primitive Roots

## Overview
10th video in Number Theory playlist. Connects group theory (cyclic groups, generators) to number theory (orders of elements mod n).

## Scenes (target 10-13 min)

### Scene 1: Hook — Powers That Generate Everything (25s)
- Mod 7: powers of 3 give all nonzero residues
- Powers of 2 only give {1, 2, 4} — not everything
- Question: which a generates all of (Z/nZ)*?
- Content budget: intro + 2 examples

### Scene 2: Order of an Element (2 min)
- Definition: ord_n(a) = smallest k > 0 with a^k = 1 (mod n)
- ord_n(a) always divides phi(n) (Lagrange's theorem)
- Examples: ord_7(3) = 6, ord_7(2) = 3
- Content budget: definition box + 3 examples

### Scene 3: Primitive Root Definition (1.5 min)
- a is a primitive root mod n if ord_n(a) = phi(n)
- It generates the entire multiplicative group
- Examples: 3 is a primitive root mod 7 (phi(7)=6)
- 2 is NOT a primitive root mod 7
- Content budget: definition + 2 comparison examples

### Scene 4: Existence for Primes (2 min)
- Theorem: primitive roots exist for every prime p
- The multiplicative group (Z/pZ)* is cyclic
- Number of primitive roots = phi(phi(p)) = phi(p-1)
- Example: phi(6) = 2, and indeed 3 and 5 are primitive roots mod 7
- Content budget: theorem + formula + example

### Scene 5: When Do Primitive Roots Exist? (2 min)
- Primes: always
- p^k for odd prime p: always
- 2p^k: always
- 4: yes (primitive root = 3)
- 2^k for k >= 3: NEVER
- Content budget: 5 conditions listed progressively

### Scene 6: Finding Primitive Roots (2 min)
- To test if g is a primitive root mod p:
  - Factor phi(p) = p-1 = q1^a1 * q2^a2 * ...
  - Check g^((p-1)/qi) != 1 (mod p) for each prime factor qi
- If all checks pass, g is a primitive root
- Content budget: algorithm steps + example

### Scene 7: Applications and Summary (1.5 min)
- Discrete logarithm problem
- Diffie-Hellman key exchange
- Summary of when primitive roots exist
- Next: Quadratic Residues
- Content budget: 3 points + outro

## Key Formulas
1. ord_n(a) = min{k > 0 : a^k = 1 (mod n)}
2. ord_n(a) | phi(n)
3. # primitive roots mod p = phi(p-1)
4. Test: g^((p-1)/q_i) != 1 (mod p) for each prime q_i | (p-1)
