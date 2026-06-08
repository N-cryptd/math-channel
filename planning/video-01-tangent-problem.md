# Video Plan: The Tangent Problem

## Overview
- **Topic**: What a derivative is — motivated by the tangent line problem
- **Hook**: "What does 'instantaneous speed' actually mean?"
- **Aha moment**: The tangent line is the limit of secant lines — the derivative is the slope of that tangent
- **Target audience**: Students who know basic algebra and functions (pre-calculus level)
- **Length**: ~12 minutes
- **Resolution**: 1080p 60fps (production), 480p 15fps (draft)

## Color Palette
- Background: #2D2B55
- Primary: #58C4DD — key concepts, the curve, the tangent line
- Secondary: #83C167 — supporting elements, secant lines
- Accent: #FFFF00 — the "aha" moment, the derivative formula
- Error/warning: #FF6B6B — incorrect approaches (briefly shown)

## Arc: Discovery

## Scene 1: The Hook — "What is Speed?" (~45s)
**Purpose**: Make the viewer feel the problem before defining it
**Layout**: FULL_CENTER

### Visual elements
- Text: "What does it mean to go 60 mph... at a single instant?"
- A car moving along a road (animated dot on a number line)
- Position vs time graph appears

### Animation sequence
1. Text fades in center — pose the question (~2s)
2. Number line appears, dot moves from left to right at varying speed (~8s)
3. Position-time graph builds up as the dot moves (~5s)
4. Pause — "How fast was it going at t = 3?" (~2s)

### Subtitle
"If you drive 60 miles in one hour, your average speed is 60 mph. But what about this exact moment?"

---

## Scene 2: Average Speed is Easy (~90s)
**Purpose**: Establish what we CAN compute — set up the contrast
**Layout**: LEFT_RIGHT (graph left, text right)

### Visual elements
- Position-time graph (reuse from Scene 1)
- Secant line connecting two points on the curve
- Formula: average speed = Δy / Δx
- Moving second point approaching the first

### Animation sequence
1. Graph slides to left side (~1s)
2. Two points highlighted on the curve — t=2 and t=5 (~2s)
3. Secant line drawn between them (~2s)
4. Formula appears on right: "Average speed = Δy / Δx" (~2s)
5. Calculate the slope — numeric values fill in (~3s)
6. "This is the slope of the secant line" — line highlighted (~2s)
7. "But what if the points get closer?" — second point slides toward first (~5s)
8. Secant lines drawn at intermediate positions, showing convergence (~5s)

### Subtitle
"Average speed over an interval is just rise over run — the slope of a secant line."

---

## Scene 3: The Problem Gets Harder (~60s)
**Purpose**: Show the limit of average speed — the viewer should feel the gap
**Layout**: FULL_CENTER with split panels

### Visual elements
- Same curve, two points very close together
- Zoomed-in view of the curve near the point
- Secant lines getting steeper/flatter
- Text: "As Δt → 0, what happens?"

### Animation sequence
1. Graph with two very close points (~2s)
2. Show Δt shrinking: 1.0, 0.1, 0.01, 0.001... (~4s)
3. Secant lines drawn at each interval, increasingly similar (~6s)
4. Zoom into the region near the point (~3s)
5. "They're converging to something..." (~2s)
6. Pause — "but Δt = 0 means dividing by zero" (~3s)

### Subtitle
"As the interval shrinks, the secant lines approach a limit — but we can't just set Δt to zero."

---

## Scene 4: The Key Insight — Tangent as Limit (~120s) **AHA MOMENT**
**Purpose**: Reveal that the tangent line IS the limit of secant lines
**Layout**: PROGRESSIVE (build up from center)

### Visual elements
- The original curve
- Ghost secant lines (opacity 0.3) converging
- THE tangent line appears — bright yellow (accent color)
- Limit formula: dy/dx = lim(Δt→0) Δy/Δx
- Zoom-in showing tangent "touching" the curve

### Animation sequence
1. Start with all the secant lines still visible (~2s)
2. Fade them to low opacity (0.3) — "they're all approaching this" (~3s)
3. TANGENT LINE appears in yellow — bold, thick (~3s)
4. Zoom in — tangent touches curve at exactly one point (~4s)
5. Formula appears: dy/dx = lim_{Δt→0} [f(t₀+Δt) - f(t₀)] / Δt (~4s)
6. Each part of the formula highlighted as it's explained (~6s)
7. "THIS is the derivative — the instantaneous rate of change" (~3s)
8. Back to the car analogy — "your speed at t=3 is the derivative of position at t=3" (~4s)

### Subtitle
"The tangent line is the limit of secant lines. Its slope is the derivative — your instantaneous speed."

---

## Scene 5: Notation (~60s)
**Purpose**: Introduce standard notation — Leibniz and Lagrange
**Layout**: GRID (two columns)

### Visual elements
- Left: Leibniz notation — dy/dx
- Right: Lagrange notation — f'(x)
- Both with geometric interpretation
- Prime notation for higher derivatives

### Animation sequence
1. "Mathematicians have two main ways to write this" (~2s)
2. Left column: dy/dx with Δy/Δx → dy/dx animation (~5s)
3. Right column: f'(x) "read f-prime of x" (~3s)
4. "They mean the same thing" — equals sign connects them (~3s)
5. Higher derivatives: f''(x), f'''(x), d²y/dx² (~5s)
6. "We'll use both depending on context" (~2s)

### Subtitle
"Leibniz: dy/dx. Lagrange: f'(x). Same idea — the slope of the tangent line."

---

## Scene 6: First Example — Computing a Derivative (~90s)
**Purpose**: Show the definition in action with f(x) = x²
**Layout**: LEFT_RIGHT (work left, graph right)

### Visual elements
- f(x) = x² curve on the right
- Step-by-step limit computation on the left
- Tangent line at x=1 appearing as the limit resolves

### Animation sequence
1. "Let's compute the derivative of f(x) = x²" (~2s)
2. Parabola drawn on right side (~2s)
3. Limit definition written out: lim_{h→0} [f(x+h) - f(x)] / h (~3s)
4. Substitute: lim_{h→0} [(x+h)² - x²] / h (~2s)
5. Expand: lim_{h→0} [x² + 2xh + h² - x²] / h (~3s)
6. Simplify: lim_{h→0} [2xh + h²] / h (~2s)
7. Factor: lim_{h→0} [h(2x + h)] / h (~2s)
8. Cancel h: lim_{h→0} (2x + h) = 2x (~3s)
9. "The derivative of x² is 2x" — highlight yellow (~3s)
10. On the graph: tangent line at x=1 has slope 2 (~3s)
11. Tangent line at x=3 has slope 6 (~3s)

### Subtitle
"Using the definition: the derivative of x-squared is 2x."

---

## Scene 7: What We Learned + Preview (~45s)
**Purpose**: Recap and tease the next video
**Layout**: PROGRESSIVE

### Visual elements
- Summary bullet points
- "Next video: Power Rule — computing derivatives without limits"
- Subscribe CTA

### Animation sequence
1. Bullet points appear one by one (~8s):
   - "The derivative = slope of the tangent line"
   - "It's the limit of secant line slopes"
   - "f'(x) = lim_{h→0} [f(x+h) - f(x)] / h"
2. "Next time: faster ways to compute derivatives" (~3s)
3. "Thanks for watching" (~2s)
4. Subscribe animation (~2s)

### Subtitle
"The derivative captures instantaneous change. Next: the power rule and more."

---

## Post-Production Notes
- Background music: Subtle ambient throughout, lower during formula reveals
- All text uses Menlo monospace font
- Scene transitions: FadeOut all mobjects, 0.3s pause
- Subtitles burned into video (self.add_subcaption)
- Outro: Channel logo + subscribe (reuse template)
