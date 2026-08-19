# Video 220: Algebraic Extensions — Advanced Abstract Algebra

## Overview
Building on Video 219's introduction to field extensions, this video goes deeper into algebraic extensions specifically. We prove that every finite extension is algebraic, characterize when finitely generated extensions are finite, show that the sum and product of algebraic elements remain algebraic, and introduce algebraic closures. This is the machinery needed for splitting fields and Galois theory.

## Competitive Analysis (2026-08-19)

Already completed — see channel-analysis/improvements.md section "[2026-08-19] Algebraic Extensions (Video 220)".

Key insights from analysis:
- Position as "the missing foundation" for popular Galois theory videos (Mathemaniac 549K, Aleph 0 314K)
- Animate the vector space perspective: every finite extension has a basis
- The tower law as climax with animated dimension-counting (already covered in Video 219, so we build on it)
- Adopt Mathemaniac's storytelling: each section raises a question the next answers
- Avoid Borcherds' 27-min proof-heavy density, Kinney's 52-min whiteboard

## Scenes (target: 12-15 min)

### Scene 1: Hook — Why Algebraic? (25s)
- **Content:** Quick recap: from Video 219, algebraic elements satisfy polynomials. Now: what if EVERY element of E/F is algebraic over F? That's an algebraic extension — the most important kind.
- **Budget:** play_intro + 2 text items
- **Narration:** ~30 words / 12s

### Scene 2: Definition and First Examples (40s)
- **Content:** E/F is algebraic if every alpha in E is algebraic over F. Every finite extension is algebraic (proof sketch: in a finite extension, powers of any element must be linearly dependent).
- **Budget:** section_divider + title + formula + 2 text items
- **Narration:** ~50 words / 20s

### Scene 3: Finite Implies Algebraic — Proof (50s)
- **Content:** Take E/F finite of degree n. For any alpha in E, the n+1 elements 1, alpha, alpha^2, ..., alpha^n must be linearly dependent. This gives a polynomial relation.
- **Budget:** title + MathTex for the dependency + 2 text items
- **Narration:** ~60 words / 24s

### Scene 4: Simple Extensions (45s)
- **Content:** K(alpha)/K is always a simple extension. If alpha is algebraic, K(alpha) is finite with degree = deg(m_alpha). If transcendental, K(alpha) is isomorphic to K(x), the rational function field.
- **Budget:** section_divider + title + formula + 2 text items
- **Narration:** ~50 words / 20s

### Scene 5: Finitely Generated Algebraic Extensions (50s)
- **Content:** If alpha_1, ..., alpha_n are algebraic over K, then K(alpha_1, ..., alpha_n) is a finite (hence algebraic) extension. Proof by iterating the tower law.
- **Budget:** section_divider + title + formula (tower) + 2 text items
- **Narration:** ~55 words / 22s

### Scene 6: Sum and Product of Algebraic Elements (60s)
- **Content:** If alpha and beta are algebraic over K, then alpha+beta, alpha*beta, and alpha^{-1} (if alpha != 0) are algebraic. Proof: K(alpha, beta) is finite over K, and all these elements live in it.
- **Budget:** section_divider + title + formula + 2 text items
- **Narration:** ~65 words / 26s

### Scene 7: The Field of Algebraic Numbers (45s)
- **Content:** The set of all algebraic numbers Q-bar = {alpha in C : alpha algebraic over Q} forms a field. It's a countable subfield of C containing all roots of all polynomials.
- **Budget:** title + formula + 2 text items
- **Narration:** ~50 words / 20s

### Scene 8: Algebraic Closure (50s)
- **Content:** A field K is algebraically closed if every non-constant polynomial in K[x] has a root in K. Equivalently, the only irreducible polynomials are linear. The algebraic closure of K is the smallest algebraically closed field containing K.
- **Budget:** section_divider + title + formula + 2 text items
- **Narration:** ~55 words / 22s

### Scene 9: Examples of Closures (40s)
- **Content:** C is algebraically closed (Fundamental Theorem of Algebra). Q-bar is the algebraic closure of Q (but not Q itself — x^2-2 has no root in Q). R is not algebraically closed (x^2+1 has no root).
- **Budget:** title + 3 text items (progressive reveal replaces)
- **Narration:** ~45 words / 18s

### Scene 10: Summary + Outro (30s)
- **Content:** Key takeaways. Tease: splitting fields (next video).
- **Budget:** section_divider + title + 3 text items + play_outro
- **Narration:** ~50 words / 20s

## Key Formulas
- E/F algebraic: every alpha in E is algebraic over F
- Finite => algebraic (n+1 elements 1, alpha, ..., alpha^n are LD)
- [K(alpha):K] = deg(m_alpha) if alpha algebraic
- K(alpha_1,...,alpha_n)/K finite if all alpha_i algebraic (tower law iteration)
- alpha+beta, alpha*beta algebraic if alpha, beta algebraic
- Q-bar = algebraic closure of Q (countable!)
- K algebraically closed: every f in K[x] splits completely
