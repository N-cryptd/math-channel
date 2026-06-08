# Video 03: Product and Quotient Rules
## Overview
- **Topic**: Derivatives of products and quotients
- **Hook**: "We can differentiate polynomials term by term. But what about x^2 * sin(x)?"
- **Aha moment**: The product rule is the "anti-simplify" — it creates MORE terms, and that's correct
- **Target audience**: Watched Videos 01-02
- **Length**: ~12 min

## Scenes
1. **Hook** — Why can't we just multiply first? The product of two functions isn't the product of derivatives (~60s)
2. **Visual intuition** — Area model: the product (a+h)(b+k) = ab + ak + hb + hk. The derivative is ak + hb, not (a+h)(b+k) (~90s)
3. **Product rule statement** — (fg)' = f'g + fg', with geometric area animation (~60s)
4. **Examples** — x^2 * e^x, x * sin(x) (~90s)
5. **Quotient rule** — (f/g)' = (f'g - fg') / g^2, derived from product rule + chain rule (~60s)
6. **Common mistakes** — why (fg)' ≠ f'g', the mnemonic "low d-high minus high d-low" (~45s)
7. **Recap + Preview** — "Next: the chain rule for compositions" (~45s)

---

# Video 04: The Chain Rule
## Overview
- **Topic**: The chain rule for composite functions
- **Hook**: "What's the derivative of sin(x^2)? It's not cos(x^2)..."
- **Aha moment**: The chain rule is just a rate multiplier — outer rate * inner rate, like a gear system
- **Target audience**: Watched Videos 01-03
- **Length**: ~12 min

## Scenes
1. **Hook** — The tower of functions: h(x) = sin(x^2) is really f(g(x)) where g(x)=x^2, f(u)=sin(u) (~60s)
2. **Gear metaphor** — Animated gears: turning the outer gear (sin) at a rate that depends on how fast the inner gear (x^2) turns (~90s)
3. **Chain rule statement** — h'(x) = f'(g(x)) * g'(x), with the gear animation (~60s)
4. **Examples** — sin(x^2), e^{3x}, (2x+1)^5, sqrt(x^2+1) (~120s)
5. **Chain rule with product rule** — Combined: x * sin(x^2) (~60s)
6. **Implicit differentiation preview** — Using chain rule to differentiate both sides of an equation (~60s)
7. **Recap + Preview** — "Next: implicit differentiation and related rates" (~45s)

---

# Video 05: Implicit Differentiation & Related Rates
## Overview
- **Topic**: Differentiating equations that aren't solved for y, and applying derivatives to rates of change
- **Hook**: "What's the slope of a circle? You can't solve y = sqrt(r^2 - x^2) every time..."
- **Aha moment**: Implicit differentiation lets you differentiate ANY equation — just apply chain rule to y terms
- **Target audience**: Watched Videos 01-04
- **Length**: ~12 min

## Scenes
1. **Hook** — The circle x^2 + y^2 = 25. What's dy/dx at (3,4)? (~60s)
2. **The technique** — Differentiate both sides, treat y as a function of x (chain rule!), solve for dy/dx (~90s)
3. **Circle example worked out** — Full step-by-step, verify the answer geometrically (~60s)
4. **Related rates** — The ladder problem: a 10ft ladder slides down a wall at 2 ft/s. How fast is the bottom moving? (~120s)
5. **Another rate problem** — Expanding ripples: stone dropped in a pond, how fast does the area grow? (~60s)
6. **Strategy** — General framework for related rate problems: draw picture, write equation, differentiate, plug in values (~45s)
7. **Recap + Preview** — "Next: the Mean Value Theorem and applications" (~45s)

---

# Video 06: Exponential and Logarithmic Derivatives
## Overview
- **Topic**: Derivatives of e^x, ln(x), a^x, log_a(x)
- **Hook**: "e^x is the only function that is its own derivative. Why?"
- **Aha moment**: The derivative of a^x involves a^x times ln(a) — and ln(a) is the 'correction factor' that makes e special
- **Target audience**: Watched Videos 01-04
- **Length**: ~12 min

## Scenes
1. **Hook** — What function equals its own derivative? (~60s)
2. **The number e** — Geometric definition: e is the base where the tangent to y=a^x at x=0 has slope 1 (~90s)
3. **Derivative of e^x** — Using the limit definition, show that (e^h - 1)/h → 1 as h → 0 (~60s)
4. **Derivative of a^x** — Rewrite a^x = e^{x ln a}, chain rule gives a^x * ln(a) (~60s)
5. **Derivative of ln(x)** — Inverse function theorem: if y=ln(x), then x=e^y, differentiate implicitly (~60s)
6. **Logarithmic differentiation** — Technique for tricky products: y = x^x (~90s)
7. **Recap** — "Next: trigonometric derivatives" (~45s)
