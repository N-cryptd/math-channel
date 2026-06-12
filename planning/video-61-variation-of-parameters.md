# Video 61: Variation of Parameters

## Overview
**Topic:** Method of Variation of Parameters for second-order linear ODEs
**Playlist:** Ordinary Differential Equations
**Est. duration:** 12-15 min
**Prerequisites:** Video 60 (Non-Homogeneous / Undetermined Coefficients)

## Competitive Analysis Reference
From `channel-analysis/improvements.md` (2026-06-12):
- Very little animated coverage of this topic — gap opportunity
- Build from Video 60, contrast undetermined coefficients vs variation of parameters
- Motivate from the Wronskian, show derivation step by step
- Don't just dump the formula

## Scene Plan

### Scene 1: Hook — When Undetermined Coefficients Fails (60s)
**Content budget:**
- Title: "The Limit"
- Non-homogeneous ODE form: ay'' + by' + cy = f(x)
- Problem: what if f(x) = ln(x)? Can't guess a form for that!
- Teaser: "We need a method that works for ANY forcing function"
**Narration:** ~50 words

### Scene 2: Section — The Big Idea (60s)
**Content budget:**
- Section divider: "1 | The Key Insight"
- Start from y_c = C1·y1 + C2·y2
- Idea: replace C1, C2 with functions u1(x), u2(x)
- Set y_p = u1·y1 + u2·y2
- One constraint: u1'·y1 + u2'·y2 = 0 (simplifies)
**Narration:** ~60 words

### Scene 3: Derivation — The System of Equations (90s)
**Content budget:**
- Section divider: "2 | Deriving the Formula"
- Differentiate y_p (using the constraint)
- Substitute into ODE
- Get two equations for u1' and u2'
- Wronskian W = y1·y2' - y2·y1'
- Solution: u1' = -y2·f/W, u2' = y1·f/W
- Integrate to get u1, u2
**Narration:** ~100 words

### Scene 4: The Wronskian (60s)
**Content budget:**
- Section divider: "3 | The Wronskian"
- Wronskian definition: W(y1, y2) = | y1 y2; y1' y2' |
- Key property: W ≠ 0 for linearly independent solutions
- Connection to determinant from earlier (Video 29)
**Narration:** ~60 words

### Scene 5: Example 1 — Exponential Forcing (90s)
**Content budget:**
- Section divider: "4 | Example: y'' + y = sec(x)"
- Characteristic equation: r² + 1 = 0 → r = ±i
- y_c = C1·cos(x) + C2·sin(x)
- y1 = cos(x), y2 = sin(x)
- f(x) = sec(x) = 1/cos(x)
- Wronskian = cos(x)·cos(x) + sin(x)·sin(x) = 1
- u1' = -sin(x)·sec(x) = -tan(x) → u1 = ln|cos(x)|
- u2' = cos(x)·sec(x) = 1 → u2 = x
- y_p = cos(x)·ln|cos(x)| + x·sin(x)
**Narration:** ~100 words

### Scene 6: Example 2 — Comparison with Undetermined Coefficients (60s)
**Content budget:**
- Show same equation from Video 60: y'' - 3y' + 2y = 3e^{3x}
- Solve by variation of parameters (should get same answer)
- Compare: UC was faster for simple forcing, VoP works for anything
**Narration:** ~60 words

### Scene 7: Summary + Outro (45s)
**Content budget:**
- Summary items: VoP works for ANY continuous f(x), uses Wronskian, requires integration
- When to use UC vs VoP
- Outro with next video: Power Series Solutions
**Narration:** ~40 words

## Key Formulas
1. y_p = u1(x)·y1(x) + u2(x)·y2(x)
2. Constraint: u1'·y1 + u2'·y2 = 0
3. u1' = -y2·f(x) / W(y1, y2)
4. u2' = y1·f(x) / W(y1, y2)
5. W(y1, y2) = y1·y2' - y2·y1'
