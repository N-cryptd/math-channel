# Video 261: Quadratic Residues

## Overview
11th video in Number Theory playlist. Introduces quadratic residues, the Legendre symbol, and Euler's criterion as the key computational tool.

## Scenes (target 10-13 min)

### Scene 1: Hook — Which Squares Appear? (25s)
- Squares mod 7: 1, 4, 2, 2, 4, 1 → only {1, 2, 4} are squares
- Squares mod 5: 1, 4, 4, 1 → only {1, 4}
- Half the nonzero residues are squares, half are not (for odd primes)

### Scene 2: Definition (2 min)
- a is a QR mod p if there exists x with x^2 = a (mod p)
- Otherwise a is a QNR (quadratic nonresidue)
- Examples mod 7: QRs are 1, 2, 4; QNRs are 3, 5, 6

### Scene 3: The Legendre Symbol (2 min)
- (a/p) = 1 if QR, -1 if QNR, 0 if p|a
- Multiplicative: (ab/p) = (a/p)(b/p)
- Examples with concrete numbers

### Scene 4: Euler's Criterion (2.5 min)
- (a/p) = a^((p-1)/2) mod p
- Proof: a^((p-1)/2) squared equals a^(p-1) = 1, so value is +-1
- It's +1 iff a is a QR
- Example: (2/7) = 2^3 = 8 = 1 mod 7 → QR (confirmed: 3^2=9=2)

### Scene 5: Properties and Examples (2 min)
- (1/p) = 1, (-1/p) = (-1)^((p-1)/2)
- (a^2/p) = 1 always
- Computing Legendre symbols via Euler's criterion

### Scene 6: Summary and Teaser (1.5 min)
- Key takeaways
- Teaser: quadratic reciprocity lets us flip (p/q) to (q/p)
- Next video: Quadratic Reciprocity

## Key Formulas
1. (a/p) = 1 if QR, -1 if QNR, 0 if p|a
2. (ab/p) = (a/p)(b/p)
3. (a/p) = a^((p-1)/2) (mod p) [Euler's criterion]
4. (-1/p) = (-1)^((p-1)/2)
