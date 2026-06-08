# Video Plan: The Power Rule

## Overview
- **Topic**: The power rule for derivatives — computing derivatives without limits every time
- **Hook**: "Last time we found the derivative of x^2 using a long limit calculation. What if I told you there's a shortcut?"
- **Aha moment**: The power rule works for ALL real powers, not just integers — and connects to the binomial theorem
- **Target audience**: Students who watched Video 01 (know the limit definition of derivative)
- **Length**: ~12 minutes
- **Resolution**: 1080p 60fps (production), 480p 15fps (draft)

## Color Palette
- Background: #2D2B55
- Primary: #58C4DD — formulas, curves
- Secondary: #83C167 — pattern recognition, "look at this"
- Accent: #FFFF00 — the power rule formula, key results
- DIM: #888888 — scaffolding, old work being replaced

## Arc: Problem-Solution
1. Problem — the limit definition is tedious
2. Pattern recognition — derivatives of x, x^2, x^3
3. Conjecture — the power rule
4. Proof — binomial theorem justification
5. Generalization — negative, fractional powers
6. Result — the shortcut that works

## Scene 1: Recap + Motivation (~60s)
**Purpose**: Remind the viewer of last time, motivate a faster method
**Layout**: FULL_CENTER

### Visual elements
- Brief flashback: the 6-step limit computation from Video 01
- Text: "That was a lot of work for just x^2..."
- "What about x^5? x^100?"

### Animation sequence
1. Last video's result fades in: f'(x^2) = 2x (~2s)
2. Brief flash of the limit steps, quickly faded out (~3s)
3. "What if we need f'(x^5)?" — new problem (~2s)
4. "The limit would take forever..." — frustrated tone (~3s)
5. "There must be a pattern." — transition (~2s)

### Subtitle
"Last time we used the limit definition to find the derivative of x-squared. It took six steps. What about x to the fifth?"

---

## Scene 2: Hunting for the Pattern (~90s)
**Purpose**: Compute a few derivatives, let the viewer see the pattern emerge
**Layout**: LEFT_RIGHT (computations left, graphs right)

### Visual elements
- Three computation panels: x^1, x^2, x^3
- Corresponding tangent lines on three small graphs
- Results column accumulating

### Animation sequence
1. "Let's compute a few more using the definition" (~2s)
2. f(x) = x → f'(x) = 1 (quick, 2 steps) (~4s)
3. f(x) = x^2 → f'(x) = 2x (already done, recap) (~3s)
4. f(x) = x^3 → f'(x) = 3x^2 (full computation shown) (~12s)
5. Results column: 1x^0, 2x^1, 3x^2 (~3s)
6. Highlight the pattern: coefficient = old exponent, new exponent = old - 1 (~5s)
7. "The power comes down, and decreases by one" (~3s)

### Subtitle
"The derivative of x to the n is n times x to the n minus one. Let's verify this."

---

## Scene 3: The Power Rule — Statement (~60s) **AHA MOMENT**
**Purpose**: State the rule clearly with visual emphasis
**Layout**: FULL_CENTER, big formula

### Visual elements
- THE formula: d/dx[x^n] = nx^{n-1} (large, yellow accent)
- Geometric animation: the exponent n "falls down" as a coefficient, the original exponent decreases by 1
- Examples filling in below

### Animation sequence
1. Formula appears in yellow: d/dx[x^n] = nx^{n-1} (~3s)
2. Animation: the "n" drops down to become the coefficient, the old n becomes n-1 (~4s)
3. "This is the Power Rule" — label (~2s)
4. Quick examples: x^4 → 4x^3, x^7 → 7x^6, x^10 → 10x^9 (~6s)
5. Each result appears with a satisfying animation (~8s)
6. "No limits needed. Instant." (~2s)

### Subtitle
"The Power Rule: the derivative of x to the n equals n times x to the n minus one."

---

## Scene 4: Proof Using the Binomial Theorem (~120s)
**Purpose**: Prove the rule for positive integers — show where it comes from
**Layout**: PROGRESSIVE (top-down derivation)

### Visual elements
- Limit definition at top
- Binomial expansion in the middle (animated)
- Cancellation steps
- Final result highlighted

### Animation sequence
1. "But why does this work? Let's prove it for positive integers." (~3s)
2. Write the limit definition: lim_{h→0} [(x+h)^n - x^n] / h (~4s)
3. "We need to expand (x+h)^n — the binomial theorem!" (~3s)
4. Write binomial theorem (x+h)^n = x^n + nx^{n-1}h + ... + h^n (~5s)
5. "Substitute into the limit" (~2s)
6. Show the full fraction, x^n cancels with -x^n (~4s)
7. Factor out h from remaining terms (~3s)
8. "Now h cancels with the denominator" — highlight (~3s)
9. Set h = 0 → only the first term survives: nx^{n-1} (~4s)
10. "And that's it. The power rule." (~2s)
11. "Notice: every term except the first has an h, so they all vanish." (~3s)

### Subtitle
"Using the binomial theorem: when we expand (x plus h) to the n, only the first two terms survive the limit."

---

## Scene 5: Extending Beyond Integers (~90s)
**Purpose**: Show the rule works for negative and fractional powers too
**Layout**: SPLIT_TOP_BOTTOM (negative powers top, fractional bottom)

### Visual elements
- Negative power example: f(x) = 1/x = x^{-1}, show derivative is -x^{-2}
- Fractional power example: f(x) = √x = x^{1/2}, show derivative is (1/2)x^{-1/2}
- Graphs for both

### Animation sequence
1. "The power rule isn't just for positive integers" (~2s)
2. "What about 1/x? That's x to the negative one." (~3s)
3. Apply the rule: f'(x) = -1 · x^{-2} = -1/x^2 (~5s)
4. Small graph showing 1/x and its derivative (~5s)
5. "Or the square root — that's x to the one half" (~3s)
6. Apply the rule: f'(x) = (1/2) · x^{-1/2} = 1/(2√x) (~5s)
7. Small graph showing √x and its derivative (~5s)
8. "Works for any real power n." — text on screen (~3s)
9. "We'll prove the general case later with logarithmic differentiation." (~3s)

### Subtitle
"The power rule works for negative and fractional powers too — any real number n."

---

## Scene 6: Combining with Linearity (~60s)
**Purpose**: Show how the power rule combines with sum/difference rules
**Layout**: LEFT_RIGHT (rule left, example right)

### Visual elements
- Linearity rules: d/dx[cf] = cf', d/dx[f+g] = f' + g'
- Worked example: f(x) = 3x^4 - 5x^2 + 7x - 2
- Step-by-step differentiation

### Animation sequence
1. "The derivative also respects addition and scaling" (~3s)
2. Write linearity rules (~5s)
3. "This means we can differentiate polynomials term by term" (~3s)
4. Example: f(x) = 3x^4 - 5x^2 + 7x - 2 (~3s)
5. Apply power rule to each term step by step (~8s)
6. f'(x) = 12x^3 - 10x + 7 (~3s)
7. "Each term independently. Clean and mechanical." (~3s)

### Subtitle
"The derivative is linear: you can differentiate term by term. Polynomials become easy."

---

## Scene 7: Recap + Preview (~45s)
**Purpose**: Summarize and tease the product/quotient rules
**Layout**: PROGRESSIVE

### Visual elements
- Summary: power rule statement, domain, proof method
- "Next: What about x^x? We need the product and chain rules"
- Subscribe CTA

### Animation sequence
1. Bullet points appear:
   - "The power rule: d/dx[x^n] = nx^{n-1}"
   - "Proved for positive integers using the binomial theorem"
   - "Works for all real powers"
   - "Combine with linearity to differentiate any polynomial"
2. "Next time: when the power rule isn't enough — the product and chain rules" (~4s)
3. Outro (~3s)

### Subtitle
"The power rule is your first shortcut. But not everything is a simple power — next: the chain rule."
