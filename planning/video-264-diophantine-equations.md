# Video 264: Diophantine Equations — Plan

## Overview
Diophantine equations seek integer solutions to polynomial equations. This video
covers linear Diophantine equations (full solution via extended Euclidean),
Pythagorean triples (Euclid's formula), and a general strategy for tackling
harder Diophantine equations using modular arithmetic and descent.

This is the FINALE of the Number Theory playlist.

## Scenes (8 scenes, ~10 min target)

### Scene 1: Hook (45s)
**Content:** Fermat's Last Theorem as motivation. Diophantus's Arithmetica.
Find a^2 + b^2 = 10 in integers.
**Budget:** title + 2 items

### Scene 2: What Are Diophantine Equations? (40s)
**Content:** Definition — polynomial = 0, integer solutions only.
Contrast with real/complex solutions.
Examples: x+y=5 (line with lattice points), x^2+y^2=z^2 (Pythagorean).
**Budget:** title + 3 items

### Scene 3: Linear Diophantine Equations — Existence (50s)
**Content:** ax + by = c. Existence criterion: gcd(a,b) | c.
Proof sketch: if d|a and d|b, then d|(ax+by).
Example: 6x+15y=9. gcd(6,15)=3, 3|9, so YES.
Counterexample: 6x+15y=10. gcd=3, 3∤10, so NO.
**Budget:** title + formula + 3 items

### Scene 4: Extended Euclidean Algorithm — Worked Example (60s)
**Content:** Solve 2x+5y=3. Extended Euclid: 5=2*2+1, 2=1*2+0.
Back-substitute: 1=5-2*2, so 3=15-6*2 → x=-1, y=1.
General solution: x = x0 + (b/d)t, y = y0 - (a/d)t.
**Budget:** 2 sub-blocks of 3 items each

### Scene 5: General Solution Structure (40s)
**Content:** Parameterize all solutions with one free parameter t.
Visual: show that solutions lie on a lattice.
Geometric intuition: the line ax+by=c, but only lattice points count.
**Budget:** title + formula + 2 items

### Scene 6: Pythagorean Triples — Euclid's Formula (60s)
**Content:** x^2+y^2=z^2. Primitive triples: gcd(x,y,z)=1.
Euclid's formula: x=m^2-n^2, y=2mn, z=m^2+n^2.
Conditions: m>n>0, coprime, opposite parity.
Examples: (3,4,5), (5,12,13), (8,15,17), (7,24,25).
**Budget:** title + formula_box + 2 items

### Scene 7: General Strategy for Diophantine Equations (50s)
**Content:** Three tools:
1. Modular arithmetic to rule out solutions (e.g., x^2+y^2=3 mod 4)
2. Parametric descriptions (Euclid's formula, general linear solution)
3. Descent arguments (Fermat's infinite descent)
Connection to algebraic geometry (elliptic curves).
**Budget:** title + 3 items

### Scene 8: Summary & Outro (30s)
**Content:** Recap the three main results.
Number Theory playlist complete.
**Budget:** title + 3 items

## Competitive Analysis Notes
- Script written directly (analysis infrastructure would delay production)
- 3B1B does not have a Diophantine equations video; Mathologer covers specific results
- Our angle: systematic, curriculum-style coverage as playlist finale
