# Video 257: Fermat's Little Theorem

## Playlist: Number Theory (Videos 251-265)
## Duration Target: 10-15 minutes
## Prerequisites: Video 254 (Modular Arithmetic), Video 256 (Chinese Remainder Theorem)

---

## Scene Plan

### Scene 1: Hook -- Powers Modulo p (50s)
- Opening question: what is 2^100 mod 7? Naively impossible to compute.
- Show pattern: 2^1=2, 2^2=4, 2^3=1, 2^4=2, 2^5=4, 2^6=1 mod 7
- Period is 6 = 7-1. Coincidence? No -- Fermat's Little Theorem.

### Scene 2: Statement of the Theorem (70s)
- Section divider: "1. The Theorem"
- Two equivalent forms:
  - a^(p-1) = 1 (mod p) when gcd(a,p) = 1
  - a^p = a (mod p) for all integers a
- Concrete examples: 3^6 = 1 (mod 7), 5^10 = 1 (mod 11)

### Scene 3: Proof via Group Theory / Lagrange (120s)
- Section divider: "2. The Proof (Group Theory)"
- The multiplicative group (Z/pZ)^* has order p-1
- By Lagrange's theorem, the order of any element divides p-1
- So a^(p-1) = 1 (mod p)
- Alternative direct proof: the map x -> ax is a permutation of {1,...,p-1}
- Therefore product(ax) = product(x) for x in {1,...,p-1}
- So a^(p-1) * (p-1)! = (p-1)! (mod p), hence a^(p-1) = 1 (mod p)

### Scene 4: Wilson's Theorem (90s)
- Section divider: "3. Wilson's Theorem"
- Statement: (p-1)! = -1 (mod p) if and only if p is prime
- Show: from FLT proof, (p-1)! is its own inverse mod p
- The only self-inverse elements in (Z/pZ)^* are 1 and -1
- Since p > 2, (p-1)! = -1 (mod p)
- Example: 6! = 720 = 7*102 + 6 = -1 (mod 7)

### Scene 5: Applications (90s)
- Section divider: "4. Applications"
- Computing large powers mod p: 2^100 mod 7 = 2^(96+4) = (2^6)^16 * 2^4 = 1^16 * 16 = 2 (mod 7)
- Modular inverse: a^(-1) = a^(p-2) (mod p)
- Primality testing (Fermat test): if a^(p-1) != 1 (mod p), p is composite
- Foundation of RSA and modern cryptography

### Scene 6: Summary & Outro (50s)
- Section divider: "5. Key Takeaways"
- a^(p-1) = 1 (mod p) when gcd(a,p) = 1
- Proof via Lagrange's theorem or direct permutation argument
- Wilson's theorem: (p-1)! = -1 (mod p)
- Applications: fast modular exponentiation, inverses, primality testing

---
## Technical Notes
- Script file: scripts/graduate/video-257-fermats-little-theorem.py
- Class name: Video257_FermatsLittleTheorem
- Uses v2 templates (LayoutEngine, channel_branding)
- 6 scenes total, targeting ~8-10 min rendered