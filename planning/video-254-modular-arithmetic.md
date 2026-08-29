# Video 254: Modular Arithmetic

## Playlist: Number Theory (Videos 251-265)
## Duration Target: 10-15 minutes
## Prerequisites: Video 251 (Divisibility), Video 253 (FTA)

---

## Scene Plan

### Scene 1: Hook -- Clock Arithmetic (45s)
**Content budget:** title + 3 items
- What time is it 10 hours after 7 o'clock? Answer: 5 o'clock
- This is modular arithmetic mod 12
- Widely used in cryptography, CS, and daily life

### Scene 2: Formal Definition (60s)
- Section divider: "1. Congruence"
- a = b (mod n) iff n | (a - b)
- Equivalence relation: reflexive, symmetric, transitive
- Equivalence classes: Z/nZ = {0, 1, ..., n-1}

### Scene 3: Arithmetic Rules (75s)
- Section divider: "2. Arithmetic Mod n"
- Addition: (a + b) mod n = ((a mod n) + (b mod n)) mod n
- Multiplication: (a * b) mod n = ((a mod n) * (b mod n)) mod n
- Example computations

### Scene 4: Exponentiation and Fermat's Little Theorem (75s)
- Fast exponentiation: a^k mod n
- Fermat's Little Theorem: if p prime, a^p = a (mod p)
- Or: a^(p-1) = 1 (mod p) when p does not divide a

### Scene 5: Applications (60s)
- ISBN check digits
- Hash functions in CS
- Cryptography teaser (RSA needs this)

### Scene 6: Summary & Outro (45s)

---

## Technical Notes
- Clock visual in Scene 1: Circle with hour markers
- Modular arithmetic: show number line wrapping around
- Script file: scripts/graduate/video-254-modular-arithmetic.py
- Class name: Video254_ModularArithmetic
