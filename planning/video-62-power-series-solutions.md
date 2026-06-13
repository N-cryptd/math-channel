# Video 62: Power Series Solutions

## Overview
**Topic:** Solving ODEs using power series expansions
**Playlist:** Ordinary Differential Equations
**Est. duration:** 12-15 min
**Prerequisites:** Video 61 (Variation of Parameters), Videos 20-21 (Power Series / Taylor Series)

## Competitive Analysis Reference
From `channel-analysis/improvements.md` (2026-06-12):
- **No 3B1B video** on this topic — major competitive gap
- Dr. Trefor Bazett: Start with y'=y simplest example, review series basics (110K views)
- blackpenredpen: Pure computation, 38 min, 525K views — shows huge demand despite poor production
- Houston Math Prep: Systematic method, includes initial conditions (502K views)
- Steve Brunton: Frame as universal tool, can even handle nonlinear ODEs (49K views)
- **Key insight**: Animate INDEX SHIFTING clearly (where students struggle most)
- **Key insight**: Recover known solutions for validation (e^x from y'=y)
- **Adopt**: Universal tool framing, simplest example first, then Airy's equation

## Scene Plan

### Scene 1: Hook — When Other Methods Fail (60s)
**Content budget:**
- Title: "The Universal Method"
- Recall: we've learned separation, linear, undetermined coefficients, variation of parameters
- Problem: y'' - xy = 0 (Airy's equation) — none of our methods work (variable coefficient, non-constant coefficient)
- Solution: express y as an infinite series and find the coefficients
- Based on Steve Brunton's "universal tool" framing
**Narration:** ~50 words

### Scene 2: Power Series Review (60s)
**Content budget:**
- Section divider: "1 | Power Series Recap"
- General form: y = sum_{n=0}^{inf} a_n * x^n
- Key identities: e^x, sin(x), cos(x) as series (brief, from Videos 20-21)
- Differentiation rule: y' = sum_{n=1}^{inf} n*a_n * x^{n-1} = sum_{n=0}^{inf} (n+1)*a_{n+1} * x^n
- INDEX SHIFT is the key technique — animate the shift
- Concise (unlike Trefor's long review) — our audience already knows power series
**Narration:** ~60 words

### Scene 3: Example 1 — y' = y (90s)
**Content budget:**
- Section divider: "2 | Simplest Example: y' = y"
- Assume y = sum a_n x^n
- Substitute: y' = sum (n+1)*a_{n+1} * x^n = sum a_n * x^n
- Match coefficients: (n+1)*a_{n+1} = a_n for all n
- Recurrence: a_{n+1} = a_n / (n+1)
- a_0 = a_0 (free), a_1 = a_0/1 = a_0, a_2 = a_1/2 = a_0/2!, ...
- a_n = a_0 / n!
- Solution: y = a_0 * sum x^n/n! = a_0 * e^x (recover known result)
- "Aha moment": the series method gives us the exponential we already know
**Narration:** ~100 words

### Scene 4: Index Shifting Technique (60s)
**Content budget:**
- Section divider: "3 | The Art of Index Shifting"
- Show the general technique: sum_{n=0}^{inf} c_n * x^n vs sum_{n=k}^{inf} c_{n-k} * x^{n-k}
- The substitution n -> n+k shifts index and power simultaneously
- Common pattern: align all sums to have the SAME power of x
- Visual: show terms lining up like puzzle pieces
- This is the key skill for harder problems
**Narration:** ~60 words

### Scene 5: Example 2 — Airy's Equation y'' - xy = 0 (120s)
**Content budget:**
- Section divider: "4 | Airy's Equation: y'' - xy = 0"
- The equation from our hook — now we can solve it
- y = sum a_n x^n, y'' = sum n(n-1)*a_n * x^{n-2}
- xy = sum a_n * x^{n+1}
- Need to shift indices to match powers of x
- y'': shift index m = n-2, then n = m+2: sum (m+2)(m+1)*a_{m+2} * x^m
- xy: shift index m = n+1, then n = m-1: sum a_{m-1} * x^m
- Match: (m+2)(m+1)*a_{m+2} = a_{m-1}
- Recurrence: a_{n+2} = a_{n-1} / ((n+2)(n+1)) for n >= 1
- Separate into even/odd series
- a_0 and a_1 are free (two linearly independent solutions)
- Show first few terms of each series
- Mention: this CANNOT be expressed in terms of elementary functions
**Narration:** ~150 words

### Scene 6: Initial Conditions and Convergence (60s)
**Content budget:**
- Section divider: "5 | Initial Conditions"
- How initial conditions determine the free coefficients
- a_0 = y(0), a_1 = y'(0)
- For Airy's equation: y(0)=1, y'(0)=0 gives only the even series
- Convergence: power series solutions converge within their radius of convergence
- Connection to Taylor series: this IS Taylor's theorem applied to ODEs
**Narration:** ~60 words

### Scene 7: Summary + Outro (45s)
**Content budget:**
- Summary: power series solutions work when other methods fail
- Steps: assume series form, substitute, match coefficients, solve recurrence
- Key skill: index shifting
- Applications: Airy's equation (optics), Bessel's equation (cylindrical waves), Hermite (quantum mechanics)
- Outro: preview next video (Laplace Transforms)
**Narration:** ~50 words

## Key Formulas
1. y = sum_{n=0}^{inf} a_n * x^n
2. y' = sum_{n=0}^{inf} (n+1)*a_{n+1} * x^n (index-shifted)
3. y'' = sum_{n=0}^{inf} (n+2)(n+1)*a_{n+2} * x^n (index-shifted)
4. Recurrence relation from matching coefficients
5. Initial conditions: a_0 = y(0), a_1 = y'(0)

## Color Coding
- PRIMARY (#5BC0EB): power series terms, sums
- SECONDARY (#7BC950): derivatives, y', y''
- ACCENT (#FFD166): recurrence relations, key results
- RED (#EF476F): the ODE itself, the equation to solve
