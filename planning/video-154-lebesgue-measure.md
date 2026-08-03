# Video 154: Lebesgue Measure — Plan

**Playlist:** Measure Theory  
**Prerequisites:** Videos 151 (Measure Theory Intro), 152 (Sigma-Algebras), 153 (Measures)  
**Estimated duration:** 10-12 minutes  
**Key formulas:** Lebesgue outer measure m*(A), interval cover definition, translation invariance, m*(Q ∩ [0,1]) = 0

## Competitive Analysis Reference
See `channel-analysis/improvements.md` entry [2026-08-03]. Key insights:
- Abide By Reason (652K views) starts with Dirichlet function failure — adopt this hook
- vcubingx (386K views) uses horizontal-slicing visual — our video is about the MEASURE not the integral, but we reference this visual
- We are the ONLY channel with a full animated measure theory series — structural advantage

## Scene Breakdown

### Scene 1: Hook — "Where Riemann Breaks" (~60s)
**Content budget:** Title + 3 items
- Motivation: The Dirichlet function (1 on rationals, 0 on irrationals) is NOT Riemann integrable
- Show vertical rectangles failing to converge (upper sums = 1, lower sums = 0)
- "We need a way to measure sets that doesn't depend on the order of approach"
- [Based on Abide By Reason's approach]

### Scene 2: Section Divider — "Lebesgue Outer Measure" (~5s)
### Scene 3: The Outer Measure Definition (~90s)
**Content budget:** Title + 3-4 items (formulas)
- For any A ⊆ R, define: m*(A) = inf { Σ |I_n| : A ⊆ ∪ I_n, each I_n an open interval }
- "We cover A with countably many intervals and take the smallest total length"
- Example: m*([0,1]) = 1 (trivially)
- Visual: intervals covering a set on the number line

### Scene 4: Translation Invariance (~60s)
**Content budget:** Title + 2-3 items
- m*(A + x) = m*(A) for any x ∈ R
- "Shifting a set doesn't change its measure"
- This is what makes Lebesgue measure "geometrically natural"

### Scene 5: The Rationals Have Measure Zero (~90s)
**Content budget:** Title + 3-4 items
- Key result: m*(Q ∩ [0,1]) = 0
- Proof sketch: enumerate rationals as q_1, q_2, ...; cover q_i by interval of length ε/2^i
- Total length = Σ ε/2^i = ε, which can be made arbitrarily small
- Visual: shrinking intervals around rational points on [0,1]
- "Almost all of [0,1] is irrational — in a precise measure-theoretic sense"

### Scene 6: Section Divider — "Caratheodory's Criterion"
### Scene 7: Measurable Sets (~90s)
**Content budget:** Title + 3 items (formulas)
- A set E is Lebesgue measurable iff: m*(A) = m*(A ∩ E) + m*(A \ E) for all A ⊆ R
- This IS the Caratheodory condition from Video 153!
- The Lebesgue sigma-algebra L = { E ⊆ R : E is Lebesgue measurable }

### Scene 8: Key Properties (~60s)
**Content budget:** Title + 3 items
- L contains all open sets, hence all Borel sets
- Every subset of a null set is measurable (and has measure 0)
- L is translation-invariant
- [a,b] has measure b-a (Lebesgue measure agrees with length!)

### Scene 9: Summary & Outro (~30s)
**Content budget:** Recap + outro card
- Lebesgue outer measure: covers with intervals
- Lebesgue measurable: Caratheodory condition
- The rationals are "small" (measure zero) but dense
- Preview: Lebesgue integral (next video)
