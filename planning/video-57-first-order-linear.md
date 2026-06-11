# Video 57: First-Order Linear Equations

## Overview
- **Playlist:** Ordinary Differential Equations
- **Duration target:** 10-12 minutes
- **Class name:** `Video57_FirstOrderLinear`
- **Script file:** `scripts/undergraduate/video-57-first-order-linear.py`

## Competitive Analysis Reference
No dedicated competitive analysis was run for this video. The plan draws on general
observations from ODE playlists by Trefor Bazett, 3Blue1Brown (DE chapter),
and Khan Academy. Key decisions:
- Frame the integrating factor as a "multiplication trick" rather than a
  mysterious formula (following Trefor Bazett's motivational approach)
- Start with dy/dx + P(x)y = Q(x) as the standard form and show WHY
  separation fails (contrast with Video 56)
- Derive the integrating factor step by step from first principles
- Two worked examples: simple (constant coefficient) → applied (mixing problem)
- Color-code: P(x) in PRIMARY, Q(x) in SECONDARY, mu in ACCENT

## Scene Plan

### Scene 1: Hook — When Separation Fails (~1.5 min)
**Content budget (max 5 items):** Title, recall separable form, example that isn't separable, standard form reveal
- Start with play_intro()
- "Last time we solved separable equations — dy/dx = g(x)h(y). Clean, elegant."
- "But what about dy/dx + 2y = 3? You can't separate the variables."
- Show: dy/dx + P(x)y = Q(x) — the standard form of a first-order linear ODE
- "There's a different trick for these: the integrating factor."

### Scene 2: What Does "Linear" Mean? (~1.5 min)
**Content budget:** Section divider, definition, linearity test, examples vs non-examples
- Section divider "1 — What Makes It Linear?"
- A first-order ODE is linear if it can be written as dy/dx + P(x)y = Q(x)
- Linearity means y and dy/dx appear to the first power only — no y^2, no sin(y), no y·dy/dx
- Linear examples: dy/dx + 3y = x, dy/dx + (1/x)y = e^x
- NOT linear: dy/dx + y^2 = 1 (y^2), dy/dx + sin(y) = 0 (sin(y))
- Contrast with separability: linear is about degree 1 in y; separable is about factoring

### Scene 3: Deriving the Integrating Factor (~2.5 min)
**Content budget:** Section divider, standard form, derivation steps, formula reveal
- Section divider "2 — The Integrating Factor"
- Start with dy/dx + P(x)y = Q(x)
- Goal: turn the left side into d/dx[something · y] via the product rule
- "The product rule says d/dx[mu · y] = mu · dy/dx + mu' · y"
- "For this to match our equation, we need mu' = mu · P(x)"
- This gives d(mu)/mu = P(x) dx → ln|mu| = integral P dx → mu = e^{integral P dx}
- Highlight: mu(x) = e^{integral P(x) dx} — the integrating factor
- Multiply both sides by mu: d/dx[mu · y] = mu · Q
- Integrate both sides: mu · y = integral mu · Q dx + C
- Final formula: y = (1/mu)(integral mu · Q dx + C)

### Scene 4: Example 1 — Constant Coefficient (~2 min)
**Content budget:** Section divider, equation, IF computation, solution steps, answer
- Section divider "3 — Example: Constant Coefficient"
- dy/dx + 2y = 6 (simple: P(x) = 2, Q(x) = 6)
- mu = e^{integral 2 dx} = e^{2x}
- Multiply: e^{2x} dy/dx + 2e^{2x}y = 6e^{2x}
- Left side is d/dx[e^{2x}y] = 6e^{2x}
- Integrate: e^{2x}y = 3e^{2x} + C
- y = 3 + Ce^{-2x}
- Physical interpretation: approaches the constant solution y = 3

### Scene 5: Example 2 — Mixing Problem (~2 min)
**Content budget:** Section divider, problem setup, equation, solution, interpretation
- Section divider "4 — Example: Mixing Problem"
- Tank with 100 L of water, 5 kg of salt dissolved
- Fresh water flows in at 2 L/min, mixture drains at 2 L/min
- dy/dt = rate in - rate out = 0 - (y/100)(2) = -y/50
- dy/dt + (1/50)y = 0 — this is actually separable AND linear!
- Solution: y(t) = 5e^{-t/50}
- "The salt halves roughly every 35 minutes — exponential decay"
- Note: this example is linear with Q(x) = 0, so it's also separable — tie back to Video 56

### Scene 6: Summary + Preview (~1.5 min)
**Content budget:** Summary items, formula recap, next video teaser, outro
- Standard form: dy/dx + P(x)y = Q(x)
- Integrating factor: mu = e^{integral P dx}
- Multiply both sides by mu, left side becomes d/dx[mu·y]
- Integrate, solve for y
- "This technique handles equations that separation can't. But what about higher-order linear equations? That's next."
- play_outro() — tease "Second-Order Linear Equations"

## Key Formulas
- dy/dx + P(x)y = Q(x) (standard form)
- Product rule: d/dx[mu·y] = mu·dy/dx + mu'·y
- Integrating factor: mu(x) = e^{integral P(x) dx}
- d/dx[mu·y] = mu·Q(x) (after multiplying by IF)
- y = (1/mu)(integral mu·Q dx + C) (general solution)
- Example 1: y = 3 + Ce^{-2x}
- Example 2: y(t) = 5e^{-t/50}

## Animation Notes
- Scene 3 derivation is the signature moment — animate the product rule alignment step by step
- Color-code consistently: P(x) in PRIMARY, Q(x) in SECONDARY, mu in ACCENT, y in WHITE
- Show the "aha" moment when mu · dy/dx + mu' · y matches mu(dy/dx + Py)
- For examples, use the same 4-step visual pattern as Video 56 for consistency
- The mixing problem could have a simple diagram (tank with arrows), but keep it minimal
- Transition from Video 56's separation method to this video's IF method should feel like a natural escalation
