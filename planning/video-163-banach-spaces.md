# Video 163: Banach Spaces

**Playlist:** Functional Analysis (Video 2 of 12)
**Class:** Video163_BanachSpaces
**File:** scripts/graduate/video-163-banach-spaces.py
**Estimated duration:** ~560s (9 min)

## Topics
1. Hook: The rational numbers are not "complete" — sequences that should converge don't
2. Cauchy sequences: definition and intuition
3. Completeness: when every Cauchy sequence converges to a limit IN the space
4. Definition of a Banach space (complete normed space)
5. Examples: R, R^n, C[a,b] with sup-norm are Banach; Q is NOT Banach
6. Non-example: continuous functions with L1 norm are NOT complete
7. Why completeness matters: guarantees limits exist, enables functional analysis theorems
8. Preview of inner product spaces (next video)

## Prerequisites
- Video 162 (Normed Spaces) — complete
- Measure Theory Video 158 (L^p spaces)
- Real Analysis Videos 100-101 (Sequences, Cauchy sequences, Convergence)

## Competitive Analysis
Based on analysis of:
- Abide By Reason: "Weird spaces where π = 4" (286K views, Manim animated, June 2025) — HIGH RELEVANCE
- Frederic Schuller: "Banach Spaces - Lec02" (101K views, blackboard lecture, 2016)
- @brightsideofmaths: "Functional Analysis 6" (105K views, combined norm + Banach, tablet)

Key insights from competitors:
- Abide By Reason uses the "π = 4 in l∞" as a hook — VERY engaging. We should reference this intuition.
- Schuller is thorough but dry (blackboard, 1hr+ lecture)
- Most competitors cover normed spaces + Banach in one video; we separate them for depth.

Key differentiators: We build from Cauchy sequences in R (familiar) to abstract Banach spaces, use the Q gap example as motivation, show why completeness matters with the L1 counterexample.

## Scene Plan

### Scene 1: Hook — The Holes in Q (40s)
**Content budget:** Intro + title + 2 text items
- Play intro: "Banach Spaces", "Functional Analysis"
- "Consider the sequence: 3, 3.1, 3.14, 3.141, 3.1415, ... (approaching π)"
- "In Q, this sequence is Cauchy but has no limit — π is not rational!"
- "Banach spaces fix this: every Cauchy sequence converges IN the space"

### Scene 2: Cauchy Sequences (45s)
**Content budget:** Title + formula + 2 text items
- Formal definition: for all ε > 0, there exists N such that ||x_n - x_m|| < ε for all n,m ≥ N
- Intuition: the terms get arbitrarily close to each other
- Key point: in a complete space, Cauchy = convergent

### Scene 3: Definition of a Banach Space (50s)
**Content budget:** Title + definition box + 2 text items
- A Banach space is a COMPLETE normed vector space
- Completeness means: every Cauchy sequence converges to a limit IN the space
- Color-code: normed space definition (from video 162) + completeness condition

### Scene 4: Examples — Banach Spaces (50s)
**Content budget:** Title + 3 examples (progressive reveal)
- R with |x| is Banach (complete)
- R^n with ||.||_2 is Banach (complete)
- C[a,b] with sup-norm is Banach (uniform convergence)

### Scene 5: Non-Examples — NOT Banach (55s)
**Content budget:** Title + 2 non-examples
- Q with |x|: Cauchy sequence converging to √2 has no limit in Q
- C[0,1] with L1 norm: sequence of functions converges to a discontinuous function — not in C[0,1]
- Motivating: "completeness depends on the norm!"

### Scene 6: Why Completeness Matters (45s)
**Content budget:** Title + 3 items (progressive reveal)
- Theorems like Banach Fixed Point, Open Mapping, Closed Graph all require completeness
- Without completeness: limits can "escape" the space
- "Completeness is what makes analysis work!"

### Scene 7: Summary + Outro (40s)
**Content budget:** Summary items + outro
- Recap: Banach space = complete normed space
- Cauchy sequences are the key concept
- Not all normed spaces are Banach — depends on the norm
- Preview: Inner Product Spaces (Video 164)

## Visual Design Notes
- Use color coding: PRIMARY for Banach (complete), RED for non-Banach (not complete)
- Cauchy sequence visualization: animate dots converging on a number line
- For Q counterexample: show the "hole" at √2 on the rational number line
- Formula box for the completeness definition
- Two-column for examples vs non-examples
