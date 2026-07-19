# Video 126: Complex Numbers Revisited — Introduction to Complex Analysis

**Playlist:** Complex Analysis (Video 1 of 13)
**Class:** Video126_ComplexAnalysisIntro
**Script:** scripts/undergraduate/video-126-complex-analysis-intro.py
**Est. Duration:** 12 min
**Status:** PLAN → SCRIPT

## Competitive Analysis Summary

No prior competitive analysis found for this topic. Notable competitor coverage:
- **3Blue1Brown:** Chapter "Complex Numbers" (Essence of Linear Algebra series has visual complex plane, but no dedicated complex analysis playlist). His style uses geometric intuition, color-coded vectors.
- **Mathologer:** Has covered complex numbers (sqrt(-1), Euler's identity) with historical narrative and deep visual exploration.
- **Michael Penn:** Standard chalkboard-style proofs on complex analysis topics.
- **Dr. Peyam:** Full complex analysis lecture series, traditional approach.

**Techniques to adopt:**
- Visual representation of complex plane as the primary teaching tool (3B1B style)
- Geometric interpretation of operations (multiplication as rotation+scaling)
- Euler's formula as a visual "aha" moment with the unit circle
- Progressive build-up: real → imaginary → complex → polar → Euler

**Techniques to avoid:**
- Dense proof-heavy approach without visuals
- Jumping straight to formal definitions without motivation

## Scene Plan

### Scene 1: Hook — "What Lies Beyond the Real Line?" (~40s)
- Open with the real number line (visual: horizontal axis)
- Ask: "Where does the equation x^2 = -1 live?"
- Introduce the motivation: extending the real numbers
- Bridge from real analysis (Video 99-110) to complex analysis

### Scene 2: Complex Numbers — Definition and Notation (~50s)
- Define z = a + bi, where i^2 = -1
- Real part (Re(z)) and imaginary part (Im(z))
- Visual: point on the complex plane
- Examples: 3+2i, -1+4i, 5-3i

### Scene 3: The Complex Plane (~60s)
- Build the Argand diagram step by step
- Real axis (horizontal), imaginary axis (vertical)
- Plot several complex numbers as points
- Connect to vectors: each complex number IS a vector
- Reference to linear algebra (vectors from Videos 25-40)

### Scene 4: Complex Arithmetic — Geometric View (~60s)
- Addition: parallelogram law (vector addition)
- Multiplication: rotate + scale
- Visual examples with colored arrows
- Key insight: i acts as a 90-degree rotation

### Scene 5: Modulus and Argument — Polar Form (~60s)
- Define |z| = sqrt(a^2 + b^2) — distance from origin
- Define arg(z) — angle with real axis
- z = r(cos(theta) + i*sin(theta))
- Visual: polar coordinates on the complex plane

### Scene 6: Euler's Formula — The Crown Jewel (~70s)
- The unit circle parameterization
- Euler's formula: e^(i*theta) = cos(theta) + i*sin(theta)
- Visual: tracing the unit circle as theta varies
- Special case: e^(i*pi) + 1 = 0 (Euler's identity)
- Brief explanation connecting exp, trig, and complex numbers

### Scene 7: Operations in Polar Form (~50s)
- Multiplication: multiply moduli, add arguments
- Division: divide moduli, subtract arguments
- De Moivre's theorem: (cos(theta) + i*sin(theta))^n = cos(n*theta) + i*sin(n*theta)
- Visual demonstration

### Scene 8: Summary and Road Ahead (~40s)
- Key takeaways: complex plane, polar form, Euler's formula
- Teaser for next video: complex functions (Video 127)
- What makes complex analysis special: complex differentiability
- Outro

## Content Budget per Scene

| Scene | Elements on Screen | Notes |
|-------|-------------------|-------|
| 1 | Max 3 | Number line, question text, i symbol |
| 2 | Max 4 | Definition formula, Re/Im labels, examples |
| 3 | Max 5 | Axes, 3-4 plotted points, labels |
| 4 | Max 4 | Two vectors, result vector, formula |
| 5 | Max 4 | Polar grid/triangle, r/theta labels, formula |
| 6 | Max 4 | Unit circle, formula, Euler identity |
| 7 | Max 4 | Multiplication visual, De Moivre formula |
| 8 | Max 3 | Summary list, teaser text, channel outro |

## Color Coding
- PRIMARY (#5BC0EB): Complex plane axes, real part
- SECONDARY (#7BC950): Imaginary part, polar elements
- ACCENT (#FFD166): Key formulas, Euler's formula, highlights
- RED (#EF476F): Special values (Euler's identity)
